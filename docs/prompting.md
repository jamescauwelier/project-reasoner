# Prompting

Prompts are the inputs given to the AI model to elicit responses. The simplest prompts are just static texts. For more
advanced use cases, prompts can be dynamically composed based on context, user inputs, or other factors.

## Motivation

The motivation for defining prompt composition as a first-class concept in our knowledge graph, is that it enables 
graph reasoning on how dynamic additions to the graph can influence the prompting of the agent. If this were not 
embedded in the graph, it would have to be handled outside of it, meaning it would need hardcoded logic.

## Components

### `PromptTemplate`

A `PromptTemplate` defines an entity that describes to a composer how to construct a specific prompt. To do this, it 
contains a template, which uses the [Jinja 2 template language](https://jinja.palletsprojects.com/en/stable/templates/).

Additionally, it provides information on how to pull in the relevant data and its constraints. It uses descriptions in 
`PromptTemplateParameter` definitions.

### `PromptComposer`

A template is only useful when it can be composed into a final prompt. A `PromptComposer` is responsible for taking a
`PromptTemplate`, and documenting where the necessary data can be found to fill in the template parameters.

A KG runtime can use this information to run Jinja2 template rendering, pulling in the relevant data from the KG as 
needed to produce the `Prompt` and persist it in the graph. This `Prompt` is then used to prompt the AI model.

### `Prompt`

A piece of fulltext that is used to prompt an LLM model and becomes part of a `ChatHistory`.

## Tasks

- [ ] Define a `Prompt`
  - [ ] add static text property
  - [ ] add an optional reference to a `PromptComposer` to document its origin
- [ ] Define a `PromptComposer`
  - [x] Define a `PromptTemplate`
    - [x] Install Jinja2 template engine
    - [x] Define how to represent a Jinja2 template in RDF
    - [x] Finalize the template representation
    - [ ] Create a way to pass in application commands to build the knowledge graph with prompt templates
      - [ ] Define a `ReasoningApplication`
        - [ ] Initializes and manages the KG for reasoning
        - [ ] Receives command objects to mutate the KG 
          - build an example for `PromptTemplate` and `PromptTemplateParameter` creation
        - [ ] Receives query objects to pull data from the KG
          - build an example for `PromptTemplate` and `PromptTemplateParameter` creation
  - [ ] Define `PromptContext` definitions to pull in relevant data
    - is this done using shacl, sparql, URIRef?