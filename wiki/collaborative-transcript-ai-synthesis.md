---
description: "An LLM given the raw transcript of an unaided stakeholder discussion synthesized the best-rated requirements artifact, beating a structured AI-collection platform and direct prompting."
aliases: ["transcript-synthesis condition"]
sources: ["neto-2026"]
---
# Collaborative-transcript AI synthesis

> When a distillation step turns many collected constraints into one
> artifact, what it is handed matters more than what collected them: giving
> the synthesizer the raw discussion outscored giving it a structured tool's
> output.

## Definition / Mechanism

A between-subjects controlled experiment compared four ways to produce one
requirements artifact from the same problem scenario: (A) stakeholders
collaborate and write the document by hand, no AI; (B) stakeholders
collaborate through a structured platform whose built-in applet synthesizes
the final artifact; (C) an LLM generates the artifact directly from the
problem description, no stakeholder input; (D) an LLM synthesizes the
artifact from the raw transcript of Condition A's unaided discussion. Two
independent RE specialists scored each artifact on ISO/IEC/IEEE 29148
dimensions (completeness, clarity, consistency, absence of [[efe-planning-as-variational-inference|ambiguity]],
detail, traceability, overall quality). Condition D scored highest or
joint-highest on every dimension. "We provided the discussion transcript
produced during Condition A to a Large Language Model, which generated a
requirements artifact based on the information contained in the
collaborative discussion." "This artifact achieved the highest score for
completeness (5.0) and detail (3.5), while also obtaining the highest or
joint-highest scores for clarity, consistency, traceability, and overall
quality."[^c1]

The authors read this as a role effect, not an AI-versus-human effect:
"the results also suggest that the quality of generated artifacts depends
on the role assigned to AI within the process. While direct prompting
produced a positively evaluated artifact, the highest-rated artifacts were
obtained when AI synthesized information generated through stakeholder
collaboration."[^c2]

The unaided manual condition anchored the bottom: "Condition A,
corresponding to the collaborative process without AI support, received the
lowest ratings across all evaluated quality dimensions."[^c3]

## Why it matters

This is a direct manipulation of what a synthesis/distillation step
receives as input. Structured collection (Condition B) truncates the
discussion into the platform's categories before synthesis; the raw
transcript (Condition D) does not. The higher scores for D over B suggest
the truncation itself, not just the presence of AI, cost quality — an
answer to "what should feed the distiller" that a purely formal treatment
of distillation does not supply.

## Limits

- Exploratory pilot: six participants in two collaboration groups, one
  scenario (a room-reservation system), two evaluators, no inferential
  statistics — the numbers are directional, not a generalizable effect
  size.
- Confounded by design: Conditions B and D differ in both the collaboration
  medium (platform vs. free discussion) and the synthesis mechanism
  (built-in applet vs. general LLM), so the transcript-richness effect is
  not isolated from those other differences; the paper's own Threats to
  Validity section names this.
- One synthesizing model, one prompt formulation, unreported — the effect
  of transcript access on synthesis quality is not shown to generalize
  across models or prompts.

## Related

[[distillation-input-debt]] · [[sufficient-statistic]] · [[constraint-as-information]]

[^c1]: neto-2026 — "We provided the discussion transcript produced during Condition A to a Large Language Model, which generated a requirements artifact based on the information contained in the collaborative discussion."
[^c2]: neto-2026 — "the results also suggest that the quality of generated artifacts depends on the role assigned to AI within the process. While direct prompting produced a positively evaluated artifact, the highest-rated artifacts were obtained when AI synthesized information generated through stakeholder collaboration."
[^c3]: neto-2026 — "Condition A, corresponding to the collaborative process without AI support, received the lowest ratings across all evaluated quality dimensions."
