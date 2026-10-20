---
description: "A pair of runs on one input, wrong at an early checkpoint and right at a later one with a different tool sequence, is taken as evidence of revising a decision after new evidence."
aliases: ["self-reflection sampling", "SRS", "self-reflective case mining", "checkpoint-flip mining"]
sources: ["arxiv-2512-14157"]
---
# Checkpoint-flip revision sampling

A model that answers the same input wrongly at one point of its training and rightly at a later one carries, in that difference, a record of revision. The record counts only if the two answers were reached with different evidence-gathering. Ophiuchus, a medical model described as "a versatile, tool-augmented framework" that calls zoom and segmentation tools mid-reasoning, builds part of its training data from such records.[^c11] The condition is written over two trajectories for the same image and question at different checkpoints: their "tool-invocation sequences differ and the answer correctness flips".[^c1]

The pipeline is mechanical. After each SFT epoch the authors record the model's outputs and answers and look for such pairs, "then examine them to identify such cases".[^c2] Each matched pair is reconciled into one ground-truth reasoning trajectory, and the model is fine-tuned on the resulting subset with an objective like the one used for the cold-start stage. The stated purpose is that the model can "reassess tool outputs and, when necessary, to revise its tool-invocation decisions".[^c3] The motivation is that "errors can occur even when tools are invoked",[^c4] so a returned crop or mask is not automatically a safe basis for the next step.

The second condition carries the concept. A change of answer alone would not qualify; the change has to come with a change in what was looked at. The authors call such a pair "evidence of self-reflective strategy revision".[^c5] The record thus separates a revised decision about looking from a re-sampled answer, and it takes that record from the model's own training history rather than from a correction written by someone else. The cold-start traces were a different matter: they came from a stronger model, since "We leverage GPT-5 (OpenAI, 2025) to generate reasoning paths".[^c6]

What was measured. The comparison that isolates the self-reflection data is with a model trained for 12 epochs of plain SFT on the same cold-start set. The authors report that "the subsequent improvements primarily stem from fine-tuning on the self-reflection data rather than merely increasing the number of SFT epochs".[^c7] In the training dynamics, tool-call count and response length both rise early and fall later, and "Without self-reflection, early expansion is weaker".[^c8] I did not read the table values behind these comparisons in the slices I have, so the claims above are the authors' statements, not numbers I checked.

## Limits

- The rule needs labels. Correctness is checked against ground truth: "we simply check the exact match between the predicted and GT answers" for closed questions.[^c9] As written, the sampler cannot run on an unlabelled stream of model outputs.
- A flip is not necessarily revision. Sampling variance can produce a correct late answer reached with a different tool sequence. The paper groups every pair that meets the rule as self-reflection and does not report how many of them are noise. My reading is that the second condition raises the bar but does not remove this case.
- The comparison is against more SFT epochs, not against other ways of building revision data, such as the injected errors in [[reflection-token-error-injection]]. The text does not show which construction teaches revision better.
- One backbone: the experiments are "on Qwen2.5-VL-7B",[^c10] on medical VQA and segmentation. Whether the flip signal carries over to other domains or to other models is not tested.

## Related

- [[two-stage-decision-sampling]] — the decision to revise is what this sampling is meant to teach; that note isolates the decision stage, while this one supplies pairs of trajectories as training examples for it.
- [[reflection-token-error-injection]] — revision trained from errors placed at known positions; here the errors come from the model's own training history.
- [[strategic-perception-timing]] — when to look again mid-chain; the revised tool call in this method is one instance of that timing decision.
- [[tool-integrated-reasoning]] — the loop in which the revised call sits: each tool output re-enters the context before the next decision.
- [[sycophantic-capitulation]] — answer flips under pushback, the case where a change of answer is not tied to new evidence.

[^c1]: arxiv-2512-14157 — "tool-invocation sequences differ and the answer correctness flips"
[^c2]: arxiv-2512-14157 — "then examine them to identify such cases"
[^c3]: arxiv-2512-14157 — "reassess tool outputs and, when necessary, to revise its tool-invocation decisions"
[^c4]: arxiv-2512-14157 — "errors can occur even when tools are invoked"
[^c5]: arxiv-2512-14157 — "we regard this as evidence of self-reflective strategy revision"
[^c6]: arxiv-2512-14157 — "We leverage GPT-5 (OpenAI, 2025) to generate reasoning paths"
[^c7]: arxiv-2512-14157 — "the subsequent improvements primarily stem from fine-tuning on the self-reflection data rather than merely increasing the number of SFT epochs"
[^c8]: arxiv-2512-14157 — "Without self-reflection, early expansion is weaker"
[^c9]: arxiv-2512-14157 — "we simply check the exact match between the predicted and GT answers"
[^c10]: arxiv-2512-14157 — "on Qwen2.5-VL-7B"
[^c11]: arxiv-2512-14157 — "a versatile, tool-augmented framework"
