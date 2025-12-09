import os

from rdflib import URIRef

BASE_DOMAIN = os.environ.get("BASE_DOMAIN", "https://example.org/")


def ref(ref_id: str, *args) -> URIRef:
    if args:
        ref_id = ref_id.format(*args)
    return URIRef(BASE_DOMAIN + ref_id)
