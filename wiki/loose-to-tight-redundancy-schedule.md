---
description: "A context picker trained first with a loose redundancy margin for recall, then a tight one for compactness, avoided the cold start that a compactness-only reward fell into."
aliases: ["coarse-to-fine redundancy margin", "recall-then-precision curriculum", "two-stage recall-precision schedule", "loose-to-tight margin"]
sources: ["arxiv-2512-14465"]
---
# Loose-to-tight redundancy schedule

A reward for choosing a subset of passages can score how much of the needed evidence is covered and penalise picks beyond the needed size plus a margin. The paper's point concerns how that margin is set over training. The same policy is trained in two consecutive phases. In the first, the allowed size is the gold set plus a relaxed margin, so over-selection is tolerated. The authors justify this by saying that for multi-hop questions "missing even a single hop in the evidence chain can cause a failure, whereas including a few extra passages is often harmless at this stage."[^s1] In the second, the margin is tightened, and the stated aim is that "Stage II targets input conciseness while preserving sufficiency."[^s2] The two phases run in sequence: "The training is sequential: we first" train with the first reward, then continue from that checkpoint with the second.[^s3]

The mechanism the authors give is a cold-start argument. A reward that penalises every extra passage gives little to learn from when the policy has no good sets yet. In their words, "exploring larger subsets incurs immediate length penalties, while small random subsets rarely contain the complete evidence chain required for reasoning."[^s4] The first phase supplies the high-recall starting point. Removing it is the largest single ablation the paper reports. A variant trained only with the second-stage objective reaches a judge accuracy "14.1 points below the full two-stage Context-Picker" on LoCoMo, and the authors say the policy then "gets trapped in a local optimum of selecting overly sparse contexts to minimize penalties".[^s5]

The second phase's own gain is smaller and depends on the dataset. The paper reports that Stage II "further improves accuracy on four out of five benchmarks while also shortening the selected contexts."[^s6] On the one benchmark where it loses, the recall-only stage was tied with the strongest baseline, "tied with RankRAG, indicating that the coarse stage effectively maximizes evidence coverage",[^s10] and the authors say the tighter margin "can occasionally prune borderline but helpful cues."[^s7]

The transferable concept is that a size penalty may need a recall-first phase so that there is something to shrink. A selection objective that starts tight may never reach a useful region. Whether this holds outside reinforcement learning, for instance when a model is prompted to pick evidence and then asked to compress it, is not tested in the text. That extension is my inference.

## Limits

- The schedule is measured in one ablation, on one dataset, LoCoMo. The paper's larger comparisons use the full two-stage method and do not isolate the schedule on the other four datasets.
- The two stages differ in more than the margin. The second stage also strengthens the redundancy penalty in the reward.[^s8] The "w/o Stage 1" variant therefore conflates a different starting point with a different objective, and the text does not separate them.
- The authors state that the picker "is robust to the exact split between T1" and T2 "as long as Stage I is given enough updates".[^s9] That is their observation from training, not a sweep reported in the part read.
- The cold-start explanation is the authors' reading of the training dynamics. The paper shows the training curves but does not isolate the sparsity mechanism with a measurement of its own.
- The schedule presupposes a trained policy. It does not say what a single prompted call should do, and no non-trained variant is reported.

## Related

- [[leave-one-out-minimal-evidence-set]] — the mined sets that the margin is measured against; the schedule depends on the targets that the leave-one-out search produces.
- [[minimal-sufficient-level-reward]] — a reward that subtracts when the chosen tier exceeds the minimal one; the same penalty shape, without a recall-first phase.
- [[generate-then-verify-candidate-pipeline]] — another recall-then-precision split, but as two stages of a pipeline rather than of training; its reported F1 gain is modest.

[^s1]: arxiv-2512-14465 — "whereas including a few extra passages is often harmless at this stage"
[^s2]: arxiv-2512-14465 — "Stage II targets input conciseness while preserving sufficiency"
[^s3]: arxiv-2512-14465 — "The training is sequential: we first"
[^s4]: arxiv-2512-14465 — "exploring larger subsets incurs immediate length penalties"
[^s5]: arxiv-2512-14465 — "14.1 points below the full two-stage Context-Picker"
[^s6]: arxiv-2512-14465 — "further improves accuracy on four out of five benchmarks while also shortening"
[^s7]: arxiv-2512-14465 — "it can occasionally prune borderline but helpful"
[^s8]: arxiv-2512-14465 — "the redundancy penalty in the reward (Eq. 6)"
[^s9]: arxiv-2512-14465 — "robust to the exact split between T1"
[^s10]: arxiv-2512-14465 — "tied with RankRAG, indicating that the coarse stage effectively maximizes evidence coverage"
