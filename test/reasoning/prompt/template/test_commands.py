from typing import Dict, Optional

from project_reasoner.prompt.template import PromptTemplateParameterDataType
from project_reasoner.reasoning.prompt.template.commands import (
    CreatePromptTemplateCommand,
)
from test.reasoning.test_reasoning_application import TestApplication


class TestCreatePromptTemplateCommand:

    def test_command_must_have_a_name_field(self):
        expected_name = "Sample Prompt Template"
        command = TestCreatePromptTemplateCommand.create(name=expected_name)
        assert command.name == expected_name

    def test_command_must_have_a_template_field(self):
        expected_template = "This is a sample template named: {{template_name}}."
        command = TestCreatePromptTemplateCommand.create(template=expected_template)
        assert command.template == expected_template

    def test_command_must_have_a_parameters_field(self):
        expected_parameter_definitions = {"template_name": "string"}
        command = TestCreatePromptTemplateCommand.create(
            template="This is a sample template named: {{template_name}}.",
            parameter_definitions=expected_parameter_definitions,
        )
        assert command.parameter_definitions == expected_parameter_definitions

    @staticmethod
    def create(
        name: str = "",
        template: str = "",
        parameter_definitions: Optional[Dict[str, str]] = None,
    ):
        return CreatePromptTemplateCommand(
            name=name, template=template, parameter_definitions=parameter_definitions
        )


class TestApplicationPromptManagement:
    def test_prompts_can_be_created(self):
        app = TestApplication.create()
        created_prompt_template = app.create_prompt_template(
            TestCreatePromptTemplateCommand.create(
                name="Analysis Prompt",
                template="Analyze the following project: {{project_description}}.",
                parameter_definitions={"project_description": "text"},
            )
        )
        assert created_prompt_template.id is not None
        assert created_prompt_template.name is "Analysis Prompt"
        assert (
            created_prompt_template.template
            is "Analyze the following project: {{project_description}}."
        )
        assert created_prompt_template.parameter_definitions[0].id is not None
        assert (
            created_prompt_template.parameter_definitions[0].label
            == "project_description"
        )
        assert (
            created_prompt_template.parameter_definitions[0].data_type
            == PromptTemplateParameterDataType.TEXT
        )
