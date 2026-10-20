---
description: "In two-arm bandits with several fidelities, the cost-optimal allocation puts weight on a single fidelity per arm almost everywhere, so each arm has one optimal fidelity."
aliases: ["optimal fidelity", "sparse optimal cost allocation over fidelities"]
sources: ["doi-10-48550-arxiv-2406-03033"]
---
# Single fidelity per arm sparsity

When an arm can be sampled at several fidelities, the cost-optimal allocation is a distribution over arm–fidelity pairs. The natural question is how many fidelities of one arm it uses at once. The answer in the paper is: almost never, at least for two arms. In a two-arm bandit with M fidelities, the set of instances for which some optimal allocation puts positive cost weight on two different fidelities of the same arm "whose Lebesgue measure is zero."[^c1] So in almost all such instances, every optimal allocation gives each arm a single fidelity m*_a with positive weight. The paper states the consequence directly: "in most cases of 2 × M bandits, only one fidelity per arm has non-zero weight."[^c2]

The sparsity is a claim about the maximiser of the lower bound in the multi-fidelity cost-complexity game (see [[multi-fidelity-cost-complexity-lower-bound]]). For any number of arms, the paper proves a weaker statement: at the optimum, each arm has at least one fidelity with positive weight.[^c3] The two-arm result is what makes an "optimal fidelity" a well-defined object per arm. For a given instance, the question "which fidelity should this arm be sampled at" then has, generically, one answer: the single fidelity that carries that arm's cost.

The concept differs from earlier notions. Previous multi-fidelity best-arm papers already proposed arm-dependent optimal fidelities, and the paper checks them against its own bound: "these concepts do not comply with the concept of optimal fidelity" that its lower bound produces.[^c4] On some instances, following the older notion leads to suboptimal cost. So the sparsity result identifies a different object from the one the earlier literature called optimal fidelity, and the two should not be merged.

The paper also notes that the sparsity result is not a method: "this result does not offer an easy way to compute these optimal arm-dependent fidelities."[^c5] Knowing that the optimal fidelity is generically unique does not tell a strategy which fidelity it is without solving the max-min game, and the paper's appendix gives only special cases where the fidelity can be computed directly.[^c6]

## Limits

The sparsity theorem is proved for K = 2 arms. The authors correct an earlier version whose statement was for any K: "the proof holds only for K = 2."[^c7] For more than two arms the paper gives only the weaker result that each arm has some positive-weight fidelity, so the single-fidelity claim is not established in general.

"Almost all" is a Lebesgue-measure statement over the space of instances. It says the exceptional set is negligible, not that such instances are absent or rare in any particular application. An instance on the exceptional set can have two fidelities of one arm in its optimal allocation, and the text I read does not characterise them.[^c1]

The result concerns the optimal allocation of the lower bound's game. It does not say that an algorithm which tracks that allocation will concentrate on one fidelity per arm during sampling, since the paper's own algorithm tracks pull proportions derived from cost proportions with forced exploration.[^c8]

The sparsity was established by proof, not by experiment in the part of the text read. Its dependence on the bias bounds ξ and the costs λ is not explored in what I read.[^c9]

## Related

- [[multi-fidelity-cost-complexity-lower-bound]] — the bound whose optimal allocation this result describes
- [[pac-best-arm-sample-complexity-lower-bound]] — a unit-cost best-arm bound with no fidelity structure, where the question of a per-arm fidelity does not arise

[^c1]: doi-10-48550-arxiv-2406-03033 — "whose Lebesgue measure is zero."
[^c2]: doi-10-48550-arxiv-2406-03033 — "in most cases of 2 × M bandits, only one fidelity per arm has non-zero weight."
[^c3]: doi-10-48550-arxiv-2406-03033
[^c4]: doi-10-48550-arxiv-2406-03033 — "these concepts do not comply with the concept of optimal fidelity"
[^c5]: doi-10-48550-arxiv-2406-03033 — "this result does not offer an easy way to compute these optimal arm-dependent fidelities."
[^c6]: doi-10-48550-arxiv-2406-03033
[^c7]: doi-10-48550-arxiv-2406-03033 — "the proof holds only for K = 2."
[^c8]: doi-10-48550-arxiv-2406-03033
[^c9]: doi-10-48550-arxiv-2406-03033
