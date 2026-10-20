---
description: "Best-arm identification under a variance threshold: the sample complexity is set by a hardness that adds variance gaps to mean gaps and reduces to H1 when the threshold is loose."
aliases: ["VA-LUCB", "variance-constrained BAI", "variance-aware best-arm identification", "variance-aware hardness H_VA", "risk-constrained best-arm identification under a variance threshold"]
sources: ["doi-10-48550-arxiv-2201-10142"]
---
# Variance-constrained best-arm identification

In fixed-confidence best-arm identification the learner must name the arm with the highest mean. With a feasibility constraint the target changes: the learner must name the arm with the highest mean among the arms that also satisfy a second condition. Here the second condition is on variance. An arm is feasible when its variance is below a threshold σ̄², and the target is the best feasible arm, i* = argmax{µ_i : σ_i² ≤ σ̄²}. The constraint is "strictly smaller than a given threshold",[^c1] and the learner must also decide whether any feasible arm exists at all.

The point of the formulation is that the two parts of the answer are different statistics. The authors say that they "seek optimality in the mean and feasibility in the" variance,[^c2] and that they want "the best arm strictly satisfying the risk constraint without any slack or suboptimality".[^c3] A high-mean arm that is slightly too risky cannot be returned, and a low-variance arm that is much worse in mean cannot be returned either. Both checks must be made before an arm is named.

**The mechanism.** VA-LUCB, the algorithm the paper proposes, keeps a confidence interval for the mean and one for the variance of every arm, built from that arm's own samples. From the variance intervals it sorts the arms into three sets: those whose upper variance bound is below σ̄² (empirically feasible), those whose interval straddles σ̄² (almost feasible), and those whose lower bound is above σ̄² (infeasible). The empirically best feasible arm is the candidate. An arm that is possibly feasible and whose upper mean bound exceeds the candidate's lower mean bound is a competitor, and only competitors are sampled further, which "also motivates our stopping rule".[^c4] The sampling is asymmetric on purpose. For an arm that is confidently feasible, "only its sample mean needs to be further examined"; an arm whose feasibility is still open needs more pulls for its variance as well.[^c5]

**The hardness.** The sample complexity is governed by a single number, H_VA, which the paper calls "fundamental variance-aware hardness quantity".[^c6] It is a sum of terms over the arms. Some terms carry inverse squared mean gaps for feasible suboptimal arms and for the best feasible arm. The others carry inverse squared variance gaps, |σ_i² − σ̄²|, for arms that lie on the far side of the threshold from the best feasible arm, and inverse squared mean gaps for the risky arms that could mislead the search. The authors tie the terms to the sampling steps. The last term, for instance, is the cost of ruling out arms that are infeasible or suboptimal: once that is settled, the learner can "eliminate them, which explains the last term in HVA".[^c13] The printed formula is poorly extracted in the text I read, so I do not reproduce it.

The upper bound on the time to termination is of order H_VA up to a logarithmic factor, and the paper proves an information-theoretic lower bound: "is optimal up to a factor logarithmic in HVA".[^c7] So the constant is not a free design parameter. Two properties tie it to the classical setting. When the threshold is loose, H_VA reduces to the unconstrained hardness H1, "HVA reduces to the",[^c8] and when the constraint is inactive the algorithm particularizes to LUCB.[^c9] The algorithm is also parameter-free: it "can output the best feasible arm i* without knowledge of any parameters that define the instance".[^c10]

## Limits

- The lower bound matches the upper bound only up to a logarithmic factor in H_VA. The text does not establish exact constants, so the claim is about the order of the sample complexity, not its leading term.
- The target is unique and strictly feasible: the authors assume "that, if it exists, the best feasible arm is unique" and that its variance is strictly below σ̄². The boundary case, where the best arm's variance equals the threshold, is treated in an appendix I did not read.[^c11]
- Rewards are taken bounded: "For the sake of clarity, we consider bounded rewards."[^c14] Sub-Gaussian extensions are deferred to an appendix.[^c15] Heavier tails are not covered in the part I read.
- The experiments are simulations on chosen instances that vary the terms of H_VA, and the paper reports that the algorithm "reduc[es] the sample complexity significantly".[^c12] They are not a field test. The comparison with the algorithm of David et al. uses a variant that "can only be applied if some unknown parameters" such as the suboptimality gaps are known.[^c16] So that baseline is given information VA-LUCB does not use (my reading).
- Variance is one risk measure. The authors say the framework extends to other risk measures "as long as there are appropriate concentration bounds".[^c17] That extension is stated as possible, not shown here.
- Transfer to asking is my inference, not the paper's. The part that may carry over is the separation of the feasibility check from the objective check, and the rule that a candidate confidently outside the constraint need not be examined for its objective. Whether this changes how questions are formulated or answered in practice is untested.

## Related

- [[risk-aware-characteristic-time]] — the asymptotic counterpart under an EVaR constraint: an exact constant as δ → 0, where this note's hardness is a finite-sample quantity on a variance threshold.
- [[pac-best-arm-sample-complexity-lower-bound]] — the unconstrained PAC bound; H_VA reduces to its H1 when the threshold is loose.
- [[cost-aware-best-arm-identification]] — another second statistic per arm, but a cost paid while testing, not a gate on which arms may be named.
- [[entropic-value-at-risk]] — a different risk measure that could occupy the same constraint slot, subject to the concentration bounds the authors require.

[^c1]: doi-10-48550-arxiv-2201-10142 — "is strictly smaller than a given threshold"
[^c2]: doi-10-48550-arxiv-2201-10142 — "we seek optimality in the mean and feasibility in the"
[^c3]: doi-10-48550-arxiv-2201-10142 — "best arm strictly satisfying the risk constraint without any slack"
[^c4]: doi-10-48550-arxiv-2201-10142 — "only the competitor arms in the set"
[^c5]: doi-10-48550-arxiv-2201-10142 — "needs to be further examined"
[^c6]: doi-10-48550-arxiv-2201-10142 — "fundamental variance-aware hardness quantity HVA"
[^c7]: doi-10-48550-arxiv-2201-10142 — "is optimal up to a factor logarithmic in HVA"
[^c8]: doi-10-48550-arxiv-2201-10142 — "HVA reduces to the"
[^c9]: doi-10-48550-arxiv-2201-10142 — "A hardness parameter HVA is identified"
[^c10]: doi-10-48550-arxiv-2201-10142 — "parameter free, in the sense that Algorithm 1 can output the"
[^c11]: doi-10-48550-arxiv-2201-10142 — "We assume that, if it exists, the best feasible arm is unique"
[^c12]: doi-10-48550-arxiv-2201-10142 — "reducing the sample complexity significantly,"
[^c13]: doi-10-48550-arxiv-2201-10142 — "eliminate them, which explains the last term in HVA"
[^c14]: doi-10-48550-arxiv-2201-10142 — "For the sake of clarity, we consider bounded rewards,"
[^c15]: doi-10-48550-arxiv-2201-10142 — "to sub-Gaussian rewards in App. E."
[^c16]: doi-10-48550-arxiv-2201-10142 — "applied if some unknown parameters"
[^c17]: doi-10-48550-arxiv-2201-10142 — "as there are appropriate concentration bounds"
