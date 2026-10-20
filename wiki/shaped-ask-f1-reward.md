---
description: "Decomposing a sparse harmonic-mean metric into a dense per-question precision reward plus a terminal recall reward trains help-seeking judgment with RLVR, and the skill transfers across domains."
aliases: ["shaped Ask-F1 reward", "RLVR on Ask-F1"]
sources: ["arxiv-2604-09408"]
---
# Shaped Ask-F1 reward

> A metric built to resist gaming is, by the same construction, too sparse
> to differentiate — so it is split back into pieces before it can teach.

## Definition / Mechanism

[[ask-f1-selective-escalation-metric|Ask-F1]] "captures the right objective
but its harmonic-mean formulation is both abstracted and inherently sparse,
making it difficult [to] use to optimize directly with RL."[^c1]
Trinh et al. (2026) decompose it into two reward terms
supplied at different points in the trajectory. A per-step reward scores
every `ask_human()` call the moment it is issued: "+0.3 if q targets a
registered blocker, −0.1 if q is irrelevant or duplicates a resolved
blocker. The asymmetric magnitude encourages exploration of the question
space while penalizing noise." A terminal reward scores overall
coverage only at episode end, and only conditionally: "a terminal reward
captures overall coverage: $r_{terminal} = |B_{discovered}|/|B|$ when at
least one blocker is found, and 0 otherwise. The gate prevents degenerate
policies that avoid asking entirely." The split assigns each term a
distinct job — "per-step rewards shape precision; terminal coverage shapes
recall" — turning one sparse end-of-episode number into a signal dense
enough to credit-assign per question.

Trained into Qwen3-32B via LoRA (SkyRL, RLVR, no human annotation) on 120
tasks and evaluated on 30 held out per domain, the shaped reward "improves
both precision and recall on held-out tasks in both domains" and, more
tellingly, "a model trained exclusively on SQL tasks shows corresponding
Ask-F1 improvements on held-out SWE tasks, and vice versa. This transfer is
the strongest evidence that help-seeking judgment is a general skill, not a
domain-specific heuristic."[^c4]

## Why it matters

This is a training-signal answer to the mechanism gap the metric alone only
names: judgment about when to ask is "undertrained rather than untrainable"
— a verifiable, human-annotation-free reward moves it, and the improvement
in the process metric (Ask-F1) tracks the outcome metric (pass@3) in
lockstep, so the reward is not optimizing a proxy divorced from task
success.

## Limits

- Demonstrated on one 32B model with LoRA, one training framework, and 120
  training tasks per domain; whether the shaping recipe (fixed +0.3/−0.1
  step magnitudes, single-blocker terminal gate) holds at other scales or
  with full-parameter fine-tuning is unverified.
- The reward depends on the same frozen-LLM relevance judge as Ask-F1
  itself, so a systematic judge error becomes a systematic training signal
  error, not just a systematic evaluation error.
- Cross-domain transfer is reported only between two domains (SQL and SWE)
  that share the same tool interface and judge; transfer to a domain
  without a comparably clean blocker registry is untested.

## Related

- [[ask-f1-selective-escalation-metric]] — the metric this reward is a
  dense decomposition of.
- [[question-budgets]] — the asymmetric per-question reward is a learned,
  RL-internalized version of an externally imposed question-cost budget.
- [[abstention]] — the terminal, gated coverage term plays the role of a
  reject-option's activation condition, but for asking rather than
  answering.

[^c1]: arxiv-2604-09408 — "Ask-F1 captures the right objective but its harmonic-mean formulation is both abstracted and inherently sparse, making it difficult use to optimize directly with RL."
[^c4]: arxiv-2604-09408 — "a model trained exclusively on SQL tasks shows corresponding Ask-F1 improvements on held-out SWE tasks, and vice versa. This transfer is the strongest evidence that help-seeking judgment is a general skill, not a domain-specific heuristic."
