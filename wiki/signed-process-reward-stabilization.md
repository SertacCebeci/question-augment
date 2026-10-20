---
description: "A signed, heavy-tailed step reward is stabilised by zeroing small values, shrinking negatives so the policy does not learn to stop searching, and log-clipping extremes."
aliases: ["dead zone and asymmetric negative scaling", "stabilization of step-level information gain", "asymmetric negative scaling of process rewards"]
sources: ["doi-10-48550-arxiv-2604-15148"]
---
# Signed process reward stabilization

> A raw step score that can be positive or negative, and is noisy, is conditioned in three fixed steps before it reaches the policy gradient: small values are dropped, negative values are shrunk, and extreme values are compressed.

## Mechanism

Liang et al. (2026) argue that differences of raw LLM log-probabilities "inherently exhibit high variance and heavy-tailed distributions", and that if used directly, extreme values and estimation noise can destabilize training or induce degenerate behaviour.[^c1] They process the raw step score (see [[counterfactual-retrieval-information-gain]]) in three ordered steps.

The first is a dead zone. For questions the model answers from memory, the score is driven by memory rather than by the query; the authors write that "For questions the model can answer from parametric knowledge, IG does not faithfully reflect query quality".[^c2] Any score with absolute value below a threshold delta is set to zero. The default is delta = 0.5 nats per answer token: "We use δ = 0.5 by default."[^c3]

The second is asymmetric negative scaling. A negative score says the retrieval was less helpful than random documents, which suggests a poor query. The authors observed that "full-strength penalties for negative IG can cause the model to collapse to a degenerate strategy of never issuing search queries", which avoids all negative signals.[^c4] So negative values are multiplied by lambda < 1 (default 0.1), while positive values pass unchanged. The stated effect is that "the optimal strategy is to search and search well, rather than to avoid searching entirely."[^c5] The authors keep lambda above zero because with lambda = 0, poorly formed queries become gradient-wise indistinguishable from non-query tokens; they report that lambda = 0 underperforms lambda = 0.1 in their sensitivity analysis.[^c6]

The third is soft clipping. Values beyond a threshold eta (default 3.0) are compressed logarithmically, so ordering is preserved while magnitude is reduced: "Extreme IG values can dominate the reward signal and cause gradient instability."[^c7] The authors note that the surviving negative values "rarely exceed" about -3 nats, so after scaling they fall roughly between -0.3 and -0.05, well below the clipping threshold. Clipping therefore mainly bounds the positive side.[^c8]

The order is fixed: dead zone first, then negative scaling, then clipping. The authors report that each mechanism "addresses a substantial and distinct fraction of the search steps" in their training checkpoints.[^c9]

## What the bundle is for

The three mechanisms are not a general variance reduction. Each targets a failure the authors saw. The dead zone removes scores that reflect memory rather than the query. Negative scaling removes an incentive to stop searching. Clipping removes gradient spikes from large values. The asymmetry is the one that matters for design: a penalty on bad queries is the natural choice, and the authors' point is that it can be exploited by not querying at all.

## Limits

- The thresholds (delta 0.5, eta 3.0, lambda 0.1) are set once and used across all experiments "without dataset-specific tuning". Their robustness is analysed in RQ4, which was not read in this pass, so the choice of constants is not checked here.
- The "never search" collapse is reported as an observation in the authors' training runs. The slices read do not include the run in which the full-strength penalty was tried, so the size of the collapse is not known.
- The dead zone is a hard threshold on a noisy quantity. A query on a question the model half-knows can land just inside or outside delta, and the abrupt change in value at delta is not smoothed.
- Each mechanism is motivated by the score's own distribution, which is specific to one scoring rule, one model family and one training set. Whether the same thresholds suit another log-likelihood difference is untested; the transfer is my inference.
- The authors apply the bundle as an ordered pipeline. The effect of each piece on final accuracy (the component ablation) was not read; the claim that each is necessary rests on the authors' ablation section, which was not checked here.

## Related

- [[counterfactual-retrieval-information-gain]] — the raw score this bundle conditions
- [[query-token-advantage-modulation]] — how the conditioned score is written onto query tokens in the advantage
- [[sequence-likelihood-confidence]] — the answer log-probability whose differences are heavy-tailed in the same way
- [[information-gain-reward]] — a clarification reward that uses a log-likelihood shift and no comparable conditioning step in the sources read

[^c1]: doi-10-48550-arxiv-2604-15148 — "inherently exhibit high variance and heavy-tailed distributions"
[^c2]: doi-10-48550-arxiv-2604-15148 — "For questions the model can answer from parametric knowledge, IG does"
[^c3]: doi-10-48550-arxiv-2604-15148 — "We use δ = 0.5 by default."
[^c4]: doi-10-48550-arxiv-2604-15148 — "full-strength penalties for negative IG can cause the model to collapse to a degenerate strategy of"
[^c5]: doi-10-48550-arxiv-2604-15148 — "This asymmetry ensures that the optimal strategy is to search and search"
[^c6]: doi-10-48550-arxiv-2604-15148 — "analysis in Figure 4 confirms that λ=0 underperforms λ=0.1"
[^c7]: doi-10-48550-arxiv-2604-15148 — "Extreme IG values can dominate the reward signal and cause gradient instability"
[^c8]: doi-10-48550-arxiv-2604-15148 — "raw negative IG values surviving the dead zone rarely exceed"
[^c9]: doi-10-48550-arxiv-2604-15148 — "confirming that each mechanism addresses a substantial and distinct fraction of the search steps"
