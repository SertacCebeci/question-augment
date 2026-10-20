---
description: "A relative vote-share test added to an absolute self-consistency band, screening out self-play questions whose top two pseudo-label votes are too close before they enter training."
aliases: ["double-confidence filtering"]
sources: ["wei-2026-diagevo"]
---
# Double-confidence filtering

> A generated question with no ground-truth answer is kept for training
> only if its solver-vote pseudo-label is both moderately hard to reach and
> unambiguous once reached — one absolute test, one relative test.

## Mechanism

Wei et al. (2026) sample $N$ solver responses to each
candidate question $x$; the majority answer becomes the pseudo-label
$\hat y(x)$, with $p_1(x)$ its vote share and $p_2(x)$ the second most
common answer's share. "We call a question high-conflict when its two
leading answers receive similar vote shares. Its majority pseudo-label can
change across response samples. Training on this unstable pseudo-label can
reinforce errors across rounds. DiagEvo therefore adds a relative
confidence constraint that compares the two leading vote shares. The
absolute and relative confidence constraints together form
double-confidence filtering."[^c1]

The retained training set is defined by both constraints together: "We
retain questions that satisfy both confidence constraints: $D_{train} =
\{x \mid p_{low} \le p(x) \le p_{high}, p_1(x) \ge \tau \cdot p_2(x)\}$."[^c2]

## Why it matters

This is a filter on whether a self-generated question's answer counts as a
usable constraint at all (stall 7's question in miniature, applied at
training-set-construction time rather than at asking time): an
intermediate-difficulty band alone accepts a question whose top two
candidate answers are nearly tied, and training on that unstable majority
can "reinforce errors across rounds" — the relative test catches exactly
that case. The paper's ablations credit part of DiagEvo's overall gain to
this filter jointly with its curriculum memory: "Ablations show that the
[[hierarchical-error-cause-memory|hierarchical error-cause memory]] and double-confidence filtering both
contribute to these gains."[^c3]

## Limits

- The self-consistency score $p(x)=p_1(x)$ is computed from the solver's
  own sampled votes, not from an external check — a solver that is
  confidently and consistently wrong passes the filter unflagged.
- The thresholds $p_{low}, p_{high}, \tau$ are fixed hyperparameters in the
  reported runs; no sensitivity analysis of the filter's cutoffs was read
  for this note.
- Reported only inside the DiagEvo pipeline (Qwen3-4B/8B, OctoThinker-8B
  solvers); no ablation isolating double-confidence filtering from the
  memory mechanism was read in the slices examined.

## Related

[[hierarchical-error-cause-memory]] · [[investigative-question-grpo-training]]

[^c1]: wei-2026-diagevo — "We call a question high-conflict when its two leading answers receive similar vote shares. Its majority pseudo-label can change across response samples. Training on this unstable pseudo-label can reinforce errors across rounds. DiagEvo therefore adds a relative confidence constraint that compares the two leading vote shares. The absolute and relative confidence constraints together form double-confidence filtering."
[^c2]: wei-2026-diagevo
[^c3]: wei-2026-diagevo — "Ablations show that the hierarchical error-cause memory and double-confidence filtering both contribute to these gains."
