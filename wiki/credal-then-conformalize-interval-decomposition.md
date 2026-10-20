---
description: "Build a credal envelope that widens where data are sparse, then split-conformalize it: interval width splits into aleatoric core, epistemic inflation and a distribution-free calibration slack."
aliases: ["CREDO", "credal-then-conformalize", "conformalized credal envelope", "endpoint-trimmed posterior credal set"]
sources: ["arxiv-2603-06826"]
---
# Credal-then-conformalize interval decomposition

Split conformal intervals have guaranteed marginal coverage but can stay narrow where the predictor is extrapolating, because common regression scores mostly track aleatoric variability.[^c1] Credal sets (sets of plausible predictive distributions) make epistemic uncertainty visible but carry no calibration guarantee.[^c2] CREDO separates the two roles: the credal step decides where the interval should be wide, and the conformal step alone supplies the coverage guarantee.

## Mechanism

1. **Envelope by endpoint trimming.** Draw parameters from a posterior, compute each draw's lower and upper predictive quantiles at x, and take the empirical (γ/2)-quantile of lower endpoints and (1−γ/2)-quantile of upper endpoints. This discards the extreme endpoints and gives the envelope [ℓ(x), u(x)].[^c3]
2. **Data-density-aware trimming.** Replace the fixed γ with γ(x), driven by a kNN-radius scarcity score. Sparse regions get small γ, so less trimming and a wider envelope; dense regions get large γ and a tight one.[^c4] Because γ(x) depends only on covariates, split-conformal validity is untouched.[^c5]
3. **Conformalize.** Calibrate a distance-to-envelope score and widen both ends by τ̂, giving C(x) = [ℓ(x) − τ̂, u(x) + τ̂].

## Decomposition

The final length is the posterior-mean interval length U_A(x) (the aleatoric core), plus the envelope length minus U_A(x) (the epistemic contribution), plus 2τ̂ (the calibration slack).[^c6] This lets one ask, at a given x, why the interval is wide: noise, lack of local evidence, or global miscalibration. The paper's check is that the epistemic share is larger for outliers than for inliers on real datasets, especially in small-data domains.[^c7]

## Guarantees

- The envelope covers at least 1−α0 under every distribution in the credal set.[^c8]
- Posterior predictive mass inside the trimmed envelope is at least (1−γ)(1−α0).[^c9]
- Under exchangeability the conformalized interval has marginal coverage at least 1−α.[^c10]
- Under correct specification and posterior consistency, the envelope converges to the oracle quantiles and τ̂ vanishes.[^c11]

## Limits

- Coverage is marginal, not conditional; the guarantee does not itself say the epistemic part is correctly sized locally.
- The "epistemic" share is only as good as the posterior and the kNN scarcity proxy; it is a diagnostic, not a measured ground truth. The outlier-vs-inlier test is indirect validation (my reading).
- The vanishing-slack result needs correct specification; under misspecification the slack absorbs the error, and the decomposition then mixes misspecification into "calibration slack" (my inference).
- Regression intervals only; no transfer to text-question tasks was tested. Whether the three-way split informs when an agent should ask is my conjecture, not a finding.

## Related

- [[conformal-prediction]] — the calibration layer CREDO sits on
- [[uncertainty-decomposition]] — the aleatoric/epistemic split here is a width decomposition, not an action rule
- [[conformal-set-size-calibration-tradeoff]] — efficiency versus guarantee in conformal sets
- [[credal-concept-bottleneck-decomposition]] — another credal-set decomposition

[^c1]: arxiv-2603-06826 — "widely used regression scores (including residual scores and CQR-style quantile-distance scores) often track primarily aleatoric variability"
[^c2]: arxiv-2603-06826 — "credal prediction sets are typically model-based and thus uncalibrated"
[^c3]: arxiv-2603-06826 — "This discards the γ/2 lowest lower endpoints and the γ/2 highest upper endpoints under the posterior."
[^c4]: arxiv-2603-06826 — "A smaller γ(x) retains more posterior realizations, typically yielding a wider envelope to capture epistemic uncertainty"
[^c5]: arxiv-2603-06826 — "because γ(x) depends only on the covariates X, the split conformal validity of Equation (2) is preserved"
[^c6]: arxiv-2603-06826 — "an interpretable decomposition of the final conformal interval length"
[^c7]: arxiv-2603-06826 — "The uncertainty decomposition successfully attributes a higher proportion of epistemic uncertainty to outliers compared to inliers"
[^c8]: arxiv-2603-06826 — "PF (Y ∈ [ℓ(x), u(x)] | X = x) ≥ 1 − α0 ."
[^c9]: arxiv-2603-06826 — "P(Y ∈ [ℓ(x), u(x)] | X = x, Dtr ) ≥ (1 − γ)(1 − α0 )."
[^c10]: arxiv-2603-06826 — "satisfies the distribution-free guarantee"
[^c11]: arxiv-2603-06826 — "the conformal expansion τ̂ vanishes, and the conditional coverage converges to the nominal level"
