# Project Reasoner

The main purpose of this project is to develop an LLM agent that can more deeply inquire about the requirements of a 
software project. The main approach will be to implement a facilitator agent applying event storming, an approach that
is common when using Domain Driven Design (DDD).

To enable the reasoning capabilities of the agent, a knowledge graph will be constructed. This explores how capable an 
in-memory RDF graph could be to support reasoning instead of relying on brittle LLM reasoning prompts.

The agent will:

- gather requirements for a software project
- reason about project goals, progress, constraints, etc.
- record how it reasons it's way through an event storming session
- act as a context manager to provide compact excerpts to the LLM agent

## Architecture

This is an experimental topic, without the need for a production deployment. Therefore, the architecture is quite simple.

### Dependencies

- [JSON-LD](https://json-ld.org/) 
  - [Specification](https://www.w3.org/TR/json-ld/)
- RDFLib
  - [Github](https://github.com/RDFLib/rdflib) 
  - [Manual](https://rdflib.readthedocs.io/en/stable/)
- SHACL
  - [Specification](https://www.w3.org/TR/shacl/)
- [pySHACL](https://github.com/RDFLib/pySHACL)

### Knowledge Graph

Graphs are usually represented either using RDF triples or property graphs. Production systems often use the latter in 
products such as Neo4J. However, RDF triples have a more established set of specifications for defining shapes and in 
how to enable advanced reasoning. Therefore, we'll be using this approach.

### Agent Capabilities

There are many possibilities for local first agent architectures using knowledge graphs for reasoning. However, since 
these would have to rely on less mature frameworks, we'll be exploring a proof-of-concept in LangChain / LangGraph.

## Tasks

### Representing Projects

We need to define how a software project can be represented in a knowledge graph.

- [ ] Design a project representation approach

### Representing Event Storming

Event storming is an approach to gather requirements and goes through various stages. We need to find a knowledge graph
representation for this reasoning process.

- [x] Project
  - [x] Start with a simple description, the 'what' of a project, e.g. "a personal finance app"
  - [x] Now supplement with goals / aims for the project (the why's), e.g. "to help users get insights in their spending habits"
- [x] Initial event features
  - [x] Define an event including a description, e.g. "Receiving a bank transaction detail"
  - [x] Delete events that are no longer relevant, e.g. because there are duplicates
  - [x] List all known events
- [ ] TODO: detailing (un)grouping of events to identify boundaries
- [ ] TODO: brainstorm on what details can be added to events
  - [ ] Processes / Flows
  - [ ] Commands + constraints
  - [ ] Policies / Rules
  - [ ] Actors
- [ ] TODO: extract feature definitions from domain knowledge and project goals

### Chat Interface

- [ ] Setup a simple chat interface, using mostly ready made components to avoid having to create a new UI

### Agent Reasoning

- [ ] With all the above, in place, create a plan for how the reasoning agent will use the graph representations

#### [Learning](./learning.md) 

In essence, for reasoning, the agent goes through interactions where it has certain goals or tasks to perform. It needs
to know how to query for the learning it needs to do, and how to evaluate the responses it gets back. Finally, it needs
to know how to end an interactive sessions with an output capturing what it has learned.

##### Representing Reasoning / Learning Flows

- [ ] Define a `LearningGoal`, e.g. to understand a project specification
  - [ ] Create a basic `LearningGoal` definition
  - [ ] Extend with `ValidationCriteria` that evaluate whether the goal has been achieved
    - [ ] Define a `Quality`, e.g. relevance
    - [ ] Define a `QualityValidator`, e.g. 
- [ ] Define a `LearningSession` to collect interactions towards a learning goal
  - [ ] Define a `MessageHistory`
  - [ ] Add `Message` entries to the history, with properties `role` and `content`

**What would be a useful case study?**

Let's consider learning about a personal finance app project. First, we'd like to know the goals of the project and a 
short description. For each of the goals, if we are using event storming, we consider what the events would be related
to this goal.

To query for the project description, we need to know what properties an answer would possess:

- contains a short summary description
- describes the software context(s) in which the software should run, e.g. a web application, mobile app, etc.
- describes the real world contexts in which the software will be useful, e.g. in financial planning offices, for personal use, etc.
- describes what motivates the creation of the software
  - how is it useful?
  - how is it different from other solutions?



##### Running Learning Sessions

- [ ] Brainstorm on how to perform a learning session based on learning goal definitions
