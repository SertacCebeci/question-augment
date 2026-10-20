---
description: "A Beta posterior whose pseudo-counts decay by a factor γ each step: effective sample size settles at 1/(1−γ), so the belief variance keeps a positive floor instead of vanishing."
aliases: ["Beta-Bernoulli with forgetting factor", "exponentially forgetting Beta posterior", "discounted Bayesian filter", "exponential forgetting filter"]
sources: ["arxiv-2512-20884", "arxiv-2512-18489", "doi-10-7554-elife-81256"]
---
# Forgetting-factor Beta-Bernoulli belief

An agent holds its belief in a proposition as a Beta(α, β) distribution, where α and β are pseudo-counts of positive and negative evidence. A forgetting factor γ, with 0 ≪ γ < 1 (the paper's example is γ = 0.99), multiplies the old counts before each new binary observation y_t ∈ {0, 1} is added: α_t = γα_{t−1} + y_t and β_t = γβ_{t−1} + (1 − y_t). The mechanism is a geometric discount: "This factor exponentially decays the weight of old observations while incorporating new evidence."[^c1]

Summing the two updates gives a recurrence for the total weight N_t = α_t + β_t, namely N_t = γN_{t−1} + 1. Each step adds exactly one unit of evidence and removes a fraction 1 − γ of what is already held. The total therefore has a fixed point, N_eq = 1/(1−γ), and stops growing. The paper puts it as the effective sample size "stabilises instead of growing to infinity".[^c2] Without the discount (γ = 1), N grows with t, and as N grows the variance of a Beta posterior falls toward zero. That is the static case the paper sets out to escape. The statement that the variance goes to zero is my reading of the variance formula below, not a quoted result.

The paper measures epistemic uncertainty as the variance of the belief, Var(θ) = αβ / ((α+β)²(α+β+1)). Two consequences follow from it. At fixed N the variance is largest when α = β, that is when E[θ] = 0.5; the paper calls this the state of "maximum ambiguity" where the agent should learn most. And because N is capped, the variance cannot fall to zero in a non-trivial environment. The paper states that "the variance converges to a non-zero" lower bound δ(γ) > 0.[^c3]

My own arithmetic, not the paper's: with the mean θ fixed and N at N_eq, Var = θ(1−θ)/(N+1), so the floor is θ(1−θ)(1−γ)/(2−γ). At γ = 0.999 and θ = 0.5 that is about 2.5 × 10⁻⁴. The floor is set by the chosen γ and by the mean; it is not an estimate of anything in the environment. The step from "highest variance" to "largest expected reduction in uncertainty" is a different claim. The paper states it as a "known property of this model that this state of maximum prior" variance is also the state from which one observation helps most, with no citation in the text.[^c4] The variance formula supports the first half; the second half is asserted.

## Transfer and nearby methods

The update is the Beta-Bernoulli conjugate posterior of [[thompson-sampling]], whose guarantees are stated for a stationary θ. The discount is one of two ways to track a moving θ. The other, used in [[learnability-posterior-curriculum]], keeps only the last µ observations per node. A discount keeps every past observation but weights it geometrically; a window drops old observations at once. The paper does not compare the two.

The same discount can be read as a tempering of the posterior rather than as a count decay. Arxiv-2512-18489 writes the forgetting step as one in which the belief "tempers the posterior belief" before each new observation, that is, the posterior is raised to the power γ.[^c10] Its endpoints are described as "memory, while γ → 0 approaches a memoryless state."[^c11] For a Beta posterior, raising the density to the power γ scales the excess counts α−1 and β−1 by γ, which is the count decay above up to a constant offset. That correspondence is my inference, not the paper's.

What the note above leaves open is where γ comes from. The later paper does not set it by hand. It chooses γ* by minimising the total KL divergence between a language model's predictive distribution at each step and the predictive distribution of the discounted filter, solved with L-BFGS-B.[^c12] A fitted value below one "provides direct evidence of discounting."[^c13] This is an estimate from a trajectory, not a rule for choosing γ before any data arrive, so the hand-set limit below still stands. The same paper reports that for every model it tested "the fitted γ ∗ is significantly below 1."[^c14]

A second source for the discount is a cost on the precision of the belief itself, not a choice made by hand. Prat-Carrabin and colleagues write the cost of a belief "as the negative of its entropy", and minimise a divergence from the Bayesian posterior plus that cost.[^c16] The minimiser raises the product of prior and likelihood to the power 1/(λ+1) at each step, which is the tempering reading given above, now derived from a cost. Unrolled, an observation k trials back carries weight (1/(λ+1))^k. That expansion is my reading of their Equation 6, so in this note's notation γ = 1/(λ+1). The paper says the result "amounts to an exponential discount of remote observations"[^c17], and that it derives the forgetting "as an optimal solution to a problem of constrained inference" rather than positing it.[^c18] This partly answers the hand-set limit below: γ becomes a function of a cost weight λ. It does not remove the free parameter, since λ is itself chosen, and the paper fits it to each subject's predictions, "of each subject, by maximizing their likelihoods."[^c19] The precision-cost family is contrasted with a bias-inducing cost in [[unpredictability-cost-belief-bias]].

## Limits

- Simulation only. The environment is "k = 100 independent propositions"[^c5] whose truth is a Bernoulli stream with one flip, from θ* = 0.8 to θ* = 0.2 at t = 501. No LLM agent, forum or retrieval step is run, although the abstract says "Simulation results validate this" architecture.[^c6]
- Propositions are treated as independent, and feedback as binary. The paper says the framework "relies on two simplifying assumptions", and the correlated and soft-evidence cases are discussed but not analysed.[^c7]
- γ is a hand-set parameter. The paper calls it a "direct, quantifiable trade-off"[^c8] between memory and adaptation, and gives no rule for choosing it. Its three example values (1.0, 0.999, 0.95) are chosen for the figures.
- The step from "a variance floor exists" to "the agent has a motive to act" is a reading, not a theorem. A decaying memory keeps variance positive whether or not the agent acts, so the floor alone does not show that acting lowers it. This is my inference.
- Epistemic caching, which evicts a proposition when its effective count falls below a threshold ("We define a significance threshold Nmin"[^c9]), is described as a variant of least-recently-used eviction. No hit rate, memory use or retrieval accuracy is reported for it.
- Exponential forgetting treats a real change and random noise alike: both lower the weight of old evidence at the same rate. The paper does not test whether the forgetting rate can tell drift from noise.
- The cost-based derivation has its weight fitted, not tested against a rival. The authors read the cross-condition correlation of fitted weights as a stable subject trait, "instead of varying with the stimulus probability."[^c20] One binary task supports that reading; nothing here shows the same weight across other tasks or non-binary feedback.
- The fitted γ* in the language-model study belongs to one model and one probe. Its trajectory has a single abrupt change, "with a parameter changepoint at t = 51"[^c15]. A γ* fitted this way describes that trajectory; it does not show a stable memory length across other changes, and gradual drift is not tested. This reading of the probe design is my inference.

## Related

- [[thompson-sampling]] — the same conjugate Beta-Bernoulli posterior, with stationary θ assumed
- [[learnability-posterior-curriculum]] — a sliding window over recent observations, the alternative way to forget
- [[expected-information-gain]] — the information-maximising score that the paper's variance argument is meant to approximate; no equivalence is shown here
- [[uncertainty-sampling-regime-shift-lag]] — the query rule that targets this variance, and how it fares after a flip
- [[update-misspecification-divergence]] — splits a language model's error into its updating and its fitted discount family, using the same discount as the reference filter
- [[unpredictability-cost-belief-bias]] — the other cost family in the same framework: it biases the belief toward predictable environments instead of discounting old evidence
- [[attractive-repulsive-sequential-effects]] — the prediction pattern the precision-cost discount produces, including a repulsive lag-three effect

[^c1]: arxiv-2512-20884 — "This factor exponentially decays the weight of old observations while incorporating new evidence."
[^c2]: arxiv-2512-20884 — "stabilises instead of growing to infinity"
[^c3]: arxiv-2512-20884 — "the variance converges to a non-zero"
[^c4]: arxiv-2512-20884 — "known property of this model that this state of maximum prior"
[^c5]: arxiv-2512-20884 — "k = 100 independent propositions"
[^c6]: arxiv-2512-20884 — "Simulation results validate this"
[^c7]: arxiv-2512-20884 — "relies on two simplifying assumptions"
[^c8]: arxiv-2512-20884 — "direct, quantifiable trade-off"
[^c9]: arxiv-2512-20884 — "We define a significance threshold Nmin"
[^c10]: arxiv-2512-18489 — "tempers the posterior belief"
[^c11]: arxiv-2512-18489 — "memory, while γ → 0 approaches a memoryless state."
[^c12]: arxiv-2512-18489 — "discount factor γ ∗ by minimizing the total KL divergence"
[^c13]: arxiv-2512-18489 — "provides direct evidence of discounting."
[^c14]: arxiv-2512-18489 — "the fitted γ ∗ is significantly below 1"
[^c15]: arxiv-2512-18489 — "with a parameter changepoint at t = 51"
[^c16]: doi-10-7554-elife-81256 — "as the negative of its entropy"
[^c17]: doi-10-7554-elife-81256 — "amounts to an exponential discount of remote observations"
[^c18]: doi-10-7554-elife-81256 — "we derive it as an optimal solution to a problem of constrained inference"
[^c19]: doi-10-7554-elife-81256 — "of each subject, by maximizing their likelihoods"
[^c20]: doi-10-7554-elife-81256 — "instead of varying with the stimulus probability"
