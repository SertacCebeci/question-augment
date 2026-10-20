---
description: "A code-agent benchmark that replaces one-shot fully-specified prompts with underspecified intent resolved by a Code Agent/UI Agent/User LLM feedback loop over multiple rounds."
aliases: ["Asuka-Bench"]
sources: ["wang-2026-asuka"]
---
# Asuka-Bench

> A code agent is never told the full spec up front; it is scored on how
> fast it closes the gap between an underspecified request and a rendered
> target by acting, observing browser-grounded feedback, and revising —
> not by asking a clarifying question.

## Definition / Mechanism

Existing code-generation and web-generation benchmarks score a single
mapping from a complete, unambiguous prompt to a one-shot output.
Asuka-Bench instead pairs a **deliberately underspecified** initial
request with a closed loop of three roles: a Code Agent generates a web
project from the underspecified request; a UI Agent deploys it and drives
browser interaction to judge natural-language test criteria from rendered
behaviour, not source code; a User LLM turns the per-criterion pass/fail
outcomes into natural-language feedback for the Code Agent's next round.
The loop repeats until all criteria pass or a round cap is reached. The
benchmark has 50 web tasks, 784 evaluation criteria and 2,402 expected
outcomes, run across 8 LLMs and 2 agent frameworks (Claude Code,
OpenHands).[^c1]

The loop resolves [[efe-planning-as-variational-inference|ambiguity]] entirely through **observed, browser-grounded
[[outcome-feedback|outcome feedback]]** — pass/fail plus a natural-language reason — never
through an explicit clarifying question exchanged with a user; no role in
the loop asks the requester anything.

## Why it matters

Two headline measurements, on 8 frontier LLMs (GPT-5.4, Claude-4.6-Sonnet,
Gemini-3.1-Pro, GLM-5, Qwen3.5-Plus, Kimi-K2.6, MiniMax-M2.7,
Seed-2.0-Pro): weighted Task Pass Rate varies by 38 percentage points
across models, and "even the strongest model completes only 52% of
projects after three rounds."[^c2]

Comparing a single round on a fully-specified ("Clarified PRD") prompt
against three rounds on the underspecified query with browser-grounded
feedback: "The first ambiguous round loses 9–18 pp relative to the PRD
baseline, but every model overtakes its PRD score by Round 3 (net gains
8.7–26.6 pp), confirming that multi-round refinement on an ambiguous start
can match—and exceed—a fully specified one-shot prompt."[^c3]

A second, separable finding: repair-from-feedback ability does not track
first-round generation quality. "Kimi-K2.6 on OpenHands climbs 44.3% →
74.7% → 86.6%, ending second-best in its framework after a mediocre first
round." The paper reads this as showing "repair-from-feedback ability is
largely decoupled from first-round generation quality, revealing a
capability axis that existing one-shot benchmarks cannot surface."[^c4]

## Limits

- The claim that iterative refinement can match or exceed a fully
  specified one-shot prompt rests on giving both conditions "the same
  eventual information" (PRD-1R vs. three ambiguous rounds) in one domain
  (self-contained frontend web generation with simulated data); it does
  not show refinement beats specification when the two are not
  information-matched, or outside this domain.
- The feedback channel is a User LLM synthesising UI-Agent test results,
  not a human; the paper's own human-agreement check (93.35% accuracy,
  96.52% F1 against expert annotators on a 50-project, 5-model sample)
  bounds but does not eliminate simulated-user noise, and was not read in
  full by this note.
- No role in the loop ever asks a clarifying question of the requester —
  the mechanism is closer to test-driven repair than to the clarification
  benchmarks family on this stall's map ([[clarification-benchmarks]]),
  which scores whether an agent elicits missing information by asking; a
  reader should not treat Asuka-Bench's numbers as comparable to that
  table.

## Related

[[clarification-benchmarks]] · [[dag-aware-evaluation-protocol]] · [[questioning-and-solving]]

[^c1]: wang-2026-asuka — "Each task is resolved through a closed loop: a Code Agent generates a web project, a UI Agent executes test cases on the deployed site, and a User LLM turns evaluation outcomes into natural-language feedback for the next round. The benchmark comprises 50 web tasks with 784 evaluation criteria and 2,402 expected outcomes. We benchmark 8 LLMs across 2 agent frameworks."
[^c2]: wang-2026-asuka — "weighted Task Pass Rate varies by 38 percentage points and models also differ substantially in their ability to repair from feedback. Asuka-Bench is also far from saturated: even the strongest model completes only 52% of projects after three rounds."
[^c3]: wang-2026-asuka — "The first ambiguous round loses 9–18 pp relative to the PRD baseline, but every model overtakes its PRD score by Round 3 (net gains 8.7–26.6 pp), confirming that multi-round refinement on an ambiguous start can match—and exceed—a fully specified one-shot prompt."
[^c4]: wang-2026-asuka — "Kimi-K2.6 on OpenHands climbs 44.3% → 74.7% → 86.6%, ending second-best in its framework after a mediocre first round."
