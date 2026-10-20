---
description: "With Gaussian arms of unknown variance, the best-arm sample-complexity lower bound exceeds the known-variance one, and the paper finds the excess rather small in typical instances."
aliases: ["unknown-variance lower bound", "two-parameter characteristic time", "T*(mu, sigma^2) characteristic time", "known-versus-unknown variance complexity gap"]
sources: ["doi-10-48550-arxiv-2210-00974"]
---
# Unknown-variance characteristic time

In fixed-confidence best-arm identification, a δ-correct algorithm must spend, in expectation, at least a multiple of log(1/δ) samples, and the multiple is a characteristic time. Its definition is a game. The learner chooses an allocation of samples over arms; an adversary chooses the cheapest alternative instance in which some other arm would be the best. The characteristic time is the value of this game. For Gaussian arms with known variances the alternatives only move means, and the lower bound is a function of the means and variances alone.[^c1]

When the variances are unknown, the alternatives may also change them. Jourdan, Degenne and Kaufmann write the lower bound for this two-parameter class, T*(µ, σ²), and compare it with the known-variance quantity T*_σ²(µ). The comparison goes through a transportation cost: for a pair of arms, the cheapest way to make one of them look better, paying a weighted divergence for each arm moved. For known variances the infimum over the new mean has a closed form in the gap between the two means and the variances divided by the allocation. For unknown variances the infimum over the new mean "has no simple analytic form",[^c2] and must be computed numerically.

The variance change has a visible effect. The cheapest alternative to the best arm does not keep its variance: "the closest alternatives have an increased variance".[^c3] An alternative that is close in mean is also made noisier, so it is harder to rule out, which is why the unknown-variance bound is at least the known one. The paper's relation is one-sided and tight in one regime: when a mismatch quantity d(µ, σ²) is at most 1, the two complexities are close, and their ratio lies between log 2 and 1.[^c5]

The headline is the size of the gap. The authors state that their analysis "reveals that this impact is rather small".[^c4] Their random-instance experiments with ten arms compare two wrappers that handle unknown variances, and they perform alike; the experiments do not measure the known-variance gap directly.[^c9]

## Limits

- The gap is established for expected sample complexity, for δ-correct algorithms, and for Gaussian arms. It does not transfer to other reward families, and the paper's comparisons use a single family of random instances with K = 10.
- "Small" is a typical-case statement. The ratio of the two characteristic times can be arbitrarily large: "there exist instances with an arbitrarily large complexity ratio".[^c6] The authors only conjecture that such instances are always easy, with both quantities small: "We conjecture that they always correspond to easy problems".[^c7] The conjecture is not proved here.
- The fixed-budget setting is not covered. The authors say that "the probability of misidentifying the best-arm is still an open problem" in that setting.[^c8]
- The lower bound is a benchmark, not an algorithm. The paper's algorithms that match it are discussed in the related notes, and the characteristic time says nothing about how much an algorithm wastes before it reaches it.

## Related

- [[pac-best-arm-sample-complexity-lower-bound]] — the distribution-free PAC bound of order n/ε² log(1/δ); the characteristic time is the instance-dependent refinement for Gaussian arms.
- [[risk-aware-characteristic-time]] — the same kind of object under an EVaR risk constraint, where a KL projection replaces the transportation cost.
- [[variance-constrained-best-arm-identification]] — variance as a feasibility constraint on the answer, not as a nuisance parameter that the lower bound must account for.
- [[empirical-variance-glr-stopping-rule]] — the algorithm family that plugs in an estimated variance and therefore targets the smaller known-variance quantity.

[^c1]: doi-10-48550-arxiv-2210-00974 — "An algorithm which is δ-correct on all problems in"
[^c2]: doi-10-48550-arxiv-2210-00974 — "the infimum in the mean parameter λ in the transportation cost for unknown variance has no simple analytic form"
[^c3]: doi-10-48550-arxiv-2210-00974 — "the closest alternatives have an increased variance"
[^c4]: doi-10-48550-arxiv-2210-00974 — "reveals that this impact is rather small"
[^c5]: doi-10-48550-arxiv-2210-00974 — "the two complexities are close"
[^c6]: doi-10-48550-arxiv-2210-00974 — "there exist instances with an arbitrarily large complexity ratio"
[^c7]: doi-10-48550-arxiv-2210-00974 — "We conjecture that they always correspond to easy problems"
[^c8]: doi-10-48550-arxiv-2210-00974 — "the probability of misidentifying the best-arm is still an open problem"
[^c9]: doi-10-48550-arxiv-2210-00974 — "We assess the performance on 1000 random instances"
