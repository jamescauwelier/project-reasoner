from rdflib import URIRef


class GV:

    # @staticmethod
    # def type_ref(type_name: str) -> URIRef:
    #     return URIRef("https://good.vibrations.dev/types/" + type_name)

    prompt_template: URIRef = URIRef("https://good.vibrations.dev/types/prompt_template")
    prompt_template_name: URIRef = URIRef("https://good.vibrations.dev/props/prompt_template/name")
    prompt_template_contents: URIRef = URIRef("https://good.vibrations.dev/props/prompt_template/contents")
    prompt_template_has_parameter: URIRef = URIRef("https://good.vibrations.dev/props/prompt_template/has_parameter")
    prompt_template_parameter_set: URIRef = URIRef("https://good.vibrations.dev/props/prompt_template/parameter_set")

    prompt_template_parameter: URIRef = URIRef("https://good.vibrations.dev/types/prompt_template_parameter")
    prompt_template_parameter_label: URIRef = URIRef("https://good.vibrations.dev/props/prompt_template_parameter/label")
    prompt_template_parameter_type: URIRef = URIRef("https://good.vibrations.dev/props/prompt_template_parameter/type")

    # relationships
    parameterizes: URIRef = URIRef("https://good.vibrations.dev/relationships/parameterizes")