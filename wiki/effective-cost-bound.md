---
description: "Predicted search cost is the bits an agent must acquire over the bits each action gains, times the cost per action; under stated assumptions it lower-bounds expected cost."
aliases: ["effective cost", "C_eff", "ACP effective cost", "information-to-cost search cost", "a priori solvability cost"]
sources: ["arxiv-2512-07631"]
---
# Effective cost of an information search

Before searching, an agent can ask how much information its answer needs. The work's quantity is the entropy of the goal indicator under the prior. If the goal set holds a fraction p of the candidates, the requirement is the binary entropy of p, largest at p = 1/2, so that "Problems with rare solutions require more information than those with abundant solutions."[^c1] Each action gives an expected gain, the [[mutual-information]] between its outcome and the goal indicator, and it costs C_s.[^c2] The effective cost divides the requirement by the gain per action and multiplies by the cost per action: C_eff = (I_total / I_s) × C_s.[^c3] The solvability criterion is that an agent with budget B can solve the problem only if B ≥ C_eff.[^c4] The estimate uses only the problem's structure and the agent's capabilities, so it exists before the first action.

**What is bounded.** Let each action add a gain X_i to a running sum, and stop at the first n where the sum reaches I_total. The model takes the outcomes to be conditionally independent given the history, with bounded second moments and diminishing expected gains, "Diminishing returns: expected gains satisfy" µ_1 ≥ µ_2 ≥ … ≥ µ_inf > 0.[^c5] Optional stopping on the sum minus its expectation then gives E[sum of the stopped gains] = E[sum of µ_i up to N]. Each µ_i is at most the initial gain I_s = µ_1, so the expected number of steps is at least I_total / I_s, and the expected cost is at least C_eff. The upper side adds the overshoot, the amount by which the sum passes I_total. The expected overshoot is bounded using "for independent non-identically distributed variables bounds expected overshoot," which gives E[C] ≤ C_s(I_total/µ_inf + M_2/µ_inf²), with M_2 the largest second moment of the gains.[^c6] The lower bound is the part the work calls practical: "no strategy can do better on average."[^c7]

**High-probability reading.** When each gain is bounded by M, Hoeffding's inequality gives a step count that finishes with probability at least 1 − δ. The work says this lets one set "reserves proportional to log(1/δ)" for missions where overrunning a budget is costly.[^c8] The expected-cost bound answers a different question from the tail bound, and a budget that must not be exceeded needs the tail one.

**Evidence.** Two experiments are reported. In the first, an agent identifies the slope of a noisy line y = ax + ε by choosing query points, with a Gaussian-process surrogate estimating both quantities and an LLM agent making the queries. "The ACP estimate consistently lower-bounds" the steps needed, and the gap grows with noise.[^c9] In the second, backtracking search for 3-colourings of random graphs G(n, p) with n up to 15 runs over 750 instances, with the ACP agent using C_eff only to order its choices. Across those instances, "ACP always satisfies the lower-bound condition."[^c10]

## Limits

- The bound is proved under the stochastic model in §3.1: conditionally independent outcomes, bounded moments and decreasing expected gains. The text does not check these for an LLM agent. Its two agent tests are one noisy linear task and one graph family, both with a known structure. Whether a language model's answers give gains with that shape is not shown (my inference).
- The lower bound is stated with µ_1, the largest expected gain, while the definition of C_eff averages the gains "under the optimal policy." The text does not reconcile the two. When gains fall fast, µ_1 sits far above the average, so the bound is valid but loose (my inference).
- Definition 2.4 picks the action with the highest expected gain per unit cost, and the text says this "maximizes information gained per resource spent."[^c11] The theorem bounds the cost of whatever policy runs; the text does not show that the greedy ratio minimises expected cost.
- The gap between the two sides is governed by M_2/µ_inf², which the work calls a signal-to-noise ratio. Where it is large, the upper bound says little.
- The quantities are estimated. The Monte Carlo error is a Hoeffding bound on sampled gains, and the surrogate error is a sketch rather than a proof. The work itself says: "Practical solvability tests should include this margin."[^c12]
- The approximation extension is not tested. Relaxing the goal "reduces information requirements," and an NP-hard inapproximability result would make the predicted cost infinite for unreachable accuracy.[^c13] Those are statements about the formula, with no experiment behind them.
- "The framework generalizes across LLM-based and agentic workflows" is a claim of the work, not a measurement beyond its two tasks.[^c14]

## Related

- [[entropy]] — the requirement I_total is the binary entropy of the goal indicator, the only form the work uses.
- [[mutual-information]] — the per-action gain I_s is the mutual information between an outcome and the goal indicator.
- [[expected-information-gain]] — the numerator of the ratio rule in Definition 2.4; the ratio itself, gain per unit cost, is what this note adds.
- [[voi-per-cost-modality-selection]] — also ranks actions by gain per unit cost, but gives no bound on the total cost of a search.
- [[stopping-rules]] — its four rules do not include an expected-cost bound; this note gives one for a threshold on cumulative gain.
- [[sprt]] — Wald's test minimises the expected number of observations under its own error model; the bound here rests on different assumptions (diminishing expected gains, not a two-hypothesis likelihood ratio).
- [[rate-distortion-theory]] — relaxing the goal lowers the information requirement, the same trade that a fidelity target makes in rate-distortion.

[^c1]: arxiv-2512-07631 — "Problems with rare solutions require more information than those with abundant solutions."
[^c2]: arxiv-2512-07631 — "the mutual information between the outcome and goal indicator."
[^c3]: arxiv-2512-07631 — "When actions have uniform cost, Ceffective simplifies to the number of steps times cost per step."
[^c4]: arxiv-2512-07631 — "An agent with budget B can solve a problem if"
[^c5]: arxiv-2512-07631 — "Diminishing returns: expected gains satisfy"
[^c6]: arxiv-2512-07631 — "for independent non-identically distributed variables bounds expected overshoot"
[^c7]: arxiv-2512-07631 — "no strategy can do better on average"
[^c8]: arxiv-2512-07631 — "setting reserves proportional to log(1/δ)"
[^c9]: arxiv-2512-07631 — "The ACP estimate consistently lower-bounds"
[^c10]: arxiv-2512-07631 — "ACP always satisfies the lower-bound condition"
[^c11]: arxiv-2512-07631 — "This policy maximizes information gained per resource spent"
[^c12]: arxiv-2512-07631 — "Practical solvability tests should include this margin."
[^c13]: arxiv-2512-07631 — "Inapproximability manifests as infinite predicted cost for unattainable accuracy levels"
[^c14]: arxiv-2512-07631 — "The framework generalizes across LLM-based and agentic workflows"
