# Prompting

Prompts are the inputs given to the AI model to elicit responses. The simplest prompts are just static texts. For more
advanced use cases, prompts can be dynamically composed based on context, user inputs, or other factors.

## Motivation

The motivation for defining prompt composition as a first-class concept in our knowledge graph, is that it enables 
graph reasoning on how dynamic additions to the graph can influence the prompting of the agent. If this were not 
embedded in the graph, it would have to be handled outside of it, meaning it would need hardcoded logic.

## Tasks

- [ ] Define a `Prompt`
  - [ ] add static text property
  - [ ] add an optional reference to a `PromptComposer` to document its origin
- [ ] Define a `PromptComposer`
  - [ ] Define a `PromptTemplate`
    - [ ] Install Jinja2 template engine
    - [ ] Define how to represent a Jinja2 template in RDF
    - [ ] Finalize the template representation
  - [ ] Define `PromptContext` definitions to pull in relevant data
    - is this done using shacl, sparql, URIRef?