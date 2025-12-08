from src.knowledge_graph import KnowledgeGraph
from src.project.description import (
    find_project_description,
    add_project_description_command,
)


def test_a_project_description_starts_empty():
    knowledge = KnowledgeGraph()
    description = knowledge.query(find_project_description())
    assert description is None


def test_a_project_description_can_be_added_and_retrieved():
    knowledge = KnowledgeGraph()
    knowledge.update(add_project_description_command("This is a test project."))
    description = knowledge.query(find_project_description())
    assert description == "This is a test project."
