---
description: "A tutoring architecture that routes each graded response to auto-correct, confirm, a follow-up question, or teacher escalation by the assessor's confidence, not correctness alone."
aliases: ["detect-verify-escalate pipeline", "detect-verify-escalate architecture"]
sources: ["imran-2026"]
---
# Detect-verify-escalate pipeline

> When an automated tutor is unsure whether a correct answer hides a
> misconception, it does not guess and it does not always call a human —
> it asks a targeted follow-up question and reserves escalation for the
> cases that stay suspicious.

## Definition / Mechanism

Imran & Bulathwela (2026) route every correct-answer response through a
graduated rubric (separating the answer mark from the method mark, after
standard mathematics assessment practice) into one of four actions: Red
(wrong answer, handled by answer-key lookup, no LLM), Green (clear
reasoning, confirmation), Amber-1 (needs clarification, follow-up
question), and Amber-2 (misconception detected, verification then teacher
escalation).[^c1]

Route assignment uses one LLM prompted with the question, the student's
answer, the explanation, and a mark scheme describing the expected
reasoning method.[^c2]

For Amber-1 cases — correct answer, explanation too brief to judge — the
same model generates a targeted diagnostic follow-up question using either
a variant-problem strategy (a near-transfer problem where the suspected
misconception would produce a wrong answer) or a probe-the-gap strategy
(asking about the specific step the student omitted), rather than
confirming the student or escalating to a teacher on insufficient
evidence.[^c3]

Two deployment modes read the same routes differently. A teacher-dashboard
mode filters a review queue, so a conservative (low-false-positive) model
suits it; an autonomous-tutor mode instead fires the follow-up question on
every flag, since asking a student to explain their reasoning is good
formative practice whether or not a misconception is present, so false
positives are pedagogically benign in that mode and false negatives — a
misconception left unchallenged — are treated as the expensive error.[^c4]

An ablation isolates what the mark scheme buys: removing it from the
prompt leaves misconception-detection unchanged but raises the TC
false-positive rate from 18.0% to 25.4%; the mark scheme is a precision
control on the routing decision, not a recall control.[^c5]

The proof of concept generates follow-up questions for 7 True-Misconception
instances from the test set; no student responses to these questions have
been collected, so the follow-up route itself is unvalidated in the
field.[^c6]

## Why it matters

This is a concrete instance of routing that is not "ask vs. don't ask" but
"which of four actions, keyed to the asker's own confidence in its
diagnosis rather than to the student's answer." It operationalizes a rule
this wiki states elsewhere only as a heuristic — ask only when uncertain,
escalate only when suspicious and still unresolved — as a fixed table
rather than a learned or computed criterion.

## Transfer

| | |
|---|---|
| **In its home field** | Formative-assessment theory (Black & Wiliam 1998): elicit evidence of learning, interpret it, respond appropriately; the answer-mark/method-mark distinction from summative marking schemes |
| **Here** | An automated tutor's action-selection step after grading: which of {auto-correct, confirm, ask, escalate} to take next |
| **What survives** | The three-step elicit/interpret/respond structure, and the principle that a low-confidence interpretation should trigger more evidence-gathering (the follow-up question) instead of a forced binary call |
| **What does not** | Any general, calibrated threshold for "confident enough to ask rather than escalate" — the four routes here are rubric categories assigned by one LLM's zero-shot prompt on one dataset, not a decision rule validated against ground truth or a second model family |

## Limits

- The routing categories are read off one LLM's output on 3,702 responses
  to 15 questions on one platform; not cross-validated against another
  dataset, subject, or model family.
- The "false positives are benign in autonomous mode" argument is a design
  stance the paper states, not a measured outcome — the follow-up-question
  route has not been tested with real students.
- The pipeline presupposes an answer key and a mark scheme already exist
  for every question; it does not cover open-ended tasks without a
  predefined expected reasoning method.

## Related

[[correct-answer-trap]] · [[value-of-information]] · [[semantic-entropy]]

[^c1]: imran-2026 — "Red (wrong answer, handled by answer-key lookup), Green (clear reasoning, confirmation), Amber-1 (needs clarification, follow-up question), and Amber-2 (misconception detected, verification then teacher escalation)."
[^c2]: imran-2026 — "The model receives the question, student answer, explanation, and a mark scheme describing the expected reasoning method."
[^c3]: imran-2026 — "the same model generates a targeted diagnostic follow-up question using either a variant-problem strategy"
[^c4]: imran-2026 — "false positives are pedagogically benign in this mode; false negatives (student leaves with misconception unchallenged) are the expensive error."
[^c5]: imran-2026 — "raises the TC false positive rate from 18.0% to 25.4%"
[^c6]: imran-2026 — "no student responses to these questions have been collected."
