---
description: "A majority vote can stop sampling once the leader's lead over the runner-up crosses a threshold fixed by error budgets and an assumed per-vote accuracy, so easy items take fewer draws."
aliases: ["Bayesian sequential probability ratio test", "BSPRT", "early-stopped majority vote", "vote-gap stopping rule", "adaptive rollout allocation"]
sources: ["arxiv-2512-02882"]
---
# Vote-gap sequential stopping

A fixed-budget majority vote draws the same number of samples for every question. A sequential vote draws one sample at a time and halts when the evidence for the leading answer is enough. In test-time policy optimisation the vote is a pseudo-label, because no ground truth exists at test time: the paper's position is that "we can estimate a selfconsistent pseudo-label from multiple rollouts to guide adaptation."[^c1]

The setup is concrete. Each completion is mapped to one of m answer classes. If the correct class is j, each vote lands on j with probability p0 and otherwise on one of the other m−1 classes. "This categorical noise model captures the intuition" that correct answers appear more often, and it gives a one-dimensional statistic for the test: the vote-count gap between the leader L and the runner-up S.[^c2] With uniform priors the Bayes factor between those two hypotheses is κ raised to the gap, where κ = p0(m−1)/(1−p0). Each extra vote of lead multiplies the odds of the leader over the runner-up by the same κ. (The formula is the paper's; the reading of κ as a per-vote odds multiplier is mine.)

Because the Bayes factor depends only on the gap, the sequential test reduces to thresholds on an integer. The paper defines Wald thresholds from user-chosen error budgets α and β,[^c3] and then "threshold on the integer gap" decides the stop.[^c4] Sampling halts when the gap reaches the bound for the leader, or the bound for the runner-up, or a hard cap M is hit. The paper keeps κ above one by requiring p0 to exceed 1/m. The text extraction drops the fraction, so the exact condition is my reading of "in practice we ensure p0 > m."[^c5]

The adaptivity follows from the gap. An easy item widens its lead in a few draws; a hard item keeps sampling until the cap. The paper's motivation is that "easy instances establish consensus quickly" while fixed budgets spend the same draws on everything.[^c6] The draws are not thrown away after the vote. Sampling runs until the later of the minimum retained count and the stopping time, "guaranteeing at least N retained rollouts for" the policy update.[^c7] So one set of rollouts serves as both the vote and the on-policy batch.

The reported effect is on cost, not on a theorem. On GPQA with Qwen2.5-Math-1.5B, the paper reports that OptPO with PPO beats TTRL with PPO on its accuracy metrics while token use falls from 262M to 144M, "a 45% compute saving."[^c8]

## What survives the transfer, and what needs a number

The gap rule needs p0, and test time supplies no labels to measure it. The paper estimates p0 from the vote share among the minimum retained rollouts and then multiplies by a factor of 0.6, because the majority share "is higher than real accuracy."[^c9][^c10] The authors say this "stabilizes BSPRT thresholds without labeled data."[^c11] The threshold therefore rests on a plug-in estimate and a hand-set constant. The stopping structure, stop on accumulated evidence and let the count be an output, survives. The numbers do not survive without that estimate.

## Limits

- The guarantee assumes votes are conditionally independent given the true class, and that p0 is the same for every draw on the same prompt. The paper states both assumptions; the sections read do not test them. Correlated rollouts are where the independence assumption is most likely to fail.
- The Wald boundaries are approximations. The [[sprt]] note records that approximate boundaries guarantee neither the stated error rates nor optimality. The paper's section heading "Rollout Allocation with Probabilistic Optimality" inherits that gap, and the text read does not close it.
- The implementation adds a rule the sequential test does not contain: "We require exceeding this confidence level 5 times across the rollouts."[^c12] The stop is therefore a repeated-crossing rule, not a single boundary hit. The paper gives this as a rigour choice; its effect on the error rate is not measured in the sections read.
- The vote needs a finite answer set. "Each completion y is mapped to a" canonical answer class,[^c13] which fits math and multiple-choice science. Free-text answers would need grouping first, and the paper does not address that.
- The per-prompt stop is not a claim about a stream of prompts. My inference: nothing here bounds the error across many items, which is the question [[anytime-valid-majority-stopping]] answers with a different tool.
- The evidence is on math and science benchmarks with verifiable answers, and the cost measure is tokens. Wall-clock time and other models were not in the sections read.

## Related

- [[sprt]] — the general two-hypothesis test this is an instance of; here the observations are votes and the threshold is on their gap.
- [[anytime-valid-majority-stopping]] — the e-process route to a sequential majority stop with a per-prompt error bound, which the Wald thresholds here do not carry.
- [[majority-vote-mode-certificate]] — the fixed-n bound on a majority vote, where the sample size is set before sampling.
- [[likelihood-ratio]] — the quantity whose gap-dependence makes the reduction to thresholds possible.

[^c1]: arxiv-2512-02882 — "we can estimate a selfconsistent pseudo-label from multiple rollouts to guide adaptation"
[^c2]: arxiv-2512-02882 — "This categorical noise model captures the intuition"
[^c3]: arxiv-2512-02882 — "we define Wald thresholds as"
[^c4]: arxiv-2512-02882 — "threshold on the integer gap"
[^c5]: arxiv-2512-02882 — "in practice we ensure p0 > m"
[^c6]: arxiv-2512-02882 — "easy instances establish consensus quickly"
[^c7]: arxiv-2512-02882 — "guaranteeing at least N retained rollouts for"
[^c8]: arxiv-2512-02882 — "a 45% compute saving"
[^c9]: arxiv-2512-02882 — "a degradation factor 0.6 to obtain a more realistic estimate of p0"
[^c10]: arxiv-2512-02882 — "probability is higher than real accuracy"
[^c11]: arxiv-2512-02882 — "stabilizes BSPRT thresholds without labeled data"
[^c12]: arxiv-2512-02882 — "We require exceeding this confidence level 5 times across the rollouts"
[^c13]: arxiv-2512-02882 — "Each completion y is mapped to a"
