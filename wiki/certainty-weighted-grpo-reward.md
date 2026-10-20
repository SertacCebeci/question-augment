---
description: "A GRPO reward scaled by the agent's own belief certainty, so clarification is rewarded only when the model is genuinely unsure and confident tool calls are rewarded in full."
aliases: ["uncertainty-weighted GRPO", "certainty-weighted reward"]
sources: ["suri-2025"]
---
# Certainty-weighted GRPO reward

> A training signal for "ask vs act" that reads the model's own belief
> state instead of a judge's opinion of question quality.

## Definition / Mechanism

Suri et al. define, for an action $a_t$ (a tool call or a question) taken
under belief $\pi_c(t)$ over candidate tool calls, a certainty term
"Cert(at ) = maxc πc (t) if at is a tool call, 1 − maxc πc (t) if at is a
question, and 1 otherwise," and multiply it into a hand-scored base reward:
"Rcategory (at ) = Cert(at ) · rbase (at ) which up-weights confident
correct tool calls, penalizes low-certainty calls, and rewards
clarification only when uncertainty is high."[^c1]

The scaled reward trains a Group Relative Policy Optimization (GRPO)
policy — sampling several candidate actions per prompt and pushing the
policy toward those exceeding the group's mean reward — on 9K examples
drawn from the When2Call benchmark, where the model chooses among
`AskQuestion`, `CallTool`, `Decline`, or `DirectAnswer`.[^c2]

## Why it matters

On When2Call, the paper reports the certainty-weighted reward "boosts
When2Call accuracy from 36.5% to 65.2% (3B model) and 36.7% to 62.9% (7B
model) through uncertainty-weighted GRPO training, demonstrating more
sample-efficient reinforcement learning for tool-calling agents."[^c3]

The authors state the reward "needs no critic to judge question quality"
and is "self-calibrating" because the certainty term comes from the
policy's own belief rather than an external judge.[^c4]

## Transfer

| | |
|---|---|
| **In its home field** | GRPO (Shao et al. 2024) is a critic-free variant of PPO: it samples several completions per prompt and updates toward those exceeding the group mean reward, developed for domains with a checkable reward such as a math proof or a [[proactive-expertise-clarification|passing]] unit test. |
| **Here** | The checkable signal is replaced by the model's own posterior over candidate tool calls — a self-referential certainty term multiplied into a hand-scored base reward for schema correctness and action-type match. |
| **What survives** | The group-relative, critic-free update itself, and GRPO's tolerance for a scalar reward with no smooth gradient through it. |
| **What does not** | GRPO's original motivation — an externally checkable ground truth. Here the certainty term is computed from the same model being trained, so a reward that looks well-calibrated could instead reflect the model's own miscalibration; the paper does not report an independent check of `Cert` against ground-truth correctness. |

## Limits

- The reward's soundness depends on the belief state $\pi_c(t)$ itself
  being a reasonable estimate; the paper does not audit `Cert` against
  independently measured tool-call correctness, only against downstream
  task accuracy.
- Reported gains are on one benchmark family (When2Call/BFCLv2) built by
  related prior work, at two model scales (3B, 7B); no independent
  replication is on record.
- The base reward `rbase` mixes format, tool-match and classification terms
  by hand-set weights (1.5 / 1.0 / up to 2.0); the certainty scaling is
  multiplicative on top of that hand design, not a replacement for it.

## Related

[[investigative-question-grpo-training]] · [[uncertainty-decomposition]] · [[tool-call-evpi-question-selection]] · [[calibration]] · [[value-of-information]]

[^c1]: suri-2025 — "Cert(at ) = maxc πc (t) if at is a tool call, 1 − maxc πc (t) if at is a question, and 1 otherwise"
[^c2]: suri-2025 — "AskQuestion, CallTool(parameters), Decline, or DirectAnswer"
[^c3]: suri-2025 — "boosts When2Call accuracy from 36.5% to 65.2% (3B model) and 36.7% to 62.9% (7B model) through uncertainty-weighted GRPO training, demonstrating more sample-efficient reinforcement learning for tool-calling agents"
[^c4]: suri-2025
