---
description: "A dependency DAG over validated user-specific framing factors that orders which one a personalization refiner elicits next, essential factors and their ancestors first."
aliases: ["intent elicitation graph", "IEG"]
sources: ["yoon-2026"]
---
# Intent elicitation graph

> A structure that orders the next clarifying question by what it unlocks in
> a dependency graph, not by how much it would reduce [[entropy]].

## Definition / Mechanism

Yoon & Lee (2026) build a personalized-deep-research query
refiner that must decide which user-specific factor (goal, constraint,
preference, evaluation criterion) to ground next before handing a refined
query to a downstream research agent. Candidate factors are first
extracted from the query and a personalization rubric, then filtered: "A
candidate is retained only when its answer can vary across users,
materially affect downstream planning, and is not already specified by
q." Each retained factor is flagged essential when "leaving it unresolved
would likely omit a major decision branch, apply inappropriate comparison
criteria, or produce materially underspecified recommendations."[^c1]

The validated factors are then organized into the Intent Elicitation
Graph: "an Intent Elicitation Graph is constructed as a directed acyclic
graph G = (V, D), where V = E and the initial query acts as an external
root. An edge (ei , ej ) ∈ D indicates that resolving ei can change
whether or how ej should be elicited." A factor that is inactive until a
parent is covered is marked late-activatable.[^c2]

The order this yields is structural, not ranked by value: "For each
subgraph, targets are ordered so no child precedes its parent" and "When
several targets are eligible, optional targets closer to the essential
[[backbone-of-a-formula|backbone]] are prioritized." A run starts from the subgraph of essential
factors and their ancestors before touching optional ones.[^c3]

## Why it matters

This answers stall 2 with a mechanism that needs no expected-value
computation: precedence is read off the graph's edges, and importance
enters only through the essential/optional split and the backbone-first
rule, not through a per-step score. The graph doubles as an answer to
stall 1 (its nodes are the validated axes) and touches stall 3 (each
elicitation is scoped to one node, so the graph also fixes what a single
question is allowed to be about).

## Transfer

| | |
|---|---|
| **In its home field** | personalized deep-research query refinement: an LLM (GPT-5.4 in the paper) builds one IEG per instance offline, used only to scaffold training trajectories |
| **Here** | a general recipe for ordering questions whose relevance to each other is dependency, not correlation — essential nodes and their ancestors first, optional nodes ordered by graph-proximity to that backbone |
| **What survives** | precedence from structure alone, an explicit split between mandatory and optional axes, and atomic one-node-per-question elicitation |
| **What does not** | the run-time lookup. What generalizes is the training-time scaffold only. |

The graph is never consulted while questioning happens: "The IEG is used
only for trajectory construction and is unavailable at inference."[^c4]

## Limits

- **The graph is a training artifact, not a run-time one.** The policy that
  acts on real queries never sees the IEG; it only inherits whatever
  ordering behaviour the trajectories built from it instilled. Any claim
  that live questioning "follows" the graph is an inference from training
  supervision, not an observed property of deployment.
- **Node validity rests on an LLM annotator's judgement** (GPT-5.4 building
  both the target set and the graph), with no ground-truth dependency
  structure to check it against.
- Domain is narrow: user-specific framing factors for research-report
  personalization. Whether "resolving ei changes whether/how ej should be
  elicited" generalizes to axes with cyclic or many-to-many dependencies is
  not addressed — the construction requires a DAG.

## Related

[[attribute-exploration]] · [[generalized-binary-search]] · [[expected-information-gain]] · [[g-steer]]

[^c1]: yoon-2026 — "A candidate is retained only when its answer can vary across users, materially affect downstream planning, and is not already specified by q."
[^c2]: yoon-2026 — "an Intent Elicitation Graph is constructed as a directed acyclic graph G = (V, D), where V = E and the initial query acts as an external root. An edge (ei , ej ) ∈ D indicates that resolving ei can change whether or how ej should be elicited."
[^c3]: yoon-2026 — "For each subgraph, targets are ordered so no child precedes its parent."
[^c4]: yoon-2026 — "The IEG is used only for trajectory construction and is unavailable at inference."
