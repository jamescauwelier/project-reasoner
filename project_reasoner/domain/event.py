from dataclasses import dataclass

from rdflib import URIRef

from project_reasoner.ref import ref


@dataclass(frozen=True)
class DomainEvent:
    id: URIRef
    description: str


def domain_event_ref(domain_event_id: str) -> URIRef:
    return ref("domain_event/{0}", domain_event_id)
