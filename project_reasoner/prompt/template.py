from dataclasses import dataclass, field
from enum import Enum
from typing import List
from uuid import uuid4, UUID

from rdflib import URIRef, RDF, Literal

from project_reasoner.good_vibrations.types import GV
from project_reasoner.ref import ref


class PromptTemplateParameterDataType(Enum):
    TEXT = "text"


@dataclass(frozen=True)
class PromptTemplateParameter:
    id: URIRef
    label: str
    data_type: PromptTemplateParameterDataType


@dataclass(frozen=True)
class PromptTemplate:
    id: URIRef
    name: str
    template: str
    parameter_definitions: List[PromptTemplateParameter] = field(
        default_factory=lambda: []
    )


def prompt_template_ref(template_id: UUID) -> URIRef:
    return ref(f"prompt_template/{str(template_id)}")


def prompt_template_parameter_ref(parameter_id: UUID) -> URIRef:
    return ref(f"prompt_template_parameter/{str(parameter_id)}")


def create_prompt_template(name: str, contents: str) -> PromptTemplate:
    return PromptTemplate(id=prompt_template_ref(uuid4()), name=name, template=contents)


def create_prompt_template_parameter(
    label: str, data_type: PromptTemplateParameterDataType
) -> PromptTemplateParameter:
    return PromptTemplateParameter(
        id=prompt_template_parameter_ref(uuid4()), label=label, data_type=data_type
    )


def add_prompt_template_command(template: PromptTemplate):
    def command(g):

        # defines general template properties
        g.add((template.id, RDF.type, Literal(GV.prompt_template)))
        g.add((template.id, GV.prompt_template_name, Literal(template.name)))
        g.add((template.id, GV.prompt_template_contents, Literal(template.template)))

        # constructs a parameter bag
        for parameter in template.parameter_definitions:

            # first, create the parameter node
            g.add((parameter.id, RDF.type, GV.prompt_template_parameter))
            g.add(
                (
                    parameter.id,
                    GV.prompt_template_parameter_label,
                    Literal(parameter.label),
                )
            )
            g.add(
                (
                    parameter.id,
                    GV.prompt_template_parameter_type,
                    Literal(parameter.data_type.name),
                )
            )
            g.add((parameter.id, GV.parameterizes, URIRef(template.id)))

    return command


def remove_prompt_template_command(template_ref: URIRef):
    def command(g):
        g.remove((template_ref, None, None))

    return command


def find_prompt_template_by_id(template_ref: URIRef):
    def query(graph):
        template_data = graph.query(
            f"""
            SELECT ?p ?o WHERE {{
                <{template_ref}> ?p ?o .
            }}
            """
        )

        props = {}
        for result in template_data:
            props[result.p] = result.o

        if len(props) > 0:
            tpl = PromptTemplate(
                id=template_ref,
                name=str(props[GV.prompt_template_name]),
                template=str(props[GV.prompt_template_contents]),
            )

            parameter_data = graph.query(
                f"""
                SELECT ?param ?label ?data_type WHERE {{
                    ?param <{GV.parameterizes}> <{template_ref}> .
                    ?param <{GV.prompt_template_parameter_label}> ?label .
                    ?param <{GV.prompt_template_parameter_type}> ?data_type .
                }}
            """
            )

            for data in parameter_data:
                parameter = PromptTemplateParameter(
                    id=data.param,
                    label=str(data.label),
                    data_type=PromptTemplateParameterDataType[
                        data.data_type.toPython()
                    ],
                )
                tpl.parameter_definitions.append(parameter)

            return tpl

        return None

    return query
