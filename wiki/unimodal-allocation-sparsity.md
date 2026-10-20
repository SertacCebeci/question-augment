---
description: "Under a unimodal ordering of means, the optimal sampling allocation for finding the best arm is supported on the best arm and its neighbours, so the problem reduces to three arms."
aliases: ["sparsity pattern of oracle weights", "unimodal sparsity pattern"]
sources: ["doi-10-48550-arxiv-2411-01898"]
---
# Unimodal allocation sparsity

Suppose the arm means rise with the index up to a unique maximum and then fall. Under this structure, best-arm identification is much smaller than its number of arms suggests. The optimal sampling allocation, the proportions that the characteristic time's inner maximisation returns, puts weight only on the best arm and its neighbours; every other arm gets zero. The paper states this as a rewriting of the characteristic time, which "reveals a sparsity pattern of the oracle weights",[^c1] so that the optimal weights "are only spread among the best arm" and its neighbouring arms.[^c2]

The mechanism is a reduction. Restricted to the neighbourhood, the sup-min over allocations becomes a minimum over the neighbours of a pairwise term, and the paper says this "establishes a reduction of Unimodal BAI to unstructured BAI" on a three-arm set.[^c3] The consequence it draws is that "we inherit a fast and K-independent algorithm" for the oracle weights.[^c4] The reduction is an equality only at the optimal allocation: the paper notes that "This equality does not hold for arbitrary weights", so a generic solver over all arms does not gain it.[^c5] The abstract gives the headline form: "only three arms contribute to the leading confidence-dependent cost".[^c6] The structure is not incidental to the algorithms: "is a central component of our algorithms".[^c7]

The reason local information is enough is the paper's argument that "As local information is sufficient for global optimality".[^c8] That is what lets the optimistic tracking rule restrict its samples: "O-TaS exploits the sparsity pattern by limiting the" pulls to the best arm and its neighbours.[^c9] My reading is that arms outside that set need no samples asymptotically; the paper proves this for its own algorithm, not as a general principle.

## Limits

The sparsity is asymptotic. The worst-case bound says that "a linear dependence on the number of arms is unavoidable in the confidence-independent" cost,[^c10] and that sparsity "is only possible asymptotically".[^c11] The hard instances are flat with a single spike: "the instance is flat with a spike on the best arm",[^c12] and so "an algorithm has to sample all arms before finding the best one".[^c13] At moderate confidence, then, the three-arm picture does not describe the sample count. The paper's worst-case lower bound also holds only for K specific instances: "Theorem 2.3 is not valid for any" instance.[^c14]

The structure is imposed on the mean vector, which the algorithms must first map into the unimodal class. Empirical means "might not be unimodal",[^c15] and the paper's map is one choice among several, since "other choices could have been made".[^c16] The paper works in a one-parameter exponential family setting,[^c18] and the sparsity results are stated for that setting.

The paper mentions sparsity patterns elsewhere: "the instance-dependent lower bound have arisen in the" minimum threshold problem, good-arm identification and multi-fidelity bandits.[^c17] It presents these as similar phenomena, not as the same structure. Whether another structure yields the same neighbourhood property is my inference, and this text does not test it.

## Related

- [[risk-aware-characteristic-time]] — the general sup-min characteristic time; this note is its restriction to unimodal means.
- track-and-stop — the sampling rule whose oracle becomes cheap under this sparsity.
- [[local-evidence-stopping-rule]] — the stopping statistic that uses the same three-arm neighbourhood.

[^c1]: doi-10-48550-arxiv-2411-01898 — "reveals a sparsity pattern of the oracle weights"
[^c2]: doi-10-48550-arxiv-2411-01898 — "are only spread among the best arm"
[^c3]: doi-10-48550-arxiv-2411-01898 — "establishes a reduction of Unimodal BAI to unstructured BAI"
[^c4]: doi-10-48550-arxiv-2411-01898 — "we inherit a fast and K-independent algorithm"
[^c5]: doi-10-48550-arxiv-2411-01898 — "This equality does not hold for arbitrary weights"
[^c6]: doi-10-48550-arxiv-2411-01898 — "only three arms contribute to the leading confidence-dependent cost"
[^c7]: doi-10-48550-arxiv-2411-01898 — "is a central component of our algorithms"
[^c8]: doi-10-48550-arxiv-2411-01898 — "As local information is sufficient for global optimality"
[^c9]: doi-10-48550-arxiv-2411-01898 — "O-TaS exploits the sparsity pattern by limiting the"
[^c10]: doi-10-48550-arxiv-2411-01898 — "a linear dependence on the number of arms is unavoidable in the confidence-independent"
[^c11]: doi-10-48550-arxiv-2411-01898 — "is only possible asymptotically"
[^c12]: doi-10-48550-arxiv-2411-01898 — "the instance is flat with a spike on the best arm"
[^c13]: doi-10-48550-arxiv-2411-01898 — "an algorithm has to sample all arms before finding the best one"
[^c14]: doi-10-48550-arxiv-2411-01898 — "Theorem 2.3 is not valid for any"
[^c15]: doi-10-48550-arxiv-2411-01898 — "might not be unimodal"
[^c16]: doi-10-48550-arxiv-2411-01898 — "other choices could have been made"
[^c17]: doi-10-48550-arxiv-2411-01898 — "the instance-dependent lower bound have arisen in the"
[^c18]: doi-10-48550-arxiv-2411-01898 — "The arms distributions belong to a given one-parameter exponential family"
