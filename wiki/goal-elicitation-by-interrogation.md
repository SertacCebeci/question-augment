---
description: "A zero-label method that interrogates a code-defined AI pipeline before choosing evaluation metrics, converting each design ambiguity into a confirmed-fact constraint."
aliases: ["Litmus", "goal elicitation by interrogation"]
sources: ["gupta-2026-litmus"]
---
# Goal elicitation by interrogation

> Before asking *which metric?*, ask *what must be measured and why* — a
> code-grounded interrogation step that precedes metric selection rather
> than following it.

## Definition / Mechanism

Litmus first reconstructs a code-grounded component graph of an AI
pipeline from static analysis plus LLM synthesis (roles, capabilities,
failure surfaces), then maps each component to an evaluation-pattern
taxonomy that narrows which metric families are *plausible* without
selecting any. Because code exposes where measurement may be needed
without specifying what should count as success, failure, or acceptable
risk, Litmus converts each remaining metric-affecting [[efe-planning-as-variational-inference|ambiguity]] into an
explicit question — practitioner-facing or internal — whose answer is
recorded as a confirmed fact: a constraint that admits, rejects, or
re-scopes a candidate metric. "Litmus first identifies what must be
measured and why, then converts those answers into constraints for
constructing a justified, per-stage metric portfolio."[^c1]

Practitioner-facing questions are tied to a specific design decision:
"Practitioner-facing clarification questions target under-specified
decisions that affect metric design, such as which processing tier
carries production traffic or whether a fallback path is expected to
fire often or rarely." Each such question is emitted with an explicit
statement of the metric decision its answer would resolve, before any
metric is finalized.[^c2]

## Why it matters

Metric selection is treated as downstream of an unresolved inquiry
problem rather than a lookup. On three real code-defined pipelines
(account grouping, scientific QA, inherent-risk assessment), the
resulting zero-label portfolio out-ranked label-fitted and
rubric-generating baselines on validity against held-out quality labels:
"Despite using zero labels at design time, Litmus attains the strongest
label agreement on all three pipelines (ρ = 0.51, 0.72, 0.32), ahead of
every baseline including the label-fitted AutoMetrics."[^c3]

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | inquiry-based uncertainty resolution / clarification-question generation (Rao & Daumé III, 2018) | evaluation-metric design for AI pipelines |
| What survives | a question is asked only when its answer resolves a specific downstream decision | each question carries an explicit metric-impact statement naming the decision it settles |
| What does not | ranking candidate questions by expected value of the answer (EVPI) | Litmus does not compute or report an EVPI-style score for its questions; candidates come from the pipeline-taxonomy mapping, not a utility ranking |

The paper states the borrowing itself: "This is fundamentally an inquiry
problem — the same uncertainty-resolution view that underlies
clarification-question generation (Rao and Daumé III, 2018). We adopt
this view for AI-system evaluation."[^c4]

## Limits

The claim that interrogation changes what gets measured rests on
Litmus's own architecture reconstruction being accurate enough to pose
the right questions; the authors have not yet isolated whether the
*clarification channel itself* — as opposed to the code-grounded taxonomy
mapping — is what drives the validity gain: "the clarification-question
channel is a design affordance whose end-to-end benefit (practitioner
answers measurably changing the resulting metrics) is established here
at the specification level and warrants a dedicated human study."[^c5]
All three evaluation domains are scored by a single judge-model family,
so the ranking, not the absolute numbers, is the defensible claim.

## Related

[[expected-information-gain]] · [[value-of-information]] · [[defect-localization]] · [[sensitivity-weighted-question-score]]

[^c1]: gupta-2026-litmus — "Litmus first identifies what must be measured and why, then converts those answers into constraints for constructing a justified, per-stage metric portfolio."
[^c2]: gupta-2026-litmus — "Practitioner-facing clarification questions target under-specified decisions that affect metric design, such as which processing tier carries production traffic or whether a fallback path is expected to fire often or rarely."
[^c3]: gupta-2026-litmus
[^c4]: gupta-2026-litmus — "This is fundamentally an inquiry problem—the same uncertainty-resolution view that underlies clarification-question generation (Rao and Daumé III, 2018). We adopt this view for AI-system evaluation."
[^c5]: gupta-2026-litmus — "the clarification-question channel is a design affordance whose end-to-end benefit (practitioner answers measurably changing the resulting metrics) is established here at the specification level and warrants a dedicated human study."
