# Event Storming

The analysis in this project is loosely based on the event storming approach for gathering requirements. Loosely, because
event storming relies heavily on human facilitation of groups of people not usually found in the same room.

To document a project using event storming, we can follow these general steps:

- Identify the main goal of defining the software project.
- Identify the main events relevant to the project.
- Identify the actors involved in the events.
- Dig deeper to identify events and processes in greater details.

At a first level, we should understand the project better in terms of:

- goals
- features
- use cases

Ideally, we should get a software design out of this process, containing:

- Bounded contexts, with a context definition, responsibilities, and interfaces.
- Aggregates, and their consistency guarantees.
- Entities and value objects.