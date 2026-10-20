---
description: "Entropic Value-at-Risk is the tightest Chernoff-style bound on CVaR; its exponential-moment infimum equals a worst case over a KL ball whose radius the level alone sets."
aliases: ["EVaR", "entropic value at risk"]
sources: ["doi-10-48550-arxiv-2510-04728"]
---
# Entropic Value-at-Risk (EVaR)

EVaR is a risk measure for a loss or reward distribution at a tail level α. Its primary definition is through the moment-generating function: EVaR is the infimum over z > 0 of (1/z) log E[e^{zX}] + ρ/z, with ρ := −log(1−α).[^c1] The authors call it "the tightest Chernoff-style bound on (C)VaR", and they state that it "serves as the tightest coherent upper bound on Conditional Value-at-Risk (CVaR)".[^c2] Because the infimum sits over z, the measure is a nested optimization: the source says the difficulty lies in "the nested infimum over z".[^c3]

The second definition is distributionally robust. EVaR at level α equals the supremum of E_Q[X] over measures Q absolutely continuous with respect to P whose KL divergence from P is at most ρ.[^c4] This is the point where EVaR differs from its close relative, the entropic risk measure ERM_z, which fixes a risk parameter z and so applies a soft penalty on the KL divergence. In the authors' words, "EVaR uses a hard constraint on the KL-divergence", and the level α alone sets the radius of the uncertainty set.[^c5] A larger z in ERM gives more adversarial Q and a more conservative estimate; in EVaR the z is an internal variable optimized away, so one number, α, fixes the whole ambiguity set.

Two consequences follow from the definitions as the source states them. First, EVaR is never less than CVaR at the same level, so an EVaR-feasible solution is a conservative certificate for a CVaR constraint.[^c6] Second, the risk-aversion EVaR encodes is invisible inside a one-parameter exponential family: there EVaR is strictly increasing in the mean, so "the arm minimizing EVaRα coincides with the arm minimizing the mean".[^c7] The source notes that in that family the best-arm problem is already solved by the mean-based theory. EVaR can only change which arm is best when the distributions vary in shape beyond the mean, which is the nonparametric setting the paper studies.

For bandits this matters because the decision rule is no longer a function of the mean. The paper evaluates an arm by the EVaR of its empirical distribution, and its algorithm recommends the arm whose empirical EVaR is lowest at the stopping time: "output the arm minimizing the empirical EVaR".[^c8] The sample-complexity side of that problem is a separate note: [[risk-aware-characteristic-time]].

## Limits

The analysis is restricted to distributions on a bounded interval. The source says it focuses "in the sequel on the set of probability distributions supported on the interval", taken as [0, 1], so tails beyond the support are outside the claim.[^c9] The CVaR relation is cited to Ahmadi-Javid (2011), not re-derived in the text I read. The text I read contains no numerical comparison of EVaR against CVaR or ERM, so it does not show which measure a decision-maker should prefer; that choice is a modelling decision the paper does not make. The statement that EVaR is conservative for CVaR constraints is a bound, not a claim that EVaR tracks CVaR closely.

## Related

- [[risk-aware-characteristic-time]] — the sample-complexity constant for best-arm identification under EVaR, built from KL projections of this measure
- [[step-level-risk-calibrated-router]] — penalizes a CVaR tail in its objective; EVaR is the upper bound on CVaR the paper points to, so the two differ by a conservative relaxation (this link is my inference, not the paper's claim)
- [[pac-best-arm-sample-complexity-lower-bound]] — the mean-based PAC bound; under EVaR the target arm changes with the risk level, so that bound's target does not carry over

[^c1]: doi-10-48550-arxiv-2510-04728 — "Defined via its exponential-moment form, EVaR is the tightest Chernoff-style bound on (C)VaR"
[^c2]: doi-10-48550-arxiv-2510-04728 — "it serves as the tightest coherent upper bound on Conditional Value-at-Risk (CVaR)"
[^c3]: doi-10-48550-arxiv-2510-04728 — "the nested infimum over z"
[^c4]: doi-10-48550-arxiv-2510-04728 — "the worst-case expectation over an ambiguity set"
[^c5]: doi-10-48550-arxiv-2510-04728 — "EVaR uses a hard constraint on the KL-divergence"
[^c6]: doi-10-48550-arxiv-2510-04728 — "EVaR-feasible solutions provide conservative certificates for CVaR constraints"
[^c7]: doi-10-48550-arxiv-2510-04728 — "the arm minimizing EVaRα coincides with the arm minimizing the mean"
[^c8]: doi-10-48550-arxiv-2510-04728 — "output the arm minimizing the empirical EVaR"
[^c9]: doi-10-48550-arxiv-2510-04728 — "focus in the sequel on the set of probability distributions supported on the interval"
