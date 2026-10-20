---
description: "Query the inputs where the two extremal consistent surrogates, one maximising and one minimising a metric, disagree most; the surrogate only has to rank candidates, not copy the black box."
aliases: ["bound-disagreement sampling", "extremal-surrogate disagreement", "top-k bound disagreement"]
sources: ["arxiv-2601-03087"]
---
# Bound-disagreement query selection

Once an auditor holds a version-space interval (see [[version-space-metric-interval]]), it has two hypotheses for free: the one that pushes the metric up and the one that pushes it down. The selection rule scores each unqueried input x by the gap between them, dist(x) = |h_max(x) − h_min(x)|, and queries the top-k scorers on the black box.[^c1] In my reading, the rationale is that the metric's bound is least determined where the two extremes disagree. The paper's figure caption says the chosen queries shrink the distance between the bounds in those regions, "between the lower and upper in high-disagreement regions."[^c2]

The step that matters is the choice of top-k over an ε-driven loop. The paper states that it adopts "top-k rather than" the disagreement loop of Yan and Zhang (2022), which iterates until the surrogate's own diameter falls below a threshold.[^c3] That loop needs the surrogate to copy the black box, since "Such schemes require the surrogate to reliably mimic the black box." The paper's top-k needs less: "This is a strictly weaker requirement as it demands" a consistent ordering of candidates rather than accurate scores.[^c4] It reports that the rule "remains effective even under partial surrogate" agreement with the black box's scores, and it puts the point where the surrogate starts to mimic the black box at roughly 500 to 750 queries in its own setting.[^c9]

Two details matter for the estimate, not for the rule. The queried set is not a random sample, so the paper applies "distributional regularisation" using subgroup and label marginals "to mitigate selection-induced bias in fairness estimation."[^c5] The rule also has a Bayesian-optimisation counterpart, which the paper says "searches over" acquisition features that include bound disagreement, as a proxy for uncertainty.[^c10] The two are close: "Both approaches, however, seem to work similarly well."[^c6]

The measured comparison uses the same two case studies as the interval note. On Bias-in-Bios at the strict threshold ε = 0.02, the disagreement variant performed "with disagreement performing" slightly better than the Bayesian one.[^c8] The paper summarises the trade-off as "prioritises fast early interval shrinkage, while BO" tending to give better mid-budget accuracy.[^c7]

## Limits

- The paper evaluates the rule on one metric, ΔAUC, and on two datasets with a small BERT surrogate. Whether ranking by bound disagreement works for other fairness metrics is not tested here.
- The claim that top-k needs only a consistent ranking is argued from the structure of the rule and checked only in the paper's own setting. It is not a measured property of surrogate families in general.
- Selection by the widest-disagreement inputs is greedy. The paper does not show that the top-k batch is the best k-batch, nor that the rule beats random sampling after the budget is spent; the cumulative-error comparison is the evidence offered.
- My inference: because the rule concentrates queries where the two extremes disagree, inputs far from the surrogate's decision boundary can be starved, so the regularisation step is doing real work and is not an afterthought.

## Related

- [[version-space-metric-interval]] — the interval whose two extremal hypotheses this rule reads.
- [[rashomon-committee-querying]] — also picks queries by disagreement among models in an ε-version space, but by vote entropy over a Gibbs-weighted committee; this rule uses only the two extremes of the metric, which is a different and smaller object.
- [[active-testing]] — also chooses which items to spend a budget on, but scores by the inputs alone and corrects the resulting selection bias by reweighting; this rule scores by where the metric's bound is open.

[^c1]: arxiv-2601-03087 — "by scoring each unqueried candidate via the disagreement of"
[^c2]: arxiv-2601-03087 — "between the lower and upper in high-disagreement regions"
[^c3]: arxiv-2601-03087 — "We adopt top-k rather than"
[^c4]: arxiv-2601-03087 — "This is a strictly weaker requirement as it demands"
[^c5]: arxiv-2601-03087 — "mitigate selection-induced bias in fairness estimation"
[^c6]: arxiv-2601-03087 — "Both approaches, however, seem to work similarly well,"
[^c7]: arxiv-2601-03087 — "prioritises fast early interval shrinkage, while BO"
[^c8]: arxiv-2601-03087 — "with disagreement performing"
[^c9]: arxiv-2601-03087 — "holds only after roughly 500–750 queries in"
[^c10]: arxiv-2601-03087 — "we test Bayesian optimisation which searches over"
