---
description: "In fixed-confidence best-arm identification under EVaR, the sample-size constant is a sup-min of KL projections onto the EVaR-feasible sets, and a Track-and-Stop rule matches it asymptotically."
aliases: ["characteristic time T(mu)", "risk-aware characteristic time", "KL-projection lower bound for risk-averse best-arm identification"]
sources: ["doi-10-48550-arxiv-2510-04728"]
---
# Risk-aware characteristic time

In fixed-confidence best-arm identification, a δ-correct algorithm must spend at least a number of samples that grows like a constant times log(1/δ), and the constant is a property of the instance. Garivier and Kaufmann's lower bound writes it as a supremum over sampling proportions t in the probability simplex of an infimum over alternative instances of Σ t_a KL(µ_a, ν_a), and its inverse is the characteristic time T(µ).[^c1] Ahmadipour and Garivier keep this structure for the best arm under EVaR: the general lower bound "remains the same in the general form".[^c1] What changes is the divergence inside the infimum, because an alternative instance must now change which arm has the lowest EVaR, not which arm has the highest mean.

The divergence is a KL projection with a feasibility constraint on EVaR. The paper defines two of them: KL^U_inf(η, ν), the smallest KL from η to a distribution whose EVaR is at least ν, and KL^L_inf(η, ν), the smallest KL from η to a distribution whose EVaR is at most ν.[^c2] These are asymmetric, and the paper gives separate analyses for the two forms. Under the assumption that arm 1 is the best arm, the constant reduces to a supremum over t of a minimum over the other arms j of an infimum over a common threshold x: the two arms are moved, at cost t_1 KL^U and t_j KL^L, until they reach the same EVaR level, and "the minimum achieves at a common point for the two terms".[^c3]

The two projections differ in convexity, and this is what makes the constant harder to compute. KL^U is a convex program: its constraint is a superlevel set of the EVaR functional, which is convex. KL^L is generally nonconvex, since its constraint is "a sublevel set of a concave functional, which is generally nonconvex".[^c4] The paper computes KL^U through a dual with an auxiliary measure Q, and it computes KL^L as a one-dimensional search over z with a convex inner projection in each step. The source says the latter "remains computationally tractable in practice".[^c5]

The algorithm that matches the bound is a Track-and-Stop design with C-tracking of the oracle proportions and a generalized likelihood-ratio stopping statistic built from these projections, evaluated on the empirical distributions at each round.[^c6] The paper's claim is that the procedure is δ-correct and asymptotically optimal: "the sampling proportions converge to the oracle set", which yields "δ-correctness and asymptotic optimality".[^c6] Its abstract puts the result this way: the algorithm is "δ-correct" and the lower bound "we prove is asymptotically matched".[^c7] The stopping statistic has the same shape as the plug-in likelihood-ratio rules in [[plug-in-glr-stopping-rule]], with the Gaussian divergence replaced by the EVaR-tailored KL projections.

## Limits

The matching is asymptotic. The result is stated as a limit as δ → 0 of the expected stopping time divided by log(1/δ); it does not give a finite-sample sample complexity in the text I read. The extracted text of the main theorem is garbled, so I rely on the abstract and conclusion for its exact form and do not reproduce its inequality.

No experiments appear in the text I read. The practicality claim for KL^L rests on the phrase "tractable in practice" and on the structure of the computation, not on a timed benchmark. The set of optimal proportions can be non-unique, and the paper handles this with upper hemicontinuity of the argmax correspondence, which gives stability of the oracle weights, not uniqueness or a convergence rate.

The analysis assumes rewards bounded in [0, 1], a nonparametric class, and K ≥ 2 arms with one fixed risk level α. The characteristic time is therefore defined for a single α; the text does not give a family over α or a unified constant across risk measures. The conclusion names that unified treatment as an open direction, not as a result: "developing a unified framework that treats coherent risks under a single universal constraint class".[^c8]

Exact identification of the best EVaR arm is a different target from the epsilon-optimal PAC problem. The PAC bound in [[pac-best-arm-sample-complexity-lower-bound]] is about an epsilon-good arm with a 1/eps² constant; this constant is about the exact best arm and scales with log(1/δ). The two should not be read as the same bound.

## Related

- [[entropic-value-at-risk]] — the risk measure whose KL projections define this constant
- [[plug-in-glr-stopping-rule]] — another plug-in likelihood-ratio stopping rule; same shape, different divergence (my inference on the shared structure)
- [[pac-best-arm-sample-complexity-lower-bound]] — a distinct best-arm target with a distinct constant; not the same bound
- [[multi-fidelity-cost-complexity-lower-bound]] — the same sup-min game shape with cost-weighted rather than risk-weighted divergences; the two constants are not the same object (my inference from the shape)

[^c1]: doi-10-48550-arxiv-2510-04728 — "remains the same in the general form"
[^c2]: doi-10-48550-arxiv-2510-04728 — "are asymmetric and require separate analyses for the upper and lower forms"
[^c3]: doi-10-48550-arxiv-2510-04728 — "achieves at a common point for the two terms"
[^c4]: doi-10-48550-arxiv-2510-04728 — "a sublevel set of a concave functional, which is generally nonconvex"
[^c5]: doi-10-48550-arxiv-2510-04728 — "it remains computationally tractable in practice"
[^c6]: doi-10-48550-arxiv-2510-04728 — "the sampling proportions converge to the oracle set"
[^c7]: doi-10-48550-arxiv-2510-04728 — "which we prove is asymptotically matched"
[^c8]: doi-10-48550-arxiv-2510-04728 — "developing a unified framework that treats coherent risks under a single universal constraint class"
