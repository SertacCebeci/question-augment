---
description: "A sampling rule is stable when its sample covariance settles to a deterministic limit; then adaptively sampled estimates are asymptotically normal, with Wald intervals at a slower rate."
aliases: ["stability condition", "Lai-Wei stability", "stable sample covariance", "deterministic-limit stability", "stability for adaptive inference"]
sources: ["arxiv-2512-00222"]
---
# Adaptive-design stability

Data gathered by a rule that looks at its own past are not i.i.d., and the tools built for i.i.d. data can fail on them. The paper's opening states the problem: "benign adaptive sampling schemes can introduce severe biases, rendering traditional statistical inference".[^s1] Stability is the condition that restores a limit theorem. A sequence of sample covariance matrices Λ_T is stable when there is a sequence of deterministic positive definite matrices Σ_T with Σ_T^{-1} Λ_T → I_d; the paper's definition is phrased as Λ_T "admits a deterministic limit".[^s2] Once the design has a fixed normalization, the estimate can be asymptotically normal, and the abstract puts the condition as: "if the rate at which an algorithm takes actions converges to a deterministic limit, one can expect that certain parameters are asymptotically normal."[^s3]

The reason a fixed normalization is needed: under adaptive sampling the terminal design is random and depends on the history, so "its spectrum can vary across runs", and a single deterministic normalization under which the error has a normal limit may not exist.[^s4] Stability is the assumption that removes this run-to-run variation in the design's spectrum. The paper notes the object that must stabilize differs by setting. In the multi-armed bandit case it is the arm pull rates; in the adaptive linear regression of Lai and Wei it is the sample covariance matrix. Lai and Wei also showed that asymptotic normality "can fail in the absence of this stability property."[^s5]

The paper's contribution is to show that LinUCB, a UCB-type method for linear bandits,[^s6] is stable in this sense. Its non-leading eigenvalues of the cumulative covariance are shown to "converge to a deterministic limit".[^s7] Under unit-ball actions and sub-Gaussian noise, the error projected onto the orthogonal complement of the true parameter satisfies a central limit theorem with isotropic limiting covariance, after a rescaling. This gives Wald-type confidence sets that, the paper says, "do not depend on the feature covariance matrix and are asymptotically tighter than existing nonasymptotic" sets.[^s8] The gain in tightness is the usual one for a limit theorem: "if asymptotic normality holds, one can construct substantially tighter confidence sets than those derived from concentration inequalities."[^s9]

Stability depends on how much the policy explores. The exploration weight β has a window: "if β is too small, the policy chases noise, the design fails to stabilize, and the estimator cannot achieve" a clean limit; "if β is too large, the policy over-explores, dispersing samples" and slowing the concentration toward the limit.[^s10] The price of adaptivity is a slower rate: "with T observations, the estimator concentrates at Op (T −1/4 ), in contrast to the Op (T −1/2 ) rate" of the i.i.d. setting.[^s11] So a Wald interval built on stable adaptive data is valid but wider than its i.i.d. counterpart at the same sample size.

## Limits

- The result is for one setting: the action set is the unit ball and the true parameter lies on the unit sphere. The paper says so directly: "However, our results pertain to the case where the action set is the unit ball."[^s12] For finite action sets the result "depend[s] on whether these action sets ensure good coverage"; that case is illustrated by a movie-recommendation experiment and left as future work.[^s13]
- Only the terminal estimator's asymptotic normality is shown; Berry-Esseen rates of convergence to the limit are listed as an open direction.[^s14]
- The sub-Gaussian noise assumption is described as "crucial" for asymptotic normality under adaptive sampling; for nonadaptive algorithms the paper says weaker conditions suffice.[^s15]
- The confidence sets are spherical and their diameter is deterministic only "modulo randomness in the variance estimate".[^s16] The empirical check is a simulation study; the abstract says only that "numerical simulations corroborate our findings."[^s17]
- The stability that is proved is for LinUCB. Whether other adaptive rules are stable is not shown here. The paper's introduction reports that for Thompson sampling stability fails "unless the posterior variance is inflated by a logarithmic factor".[^s18]
- Nothing here bears on asking or answering questions with language models. The transfer to that setting is my inference, and the work does not test it.

## Related

- [[upper-confidence-bound-index]] — the index policy whose stability in the multi-armed case the paper builds on; LinUCB is its linear-bandit form.
- [[thompson-sampling]] — a posterior-sampling rule that, by the paper's report, is not stable without an inflated posterior variance.
- [[reference-drift-decomposition]] — the same kind of result for running averages: stabilization reduces to convergence of a predictable drift.
- [[multi-armed-testing-by-betting]] — validity under adaptive allocation obtained without a limit theorem, through e-processes.

[^s1]: arxiv-2512-00222 — "benign adaptive sampling schemes can introduce severe biases, rendering traditional statistical inference"
[^s2]: arxiv-2512-00222 — "admits a deterministic limit"
[^s3]: arxiv-2512-00222 — "which an algorithm takes actions converges to a deterministic limit, one can expect that certain parameters are asymptotically normal."
[^s4]: arxiv-2512-00222 — "its spectrum can vary across runs"
[^s5]: arxiv-2512-00222 — "can fail in the absence of this stability property."
[^s6]: arxiv-2512-00222 — "a canonical UCB-type method tailored to linear bandits"
[^s7]: arxiv-2512-00222 — "the non-leading eigenvalues and show that they converge to a deterministic limit."
[^s8]: arxiv-2512-00222 — "not depend on the feature covariance matrix and are asymptotically tighter than existing nonasymptotic"
[^s9]: arxiv-2512-00222 — "if asymptotic normality holds, one can construct substantially tighter confidence sets than those"
[^s10]: arxiv-2512-00222 — "if β is too small, the policy chases noise, the design fails to stabilize, and the estimator cannot achieve"
[^s11]: arxiv-2512-00222 — "with T observations, the estimator concentrates at Op (T −1/4 ), in contrast to the Op (T −1/2 ) rate"
[^s12]: arxiv-2512-00222 — "However, our results pertain to the case where the action set is the unit ball."
[^s13]: arxiv-2512-00222 — "depend on whether these action sets ensure good coverage"
[^s14]: arxiv-2512-00222 — "Berry-Esseen bounds characterizing distributional rates of convergence to the asymptotic distribution"
[^s15]: arxiv-2512-00222 — "for nonadaptive algorithms, asymptotic normality often follows from much weaker conditions"
[^s16]: arxiv-2512-00222 — "modulo randomness in the variance estimate"
[^s17]: arxiv-2512-00222 — "Numerical simulations corroborate our findings."
[^s18]: arxiv-2512-00222 — "unless the posterior variance is inflated by a logarithmic factor (Halder et al., 2025)."
