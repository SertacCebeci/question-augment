---
description: "A tutor agent's need-triggered, diagnosis-withholding Socratic prompts raised OSCE communication and empathy scores over a non-LLM control in a 100-student RCT, without improving diagnostic accuracy."
aliases: []
sources: ["yang-2026"]
---
# Gated Socratic scaffolding

> A tutor agent that only speaks when a separate evaluator agent flags a
> specific failure, and even then never states the diagnosis, measurably
> improved trainees' later, unassisted interview performance — mostly in
> how they communicated, not in what they concluded.

## Definition / Mechanism

Yang et al. (2026) test a three-agent design for clinical-interview
training: a patient agent answers the student's questions from a scripted
case; a turn-level evaluator agent watches each student turn and decides
whether it needs help; and a tutor agent speaks only when the evaluator
says so. The system includes a patient agent for simulated dialog, a tutor
agent providing [[staged-socratic-hint-policy|Socratic]] prompts for history taking, clinical reasoning,
and empathic communication without disclosing diagnostic information, and
a turn-level evaluator agent that monitors clinical progress without
revealing summative scores.[^c1]

The evaluator's triggers are named categories, not left to judgement, and
even a triggered tutor may not resolve the case for the student: tutor
prompts were triggered only when the turn evaluator identified a
meaningful need for intervention, such as missing key information,
conversational impasse, [[premature-closure|premature closure]], communication breakdown, or
professionalism concerns, and the tutor was instructed not to directly
reveal the final diagnosis, key differential diagnoses, or case answers.
What it may say instead is reflective questions or brief hints — whether
the current information suffices for a conclusion, a reminder to address
the patient's expressed distress, a suggestion to summarize.[^c2]

The trial: 100 third-year medical students randomized 1:1; 95 (47
multi-agent, 48 control) completed the workflow and entered the primary
analysis. The control was a non-LLM, computer-based progressive-disclosure
activity built from the same authored case materials, with tutor
scaffolding, process monitoring and feedback removed. The examination mode
was identical for both groups: a patient-only AI standardized patient,
teaching and process-monitoring agents removed, no Socratic prompts or
real-time feedback, scored afterwards in the background by the final
evaluator.[^c7]

On that exam, students trained under the gated, non-disclosing tutor
scored higher: the mean final examination score was 71.8% in the
multi-agent group and 55.6% in the control group; a Mann-Whitney U test
showed a statistically significant between-group difference
(P = 5.51 × 10−5), with a large standardized effect size favoring the
multi-agent group (Hedges' g = −0.81; Table S3 reports −0.814), and
assignment to the multi-agent group was associated with a
16.4-percentage-point higher final examination score in a linear model
(β = 16.4; 95% CI, 7.7 to 25.1; P = 3.30 × 10−4).[^c3]

The gain concentrated in the communication domain and, at item level, in
observable empathic expression: the mean communication score was higher
in the multi-agent group (3.53 vs. 2.64, P = 4.14 × 10−4, g = −0.79), and
the largest single checklist gain was expressing empathy, 31 percentage
points higher, significant after Holm correction (P = 8.30 × 10−4).[^c4]
Diagnostic accuracy did not differ (86% control vs. 84% multi-agent,
P = 1.000); the authors call this null expected, since both arms saw the
same authored cases and the same core diagnostic content, and say it
should not be read as a failure of the intervention.[^c5]

## Why it matters

This is a controlled, measured contrast — not a case study — between an
asking-support agent restricted to *process* constraints (has the student
covered X, has the student addressed the patient's distress) and a
matched-content condition with no such agent. It separates two things this
wiki's selection and source criteria usually bundle: *whether* to
intervene at all (gated on a named trigger, not every turn) and *what* an
intervention may contain (never the answer itself).

It sits next to [[non-advisory-dialogue]] but is not the same policy:
that asker may emit only respondent-grounded reflective questions; this
tutor may also give brief hints and directive reminders, as long as the
diagnosis, differentials and case answers stay withheld.

## Transfer

| | |
|---|---|
| **Home field** | Developmental psychology's zone of proximal development: a learner can do with timely, structured assistance what they cannot yet do alone; yang-2026 name scaffolding theory and ZPD as the design's theoretical basis. |
| **Here** | The tutor's prompts assist the *process* of history-taking, reasoning and rapport-building without ever supplying the diagnostic content itself. |
| **What survives** | Assisting process while withholding content moved a measured outcome by itself — the effect does not depend on the tutor ever being right about the diagnosis. |
| **What does not** | ZPD's core mechanism — assistance *faded* as a specific learner's competence grows — is untested: each participant completed two learning sessions under the same fixed-rule tutor, and faded scaffolding is named as future work, not a result. |

[^c6.1][^c6.2][^c6]

## Limits

- The comparator is a structured non-LLM control — a computer-based
  progressive-disclosure activity — not a human tutor or human
  standardized patient. The result says gated Socratic scaffolding beats
  no scaffolding under matched content; it says nothing about whether it
  beats, matches, or falls short of a human tutor's feedback.[^c8]
- One institution (Guangzhou Medical University), one narrow domain (three
  acute-abdominal cases), one third-year cohort (n = 95 analyzed); the
  authors say the findings generalize with caution to other specialties.
  The trigger vocabulary and effect sizes are conditioned on this domain
  and population.[^c9]
- The ZPD framing in `## Transfer` is yang-2026's secondhand citation of
  the developmental-psychology literature, not read by this wiki; it is
  reported as the paper's stated rationale, not an independently verified
  claim.
- The headline statistics in[^c3] (P = 5.51 × 10−5, Hedges' g = −0.81,
  β = 16.4) sit where the text extract line-wraps "between-" / "group"
  and "group" / "(Hedges' g"; an earlier locator pass failed on quotes that
  straddled the wrap. The evidence is therefore quoted as single-line
  spans — the 71.8% vs. 55.6% means, the P value line, the β line — plus
  Table S3's final_score row; if a locator still cannot resolve them, the
  figures stand unverified pending a reviewer's manual confirmation
  against §2.2 and Table S3.
- No delayed follow-up: whether the communication gain is sustained over
  time or transfers to higher-stakes clinical settings is unmeasured — the
  authors name delayed transfer assessment as future work.[^c10]

## Related

[[socratic-method]] · [[non-advisory-dialogue]] · [[information-gathering-interview-style]] · [[five-whys]]

[^c1]: yang-2026 — "The system includes a patient agent for simulated dialog, a tutor agent providing Socratic prompts for history taking, clinical reasoning, and empathic communication without disclosing diagnostic information, and a turn-level evaluator agent that monitors clinical progress without revealing summative scores."
[^c2]: yang-2026 — "Tutor prompts were triggered only when the turn evaluator identified a meaningful need for intervention, such as missing key information, conversational impasse, premature closure, communication breakdown, or professionalism concerns."
[^c3]: yang-2026 — "examination score was 71.8% in the multi-agent group and 55.6% in the control group"
[^c4]: yang-2026 — "the mean communication score was higher in the multi-agent group than in the control group (3.53 vs. 2.64). This difference was statistically significant (P = 4.14 × 10−4 ) and corresponded to a large effect size (g = −0.79)"
[^c5]: yang-2026 — "Correct initial diagnoses were made in 86% of control cases and 84% of multi-agent cases (P = 1.000)"
[^c6.1]: yang-2026 — "Scaffolding theory and the zone of proximal development (ZPD) provide the theoretical basis for this design."
[^c6.2]: yang-2026 — "After login and onboarding, each participant completed two learning sessions under the assigned condition."
[^c7]: yang-2026 — "A total of 100 students were enrolled and randomly assigned to either the multi-agent AI standardized patient"
[^c8]: yang-2026 — "The CT condition was a structured non-LLM control rather than a human standardized-patient or AI-dialogue comparator."
[^c9]: yang-2026 — "Participants were third-year undergraduate students majoring in clinical medicine at Guangzhou Medical"
[^c10]: yang-2026 — "Fifth, the study did not include delayed follow-up. Consequently, it remains"
[^c6]: yang-2026
