---
description: "Neyman allocation splits samples between two arms in proportion to their standard deviations; for fixed-budget best-arm identification it attains the exact two-arm minimax constant."
aliases: ["Neyman optimal allocation", "standard-deviation-proportional allocation", "plug-in Neyman allocation"]
sources: ["doi-10-48550-arxiv-2506-24007"]
---
# Neyman allocation

Neyman allocation is a rule for splitting a fixed sample budget across arms: each arm receives a share proportional to its outcome standard deviation, not an equal share. In the fixed-budget best-arm setting the proportions are the thing being chosen. "The sampling proportions are proportional to the estimated standard deviations."[^c1] It is not the Neyman–Pearson lemma in [[neyman-pearson-lemma]], which concerns tests; the shared name is the only link between them in this text.

What it buys is visible in the Bernoulli case, where the variances at a near tie are almost equal. Under equal sampling, the standard deviation of the scaled difference between two sample means is set by the sum of the two variances. Under Neyman allocation, "whereas under Neyman allocation the corresponding" quantity is the sum of the two standard deviations, and the gap between the two squared values is of order T^-1 along a near tie.[^c2] So the Neyman split makes the difference of the sample means as precise as the variance structure allows, in the limit.

The sharper statement is about the constant. For two arms, "attained asymptotically by the deterministic Neyman allocation" is the strategy that reaches the exact minimax constant for simple regret, with the empirical-best arm recommended at the end.[^c3] The text adds that "together with the empirical-best recommendation, and no sampling rule that adapts" to the observed outcomes improves that constant. So for two arms the best one can do in the limit is a fixed, variance-proportional split; reacting to outcomes buys nothing at the constant level.[^c4] The closed form that results is described in [[minimax-simple-regret-constant]].

The allocation needs the standard deviations, which depend on the unknown means. The procedure in the paper handles this with a pilot: "a pilot phase whose fraction of the total budget converges to zero" is spent first, and the variances are estimated from it. "It estimates the variances needed for allocation from the pilot observations."[^c5] The pilot is a vanishing share of the budget, so it does not change the leading constant, but its estimation error is handled only in the asymptotic analysis.

## Limits

- The closed-form optimality is for two arms. For three or more arms the sampling rule is not a fixed split. The paper's strategy switches: "When at least three arms remain, SMAS uses a sequential allocation rule that is" updated after each observation.[^c6] A static split can do no better than the sequential game: the static value is at least as large, and the appendix gives a three-arm example where it is strictly larger.[^c7] So Neyman's split is not the answer for K ≥ 3.
- The rule is optimal in the limit as the budget grows. At finite budgets the split is a heuristic whose performance was not measured in the text I read.
- The allocation uses estimated variances. The estimation is analysed only in the asymptotic sense the paper proves; a finite-sample penalty for a noisy pilot is not quantified here, and I did not check the pilot's exact size.
- The Bernoulli section makes a related point that should not be read as a general claim. "the same leading Bayes constant without estimating the variances" can be attained by uniform arm selection among the retained arms.[^c8] The paper states this for the Bayes criterion. It does not say the same holds for the minimax constant, so it is not a reason to drop the Neyman split when the worst case is the target.

## Related

- [[minimax-simple-regret-constant]] — the constant this two-arm allocation attains, and the near-tie mechanism behind it
- [[pac-best-arm-sample-complexity-lower-bound]] — the fixed-confidence setting, where allocation is judged by sample complexity rather than by the constant at a fixed budget

[^c1]: doi-10-48550-arxiv-2506-24007 — "The sampling proportions are proportional to the estimated standard deviations."
[^c2]: doi-10-48550-arxiv-2506-24007 — "whereas under Neyman allocation the corresponding"
[^c3]: doi-10-48550-arxiv-2506-24007 — "attained asymptotically by the deterministic Neyman allocation"
[^c4]: doi-10-48550-arxiv-2506-24007 — "together with the empirical-best recommendation, and no sampling rule that adapts"
[^c5]: doi-10-48550-arxiv-2506-24007 — "It estimates the variances needed for allocation from the pilot observations."
[^c6]: doi-10-48550-arxiv-2506-24007 — "When at least three arms remain, SMAS uses a sequential allocation rule that is"
[^c7]: doi-10-48550-arxiv-2506-24007 — "Appendix A gives a three-arm example in which the inequality is strict"
[^c8]: doi-10-48550-arxiv-2506-24007 — "the same leading Bayes constant without estimating the variances"
