---
description: "Scoring each query as expected entropy reduction minus latency and congestion cost, and halting when the best score is non-positive, beats stopping rules that ignore cost-aware choice of what to ask."
aliases: ["cognitive friction", "triadic cognitive architecture", "net-utility stopping", "bounded deliberation"]
sources: ["arxiv-2603-30031", "arxiv-2512-14040"]
---
# Cost-priced joint selection and stopping

> Which question to ask next and when to stop asking are one decision, priced
> in the same currency: information bought minus delay and load incurred.

## Mechanism

Wang et al.'s Triadic Cognitive Architecture (arxiv-2603-30031) treats a tool-using agent as holding a belief over hypotheses plus a congestion state, and querying tools that return noisy evidence. Each prospective query is scored by a belief-dependent benefit, the [[value-of-information]] measured as expected entropy reduction, against two environment-dependent costs, spatial (live congestion plus the action's load) and temporal (delay). The discrete version is a net utility:

> "U (a; bt , t, Ct ) = d ∆H(a | bt ) − α λS (Ct + Ω(a)) + β (t + τ (a))"

The paper's own prose gives the rule: the controller picks the action with the highest net utility and halts when even the best query has non-positive net value.[^c1] The continuous-time formulation is an optimal-stopping problem (a Hamilton-Jacobi-Bellman variational inequality over belief and congestion); the experiments use a myopic one-step approximation that omits continuation value.[^c2] Information value is estimated by Monte Carlo rollouts: clone the belief, sample an observation, update, and record the entropy drop.[^c3]

## What was measured

In a synthetic emergency-diagnosis testbed (EMDG), a greedy ReAct agent that maximises entropy reduction only picked the slow, high-load MRI network at step 0 in every seed, while the cost-priced controller picked the fast Hematology Lab in every seed.[^c4] The paper explains the baseline's failure as lacking a stopping rule that compares marginal entropy reduction with time-sensitive viability loss, so it keeps querying when entropy is already low.[^c5] Reported over 200 seeds, deliberation time fell from 114.5 to 14.5 steps and terminal viability rose from 56.8 to 93.0, with accuracy saturated at 1.00 for both (so the difference is attributed to stopping and selection quality, not inference).[^c6]

The key control is that stopping alone does not explain the gain. Two baselines kept the greedy MRI selection and added a calibrated stopping rule (entropy threshold; fixed query count matched to the controller's mean). The paper concludes:

> "results indicate that selection and stopping must be optimized jointly; stopping alone is insufficient under high-latency tool profiles."[^c7]

A fixed budget of three MRI queries did worse than unconstrained ReAct (viability 50.9 against 56.8), because three slow queries exhaust the time budget.[^c8]

A second measurement, on a different task, is a chart-reading agent that also scores each tool by an information-gain term minus a per-call cost weight, under a call budget. ChartAgent's scheduler starts from the rule that "We score each tool by its expected information gain (EIG)", with the cost-gain trade-off set by a weight and a budget.[^c9] On a ChartBench subset the cost weight does not act monotonically. Raising it from 0.0 to 0.2 "reduces the average number of tool invocations from 9.8 to 6.1" while accuracy rose from 77.3% to 78.6%.[^c10] At the largest weight tested, "the scheduler turns overly conservative," making about 4.3 calls and losing accuracy.[^c11] A budget of three calls gave "yielding 73.2% accuracy with 3.0 tool invocations."[^c12] So in this agent a cost-priced rule has an interior optimum in the weight, and the budget is a second lever. The sweep varied one parameter at a time with the other at its default, and the test is one benchmark, so it does not show the joint selection-and-stopping result above.

## Limits

- Everything is simulated: a small, deliberately accuracy-saturated testbed plus a second synthetic environment. Nothing here is a human or real-LLM asker; the mapping of belief to model logits and cost to API latency is proposed, not tested.
- Costs are assumed known and fixed per tool, and weights (alpha, beta, lambda) are hand-set; sensitivity is swept univariately only.
- The deployed rule is myopic; the HJB optimality claim applies to the continuous idealisation, and a gap to the discrete controller is acknowledged by the paper.
- The "viability" metric decays with time by construction, so the advantage of avoiding delay is partly built into the environment. That the effect transfers to settings where delay is cheap is my inference, not shown.
- Rollout VOI is costly in large tool sets; amortisation is suggested only.

## Related

- [[value-of-information]] — the benefit term of the utility.
- [[planner-dynamic-stopping]] — a learned sufficiency judgement versus this explicit priced rule.
- [[cost-optimal-query-policy]] — another account of choosing queries under cost.
- [[friction-functional]] — a different, unrelated use of "friction" (epistemic risk of a response), not this spatial and temporal cost.

[^c1]: arxiv-2603-30031 — "The controller chooses the action maximizing net utility and halts when even the best"
[^c2]: arxiv-2603-30031 — "This myopic stopping rule omits continuation value"
[^c3]: arxiv-2603-30031 — "each rollout clones the current belief, samples a Dirichlet-likelihood observation,"
[^c4]: arxiv-2603-30031 — "At step 0, greedy ReAct selects MRI_Network in 100% of seeds, whereas the triadic"
[^c5]: arxiv-2603-30031 — "The baseline lacks a stopping rule that compares marginal entropy reduction"
[^c6]: arxiv-2603-30031 — "Accuracy is intentionally saturated"
[^c7]: arxiv-2603-30031 — "results indicate that selection and stopping must be optimized jointly; stopping alone is insufficient under high-latency tool profiles."
[^c8]: arxiv-2603-30031 — "Fixed-K performs worse than unconstrained ReAct (50.9 vs. 56.8) because forcing three"
[^c9]: arxiv-2512-14040 — "We score each tool by its expected information gain (EIG)"
[^c10]: arxiv-2512-14040 — "reduces the average number of tool invocations from 9.8 to 6.1"
[^c11]: arxiv-2512-14040 — "the scheduler turns overly conservative"
[^c12]: arxiv-2512-14040 — "yielding 73.2% accuracy with 3.0 tool invocations"
