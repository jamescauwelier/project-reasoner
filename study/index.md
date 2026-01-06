# Study Notes

## JSON-LD

[[Spec](https://www.w3.org/TR/json-ld/) | [Playground](https://json-ld.org/playground/next/)]

## JSON-LD Star

[[Spec](https://json-ld.github.io/json-ld-star/)]

For now, we focus on standard JSON-LD.

## SHACL

[[Spec](https://www.w3.org/TR/shacl/) | [Playground](https://shacl-playground.zazuko.com/)]

SHACL is a language for describing and validating RDF graphs by defining shapes and constraints.

### Working with context

A graph contains context such as this:

```json
{
"@context": {
    "sh": "http://www.w3.org/ns/shacl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
    "@graph": []
}
```

When SHACL does not properly validate the shapes, verify the context!

## SHACL Advanced Features

[[Spec](https://www.w3.org/TR/shacl-af/)]