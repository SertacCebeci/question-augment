---
description: "A GRPO reward that adds a Brier/ECE calibration term and a rollout-group-supervised abstention term to accuracy, training a model to say \"not sure\" without hand-labelled unanswerable examples."
aliases: ["calibration reward", "abstention reward"]
sources: ["ding-2026"]
---
# SAVOR calibration-abstention reward

> A GRPO reward that scores the model's own confidence against its
> rollout group's realised accuracy, instead of scoring which answer a
> judge prefers.

## Definition / Mechanism

Ding et al. train the confidence signal used by
[[confidence-triggered-visual-reattention]] with a five-term GRPO reward
$R^{(g)} = R_{acc} + \lambda_1 R_{cal} + \lambda_2 R_{abs} + \lambda_3
R_{span} - \lambda_4 R_{cost}$. Beyond an accuracy term, "the reward
includes a [[calibration]] term that compares confidence with empirical
rollout accuracy, and an [[abstention]] term that discourages confident
guesses when the visual evidence is weak."[^c1]

The calibration term is a per-rollout Brier penalty on the answer
confidence plus a group-level Expected-Calibration-Error bonus. The
abstention term rewards the designated answer "I am not sure" only when
the prompt is judged intrinsically hard for the group, "where
'intrinsically uncertain' means that most rollouts in the group are
incorrect and the group accuracy is below a threshold τu."[^c2]

Because the reward reads this off the sampled rollouts rather than an
annotated label, "the abstention reward is therefore supervised by the
rollout group itself, removing the need for explicit 'unanswerable'
labels."[^c3]

## Why it matters

On the adversarial split of POPE, "Expected Calibration Error is reduced
from 0.272 with vanilla GRPO to 0.085 with Savor."[^c4]

The comparison is against DPO-family baselines (HA-DPO, mDPO, HALVA) and
vanilla GRPO retrained on the same prompt mix, which isolates the gain to
the added calibration and abstention terms rather than to more or
different training data.

## Transfer

| | |
|---|---|
| **Home field** | Statistical forecast evaluation — the Brier score and Expected Calibration Error measure how well a stated probability matches realised outcome frequency, developed for scoring human and weather forecasters. |
| **Here** | Both scores are folded directly into the per-rollout GRPO advantage as reward terms, so the policy is optimised against its own calibration error rather than against a preference judgement. |
| **What survives** | The scoring rules themselves — squared error against the outcome, and the binned confidence-vs-accuracy gap — and their property of penalising over- and under-confidence symmetrically. |
| **What does not** | The forecaster-scoring setting's independent, externally resolved outcome. Here "correctness" is read off the same model's rollout group and training annotations, not an outside resolution, so the target the reward chases can itself carry the group's own bias; the paper reports no external audit of this. |

## Limits

- Calibration and abstention are scored against rollout-group correctness
  and training-time annotations, not an outcome external to the training
  pipeline; a systematically biased rollout group would reward
  calibration against its own bias.
- Reported gains are against re-trained DPO-family and vanilla-GRPO
  baselines on one ~100K-prompt mix and two ~8B backbones; no
  independent replication is on record here.
- The five terms are combined with hand-set weights $\lambda_1$–$\lambda_4$;
  this note does not carry the paper's own ablation figures on how
  sensitive the calibration gain is to those weights.

## Related

[[confidence-triggered-visual-reattention]] · [[certainty-weighted-grpo-reward]] · [[calibration]] · [[abstention]] · [[calibration-training]]

[^c1]: ding-2026 — "the reward includes a calibration term that compares confidence with empirical rollout accuracy, and an abstention term that discourages confident guesses when the visual evidence is weak."
[^c2]: ding-2026
[^c3]: ding-2026
[^c4]: ding-2026 — "Expected Calibration Error is reduced from 0.272 with vanilla GRPO to 0.085 with Savor."
