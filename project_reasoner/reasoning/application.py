from typing import Optional

from project_reasoner.knowledge_graph import KnowledgeGraph
from project_reasoner.prompt.template import (
    PromptTemplate,
    create_prompt_template,
    add_prompt_template_command,
)
from project_reasoner.prompt.template import (
    create_prompt_template_parameter,
    PromptTemplateParameterDataType,
)
from project_reasoner.reasoning.prompt.template.commands import (
    CreatePromptTemplateCommand,
)


class ReasoningApplication:
    def __init__(self, name: str, kg: Optional[KnowledgeGraph] = None):
        self.__name: str = name
        self.__graph: KnowledgeGraph = kg or KnowledgeGraph()

    @property
    def name(self):
        return self.__name

    def create_prompt_template(
        self, command: CreatePromptTemplateCommand
    ) -> PromptTemplate:
        prompt_template = create_prompt_template(
            name=command.name,
            contents=command.template,
        )
        if command.parameter_definitions is not None:
            for label, data_type in command.parameter_definitions.items():
                prompt_template.parameter_definitions.append(
                    create_prompt_template_parameter(
                        label=label,
                        data_type=PromptTemplateParameterDataType[data_type.upper()],
                    )
                )
        self.__graph.update(add_prompt_template_command(prompt_template))

        return prompt_template
