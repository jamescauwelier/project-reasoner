import os

from rdflib import URIRef

BASE_DOMAIN = os.environ.get("BASE_DOMAIN", "https://example.org/")


def ref(ref_id: str) -> URIRef:
    return URIRef(BASE_DOMAIN + ref_id)
