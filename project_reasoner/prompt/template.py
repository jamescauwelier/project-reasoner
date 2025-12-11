from dataclasses import dataclass
from uuid import uuid4, UUID

from rdflib import URIRef, RDF, Literal
from rdflib.plugins.sparql.processor import SPARQLResult

from project_reasoner.good_vibrations.types import GV
from project_reasoner.ref import ref


@dataclass(frozen=True)
class PromptTemplate:
    id: URIRef
    name: str


def prompt_template_ref(template_id: UUID) -> URIRef:
    return ref(f"prompt_template/{str(template_id)}")


def create_prompt_template(name: str) -> PromptTemplate:
    return PromptTemplate(id=prompt_template_ref(uuid4()), name=name)


def add_prompt_template_command(template: PromptTemplate):
    def command(g):
        g.add((template.id, RDF.type, Literal(GV.prompt_template)))
        g.add((template.id, GV.prompt_template_name, Literal(template.name)))

    return command


def remove_prompt_template_command(template_ref: URIRef):
    def command(g):
        g.remove((template_ref, None, None))

    return command


def find_prompt_template_by_id(template_ref: URIRef):
    def query(graph):
        results: SPARQLResult = graph.query(
            f"""
            SELECT ?p ?o WHERE {{
                <{template_ref}> ?p ?o .
            }}
            """
        )

        props = {}
        for result in results:
            props[result.p] = result.o

        if len(props) > 0:
            return PromptTemplate(
                id=template_ref,
                name=str(props[GV.prompt_template_name]),
            )

        return None

    return query
