from dataclasses import dataclass
from uuid import uuid4, UUID

from rdflib import URIRef

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
