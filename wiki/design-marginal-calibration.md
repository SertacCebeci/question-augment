---
description: "A predictive distribution is calibrated relative to the design measure over the inputs it will be asked about, a property testable on fresh inputs but not on one realization."
aliases: ["µ-calibration", "design-measure calibration", "calibration under the design measure"]
sources: ["arxiv-2512-05611"]
---
# Design-marginal calibration

A predictive distribution is calibrated only relative to a distribution over the inputs where it will be used. Pion and Vazquez call this µ-calibration. After conditioning on the data, a fresh input X is drawn from a design measure µ, and a predictive family is µ-calibrated when its statements "match the distribution of f (X) under" X ∼ µ.[^c1] The design measure is the thing "which governs how observation points are drawn".[^c2]

Two forms follow. µ-coverage asks how often the true value falls inside a central interval, averaged over X ∼ µ; calibration at level 1 − α means that this frequency equals 1 − α.[^c3] µ-probabilistic calibration asks that the probability integral transform, evaluated at the true value, be uniform: "the PIT values F̂n (f (X) | X) are uniform on [0, 1] under X ∼ µ."[^c4] Both are computed from the predictive CDF at each x, so the mechanism is a change of reference: the target is not the fit at the observed points but the spread of f over the input distribution.

The reason for this reference is testability. A GP posterior at a fixed x has a density that is positive on every open interval, so "a single realization f (x) cannot empirically falsify it."[^c5] The spatial versions "can be estimated and tested on an independent test design, then rejected if they fail."[^c6] The paper also warns that checking on the observation points is not enough: "evaluating KS–PIT on observations using cross-validation can be misleading."[^c7]

What the paper measures. On the Goldstein–Price function, interpolated with a GP with constant mean and Matérn covariance, the maximum-likelihood hyperparameters "achieve low RMSE, consistent with the empirical findings of Petit et al. (2023), but poor calibration."[^c8] Post-processed predictors "improve calibration on the test set without degrading accuracy."[^c9] Both statements come from one benchmark and one kernel family.

Read for asking and answering (my inference, not the work's claim): a stated confidence can be calibrated over the inputs it was checked on and miscalibrated over the inputs that actually arrive. The paper's µ is a design, not a question distribution, so the transfer to questions is mine. The measured version of the same gap for retrieval is in [[real-query-distribution-transfer-failure]].

## Limits

- Calibration is necessary, not sufficient. "µ-probabilistic calibration alone does" not penalize diffuse predictions: "not penalize overly diffuse or uninformative predictive distributions." Sharpness must be scored separately, here with proper scoring rules.[^c10]
- µ-coverage averages over inputs. A region that is badly calibrated can be hidden in the average unless µ puts mass on it; this follows from the definition (my inference, not a tested result here).
- The results are for GP interpolation with exact observations. Figure 1 shows one benchmark function with one mean and kernel; the abstract reports experiments on "benchmark functions", which I did not read in full, so the breadth of the empirical claim is not checked here.
- Whether a real question distribution is close enough to µ for the guarantee to transfer is not addressed; the wiki's extension to questions is untested.

## Related

- [[calibration]] — the general property; this note fixes the reference distribution it is measured against.
- [[conformal-prediction]] — the finite-sample coverage guarantee under exchangeability that the paper adapts to GP interpolation; that guarantee is marginal in the same averaged sense as µ-coverage.
- [[real-query-distribution-transfer-failure]] — a measured case where the inputs a system is tested on differ from the ones it meets in use.

[^c1]: arxiv-2512-05611 — "is said to be µ-calibrated if its predictive statements match the distribution of f (X) under"
[^c2]: arxiv-2512-05611 — "which governs how observation points are drawn"
[^c3]: arxiv-2512-05611 — "Calibration at level 1 − α means δα (F̂n ; µ) = 1 − α."
[^c4]: arxiv-2512-05611 — "that the PIT values F̂n (f (X) | X) are uniform on [0, 1] under X ∼ µ."
[^c5]: arxiv-2512-05611 — "a single realization f (x) cannot empirically falsify it"
[^c6]: arxiv-2512-05611 — "can be estimated and tested on an independent test design, then"
[^c7]: arxiv-2512-05611 — "evaluating KS–PIT on observations using cross-validation can be misleading"
[^c8]: arxiv-2512-05611 — "achieve low RMSE, consistent with the empirical findings of Petit et al. (2023), but poor calibration."
[^c9]: arxiv-2512-05611 — "improve calibration on the test set without degrading accuracy"
[^c10]: arxiv-2512-05611 — "not penalize overly diffuse or uninformative predictive distributions."
