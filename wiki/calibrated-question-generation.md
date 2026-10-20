---
description: "Score a generated question by whether exactly one of two capability-bounded solver models answers it, after the asker probes both via dialogue."
aliases: ["Ask-E", "calibrated question generation", "evaluation as mutual supervision"]
sources: ["pratt-2026"]
---
# Calibrated question generation (Ask-E)

> A question is scored not by a supervisor's judgement of its content but by
> whether it splits two solver models of known, ordered ability — exactly
> one must succeed.

## Definition / Mechanism

Pratt, Park & Geng (2026) define a target difficulty range by
two existing boundary solver models, a weaker and a stronger. "A generated
question is successfully calibrated if exactly one of the two models can
solve it, placing it precisely within the target range and differentiating
the capabilities of these models."[^c1]

The asker does not write the question cold. "The asker first probes the
models in the pair to identify their capability difference, and then
produces a final question that targets this span between the two models'
skill levels."[^c2]

Grading uses a separate cross-check solver (a frontier model on the
benchmark, the asker's own current weights during RL training) to score
the final answers; a session only counts when independent samples of the
cross-check agree, so an unstable or ambiguous answer is discarded rather
than scored as calibrated. A question is *too easy* if both boundary
solvers answer correctly, *too hard* if both fail, *calibrated* if exactly
one succeeds. During RL training the per-rollout reward sums a [[calibration]]
term (+1.0 calibrated, +0.2 too easy, −0.2 too hard), a format penalty, and
an embedding-diversity bonus; the boundary set is restricted to models at
or below the asker's own ability and their tokens are masked from the
loss, so no stronger model's reasoning can leak into the policy.

## Known as

| Field | Name there | Match |
|---|---|---|
| LLM training/evaluation (Pratt et al. 2026) | Ask-E | exact — the environment's proper name |
| LLM training/evaluation (Pratt et al. 2026) | calibrated question generation | exact — the task Ask-E benchmarks and trains |
| LLM training/evaluation (Pratt et al. 2026) | evaluation as mutual supervision | close — the paper's framing for why the task grades itself, not the scoring mechanism |
[^c3]

## Why it matters

"State-of-the-art models achieve only 44.9% success rate, demonstrating
substantial room for improvement," and even frontier models stay below 50%
calibration across boundary-solver pairs.[^c4]

The score is self-scaling: as models improve, stronger boundary pairs raise
the difficulty ceiling automatically, unlike a fixed problem set that
saturates.

## Limits

- Depends on questions with a checkable answer: the reward and the
  benchmark both need rule-based or LLM-judged equivalence matching, so the
  calibration signal is defined here for math and needs a different
  cross-check for open-ended domains.
- "Calibrated" is relative to a fixed, finite boundary-solver set, not an
  absolute difficulty scale; the paper's own limitations note that a
  question with an unstable or ambiguous answer could in principle satisfy
  the calibration criterion without probing real skill, mitigated only by
  discarding sessions where the cross-check samples disagree.
- The cross-check solver itself is a model, not ground truth: on the
  benchmark a frontier model's three-sample consensus stands in for
  correctness, so a systematic error shared across cross-check samples
  would misgrade calibration undetected.

## Related

[[investigative-question-grpo-training]] · [[mutual-information]] · [[question-asking-skill-transfer]] · [[expected-information-gain]]

[^c1]: pratt-2026 — "A generated question is successfully calibrated if exactly one of the two models can solve it, placing it precisely within the target range and differentiating the capabilities of these models."
[^c2]: pratt-2026 — "The asker first probes the models in the pair to identify their capability difference, and then produces a final question that targets this span between the two models’ skill levels."
[^c3]: pratt-2026 — "we present Ask-E, an environment that benchmarks and trains models on their ability to write questions at a given skill level"
[^c4]: pratt-2026 — "State-of-the-art models achieve only 44.9% success rate, demonstrating substantial room for improvement."
