---
description: "Weighting each reward signal by a softmax over its estimated reliability lets noisy proxies count less; the reliability estimate can be built without labels."
aliases: ["adaptive reliability weighting", "reliability-weighted reward", "softmax reliability weights"]
sources: ["arxiv-2512-22545"]
---
# Reliability-weighted signal fusion

A reward built from several imperfect signals needs a rule for combining them. The simplest rule is an unweighted sum, which lets a noisy signal count as much as a reliable one. SR-MCR instead gives each signal a weight from a softmax over its reliability: the weight of signal k is exp(α·Relia_k) divided by the sum of exp(α·Relia_j) over all signals. The weights sum to one, and the temperature α sets how sharply reliability separates them.[^f1] The fused reward is then the weighted sum of the normalized signals.[^f2]

The formalism does not say what reliability is. The paper offers three instantiations: the Pearson correlation between a raw signal and task accuracy on a small labelled set, the inverse variance of the signal, or an exponential-moving-average stability measure.[^f3] Only the first needs labels, and the paper confines labels to that one stage: "This calibration stage is the only place that may" use them.[^f4] Without a labelled set, the paper falls back to "GT-free proxies—inverse variance, EMA stability," or to uniform weights.[^f5]

The reason given for weighting is variation across domains. A signal can be informative in one setting and noise in another. Lexical overlap is the paper's example: it is "more informative in QA than in math reasoning."[^f6] The reliability estimate is therefore not fixed. The training loop re-estimates it each iteration: its algorithm has a step, "Reliability update: update Reliak (e.g., EMA or variance)," before the weights are recomputed.[^f7]

Before fusion, each raw signal is winsorized and min–max normalized to [0, 1], so the weights act on signals already on one scale.[^f8] The five signals in SR-MCR are sentence-level semantic alignment, lexical overlap, non-redundancy, CLIP-based visual grounding, and NLI-based step coherence. Each is a proxy for a property the paper wants the reasoning to have, not a measure of correctness.

What survives the transfer: a softmax over any scalar per-signal score, where the score is whatever estimates reliability on the target domain. What does not survive automatically: the softmax weights are not probabilities that a signal is right. A reliable signal that is redundant with another is counted twice, and nothing in the formula notices (my inference). A weighted sum also lets a strong component cover a failing one; [[compensatory-leakage]] names that flaw of scalar combination, and reweighting does not remove it.

## Limits

- The text read contains no comparison of the adaptive weights against the uniform fallback, which the paper offers as an option: "or uniform weights λk = 1/5."[^f9] The reward ablations remove whole terms, and "Removing any reward term" consistently reduces performance; they do not remove the weighting itself.[^f11] The gain from reliability weighting is therefore not isolated.
- The label-free variants measure steadiness, not tracking. Inverse variance and EMA stability say how stable a signal is across samples. A signal can be steady and consistently wrong (my inference).
- The motivation is asserted. The introduction says single proxies "miscalibrate signals" across heterogeneous tasks.[^f10] The text offers one example and no measurement of how often this happens.
- The temperature α is named but its value is not reported in the sections read. The weights are re-estimated during training, so they move with the policy being trained (my reading of Algorithm 1).
- The method's own reliability proxies are computed from the same model outputs as the signals. No independent check of whether a high-reliability signal is actually right is described.

## Related

- [[cross-provider-judge-ensemble]] — pooling judges, where weighting by reliability is named as the open question
- [[rater-effects-latent-score-model]] — unreliable raters are down-weighted by a latent model rather than a softmax
- [[pessimistic-min-judge-aggregation]] — combining judges by the minimum, which avoids weighting by taking the worst verdict
- [[compensatory-leakage]] — the flaw of scalar combination that a weighted sum can hide

[^f1]: arxiv-2512-22545 — "where α > 0 is a temperature that controls sharpness"
[^f2]: arxiv-2512-22545 — "Reward computation: compute {sk } and fuse into"
[^f3]: arxiv-2512-22545 — "The reliability score Reliak can be instantiated as"
[^f4]: arxiv-2512-22545 — "This calibration stage is the only place that may"
[^f5]: arxiv-2512-22545 — "we use GT-free proxies—inverse variance, EMA stability,"
[^f6]: arxiv-2512-22545 — "lexical overlap is more informative in QA than in math reasoning"
[^f7]: arxiv-2512-22545 — "Reliability update: update Reliak (e.g., EMA or"
[^f8]: arxiv-2512-22545 — "each raw score sk is first winsorized (clipped at the"
[^f9]: arxiv-2512-22545 — "or uniform weights λk = 1/5."
[^f10]: arxiv-2512-22545 — "reward proxies (e.g., lexical overlap) miscalibrate signals"
[^f11]: arxiv-2512-22545 — "Removing any reward term"
