from dataclasses import dataclass
from uuid import uuid4, UUID

from rdflib import URIRef, RDF

from project_reasoner.good_vibrations.types import GV
from project_reasoner.ref import ref


@dataclass(frozen=True)
class PromptTemplate:
    id: URIRef


def prompt_template_ref(template_id: UUID) -> URIRef:
    return ref(f"prompt_template/{str(template_id)}")


def create_prompt_template() -> PromptTemplate:
    return PromptTemplate(
        id=prompt_template_ref(uuid4()),
    )


def add_prompt_template_command(template: PromptTemplate):
    def command(g):
        g.add((template.id, RDF.type, GV.prompt_template))

    return command


def remove_prompt_template_command(template_ref: URIRef):
    def command(g):
        g.remove((template_ref, None, None))

    return command


def find_prompt_template_by_id(template_ref: URIRef):
    def query(graph):
        results = graph.query(
            f"""
            SELECT ?p ?o WHERE {{
                <{template_ref}> ?p ?o .
            }}
            """
        )

        if len(results) > 0:
            return PromptTemplate(
                id=template_ref,
            )

        return None

    return query
