import pytest

from project_reasoner.knowledge_graph import KnowledgeGraph
from project_reasoner.prompt.template import (
    create_prompt_template,
    PromptTemplate,
    add_prompt_template_command,
    find_prompt_template_by_id,
    remove_prompt_template_command,
)


def __create_prompt_template(name: str = "Sample Template") -> PromptTemplate:
    return create_prompt_template(name=name)


def test_prompt_templates_have_an_id_property():
    # creates prompt template
    template = __create_prompt_template()

    # persist in graph
    graph = KnowledgeGraph()
    graph.update(add_prompt_template_command(template))
    template = graph.query(find_prompt_template_by_id(template.id))

    assert template.id is not None


def test_prompt_templates_have_a_name_property():

    # creates prompt template
    template = __create_prompt_template(name="Prompt Template Name")

    # persist in graph
    graph = KnowledgeGraph()
    graph.update(add_prompt_template_command(template))
    template = graph.query(find_prompt_template_by_id(template.id))

    assert template.name == "Prompt Template Name"


@pytest.mark.skip(reason="Not yet implemented")
def test_prompt_templates_have_a_contents_property():
    pass


@pytest.mark.skip(reason="Not yet implemented")
def test_prompt_templates_have_a_parameters_property():
    pass


def test_prompt_templates_can_be_queried():
    created_template = __create_prompt_template()
    graph = KnowledgeGraph()
    graph.update(add_prompt_template_command(created_template))
    queried_template = graph.query(find_prompt_template_by_id(created_template.id))
    assert queried_template is not None
    assert queried_template.id == created_template.id


def test_prompt_templates_can_be_removed_from_graph():
    created_template_1 = __create_prompt_template()
    created_template_2 = __create_prompt_template()
    graph = KnowledgeGraph()
    graph.update(add_prompt_template_command(created_template_1))
    graph.update(add_prompt_template_command(created_template_2))
    graph.update(remove_prompt_template_command(created_template_1.id))
    queried_template_1 = graph.query(find_prompt_template_by_id(created_template_1.id))
    queried_template_2 = graph.query(find_prompt_template_by_id(created_template_2.id))
    assert queried_template_1 is None
    assert queried_template_2 is not None
