---
description: "A consensus answer chosen by summing each sample's average step confidence rather than counting votes, so a confident minority path can beat a frequent but uncertain majority answer."
aliases: ["confidence-weighted pseudo-label", "confidence-weighted voting", "average step confidence consensus", "SCOPE step-wise confidence"]
sources: ["arxiv-2512-15146"]
---
# Step-confidence-weighted consensus

A set of sampled answers can be reduced to one label by counting votes, or by weighting each vote with how sure the model was while it wrote that answer. The second is the mechanism here. The paper splits each response into reasoning steps, "by newline delimiter" (blank lines), and computes the confidence of a step by "averaging the confidence scores of" its tokens.[^s1] The response's score is the average over its steps. The consensus label is then the candidate answer with the largest sum of these scores, not the largest count: "Unlike naive majority voting, our method assigns higher importance to responses with higher average step confidence."[^s2]

The paper's illustration is a single question with eight sampled responses whose votes for five candidate answers are 1, 3, 1, 2 and 1. Plain majority selects the answer with three votes. That answer's paths show low confidence, while the answer with two votes "demonstrates higher accumulated confidence and is the correct solution."[^s3] The label therefore moves from the popular answer to the confident one. The reward for each sampled response then tests agreement with this weighted label.

The motivation is the same as in other self-consensus reward schemes: the paper argues that counting treats every vote alike, "treats all votes equally", so a wrong majority is rewarded.[^s4] In its ablation, returning to majority voting while keeping everything else lowered the score on AIME 2024 for Qwen3-8B, and the authors read this as "confirming that naive majority voting is an unreliable proxy for reasoning".[^s5]

What survives transfer to asking and answering: a vote can be weighted by a graded signal the model already produces, so the choice among its own candidate answers need not be a count. What does not transfer by itself is the training loop, the reward it feeds, and any claim that the weighted answer is better at inference time. The paper uses the consensus only as a reward target.

## Limits

- The evidence is one paper. Its tasks are competition math (AIME, AMC) on Qwen and LLaMA models inside a reinforcement-learning loop. The weight is measured only as one part of a larger method (SCOPE), which also partitions responses into subgroups; the ablation removes the confidence term but cannot show what the confidence term does on other tasks.
- The step is defined by a heuristic: the paper says its "step definition relies on heuristic segmentation based on newline characters," and that this "assumes a structured generation pattern."[^s6] A model whose output does not break at blank lines gets different steps, and so a different weight.
- The confidence is the model's own token-level signal. Nothing in the text checks whether a confidently wrong path can take the vote. The paper's example is one where confidence helps; a confidently wrong majority would be weighted up in the same way. This is my inference, not a tested result.
- The pseudo-label accuracy diagnostic compares the full method with TTRL, not the confidence term alone: "SCOPE consistently improves PLA over TTRL across different subgroup" settings.[^s7] So the diagnostic does not isolate the weighting.
- Compared with a tool check, the weight is not a verification. Whether a model's own confidence carries as much signal as an external check is not measured in this work.

## Related

- [[verification-weighted-voting]] — the same operation (weight votes rather than count them), with an external code check as the weight instead of the model's own confidence
- [[certainty-weighted-grpo-reward]] — scales a reward by the model's own certainty; here the certainty scales a vote that sets the reward target
- [[stepwise-confidence-temporal-signature]] — the trajectory of confidence over reasoning steps; the average step confidence here collapses that trajectory to a mean

[^s1]: arxiv-2512-15146 — "calculated by averaging the confidence scores of"
[^s2]: arxiv-2512-15146 — "assigns higher importance to responses with higher"
[^s3]: arxiv-2512-15146 — "demonstrates higher accumulated confidence and is the"
[^s4]: arxiv-2512-15146 — "This coarsegrained estimation process treats all votes equally"
[^s5]: arxiv-2512-15146 — "confirming that naive majority voting is an unreliable proxy for reasoning"
[^s6]: arxiv-2512-15146 — "on heuristic segmentation based on newline characters."
[^s7]: arxiv-2512-15146 — "SCOPE consistently improves PLA over TTRL across different subgroup"
