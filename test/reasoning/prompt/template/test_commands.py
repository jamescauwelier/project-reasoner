from typing import Dict, Optional

from project_reasoner.reasoning.prompt.template.commands import (
    CreatePromptTemplateCommand,
)


class TestCreatePromptTemplateCommand:

    @staticmethod
    def __create(
        name: str = "",
        template: str = "",
        parameter_definitions: Optional[Dict[str, str]] = None,
    ):
        if parameter_definitions is None:
            parameter_definitions = {}
        return CreatePromptTemplateCommand(
            name=name, template=template, parameter_definitions=parameter_definitions
        )

    def test_command_must_have_a_name_field(self):
        expected_name = "Sample Prompt Template"
        command = TestCreatePromptTemplateCommand.__create(name=expected_name)
        assert command.name == expected_name

    def test_command_must_have_a_template_field(self):
        expected_template = "This is a sample template named: {{template_name}}."
        command = TestCreatePromptTemplateCommand.__create(template=expected_template)
        assert command.template == expected_template

    def test_command_must_have_a_parameters_field(self):
        expected_parameter_definitions = {"template_name": "string"}
        command = TestCreatePromptTemplateCommand.__create(
            template="This is a sample template named: {{template_name}}.",
            parameter_definitions=expected_parameter_definitions,
        )
        assert command.parameter_definitions == expected_parameter_definitions
