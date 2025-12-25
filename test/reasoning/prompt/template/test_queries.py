from typing import Optional
from uuid import uuid4

from project_reasoner.reasoning.prompt.template.commands import (
    CreatePromptTemplateCommand,
)
from project_reasoner.reasoning.prompt.template.queries import (
    FindOnePromptTemplateByIdQuery,
)
from test.reasoning.test_reasoning_application import TestApplication


class TestCreateFindOnePromptTemplateByIdQuery:
    @staticmethod
    def create(template_id: Optional[str] = None) -> FindOnePromptTemplateByIdQuery:
        if template_id is None:
            template_id = str(uuid4())
        return FindOnePromptTemplateByIdQuery(template_id=template_id)

    def test_query_must_have_a_template_id(self):
        query = TestCreateFindOnePromptTemplateByIdQuery.create()
        assert query.template_id is not None


class TestApplicationPromptTemplateQuerying:

    def test_applications_return_nothing_for_nonexistent_prompt_template(self):
        app = TestApplication.create()
        prompt_template = app.find_one_prompt_template_by_id(
            FindOnePromptTemplateByIdQuery(template_id=str(uuid4()))
        )
        assert prompt_template is None

    def test_applications_return_existing_templates_by_id(self):
        app = TestApplication.create()
        created_prompt_template = app.create_prompt_template(
            CreatePromptTemplateCommand(
                name="Existing Template",
                template="This is an existing template.",
                parameter_definitions=None,
            )
        )
        retrieved_prompt_template = app.find_one_prompt_template_by_id(
            FindOnePromptTemplateByIdQuery(template_id=str(created_prompt_template.id))
        )

        assert retrieved_prompt_template is not None
        assert retrieved_prompt_template.id == created_prompt_template.id
