---
description: "A triage dialogue benchmark grounding each disclosed patient fact to its source EHR event and first turn, linking question order to information gain."
aliases: ["EHR2Dial-Triage"]
sources: ["zhu-2026-elicited"]
---
# EHR2Dial-Triage — EHR-grounded triage dialogue benchmark

## Definition / Mechanism

Zhu et al. (2026) build triage conversations between a
clinician-role LLM and a patient-role LLM from MIMIC-IV-ED encounters, under
an explicit information partition: clinician-visible facts $C_i$ available
at dialogue onset, and patient-reportable facts $P_i$ that the clinician
must elicit through questions. A verifier checks each patient utterance
against the source record: "A fluent generated response is not necessarily
supported by the source record. A verifier therefore maps accepted clinical
disclosures to normalized atomic facts and links each fact to its eligible
source in Ci or Pi." Every accepted disclosure keeps its round index and
speaker role, so "a completed episode therefore yields a machine-readable
ledger that traces each accepted disclosure back to its exact source event
in the EHR and identifies when and by whom it first entered the dialogue."[^c1]

This event–turn lineage is what makes the questioning policy measurable: a
fact only counts once, at the round it is first disclosed, so the benchmark
can attribute an information increment to the question that produced it
rather than to the conversation as a whole.

## Why it matters

A fixed, patient-disjoint logistic-regression reader applied to the
cumulative disclosed facts at each round shows the elicited information is
predictive of the actual triage outcome, not just topically relevant: "By
Round 10, the dialogues cover 66% of all eligible patient-reportable facts
and 86% of facts designated as triage-important... Mean predictive [[entropy]]
decreases from 1.61 nats initially to approximately 1.04 nats at Round 10,
while top-1 ESI accuracy reaches 59%, compared with a 42% majority-class
baseline."[^c2]

Comparing clinician LLMs on the same event-turn ledger shows their axis
selection converges early: "Models behave similarly during the early part
of the interaction. At Round 2, FactCov ranges only from 18.9% to 19.8%,
and coverage remains tightly clustered at Round 6 52.7%–53.9%. This suggests
that most models identify a similar set of high-priority questions early in
the interview, when common symptom, history, and medication information is
still readily available."[^c3]

For stall 2 (which axis first), this is a rare case where "which question
was asked, and what did it actually add" is auditable per turn rather than
inferred: the ledger, not a self-report, decides whether a model's question
order tracks the axes that most reduce outcome uncertainty.

## Transfer

| | |
|---|---|
| **In its home field** | ED triage / clinical-dialogue benchmarking: patient facts are grounded in a structured EHR to constrain and audit a generated conversation |
| **Here** | a general device for scoring a multi-turn asking policy: link each answer to the source fact it came from and the turn it first appeared, then measure a fixed downstream predictor's uncertainty over that ledger, round by round |
| **What survives** | the provenance link (disclosure → source event → first turn) as a way to isolate one question's marginal contribution to outcome-relevant uncertainty, independent of the conversation's fluency |
| **What does not** | the EHR-specific structure — a normalized fact taxonomy, the $C_i$/$P_i$ role split, and the five-level ESI target — none of which exist outside a clinical record |

## Limits

- This note rests on the benchmark's own internal-validity claim, not on
  clinical validation: the paper states directly that these analyses
  "evaluate the internal design of the benchmark; they do not establish
  clinical validity or readiness for deployment."[^c4]
- The patient side is an LLM simulator, not a real patient, and the reader
  that produces the entropy/accuracy numbers is a fixed logistic-regression
  proxy for triage relevance, not the actual ESI-assignment process — so
  the reported information gain measures agreement with a proxy classifier,
  not with a clinician's own use of the same evidence.
- Single corpus (MIMIC-IV-ED, 4,041 encounters), single fixed ten-round
  budget and stopping rule across all compared models, so the axis-order
  convergence result may reflect that shared budget rather than a
  model-independent property of triage.

## Related

[[mediq]] · [[under-triage]] · [[expected-information-gain]] · [[value-of-information]]

[^c1]: zhu-2026-elicited
[^c2]: zhu-2026-elicited
[^c3]: zhu-2026-elicited — "Models behave similarly during the early part of the interaction. At Round 2, FactCov ranges only from 18.9% to 19.8%, and coverage remains tightly clustered at Round 6 52.7%–53.9%. This suggests that most models identify a similar set of high-priority questions early in the interview, when common symptom, history, and medication information is still readily available."
[^c4]: zhu-2026-elicited — "These analyses evaluate the internal design of the benchmark; they do not establish clinical validity or readiness for deployment."
