from dataclasses import dataclass


@dataclass(frozen=True)
class FindOnePromptTemplateByIdQuery:
    template_id: str
