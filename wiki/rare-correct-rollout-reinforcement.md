---
description: "In outcome RL on factual questions, a question with no correct sample out of 128 still trains the model: rare correct rollouts occur during training and get reinforced."
aliases: ["rare-success reinforcement", "inaccessible-example training signal", "suppressed-knowledge reinforcement"]
sources: ["doi-10-48550-arxiv-2605-07153"]
---
# Rare correct rollout reinforcement

In outcome-only RL with a binary reward, a training question that the base model answers correctly in none of its samples looks like the least useful kind. Its rollout group carries no positive reward, so on the naive reading there is nothing to reinforce. The paper's data-attribution study finds the opposite for factual recall. Training questions were split by the count c of correct answers in 128 pre-RL samples, and the zero region is "inaccessible@128 (c = 0)".[^b1] That region is "only ∼18% of the full training data," yet "it alone recovers ∼83% of the full-data RL gain."[^b2] The partially accessible subset recovers 70% and the highly accessible subset 31%.[^b3] Training on the two low-count subsets together "yields the highest overall gain, recovering the full-data" RL gain on average.[^b4]

The mechanism the paper gives is that a zero count in 128 samples does not mean the answer never comes up during training. "Tracking the training dynamics reveals why: some of these facts retain a nonzero probability of emerging during repeated rollouts."[^b5] For the representative case shown, Qwen, "The average reward starts extremely low"[^b6] and "it rises steadily throughout training."[^b7] The authors read the rise this way: once a rare correct response appears, "their signals are progressively reinforced,"[^b8] because "they are occasionally generated during repeated RL rollouts."[^b9]

The accessibility count is the frequency with which a correct trajectory can be sampled. In a group-relative setting such as GRPO, a group in which every rollout is wrong gives no contrast, so a zero-count question produces a gradient only in the rare groups where a success occurs. The paper's point is that these rare groups are where much of the factual gain comes from. (My inference on the group arithmetic; the paper uses the group-relative setting but states the consequence in its own words.)

The other end of the difficulty range fails for a different reason. Highly accessible facts "yields limited group-relative advantages,"[^b10] because the model is already right and there is little to contrast. Near-zero initial accuracy, in the paper's SimpleQA case, "leaves the model struggling with extremely sparse rewards."[^b11] The paper's summary is that "factual RL requires datasets with non-trivial initial accuracy."[^b12] So zero-count questions help only inside a dataset where the model is already right on some questions. The paper goes on to say that "data curation for factual RL should prioritize" these low-count examples over those of intermediate difficulty.[^b13] That is the authors' recommendation for one setting. This note keeps the mechanism and does not turn the recommendation into a rule for choosing questions.

## Limits

- One setting. The data are closed-book, one-hop, non-chain-of-thought factual QA, trained with GRPO and an LLM-judged binary reward. Other RL objectives, reasoning tasks and open-ended answers are not tested here.
- The attribution compares separately trained subsets, not removals from the full set. The paper keeps hyperparameters fixed and "balance[s] data sizes within each comparison group," so the recovery figures compare subsets at matched size, and a subset's share of the gain is not a marginal contribution. (My inference from the design.)
- The zero region is defined by 128 samples. A question with a small true probability can land there by chance, and the paper drops the 1-to-2 bin because it is hard to separate "from random sampling noise."[^b14] So the zero region mixes answers that are unreachable with answers that are rarely reachable. The rare-success account fits the second group; the data here do not separate the two.
- The reward curve is shown for one model. The paper gives "a representative case with full results in Appendix K,"[^b15] and that appendix was not read for this note.
- "Rare success" is the paper's account of the average-reward curve. The text read shows that average reward rises. It does not trace which individual questions produce the rare correct rollouts. (My inference.)

## Related

- [[sampled-answer-accessibility]] — the count that splits the training data into these regions.
- [[edge-of-competence-selection]] — a selection rule that treats zero coverage as having no correct trajectory to reinforce; this factual result cuts against that reading, and that note carries the caveat.
- [[zero-variance-group-waste]] — the group-level side of the same mechanism, where a group with no contrast gives no signal (my inference from the group-relative setting).

[^b1]: doi-10-48550-arxiv-2605-07153 — "inaccessible@128 (c = 0)"
[^b2]: doi-10-48550-arxiv-2605-07153 — "accounts for only ∼18% of the full training data, it alone recovers ∼83% of the full-data RL gain"
[^b3]: doi-10-48550-arxiv-2605-07153 — "accessible (70%) and highly accessible (31%) subsets."
[^b4]: doi-10-48550-arxiv-2605-07153 — "yields the highest overall gain, recovering the full-data"
[^b5]: doi-10-48550-arxiv-2605-07153 — "some of these facts retain a nonzero probability of emerging during"
[^b6]: doi-10-48550-arxiv-2605-07153 — "The average reward starts extremely low"
[^b7]: doi-10-48550-arxiv-2605-07153 — "it rises steadily throughout training"
[^b8]: doi-10-48550-arxiv-2605-07153 — "their signals are progressively reinforced."
[^b9]: doi-10-48550-arxiv-2605-07153 — "they are occasionally generated during repeated RL rollouts."
[^b10]: doi-10-48550-arxiv-2605-07153 — "highly accessible facts yields limited group-relative advantages"
[^b11]: doi-10-48550-arxiv-2605-07153 — "leaves the model struggling with extremely sparse rewards"
[^b12]: doi-10-48550-arxiv-2605-07153 — "factual RL requires datasets with non-trivial initial accuracy."
[^b13]: doi-10-48550-arxiv-2605-07153 — "data curation for factual RL should prioritize"
[^b14]: doi-10-48550-arxiv-2605-07153 — "to distinguish from random sampling noise"
[^b15]: doi-10-48550-arxiv-2605-07153 — "a representative case with full results in Appendix K."
