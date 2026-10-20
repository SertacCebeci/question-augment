---
description: "Weitzman's Pandora's Box: each costly-to-open option has a reservation price, the outside value where opening it breaks even; opening in descending order of these prices is optimal."
aliases: ["Pandora's Box", "Weitzman reservation price", "search with costly inspection", "non-obligatory inspection", "backup price"]
sources: ["doi-10-48550-arxiv-2608-20316"]
---
# Pandora's box with reservation prices

A decision-maker faces $M$ boxes, each with a value "known to her only in distribution",[^p1] and opening box $m$ costs $c_m$. She may stop at any time and keep the best value seen so far. This is the classical model of search with costly inspection, and its solution rests on one scalar per box.

The reservation price $u_m$ is the outside-option value $v$ at which the expected gain from opening box $m$ exactly pays its cost: $\mathbb{E}[(V_m - u_m)^+] = c_m$.[^p2] The intuition is direct. If the best value found so far is $v$, opening box $m$ has net expected payoff $\mathbb{E}[(V_m - v)^+] - c_m$, and this is positive "when the expected upside exceeds the cost".[^p3] Inspection pays exactly when the current best is below the reservation price. The quantity is a net-of-cost gain whose sign decides whether to look, the same shape as the [[value-of-information]] rule, with an outside option in place of an action set.

For the obligatory-inspection variant, where the box finally chosen must be opened, the policy needs only the prices. Pandora "opens the boxes in descending order of their reservation prices", and stops once the best value seen exceeds the highest reservation price among the boxes still unopened.[^p4] The source states the consequence as "reservation prices alone determine the optimal policy".[^p5] The search is sequential, because each opened box can change which remaining inspections still justify their cost.[^p6]

The non-obligatory variant lets her take an unopened box without paying its cost, accepting that its value may disappoint.[^p7] Its optimal adaptive policy is NP-hard, so the tractable route restricts to committing policies. One box is held out as a sealed option, valued at its backup price: "the outside option that makes Pandora indifferent to committing to the sealed box sight-unseen" versus paying to inspect it.[^p8] The backup price is a different object from the reservation price. The source notes that the two coincide in ordering only on one side of a cost threshold: "For costs exceeding this threshold (very expensive boxes), the inequality reverses."[^p9]

Under a Gaussian model, where the value of a box given the cheap signals is normal with a predicted mean $\mu$ and spread $\sigma$, the value of opening against an outside option $v$ becomes $(\mu - v)\Phi(\alpha) + \sigma\phi(\alpha)$ with $\alpha = (\mu - v)/\sigma$. This is "the expectation of a Gaussian censored at" $v$, and the reservation price "can be obtained by simple root-finding" on it.[^p10][^p11] The closed form is a property of the Gaussian assumption, not of box problems in general.

What survives the transfer to any setting is the structure: rank by reservation price, inspect while the best seen is below the top remaining price, and commit. What the formulas need is a known distribution for each box, a known inspection cost, and, in the classical statement, boxes that are independent of one another.

## Limits

- The optimality result assumes the box distributions are known and the boxes are independent. The paper's own routing application flags that its policies assume this: "must contend with an additional complication: the hidden values of the boxes are" correlated in practice.[^p12] Once they are learned or correlated, the optimum is not established by these formulas.
- The Gaussian form is an approximation: "real box values are rarely strictly Gaussian".[^p13] The paper reports that a non-Gaussian alternative did not improve routing success or inspection cost in its experiments.[^p14] That is one set of domains, not a general result.
- The non-obligatory policy is not the optimum. It is a restriction "to committing policies" chosen because the adaptive optimum is intractable.[^p15] How far the restriction falls short is not bounded in the text read here. (This note's reading.)
- The source's experiments are routing and inference-time tasks; no claim about human questioners or stopping in dialogue is made or tested.

## Related

- [[value-of-information]] — the reservation rule is a net-of-cost inspection rule with an outside option in place of an action set.
- [[stopping-rules]] — the Pandora stop ("the best seen exceeds every remaining price") is one more answer to when to stop gathering.
- [[cost-priced-joint-selection-and-stopping]] — also halts once the best net score is non-positive, but its score is linear in the gain rather than a reservation price.
- [[explicit-prior-cost-aware-exploration]] — LLM agents told a prior on a Pandora's Box game; its rule is a posterior threshold, not a reservation price.
- [[costly-value-estimation-routing]] — the routing instance: specialists as boxes, costly value estimates as what opening reveals.

[^p1]: doi-10-48550-arxiv-2608-20316 — "each with a hidden value which is known to her only in distribution"
[^p2]: doi-10-48550-arxiv-2608-20316 — "is the outside-option value at which this net value is exactly zero"
[^p3]: doi-10-48550-arxiv-2608-20316 — "which is positive when the expected upside exceeds the cost"
[^p4]: doi-10-48550-arxiv-2608-20316 — "Pandora opens the boxes in descending order of their reservation prices"
[^p5]: doi-10-48550-arxiv-2608-20316 — "Weitzman (1979) showed that reservation prices alone determine the optimal policy"
[^p6]: doi-10-48550-arxiv-2608-20316 — "acquired so far will help determine whether the remaining inspections still justify their cost"
[^p7]: doi-10-48550-arxiv-2608-20316 — "any unopened box, committing to it without paying the inspection cost"
[^p8]: doi-10-48550-arxiv-2608-20316 — "is the outside option that makes Pandora indifferent to committing to the sealed box sight-unseen"
[^p9]: doi-10-48550-arxiv-2608-20316 — "For costs exceeding this threshold (very expensive boxes), the inequality reverses."
[^p10]: doi-10-48550-arxiv-2608-20316 — "the expectation of a Gaussian censored at"
[^p11]: doi-10-48550-arxiv-2608-20316 — "can be obtained by simple root-finding on Equation (5)"
[^p12]: doi-10-48550-arxiv-2608-20316 — "must contend with an additional complication: the hidden values of the boxes are"
[^p13]: doi-10-48550-arxiv-2608-20316 — "real box values are rarely strictly Gaussian"
[^p14]: doi-10-48550-arxiv-2608-20316 — "does not yield an improvement in overall routing success and inspection cost"
[^p15]: doi-10-48550-arxiv-2608-20316 — "so we use a tractable restriction to committing policies"
