---
description: "A GLLR stopping rule for known M optima tests every M-subset of arms against the rest and stops when one subset dominates, so tied arms need not be separated."
aliases: ["GLLR stopping rule", "tie-aware Track-and-Stop stopping rule", "M-subset generalized likelihood ratio test"]
sources: ["doi-10-48550-arxiv-2505-15643"]
---
# Tie-aware GLR stopping rule

A fixed-confidence learner "chooses a stopping time τ and outputs a recommendation" once the data are sufficient.[^t1] The paper's baseline for a unique optimum is a likelihood-ratio design: "Track-and-Stop algorithm stands out for its principled foundation based on likelihood ratio statistics."[^t2] Truong's change is in what the stopping statistic compares. With the number M of optima known, the candidates are M-subsets of arms rather than single arms.

For each M-subset and each arm a outside it, the rule forms a generalized-likelihood-ratio statistic. It uses the counts and KL divergences of arm a and of the subset's members, measured against a pooled mean for the group. This is my reading of the displayed formula, which the text extraction garbles. The statistic is then maximized over subsets and minimized over the outside arms. The rule stops at the first time this combined statistic passes a threshold: "Next, we use the following stopping rule"[^t3] with the threshold written as "β(t, δ) is an exploration rate to be adjusted."[^t4] The paper's threshold depends on the number of arms K and on M. The decoding step then takes the recommended arm from the winning subset.

The structure is what makes ties cheap. The statistic commits only when one group of M arms is ahead of every challenger. Nothing requires the arms inside the winning group to be separated from each other. This matches the lower bound in [[known-multiplicity-bai-lower-bound]], which charges the strategy for the challenger, not for ordering the tied arms. The paper's motivation is that ordinary rules "may over-sample to distinguish between" equally optimal arms.[^t5]

Sampling is handled by the Track-and-Stop design of the earlier literature. "We adopt the same sampling rules as described in [3," the paper says, and "The core idea is to match the optimal sampling" proportions by tracking a plug-in estimate of them.[^t6] Plug-in tracking alone can discard an arm too early, so the rule enforces exploration: "enforce sufficient exploration across all arms to ensure fast" convergence of the means.[^t7] A second rule, D-Tracking, is offered as "An alternative, often more practical rule."[^t8] The paper states that "Both sampling rules are guaranteed to ensure that the empirical sampling proportions converge to the optimal allocation,"[^t9] and this convergence is taken from the earlier work rather than reproved.

The optimality claim is asymptotic and in expectation. The paper's section heading is "Asymptotic Optimality in Expectation,"[^t10] and the conclusion says the modified algorithm, "equipped with an appropriate stopping rule based on generalized log-likelihood ratio" statistics, "achieves this bound asymptotically."[^t11] The abstract puts it as: "we propose a modified, tieaware stopping rule and prove that it achieves asymptotic" instance-optimality.[^t12]

## Limits

- Optimality is asymptotic and in expectation, and it is proved for exponential families.[^t13] Finite-δ behaviour is controlled only through the threshold, and I did not verify its constants.
- The rule requires M to be known exactly. The sections I read do not cover a misspecified M (my observation).
- The displayed statistic and threshold are garbled in the extracted text. I describe their structure, not their constants.
- The convergence of the sampling proportions is cited from prior work, so the guarantee rests on that result as well as on this paper's proof.
- I did not find a simulation of the stopping rule in the sections I read. The abstract's "practical guidance" is therefore untested here.
- The analysis concerns independent draws from bandit arms. Whether a question-asking process with dependent, non-stationary answers satisfies the same structure is my inference, not something the paper shows.

## Related

- [[known-multiplicity-bai-lower-bound]] — the lower bound this rule attains asymptotically; the stopping rule is the matching upper-side construction.
- [[plug-in-glr-stopping-rule]] — another GLR stopping rule with a calibrated boundary. That one handles unknown sampling variance in contextual pairwise tests; this one handles tied optima in a bandit.
- [[stopping-rules]] — the general sequential-stopping note this rule is one instance of.
- [[pac-best-arm-sample-complexity-lower-bound]] — the uniform PAC bound that no adaptive sampler beats in order, which the instance-dependent analysis here refines.

[^t1]: doi-10-48550-arxiv-2505-15643 — "the learner chooses a stopping time τ and outputs a recommendation"
[^t2]: doi-10-48550-arxiv-2505-15643 — "Track-and-Stop algorithm stands out for its principled foundation based on likelihood ratio statistics"
[^t3]: doi-10-48550-arxiv-2505-15643 — "Next, we use the following stopping rule"
[^t4]: doi-10-48550-arxiv-2505-15643 — "β(t, δ) is an exploration rate to be adjusted"
[^t5]: doi-10-48550-arxiv-2505-15643 — "standard algorithms may over-sample to distinguish between"
[^t6]: doi-10-48550-arxiv-2505-15643 — "The core idea is to match the optimal sampling"
[^t7]: doi-10-48550-arxiv-2505-15643 — "enforce sufficient exploration across all arms to ensure fast"
[^t8]: doi-10-48550-arxiv-2505-15643 — "An alternative, often more practical rule is D-Tracking,"
[^t9]: doi-10-48550-arxiv-2505-15643 — "Both sampling rules are guaranteed to ensure that the empirical sampling proportions converge to the optimal allocation,"
[^t10]: doi-10-48550-arxiv-2505-15643 — "Asymptotic Optimality in Expectation"
[^t11]: doi-10-48550-arxiv-2505-15643 — "statistics—achieves this bound asymptotically."
[^t12]: doi-10-48550-arxiv-2505-15643 — "we propose a modified, tieaware stopping rule and prove that it achieves asymptotic"
[^t13]: doi-10-48550-arxiv-2505-15643 — "Let µ be a bandit model from an exponential"
