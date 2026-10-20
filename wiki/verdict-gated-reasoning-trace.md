---
description: "A judge trains on its own reasoning traces only where the verdict matches a preference known by construction in both response orders; the verdict gates the trace."
aliases: ["verdict-filtered self-training", "outcome-gated rationale", "correct-verdict trace filtering", "self-generated judge traces with order check"]
sources: ["arxiv-2512-05145"]
---
# Verdict-gated reasoning trace

A judge that writes a reasoning trace and then a verdict can be trained on its own output, provided something outside the trace decides which outputs count. In the paper the outside check is a preference known by construction. For each pair, the current judge is sampled several times; each sample is a reasoning trace and a binary decision. Only samples whose decision picks the known preferred response are kept: the training set is built "by selecting only samples where the model correctly identifies the preference."[^v1]

The gate is applied twice, once per response order. Each pair is judged with the preferred response first and again with it second, and "pairs where the model makes the correct judgment in both configurations" are the ones retained.[^v2] The stated purpose is to separate a real signal from position: a judge that is right in only one order is probably answering the position, not the content. The stated reason is that correct judgments in both orders show the model's reasoning outweighs its positional bias, "reducing cases where the model arrives at the right" answer for the wrong reasons.[^v3]

Training is ordinary supervised fine-tuning on the kept traces: "We use supervised fine-tuning to train the judge using the curated dataset."[^v4] The trace and the verdict are the target together, so the judge is taught to reason toward the preference, not only to output it. The authors describe this as bootstrapping from the judge's own reasoning without amplifying its mistakes; in their words, "This focuses learning on reasoning patterns that consistently lead to correct judgments."[^v5]

## What the gate changed

The gate is loose by design, so the amount it keeps is a result. The share of training data that survives rises with each iteration: "the percentage of retained training data increases from 19% at" the baseline, "baseline to 43% by iteration 4."[^v6] The paper reads the rising share as a judge that has become better, so the same gate admits more of its traces. The loop iterates until "performance plateaus, operationally defined as less than 1% relative" gain over three iterations.[^v7]

The headline result for this training is "Our method improves the model from 0.38 to 0.51 overall accuracy" on VL-RewardBench, for a Llama-3.2-11B-based judge.[^v8]

## Limits

- The gate checks the verdict, not the trace. The paper's own example is a judge whose reasoning favored style over accuracy and missed "failing to identify that Response A contains a transcription error."[^v9] The authors state the consequence: "the correctness of the preferred answer does not guarantee the validity of the judgment reasoning."[^v10] A right verdict with a broken trace passes the gate.
- The reasoning-quality check is small. A blind manual evaluation of 20 sampled examples is the only direct look at the traces in the text I read.[^v11] Twenty examples cannot show how often a kept trace is unsound.
- Position bias is handled by a filter, not measured. The text reports the retention rate, not how much position preference remains in the judge after training. My reading: the both-orders rule removes pairs the judge gets right only by position, but does not show the judge is free of position bias. See [[bidirectional-preference-entropy]] for the same order swap used as an uncertainty score.
- The gate inherits its label. Whatever the construction calls preferred becomes the target: a consensus in [[majority-consensus-preference-pair]], an edit direction in [[controlled-error-injection]]. The gate cannot correct a wrong known preference.
- Later iterations are not monotone. On the reasoning dimension the paper reports "non-monotonic optimization behavior with peak performance at iteration 3 (0.612)," which it reads as "potential signs of overfitting in later iterations."[^v12]
- The gain does not reach every dimension. The paper says its synthetic data did not cover harmful content: "our framework does not generate synthetic training data containing biased, toxic, or otherwise" harmful outputs, and safety gains were small.[^v13] The gate only selects among what the construction produces.

## Related

- [[majority-consensus-preference-pair]] — the known preference this gate checks when no gold label exists.
- [[controlled-error-injection]] — the known preference for open-ended answers, where the edit fixes the direction.
- [[bidirectional-preference-entropy]] — the same both-orders check, used there to score a judge's uncertainty rather than to choose training targets.
- [[retrieval-grounded-rationale-distillation]] — another way to shape the traces a student learns from: there the evidence is put in the teacher's prompt, here the verdict is checked after the trace is written.
- [[mcq-answer-position-bias]] — the first-position preference that the both-orders rule is meant to filter out, in the multiple-choice case.

[^v1]: arxiv-2512-05145 — "by selecting only samples where the model correctly identifies the preference"
[^v2]: arxiv-2512-05145 — "pairs where the model makes the correct judgment in both configurations."
[^v3]: arxiv-2512-05145 — "reducing cases where the model arrives at the right"
[^v4]: arxiv-2512-05145 — "We use supervised fine-tuning to train the judge using the curated dataset"
[^v5]: arxiv-2512-05145 — "This focuses learning on reasoning patterns that consistently lead to correct judgments."
[^v6]: arxiv-2512-05145 — "the percentage of retained training data increases from 19% at"
[^v7]: arxiv-2512-05145 — "We iterate the training process until overall performance plateaus, operationally defined as less than 1% relative"
[^v8]: arxiv-2512-05145 — "Our method improves the model from 0.38 to 0.51 overall accuracy"
[^v9]: arxiv-2512-05145 — "failing to identify that Response A contains a transcription error."
[^v10]: arxiv-2512-05145 — "the correctness of the preferred answer does not guarantee the validity of the judgment reasoning."
[^v11]: arxiv-2512-05145 — "Blind manual evaluation of 20 randomly"
[^v12]: arxiv-2512-05145 — "non-monotonic optimization behavior with peak performance at iteration 3 (0.612)"
[^v13]: arxiv-2512-05145 — "our framework does not generate synthetic training data containing biased, toxic, or otherwise"
