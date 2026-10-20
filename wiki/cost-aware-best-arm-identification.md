---
description: "Identifying the best arm when each pull has its own cost sets a lower bound on total cost, and the optimal allocation tilts toward cheap arms; in two Gaussian arms the cost enters as a square root."
aliases: ["CABAI", "cost-aware best arm identification", "cost-aware pure exploration", "cost-weighted best-arm identification"]
sources: ["doi-10-48550-arxiv-2402-16710"]
---
# Cost-aware best-arm identification

In fixed-confidence best-arm identification a learner samples arms until it can name the best one with confidence 1 − δ. Cost-aware best-arm identification (CABAI) adds one thing: each arm carries a second random quantity, a cost, and the thing minimised is the cost paid before the decision, not the number of pulls. The model is written so that "each arm is in addition associated with a cost distribution to model the object for testing".[^c1] The goal "is to identify the highest reward arm using the minimum cost possible".[^c2]

The mechanism is an objective split between two phases. The work frames it as "the separation of testing and implementation phases", in which the "objective shift between phases, i.e., cost for testing and reward for implementation".[^c3] Sampling is judged by what it costs; the choice that follows is judged by reward. Plain best-arm identification treats both as one quantity, the number of pulls, and so it cannot say that a cheap arm deserves more of the budget than an expensive arm of equal information.

**The lower bound.** For any δ-PAC algorithm the expected cumulative cost grows at least like T\*(µ) log(1/δ), where T\*(µ)⁻¹ is a sup over allocations w of an inf over alternative models of a KL term weighted by w_a over c_a, as displayed in the paper's Theorem 1. The authors read it as "O(log(1/δ)) cumulative cost is inevitable to identify the optimal arm".[^c4] The allocation that matters is the share of total cost, not of pulls: the optimal weight "characterizes the optimal proportion of the total cumulative cost from pulling arm a".[^c5] The consequence is a reversal of the usual allocation. In the paper's three-arm example the optimal proportions of pulls shift toward the cheapest arm, and the table note states that CABAI "emphasizes more on low-cost arms to complement high-cost arms".[^c6]

**The square-root law.** For two arms with unit-variance Gaussian rewards the bound has a closed form, and the authors note that "the dependence on cost is non-trivial but somehow involves the square root".[^c7] My own inference from the displayed corollary is that the cost term has the shape (√c₁ + √c₂)² over the squared reward gap, multiplied by log(1/δ). The text as extracted does not settle the leading constant, so only the shape is taken here. My own inference is that the square root is why a large cost ratio moves the sampling share less than a linear cost weight would; the paper does not state this comparison.

**Reaching the bound.** The algorithm that matches the lower bound asymptotically, CTAS, tracks the optimal cost proportions, but "optimization problem at each time step, which exerts relatively high computational complexity".[^c8] A cheaper rule, Chernoff Overlap, samples by "the square-root rule", which "weighs Na (t) with ca".[^c9] In the two-arm case the authors show it "asymptotically cost-optimal for this special case".[^c10] The practical claim is that ignoring cost "results in sub-optimality in practice".[^c11]

## Limits

- The closed form is for two Gaussian arms with unit variance. For K ≥ 3 there is "no closed-form expression for w∗ in general bandit models with K ≥ 3"; the optimal allocation is found by iterative bisection in the appendix, not in closed form.[^c12]
- The optimality guarantee is asymptotic in δ → 0. The cheap algorithm inherits no such guarantee: "CO does not inherit the strong theoretical guarantees of CTAS".[^c13] Whether it has a provable gap in general is left open: "a provable suboptimality gap is an interesting future research problem".[^c14]
- Costs are random in the model, and this costs extra exploration: the rule needed more exploration "due to the added variance from random costs".[^c15] The paper's experiments use one illustrative configuration (µ = [1.5, 1, 0.5], c = [1, 0.1, 0.01]) and simulated draws, not a real testing pipeline; that is my reading of the setup.
- The arms are product candidates with independent reward and cost draws. Treating a question as an arm pull with a known cost and a fixed gap is my own inference, not something the paper tests; it assumes answers are independent noisy draws, which question-asking seldom gives.

## Related

- [[pac-best-arm-sample-complexity-lower-bound]] — the unit-cost lower bound this one generalises: cost replaces the pull count as the quantity bounded
- [[plug-in-glr-stopping-rule]] — the same family of likelihood-ratio stopping statistic that the paper uses for its stopping rule
- [[risk-aware-characteristic-time]] — another change to the best-arm characteristic time, here by a risk constraint instead of a cost
- [[cost-aware-module-selection-for-help-queries]] — a cost-aware query choice where the cost is the asker's cost of being answered, not the cost of sampling
- [[active-inference-context-acquisition]] — a cost-weighted stopping rule in a different setting

[^c1]: doi-10-48550-arxiv-2402-16710 — "each arm is in addition associated with a cost distribution to model the object for testing"
[^c2]: doi-10-48550-arxiv-2402-16710 — "is to identify the highest reward arm using the minimum cost possible"
[^c3]: doi-10-48550-arxiv-2402-16710 — "objective shift between phases, i.e., cost for testing and reward for implementation."
[^c4]: doi-10-48550-arxiv-2402-16710 — "cumulative cost is inevitable to identify the optimal arm"
[^c5]: doi-10-48550-arxiv-2402-16710 — "characterizes the optimal proportion of the total cumulative cost from"
[^c6]: doi-10-48550-arxiv-2402-16710 — "Noticeably, CABAI emphasizes more on low-cost arms to complement high-cost arms."
[^c7]: doi-10-48550-arxiv-2402-16710 — "It is noticeable that the dependence on cost is non-trivial but somehow involves the square root"
[^c8]: doi-10-48550-arxiv-2402-16710 — "optimization problem at each time step, which exerts relatively high computational complexity"
[^c9]: doi-10-48550-arxiv-2402-16710 — "called the square-root rule."
[^c10]: doi-10-48550-arxiv-2402-16710 — "asymptotically cost-optimal for this special case"
[^c11]: doi-10-48550-arxiv-2402-16710 — "action cost results in sub-optimality in practice"
[^c12]: doi-10-48550-arxiv-2402-16710 — "there is no closed-form expression for w∗ in general bandit models with K ≥ 3"
[^c13]: doi-10-48550-arxiv-2402-16710 — "CO does not inherit the strong theoretical guarantees of CTAS"
[^c14]: doi-10-48550-arxiv-2402-16710 — "a provable suboptimality gap is an interesting future research problem"
[^c15]: doi-10-48550-arxiv-2402-16710 — "due to the added variance from random costs"
