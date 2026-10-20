---
description: "Adding a second signal such as CoT length, tied to ability through a correlated latent speed, tightens ability estimates beyond accuracy alone; the gain grows with the correlation's size."
aliases: ["latency-response theory", "hierarchical IRT-RT model", "joint accuracy and response-time model", "speed-accuracy joint model", "CoT length as response time"]
sources: ["arxiv-2512-07019"]
---
# Ability-speed correlation as collateral information

A binary correct/incorrect response carries one bit about a respondent's ability. A second process measurement, taken on the same trial, can carry more about that ability when the two latent traits are linked. The Latency-Response Theory (LaRT) model makes the link explicit. It "jointly models both the response accuracy" and the length of the chain of thought (CoT), and it adds "a key correlation parameter between the latent ability and the latent speed".[^c1] Accuracy follows an item response model with a probit link, so the probability of a correct answer depends on the ability θ. The log of the CoT length is normal with mean ω − φτ, where τ is a latent speed, and the pair (θ, τ) is bivariate normal with correlation ρ. The paper states that "the off-diagonal entry of Σ is denoted by ρ, so that Σ is essentially a correlation matrix".[^c2]

The mechanism is simple. A length observed for model i is evidence about τ_i. Because τ is correlated with θ, that evidence shifts the estimate of θ as well. When ρ = 0 the length is uninformative about ability and the model reduces to ordinary IRT. The paper's precision result says the asymptotic precision of θ increases with |ρ|: "the variance decreases as |ρ| increases and is maximized at ρ = 0", where "the IRT case where CoT information is ignored" sits.[^c3] So the same accuracy data yields tighter ability intervals when a correlated process signal is also recorded. The paper's simulations and real-data runs report shorter confidence intervals and better estimation accuracy than IRT on the same responses.

The sign of the link is an empirical matter. On the authors' benchmark data the estimated ρ is "negative, confirming that LLMs with stronger math reasoning ability have longer CoT".[^c4] The stronger model reasons longer, so the length is a signal that correlates with ability rather than a separate quantity. The gain therefore comes from the population relation, not from the length being a measure of effort in itself. The paper takes the hierarchical framework's stance: it "treats response time as an observable process signal linked to latent traits" and "does not commit to a particular cognitive mechanism".[^c5]

The length model is a computational convenience. The log-normal "serves as an asymptotic approximation to common count distributions" when counts are large, and the authors report that "in our applications fewer than 1% of the CoT are shorter than 10".[^c6]

## Limits

- The precision result is an asymptotic-variance statement, derived from an asymptotic normality theorem for the latent traits. The gain at a finite number of items is shown by simulation, not by the formula. (My reading of the theorem's scope; the paper does not spell out the finite-sample case in the quoted part.)
- The gain is zero at ρ = 0. A population in which reasoning length is unrelated to accuracy, or a model family that decouples the two, would give nothing from this mechanism. The paper's ρ is estimated on its own benchmarks and LLM set.
- Identifiability holds only up to a sign, which the authors fix by requiring positive sums of discriminations; it needs "at least three items that differentiate the latent ability and at least three items that differentiate the latent speed".[^c7]
- Latent traits are assumed independent across LLMs: "We make the assumption of prior independence for the latent traits in the current LaRT framework".[^c8] Models from one family would violate this, and the paper leaves that extension open.
- The work is restricted to binary responses: "we focus on binary (correct/incorrect) LLM responses".[^c9] Graded or multi-attempt responses, and CoT content rather than CoT length, are not modelled.
- The evidence is one group's benchmark data plus simulations. It does not show that longer CoT means more reasoning, only that length and accuracy co-vary across models.

## Related

- [[pairwise-confidence-adaptive-ranking]] — adaptive ranking estimates each model's ability from its answers alone; a correlated speed term is a second signal that could sharpen the same estimate (my inference, not tested there).
- [[simulated-respondent-icc]] — IRT parameters for LLM evaluation taken from simulated respondents; that note changes where the item parameters come from, while this one changes the measurement model for the respondent.

[^c1]: arxiv-2512-07019 — "which jointly models both the response accuracy"
[^c2]: arxiv-2512-07019 — "the off-diagonal entry of Σ is denoted by ρ, so that Σ is essentially a correlation matrix"
[^c3]: arxiv-2512-07019 — "the variance decreases as |ρ| increases and is maximized at ρ = 0"
[^c4]: arxiv-2512-07019 — "negative, confirming that LLMs with stronger math reasoning ability have longer CoT"
[^c5]: arxiv-2512-07019 — "treats response time as an observable process signal linked to latent traits"
[^c6]: arxiv-2512-07019 — "the log-normal distribution serves as an asymptotic approximation to common count"
[^c7]: arxiv-2512-07019 — "Condition 1 ensures LaRT identifiability only up to a sign indeterminacy"
[^c8]: arxiv-2512-07019 — "We make the assumption of prior independence for the latent traits in the current LaRT framework"
[^c9]: arxiv-2512-07019 — "we focus on binary (correct/incorrect) LLM responses"
