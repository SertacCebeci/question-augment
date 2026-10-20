---
description: "F-DACE fuses disagreeing causal-effect estimators as fuzzy memberships and applies non-compensatory vetoes to output recommend, do-not-recommend, or mandatory abstention."
aliases: ["F-DACE"]
sources: ["dey-2026"]
---
# F-DACE

> Three causal estimators can each look defensible and still disagree; F-DACE
> refuses to average them into one number and instead asks whether the
> disagreement itself is small enough to act on.

## Definition / Mechanism

Dey (2026) defines F-DACE as a decision layer sitting on three
independent causal estimators (an EconML DML causal forest, a DoWhy backdoor
regression, a two-way-fixed-effects check). It first rejects any component
whose treatment definition, outcome, grain or population does not match the
others' — an **estimand contract** check that runs before fusion. Surviving
components are mapped into fuzzy memberships: precision membership rises
linearly with the effect's standardized magnitude, directional membership is
a normal-CDF transform of the effect-to-error ratio, and validity is the
*minimum* of overlap and refutation membership, so a strong diagnostic cannot
offset a failed one. Pairwise agreement combines standardized effect
proximity, confidence-interval overlap and sign agreement; evidence-weighted
directional support is then multiplied by that agreement score.[^c1]

The decision layer recommends when positive support clears 0.65 and negative
support stays under 0.35 (symmetrically for do-not-recommend), and abstains
whenever mean evidence is below 0.45, agreement is below 0.35, any overlap or
refutation score is below 0.20, or informative estimators disagree in sign —
"a veto prevents compensation: a precise forest cannot override a failed
overlap diagnostic or an informative sign conflict."[^c2]

Across 180 seeded panel simulations spanning six identification conditions,
F-DACE reached a decision in 67.2% of runs and limited false recommendations
to 17.2%, against 33.3% (causal forest alone) and 35.6% (backdoor regression
alone) — matching a deterministic three-estimator unanimity rule rather than
beating it. On a 6,435-store-week Walmart retail panel it abstained on all
five markdown indicators tested, each for a different named reason (an
imprecise estimate, a failed placebo refutation, a direct sign conflict).[^c3]

## Why it matters

F-DACE is a worked instance of turning "these constraints disagree" into a
declared no-decision rather than a silently-picked point estimate — a
stopping judgement (stall 7) made from multiple, possibly conflicting,
sources of evidence rather than from a single posterior.

## Transfer

| | |
|---|---|
| Home field | causal machine learning for retail decision support: CATE estimators, propensity overlap, placebo refutation |
| Here | deciding whether accumulated, possibly disagreeing evidence is enough to commit to an answer at all |
| What survives | graded (fuzzy) membership for separate quality signals instead of one composite score; the non-compensatory veto — one failed check cannot be bought back by others; an explicit third output (abstain) instead of always returning the best point estimate |
| What does not | the specific membership functions and thresholds (calibrated to CATE standard errors and propensity overlap, meaningless outside causal ML); the requirement that fused components share one exact estimand before fusion is attempted at all |

## Limits

- Nearly all (30 of 31) false recommendations in the simulation occurred
  under shared unmeasured confounding — a condition where every component
  estimator shares the same omitted variable, which the paper states "no
  fusion rule can diagnose." The veto mechanism reduces false recommendations
  from disagreement, not from correlated error across all fused sources.[^c4]
- Thresholds (0.65 / 0.35 / 0.45 / 0.35 / 0.20) are hand-declared before the
  retail application and varied only over 0.55–0.75 as a sensitivity check;
  no argument is given that they generalize outside causal panel estimation.
- Evaluated on one synthetic benchmark and one retail dataset; F-DACE matches
  rather than beats simple deterministic unanimity on the reported metric, so
  the fuzzy machinery's advantage over a crisp AND-of-checks rule is not yet
  demonstrated by these numbers alone.

## Related

[[abstention]] · [[status-preserving-verification]] · [[stopping-rules]] · Stopping

[^c1]: dey-2026 — "Validity is the minimum of overlap and refutation membership, so a strong diagnostic cannot compensate for a failed one."
[^c2]: dey-2026 — "A veto prevents compensation: a precise forest cannot override a failed overlap diagnostic or an informative sign conflict."
[^c3]: dey-2026 — "F-DACE made a decision in 67.2% of runs and limited false recommendations to 17.2%; the corresponding rates were 33.3% for the causal forest and 35.6% for backdoor regression, matching deterministic unanimity rather than dominating it."
[^c4]: dey-2026 — "Nearly all (30 of 31) false recommendations occurred under shared unmeasured confounding, which no fusion rule can diagnose when every component shares the omitted variable."
