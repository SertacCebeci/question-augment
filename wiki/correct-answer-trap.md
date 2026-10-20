---
description: "Checking a student's answer for correctness alone under-detects misconceptions when a flawed method happens to produce a correct answer — measured at 43-16 points below reasoning-model detection."
aliases: ["correct answer trap", "CAT"]
sources: ["imran-2026"]
---
# Correct answer trap

> A named failure mode of automated assessment: when a student's flawed
> reasoning happens to produce the right answer, a system that grades on
> correctness alone confirms the misconception instead of catching it.

## Definition / Mechanism

Imran & Bulathwela (2026) term this the correct answer trap (CAT): the
under-detection of misconceptions when flawed reasoning produces a correct
answer.[^c1]

On 20,964 real responses to 15 diagnostic mathematics questions from the
Eedi platform (a held-out test set of 3,702 responses, 61 of them "True
Misconception" — correct MCQ answer, flawed written reasoning), a
fine-tuned BERT classifier detects only 57.4% [95% CI 44.5, 69.4] of these
hidden misconceptions, and standard ML interventions (class-weighted
sampling, data augmentation, focal loss, cross-encoder architecture, NLI
reformulation) all fall within that baseline's confidence interval —
despite near-perfect detection of ordinary wrong answers.[^c2]

A reasoning-capable open-weight model (Gemma 4, 26B, 3.8B active
parameters) raises detection to 83.6% [72.1, 91.4], but at the dataset's
1.6% prevalence, 84% detection combined with an 18% false-positive rate on
correctly-reasoning students yields only roughly 10.9% positive predictive
value — about eight false alarms per genuine catch.[^c3]

The failure concentrates by question design: two of the fifteen questions
account for 71% of hidden-misconception cases in the dataset, and both let
a flawed procedure coincide with a correct numeric output.[^c4]

## Why it matters

The trap is a selection-axis failure, not a modelling one: a system that
stops at the answer-correctness axis because the answer is correct never
opens the reasoning-validity axis at all. The paper's response is
architectural — [[detect-verify-escalate-pipeline]] — not a better
classifier on the same axis.

## Limits

- All figures come from 15 mathematics MCQ questions on one platform
  (Eedi), with the True-Misconception cases concentrated in 2 items;
  generalization to other subjects, open-response formats, or platforms is
  untested.
- The test set has only 61 True-Misconception examples; the reported
  interval on BERT's 57.4% ([44.5, 69.4]) spans 25 points.
- The 8-false-alarms-per-detection figure is specific to Gemma 4 26B's 18%
  false-positive rate at 1.6% prevalence; it does not transfer to another
  model or another classroom's misconception base rate without
  recomputation.

## Related

[[detect-verify-escalate-pipeline]] · [[semantic-entropy]] · [[value-of-information]]

[^c1]: imran-2026 — "the under-detection of misconceptions when flawed reasoning produces a correct answer"
[^c2]: imran-2026 — "BERT detects only 57% of correctanswer misconceptions despite near-perfect wrong-answer classification (FM recall 100%)."
[^c3]: imran-2026 — "at 1.6% prevalence, even 84% detection with 18% false positive rate yields only 10.9% positive predictive value (roughly 8 false alarms per genuine detection)."
[^c4]: imran-2026 — "The two questions that account for 71% of hidden misconceptions in our dataset both violate this principle: their structure allows flawed procedures to produce correct outputs."
