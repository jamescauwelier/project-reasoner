from rdflib import URIRef


class GV:

    # @staticmethod
    # def type_ref(type_name: str) -> URIRef:
    #     return URIRef("https://good.vibrations.dev/types/" + type_name)

    prompt_template: URIRef = URIRef("https://good.vibrations.dev/types/prompt_template")
    prompt_template_name: URIRef = URIRef("https://good.vibrations.dev/props/prompt_template/name")