---
description: "Best-arm identification with a covariate seen before each pull targets the highest covariate-marginalized mean, not the per-context best; the covariate can only lower the sample-complexity bound."
aliases: ["contextual BAI", "best-arm identification with contextual information", "marginalized-mean best arm", "covariate-assisted best-arm identification"]
sources: ["doi-10-48550-arxiv-2106-14077"]
---
# Contextual best-arm identification

In fixed-confidence best-arm identification, a learner pulls arms until it can name the arm with the highest mean at a stated error rate, using as few pulls as possible. In the contextual version, a covariate X_t is observed before each arm is chosen, and the reward distribution of each arm depends on it. The mechanism that matters is the target. The best arm is the one with the highest mean averaged over the covariate distribution, and the authors say the aim is "not the mean reward conditioned on contexts."[^c1] They also say their "primary interest is not in the mean reward" within each context.[^c2] The same arm can therefore win marginally while losing inside some contexts, and an algorithm that names the best arm context by context answers a different question.

The information that enters is side information. The covariate is not the object of the question, but it can still be used to decide which arm to sample and how to read the samples. The authors assume the covariates are drawn "independent and identically distributed" across rounds.[^c3] Under that assumption, the marginal mean of an arm is the average over the covariate distribution of its per-context means, so the learner has to allocate pulls over (arm, context) pairs rather than over arms alone.

What the covariate changes is the sample complexity. The authors derive an instance-specific lower bound on the expected stopping time of any delta-PAC strategy. The bound is a sup over allocations, of an inf over alternative models, of a sum over contexts weighted by the context distribution. Its contextual form is never larger than the non-contextual bound: "suggesting that a faster BAI may be possible" is the authors' phrasing,[^c4] and they summarise it as "the contextual information either helps or does not harm the BAI."[^c5] Read literally, the bound can only drop when a covariate is added. The paper does not claim that every covariate drops it. The lower bound is a sup-inf formula, so a reader cannot compute it from the abstract alone.

The lower bound is attained in two settings. The first is two arms with rewards and covariate jointly Gaussian, where the "two-armed Gaussian bandits where the arms and context jointly" follow a multivariate normal law.[^c6] The second is finite contexts with rewards from a one-parameter exponential family, where a tracking algorithm matches the bound (see [[contextual-track-and-stop]]). In both, the expected number of arm draws "asymptotically matches the lower bound."[^c7] The allocation that achieves the bound need not be unique. The authors note that the estimated allocations converge to the set of optimal allocations "even though they might not converge to a point."[^c8]

The non-contextual reference point is the instance-specific bound of Garivier and Kaufmann, which is sharper than the uniform PAC bound in [[pac-best-arm-sample-complexity-lower-bound]]. The gain described here is also instance-specific: it depends on the covariate-reward structure of the particular problem, not on the number of arms alone.

## Limits

- The matching algorithms cover two cases only: a two-armed Gaussian problem and finite contexts with exponential-family rewards. For general continuous contexts the paper gives a lower bound, not an algorithm that attains it.
- Optimality is asymptotic. The matching statements concern the expected number of draws in the limit, not a finite-sample bound (my reading of the statements, which the abstract phrases as asymptotic).
- The finite-context optimality result assumes the context distribution is known: "the parameters of the context distribution are known."[^c9]
- The setting requires covariates that are observed before the choice and that are i.i.d. across rounds. The paper does not treat adversarial or drifting covariates.
- The claim that the covariate never hurts is a comparison of bounds. The paper does not show by experiment that every covariate gives a measurable gain, and I did not check the constants in its appendix.
- Related work on contextual pure exploration (Tekin and van der Schaar; Guan and Jiang; Deshmukh et al.) addresses the same kind of setting, but, as the authors say, "they do not discuss the instance-specific optimality."[^c10]

## Related

- [[pac-best-arm-sample-complexity-lower-bound]] — the uniform PAC bound without context; this note's bound is instance-specific and depends on the problem
- context-residual-variance-gain — the mechanism by which a covariate lowers the bound in the Gaussian case
- [[contextual-track-and-stop]] — the tracking rule that attains the bound for finite contexts
- [[cost-aware-best-arm-identification]] — another change to the best-arm lower bound, here a cost per pull rather than a covariate
- [[unimodal-allocation-sparsity]] — another structural restriction on the optimal allocation, in a setting without covariates

[^c1]: doi-10-48550-arxiv-2106-14077 — "not the mean reward conditioned on contexts"
[^c2]: doi-10-48550-arxiv-2106-14077 — "our primary interest is not in the mean reward"
[^c3]: doi-10-48550-arxiv-2106-14077 — "We assume that Xt is independent and identically distributed"
[^c4]: doi-10-48550-arxiv-2106-14077 — "suggesting that a faster BAI may be possible"
[^c5]: doi-10-48550-arxiv-2106-14077 — "the contextual information either helps or does not harm the BAI"
[^c6]: doi-10-48550-arxiv-2106-14077 — "two-armed Gaussian bandits where the arms and context jointly"
[^c7]: doi-10-48550-arxiv-2106-14077 — "number of arm draws asymptotically matches the lower bound"
[^c8]: doi-10-48550-arxiv-2106-14077 — "even though they might not converge to a point"
[^c9]: doi-10-48550-arxiv-2106-14077 — "the parameters of the context distribution are known"
[^c10]: doi-10-48550-arxiv-2106-14077 — "they do not discuss the instance-specific optimality"
