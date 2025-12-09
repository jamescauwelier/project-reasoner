import uuid
from typing import Optional

from rdflib import URIRef

from project_reasoner.knowledge_graph import KnowledgeGraph
from project_reasoner.project.goal import (
    Goal,
    goal_ref,
    create_goal_from_description,
    add_goal_command,
    find_all_goals,
    remove_goal_command,
)


def __create_goal(
    identifier: Optional[URIRef] = None, description: Optional[str] = None
):
    if identifier is None:
        identifier = goal_ref(str(uuid.uuid4()))
    if description is None:
        description = "Default goal description"
    return Goal(id=identifier, description=description)


def test_a_goal_has_an_identifier():
    goal = __create_goal(identifier=goal_ref("abc"))
    assert goal.id == URIRef("https://example.org/goals/abc")


def test_a_goal_has_a_description():
    goal = __create_goal(description="to enable healthy financial decisions")
    assert goal.description == "to enable healthy financial decisions"


def test_we_start_with_no_goals():
    knowledge = KnowledgeGraph()
    goals = knowledge.query(find_all_goals())
    assert len(goals) == 0


def test_we_can_add_and_retrieve_one_goal():
    knowledge = KnowledgeGraph()
    knowledge.update(add_goal_command(create_goal_from_description("learn python")))
    goals = knowledge.query(find_all_goals())
    assert len(goals) == 1
    assert goals[0].description == "learn python"


def test_we_can_add_and_retrieve_multiple_goals():
    knowledge = KnowledgeGraph()
    knowledge.update(add_goal_command(create_goal_from_description("learn Python")))
    knowledge.update(add_goal_command(create_goal_from_description("learn Rust")))
    goals = knowledge.query(find_all_goals())
    assert len(goals) == 2


def test_we_can_remove_a_goal():
    goal = create_goal_from_description("learn python")
    knowledge = KnowledgeGraph()
    knowledge.update(add_goal_command(goal))
    knowledge.update(remove_goal_command(goal.id))
    goals = knowledge.query(find_all_goals())
    assert len(goals) == 0
