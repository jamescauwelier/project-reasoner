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
- [ ] Initial event features
  - [ ] Define an event including a description, e.g. "Receiving a bank transaction detail"
  - [ ] Delete events that are no longer relevant, e.g. because there are duplicates
  - [ ] List all known events
- [ ] Detailing events
  - [ ] Define actors, e.g. "Consumer"
  - [ ] Optionally define scenarios that bring events together or group them

### Chat Interface

- [ ] Setup a simple chat interface, using mostly ready made components to avoid having to create a new UI

### Agent Reasoning

- [ ] With all the above, in place, create a plan for how the reasoning agent will use the graph representations

