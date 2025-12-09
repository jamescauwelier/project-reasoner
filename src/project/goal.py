import uuid
from dataclasses import dataclass

from rdflib import URIRef

from ref import ref


@dataclass(frozen=True)
class Goal:
    id: URIRef
    description: str


def goal_ref(goal_id: str) -> URIRef:
    return ref("goals/{0}", goal_id)


def create_goal_from_description(description: str) -> Goal:
    return Goal(id=goal_ref(str(uuid.uuid4())), description=description)
