---
description: "Tail-risk identification needs a bounded raw (1+ε)-moment on arm distributions: without it CVaR is unlearnable, while VaR needs no such restriction."
aliases: ["(1+ε)-moment restriction", "bounded raw moment class", "moment-restricted arm class", "heavy-tailed arm class with a moment bound"]
sources: ["doi-10-48550-arxiv-2008-07606"]
---
# Moment-bounded arm class

Tail-risk quantities such as CVaR are set by the far tail of a distribution, and a small probability can hide an arbitrarily large loss. Whether a best-arm question about such quantities can be answered at all therefore depends on how heavy the candidate distributions are allowed to be. The paper answers this by restricting the arm distributions to a class in which a raw moment of order 1+ε is bounded by a constant B, with ε and B positive. It calls this "a mild and standard raw (1 + )-moment restriction".[^c1]

**Why the restriction is needed.** Without it, CVaR cannot be learned. The paper says that "the CVaR problem is unlearnable in full generality", and that on the class of all arm distributions "any δ-correct algorithm requires an infinite number of samples in expectation" to identify the best arm among finitely many.[^c2] The mechanism is a cheap perturbation. An arm's distribution can be changed by a tiny amount in KL divergence by "shifting an arbitrarily small mass from the lower tail to the extreme right", which satisfies a CVaR constraint while costing almost no information.[^c3] The lower bound on samples then vanishes: "Thus, without any restrictions" the quantity that sets the constant is zero.[^c4]

**What the bound does.** The moment restriction closes that route. The paper states that "the moment-constraint limits the minimum and maximum possible" values of VaR and CVaR.[^c5] Both quantities then lie in a bounded interval whose width depends on B and ε, so a perturbation cannot push the tail arbitrarily far while staying close in KL. This is the property that makes the CVaR problem a finite-sample problem.

**What VaR does not need.** The VaR problem does not use this class. The paper says "We solve the VaR problem for arbitrary arm distributions".[^c6] So the moment restriction is a property of the CVaR objective, not of tail risk in general. Within canonical one-parameter exponential families the restriction is also unnecessary for the target, since the tail ordering follows the mean ordering.[^c7]

**Why heavy tails are the setting.** The paper's motivation is that "the underlying probability distributions are heavy-tailed" in finance and safety-critical settings.[^c8] For stock returns, "extensive research suggests" a tail index in a range the paper gives as [2, 5] for 1+ε; for daily exchange rates and income or wealth distributions the index can lie in (1, 2].[^c9] Those are the regimes where the mean is a poor summary and where the moment class has bite.

## Limits

- B is not identifiable from data. The paper says that "it is easy to arrive at distributions" whose moments are arbitrarily far apart while their KL divergence is arbitrarily close to zero, and "This makes it difficult to infer" B from a sample.[^c10] The distributions are not separated by the samples the algorithm sees.
- The paper's workaround is pragmatic: "One may take a pragmatic view and approximate B by estimating" the moment from observed samples and padding it up. It accepts that "it may be inaccurate and lead to sub-optimal allocations in our algorithm".[^c11] Justifying the approximation would need further distributional assumptions, which the paper says would face similar problems. The guarantee is therefore conditional on a B that the method does not verify.
- The sensitivity is measured: the experiments report that "the sample complexity is also sensitive to B".[^c12]
- Only an upper bound on one moment is imposed. Two distributions with the same bound can have very different CVaR, and the text does not claim the class is minimal or that it is the weakest restriction under which CVaR becomes learnable. That question is not tested here.
- The text read does not compare this restriction with others. Bounded support, as used in the EVaR setting, is a different restriction and the two are not interchangeable (see Related).
- Whether the moment restriction is the right idealisation for a question-asking setting is my inference, not the paper's. The point that may carry over is that a risk target can be undefined over an unrestricted family of distributions, so the family must be stated before the question is.

## Related

- [[cvar-best-arm-identification]] — the problem this class makes learnable; its sample-cost constant is defined over this class.
- [[entropic-value-at-risk]] — the EVaR setting restricts to distributions on a bounded interval rather than to a moment bound, so the two restrictions cover different distributions.
- [[variance-constrained-best-arm-identification]] — assumes bounded rewards, which is the bounded-support counterpart; a moment class is the heavy-tailed alternative (my inference on the relation).

[^c1]: doi-10-48550-arxiv-2008-07606 — "we impose a mild and standard raw"
[^c2]: doi-10-48550-arxiv-2008-07606 — "the CVaR problem is unlearnable in full generality"
[^c3]: doi-10-48550-arxiv-2008-07606 — "shifting an arbitrarily small mass from the lower tail to the extreme right"
[^c4]: doi-10-48550-arxiv-2008-07606 — "Thus, without any restrictions"
[^c5]: doi-10-48550-arxiv-2008-07606 — "the moment-constraint limits the minimum and maximum possible"
[^c6]: doi-10-48550-arxiv-2008-07606 — "We solve the VaR problem for arbitrary arm distributions"
[^c7]: doi-10-48550-arxiv-2008-07606 — "finding the best-(CVaR/VaR/mean-CVaR) arm reduces to finding the arm with the minimum mean"
[^c8]: doi-10-48550-arxiv-2008-07606 — "the underlying probability distributions are heavy-tailed"
[^c9]: doi-10-48550-arxiv-2008-07606 — "For stock returns, extensive research suggests that"
[^c10]: doi-10-48550-arxiv-2008-07606 — "This makes it difficult to infer"
[^c11]: doi-10-48550-arxiv-2008-07606 — "it may be inaccurate and lead to sub-optimal allocations in our algorithm"
[^c12]: doi-10-48550-arxiv-2008-07606 — "the sample complexity is also sensitive to B"
