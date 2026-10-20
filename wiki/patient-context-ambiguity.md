---
description: "An ambiguity whose resolving fact exists only in the asker's own undisclosed state, so it cannot be closed by parametric or external knowledge — only by asking that asker."
aliases: ["patient-context ambiguity"]
sources: ["abbasian-2026"]
---
# Patient-context ambiguity

> A question can go to a corpus or to a person; some facts exist in neither
> the model's parameters nor any retrievable corpus, only in the asker.

## Definition / Mechanism

The source distinguishes patient-context [[efe-planning-as-variational-inference|ambiguity]] from the query-side
[[ambiguity-taxonomy|ambiguity types]] (linguistic, knowledge, intent): "patient-context ambiguity
occurs when the query is understandable and the relevant general medical
knowledge may already be available, but the appropriate response depends on
a patient-specific variable that has not been disclosed. This variable may
reside only with the patient and therefore cannot be recovered from the
language model's parameters or from an external corpus."[^c1]

The distinction rests on which of three knowledge sources a response needs:
"a language model draws on parametric knowledge encoded during pretraining,
instruction tuning, or domain adaptation. Second, it may draw on external
knowledge, including clinical guidelines, biomedical literature, drug
resources, and structured ontologies, through retrieval or
knowledge-graph grounding. Third, an appropriate response may require
patient-specific contextual knowledge, including current symptoms,
diagnoses, medications, allergies, pregnancy status, and dietary
restrictions." Only the third source forces the system to ask a question
of the one party who holds the fact, rather than to look it up.[^c2]

## Why it matters

For an asking system, the type determines the source stall's answer: a
knowledge-ambiguous query is closed by retrieval or grounding, but a
patient-context-ambiguous one is closed only by directing the question at
the specific asker — no better retrieval or more parameters substitutes.
[[knowledge-graph-guided-clarification]] is this source's own demonstration
that treating the distinction this way and eliciting the missing variable
changes downstream response accuracy substantially.

## Limits

- Defined and evidenced only in healthcare chatbot queries against two
  constructed benchmarks; whether the three-way split (parametric /
  external / patient-specific) partitions cleanly in non-medical domains is
  untested here.
- The boundary is not absolute: a "patient-specific" fact such as a
  recorded allergy could in principle be retrieved from a connected
  electronic health record; the source's own framing is that such records
  are often unavailable in a patient-facing chat, not that the fact is
  unknowable in principle.

## Related

[[ambiguity-taxonomy]] · [[knowledge-graph-guided-clarification]] · [[possible-worlds]]

[^c1]: abbasian-2026
[^c2]: abbasian-2026
