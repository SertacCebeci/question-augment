---
description: "A benchmark generator that accepts a structural or temporal filter into a question's trace only when it shrinks the candidate-answer set, then verifies the fluent rewrite against that trace."
aliases: ["ChronoQG", "TKGQG benchmark construction framework", "topology-temporal subgraph sampling", "trace-grounded question generation"]
sources: ["liu-2026-chronoqg"]
---
# ChronoQG

> A generator that builds one candidate-narrowing trace at a time and refuses any step — structural or temporal — that does not actually narrow it, then asks a verifier to check the fluent rewrite still matches that trace.

## Definition / Mechanism

ChronoQG constructs temporal-knowledge-graph question-generation (TKGQG)
benchmark instances in three stages. First, it draws temporal filters from a
fixed [[temporal-constraint-taxonomy]] over point- and interval-valued facts.
Second, starting from a seed candidate-answer set $C_0$, it walks a
hop-bounded topological template and at each step applies one of
`forward_transition` (relation traversal), `structural_filter` (an extra edge
constraint), or `temporal_filter` (a constraint from the taxonomy), stopping
once the candidate set has shrunk to one entity.

"Each accepted action must update or shrink the candidate set, ensuring that
the final answer is determined by the joint effect of hop-bounded subgraph
topology and temporal constraints."[^c1]

A step that would not shrink $C_t$ is rejected outright:

"the progressive construction above enforces constraint necessity during
sampling. In this way, ChronoQG filters out the pseudo-temporal conditions …,
namely those whose removal leaves the correct answers unchanged."[^c2]

Third, it turns the accepted trace into a template question, rewrites it into
fluent language with an LLM, and checks the rewrite against the trace:

"It first constructs a template question from the accepted sampling trace,
then rewrites the template into fluent natural language through
verifier-guided agentic rewriting. Failed rewrites are repaired or
discarded, reducing semantic shift and answer leakage during benchmark
construction."[^c3]

## Why it matters

Selecting which axis (structural or temporal) to narrow next is exactly what
decides whether a generated question's surface form is redundant: a filter
applied after the fact can look like it constrains the answer while removing
no world from the candidate set. ChronoQG makes that check — does this step
change $C_t$? — a gate on every accepted action rather than a property
checked afterward.

## Limits

The necessity check only guarantees that no single accepted step in *this*
sampling order was redundant; it does not prove the final constraint set is
minimal, since a different action order could have reached the same answer
with fewer steps — no minimality claim is made in the source. The pipeline is
defined for entity/relation temporal knowledge graphs with point or interval
timestamps; it says nothing about free-text or under-specified temporal
facts.

## Related

[[temporal-constraint-taxonomy]] · [[tkgqg-constraint-count-degradation]] · [[constraint-as-information]]

[^c1]: liu-2026-chronoqg — "Each accepted action must update or shrink the candidate set, ensuring that the final answer is determined by the joint effect of hop-bounded subgraph topology and temporal constraints."
[^c2]: liu-2026-chronoqg
[^c3]: liu-2026-chronoqg — "It first constructs a template question from the accepted sampling trace, then rewrites the template into fluent natural language through verifier-guided agentic rewriting. Failed rewrites are repaired or discarded, reducing semantic shift and answer leakage during benchmark construction."
