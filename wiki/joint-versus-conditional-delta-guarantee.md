---
description: "Offline data can lower a best-arm sample bound only if the delta-guarantee is taken under the joint law of offline and online samples; conditioned on the offline path it does not help."
aliases: ["joint versus conditional correctness", "path-wise delta-correctness", "conditional delta-guarantee on offline data"]
sources: ["doi-10-48550-arxiv-2306-09048"]
---
# Joint versus conditional delta-guarantee

A fixed-confidence guarantee says the output is wrong with probability at most δ. When offline data are present, there are two ways to say over what that probability is taken. The first is the joint law: the offline samples are random, and the error event is measured over offline and online samples together. The second is the conditional law: the offline data are held fixed, and the guarantee must hold on every offline path, or on a set of offline outcomes of probability one. The paper's claim is that the two give different sample bounds. Under the joint law, offline samples can cut the online need, as in [[offline-augmented-characteristic-time]]. Under the conditional law they cannot.

The reason lies in how the question is structured. The paper's intuition is that "the best arm identification problems are composite hypothesis testing problems."[^d1] An algorithm with a probabilistic guarantee must gather enough data to rule out the alternative hypotheses. Once the offline data are fixed, every probability measure consistent with them agrees on that data, so "this data is not useful in separating them."[^d2] The fixed offline record carries no evidence about which alternative holds, and the conditional guarantee must then be met by online sampling alone. The paper draws the consequence: "such guarantees require us to ignore offline data", and "our lower bound on online samples is identical to that in the pure online setting."[^d3]

The paper therefore adopts the joint setting. Offline and online data are "generated from a common probability measure", and the δ-correctness is sought "under such joint probability measures."[^d4] This choice is what makes the offline data useful at all. The conditional case is discussed as a contrast, and the bound this note concerns is the joint one.

## Limits

The conditional-case argument is a high-level rationale in the introduction; the supporting analysis is in an appendix (B.2) that was not read for this note, so the step from "composite hypotheses" to "the bound is unchanged" is the paper's and is not checked here. The paper itself says the rationale is "intuitive" and "at a high level".

The joint guarantee is a choice, and it has a cost the paper names. Its guarantee averages over offline paths, so a realized offline record can be misleading while the average error stays below δ. The paper notes that "even along the rare paths where the samples can be highly misleading" a conditional guarantee would be required, and it does not quantify how wrong the joint guarantee can be on those paths.[^d5] Whether a practitioner should treat offline data as random draws (joint) or as a fixed record (conditional) is a modeling question the paper does not settle for applied use. Nothing here extends the contrast beyond stochastic best-arm identification with a known exponential family.

My own inference, not the paper's: the same question about joint versus fixed data arises in other settings that combine a logged dataset with new interaction, so this distinction is probably a general one to check when a reported gain from prior data is claimed. The text does not show that.

## Related

- [[offline-augmented-characteristic-time]] — the joint-guarantee bound that offline data lower; this note states the condition under which that bound holds
- [[pac-best-arm-sample-complexity-lower-bound]] — the purely online bound, which the conditional case reduces to
- [[coverage-separation-offline-online]] — another setting where offline and online data are weighed against each other

[^d1]: doi-10-48550-arxiv-2306-09048 — "the best arm identification problems are composite hypothesis testing problems"
[^d2]: doi-10-48550-arxiv-2306-09048 — "this data is not useful in separating them"
[^d3]: doi-10-48550-arxiv-2306-09048 — "our lower bound on online samples is identical to that in the pure online setting"
[^d4]: doi-10-48550-arxiv-2306-09048 — "under such joint probability measures"
[^d5]: doi-10-48550-arxiv-2306-09048 — "samples can be highly misleading"
