from rdflib import URIRef

from project_reasoner.ref import ref


def test_ref_prepends_a_base_domain():
    result = ref("test/path")
    expected = URIRef("https://example.org/test/path")
    assert result == expected


def test_ref_formats_with_args():
    result = ref("items/{0}/details/{1}", "123", "456")
    expected = URIRef("https://example.org/items/123/details/456")
    assert result == expected
