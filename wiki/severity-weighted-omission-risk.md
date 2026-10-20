---
description: "A conformal-calibrated risk score that sums the severity-weighted probability of diseases a diagnostic prediction set still excludes, giving question value a distribution-free coverage guarantee."
aliases: ["severity-weighted omission risk", "calibrated clinical risk"]
sources: ["zhou-2026"]
---
# Severity-weighted omission risk

> A diagnostic question's value is priced by how much clinically severe disease
> mass the current [[conformal-prediction|conformal prediction]] set still excludes — not by how much
> probability mass the set has shed overall.

## Definition / Mechanism

Zhou, Zhou, Zhang et al. (2026) calibrate turn-specific
conformal prediction sets $\Gamma_t=\{y\in\mathcal{Y}: 1-b_t(y)\le\hat q_t\}$
on held-out diagnostic trajectories. The existing methods they build against
"guide information acquisition with predictive uncertainty or label
[[efe-planning-as-variational-inference|ambiguity]], but overlook the asymmetric clinical risk of missing severe
diseases and lack unified long-horizon planning over whether to continue
asking questions or commit to a diagnosis."[^c1]

Their fix reweights the [[calibration]] target by a disease-specific severity
weight before calibrating, so the same split-conformal machinery is spent on
severity-weighted exclusion rather than raw label coverage: the framework
"calibrates turn-specific diagnostic prediction sets and severity-weighted
differential-diagnosis risk on held-out diagnostic trajectories; and
introduces the calibrated clinical risk into Monte Carlo Tree Search to
jointly evaluate long-horizon Ask and Commit trajectories."[^c2]

Across DDXPlus and MediQ and multiple LLMs, using this risk as the value
signal for question selection and stopping lowers diagnostic error on severe
cases without spending more questions: "our method improves Top-1 accuracy
from 92.24% with BED-LLM to 97.76%, while reducing the average number of
questions from 8.46 to 4.80," and "With Llama-3.1-8B-Instruct, for example,
Severe Error decreases from 6.47% with BED-LLM to 0.00% with our method."[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Zhou et al. (2026) | severity-weighted omission risk | exact |
| Zhou et al. (2026) | calibrated clinical risk | exact |

[^c4]

## Why it matters

This gives stall 2 a test-time, calibrated alternative to
[[expected-severity-risk]]'s train-time distilled ranking: instead of a
language policy trained once to reproduce a severity-aware ordering, this
risk is recomputed each turn from a conformal prediction set built on
held-out calibration trajectories, carrying a distribution-free coverage
guarantee the distilled ranking does not state.

## Transfer

| | |
|---|---|
| **In its home field** | split-conformal calibration gives a finite-sample, distribution-free coverage guarantee for one target distribution |
| **Here** | the target distribution is reweighted by clinical severity before calibration, so the guarantee is over severity-weighted exclusion risk rather than raw label coverage |
| **What survives** | the finite-sample, distribution-free guarantee, restated per turn |
| **What does not** | per-patient (conditional) coverage — the guarantee is marginal over the calibration population, not conditional on a given patient's trajectory so far |

## Limits

No archived, locally stored text extract of Zhou et al. (2026)
existed for this cell (the source was harvested but not yet archived); the
quotes above come from a web-rendered read of the arXiv HTML rather than a
fixed local copy, so equation numbering could not be independently
cross-checked. Reported only for domains with a labeled disease-severity
scale (DDXPlus, MediQ); nothing here is claimed for a diagnostic task without
one.

## Related

[[expected-severity-risk]] · [[sequence-level-conformal-prediction]] · [[value-of-information]]

[^c1]: zhou-2026 — "guide information acquisition with predictive uncertainty or label ambiguity, but overlook the asymmetric clinical risk of missing severe diseases and lack unified long-horizon planning over whether to continue asking questions or commit to a diagnosis"
[^c2]: zhou-2026 — "calibrates turn-specific diagnostic prediction sets and severity-weighted differential-diagnosis risk on held-out diagnostic trajectories; and introduces the calibrated clinical risk into Monte Carlo Tree Search to jointly evaluate long-horizon Ask and Commit trajectories"
[^c3]: zhou-2026 — "our method improves Top-1 accuracy from 92.24% with BED-LLM to 97.76%, while reducing the average number of questions from 8.46 to 4.80"
[^c4]: zhou-2026 — "calibrates turn-specific diagnostic prediction sets and severity-weighted differential-diagnosis risk on held-out diagnostic trajectories; and introduces the calibrated clinical risk into Monte Carlo Tree Search"
