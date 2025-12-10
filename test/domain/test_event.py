from rdflib import URIRef

from project_reasoner.domain.event import DomainEvent, domain_event_ref


def test_a_domain_event_has_an_id():
    event_id = domain_event_ref("123")
    event = DomainEvent(id=event_id, description="Domain event description")
    assert event.id == URIRef("https://example.org/domain_event/123")


def test_a_domain_event_has_a_description():
    event_id = domain_event_ref("123")
    event = DomainEvent(id=event_id, description="Domain event description")
    assert event.description == "Domain event description"
