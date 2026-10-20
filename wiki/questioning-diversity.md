---
description: "A question-set diagnostic — average pairwise cosine distance between sentence-embedded questions for one image — used to detect collapse toward redundant, near-duplicate questions."
aliases: ["questioning diversity", "question-set diversity"]
sources: ["liang-2026"]
---
# Questioning diversity

> How redundant is a set of questions generated for the same item? A
> question can pass every per-question quality check and still add
> nothing if it near-duplicates another question already asked.

## Definition / Mechanism

For an item $x$ with a generated question set $Q_x=\{q_1,\dots,q_m\}$, the
metric samples $n$ questions from $Q_x$ (repeated over multiple runs),
encodes each with a sentence-embedding model, $\ell_2$-normalizes the
embeddings $z_i$, and computes the average pairwise cosine similarity
$s_{emb}(Q_x) = \frac{2}{n(n-1)}\sum_{i<j} z_i^\top z_j$; the diversity
score is the corresponding average pairwise cosine *distance*.[^c1]

It is measured at the **question-set level**, not the per-question level,
because a single question cannot be judged redundant or non-redundant in
isolation — only against the other questions asked about the same item.
This is deliberate: perception and reasoning difficulty are scored per
question, but a question can be individually valid and reasoning-oriented
and still provide little additional supervision if it is a near-duplicate
of another question already in the set.[^c2]

## Why it matters

The map's per-step criteria ([[mutual-information|mutual information]], EIG, GBS) score one
candidate question against the current belief and say nothing about
whether a *set* of questions asked in sequence or in parallel keeps
returning to the same axis. This metric is a cheap, model-free proxy for
that failure mode: low embedding-space diversity across a question set is
evidence that selection — however it was made — collapsed onto one region
of the question space rather than one that tracks [[entropy]] reduction
directly.

## Limits

The score depends on the choice of sentence-embedding model and on the
sample size $n$; it measures surface/semantic redundancy in embedding
space, not whether two differently-worded questions target the same axis
of uncertainty or different ones, and it says nothing about whether any
individual question is grounded, answerable, or informative — those are
separate, per-question dimensions in the same protocol. Embedding distance
is a proxy for distinctness, not a computed [[value-of-information|value of information]]; two
questions can be far apart in embedding space while carrying near-zero
mutual information difference, or close together while targeting distinct
axes.

## Related

[[self-evolving-visual-questioner]] · [[mutual-information]] · [[semantic-entropy]] · [[expected-information-gain]]

[^c1]: liang-2026 — "Questioning Diversity is measured at the question-set level because diversity cannot be determined from a single question in isolation. For each image x, we consider the generated question set Qx = {q1 , . . . , qm }."
[^c2]: liang-2026 — "a question can be valid and reasoning-oriented in isolation, yet provide little additional supervision if it is a near-duplicate of other questions for the same image."
