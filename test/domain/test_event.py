from rdflib import URIRef

from project_reasoner.domain.event import (
    DomainEvent,
    domain_event_ref,
    find_all_domain_events,
    create_domain_event_from_description,
    add_domain_event_command,
    remove_domain_event_command,
)
from project_reasoner.knowledge_graph import KnowledgeGraph


def test_a_domain_event_has_an_id():
    event_id = domain_event_ref("123")
    event = DomainEvent(id=event_id, description="Domain event description")
    assert event.id == URIRef("https://example.org/domain_event/123")


def test_a_domain_event_has_a_description():
    event_id = domain_event_ref("123")
    event = DomainEvent(id=event_id, description="Domain event description")
    assert event.description == "Domain event description"


def test_we_start_with_no_domain_events():
    knowledge = KnowledgeGraph()
    goals = knowledge.query(find_all_domain_events())
    assert len(goals) == 0


def test_we_can_add_and_retrieve_one_domain_event():
    knowledge = KnowledgeGraph()
    knowledge.update(
        add_domain_event_command(
            create_domain_event_from_description("Money was spent on a bank account")
        )
    )
    goals = knowledge.query(find_all_domain_events())
    assert len(goals) == 1
    assert goals[0].description == "Money was spent on a bank account"


def test_we_can_add_and_retrieve_multiple_domain_events():
    knowledge = KnowledgeGraph()
    knowledge.update(
        add_domain_event_command(
            create_domain_event_from_description("Money was spent on a bank account")
        )
    )
    knowledge.update(
        add_domain_event_command(
            create_domain_event_from_description(
                "Money was earned and received on a bank account"
            )
        )
    )
    goals = knowledge.query(find_all_domain_events())
    assert len(goals) == 2


def test_we_can_remove_a_domain_event():
    domain = create_domain_event_from_description("Money was spent on a bank account")
    knowledge = KnowledgeGraph()
    knowledge.update(add_domain_event_command(domain))
    knowledge.update(remove_domain_event_command(domain.id))
    goals = knowledge.query(find_all_domain_events())
    assert len(goals) == 0
