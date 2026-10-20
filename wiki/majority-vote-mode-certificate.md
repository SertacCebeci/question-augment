---
description: "Majority vote over n independent samples estimates an answer distribution's mode; its error falls exponentially in n, at a rate set by the mode margin and the signal-to-noise ratio of the margin."
aliases: ["self-consistency", "majority-vote self-consistency", "majority-vote mode estimation", "Condorcet jury rule for sampled answers"]
sources: ["doi-10-48550-arxiv-2510-17472"]
---
# Majority-vote mode certificate

Draw n answers X1, …, Xn independently from one terminal distribution p over a finite set of final answers, and return the most frequent one. Self-consistency is this estimator applied to an LLM's sampled final answers. Its target is the mode of p. Under 0–1 loss the vote is the Bayes-optimal estimator of that mode,[^c1] so the question a certificate answers is how probable it is that the vote has already found the mode. The bounds the paper derives use Hoeffding, Bernstein and Chernoff–Markov inequalities,[^c2] and they give that probability as a function of n and of the mode margin δ, the gap between the two leading answer probabilities: "these bounds clarify how reliability scales with the ensemble size and with the mode margin."[^c3] The paper adds that these bounds are "not tight in the small-sample regime".[^c4]

Asymptotically the error decays exponentially in n: "the error probability decays exponentially in n."[^c5] The rate is set by the signal-to-noise ratio of the margin variable Δ = 1{X = c⋆} − 1{X = j⋆}. The paper defines it through the margin δ and the leader's own mass, "Motivated by the Gaussian bound we define the signal-to-noise ratio (SNR) by".[^c6] In my reading, an answer that leads its nearest rival by a wide gap makes Δ positive on most draws, so the vote settles after few samples; a near-tie leaves the sign of Δ close to a coin flip, and the vote needs many more draws. The paper's own summary is the same: the rate "is the SNR of the margin", and the same quantity controls the stopping rule and the training objectives discussed in [[anytime-valid-majority-stopping]] and [[consensus-reward-tilting]].

The certificate needs no verifier and no label. It needs the answer distribution to have a leader that is well separated from its rivals.

## Limits

- The Section 2 bounds are for an oracle setting: "We analyse an oracle setting where the terminal answer distribution" is known.[^c7] Estimating p from the same rollouts is the job of the stopping rule, not of these bounds.
- The guarantees assume i.i.d. rollouts and a unique mode. Violations such as ties "weaken guarantees and are handled adaptively by MMC", and the paper's own limitations section says "Our analysis assumes conditionally independent rollouts given a fixed prompt and context."[^c8]
- Answers must be binned into classes before they can be counted. For free text this "would still require some degree of response canonicalisation."[^c9] The paper does not measure how much binning error enters the bound.
- The certificate is about the vote matching the mode, not about the mode being correct. The paper frames the mode as the "optimal model-relative prediction", so a model that is confidently wrong gets a high-margin certificate for a wrong answer.[^c10] That consequence is my inference, not a result the paper states.
- The paper's experiments are on single-turn math benchmarks; the finite-sample bounds are not checked empirically in the section read.

## Related

- [[anytime-valid-majority-stopping]] — turns the fixed-n error bound into a rule that decides when to stop sampling, without fixing n in advance.
- [[self-consistency-difficulty-score]] — uses the same vote agreement as a difficulty signal; this bound is what agreement alone does not supply.
- [[consensus-reward-tilting]] — the training-side route to enlarging the margin on which this bound depends.

[^c1]: doi-10-48550-arxiv-2510-17472 — "From a statistical standpoint, majority voting is the Bayes-optimal estimator of"
[^c2]: doi-10-48550-arxiv-2510-17472 — "leveraging Hoeffding, Bernstein, Chernoff"
[^c3]: doi-10-48550-arxiv-2510-17472 — "these bounds clarify how reliability scales with the ensemble size and with the mode margin"
[^c4]: doi-10-48550-arxiv-2510-17472 — "Although not tight in the small-sample"
[^c5]: doi-10-48550-arxiv-2510-17472 — "the error probability decays exponentially in n"
[^c6]: doi-10-48550-arxiv-2510-17472 — "Motivated by the Gaussian bound we define the signal-to-noise ratio (SNR) by"
[^c7]: doi-10-48550-arxiv-2510-17472 — "We analyse an oracle setting where the terminal answer distribution"
[^c8]: doi-10-48550-arxiv-2510-17472 — "Our analysis assumes conditionally independent rollouts given a fixed prompt and context"
[^c9]: doi-10-48550-arxiv-2510-17472 — "this would still require some degree of response canonicalisation"
[^c10]: doi-10-48550-arxiv-2510-17472 — "recovering the mode is the optimal model-relative prediction"
