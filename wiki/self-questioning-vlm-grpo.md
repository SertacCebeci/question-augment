---
description: "GRPO-trained vision-language models that generate their own sub-question/sub-answer chains before a final answer, rewarded only on output format and answer correctness."
aliases: ["self-questioning framework", "SQ+GRPO", "self-questioning VLM"]
sources: ["amjith-2026"]
---
# Self-questioning VLM (GRPO)

> A vision-language model trained with Group Relative Policy Optimization
> to break a compositional visual question into its own sub-questions and
> sub-answers before committing to a final answer — with no human
> decomposition ever shown to it.

## Definition / Mechanism

Amjith (2026) trains Qwen2.5-VL-3B-Instruct with GRPO on a
reward that is 1.0 only if the output both follows a
`Sub-question/Answer …/Final Answer` structure and reaches the correct
final answer, and −1.0 otherwise; the number of sub-questions is left to
the model. The prompt gives the format but no worked example of a
decomposition. On A-OKVQA (real-world VQA), this self-questioning (SQ)
training reaches 52.2% accuracy against 51.6% for an otherwise identical
GRPO run rewarded only on the final answer (Direct+GRPO), both up from the
untrained base model's 46.8%.[^c1]

The self-questioning behaviour is not demonstrated, only rewarded: "The
model is never shown examples of how to decompose questions, it discovers
this behavior on its own, guided by a reward signal that scores whether the
output contains sub-questions and whether the final answer is correct." Its
own marginal contribution over plain RLVR training is small — a further
+0.6 percentage points on top of RL's +4.8.[^c2]

A model trained to self-question on synthetic CLEVR scenes transfers the
skill to real photographs: "A model trained with self-questioning on a
dataset of synthetic images is able to transfer this skill when tested on
real-world photographs (+2.6% over baseline)."[^c3]

The format itself is not free. On CLEVR — where the base model is already
near ceiling (97.4%) — forcing the A-OKVQA-trained self-questioning model
to use its sub-question format drops accuracy to 81.0%, recovering to 97.6%
with a direct prompt: "Self-questioning introduces a format tax: the
A-OKVQA-trained SQ model drops to 81.0% with the SQ prompt but recovers to
97.6% with a direct prompt, confirming the model weights are intact."[^c4]

## Known as

| Field | Name there | Match |
|---|---|---|
| RL for VLMs (Amjith 2026) | self-questioning framework | exact — this note's object |
| RL for VLMs (Amjith 2026) | SQ+GRPO | exact — the specific trained-model label in the paper's tables |

**Not this concept.** [[investigative-question-grpo-training]] also trains
a question-generator with GRPO, but its reward is format-plus-a-separate-LLM-judge
over investigative relevance, in a video-captioning domain, and its result
is a factual-accuracy/completeness trade-off — a different reward, a
different domain, a different measured quantity. [[chain-of-self-questioning]]
also decomposes a question before answering but is a prompt-only method
with no training signal at all. Both are filed as related, not identical.

## Why it matters

This is a case where the reward shapes *whether the agent asks itself
anything at all*, not which of several pre-existing questions to ask: the
decomposition strategy is discovered, not selected from a candidate set.
For this stall it shows that rewarding the act of sub-questioning, on top
of answer correctness, buys little once RL training is already present —
most of the accuracy gain here is RLVR, not self-questioning — and that
forcing self-questioning on a task too easy to need it costs accuracy
rather than adding robustness.

## Transfer

| | |
|---|---|
| **In its home field** | GRPO, applied by DeepSeek-R1 to text-only LLMs, rewards only a correct final answer in a structured format and lets chain-of-thought reasoning emerge without demonstrations, using group-normalised advantages instead of a learned value function. |
| **Here** | Extended to a multimodal setting — the policy must attend to image tokens while generating each sub-question — and the reward is tightened to require an explicit sub-question/sub-answer structure, not free-form reasoning text. |
| **What survives** | Reward-only emergence: decomposition behaviour appears without any human-written reasoning trace, and group-relative advantage estimation needs no separate value network. |
| **What does not** | The assumption that structure is free. In text-only CoT the format reward rarely costs accuracy; here the enforced sub-question format measurably hurts a model on questions simple enough not to need it (the format tax on CLEVR), a failure mode this transfer introduces rather than inherits. |

## Limits

- One base model (Qwen2.5-VL-3B-Instruct), one training budget (~7,000
  GRPO steps, LoRA rank 16) on two datasets; the reported magnitudes
  (+0.6pp SQ-over-RLVR, +2.6pp transfer, the CLEVR format tax) are this
  configuration's, not shown to generalise across model scale or task.
- Correctness is judged by substring containment between normalised
  ground truth and prediction, which can both over- and under-credit an
  answer independent of its actual correctness; the accuracy numbers
  inherit that metric's noise.
- The comparison isolates self-questioning from RLVR by holding
  hyperparameters and data fixed across the two runs, but both runs share
  the same reward-hacking risks of containment matching, so the two are
  not independently validated against a held-out judge.

## Related

[[investigative-question-grpo-training]] · [[chain-of-self-questioning]] · [[preference-optimization-for-questions]] · [[expected-information-gain]]

[^c1]: amjith-2026 — "On A-OKVQA, both self-questioning and standard reinforcement learning substantially improve accuracy over the untrained model (52.2% and 51.6% vs. 46.8%)."
[^c2]: amjith-2026 — "The model is never shown examples of how to decompose questions, it discovers this behavior on its own, guided by a reward signal that scores whether the output contains sub-questions and whether the final answer is correct."
[^c3]: amjith-2026 — "A model trained with self-questioning on a dataset of synthetic images is able to transfer this skill when tested on real-world photographs (+2.6% over baseline)."
[^c4]: amjith-2026 — "Self-questioning introduces a format tax: the A-OKVQA-trained SQ model drops to 81.0% with the SQ prompt but recovers to 97.6% with a direct prompt, confirming the model weights are intact."
