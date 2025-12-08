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