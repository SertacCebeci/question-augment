---
description: "A conformal-calibrated stopping rule for information-seeking agents: retrieval halts once the calibrated lower bound on a self-estimated completeness ratio clears a threshold."
aliases: ["completeness uncertainty quantification", "calibrated stopping criterion", "SeekerGym"]
sources: ["arxiv-2604-17143"]
---
# Calibrated completeness stopping

> Whether to keep retrieving is a different question from whether the last
> retrieval was correct: it asks the agent to score how much of the whole is
> still missing, and to know when that self-score can be trusted.

## Definition / Mechanism

Kim, Lee, Li & Bastani (2026) define, for an
information-seeking agent working through a passage-structured document,
completeness as the fraction of goal passages retrieved so far,
$c=|\text{Retrieved}|/N$. A reliable agent should be able to report not just
what it found but *how much of the document it has not yet covered*:
"completeness uncertainty quantification measures whether the agent
accurately estimate[s] the completeness of the information it has
gathered."[^c1]

At each step the agent is prompted for a point estimate $\hat c$ of the true
ratio. This self-report is systematically biased, so it is passed through
[[conformal-prediction]]: on a held-out calibration set of synthetic belief
states with known true ratios, nonconformity scores $e_i=|c_i-\hat c_i|$ set
an adjustment $\hat q$ (the $\lceil(n+1)(1-\alpha)\rceil/n$ quantile), giving
a prediction interval with a finite-sample coverage guarantee.[^c2]

A stopping rule is then built directly on the calibrated interval's lower
edge rather than on the raw estimate: retrieval continues only while
$\hat c - \hat q < \delta$ for a chosen threshold $\delta$, and halts the
moment the calibrated lower bound clears it — the agent commits to "done"
only when even its worst-case-corrected self-estimate says so.[^c3]

## Why it matters

Stall 10 asks how an answerer expresses residual uncertainty or
decides when to stop. Most of the wiki's stopping and abstention rules
threshold an uncertainty *score about a single answer's correctness*
([[abstention]], [[confidence-interval-calibration]], [[crc-confident-error-control|CRC]]).
This benchmark isolates a different residual-uncertainty object: not "is
this answer right" but "how much of the space I was asked to cover remains
unexplored" — a quantity with its own ground truth (the retrievable
document) independent of any single retrieved passage's accuracy. Two raw
models (GPT-oss-120b, GPT-oss-20b) track it well enough to need little
correction; four of six tested models do not, and all six share a
directional bias in the same place — the failure mode that makes external
calibration, not model self-report alone, the load-bearing part of the
stopping decision.[^c4][^c5]

## Transfer

| | |
|---|---|
| In its home field | Split [[conformal-prediction]]: a calibration set of exchangeable (score, outcome) pairs sets a distribution-free interval on an unknown scalar, most often a prediction's error. |
| Here | The scalar being intervalized is the agent's own self-estimate of *how complete its exploration is*, not a correctness score on a fixed answer, and it is measured against synthetic belief states with a constructed, known true ratio rather than sampled from live trajectories. |
| What survives | The nonconformity-score-and-quantile calibration mechanism; the finite-sample coverage guarantee; using the calibrated interval's edge, not the raw point estimate, to gate a downstream action. |
| What does not | Exchangeability between calibration and deployment: the calibration set is built by uniformly sampling passage subsets offline, while a real agent's retrieval order is sequentially correlated, so the coverage guarantee "holds by construction on the synthetic distribution" but transfer to live trajectories is untested. |

## Limits

- Four of six evaluated models yield **negative** raw $R^2$ against the true
  completeness ratio — worse than predicting the mean — before calibration;
  conformal correction restores the target 90% coverage but only by widening
  the interval for the weaker estimators, so the stopping rule's usefulness
  (a tight $\hat q$) varies sharply by model.[^c4]
- All six models share an early-stage optimism bias, overpredicting
  completeness when the true ratio is near zero — the direction of error a
  premature-stop policy would most need corrected.[^c5]
- The calibration and evaluation both use offline, synthetic belief states
  with uniformly sampled passages; whether the coverage guarantee survives
  the sequential correlation of a live retrieval trajectory, and whether the
  stopping criterion works when estimation errors can compound step over
  step, is explicitly left open by the authors.[^c6]

## Related

[[conformal-prediction]] · [[confidence-interval-calibration]] · [[abstention]] · [[crc-confident-error-control]] · [[calibration]]

[^c1]: arxiv-2604-17143 — "completeness uncertainty quantification measures whether the agent accurately estimate the completeness of the information it has gathered."
[^c2]: arxiv-2604-17143 — "we compute nonconformity scores ei = |ci − ĉi | and set the calibration adjustment q̂ to the ⌈(n + 1)(1 − α)⌉/n quantile, yielding prediction intervals [ĉ − q̂, ĉ + q̂] with coverage guarantee P(c ∈ [ĉ − q̂, ĉ + q̂]) ≥ 1 − α."
[^c3]: arxiv-2604-17143 — "if ĉ − q̂ ≥ δ then 7: break {Calibrated lower bound exceeds threshold}"
[^c4]: arxiv-2604-17143 — "four of six models yield negative R2 values on both corpora, meaning their raw estimates are less accurate than predicting the mean completeness ratio."
[^c5]: arxiv-2604-17143 — "the raw estimates also exhibit a shared early-stage optimism bias: when true completeness ratio is near zero, all models tend to overpredict the completeness ratio."
[^c6]: arxiv-2604-17143 — "calibration transfer to deployment trajectories is an open question. Additionally, while we propose a calibrated stopping criterion (ĉ − q̂ ≥ δ), our experiments evaluate completeness uncertainty quantification offline on fixed belief states; validating adaptive stopping during live exploration, where estimation errors may compound across steps, remains an important direction."
