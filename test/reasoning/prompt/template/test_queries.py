from typing import Optional
from uuid import uuid4

from project_reasoner.reasoning.prompt.template.queries import (
    FindOnePromptTemplateByIdQuery,
)


class TestCreateFindOnePromptTemplateByIdQuery:
    @staticmethod
    def create(template_id: Optional[str] = None) -> FindOnePromptTemplateByIdQuery:
        if template_id is None:
            template_id = str(uuid4())
        return FindOnePromptTemplateByIdQuery(template_id=template_id)

    def test_query_must_have_a_template_id(self):
        query = TestCreateFindOnePromptTemplateByIdQuery.create()
        assert query.template_id is not None
