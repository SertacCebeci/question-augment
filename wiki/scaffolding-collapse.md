---
description: "A failure mode where an LLM Socratic tutor, under sustained adversarial pressure, abandons guided questioning and reveals the answer directly; measured per attack type as a collapse rate."
aliases: ["scaffolding collapse"]
sources: ["shao-2026"]
---
# Scaffolding collapse

> A [[staged-socratic-hint-policy|Socratic]] tutor keeps asking probing questions instead of stating the
> solution — until, under enough student pressure, it does not. Naming and
> measuring that point is a direct empirical constraint on any axis-selection
> policy that is supposed to keep probing rather than distill early.

## Definition / Mechanism

Shao et al. (2026) define scaffolding collapse as "a
trajectory-level pedagogical failure ... in which a tutor that initially
follows Socratic constraints degenerates into a collapse mode over the
course of a dialogue," distinguishing it from a single unsafe reply because
"this degradation emerges cumulatively across turns rather than from a
single unsafe query."[^c1]

Measured on Qwen3-8B with Socratic prompting across five red-teaming attack
strategies, the collapse rate is sharply attack-dependent: "Direct Answer
Request achieves the highest collapse rate of 68%, followed by Progressive
Answer Extraction with a collapse rate of 61%. These two strategies are
substantially more effective than others, whose collapse rates remain
around 33%–36%."[^c2]

The output-level failure is preceded by a measurable shift in hidden
representations: at the turn before collapse, "(τ −2) already tracks the
onset pattern, indicating that representation drift emerges before the
behavioral collapse."[^c3]

## Why it matters

On stall 2, this is a measured limit on any policy that selects "keep
probing the current axis" turn after turn: the selection can be overridden
by accumulated pressure rather than by any single bad question, and the
override is visible in the model's internal state before it appears in the
model's output. A note that only scores the next question by information
gain has nothing to say about this drift.

## Limits

- A single, non-peer-reviewed 2026 arXiv preprint; the numbers above are
  this one paper's own classifier-based collapse-rate measure, not
  independently validated against real student outcomes. `[?]` unverified
  beyond the arXiv listing.
- Measured on one [[backbone-of-a-formula|backbone]] family (Qwen3-8B and others reported in an
  appendix this note does not draw on) under the paper's own five
  red-teaming attack strategies and five STEM domains; whether the same
  collapse rates hold for other backbones, subjects, or genuinely
  adversarial (not simulated) students is not shown here.
- "Collapse" is operationalised as the tutor's turn revealing the final
  answer or key equation; softer scaffolding failures (a hint that is too
  strong, a [[leading-question-rule|leading question]]) are not counted and may be under-measured by
  this rate.

## Related

[[socratic-method]] · [[dpo-behavioral-reprogramming]] · [[preference-optimization-for-questions]] · [[reliability-aware-dpo]]

[^c1]: shao-2026
[^c2]: shao-2026 — "Direct Answer Request achieves the highest collapse rate of 68%, followed by Progressive Answer Extraction with a collapse rate of 61%. These two strategies are substantially more effective than others, whose collapse rates remain around 33%–36%."
[^c3]: shao-2026 — "(τ −2) already tracks the onset pattern, indicating that representation drift emerges before the behavioral collapse."
