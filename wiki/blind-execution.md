---
description: "Interactive coding agents read user intent well (IAS>3.9/5) yet proactively identify missing requirements in under 40% of cases, defaulting to over-generation and hallucination instead of asking."
aliases: ["blind execution failure mode"]
sources: ["arxiv-2604-27419", "arxiv-2512-05930"]
---
# Blind execution

> An agent that reads a request accurately can still fail to notice what
> the request leaves out, and answer the gap by generating rather than
> asking.

## Definition / Mechanism

Wang et al. (2026) name **blind execution**: the
semantic misalignment between ambiguous, low-quality instructions from a
non-expert user and a coding agent's understanding of them, which the
agent resolves by proceeding on its own reading instead of surfacing the
gap.
[^c1]

They measure it inside an interactive website-generation
benchmark whose agents hold a four-way action space — `Clarify`,
`Implement`, `Verify`, `Submit` — so asking is always an available,
equally-cheap move, not a capability the agent lacks. Across nine
frontier MLLM-based agents (Qwen, Kimi, GPT-4.1, Gemma, Gemini) evaluated
this way, all of them remain trapped in blind execution regardless of
whether the action is offered.
[^c2]

The gap is not a comprehension
failure: an Intent Alignment Score judging how well an agent's stated
reasoning matches the ground-truth requirement stays above 3.9/5 for
every model, while a separate Clarification Hit Rate — whether a
`Clarify` action actually surfaces a hidden constraint — stays under
40% for all of them. Agents read the request correctly and act on the
wrong one anyway.

## Why it matters

Instructions that merely add noise are recovered better than
instructions that omit something: task-completion scores are higher
under a "rambling" user persona (redundant, low signal-to-noise
instructions) than under a "minimal" persona (a required detail simply
missing).
[^c3]

The models do not compensate for the missing
detail by asking either; they compensate by generating more code —
larger outputs correlate with higher hallucination rates (unrequested
UI elements), not with more clarification actions taken, "resulting in
increased code size and higher hallucination rates."
[^c4]

Even the
best-scoring model, evaluated end to end on a constraint-slot task
completion metric, satisfies only 38.78% of a task's oracle
constraints.
[^c5]

Together the four findings separate two things
usually conflated in an "asking" metric: a model can understand a
request (high IAS) without ever converting that understanding into a
question (low CHR) — the deficit sits specifically at the
decision to act on an unknown rather than at detecting it, and is
asymmetric by defect type (missing vs. noisy).

A controlled version of the same gap appears in PRiSM, a physics and mathematics benchmark for vision-language models. There the ambiguity is made by masking 20-30% of the input variables and replacing them with symbolic placeholders.[^c6] The prompt does ask for the missing piece: models were instructed "to request clarification when necessary."[^c7] Even so, symbolic reasoning appeared in only 4–5% of cases and deferral in 3–4%.[^c8] The paper reports that models "frequently ignored ambiguity, proceeding with unsupported completions."[^c10] A manual review found that they "seldom ask clarifying questions and often make unsupported assumptions based on" visual cues or default values.[^c9] My reading: here asking is an instruction inside the prompt rather than an action in a menu, so the shortfall cannot be put down to a missing affordance. The PRiSM scores do not separate failing to notice the gap from failing to act on it.

## Limits

- The Clarification Hit Rate and Intent Alignment Score are both
  LLM-as-judge scores (GPT-5-mini), not a ground-truth annotation of
  which hidden constraint was actually needed.
- The simulated user is itself an LLM (DeepSeek-V3.2) under a
  persona-conditioned prompt, not a human low-code user; how well the
  persona taxonomy transfers to real non-expert phrasing is not
  established in this extract.
- The result is domain-specific to interactive website generation under
  a four-action space; whether the same IAS-high/CHR-low split holds
  where clarifying is costlier or the action space is narrower is not
  tested here.
- The over-generation compensation (^c4) is a correlation across nine
  models, not an ablation that forces one model to ask more and
  measures the resulting hallucination rate.
- The PRiSM ambiguity scores come from an LLM judge, checked by hand on a
  sample.[^c11] The paper itself says that ambiguity handling is
  "assessed qualitatively via an LLM-as-judge framework."[^c12] Its masking is
  synthetic and its domain is physics and mathematics, not an interactive
  coding task, so it is not evidence about blind execution in the sense of
  the first paper.

## Related

[[clarification-benchmarks]] · [[compliance-bias]] · [[ambiguity-taxonomy]] · [[expected-information-gain]]

[^c1]: arxiv-2604-27419 — "the semantic misalignment between ambiguous, low-quality instructions from non-expert users and model understanding, which results in a failure mode that we term blind execution."
[^c2]: arxiv-2604-27419 — "frontier MLLM-based agents remain trapped in blind execution, exposing limitations in intent recognition and adaptive interaction."
[^c3]: arxiv-2604-27419 — "Almost all models achieve higher TCR score under the P-RAM setting, while significantly lower performance is observed under P-MIN setting."
[^c4]: arxiv-2604-27419 — "models tend to compensate for missing requirements through aggressive generation rather than iterative clarification, resulting in increased code size and higher hallucination rates."
[^c5]: arxiv-2604-27419 — "the best-performing model, Qwen3.6-Plus, achieving only 38.78%."
[^c6]: arxiv-2512-05930 — "20-30% of input variables and replacing them with symbolic placeholders."
[^c7]: arxiv-2512-05930 — "to request clarification when necessary."
[^c8]: arxiv-2512-05930 — "Symbolic reasoning occurred in only 4–5% of cases, and deferral in just 3–4%."
[^c9]: arxiv-2512-05930 — "models seldom ask clarifying questions and often make unsupported assumptions based on"
[^c10]: arxiv-2512-05930 — "Despite explicit instructions, models frequently ignored ambiguity, proceeding with unsupported completions."
[^c11]: arxiv-2512-05930 — "Since our judge may introduce some bias, we performed a manual review of 100 randomly"
[^c12]: arxiv-2512-05930 — "assessed qualitatively via an LLM-as-judge framework."
