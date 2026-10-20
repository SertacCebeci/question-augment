---
description: "Grading a choice by its option index instead of an exact string match makes the reward checkable without name post-processing; the paper links this to better transfer on unseen classes."
aliases: ["index-match reward", "option-index reward", "MCQ verifiable reward"]
sources: ["arxiv-2511-18305"]
---
# Closed-choice verifiable reward

A reinforcement-learning reward is only as usable as the check behind it. For fine-grained image classification, the check used by prior work is string matching: the reward is 1 when the model's final category name equals the ground-truth name. The DiVE-k paper gives three reasons this check is brittle. It needs ad hoc post-processing, it fails on answers that use scientific or common names, and it encourages memorization of the training category names.[^c1][^c2][^c3]

The alternative puts the candidate names in the prompt and scores the chosen index. The paper's reward has two parts, a format reward and an MCQ reward that "rewards a value of 1.0 if model predicts the correct" option and 0.0 otherwise.[^c4] Once the options are fixed, the authors say the reward "becomes trivially verifiable" because the model "simply has to select the correct index from the given options."[^c5][^c6] A category spelled another way, or given as a scientific rather than a common name, no longer changes the score, since the check is over option slots rather than strings. That last point is my inference from the reward definition; the paper does not state it in those words.

On zero-shot base-to-novel classification with Qwen2.5-VL-7B, the paper reports "gains of +7.8 base, +4.6 novel, and +6.2 HM" over ViRFT, the string-match baseline.[^c7] The novel-class part is where the memorization argument would show, and there the gap is small. "ViRFT gain over QWEN2.5-VL-7B model on novel categories remains" marginal, from 77.0 to 77.1 under the paper's inference pipeline, which the authors read as "suggesting their reward primarily reinforces base categories."[^c8][^c9] When ViRFT is run with that same pipeline, the paper still reports "+4.0 base, +1.8 novel" improvements for its own method.[^c10]

## Limits

- The evaluation is not string-free. Accuracy is judged by an LLM that receives the ground-truth and predicted names and is asked whether they "belong" to the same category.[^c11] Training drops string matching; the reported numbers still depend on a name judge. I found no validation of that judge in the sections I read.
- The comparison is not isolated. DiVE-k trains on MCQs built from the base model's top-k outputs, while ViRFT trains on string matches. The paper's option-source ablations vary the options inside MCQ training, not the reward type. A string-match reward trained on the same option sets was not run, so how much of the gain comes from the reward itself is untested.
- The memorization claim is asserted. The paper cites Section 4.2.1 for it, but that section opens with "We present the results for zero-shot base-to-novel generalization in Table 1."[^c12] The novel-class gap above is the only evidence I found for it, and the reading of that gap is the authors' interpretation.
- The index reward depends on the right answer being among the options. Training forces the ground truth into the set,[^c13] and the second stage "can only succeed if the correct" answer was sampled in the first.[^c14] A string reward has no such dependence on a sampled candidate set, so the index reward inherits the recall of the first stage.
- Costs and scope: the two-step inference "incurs additional" computation from two forward passes,[^c15] and the authors expect that "base LVLMs with lower intrinsic accuracy may not realize comparable gains."[^c16] The method also regresses on Pet relative to ViRFT, which the authors attribute to more options.[^c17]

## Related

- [[distractor-strength-reward-signal]] — in multiple-choice RLVR the strength of the wrong options decides whether the reward trains reasoning or guessing; this note is the reward-form side of the same setup.
- [[option-matching-shortcut]] — closed options can let a model match candidates instead of deducing; the paper claims its differential step avoids this, and I found no test of it in the sections I read.
- [[answer-string-leakage]] — the question-side shortcut, where a question containing its own answer lets a model match rather than predict.

[^c1]: arxiv-2511-18305 — "requiring ad hoc string post-processing"
[^c2]: arxiv-2511-18305 — "may use scientific or common names that cannot be validated by string matching"
[^c3]: arxiv-2511-18305 — "memorization of the training category names (Section 4.2.1)"
[^c4]: arxiv-2511-18305 — "rewards a value of 1.0 if model predicts the correct"
[^c5]: arxiv-2511-18305 — "the reward for a correct prediction becomes trivially verifiable as"
[^c6]: arxiv-2511-18305 — "model simply has to select the correct index from the given options"
[^c7]: arxiv-2511-18305 — "gains of +7.8 base, +4.6 novel, and +6.2 HM"
[^c8]: arxiv-2511-18305 — "ViRFT gain over QWEN2.5-VL-7B model on novel categories remains"
[^c9]: arxiv-2511-18305 — "suggesting their reward primarily reinforces base categories"
[^c10]: arxiv-2511-18305 — "Even when baselines are run with our inference pipeline (ViRFT*), we retain a +4.0 base, +1.8 novel improvements"
[^c11]: arxiv-2511-18305 — "ask the LLM if they belong"
[^c12]: arxiv-2511-18305 — "We present the results for zero-shot base-to-novel generalization in Table 1"
[^c13]: arxiv-2511-18305 — "To ensure that the correct answer is always an option during"
[^c14]: arxiv-2511-18305 — "the second stage can only succeed if the correct"
[^c15]: arxiv-2511-18305 — "our two-step inference process incurs additional"
[^c16]: arxiv-2511-18305 — "base LVLMs with lower intrinsic accuracy may not realize comparable gains"
[^c17]: arxiv-2511-18305 — "We observe a small regression on Pet data compared to ViRFT"
