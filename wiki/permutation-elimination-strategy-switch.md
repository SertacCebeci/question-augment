---
description: "In a causal attribution task, LLMs shift from testing each candidate pair to pruning the hypothesis space as candidates grow; XOR-type rules block the shift because single trials prune little."
aliases: ["permutation vs elimination strategy", "pair testing versus hypothesis pruning"]
sources: ["doi-10-48550-arxiv-2602-10329"]
---
# Permutation versus elimination strategy switch

Finding the pair of variables that determines an outcome from input-output trials can be done in two ways. The permutation strategy "iterates over all N2 candidate pairs and checks their consistency across all trials". The elimination strategy "processes each trial to incrementally prune incompatible pairs".[^e1] Both have the same worst-case cost, O(T × N²), and "they differ in cognitive demands and empirical efficiency".[^e2] Permutation holds one hypothesis at a time; elimination must keep the whole surviving hypothesis space: it "requires updating and maintaining a global hypothesis space", so its load is higher.[^e3]

The mechanism is pruning power. A trial pays off under elimination when it removes many hypotheses at once. For conjunctive rules a single positive trial can do this. For XOR-type rules "they do not allow for rapid pruning of the variable space through single observations".[^e4] So the value of maintaining a hypothesis space depends on the logic of the rule, not only on how large the space is.

The study generated "3000 variable attribution samples spanning 10 logical functions", with N from 3 to 16 candidate variables and T set near the minimum needed to identify the pair.[^e5] Across DeepSeek R1 and V3 and Qwen3 Thinking and Instruct, the authors "observed a clear phase transition in strategy selection": permutation dominates while N is small (below about 4), and elimination takes over as N grows.[^e6] In a logistic fit, the best model uses the log size of the hypothesis space and the trial count with an interaction, "yielded the best fit" with AIC 2727.29 and pseudo R² 0.160.[^e7] The log-space coefficient is positive[^e14] and the trial coefficient is negative.[^e15] In the authors' reading, "When more trials are available, the model tends to slightly fall back on the simpler permutation strategy".[^e8] More observations lower the value of pruning and pull the choice back toward permutation.

The divergence is on the rule. DeepSeek moves only moderately toward elimination for XOR and XNOR, while "the Qwen family almost entirely eschews elimination for XOR-like logical functions".[^e9]

The paper's ratio ρ = 2T/N² fits worse than the log-size-by-trials model. Its Table 1 caption reads "Model comparison for predicting the frequency of applying the elimination strategy".[^e10] The paper calls ρ the "Information Ratio". This is not the bandit notion [[information-ratio]], which is a different object.

## Limits

- Strategy is labelled by an LLM judge, Kimi-K2-Instruct. "The LLM-based judge achieved an accuracy of 0.86", with Cohen's kappa 0.76 against 100 human-labelled responses. That is substantial agreement, not exact labelling.[^e11]
- The authors say the trial-count effect is not clear-cut: "the relationship between the proportion of elimination and the T is unclear since the data is unbalanced".[^e12] The coefficient sign is reported, but the marginal shape is not settled.
- The fit explains a modest share of the variation: pseudo R² is 0.160 for the best model.
- One synthetic task and one family of Boolean rules. The authors say the setup "can be mapped to multiple forms of reasoning",[^e13] but no such mapping is tested. The human analogue (students who prune versus test, cited from Varma et al. 2018) is background, not a test here.
- The switch is a frequency across samples, not a per-item decision rule.

## Related

- [[test-time-scaling]] — the reasoning-token setting in which the strategy is visible.
- [[resource-rationality]] — the cost-utility account this switch is read through.
- [[bounded-rationality]] — the older satisficing account of search under cost; it gives a stopping threshold where this switch weighs a maintenance cost.
- [[information-ratio]] — a different ratio with the same name, from bandit regret; not the same object as ρ here.

[^e1]: doi-10-48550-arxiv-2602-10329 — "iterates over all N2 candidate pairs and checks their consistency across all trials"
[^e2]: doi-10-48550-arxiv-2602-10329 — "they differ in cognitive demands and empirical efficiency"
[^e3]: doi-10-48550-arxiv-2602-10329 — "the elimination strategy requires updating and maintaining a global hypothesis space"
[^e4]: doi-10-48550-arxiv-2602-10329 — "they do not allow for rapid pruning of the variable space through single observations"
[^e5]: doi-10-48550-arxiv-2602-10329 — "3000 variable attribution samples spanning 10 logical functions"
[^e6]: doi-10-48550-arxiv-2602-10329 — "we observed a clear phase transition in strategy selection"
[^e7]: doi-10-48550-arxiv-2602-10329 — "yielded the best fit"
[^e8]: doi-10-48550-arxiv-2602-10329 — "tends to slightly fall back on the simpler permutation strategy"
[^e9]: doi-10-48550-arxiv-2602-10329 — "the Qwen family almost entirely eschews elimination for XOR-like logical functions"
[^e10]: doi-10-48550-arxiv-2602-10329 — "Model comparison for predicting the frequency of applying the elimination strategy"
[^e11]: doi-10-48550-arxiv-2602-10329 — "The LLM-based judge achieved an accuracy of 0.86"
[^e12]: doi-10-48550-arxiv-2602-10329 — "the relationship between the proportion of elimination and the T is unclear since the data is unbalanced"
[^e13]: doi-10-48550-arxiv-2602-10329 — "This is a very general setup that can be mapped to multiple forms of reasoning"
[^e14]: doi-10-48550-arxiv-2602-10329 — "This is supported by a strong positive coefficient"
[^e15]: doi-10-48550-arxiv-2602-10329 — "This is reflected in the negative coefficient for trial count"
