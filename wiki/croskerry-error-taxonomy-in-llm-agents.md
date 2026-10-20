---
description: "A clinical dual-process taxonomy of diagnostic errors, moved unmodified as an annotation scheme onto LLM agent reasoning traces, minus the severity grading it needs a real patient to justify."
aliases: ["Croskerry taxonomy", "dual-process diagnostic error taxonomy", "cognitive-bias vs process-error taxonomy"]
sources: ["braitsch-2026"]
---
# Croskerry error taxonomy applied to LLM agents

> A classification of *how* a diagnostician goes wrong, built for human
> clinicians, used here to annotate an LLM's reasoning trace instead.

## Definition / Mechanism

Braitsch et al. annotate LLM reasoning traces with "a taxonomy adapted from
Croskerry's dual-process model of clinical reasoning. The taxonomy
distinguished cognitive biases from process errors."[^c1]

The cognitive-bias class comprises [[diagnostic-anchoring-in-agentic-llms|anchoring bias]] (fixating on an initial
impression despite contradictory information), confirmation bias, premature
closure (accepting a diagnosis before adequate verification), availability
bias, and search satisficing (terminating the diagnostic search after
finding one plausible explanation); the process-error class comprises
hallucinated information, logical contradiction, and over-differentiating.
Each annotated error also carries a four-level severity grade
(low/medium/high/critical).[^c2]

Applied to 1,008 model-case-round reasoning traces from 17 models: "Errors
were identified in 89 of 1,008 evaluations (8.8%), yielding 93 individual
error annotations." "Process errors were more frequent than cognitive
biases. The most common error types were search satisficing, premature
closure, and anchoring bias." Severity skewed low: "The majority of errors
were of medium severity (56/93, 60.2%) … No critical errors with the
potential to cause direct patient harm were identified."[^c3]

## Why it matters

This is a formalism import, not just a metaphor: the same named biases that
gate a novice clinician's search recur as the dominant annotated errors in
LLM agentic reasoning traces, which is the source's own argument that the
deficit is structural to sequential reasoning under uncertainty, not a
knowledge gap. [[bounded-rationality]]'s satisficing is the closest existing
formal analogue in this wiki, though defined differently — an aspiration-
level rule on option value, not "stop after one plausible diagnostic story."

## Transfer

| | Home field (clinical cognition) | Here (LLM agent evaluation) |
|---|---|---|
| Instrument | Croskerry's bias/process-error distinction, applied by a trained rater to a clinician's stated reasoning | The same category list, applied by an LLM-as-judge rater to a model's reasoning trace |
| What survives | The category definitions transfer unchanged — anchoring, satisficing, premature closure etc. keep the same operational wording | — |
| What does not | Severity is graded by potential harm to a real patient | No patient exists in the benchmark; the paper's zero-critical-errors result is a structural artifact of this, not a safety finding |

## Limits

- Croskerry's own taxonomy is known to this wiki only through Braitsch et
  al.'s description of it (their reference 21); the wiki has not read or
  independently sourced Croskerry's original publication, so the taxonomy's
  definitions are cited as reported here, not verified at origin — `[?]`
  pending its own source.
- Error identification is itself LLM-judged (Claude Opus 4.6), spot-checked
  by one human author on only 50 of 1,008 entries; full-set inter-rater
  agreement with a clinician is not reported.
- The taxonomy names five cognitive biases as one class; this note reports
  the class and its aggregate counts, not each bias's individual rate, which
  the source does not break out per type.

## Related

[[diagnostic-anchoring-in-agentic-llms]] · [[information-utilization-rate]] · [[bounded-rationality]]

[^c1]: braitsch-2026
[^c2]: braitsch-2026
[^c3]: braitsch-2026 — "Errors were identified in 89 of 1,008 evaluations (8.8%), yielding 93 individual error annotations across the 17 models with full thinking traces"
