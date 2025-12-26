from typing import Callable, Any

from rdflib import Graph, RDF, SH, Bag, Literal, BNode

from project_reasoner.good_vibrations.types import GV
from project_reasoner.ref import ref


class KnowledgeGraph:
    def __init__(self):
        self.graph = Graph()
        self.__validation_graph = Graph()
        self.__initialize_validation_graph()

    def __initialize_validation_graph(self):

        # defines a shape for prompt templates
        prompt_template_shape_id = ref("shapes/prompt_template_shape")
        self.__validation_graph.add((prompt_template_shape_id, RDF.type, SH.NodeShape))
        self.__validation_graph.add(
            (prompt_template_shape_id, SH.targetClass, GV.prompt_template)
        )

        # constrains the prompt template shape to have a name property
        properties = Bag(graph=self.__validation_graph)

        prop_one = BNode()
        properties.append((prop_one, SH.path, GV.prompt_template_name))
        properties.append((prop_one, SH.minCount, Literal(1)))
        properties.append((prop_one, SH.maxCount, Literal(1)))

        self.__validation_graph.add((prompt_template_shape_id, SH.property, prop_one))

    def update(self, command: Callable[[Graph], None]):
        command(self.graph)

    def query(self, query: Callable[[Graph], Any]) -> Any:
        return query(self.graph)
