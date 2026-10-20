---
description: "With costed fidelities, the cost to find the best arm has an instance-dependent lower bound: a max over cost proportions of a min over alternatives, weighted by information per unit cost."
aliases: ["multi-fidelity best-arm identification", "MF-BAI", "cost complexity of best-arm identification"]
sources: ["doi-10-48550-arxiv-2406-03033"]
---
# Multi-fidelity cost-complexity lower bound

Some quantities can be sampled at several fidelities: a cheap model gives a rough value, an expensive one a precise value, and each fidelity has a known cost and a known bias bound. When the goal is to name the arm with the highest mean at the top fidelity, the quality of a strategy is the total cost paid until it stops, not the number of pulls.[^c1] The setting assumes that the algorithm knows the cost and the bias bound of each fidelity, "We assume that the algorithm knows both the cost and the maximal bias of"[^c2], and that every arm's means at the lower fidelities lie within known distances ξ_m of its top-fidelity mean. So a cheap sample is a biased view of the thing that matters.

The concept is a bound on cost, derived from a game. Read a vector ω over arm–fidelity pairs as cost proportions: the share of total spending that goes to each pair. For two arms i and j, f_{i,j}(ω, µ) is a KL-type divergence from µ to the nearest instance in which j beats i and only those two arms move, each pair's divergence weighted by its cost share divided by its cost λ_m. The complexity is governed by F(ω, µ) = max_i min_{j≠i} f_{i,j}(ω, µ). The best arm is the one for which there is the most cost-weighted evidence that every other arm is not better. The lower bound states that any δ-correct strategy pays, asymptotically, at least C*(µ) times a logarithm of 1/δ, where C*(µ)^{-1} is the supremum of F over the cost simplex.[^c3]

The structure is the one already known from unit-cost best-arm identification. The paper places it in the family of "game that appears in lower bounds for BAI problems"[^c4], and says that for one fidelity with unit cost the cost complexity "coincides with the sample complexity"[^c5]. What the costs change is the trade-off the max-player faces. Its objective is an information-per-cost ratio: "between the information gained by pulling an arm at some fidelity and the cost of that fidelity."[^c6] The min-player, by contrast, "minimizes only the information available to the" algorithm to tell two instances apart.[^c7] So cost enters only through the max-player's allocation.

Two consequences follow from the definition. First, F is concave in ω: the paper notes this "is a consequence of the fact F (ω, µ) is an infimum over linear functions of ω."[^c8] Second, the same F is not concave in the pull proportions that the algorithm actually controls, since those are a nonlinear transform of the cost proportions. The optimisation is therefore easy in cost space and harder in pull space.[^c9]

The algorithm this motivates does not solve the max-min game directly. A Track-and-Stop design would need the optimal cost proportions at every step, and the authors "did not find an efficient algorithm to compute it,"[^c10] so the classical route is closed. The alternative takes a sub-gradient ascent step on F, which "requires computing gradients of F (hence only a minimization problem and not a max-min)."[^c11] The sub-gradient is computed in closed form for each pair of arms through a one-dimensional fixed-point equation, so the cost per step is polynomial in K and M.[^c12] The resulting procedure converts cost proportions into pull proportions, adds forced exploration, tracks them, and stops with a generalized-likelihood-ratio test on the f_{i,j} statistics.[^c12]

The headline result is a matching upper bound: the algorithm "is asymptotically optimal, meaning that it matches the"[^c13] lower bound as the confidence goes to one. The paper also reports that the earlier lower bounds "is looser than Theorem 3.1."[^c14] Earlier upper bounds needed extra knowledge, for instance "In [32], instead, the authors assume additional knowledge expressed as" an upper bound on the best arm's top-fidelity mean and a lower bound on the runner-up's.[^c15]

## Limits

The matching is asymptotic. The optimality statement is a limit in the confidence parameter, not a finite-δ sample bound, and the text I read does not give one.[^c16]

The algorithm assumes the costs and the bias bounds are known. The lower bound is stated for exponential-family arms, and for instances with a unique optimal arm; the text does not treat instances outside those classes.[^c17]

The constant C*(µ) has no closed form in the text. Its value is only reachable through the optimisation, and the sparsity of the optimal allocation is a generic statement, not a computation for given µ (see [[single-fidelity-per-arm-sparsity]]).[^c18]

The sub-gradient result needs F(ω, µ) > 0, and the authors say the degenerate case is handled by a modification they do not reproduce in the text I read.[^c19]

The experiments in the paper's Section 5 were not read for this note. Whether the new algorithm beats earlier methods in practice is therefore not assessed here, only the theory.[^c20]

The costs are fixed per fidelity and the biases are known. Applying the cost-weighted game to asking questions, where a "fidelity" might be a cheaper form of question and the cost is not stationary, is my own inference and was not tested in the work.

## Related

- [[pac-best-arm-sample-complexity-lower-bound]] — the unit-cost, ε-good target; its constant is a different quantity from C*(µ)
- [[risk-aware-characteristic-time]] — the same sup-min shape of a lower bound, with risk-weighted rather than cost-weighted divergences
- [[plug-in-glr-stopping-rule]] — the generalized-likelihood-ratio stopping family that the paper's stopping rule belongs to (my inference from the shape of f_{i,j})
- [[single-fidelity-per-arm-sparsity]] — where the cost-optimal allocation puts its weight, arm by arm

[^c1]: doi-10-48550-arxiv-2406-03033 — "Our first contribution is a tight, instance-dependent lower bound on the cost"
[^c2]: doi-10-48550-arxiv-2406-03033 — "We assume that the algorithm knows both the cost and the maximal bias of"
[^c3]: doi-10-48550-arxiv-2406-03033
[^c4]: doi-10-48550-arxiv-2406-03033 — "game that appears in lower bounds for BAI problems"
[^c5]: doi-10-48550-arxiv-2406-03033 — "coincides with the sample complexity"
[^c6]: doi-10-48550-arxiv-2406-03033 — "between the information gained by pulling an arm at some fidelity and the cost of that fidelity."
[^c7]: doi-10-48550-arxiv-2406-03033 — "the min-player minimizes only the information available to the"
[^c8]: doi-10-48550-arxiv-2406-03033 — "This is a consequence of the fact F (ω, µ) is an infimum over linear functions of ω."
[^c9]: doi-10-48550-arxiv-2406-03033
[^c10]: doi-10-48550-arxiv-2406-03033 — "we did not find an efficient algorithm to compute it,"
[^c11]: doi-10-48550-arxiv-2406-03033 — "which requires computing gradients of F (hence only a minimization problem and not a max-min)."
[^c12]: doi-10-48550-arxiv-2406-03033
[^c13]: doi-10-48550-arxiv-2406-03033 — "Algorithm 1 is asymptotically optimal, meaning that it matches the"
[^c14]: doi-10-48550-arxiv-2406-03033 — "previous works is looser than Theorem 3.1."
[^c15]: doi-10-48550-arxiv-2406-03033 — "In [32], instead, the authors assume additional knowledge expressed as"
[^c16]: doi-10-48550-arxiv-2406-03033
[^c17]: doi-10-48550-arxiv-2406-03033
[^c18]: doi-10-48550-arxiv-2406-03033
[^c19]: doi-10-48550-arxiv-2406-03033
[^c20]: doi-10-48550-arxiv-2406-03033
