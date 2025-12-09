import uuid
from typing import Optional

import pytest
from rdflib import URIRef

from src.project.goal import Goal, goal_ref


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


@pytest.mark.skip(reason="Not yet implemented")
def test_we_start_with_no_goals():
    pass


@pytest.mark.skip(reason="Not yet implemented")
def test_we_can_add_and_retrieve_one_goal():
    pass


@pytest.mark.skip(reason="Not yet implemented")
def test_we_can_add_and_retrieve_multiple_goals():
    pass


@pytest.mark.skip(reason="Not yet implemented")
def test_we_can_remove_a_goal():
    pass
