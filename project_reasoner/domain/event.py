import uuid
from dataclasses import dataclass
from typing import Callable, List

from rdflib import URIRef, Graph, Literal, RDF

from project_reasoner.ref import ref


@dataclass(frozen=True)
class DomainEvent:
    id: URIRef
    description: str


def domain_event_ref(domain_event_id: str) -> URIRef:
    return ref("domain_event/{0}", domain_event_id)


def create_domain_event_from_description(description: str) -> DomainEvent:
    return DomainEvent(
        id=domain_event_ref(str(uuid.uuid4())),
        description=description,
    )


def find_all_domain_events() -> Callable[[Graph], List[DomainEvent]]:
    def query(graph: Graph) -> List[DomainEvent]:
        results = graph.query(
            f"""
            SELECT ?event ?description WHERE {{
                ?event a <{ref("types/domain_event")}> .
                ?event <{ref("types/domain_event/description")}> ?description .
            }}
            """
        )

        domain_events = []
        for result in results:
            domain_events.append(
                DomainEvent(id=result.event, description=str(result.description))
            )

        return domain_events

    return query


def add_domain_event_command(domain_event: DomainEvent) -> Callable[[Graph], None]:
    def command(g: Graph):
        g.add((domain_event.id, RDF.type, ref("types/domain_event")))
        g.add(
            (
                domain_event.id,
                ref("types/domain_event/description"),
                Literal(domain_event.description),
            )
        )

    return command


def remove_domain_event_command(domain_event_id: URIRef) -> Callable[[Graph], None]:
    def command(g: Graph):
        g.remove((domain_event_id, None, None))

    return command
