from typing import Callable, Any

from rdflib import Graph


class KnowledgeGraph:
    def __init__(self):
        self.graph = Graph()

    def update(self, command: Callable[[Graph], None]):
        command(self.graph)

    def query(self, query: Callable[[Graph], Any]) -> Any:
        return query(self.graph)
