---
description: "Training a model only to generate calibrated math questions, with no correctness feedback, raised its own downstream math-answering scores."
aliases: ["RL training on Ask-E", "asking-to-answering skill transfer"]
sources: ["pratt-2026"]
---
# Question-asking skill transfer

> Reinforcement learning on question generation alone, scored only by
> whether the question splits two solver models, improved the trained
> model's own answers on separate math benchmarks.

## Definition / Mechanism

Pratt, Park & Geng (2026) train Qwen3.5-4B as an asker
policy inside [[calibrated-question-generation|Ask-E]]. "The model is
trained exclusively on question generation. It never receives feedback on
the correctness of its own answers, and its reward is derived entirely
from the answer distribution of solvers at or below its own ability."[^c1]
The boundary solvers used for reward are 12 open-weight models of 1.5B–8B
parameters, all at or below the asker's own math ability, and their tokens
are masked out of the training loss — ruling out the trained model simply
imitating a stronger model's reasoning through the reward channel.

## Why it matters

Evaluated on AIME, HMMT and IMO-AnswerBench after 200 RL steps across three
seeds: "Ask-E training improves pass@8 performance on all benchmarks with
one tie, and avg@8 performance on 3 out of 4 benchmarks. Notably, this
improvement occurs without any new math data, any interaction with
stronger models, or any feedback on the correctness of the trained model's
answers."[^c2]

The reported gains are modest — low single-digit percentage-point moves in
pass@8, one metric tied — but they are gains on the model's own
answer-generation ability produced purely by practicing question
generation.

## Limits

- One base model (Qwen3.5-4B), one training stack, 200 optimizer steps,
  three seeds; the size and the consistency of the transfer effect across
  other model families or scales is not shown.
- The boundary set is deliberately weak-only (models at or below the
  asker's own ability); the paper's causal claim — that calibrating
  questions demands the skills needed to solve them — rests on this design
  ruling out distillation from a stronger model, not on an independent
  test of the mechanism.
- Downstream evaluation is limited to math benchmarks scored by rule-based
  or LLM-judged equivalence; transfer to non-math question-asking or
  question-answering skill is untested here, and `replicated: false`
  because no independent replication of this specific transfer result was
  found in the material read for this note.

## Related

[[calibrated-question-generation]] · [[investigative-question-grpo-training]] · [[mutual-information]]

[^c1]: pratt-2026 — "The model is trained exclusively on question generation. It never receives feedback on the correctness of its own answers, and its reward is derived entirely from the answer distribution of solvers at or below its own ability."
[^c2]: pratt-2026
