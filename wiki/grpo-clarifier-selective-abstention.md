---
description: "A GRPO-trained clarifier rewarded on parser feedback learns to abstain from rewriting, cutting regressions up to 37% as one fixed dataset-level regime, not per-instance selectivity."
aliases: []
sources: ["liu-2026-beyond"]
---
# GRPO clarifier selective abstention

> Reward a rewriter on whether the rewrite helps a downstream model, and it
> may learn to stop rewriting — but only as one policy for the whole
> dataset, not a decision made case by case.

## Definition / Mechanism

Liu et al. (2026) train a last-utterance clarifier with
GRPO against a frozen discourse parser's own prediction accuracy as reward,
without supervised clarification labels. On one of three datasets this
produces a large regression drop through learned [[abstention]] rather than
better rewrites: "the learned policy improves Link+Rel F1 over the L6-FREE
baseline while substantially reducing regressions (38 → 24, -37%) ...
Notably, this gain comes not from better rewrites — repairs decrease (17 to
7) — but from avoiding harmful ones. RL therefore discovers a conservative
regime where doing less is better."[^c1]

The learned intervention rate does not generalise across datasets as one
policy: "conservative abstention on STAC, near-universal rewriting on
Molweni, and unstable behavior on MSDC ... This variation suggests that the
learning signal shapes how often to intervene, but not yet when to
intervene at the instance level."[^c2]

Grouping baseline-wrong examples by an independent repairability estimate
(best-of-8 sampling) confirms the policy tracks dataset-level rate, not
per-case difficulty: it "rarely repairs examples deemed not repairable by
the candidate rewrites (<2% across datasets), while repair rates increase
substantially with estimated difficulty" — the RL policy's edit rate stays
"near the 23.0% base rate across all four [repairability] buckets,
confirming global abstention rather than per-instance selectivity."[^c3]

## Why it matters

This is a trained instance of the same asymmetry [[selection-abstention-asymmetry]]
names architecturally: an intervention policy optimized only on aggregate
downstream reward converges to a single dataset-wide rewrite-or-abstain
rate rather than to a function of the individual case's repairability, even
though a case-level repairability signal (the best-of-8 estimate) exists
and correlates with where the policy actually succeeds. On stall 2, a
reward that only scores whether asking helped on average, without an
explicit per-instance signal, will not train per-instance selection even
when one is learnable in principle.

## Limits

- Observed on one clarifier size (Qwen3-8B skeleton), one RL algorithm
  (GRPO with a format + parser-accuracy reward), and three SDRT datasets;
  the paper attributes the dataset-level (not instance-level) convergence
  to the reward's aggregate credit assignment but does not test a
  per-instance-shaped reward to isolate the cause.[^c4]
- The 37% regression reduction is reported for STAC only; on Molweni
  regressions fall from 128 to 113 with F1 below baseline, and on MSDC
  regressions rise (105 → 125) — "abstention" here names STAC's regime
  specifically, not a universal effect of this training recipe.[^c5]

## Related

[[abstention]] · [[selection-abstention-asymmetry]] · [[rewriting-repairability-ceiling]] · [[value-of-information]]

[^c1]: liu-2026-beyond
[^c2]: liu-2026-beyond
[^c3]: liu-2026-beyond — "rarely repairs examples deemed not repairable by the candidate rewrites (<2% across datasets), while repair rates increase substantially with estimated difficulty"
[^c4]: liu-2026-beyond — "This variation suggests that the learning signal shapes how often to intervene, but not yet when to intervene at the instance level."
[^c5]: liu-2026-beyond
