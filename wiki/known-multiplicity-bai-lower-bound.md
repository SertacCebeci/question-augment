---
description: "Best-arm identification with a known number M of tied optimal arms has a sample lower bound tighter than the unknown-M bound, because the alternative must beat all M optima."
aliases: ["known-cardinality lower bound", "multi-optimal characteristic time", "tie-aware lower bound", "known-number-of-optimal-arms lower bound"]
sources: ["doi-10-48550-arxiv-2505-15643"]
---
# Known-multiplicity best-arm lower bound

In fixed-confidence best-arm identification the target is not one fixed arm but any member of the set of optimal arms. The learner must reach an output in that set with probability at least 1 − δ while spending as few samples as possible.[^c1] The classical instance-dependent lower bound was built for a unique optimum: "classical lower bounds assume a unique best arm."[^c2] When there are M tied optima and M is known in advance, the bound changes shape.

The bound says what any δ-correct strategy must pay on a given bandit. What it must pay is set by the alternatives, the bandits it must be able to tell apart from the true one. Here an alternative is one in which some non-optimal arm a has a mean above every one of the M optima; the paper writes this family with conditions such as "(λa > λ1) ∧ (λa > λ2)" continued over all tied arms.[^c3] (My reading of the displayed definition, which the text extraction garbles.)

The main statement is that for any δ-PAC strategy, the expected sample size is at least T*(µ) times kl(1 − δ, δ), where T*(µ) is a value obtained by optimizing over sampling proportions on the arms and over the alternatives.[^c4] As δ goes to zero, kl(1 − δ, δ) behaves like log(1/δ), so the asymptotic form bounds the expected sample size divided by log(1/δ) from below by T*(µ).

The mechanism, as I read the construction: the cost of an alternative is a weighted sum of KL divergences over the M tied arms and the challenger a. The tied arms enter as a group. The bound does not charge the strategy for telling the tied arms apart from one another, only for making the challenger lose to the group. That is where knowing M enters. The paper motivates the setting by noting that "standard algorithms may over-sample to distinguish between" arms that are equally optimal.[^c5]

Against the unknown-M bound of Degenne and Koolen, the paper claims the new bound is "strictly tighter than previous bounds."[^c6] Its later remark reads: "This highlights that knowing M can improve the" sample complexity.[^c7]

## Limits

- The bound is asymptotic in δ and is stated for one-parameter exponential families.[^c8] The finite-δ form is in terms of kl(1 − δ, δ) and holds for any δ-PAC strategy, but the constants were not checked.
- The paper assumes K > M. The case M = K is trivial, since any arm is then optimal.[^c9]
- What the text establishes is a lower bound. Whether a strategy attains it is a separate claim, treated in [[tie-aware-glr-stopping-rule]].
- "Strictly tighter" is the paper's claim. I did not find a numerical comparison in the sections I read, and the displayed formulas are garbled in the extraction, so I checked the structure of T* and of the alternative set rather than every constant.
- The bound assumes M is known exactly. What happens under a wrong M is not addressed in the sections I read (my observation).
- Whether any of this transfers to question-asking, where answers are not independent draws from an exponential family, is my inference and is untested here.

## Related

- [[pac-best-arm-sample-complexity-lower-bound]] — the uniform bound over n arms that holds for any sampler; this one is instance-dependent and depends on the optimal set, including its size M.
- [[tie-aware-glr-stopping-rule]] — the stopping rule that the paper shows attains this bound asymptotically.

[^c1]: doi-10-48550-arxiv-2505-15643 — "The goal is to identify any one arm in A⋆ with high probability"
[^c2]: doi-10-48550-arxiv-2505-15643 — "classical lower bounds assume a unique best arm"
[^c3]: doi-10-48550-arxiv-2505-15643 — "(λa > λ1 ) ∧ (λa > λ2 )"
[^c4]: doi-10-48550-arxiv-2505-15643 — "Then, for any δ-PAC strategy, it holds that"
[^c5]: doi-10-48550-arxiv-2505-15643 — "standard algorithms may over-sample to distinguish between"
[^c6]: doi-10-48550-arxiv-2505-15643 — "knowledge and is strictly tighter than previous bounds"
[^c7]: doi-10-48550-arxiv-2505-15643 — "This highlights that knowing M can improve the"
[^c8]: doi-10-48550-arxiv-2505-15643 — "For a one-parameter exponential family with density"
[^c9]: doi-10-48550-arxiv-2505-15643 — "The case M = K is trivial when M is known in advance,"
