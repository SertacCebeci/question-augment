---
description: "Rhetorical vs. informational question intent is linearly decodable from an LLM's last-token representation, but different probes recover non-collinear directions."
aliases: ["rhetorical question linear probing", "rhetorical signal heterogeneity"]
sources: ["arxiv-2604-14128"]
---
# Rhetorical intent is linearly readable but not along one direction

> A probe can flag a question as rhetorical with 0.8–0.9 AUROC — but a probe
> trained on one corpus calls a different set of questions "rhetorical" than
> one trained on another, even when both score equally well.

## Definition / Mechanism

**Yao, Anand, Zhuang & Jiang (2026)**: given a[^s1]
decoder-only LLM's last-token hidden state for a question (with
context), three linear probes — a training-free diffMean direction (the
difference of class-conditional means) and two trained discriminative
probes (logistic regression, linear SVM) — are fit to separate rhetorical
questions ("asked not to seek information but to persuade, challenge, or
signal stance") from information-seeking ones, on two social-media
datasets (Twitter **RQ**, Reddit **SRAQ**). Within a dataset, the trained
probes reach AUROC 0.85–0.9 on RQ and 0.8–0.85 on SRAQ.^c1 Trained on one
dataset and applied to the other, AUROC drops only modestly, to
0.7–0.8.^c2

That transfer accuracy does not mean the two datasets' probes found the
same feature. Scored on the same held-out examples, a probe's own ranking
and a transferred probe's ranking agree only moderately (Spearman often
≤0.5 at deep layers), and agreement collapses further at the ranking's
tails: overlap between the two probes' top-ranked (most confidently
rhetorical) examples is often below 0.2 Jaccard.^c3 The directions
themselves are close to orthogonal — cosine similarity 0.2–0.4 between
directions learned on RQ and on SRAQ.^c4

Qualitative inspection of the disagreement shows *why*: the two datasets'
top-ranked-rhetorical sets are drawn from different populations. The
SRAQ-trained direction ranks highest the passages where "rhetorical
questions serve as structural scaffolding for extended arguments" — a
chain of questions each opening a new stage of a discourse-level
argument.^c5 The RQ-trained direction instead ranks highest short,
syntax-driven interrogatives whose rhetorical force is local to one turn,
and — critically — it ranks a genuinely informational example second,
because "it contains genuine requests for clarification ... that the
RQ-derived direction ranks highly because of their surface interrogative
form, not because of any rhetorical intent."^c6

## Why it matters

"Is this question rhetorical" is itself a comprehension judgment — a
reading of intent behind an interrogative surface form, the same kind of
reading a [[question-under-discussion|QUD]] or a [[false-premise-question]]
check performs. This work shows that when that judgment is made linearly
from an LLM's representation, it is not one detector but a family: one
tuned to discourse-level stance-taking, another to local syntactic form.
The two disagree most exactly where it matters — on the examples each
calls most confidently rhetorical — and the syntax-tuned one will misread
a real clarifying question as rhetorical purely from its interrogative
shape. A system that discounts or filters "rhetorical" questions before
answering therefore inherits whichever notion of rhetorical its training
corpus encoded, and can silently drop genuine information-seeking
questions that merely look rhetorical on the surface.

## Limits

The analysis is linear-probing only; it "excludes signals that may be
encoded through nonlinear interactions, alternative activation pathways,
or mechanisms that are not linearly separable."^c7 It covers two
social-media domains with noisy, real-world labels, decoder-only models
only, and treats what is *decodable* from activations, not how a human or
an agent's comprehension process actually forms the rhetorical/
informational judgment. Linear separability is not shown to imply linear
controllability; the paper's own steering check is preliminary.

## Related

- [[question-under-discussion]]
- [[false-premise-question]]
- [[pragmatic-plausibility]]
- [[clarification-request]]

[^s1]: arxiv-2604-14128
