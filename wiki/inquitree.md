---
description: "An evaluation environment that turns a scientific paper into a dependency DAG of subtopics and studies, then drives an LLM agent through it as a stateful, multi-turn inquiry loop."
aliases: ["InquiTree", "Research Tree evaluation environment"]
sources: ["cui-2026"]
---
# InquiTree

> A paper becomes a graph of what must be explored before what; an agent is
> scored on the loop of proposing, observing feedback, and revising — not
> on a single final artifact.

## Definition / Mechanism

Each source paper is represented as a research tree `G = (N, E)`, a DAG
over four node types — Topic, Subtopic, Study, Result. "Crucially, the DAG
property is about subtopic-level logical dependency: edges encode which
subtopics must be explored before another subtopic can be meaningfully
pursued."[^c1]

The agent moves through Topic → Subtopic → Study → Result states,
proposing free text that the environment maps to the nearest valid
candidate node by cosine similarity of sentence embeddings; below a
threshold the state does not change: "Otherwise, the action is treated as
invalid in the current context and the environment remains in st."[^c2]

Subtopic transitions are further gated by the DAG's partial order: "To
ensure exploration follows a coherent scientific logic, we enforce
subtopic dependencies encoded in G: some subtopics are only considered
valid after certain other subtopics have been explored."[^c3]

Evaluation runs on a 30-paper pool: "starting from the neuroscience domain,
we curate 30 papers from CNS-level venues for evaluation and release
IT-18, an 18-paper open-access subset whose configurations and logs can be
publicly distributed."[^c4]

## Why it matters

This is a concrete testbed for stall 2 (which axis first) where the order
is not free-form: a subtopic's validity is gated by which other subtopics
have already been visited, so "which axis first" has a ground-truth
partial order to score against, not just a preference criterion. It also
instantiates stall 3 (how a question touches the axis): the free-text
action is only counted as touching a given axis once it clears the
similarity threshold against that axis's canonical description.

## Transfer

| | Home field | Here | Survives | Does not |
|---|---|---|---|---|
| DAG-of-prerequisites ordering | Agent-evaluation / scientific-workflow benchmarking | Scores an agent's subtopic proposals against a paper-derived prerequisite DAG | The idea of a verifiable partial order over which axis is askable next | The specific gate (embedding cosine similarity, a single threshold τ) — an artifact of this benchmark's parser, not a general account of when an axis is "reachable" |

## Limits

Single domain (neuroscience, CNS-level venues), automatically generated
hints and Fake Results checked only by an internal monotonicity sanity
check, not by independent human verification at scale; the embedding-based
action-matching step (`text-embedding-3-small`) can itself misclassify a
valid proposal as invalid, conflating parser noise with agent competence.

## Related

[[erosion-of-marginal-capabilities]] · [[interpolation-extrapolation-boundary]] · [[optimal-decision-tree]] · [[value-of-information]]

[^c1]: cui-2026 — "Crucially, the DAG property is about subtopic-level logical dependency: edges encode which subtopics must be explored before another subtopic can be meaningfully pursued."
[^c2]: cui-2026
[^c3]: cui-2026 — "To ensure exploration follows a coherent scientific logic, we enforce subtopic dependencies encoded in G: some subtopics are only considered valid after certain other subtopics have been explored."
[^c4]: cui-2026 — "starting from the neuroscience domain, we curate 30 papers from CNS-level venues for evaluation and release IT-18, an 18-paper open-access subset whose configurations and logs can be publicly distributed."
