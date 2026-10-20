---
description: "A 300-session study of three frontier models shows none asks within its own empirically optimal clarification window; strategies range from over-asking in 52% of sessions to never asking."
aliases: ["ask timing misalignment"]
sources: ["gulati-2026"]
---
# Natural ask timing misalignment

> Even where a forced-injection study can locate the trajectory window in which a clarifying question is worth most, letting a model decide for itself when to ask does not land it in that window: the gap between the measured optimum and a model's own asking behaviour is large and model-specific.

## Definition / Mechanism
Gulati et al. (2026) ran a complementary 300-session study on TheAgentCompany with three models (Claude Sonnet 4.5, GPT-5.2, Gemini 3 Flash) given a working `ask_user` tool, and overlaid each model's natural first-ask timing on the forced-injection VOI curves from the same paper. Their headline finding: "no current frontier model asks within the empirically optimal window for any dimension, with strategies ranging from over-asking (52% of sessions) to never asking at all."[^c1]

Per model: "GPT-5.2 asks in 52% of sessions with a mean first-ask timing of 43% through the trajectory. Claude Sonnet 4.5 asks in 23% of sessions at a mean timing of 50%. Gemini 3 Flash never asks (0% ask rate across all 100 sessions)." Against the optimal windows measured in [[clarification-timing-decay]] (goal ≤10%, input through ~50%): "GPT-5.2's asking at 43% is past the goal optimum (10%) but within the input window; Claude's 50% is suboptimal for goal but reasonable for input; Gemini forgoes all benefit."[^c2]

The authors note, as an unconfirmed hypothesis rather than a controlled finding, that timing alignment alone does not predict task success: "Claude achieves higher per-session success (11%) than GPT-5.2 (3%) despite asking later and less often ... suggesting that question quality may matter more than frequency, though this between-model comparison cannot isolate question quality from other model-level differences."[^c3]

## Why it matters
It separates two failures a stall-2 selection policy can have independently: picking the wrong axis, and picking the right axis at the wrong time. A model that reliably identifies the missing goal information but asks about it at 43% of the trajectory has already lost most of the goal dimension's value even though its question was well-formed — the misalignment is a timing defect, not a selection defect, and the two need different fixes.

## Limits
The finding rests on one benchmark (TheAgentCompany, 300 sessions, 3 models) and is compared against a different experimental protocol: "A behavioral confound exists between protocols: forced injection disables ask_user while natural-ask enables it, so agents may plan differently when they know they cannot ask." The "optimal window" it is measured against is itself an upper bound (see [[clarification-timing-decay]] Limits), so the true misalignment could be smaller than reported. The question-quality-over-frequency claim is explicitly flagged by the authors as a hypothesis, not a controlled result, and is reported here as such rather than as an established finding. The source is a 2026 arXiv preprint, not yet peer reviewed.[^c4]

## Related
[[clarification-timing-decay]] · [[value-of-information]] · [[clarification-benchmarks]] · [[reversibility]]

[^c1]: gulati-2026
[^c2]: gulati-2026 — "GPT-5.2 asks in 52% of sessions with a mean first-ask timing of 43% through the trajectory. Claude Sonnet 4.5 asks in 23% of sessions at a mean timing of 50%. Gemini 3 Flash never asks (0% ask rate across all 100 sessions)."
[^c3]: gulati-2026
[^c4]: gulati-2026
