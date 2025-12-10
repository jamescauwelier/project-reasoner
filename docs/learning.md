# Learning

An essential part of our reasoning agent is its ability to guide a conversation towards achieving specific learning goals.
For event storming, this means learning the events, actors, processes, and constraints relevant to a software project.

## Learning Goal

The first element to focus on is defining the goals for our learning process. And do keep in mind that these goals may
evolve as we progress through a learning session.

A learning goal could be simply described:

> Understand the goal of a particular piece of envisioned software, and how those goals translate into features and use cases.

## Learning Evaluation

A second element to learning is that we need to evaluate how well we are doing. Take the following example:

**Q**: What shall we build today?

> Answer 1: An underground pool in the forest.
> Answer 2: A personal finance app.
> Answer 3: A personal finance app to gain control of spending habits.
> Answer 4: A personal finance app to gain control of spending habits that also track my workout routines.

How should we rate these answers?

- Answer 1: Irrelevant
- Answer 2: Incomplete
- Answer 3: 
  - Relevant, but still incomplete. Who will be using the app? What kind of app, mobile, web, desktop?
  - Not specific enough to enable development.
- Answer 4: Relevant, partially incomplete, but with conflicting features. Is it a finance app or a fitness app?

There can be multiple qualities to evaluate against and some or multiple might be valid or not. The invalid or absent
qualities should enable further questioning to refine the learning process.

An `Evaluation` produces evaluation states. A relevancy evaluation would produce either a `relevant` or `irrelevant` state.
Depending on the produced state, further actions can be taken. For example, when a statement is deemed `irrelevant`, a
follow-up question can be asked. For this question to be presented, it needs to be composed, so the state `irrelevant` 
links to an action `PromptUser` and is passed a `PromptComposer` which can take in contextual information to produce the
needed prompt.

- [ ] Figure out how to represent
  - [ ] Evaluations
    - [ ] What types of evaluations are needed?
    - [ ] How to represent evaluation criteria? Just a prompt where an LLM evaluates?
    - [ ] What system executes the evaluation reasoning? Is there over graph reasoning using SHACL or SPARQL?
    - [ ] How do we represent the inputs to the evaluation? Is this a message history?
  - [ ] Evaluation States
  - [ ] Evaluation Actions
  - [ ] Prompt Composers

## Case Study

Learning goal: find out what the user wants to build.

Example evaluations:

- On what platform will the app run? Mobile, web, desktop?
- Who are the intended users of the app?
- What are the main goals of the app?