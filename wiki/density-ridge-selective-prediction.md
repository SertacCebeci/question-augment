---
description: "A density-ridge distance score over hidden-state trajectory curvature gives a label-scarce abstention threshold, beating semantic entropy and log-probability by 5-20 AUROC points."
aliases: ["density ridge score", "ridge-based selective prediction", "response-manifold detector", "SCMS ridge proximity score"]
sources: ["shamsi-2026"]
---
# Density-ridge selective prediction

> A confidence score for abstaining that needs no dense label set: fit the
> 1-D density ridge of correct generations' hidden-state kinematics, then
> score a new generation by how far it sits from that ridge.

## Definition / Mechanism

Shamsi (2026) maps each sampled completion to a six-dimensional
kinematic feature vector — mean and peak curvature, displacement linearity,
mean and peak per-step displacement, and the normalized argmax of curvature —
computed from the final-layer hidden-state trajectory of the generation. On
the correct-only training subset it fits a Gaussian KDE in this 6-D space
and extracts the 1-D density ridge (the subspace-constrained mean-shift,
SCMS, fixed points where the log-density gradient lies in the top
eigendirection and the next eigenvalue is negative), sampled as a graph of
vertices via one of three chart constructions (global LTSA, geodesic
arclength, or a stitched local-chart atlas). A test generation is scored by
the negated Euclidean distance from its projected feature point to the
nearest ridge vertex, yielding a low-dimensional geometric skeleton of the
stochastic output distribution.[^c1]

## Why it matters

Under a deliberately label-scarce [[calibration]] protocol across eight text
and vision-language models and six QA/VQA benchmarks, the ridge score is
the most performant predictor by AUROC, AURC, PRR and AUGRC on every tested
(model, dataset) cell: on every cell the ridge variant improves AUROC over
the strongest non-ridge competitor (calibrated sequence log-probability) by
5–20 points absolute and concurrently reduces AURC and AUGRC, while
[[semantic-entropy|Semantic Entropy]] and topological baselines are markedly less stable.[^c2]

An ablation across eleven SCMS kernel configurations and three naive
embedding-geometry baselines (PC1, kNN, Mahalanobis) found every SCMS
variant outranks all three naive baselines (mean ranks ≥ 11), which the
paper reads as evidence that the ridge structure itself, not generic
embedding distance, is what separates correct from hallucinated
generations.[^c3]

[[abstention|Selective prediction]] abstains when a confidence score falls below a
threshold; this wiki reads a threshold-crossing score of this kind as a
concrete, named trigger for the stopping stall — whether
the [[conditional-entropy|remaining uncertainty]] over a generation is small enough to accept —
computed without the dense labelled calibration set semantic-entropy and
probe-based scores need.[^c4]

## Transfer

| | |
|---|---|
| Home field | nonparametric statistics / manifold learning: density-ridge estimation (Ozertem & Erdogmus 2011; Genovese et al. 2014) — SCMS finds the 1-D ridge of a density under stated regularity conditions on the density and bandwidth |
| Here | scoring LLM/VLM generations for selective prediction: the "density" is a KDE over a 6-D curvature feature map of hidden-state trajectories, fit on a label-scarce correct-only calibration set |
| What survives | the SCMS ridge-finding procedure, intrinsic-dimension verification (TwoNN) supporting the 1-D clamp, and distance-to-ridge as an out-of-distribution-style score |
| What does not | the estimator's stated convergence-rate guarantee — reported as the ridge estimator's known regularity result, not re-derived or tested against the LLM feature distribution's actual density and sample size |

## Limits

- The head-to-head comparison is restricted to cells common to all
  detectors.[^c5]
- The supervised projection front-end requires both-class labels at fit
  time, so "label-scarce" means few labels, not zero.[^c6]
- Calibration uses $n_{cal}=200$ queries with $N=5$ generations each (test
  size 60); the ridge advantage's dependence on this specific scarcity
  level is untested at other calibration sizes.[^c7]
- Semantic Entropy is reported at chance on closed-form slices, which the
  paper attributes to an expected degeneracy under data and label scarcity
  rather than to a general property of semantic entropy — the 5–20 point
  gap should not be read as a claim about semantic entropy's ceiling
  outside this protocol.[^c8]

## Related

[[abstention]] · [[semantic-entropy]] · [[calibration]] · Stopping

[^c1]: shamsi-2026 — "A test generation is scored by the negated Euclidean distance from its projected feature point to the nearest ridge vertex, yielding a low-dimensional geometric skeleton of the stochastic output distribution."
[^c2]: shamsi-2026 — "Yet on every cell the ridge variant improves AUROC by 5–20 points absolute and concurrently reduces AURC and AUGRC."
[^c3]: shamsi-2026 — "every SCMS variant outranks all three naive baselines (mean ranks ≥ 11). The ridge structure, not generic embedding distance, is what separates correct from hallucinated generations."
[^c4]: shamsi-2026 — "Selective prediction abstains when a confidence score falls below a threshold."
[^c5]: shamsi-2026 — "The head-to-head comparison is restricted to cells common to all detectors."
[^c6]: shamsi-2026 — "The supervised projection front-end requires both-class labels at fit time."
[^c7]: shamsi-2026 — "calibration uses ncal = 200 queries with N = 5 generations each (test size is 60)"
[^c8]: shamsi-2026 — "Semantic Entropy is at chance on closedform slices, which is an expected degeneracy under data and label scarcity."
