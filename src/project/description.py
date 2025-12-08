from typing import Callable, Optional

from rdflib import Graph, RDF, URIRef, Literal


def add_project_description_command(description: str) -> Callable[[Graph], None]:
    def command(g: Graph):
        p = URIRef("https://good.vibrations.dev/project")
        g.add((p, RDF.type, URIRef("https://good.vibrations.dev/types/project")))
        g.add(
            (
                p,
                URIRef("https://good.vibrations.dev/types/project/description"),
                Literal(description),
            )
        )

    return command


def find_project_description() -> Callable[[Graph], Optional[str]]:

    def query(graph: Graph) -> Optional[str]:
        results = graph.query(
            """
            SELECT ?project ?description WHERE {
                ?project a <https://good.vibrations.dev/types/project> .
                ?project <https://good.vibrations.dev/types/project/description> ?description .
            }
            """
        )

        for r in results:
            return str(r.description)

        return None

    return query
