import uuid
from dataclasses import dataclass
from typing import Callable, List

from rdflib import URIRef, Graph, RDF, Literal

from ref import ref


@dataclass(frozen=True)
class Goal:
    id: URIRef
    description: str


def goal_ref(goal_id: str) -> URIRef:
    return ref("goals/{0}", goal_id)


def create_goal_from_description(description: str) -> Goal:
    return Goal(id=goal_ref(str(uuid.uuid4())), description=description)


def add_goal_command(goal: Goal) -> Callable[[Graph], None]:
    def command(g: Graph):
        g.add((goal.id, RDF.type, ref("types/goal")))
        g.add(
            (
                goal.id,
                ref("types/goal/description"),
                Literal(goal.description),
            )
        )

    return command


def remove_goal_command(goal_id: URIRef) -> Callable[[Graph], None]:
    def command(g: Graph):
        g.remove((goal_id, None, None))

    return command


def find_all_goals() -> Callable[[Graph], List[Goal]]:

    def query(graph: Graph) -> List[Goal]:
        results = graph.query(
            f"""
            SELECT ?goal ?description WHERE {{
                ?goal a <{ref("types/goal")}> .
                ?goal <{ref("types/goal/description")}> ?description .
            }}
            """
        )

        goals = []
        for result in results:
            goals.append(Goal(id=result.goal, description=str(result.description)))

        return goals

    return query
