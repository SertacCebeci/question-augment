---
description: "Thinking-judge votes for A, tie or B are aggregated by a Bradley-Terry-Davidson model with a separate tie term, fit on labelled items, so narrow margins and strong consensus stay distinct."
aliases: ["Bradley-Terry-Davidson aggregation", "distribution-calibrated aggregation", "BTD aggregation", "calibrated three-way vote model", "tie-propensity calibration"]
sources: ["arxiv-2512-03019"]
---
# Tie-aware vote calibration

A thinking judge that compares two candidates is run n times, and each run returns one vote: first wins, second wins, or tie. Majority vote takes the mode of those three counts. The mode discards how strong the evidence is: "a simple majority vote cannot distinguish between a narrow 5-to-4 decision and a decisive 9-to-0 consensus".[^c1] Tie-aware calibration keeps the full count triple (c+, c0, c−) and passes it to a probability model over the three outcomes, then picks the label that a loss would prefer.

The model is a multinomial logit, a Bradley-Terry-style model for ternary outcomes that adds Davidson's tie term.[^c2] Each item gets a latent margin u, computed from a smoothed log-ratio of the non-tie counts, and a tie logit η, computed from a smoothed log share of tie votes. The three probabilities are a softmax over e^u, e^−u and e^η. The construction keeps two quantities apart: polarity (the margin among non-tie votes) and decisiveness (the non-tie rate). The abstract says the pair is what lets the method "distinguish narrow margins from strong consensus".[^c3] A judge can have the same margin among its non-tie votes and very different tie rates; the model reads them as different evidence.

The parameters are a margin slope, a global tie baseline and a tie slope. The tie baseline is a single fitted number for the judge and prompt, and the tie slope modulates it per item, so the tie propensity is learned from labels rather than assumed.[^c4] The fit is done on a labelled calibration set, not on the decision directly. The reason given is that the decision-level loss is flat almost everywhere, since a prediction changes only when a decision boundary is crossed, so gradient methods get no signal.[^c5] The fit therefore minimizes a probabilistic score, and the decision is taken afterwards.

The decision is the label with least expected absolute error on the ordinal scale −1, 0, +1. The authors use that loss because it "scales penalties by severity": a full reversal costs twice a tie disagreement.[^c6] My reading of their decision rule is that it is not the same as taking the mode: when the tie probability is large, the least-loss label can be the tie even when one side has more votes. That reading is mine, not a result the paper states.

On WMT23 and RewardBench 2 tasks, with gemini-2.5-flash as judge, the authors report that their method "attains the best scores on all the datasets and" sample counts they tried.[^c7] Self-consistency, by contrast, on the RewardBench 2 tasks does not improve with more samples: as n grows from 4 to 12, the method improves while SC degrades or stays flat.[^c8] Against a human-majority gold label on WMT ZH→EN, the abstract reports that the method matches or exceeds individual human raters.[^c9]

The motivation is the instability of the tie rate itself. Across three prompts for the same judge, the authors found tie rates that differed significantly, and they say "This instability is a critical flaw for methods that do not calibrate for such variations".[^c10]

What survives the transfer to other settings is the structure: a judge's votes are three-way, the tie rate is a judge-specific parameter, and the decision should follow the loss the task uses. What does not survive by default is the fitted values. They belong to one judge, one prompt and one task.

## Limits

- The calibration needs labelled items. The default split is about 5% of the data, and in the authors' calibration curves a set of 20 items already "is sufficient to outperform Self Consistency by a large margin".[^c11] A setting without any labels cannot use this method as written.
- The gold labels are a consensus, not an independent truth. For WMT the six ratings per segment are majority-voted, and that consensus "serves as the gold standard".[^c12]
- Transfer across tasks is weak. The authors write that transfer between tasks "is usually weak", and some calibrations "induce sharper landscapes whose fitted parameters do" not carry over.[^c13]
- The main tables use one judge: "Tables 3 and 4 report MAE and pairwise accuracy for all aggregation methods using gemini-2.5-flash".[^c14] The authors are employed by the company that builds that judge, and say so.[^c15] Whether the gain holds for other judges is a question the main tables do not settle, and I did not check the appendix tables for other models.
- The model is for three outcomes. Extending it to a k-point scale is named as future work: "we aim to generalize this framework to broader ordinal and multi-class" outcomes.[^c16]
- My inference: the method treats the n samples as draws from one vote distribution per item. If the samples share a prompt-level bias, extra samples add little, and the calibrated tie rate would describe that bias rather than the evidence. I did not find a test of correlated samples in the sections I read.

## Related

- [[majority-vote-mode-certificate]] — the same vote counts under majority rule; its bounds assume a unique mode, and ties are where that guarantee weakens.
- [[bradley-terry-preference-model]] — the two-outcome preference family; the Davidson term added here is what models a tie.
- [[calibration]] — fitting a map from a judge's raw behaviour to labelled outcomes is the calibration step, here on vote counts.
- [[pessimistic-min-judge-aggregation]] — another way to combine parallel judges, by a minimum over scores rather than a count model over votes.
- [[answer-format-dependent-bias-measurement]] — allowing a tie option is itself a format change, and it moves measured positional bias.

[^c1]: arxiv-2512-03019 — "a simple majority vote cannot distinguish between a narrow 5-to-4 decision and a decisive 9-to-0 consensus"
[^c2]: arxiv-2512-03019 — "We adopt a multinomial logit model inspired by the Bradley"
[^c3]: arxiv-2512-03019 — "decisiveness (non-tie rate) to distinguish narrow margins from strong consensus"
[^c4]: arxiv-2512-03019 — "allows a global tie baseline via"
[^c5]: arxiv-2512-03019 — "change only when a decision boundary is crossed"
[^c6]: arxiv-2512-03019 — "MAE scales penalties by severity"
[^c7]: arxiv-2512-03019 — "Our method attains the best scores on all the datasets and"
[^c8]: arxiv-2512-03019 — "12 consistently improves our method, whereas SC tends to"
[^c9]: arxiv-2512-03019 — "or exceeds individual human raters"
[^c10]: arxiv-2512-03019 — "This instability is a critical flaw for methods that do not calibrate for such variations"
[^c11]: arxiv-2512-03019 — "of size 20 is sufficient to outperform Self Consistency by a large margin"
[^c12]: arxiv-2512-03019 — "serves as the gold standard"
[^c13]: arxiv-2512-03019 — "induce sharper landscapes whose fitted parameters do"
[^c14]: arxiv-2512-03019 — "Tables 3 and 4 report MAE and pairwise accuracy for all aggregation methods using gemini-2.5-flash"
[^c15]: arxiv-2512-03019 — "All authors are employed by Google-affiliated organizations"
[^c16]: arxiv-2512-03019 — "we aim to generalize this framework to broader ordinal and multi-class"
