---
description: "A rubric written for each question alongside its answer beats one fixed general rubric as an RL reward on average (+0.9 points), and most on instruction following (+9.22 on IFEval)."
aliases: ["instance-level rubric", "per-question rubric", "question-conditioned rubric"]
sources: ["doi-10-48550-arxiv-2605-23454", "doi-10-48550-arxiv-2601-15161"]
---
# Question-specific rubric

A rubric is a set of weighted criteria; a judge scores a response against each criterion, and the reward is the weighted sum of those scores.[^c1] A question-specific rubric is the same object written for one question at a time. The criteria are produced in the same generation pass that writes the question and its reference answer, so they follow the source knowledge and the intended answer rather than a list of dimensions reused across a whole task.[^c2] The rubric carries positive weights for desired properties and negative weights for common failure modes, so a response can be penalized for a named error, not only denied a bonus.[^c3]

The reason the granularity matters is the contrast with a binary verdict. A binary reward gives zero to any incomplete answer, whereas weighted criteria give partial credit in proportion to the importance of what is satisfied.[^c4] A question-specific rubric therefore does two things at once: it names the criteria that this question actually turns on, and it spreads the reward over them.

## What was measured

The ablation holds the training data and the GRPO setup fixed and varies only the reward.[^c5] Four rewards were compared: a blind judge that scores holistically with no rubric, a fixed general rubric of accuracy, completeness and clarity applied to every question, a judge that compares the response with the reference answer, and the question-specific rubric. Averaged over seven benchmarks, the question-specific rubric scored 52.69, the general rubric 51.79 and the blind judge 49.53.[^c6] The largest gain over the general rubric came on IFEval (+9.22).[^c7] The authors' explanation is that instruction-following constraints (formatting, length, keywords, language, structure) vary from one example to the next and are "difficult to express with a fixed set of generic criteria such as accuracy or clarity."[^c8]

The general rubric was not beaten everywhere. It did better on HealthBench and WritingBench,[^c9] and the authors state that "no reward strategy dominates every individual" benchmark.[^c10] The claim the measurement supports is therefore about robustness across heterogeneous tasks, not about a per-question rubric winning on each task.

A per-question rubric can also be grounded outside the generating model's memory. A retrieval-augmented pipeline writes instance rubrics from retrieved medical evidence and from constraints read off the query, and its rubrics cover more physician-written criteria than a one-step GPT-4o rubric.[^c16] That measures coverage of expert criteria, not the reward effect above, and it was run on one backbone and two medical benchmarks. The split into factual and interaction tracks is in [[dual-track-rubric-constraints]].

## Limits

- One base model. The authors state that "experiments are conducted exclusively on Qwen3-4BBase",[^c11] so whether the gap holds at larger scale is not shown.
- The average margin over the general rubric is 0.90 points. The appendix reports 95% confidence intervals for these ablations,[^c12] and this note did not check whether the gap clears them.
- The rubric is written and checked by models. The reward judge is Qwen3-32B,[^c13] and question and rubric quality control runs on Claude-Sonnet-4.5.[^c14] The validation step asks "whether the rubric covers the key requirements of the question."[^c15] In the sections read, no human audit of the rubrics is reported.
- The baseline is weak. The general rubric is three generic criteria. A fixed task-level rubric written by experts was not among the alternatives; whether per-question criteria beat a well-made fixed rubric is my inference and is not tested in the paper.
- The measurement concerns what the reward looks at. Whether per-question rubrics also change which questions a model is trained on, or how it answers them at inference, is not tested.

## Related

- [[single-reference-grading-confound]] — the reference-answer reward in the same ablation is strongest on HealthBench but unstable across task types, the single-reference problem again, now as an RL reward.
- [[pretraining-grounded-rubric-self-play]] — also writes a query-specific rubric from a pretraining document, but its measured gain comes from grounding the grader in that document, not from rubric granularity.
- [[rubric-difficulty-evolution]] — the other answer to a fixed rubric: extend the base rubric with mined criteria so it does not saturate.

[^c1]: doi-10-48550-arxiv-2605-23454 — "where ck denotes the k-th evaluation criterion and wk denotes its importance weight"
[^c2]: doi-10-48550-arxiv-2605-23454 — "co-generates question-specific weighted rubrics, enabling instance-level reward supervision for open-ended responses"
[^c3]: doi-10-48550-arxiv-2605-23454 — "The rubric contains weighted positive criteria for desired response properties and negative criteria for common failure modes"
[^c4]: doi-10-48550-arxiv-2605-23454 — "that would assign zero to any incomplete response"
[^c5]: doi-10-48550-arxiv-2605-23454 — "All variants use the same training dataset and GRPO setup"
[^c6]: doi-10-48550-arxiv-2605-23454 — "ARES-RL (52.69) and General Rubric (51.79), outperform the Blind Judge baseline (49.53) on"
[^c7]: doi-10-48550-arxiv-2605-23454 — "with the largest gain on IFEval (+9.22)"
[^c8]: doi-10-48550-arxiv-2605-23454 — "which are difficult to express with a fixed set of generic criteria such as accuracy or clarity"
[^c9]: doi-10-48550-arxiv-2605-23454 — "HealthBench and WritingBench, suggesting that generic quality dimensions can already be effective"
[^c10]: doi-10-48550-arxiv-2605-23454 — "no reward strategy dominates every individual"
[^c11]: doi-10-48550-arxiv-2605-23454 — "experiments are conducted exclusively on Qwen3-4BBase"
[^c12]: doi-10-48550-arxiv-2605-23454 — "Reward-design ablation results with 95% confidence intervals"
[^c13]: doi-10-48550-arxiv-2605-23454 — "the rubric judge (Qwen3-32B) is"
[^c14]: doi-10-48550-arxiv-2605-23454 — "question and rubric quality control use Claude-Sonnet-4.5"
[^c15]: doi-10-48550-arxiv-2605-23454 — "Rubric validation checks whether each criterion is well-formed, whether the rubric covers the key"
[^c16]: doi-10-48550-arxiv-2601-15161 — "scores of 50.20% and 31.90%, significantly outperforming the GPT-4o baseline"
