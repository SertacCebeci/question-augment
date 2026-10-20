---
description: "LLM agents can follow the optimal explore-or-commit rule when a prior and costs are stated, but prompting and RL alone collapse to static policies; supplying the prior restores adaptivity."
aliases: ["Calibrate-Then-Act", "CTA", "cost-aware exploration", "explore-or-commit under cost"]
sources: ["arxiv-2602-16699"]
---
# Explicit-prior cost-aware exploration

An agent that may gather information (retrieve, run a test, read a file) before committing faces a sequential decision. Each exploration step multiplies the final reward by a discount below one, and the commit step pays only if the answer is right. The optimal rule compares the cost of one more step with the value of the information it buys, so it needs a prior over the latent state the agent cannot see.

## The decision rule

In the Pandora's Box variant, one of K boxes holds the prize and the agent may verify a box (paying discount gamma) or commit. The stated optimum is to commit when the posterior of the best box exceeds gamma, and otherwise verify the most probable remaining box.[^c1] For optional retrieval QA the oracle retrieves whenever the post-retrieval accuracy discounted by gamma is at least the direct-answer accuracy.[^c2] In the file-reading coding task, latent formatting attributes (delimiter, quote character, skipped rows) must be inferred; unit tests and code runs each carry a discount, so a high cost ratio rho favors testing first.[^c3]

## Calibrate, then act

The method splits the problem in two: estimate the prior first (model confidence for QA, a trained format predictor for code), then hand it to the agent in the prompt. The authors state the idea as decoupling "the calibration of uncertainty" from action selection.[^c4] The same agent is then either prompted (CTA-Prompted) or RL-trained (CTA-RL).

## What was measured

- Even a small thinking model (Qwen3-8B) can follow the optimal policy on Pandora's Box once priors and costs are explicit; without priors or with thinking disabled, optimal-match rates are low.[^c5]
- In QA, the non-thinking prompted agent "retrieves almost always in all cost regimes", a cost-insensitive habit; the thinking agent drops to a recall heuristic (answer if a candidate comes to mind) and does not turn its own confidence into numbers.[^c6]
- In file reading, prompted and RL agents both "collapse to a static test-first policy rather than adapting across cost regimes", with 0% code-first traces.[^c7]
- Giving the prior makes behavior adaptive and puts CTA-RL on or near the Pareto frontier across cost regimes, which standard RL does not reach.[^c8]

The reading: the failure is not missing reasoning ability but missing a quantified belief; RL on the task does not extract that belief from training statistics.

## Limits

- Tasks are synthetic or narrow (a toy box game, single-retrieval QA, CSV loading with three attributes); costs are multiplicative discounts, not real latency or money.
- The prior is supplied by an estimator the authors build; how well a deployed agent can calibrate itself, or how errors in the prior propagate to the decision, is not established by the claims above.
- QA confidence is a point estimate (a Dirac delta), so value of information over a spread-out belief is not tested.
- Only Qwen3-8B was the base model for the QA and file-reading experiments; generality across models is unverified here. The reading that "no quantified belief" is the cause is the authors' interpretation of behavioral traces, not an intervention on internals.

## Related

- [[bayesian-self-escalation]] — same threshold-on-a-posterior structure, applied to escalating to a stronger model
- [[bayesian-fixed-confidence-optimal-stopping]] — optimal stopping on a posterior, the formal sibling of the commit rule
- [[implicit-escalation-threshold]] — agents hold thresholds implicitly rather than computing them, as the prompted agents here do

[^c1]: arxiv-2602-16699 — "commit if its posterior probability of a box is greater than γ"
[^c2]: arxiv-2602-16699 — "the oracle policy retrieves whenever the expected discounted accuracy after"
[^c3]: arxiv-2602-16699 — "as ρ increases, code attempts become relatively more costly, and a rational agent will tend to"
[^c4]: arxiv-2602-16699 — "which decouples the calibration of uncertainty"
[^c5]: arxiv-2602-16699 — "Without explicit priors or when the thinking"
[^c6]: arxiv-2602-16699 — "retrieves almost always in all cost regimes, reflecting a conservative and cost-insensitive strategy"
[^c7]: arxiv-2602-16699 — "collapse to a static test-first policy rather than adapting across cost regimes"
[^c8]: arxiv-2602-16699 — "CTA pushes the model towards adaptive, optimal decision making in both task settings."
