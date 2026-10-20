---
description: "Contextual Track-and-Stop tracks a plug-in optimal allocation over arm-context pairs and stops on a GLR statistic; with finite contexts it is asymptotically optimal."
aliases: ["CTS", "contextual Track-and-Stop", "context-aware Track-and-Stop", "tracking rule over arm-context pairs"]
sources: ["doi-10-48550-arxiv-2106-14077"]
---
# Contextual Track-and-Stop

Track-and-Stop is a fixed-confidence best-arm rule with three parts: a sampling rule that moves the pull proportions toward the optimal allocation, a stopping rule that halts when the evidence for the leading arm passes a threshold, and a recommendation rule that names the arm. The authors state that their algorithm "is an extension of the Track-and-Stop (TS) algorithm by Garivier and Kaufmann (2016)" for the case of a finite number of contexts.[^c1] The extension changes what is tracked. The allocation is over (arm, context) pairs, not over arms, and the statistics are the context-weighted means of the marginal target (see [[contextual-best-arm-identification]]).

The sampling rule works in three steps. The unknown means and context frequencies are replaced by running estimates. The optimal allocations for those estimates are computed, which the authors describe as tracking "the optimal allocations in the plug-in estimate."[^c2] When a context arrives, the rule first samples any arm that has fallen behind for that context, an under-sampling check that the authors call forced exploration. Otherwise it pulls the arm whose cumulative weight for that context most exceeds its pull count. The forced exploration is "an extension of D-tracking" of Garivier and Kaufmann, and the authors report it is "superior to their C-tracking" in practice.[^c3]

The stopping rule is a generalized likelihood-ratio statistic over the contextual model. The statistic compares, for each arm, the weakest of its pairwise tests against the other arms, and takes the largest such value over arms. The algorithm stops when that value crosses a threshold beta(t, delta). The authors use the stopping criterion of Kaufmann and Koolen, "which refines the stopping rule of Garivier and Kaufmann (2016)."[^c4] The recommendation is the arm with the largest context-weighted empirical mean. The paper shows the rule is delta-PAC. My reading is that the tracking condition is what carries the sample count toward the contextual lower bound. The paper says the sampling rule "can keep the allocation close to the optimal allocations," which is the property the optimality proof uses.[^c5]

In a Bernoulli experiment with two contexts and four arms, the authors compare the contextual rule with plain Track-and-Stop on the same marginal means as Garivier and Kaufmann. The contextual rule's statistic grows faster after the early rounds, and the authors say "This figure indicates that the CTS algorithm achieves" a smaller sample complexity, "as suggested by the theoretical results."[^c6] In the first rounds the contextual statistic is smaller than the plain one. The authors attribute this to the number of parameters, which "is proportional to the number of contexts," so the contextual rule needs more samples before its estimates settle.[^c7]

## Limits

- The algorithm is stated for finite contexts. The authors say "algorithm for the case of finite context" and handle continuous covariates in a different way, with a two-armed Gaussian rule (see context-residual-variance-gain).
- Computing the allocation requires solving a maximin problem at each round. The authors say "If the number of contexts and arms is very large, it may be difficult to solve."[^c8] My reading is that the cost grows with the number of pairs, but the paper does not report run times.
- The optimality statement needs the context distribution to be known in the corollary that gives the constant: "the parameters of the context distribution are known."[^c9] The experiments do not say how the context frequencies are estimated in the rule itself.
- The optimality results are asymptotic in the error rate (delta going to zero) and in the tracking condition. The experiment is a single small Bernoulli scenario with two contexts, so it does not show the size of the gain across instances.
- The early-round lag is a finite-sample effect that the paper names but does not quantify. A user with few samples per context should expect the contextual rule to be slower at first, on the paper's own account.
- The stopping rule is the GLR family of the plain algorithm, with the context-weighted statistics in place of the arm means. The paper does not establish that the GLR boundary used here is the tightest one available.

## Related

- [[contextual-best-arm-identification]] — the problem this rule solves: the marginal mean is the target, and the allocation is over arm-context pairs
- context-residual-variance-gain — the two-armed Gaussian case, where the paper uses alpha-elimination instead of tracking
- [[tie-aware-glr-stopping-rule]] — another Track-and-Stop stopping statistic, here for tied optima
- [[plug-in-glr-stopping-rule]] — a plug-in GLR stopping rule with a self-normalized boundary, a different threshold than the one used here
- [[unimodal-allocation-sparsity]] — another case where the optimal allocation has a restricted support, in a setting without covariates

[^c1]: doi-10-48550-arxiv-2106-14077 — "The strategy is an extension of the Track-and-Stop (TS) algorithm by Garivier"
[^c2]: doi-10-48550-arxiv-2106-14077 — "the optimal allocations in the plug-in estimate"
[^c3]: doi-10-48550-arxiv-2106-14077 — "superior to their C-tracking"
[^c4]: doi-10-48550-arxiv-2106-14077 — "which refines the stopping rule of Garivier and Kaufmann (2016)"
[^c5]: doi-10-48550-arxiv-2106-14077 — "the sampling rule can keep the allocation close to the optimal allocations"
[^c6]: doi-10-48550-arxiv-2106-14077 — "This figure indicates that the CTS algorithm achieves"
[^c7]: doi-10-48550-arxiv-2106-14077 — "parameters to be estimated is proportional to the number of contexts"
[^c8]: doi-10-48550-arxiv-2106-14077 — "If the number of contexts and arms is very large, it may be difficult to solve"
[^c9]: doi-10-48550-arxiv-2106-14077 — "the parameters of the context distribution are known"
