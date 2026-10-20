---
description: "LLMs asked a tabular question that requires inferring an unobserved value default to retrieval or aggregation; disclosing the task type recovers much of the gap."
aliases: ["implicit predictive TQA", "predictive intent disambiguation"]
sources: ["arxiv-2604-28076"]
---
# Implicit predictive intent

> A question can ask for a number the table does not contain, and the
> first failure is not arithmetic — it is reading the question as one
> that only asks for a number the table already has.

## Definition / Mechanism

Ji, Jiang, Zhan & Ye (2026)'s TopBench separates
two operations a tabular answerer conflates: retrieving or aggregating
facts already present in a table, and inferring an unobserved value for
a profile the table does not contain — "requiring the inference of
unobserved answers from historical patterns rather than mere retrieval.
These queries introduce two challenges: recognizing latent intent and
reliable predictive reasoning over massive tables."[^c1]

The question's surface form gives no marker distinguishing the two:
"search the charge for the 37-year-old male smoker" and "what can we
expect his bill to be" differ only in whether the described profile
exists among the rows, which the answerer must check before it can
know what kind of question it has been asked.

Across agentic workflows the dominant failure is a wrong read of the
task itself, not a wrong computation: "the model attempting to retrieve
data via code rather than performing the necessary predictive modeling.
This highlights a critical alignment failure where the model conflates
implicit predictive intent with simple information retrieval."[^c2]

The paper isolates intent misread as the bottleneck by an intervention: inject
the target column, task type and feature descriptions into the prompt,
holding the model and data fixed, and compare. Models that had defaulted
to lookup shift toward modeling and gain sharply — "the model likely
chooses the wrong task framing... a major failure mode is not coding
ability, but failure to recognize prediction as the required
operation."[^c3]

The same intervention shows the read is necessary but not sufficient:
when candidate profiles are intentionally close, disclosing the task
type "brings little benefit and sometimes hurts performance... recognizing
the intent is necessary but not sufficient; the remaining bottleneck is
prediction precision, feature engineering, and the tabular model."[^c4]
Comprehension and execution are separable failure stages, and the
benchmark's ablation is what separates them — without it, both
failures would show up as one low score.

## Why it matters

A benchmark question ordinarily carries an implicit type — retrieval,
aggregation, or inference over the unobserved — that the answerer must
recover before choosing a method, and the type is not signalled by any
lexical cue the answerer can pattern-match; it is a property of whether
the described case is in the data. An answerer that treats every
tabular question as retrieval-shaped is not making a modeling error, it
is misreading the question's partition of possible operations before
committing to one: "current LLMs face a strict barrier in bridging the
gap between intent recognition and predictive modeling... effective
intent disambiguation serves as the foundational step to activate
predictive modes and prevent models from defaulting to retrieval."[^c5]
This gives a template for isolating a comprehension failure from a
competence failure in any task where the surface question underdetermines
the operation required: hold the operation fixed by disclosure and see
whether performance recovers.

## Limits

- The benchmark pairs each query with the one historical table it
  requires; the intent-misread failure is measured under a setting that
  removes the further task of finding or constructing the right table,
  so the gap this note reports is a lower bound on intent-recognition
  difficulty in open-ended settings.
- The disclosure intervention (task type, target column, feature
  descriptions) is itself constructed by the benchmark authors from the
  ground-truth task; it demonstrates that intent is the bottleneck, not
  a mechanism by which an answerer could recover the intent unaided.
- The "necessary but not sufficient" result (Decision Making, close
  candidates) is from two models (Gemini 3 Flash, GPT-5.2) in the
  agentic setting; whether the same ceiling holds for other models or
  for Single-Point and Treatment Effect tasks is unverified.

## Related

Comprehension · [[false-premise-question]] ·
[[ambiguity-detection-localization-gap]] ·
[[recommender-premise-critique]] · [[interpretation-space]]

[^c1]: arxiv-2604-28076 — "requiring the inference of unobserved answers from historical patterns rather than mere retrieval. These queries introduce two challenges: recognizing latent intent and reliable predictive reasoning over massive tables."
[^c2]: arxiv-2604-28076 — "This degradation stems from the model attempting to retrieve data via code rather than performing the necessary predictive modeling. This highlights a critical alignment failure where the model conflates implicit predictive intent with simple information retrieval"
[^c3]: arxiv-2604-28076
[^c4]: arxiv-2604-28076 — "Candidate pairs are intentionally similar, so recognizing the intent is necessary but not sufficient; the remaining bottleneck is prediction precision, feature engineering, and the tabular model."
[^c5]: arxiv-2604-28076
