---
description: "Fixed-confidence best-arm identification for CVaR: the target is the arm with least tail risk, and its sample-size constant is a sup-min of KL projections, one of them non-convex."
aliases: ["CVaR best-arm identification", "mean-CVaR best-arm identification", "conditional value-at-risk best-arm identification", "tail-risk best-arm identification"]
sources: ["doi-10-48550-arxiv-2008-07606"]
---
# CVaR best-arm identification

Fixed-confidence best-arm identification asks which of finitely many arms is best, and how many samples a δ-correct procedure must spend before it may name one. Here "best" is a risk functional rather than a mean. Conditional value-at-risk (CVaR) at level π is the average loss in the tail beyond the value-at-risk quantile. The target is the arm with the smallest CVaR, or the smallest VaR, or the smallest weighted sum of CVaR and mean, the last one capturing the risk-return trade-off common in finance. The paper's aim is to "identify the arm with the minimum risk, measured in terms of CVaR, VaR, or a conic combination of mean and CVaR".[^c1]

**The sample-cost constant.** As in the mean case, the lower bound on the expected number of samples is a constant times log(1/δ), and the constant is a property of the instance. It is a supremum over sampling proportions t in the probability simplex of an infimum over alternative instances in which another arm has the lower CVaR, of a weighted sum of KL divergences. The displayed formula is garbled in the text I read, so I give its shape and not its symbols. The inner infimum is a KL projection with a CVaR constraint: the smallest KL from one arm's distribution to any distribution whose CVaR is at least, or at most, a threshold x. The paper says these functionals "are central to our plugin algorithm".[^c2]

**Why the two projections differ.** The projection that moves the arm to higher CVaR is a convex program. The one that moves it to lower CVaR is not, and the stated reason is concavity: CVaR is a concave function of the distribution, so the constraint "renders the feasible region non-convex".[^c3] The paper gets around this by writing CVaR as the optimal value of a minimisation over a threshold. That "helped in re-expressing" the non-convex projection "as minimization over 2 variables, fixing one of which resulted in convex optimization over the other".[^c4] So the hard projection is a one-dimensional search over a convex inner problem.

**The algorithm.** The procedure is a plug-in strategy. The paper says it "uses the generated empirical distributions as a proxy for the true distributions": at each stage the allocation problem is solved on the empirical distributions, and sampling follows the resulting proportions, with mild forced exploration.[^c5] An empirical distribution need not lie in the moment class of the next note, so it is first projected back into that class under the Lévy metric before the allocation is computed.[^c6] The paper's claim is that the sample complexity matches the lower bound as δ tends to 0: the method "matches the lower bound on the expected" number of samples, asymptotically.[^c7] To reduce the cost, the allocation is re-solved only about log n times up to n samples, and the paper states that this modification "is optimal upto a constant".[^c8]

**Two side results.** The same projections give non-asymptotic, empirical-likelihood concentration inequalities for CVaR, which the abstract says are "tighter than those for popular truncation-based empirical estimators".[^c9] The paper also states that the mean-CVaR problem is "conceptually and technically similar to the CVaR problem".[^c10]

**The VaR contrast.** VaR is treated separately: "We solve the VaR problem for arbitrary arm distributions".[^c11] Its projections have closed forms, but they are "no longer jointly-continuous in the Lévy metric", and that loss of continuity is the technical cost of the VaR case.[^c12]

**Where the mean returns.** In a canonical one-parameter exponential family, CVaR and VaR are monotone in the parameter, so "finding the best-(CVaR/VaR/mean-CVaR) arm reduces to finding the arm with the minimum mean".[^c13] The risk target differs from the mean target only when arm distributions differ in shape beyond the mean.

## Limits

- The optimality is asymptotic, as δ tends to 0. The finite-δ evidence is a simulation the paper itself calls "a brief teaser section on the experiments".[^c14] It uses three arms from Fisher-Tippett and Pareto families. The authors conclude that "optimality is in fact indicative of the performance in practice",[^c15] but three arms is a narrow test. The same section reports that "the sample complexity is also sensitive to B", the moment bound.[^c16]
- The guarantee is for a specific version of the procedure. The experiments use "a version of Track-and-Stop including C-tracking and forced exploration".[^c17] The forced exploration and the C-tracking are added components, so the claim is about that design.
- The CVaR problem is not learnable without the moment restriction in the next note, and the constant depends on the bound B. Its inputs are the arm distributions and B, and the paper does not show how B is obtained from data.
- Computation is a stated concern: "This can be computationally demanding especially as the underlying samples in the empirical distribution become large".[^c18]
- The VaR and mean-CVaR proofs are in appendices I did not read. The claims here about them come from the main text.
- Transfer to asking is my inference, not the paper's. The part that may carry over is that the target can be a tail functional of an outcome rather than its centre, so a question about worst cases needs a different stopping rule than one about averages. Whether that changes how questions are formulated is untested.

## Related

- [[moment-bounded-arm-class]] — the restriction on arm distributions without which the CVaR problem is unlearnable.
- [[risk-aware-characteristic-time]] — the same sup-min shape of lower bound under EVaR, a different risk measure; that note's constant is for one risk level.
- [[entropic-value-at-risk]] — a risk measure built from the moment-generating function, offered in the literature as a relaxation of CVaR; not the same target.
- [[pac-best-arm-sample-complexity-lower-bound]] — the mean-based bound; in exponential families the CVaR target coincides with the mean target, as above.
- [[variance-constrained-best-arm-identification]] — variance as a constraint on which arms may be named, rather than CVaR as the objective.

[^c1]: doi-10-48550-arxiv-2008-07606 — "minimum risk, measured in terms of CVaR, VaR, or a conic combination of mean and CVaR"
[^c2]: doi-10-48550-arxiv-2008-07606 — "are central to our plugin algorithm"
[^c3]: doi-10-48550-arxiv-2008-07606 — "a concave function, whence, the CVaR constraint"
[^c4]: doi-10-48550-arxiv-2008-07606 — "fixing one of which resulted in convex optimization over the other"
[^c5]: doi-10-48550-arxiv-2008-07606 — "uses the generated empirical distributions as a proxy for the true distributions"
[^c6]: doi-10-48550-arxiv-2008-07606 — "This is handled by projecting them on to L under a suitable metric"
[^c7]: doi-10-48550-arxiv-2008-07606 — "matches the lower bound on the expected"
[^c8]: doi-10-48550-arxiv-2008-07606 — "We show that it is optimal upto a constant"
[^c9]: doi-10-48550-arxiv-2008-07606 — "which are tighter than those for popular truncation-based empirical estimators"
[^c10]: doi-10-48550-arxiv-2008-07606 — "The mean-CVaR problem is conceptually and technically similar to the CVaR problem"
[^c11]: doi-10-48550-arxiv-2008-07606 — "We solve the VaR problem for arbitrary arm distributions"
[^c12]: doi-10-48550-arxiv-2008-07606 — "no longer jointly-continuous in the Lévy metric"
[^c13]: doi-10-48550-arxiv-2008-07606 — "finding the best-(CVaR/VaR/mean-CVaR) arm reduces to finding the arm with the minimum mean"
[^c14]: doi-10-48550-arxiv-2008-07606 — "This is only a brief teaser section on the experiments"
[^c15]: doi-10-48550-arxiv-2008-07606 — "optimality is in fact indicative of the performance in practice"
[^c16]: doi-10-48550-arxiv-2008-07606 — "the sample complexity is also sensitive to B"
[^c17]: doi-10-48550-arxiv-2008-07606 — "implement a version of Track-and-Stop including C-tracking and forced exploration"
[^c18]: doi-10-48550-arxiv-2008-07606 — "This can be computationally demanding especially as the underlying samples in the empirical distribution become large"
