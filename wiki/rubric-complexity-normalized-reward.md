---
description: "A GRPO reward turning per-criterion pass/fail rubric judgments into a continuous score, scaled by a log bonus for rubric size so a harder rubric pays more."
aliases: []
sources: ["arxiv-2606-05174"]
---
# Rubric-complexity-normalized reward

> Satisfying seventeen of eighteen criteria on a hard prompt is a bigger
> achievement than a perfect score on a five-criterion prompt — a reward
> that ignores rubric size cannot tell the two apart.

## Definition / Mechanism

A judge model scores a rubric $C(q) = \{(c_j, w_j)\}$ per completion by
evaluating each criterion **independently**, not the response as a whole:
"Let mk ∈ {0, 1} indicate whether the judge marks criterion ck as present
in the completion." Positive-weighted and negative-weighted criteria
are summed separately into an achieved score and a maximum possible score,
then normalized into a positive fraction $s_{norm}$ and a negative-violation
ratio $\rho$. The two are combined into one effective score before any
nonlinear transform: "ŝ = max(0, snorm − λρ) ," so unsafe or
incomplete completions are pulled toward zero without being forced there,
and partial credit on the positive side survives.

That effective score is then raised to a power and scaled by a term that
grows with the number of criteria $n_c$ relative to the largest rubric
seen in training, $n_{max}$: a logarithmic bonus, not a linear one, so the
size adjustment stays modest next to answer quality. "The Complexity-aware
variant applies a logarithmic bonus that scales with rubric size, so that
high satisfaction on demanding prompts produces a stronger reward signal
and therefore a larger policy gradient." A second, Hybrid variant
instead uses a plain linear base term plus a fixed bonus for exact,
violation-free satisfaction, trading the explicit complexity term for a
simpler shape; both stay continuous (for non-zero within-group reward
variance, which [[certainty-weighted-grpo-reward|GRPO's]] group-relative
advantage needs) and monotone in rubric quality.

Against two fixed-shape baselines from the paper the reward is contrasted
with — a hand-weighted linear sum of per-criterion pass/fail decisions,
and a single holistic Likert judgment over the whole rubric — that neither
adapts to per-prompt rubric size nor preserves criterion-level structure,
the complexity- and size-aware reward produces far larger post-training
gains on a held-out medical-QA benchmark: "Both variants produced only
modest improvements over the Qwen3-14B base model—+9.4% and +13.8%
relative accuracy, respectively far below the +38.7% and +37.6% gains
achieved by the Complexity and Hybrid rewards." The gap is not noise:
"pairwise McNemar tests confirm that both our variance-aware rewards
outperform RaR-Explicit (p < 10−5 ) and RaR-Implicit (p < 10−3 )."[^c5]

## Why it matters

Stall 5 asks how to judge whether an answer actually constrains
the unknown — its adequacy. Rubric-criterion satisfaction is one such
judgment, but a raw satisfaction fraction treats a five-item rubric and an
eighteen-item rubric as the same unit, so a system optimized against it
cannot tell "trivially adequate" from "adequate under real difficulty."
This reward makes the rubric's own size part of what counts as
informative, and shows — against two alternative aggregations of the same
per-criterion judgments — that the size-blind versions are the weaker
training signal, not merely a stylistic choice.

## Limits

- The hyperparameters ($\alpha = 1.2$, $\beta = 0.2$, $\lambda = 0.5$,
  $n_{max} = 25$) are the paper's own "theory-informed design constants,"
  hand-set and not learned or individually ablated against each other —
  only the two full variants (Complexity, Hybrid) are compared end to end.
- Normalization needs $n_{max}$, the largest rubric size seen in the
  training set, fixed in advance; the scheme does not describe what
  happens to a criterion count that exceeds it.
- Evaluated in one clinical domain (heart-focused medical QA against
  HealthBench) with one judge model; the paper itself calls
  generalization to other rubric-based domains future work, not a result.
- The scheme trusts the per-criterion judge's pass/fail call as ground
  truth; nothing here corrects for judge error, only for how the judge's
  binary calls are aggregated into a scalar.

## Related

[[dual-judge-completeness-recall]] · [[certainty-weighted-grpo-reward]] · [[heuristic-grpo-socratic-reward]] · [[cipd-factor-adequacy]] · [[calibration]]

[^c5]: arxiv-2606-05174 — "pairwise McNemar tests confirm that both our variance-aware rewards outperform RaR-Explicit (p < 10−5 ) and RaR-Implicit (p < 10−3 )."
