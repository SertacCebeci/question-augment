---
description: "An OSCE-inspired clinical benchmark that gates every evidence item behind a model-issued request, so question selection is scored apart from diagnosis."
aliases: ["ROUNDS-Bench", "Standardized Patient Simulator", "Information Gating Mechanism"]
sources: ["zhan-2026"]
---
# ROUNDS-Bench

> A dual-task clinical benchmark that withholds the whole case and releases
> each piece only in answer to a model's request, so a model's diagnosis can
> be scored separately from its evidence-gathering.

## Definition / Mechanism

Zhan, Qiu, Tan et al. (2026) build a Standardized Patient
Simulator (SP-sim) around an "Information Gating Mechanism: initiating with
only basic demographics and a chief complaint, models must unlock subsequent
evidence, such as symptom details, physical exam findings, and lab results,
through clinically logical History Taking and Test Requesting."[^c1]

The benchmark runs the same 468 cases (six clinical systems, equally
stratified, drawn from MedQA, MedMCQA, MedFound and MedCaseReasoning) through
two paired tasks: "Task 1 (Full-Context): Models receive the complete
electronic health record instantaneously, establishing the theoretical
upper bound of static diagnostic proficiency," against "Task 2 (Active
Evidence-Seeking): Models are provided only with the Chief Complaint and
must autonomously drive a multi-turn diagnostic dialogue to progressively
acquire evidence." Grading is dual: Strict diagnostic accuracy and Strict
Evidence Quality (StrictEQ) — whether the model's cited evidence is a
"complete, traceable chain," both positive and negative findings — are
scored independently per case, plus a joint Fully Supported Accuracy (FSA)
requiring both scores maximal.[^c2]

Unlike an open-ended chat evaluation, the request–response protocol "resembles
common query workflows (e.g., electronic health record retrieval), enabling
measurement of questioning efficiency and diagnostic performance across
turns during both the information acquisition and reasoning phases
separately."[^c3]

## Why it matters

For stall 2, ROUNDS-Bench is a way to isolate *which* evidence a model
chooses to request from *how well* it reasons once it has it — the paired
Task 1/Task 2 design and the accuracy/StrictEQ split let a claim about
selection strategy be measured without evidence synthesis quality
confounding it, which open-ended dialogue benchmarks (informally scored,
free-text) cannot separate as cleanly.

## Transfer

| | |
|---|---|
| In its home field | OSCE (Objective Structured Clinical Examination): a human trainee is scored on live, staged interaction with a standardized patient across dimensions including history collection and communication skill |
| Here | an LLM interacts with a simulated patient whose disclosures are gated behind a request, scored by an automated judge on two axes (diagnosis, evidence) instead of a human examiner's rubric |
| What survives | progressive disclosure — information is withheld until specifically and appropriately requested, so the examinee's request strategy is itself part of what is graded |
| What does not | the human examiner's holistic judgment of communication and process; ROUNDS-Bench substitutes an automated multi-dimensional grader whose own [[calibration|reliability]] is not validated against physician graders in this paper |

## Limits

- The grader (diagnostic accuracy, StrictEQ, FSA) is automated; the paper
  does not report inter-rater agreement between this grader and physician
  judges, unlike some other interactive clinical benchmarks (e.g. MediQ's
  Patient-system factuality check).
- The Patient Simulator's own fidelity — whether it discloses information
  the way a real patient or chart would under the same request — is not
  independently validated in the slice read.
- Single time window (2026), 15 models; whether the 468-case stratified
  cohort generalizes beyond the four source corpora used to build it is not
  established here.

## Related

[[mediq]] · [[premature-closure]] · [[value-of-information]] · Selection

[^c1]: zhan-2026 — "initiating with only basic demographics and a chief complaint, models must unlock subsequent evidence, such as symptom details, physical exam findings, and lab results, through clinically logical History Taking and Test Requesting"
[^c2]: zhan-2026 — "Task 1 (Full-Context): Models receive the complete electronic health record instantaneously, establishing the theoretical upper bound of static diagnostic proficiency."
[^c3]: zhan-2026 — "this request–response protocol improves controllability and reproducibility. It resembles common query workflows (e.g., electronic health record retrieval), enabling measurement of questioning efficiency and diagnostic performance across turns during both the information acquisition and reasoning phases separately"
