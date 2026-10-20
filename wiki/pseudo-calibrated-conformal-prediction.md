---
description: "Calibrating conformal sets on unlabeled shifted data with the model's own labels undercovers by a source ramp loss plus Lipschitz-times-shift; randomizing uncertain ones never lowers coverage."
aliases: ["hard pseudo-calibration", "source-tuned pseudo-calibration", "STPC", "unlabeled-target conformal calibration"]
sources: ["arxiv-2602-14913"]
---
# Pseudo-calibrated conformal prediction under shift

Split [[conformal-prediction]] promises marginal coverage only when calibration and test data are exchangeable. Under shift one may have labeled source data but only unlabeled target inputs. Pseudo-calibration labels the target inputs with the classifier's own prediction and computes the conformal threshold from those scores (arXiv 2602.14913).

## Why hard pseudo-labels undercover

With the score s(x,y) = -gamma_f(x,y), the predicted label has the smallest score at any x, so the pseudo-score distribution has CDF at least that of the true target scores.[^c1] The paper's reading: the thresholds are smaller than oracle calibration, and hence undercoverage can follow under shift.[^c2]

## Guarantee for hard pseudo-calibration

Assume identical label marginals and a bounded label-conditional Wasserstein-infinity shift rho, with scores Lipschitz (constant L_gamma) in x. Then the score distributions are within L_gamma * rho in Wasserstein-1.[^c3] Theorem 1 gives target coverage at least 1 - alpha - L_r(f,P) - L_gamma * rho_mix, where L_r is the classifier's ramp loss on the source.[^c4] In words: coverage loss is controlled by the source ramp loss and the shift magnitude.[^c5] Inflating the threshold by a fixed tau gives a bound with min(L_r, L_h/(1+tau/2)) in place of L_r (Corollary 1). Rho and L_gamma appear only in the bounds; the procedures do not need them.

## Source-tuned variant (STPC)

Keep the pseudo-label where an uncertainty H(x) (for example predictive entropy) is at most u, and replace it with a uniformly random label elsewhere. Since the predicted label minimizes the score, randomization can only raise scores, so thresholds and sets are never smaller than under hard pseudo-calibration. The level u is chosen as the largest grid value for which source coverage, computed with labeled source data, stays at least 1 - alpha.

Theorem 2: coverage of the randomized version is at least that of the hard version, and the lower bound gains a nonnegative "rescued mass" term R_u.[^c6] The result carries over to the data-chosen u because it is picked on an independent source-tuning set.[^c7]

## Measured

On MNIST, CIFAR-10 and CIFAR-100 with a synthetic appearance-plus-Gaussian-noise shift of strength sigma and alpha = 0.2, source and hard pseudo-calibration lose coverage as sigma grows, while the source-tuned version improves it, often approaching the oracle at moderate shifts.[^c8]

## Limits

- The bounds need the Lipschitz and bounded Wasserstein shift assumptions and equal label marginals; with unequal marginals only a total-variation relaxation is mentioned, not worked out.
- The bound is a lower bound that can be loose or clipped to zero; the guarantee is not nominal coverage. STPC's gain is monotone, not guaranteed to reach 1 - alpha.
- STPC trades size for coverage: sets are larger by construction. I did not check the efficiency numbers in the tables.
- Experiments are image classification with synthetic shift, five runs. Nothing is tested on language models or open-ended answers; applying it there is my extrapolation.
- Tuning u uses labeled source data, which is wrong in principle when the shift changes where the classifier is uncertain. The paper does not test that case.

## Related

- [[conformal-prediction]] — the exchangeability guarantee that shift breaks
- [[mondrian-conformal-prediction]] — another way to restore conditional coverage, by stratifying
- [[conformal-set-size-calibration-tradeoff]] — overconfident models get small sets; here, small sets from pseudo-labels are the failure
- [[conformal-abstention]] — sets and abstention from the same score

[^c1]: arxiv-2602-14913 — "Equivalently, the pseudo-score distribution has"
[^c2]: arxiv-2602-14913 — "smaller thresholds than oracle calibration, and hence, it can"
[^c3]: arxiv-2602-14913 — "W1 (s#P, s#Q) ≤ Lγ ρ."
[^c4]: arxiv-2602-14913 — "Theorem 1: Let Assumptions 1 and 2 hold. Let"
[^c5]: arxiv-2602-14913 — "gives coverage guarantees controlled by the source ramp loss"
[^c6]: arxiv-2602-14913 — "Part (i) guarantees that source-tuned coverage is never below"
[^c7]: arxiv-2602-14913 — "using an independent source-tuning set."
[^c8]: arxiv-2602-14913 — "Source and hard pseudo-calibration degrade as σ increases,"
