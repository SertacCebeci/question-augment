---
description: "A training reward scores each intermediate visual call against dense annotations (segment IoU, frame recall, box IoU) and averages the hits, so a right answer reached by wrong steps earns less."
aliases: ["step-level reasoning reward", "reasoning-aware reward", "RA-GRPO reasoning reward", "manipulation correctness reward"]
sources: ["arxiv-2511-23477"]
---
# Annotated step-grounding reward

A model that acts in several steps, each returning an observation, can be trained on its final answer alone or on each step as well. Video-CoM adds a per-step term to its reinforcement learning. The reasoning reward is "computed as the mean correctness over all predicted manipulations": every visual call the policy emits is checked against annotation, and the reward is the share of calls that pass.[^a1] A find-segment call is checked against the annotated valid segments, a find-frame call against annotated frame indices, and a spatial-zoom call by intersection-over-union against an annotated box, with a threshold of 0.3, measured "between predicted and ground-truth regions".[^a2]

The introduction names the three checks as "temporal IoU for find-segment, frame recall for find-frame, and spatial IoU for spatial-zoom".[^a3] The equation for the same term, as printed, tests segment and frame calls by membership in the annotated sets, not by overlap. The text I read does not reconcile the two (see Limits).

The term is added to the answer reward during training. The setup table lists the rewards as "Accuracy + Reasoning".[^a4] Because the step term is a mean over calls, it "credits partial progress even when the final answer is incorrect".[^a5] The paper's design point is that a trajectory can earn reward for its correct manipulations while its final answer is wrong.[^a6]

The argument for the term is that several manipulation sequences can reach the same correct answer, so an answer reward "cannot distinguish between grounded and spurious reasoning paths".[^a7] The same failure is handled for retrieval-augmented reasoning in [[evidence-grounded-step-reward]], where the step verdict is learned from a model. Here the check is a lookup against annotation, which needs no model judge but needs labels.

The annotation is what makes the term computable. For temporal reasoning the authors "annotate all valid segments and frames for each find-segment and find-frame operation", and they state that "These dense annotations ensure consistent grounding of visual evidence across time".[^a8][^a9]

## What was measured

The ablation caption for the reward says that "step-level reasoning rewards leads to consistent improvements" over the same training without them.[^a10] My reading of the table: the average column moves from 38.9 under GRPO to 40.5 under RA-GRPO, and the first benchmark from 66.7 to 68.7. On the paper's own Video-CoM-Bench the text says that "RA-GRPO improves both reasoning accuracy and joint Acc@IoU".[^a11] My reading of that table: joint Acc@IoU is 37.6 for GRPO, 38.1 for the SFT model and 39.2 for RA-GRPO. So the step term is the difference that takes the joint score past the SFT model; GRPO alone does not.

## Limits

- Dense annotation is a precondition. The reward exists only where every valid segment, frame and box is labelled for each operation. The paper builds these labels for its own dataset. The text does not say what they cost or whether the term transfers to video with sparse labels.
- The measure counts correct calls, not necessary ones. My inference: a trajectory whose calls are all correct but do not feed the answer scores as well as one that uses them. The text does not test whether the reward changes which calls the policy chooses, as opposed to whether the calls it makes are right.
- The text is not consistent on the segment check. The introduction says temporal IoU; the printed equation tests membership in the annotated set. The tolerance that makes a segment correct is not given in the slices I read. My reading: the segment term is a hit rate, and "IoU" is loose wording for it.
- The threshold of 0.3 is a fixed choice. Its sensitivity is not reported in what I read.
- The gain is small. My reading of the table is about 1.6 points on the average column, for one backbone: the SFT row of the setup table lists "Qwen2.5-VL-7B-Instruct".[^a12] I did not find variance across seeds in the slices I read, so a gap of this size is not shown to be above run-to-run noise.
- The reward is not compared with a label-only process reward. Those need no boxes or segments, so their cost is lower; the paper does not test whether they do as well.

## Related

- [[evidence-grounded-step-reward]] — the same spurious-success failure, handled for retrieval by a learned step verdict instead of an annotation lookup.
- [[crop-label-consistency-reward]] — a per-crop process reward that needs no boxes; it scores agreement with the model's own label, not location against annotation.
- [[coarse-to-fine-evidence-zoom]] — the answer-scored zoom reward; the annotated term instead checks the zoomed region against a ground-truth box.
- [[post-hoc-visual-augmentation]] — the same call-and-feed-back loop on images, with non-semantic transforms where this paper's calls are query-conditioned.
- [[visual-evidence-scoring]] — grades the crops a reasoner cites against ground-truth boxes at evaluation time; this note is the training-time term.

[^a1]: arxiv-2511-23477 — "computed as the mean correctness over all predicted manipulations"
[^a2]: arxiv-2511-23477 — "between predicted and ground-truth regions"
[^a3]: arxiv-2511-23477 — "temporal IoU for find-segment, frame recall for find-frame, and"
[^a4]: arxiv-2511-23477 — "Accuracy + Reasoning"
[^a5]: arxiv-2511-23477 — "credits partial progress even when the final answer is incorrect"
[^a6]: arxiv-2511-23477 — "rewarding reasoning trajectories that perform correct manipulations even when the final answer is wrong"
[^a7]: arxiv-2511-23477 — "cannot distinguish between grounded and spurious reasoning paths"
[^a8]: arxiv-2511-23477 — "we annotate all valid segments and frames for each find-segment and find-frame operation"
[^a9]: arxiv-2511-23477 — "These dense annotations ensure consistent grounding of visual evidence across time"
[^a10]: arxiv-2511-23477 — "step-level reasoning rewards leads to consistent improvements"
[^a11]: arxiv-2511-23477 — "RA-GRPO improves both reasoning accuracy and joint Acc@IoU"
[^a12]: arxiv-2511-23477 — "Qwen2.5-VL-7B-Instruct"
