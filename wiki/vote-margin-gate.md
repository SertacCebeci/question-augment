---
description: "An abstention rule that calls only when an LLM-judge panel's vote split exceeds a fixed margin, empirically isolating a higher-accuracy subset of judgments than forced answering."
aliases: ["vote-margin gate", "margin gate", "confident-call-or-abstain"]
sources: ["dooskin-2026"]
---
# Vote-margin gate

> Instead of answering every case, poll a panel and answer only when its
> votes split by more than a fixed margin — treat the panel's own
> disagreement as the abstention signal.

## Definition / Mechanism

Dooskin & Squoosh Technical Staff (2026) run a
counterbalanced 16–20-vote LLM-judge panel (Gemini 3 Flash, multimodal) on
each A/B-test screenshot pair, compute the panel's vote margin (the
fractional split between the majority and minority calls), and gate the
final call on that margin: "Gating predictions on internal panel agreement
concentrates real signal: at a vote-margin ≥ 0.6 gate the judge calls 49%
of tests and abstains on the rest, and on significant-only labels the
called subset reaches κ = 0.311 [0.025, 0.555] — the only operating point
that survives our own label-validity audit."[^c1]

On the trustworthy (statistically significant) half of the labels, the
ungated judge's Cohen's κ is statistically indistinguishable from zero
(0.108, CI crossing 0), while the margin-≥0.6 subset is the only cell in
the paper's whole program whose confidence interval excludes zero: "The
margin-≥ 0.6 row is the finding: the judge's confident calls carry real
signal even on trustworthy labels ... The judge's forced calls (no gate) do
not."[^c2]

A pre-registered held-out confirmation at the *stricter* unanimity gate
(all votes agreeing, not just margin ≥ 0.6) returned κ = −0.100
[−0.200, 0.000] on an underpowered 33-call cohort — by the paper's own
locked decision rule this "upgrades nothing and kills nothing," reported as
INCONCLUSIVE rather than confirmed.[^c3]

Vote-subsampling from the recorded 16–20-vote tallies shows the gate's
operating point survives panel-size reduction: a 9-vote panel at the same
margin ≥ 0.6 threshold reaches 46.1% coverage and κ = 0.271
(significant-only) versus 49.4%/0.311 for the full panel, "at roughly half
the full panel's inference cost."[^c4]

## Why it matters

This is a concrete instance of the $(f,g)$ selective-prediction pair from
[[abstention]]: $g$ is built entirely from the panel's own internal split,
with no labelled validation set and no named cost of rejection — a cheaper
uncertainty score than the learned ones [[abstention]] requires, usable
wherever the answerer is already a panel of independent-seeming votes.

## Limits

- Coverage replicated out-of-sample at one operating point (27.8% →
  30.3% at the unanimity gate) but the *precision* of the confident subset
  did not: the held-out confirmation at unanimity came back inconclusive,
  not confirmed, on an underpowered cohort. The margin-≥0.6 result itself
  has not had its own held-out confirmation reported in this paper — it is
  "the only operating point that survives" a label-validity audit, not a
  pre-registered replication.[^c5]
- The gate's apparent [[calibration|reliability]] is a known trap the paper names directly:
  the unanimous calls reproduced 31/31 across independent runs while
  scoring κ = −0.100 against ground truth on the held-out cohort —
  reproducibility of the gate's output is not evidence that the gated
  subset is accurate (see [[effective-independent-votes]]).[^c6]
- Demonstrated on one task (screenshot-based A/B-test winner prediction),
  one judge family (Gemini 3 Flash/Pro with two prompt variants), and one
  proprietary corpus; the threshold 0.6 was one of four examined, so a
  selection effect on the threshold itself is not excluded by the paper.

## Related

[[abstention]] · [[effective-independent-votes]] · [[calibration]]

[^c1]: dooskin-2026
[^c2]: dooskin-2026 — "The margin-≥ 0.6 row is the finding: the judge’s confident calls carry real signal even on trustworthy labels — the only cell in this research program where a significant-only CI excludes zero. The judge’s forced calls (no gate) do not."
[^c3]: dooskin-2026 — "κ = −0.100 [−0.200, 0.000] on an underpowered 33-call cohort, which by our locked decision rule upgrades nothing and kills nothing"
[^c4]: dooskin-2026 — "A 9-vote panel preserves the gated operating point within its uncertainty band at roughly half the full panel’s inference cost"
[^c5]: dooskin-2026 — "the threshold is one of four examined (selection effect possible)"
[^c6]: dooskin-2026 — "the gated calls are perfectly reproducible across independent runs (31/31) — which we show is exactly why reproducibility must never be mistaken for validity"
