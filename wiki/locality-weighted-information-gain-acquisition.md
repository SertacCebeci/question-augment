---
description: "For a Bayesian linear surrogate, greedy expected information gain reduces to locality kernel times posterior-variance direction, giving O(d log t) cumulative gain and sample complexity linear in d."
aliases: ["EAGLE acquisition", "Expected Active Gain for Local Explanations", "locality-aware active perturbation selection"]
sources: ["arxiv-2603-14894"]
---
# Locality-weighted information-gain acquisition

When a black box can only be probed by querying it, each query is a question, and the choice of which query to pose can be made by information gain. Chugh, Prasad and Shah (EAGLE) apply this to post-hoc explanation: the explainer fits a Bayesian linear surrogate with coefficients ϕ (the feature importances) from perturbed inputs z near an instance x0 and the black-box's answers y. The next perturbation is the candidate that most reduces the entropy of ϕ, i.e. the largest expected [[expected-information-gain]].[^c1]

## Mechanism

Under a Gaussian linear surrogate, the paper's Theorem 1 shows the greedy single-step criterion collapses, up to constants independent of z, to arg max π_x0(z) · zᵀ V_ϕ z. Here V_ϕ is the posterior covariance of the coefficients and π_x0 is the locality kernel.[^c2] The quadratic term measures how far a candidate lies along directions where the explanation parameters are still uncertain. The kernel term keeps the choice near the instance being explained.[^c3] The loop is simple: seed perturbations, fit, score a candidate pool, take the top batch, query, refit. The paper's experiments use 10 seeds, batches of 10 and a pool of 1000.

The contrast with BayesLIME is the kernel factor. BayesLIME picks by predictive variance alone, and the locality kernel enters only through the weights on already observed points, so its acquisition does not see locality when scoring a new candidate.[^c4] The paper also separates aleatoric from epistemic uncertainty: sampling driven by irreducible noise cannot shrink the surrogate's uncertainty, so the criterion targets the epistemic part, which is what posterior covariance measures (see [[uncertainty-decomposition]]).

## Guarantees

With bounded perturbations and precision updated as V⁻¹ = I + Σ π(z_s) z_s z_sᵀ, the authors prove cumulative information gain grows as O(d log t).[^c5] A high-probability bound on the coefficient error then gives a sufficient number of queries that grows linearly with d, logarithmically in 1/δ, and quadratically in 1/ν (the accuracy tolerance).[^c6] My reading: higher precision is expensive, extra confidence is cheap. This is the same log-determinant structure as [[gaussian-information-gain]], with the same monotone shrinkage of covariance as the mechanism.

Empirically the paper reports better run-to-run reproducibility (Jaccard of top features), neighborhood stability and sample quality than Tilia, US-LIME, GLIME and BayesLIME on tabular and image data.[^c7]

## Limits

- The equivalence in Theorem 1 holds only for the linear Gaussian surrogate and a single greedy step; batch selection takes the top B scores, which ignores redundancy among them (my observation; the paper defers set-level gain to its supplement).
- Guarantees assume the black box is locally linear plus Gaussian noise (ϕ⋆ exists); misspecification of the local model is not covered. Proofs are in the arXiv supplement and I did not read them.
- The sample-complexity statement treats ‖ϕ⋆‖ as a constant and drops constants; it is an order result, not a budget.
- Transfer to asking questions of people is my analogy: a human answerer is not a noisy linear oracle, and nothing here tests that.

## Related

- [[expected-information-gain]] — the general criterion that this specializes
- [[gaussian-information-gain]] — another log-determinant, precision-update account of gain
- [[uncertainty-decomposition]] — the aleatoric/epistemic split motivating the target
- [[bayesian-experimental-design]] — the design framework this is an instance of
- [[query-by-committee]] — a competing active-selection rule based on disagreement

[^c1]: arxiv-2603-14894 — "a post-hoc model-agnostic explanation framework that formulates perturbation selection as an information-theoretic active learning problem."
[^c2]: arxiv-2603-14894 — "arg max AE (z; fe ) = arg max πx0 (z) z⊤ Vϕ z."
[^c3]: arxiv-2603-14894 — "the perturbations that maximize the locality-weighted posterior uncertainty."
[^c4]: arxiv-2603-14894 — "acquisition strategy is not locality-aware when"
[^c5]: arxiv-2603-14894 — "information gain scales as O(d log t), where d is the feature dimension"
[^c6]: arxiv-2603-14894 — "grows linearly with the dimension d, logarithmically with the confidence"
[^c7]: arxiv-2603-14894 — "improves explanation"
