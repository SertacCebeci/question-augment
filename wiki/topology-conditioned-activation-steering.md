---
description: "Building a steering vector from a query's topology-nearest labelled examples, instead of averaging over all examples, raises source-aware clarification or abstention over a direct guess."
aliases: ["topology-conditioned local steering", "H0 topology-local steering"]
sources: ["jiang-2026"]
---
# Topology-conditioned activation steering

> A steering vector built from *this question's* nearest neighbours in
> topology space, not one fixed direction for every question, moves a model
> from answering directly toward source-aware clarification or [[abstention]].

## Definition / Mechanism

Jiang, Tang, Imani & Lan (2026) replace a single global
contrastive steering direction with a query-specific one. For a test
question $q$, its standardized [[persistent-homology-ill-posedness-detection|topology vector]]
is used to retrieve $k$ nearest neighbours from a pool of
ill-posedness-aware responses ($D^+$) and a pool of direct-answer responses
($D^-$); the local steering vector is the difference of their mean-pooled
hidden states at a chosen layer. "We instead retrieve behaviorally matched
examples in topology space and construct a local activation-space
direction." This vector is added to the hidden state at the intervention
layer at every prefill token and at each decoding step: "We then add this
vector to the hidden states at layer l⋆ ... and during decoding we apply
the same update to the current generated-token hidden state at layer l⋆."[^c1]

Averaged across nine dataset–model settings (three datasets × three
open-weight models), this raises acceptable-response rates over a global
full-vector baseline that averages the contrast over all labelled examples
instead of retrieving topology neighbours: "topology-conditioned steering
improves grounded acceptance from 11.9% to 16.4% and total acceptance from
61.4% to 70.6%."[^c2]

## Why it matters

The mechanism gives the answerer a way to act on stall 10 (commit vs. ask)
that is conditioned on *why* a question is unresolved — its own
ill-posedness signature selects the contrast pairs — rather than one
generic refusal direction applied to every unresolved question alike.

## Transfer

| | |
|---|---|
| In its home field | representation engineering / contrastive activation steering: a single global direction between behaviourally labelled example sets, added to the residual stream |
| Here | the direction is rebuilt per query from topology-nearest examples, aimed at the answerer's commit/abstain/clarify decision |
| What survives | the additive steering-vector-at-a-layer mechanism itself, and retrieval-conditioned (rather than one-size) contrast construction |
| What does not | validation beyond three 7–8B open-weight models; the fixed intervention layer ($l^\star=14$) and steering strength were not tuned per model on a held-out split in what this extract reports |

## Limits

- Requires a pre-existing labelled pool of ill-posedness-aware ($D^+$) and
  direct-answer ($D^-$) responses and precomputed topology descriptors
  before any intervention — not usable zero-shot on a new model.
- Judged by an LLM-graded grounded/generic/total-acceptable rubric, not a
  factual-correctness or human-preference metric, so the reported gains
  reflect that rubric.
- One fixed intervention layer and strength across all evaluated models and
  datasets in the reported main results.

## Related

[[persistent-homology-ill-posedness-detection]] · [[gated-activation-steering-for-abstention]] · [[abstention]] · [[semantic-entropy]]

[^c1]: jiang-2026 — "We instead retrieve behaviorally matched examples in topology space and construct a local activation-space direction."
[^c2]: jiang-2026 — "topology-conditioned steering improves grounded acceptance from 11.9% to 16.4% and total acceptance from 61.4% to 70.6%."
