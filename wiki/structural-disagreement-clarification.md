---
description: "Samples candidate structured specifications, computes symbolic disagreements across their axes, ranks disagreements by split entropy round-robin per axis, and asks the top one as a binary question."
aliases: ["disagreement-driven disambiguation", "structure-aware disambiguation"]
sources: ["arxiv-2604-02382"]
---
# Structural disagreement clarification

> Which clarification question to ask next is read off the concrete points
> where a sampled pool of candidate outputs symbolically disagree, not
> generated freely by an LLM and then scored.

## Definition / Mechanism

Yang et al. (2026) target interactive narrowing of an
underspecified Infrastructure-as-Code (IaC) request toward a hidden target
configuration $c^*$ under a fixed budget of $K$ binary questions. Each
candidate configuration is represented as a structured triple $s=(R,T,A)$ —
resources, dependency topology, and per-resource attributes — "we represent
each configuration as a structured triple s = (R, T, A)". This decomposition
"induces a structured interface that supports more efficient and systematic
intent elicitation by LLM-based agents."[^c1]

At each round, an LLM samples a pool $P$ of $N$ candidates by temperature
sampling; candidates sharing the same resources and topology are
deduplicated. Because every candidate is the same typed triple, disagreement
is computed **symbolically**, not by comparing free text: a resource type,
edge, or attribute value present in some candidates and absent or different
in others. "Each disagreement partitions the pool into the candidates on
either side of the difference."[^c2]

Disagreements are ranked by how evenly they split the pool — "We therefore
rank disagreements by how evenly they divide the candidate pool, measured by
the Shannon entropy of the induced split" — with near-consensus splits dropped
below an entropy floor. Rather than picking the single highest-entropy
disagreement regardless of axis, "the surviving disagreements are ranked
within each axis and then selected across axes in round-robin order,
preventing any single axis from dominating the question budget."[^c3]

An LLM rephrases the top disagreement's structural diff into a yes/no
question a user can answer without seeing the candidates. Because the
partition is already known, "pruning is immediate and deterministic: one
answer can eliminate multiple candidates at once, efficiently narrowing the
pool." "Regeneration is triggered when the pool is exhausted (fewer than
two candidates remain)," conditioned on the full interaction history so far;
the loop ends at budget $K$ or when no structurally distinct candidates
remain.[^c5]

## Why it matters

Against direct question generation, Best-of-N, self-consistency clustering,
and Active Task Disambiguation (ATD, which scores freely generated questions
over a question×solution grid by expected information gain), "structure-aware
disambiguation outperforms all structure-agnostic baselines: across budgets
of K=5, 10, and 15, our method achieves the best Structure score at every
budget," and its margin over ATD holds "while spending 4× our tokens and 11×
our wall-clock per task." An ablation confirms the round-robin step
itself does work: removing it and ranking by raw entropy alone, "we see a
performance drop … suggesting that the round-robin balancing does help with
IaC disambiguation." The result is a **training-free** elicitation
mechanism whose question comes from a computed diff over a typed candidate
space rather than an LLM's free generation-then-scoring of questions —
cheaper because there is no explicit question×solution grid, and targeted
because every question is guaranteed to eliminate candidates.

## Transfer

| | |
|---|---|
| **Home field** | active learning / [[generalized-binary-search]]: rank tests by how evenly they split a version space |
| **Here (structured code/config synthesis)** | the "hypothesis set" is a sampled, deduplicated pool of LLM-generated candidates, not an enumerated space; splits are computed symbolically over a typed triple and coordinated round-robin across three fixed axes |
| **What survives** | the entropy-of-split ranking rule and its rationale (an even split maximizes information from one binary answer) |
| **What does not** | no coverage guarantee over $C(I)$ — the pool is a finite sample, not the full space, and can be regenerated but never enumerated |

## Limits

Evaluated only in simulation: "our evaluation relies on a simulated
protocol: prompts rewritten from verified references and answers from a
reference-grounded oracle" — an LLM proxy that answers strictly from a
reference configuration, not a real user with genuine uncertainty or
inconsistent answers. The three-axis decomposition (resources, topology,
attributes) is specific to IaC's declarative structure; whether it transfers
to other structured-synthesis domains, as the authors themselves speculate,
is untested here.

## Related

[[generalized-binary-search]] · [[expected-information-gain]] · [[active-probing]]

[^c1]: arxiv-2604-02382 — "induces a structured interface that supports more efficient and systematic intent elicitation by LLM-based agents."
[^c2]: arxiv-2604-02382 — "Each disagreement partitions the pool into the candidates on either side of the difference."
[^c3]: arxiv-2604-02382 — "the surviving disagreements are ranked within each axis and then selected across axes in round-robin order, preventing any single axis from dominating the question budget."
[^c5]: arxiv-2604-02382 — "Regeneration is triggered when the pool is exhausted (fewer than two candidates remain)."
