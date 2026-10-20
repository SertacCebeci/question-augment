---
description: "Under unimodal means, a stopping rule can declare the best arm once it beats only its neighbours, avoiding the linear-in-K threshold of a full-sum test that stops early and errs."
aliases: ["local GLR stopping rule", "local GLR"]
sources: ["doi-10-48550-arxiv-2411-01898"]
---
# Local-evidence stopping rule

A fixed-confidence algorithm stops when the evidence for a candidate answer is large enough. The generalized likelihood-ratio statistic for "arm i is best" must be compared against alternatives in which some other arm is best. Without structure, the natural alternative set covers every arm, and the statistic becomes a sum over all arms. The paper calls this the full-sum rule and writes its threshold with a term in K log t, which "can be very large even if the lower bounds tells us that only 3 arms matter".[^c1]

Under a unimodal ordering, the paper replaces the full sum with a local test. For each arm i it defines W_t(i,j) for each neighbour j, and "represents the amount of collected evidence in favor of the hypothesis" that arm i has the larger mean than j.[^c2] The candidate answer is the arm whose weakest neighbourhood comparison is strongest, and the algorithm stops when that weakest comparison clears a threshold c(t-1, δ). Only the comparisons with the candidate's neighbours enter, so the statistic depends on three arms whatever K is. The paper's justification is structural: "Given that the true instance is unimodal" then "of local optimality is a sufficient condition to be statistically confident of global optimality".[^c3][^c4] The rule is also cheaper to evaluate, because computing W_t(i,j) "is much easier" than solving the full infimum.[^c5]

The full-sum failure is concrete. In a flat instance with one arm of mean Δ > 0 and all others at zero, the empirical means scatter around zero, and the K-linear term lets the full-sum statistic cross the threshold early. The paper's words are that "removing the linear dependence in K" from the threshold "yields early stopping and errors",[^c6] and that the full-sum rule with the heuristic threshold "violates the empirical δ-correctness criterion since it stops very early and returns wrong answers".[^c7] So the local rule does not merely save computation; it is the version that keeps the error rate. The paper says it "does not suffer from the same limitation with the dependence in K as the full-sum rule".[^c8]

## Limits

The correctness result is for Gaussian distributions with known variance and means in the unimodal class: the stopping rule with the threshold "yields a δ-correct for Gaussian distributions with known variance and mean in S".[^c9] For other one-parameter exponential families the paper refers the reader to another work, "For other classes of one-parameter exponential families",[^c10] and that extension is not checked in this text.

The guarantee also depends on the unimodal assumption. The local argument is a theorem about unimodal instances; if the true means are not unimodal, the claim that the three-arm test suffices has no support in the paper, and I do not know what the rule does then. This is my inference from the stated premise. The paper does not test misspecification. The threshold has a logarithmic term in t and a constant; the text's garbled formula is not reproduced here, and this note does not rely on its exact constants.

## Related

- [[plug-in-glr-stopping-rule]] — another GLR-type stopping statistic, calibrated for unknown variance; the local rule instead restricts the alternative set to neighbours.
- [[unimodal-allocation-sparsity]] — the same three-arm neighbourhood, on the allocation side.
- track-and-stop — the sampling rule the paper pairs with the GLR stopping rule of this kind.
- top-two-sampling — its challenger is drawn from the same neighbourhood as the local test.

[^c1]: doi-10-48550-arxiv-2411-01898 — "can be very large even if the lower bounds tells us that only 3 arms matter"
[^c2]: doi-10-48550-arxiv-2411-01898 — "represents the amount of collected"
[^c3]: doi-10-48550-arxiv-2411-01898 — "Given that the true instance is unimodal"
[^c4]: doi-10-48550-arxiv-2411-01898 — "of local optimality is a sufficient condition to be statistically confident of global optimality"
[^c5]: doi-10-48550-arxiv-2411-01898 — "It is also more computationally efficient"
[^c6]: doi-10-48550-arxiv-2411-01898 — "yields early stopping and errors"
[^c7]: doi-10-48550-arxiv-2411-01898 — "violates the empirical δ-correctness criterion since it stops very early and returns wrong answers"
[^c8]: doi-10-48550-arxiv-2411-01898 — "does not suffer from the same limitation with the dependence in K as the full-sum rule"
[^c9]: doi-10-48550-arxiv-2411-01898 — "yields a δ-correct for Gaussian distributions with known variance and mean in S"
[^c10]: doi-10-48550-arxiv-2411-01898 — "For other classes of one-parameter exponential families"
