from typing import Callable, Optional

from rdflib import Graph, RDF, Literal

from ref import ref


def add_project_description_command(description: str) -> Callable[[Graph], None]:
    def command(g: Graph):
        p = ref("project")
        g.add((p, RDF.type, ref("types/project")))
        g.add(
            (
                p,
                ref("types/project/description"),
                Literal(description),
            )
        )

    return command


def find_project_description() -> Callable[[Graph], Optional[str]]:

    def query(graph: Graph) -> Optional[str]:
        results = graph.query(
            f"""
            SELECT ?project ?description WHERE {{
                ?project a <{ref("types/project")}> .
                ?project <{ref("types/project/description")}> ?description .
            }}
            """
        )

        for r in results:
            return str(r.description)

        return None

    return query
