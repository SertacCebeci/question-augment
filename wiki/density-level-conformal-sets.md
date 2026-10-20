---
description: "Thresholding a posterior-predictive density, not a residual, gives conformal sets that can be disjoint under multimodal answers; size halves while a PAC risk bound keeps coverage."
aliases: ["HPD conformal sets", "Bayesian conformal prediction", "BCP", "decision-risk conformal threshold"]
sources: ["arxiv-2602-03331"]
---
# Density-level conformal sets

An answerer with a multimodal belief should not be forced to report one connected range. Conformal sets built from a density-based score can drop the valley between modes, and the threshold can be chosen with a high-probability guarantee rather than a bare quantile.

## Mechanism

Standard split [[conformal-prediction]] fixes a threshold lambda at an empirical quantile of calibration scores. Wu et al. (2026) instead treat lambda as a decision variable: minimise expected set size subject to the requirement that, with probability at least 1 - beta over the calibration draw, miscoverage is at most alpha.[^c1]

The score is the negative log of the posterior predictive density, fixed by the training data and so exchangeability is preserved. Thresholding it at level lambda is the same as taking the highest-posterior-density superlevel set, which can be disjoint when the predictive distribution has several modes.[^c2] Residual-based split CP and conformalised quantile regression return connected intervals and so must span the low-density valley between modes.[^c3]

Two regimes follow. With a nested threshold set (size monotone in lambda) the feasible region is a half-line and the optimum is just the smallest feasible lambda, which recovers existing PAC-style methods (Proposition 1).[^c4] For HPD sets the geometry changes abruptly when lambda crosses the density level of a secondary mode, because a connected component disappears; naive grid search can straddle that jump, and a Gaussian-process (Bayesian quadrature) estimate of expected set size is used to stabilise it.[^c5] Quadrature affects efficiency estimation only; the validity constraint comes from the Dirichlet-weighted L+ statistic of conformal risk control.[^c6]

## What was measured

- Bimodal synthetic regression (200 test points, alpha = beta = 0.2): mean set size 4.82 for split CP and 4.67 for CQR against 2.07 for BCP, with both PAC methods marked disjoint-capable.[^c7] The prior-art PAC-HPD baseline reached 2.06, so the size gain here comes from the HPD geometry, not from the extra optimisation step. This reading is mine, from the table.
- Diabetes regression with a misspecified prior: Bayesian credible intervals collapse to 49.2% coverage at an 80% target, while BCP holds 80.0%; marginal-coverage methods all sit near 79-81%, so exchangeability, not model quality, drives validity.[^c8]
- BCP matches the PAC target more reliably than the plain smallest-lambda variant (80.1% vs 79.3%) at a slightly wider interval and higher calibration time.[^c9]

## Limits

- Evidence is one synthetic 1-D bimodal task plus a diabetes regression and a classification set; no language-model or question-answering setting was tested.
- The guarantee is marginal and PAC over calibration randomness; no conditional (per-input) coverage is claimed.
- The size advantage depends on the model actually capturing the modes; a unimodal or wrong-mode posterior gives no gain (my inference).
- Quadrature adds calibration cost (1.15 s vs 0.10 s on diabetes).[^c9]
- Posterior-predictive density is approximated by importance reweighting of samples; its quality was not stress-tested here.

## Related

- [[conformal-prediction]] — the quantile-threshold base case this generalises
- [[credible-interval-undercoverage]] — credible intervals that undercover; here conformal calibration repairs it
- [[conformal-set-size-calibration-tradeoff]] — set size traded against coverage
- [[confidence-interval-calibration]] — stated intervals versus realised coverage

[^c1]: arxiv-2602-03331 — "BCP instead treats λ as a decision variable and enforces coverage with high probability over calibration randomness:"
[^c2]: arxiv-2602-03331 — "Thresholding s(x, y) = − log p̂(y | x) at level λ is equivalent to the HPD superlevel set {y : p̂(y |"
[^c3]: arxiv-2602-03331 — "In contrast, interval-constrained methods such as residual Split-CP and CQR enforce connected prediction sets and must span the low-density valley between"
[^c4]: arxiv-2602-03331 — "the feasible region of (3) is a half-line [λmin , ∞), and the unique minimiser is λ∗ = λmin ."
[^c5]: arxiv-2602-03331 — "A naive grid search can therefore straddle this discontinuity and return an unstable λ∗ ; BQ places a GP prior over λ 7→ g(λ), reducing estimation"
[^c6]: arxiv-2602-03331 — "BQ is used to estimate g(λ); the L+ constraint determines feasibility and coverage."
[^c7]: arxiv-2602-03331 — "4.82 ± 0.14"
[^c8]: arxiv-2602-03331 — "BCI collapses to 49.2% coverage under c=0.02 despite producing the narrowest intervals."
[^c9]: arxiv-2602-03331 — "BCP ensures the target coverage (80.1% vs."
