---
description: "A clinician's inquiry is scored by the share of case-essential facts a must-ask list says it should elicit, so an omitted question is counted as a lost fact rather than a lost diagnosis."
aliases: ["Inquiry Sufficiency", "IS score", "must-ask coverage", "information-elicitation coverage"]
sources: ["arxiv-2512-10206"]
---
# Inquiry sufficiency

Before the dialogue, a list of the items a clinician must ask is drawn from the case: "List all the core and most important information a doctor must ask the patient before making a correct diagnosis (e.g., past medical history, family history)."[^c1] The score is then the share of that list that the dialogue actually reached. "identify which of the core information you mentioned has actually been asked by the doctor."[^c2] Items are matched by exact terminology, and "Only consider information that is a direct match to your core list."[^c3]

The mechanism that makes this a measure of asking is the answerer's policy. The simulated patient is told: "You only need to answer the questions the doctor asks you. If a question is not asked, you do not need to provide any information."[^c4] The patient holds medical history and examination findings but not the laboratory results or the final diagnosis, "thereby reflecting the information asymmetry typical of real-world patient encounters."[^c5] Since the patient volunteers nothing, a fact missing from the record is a fact the asker did not request. The score therefore reads the question set directly: a clinician who never asks about family history loses that item whatever the diagnosis turns out to be.

In the reported run the score ranks the models, with a clear head. "GPT-5 and GPT-OSS-120B extract the most comprehensive patient information through inquiries", while "other models clustered within a narrower performance range behind."[^c6] Whether this axis is a proxy for accuracy is not settled by the paper's text I read; the reported ranking is a per-model number, and I did not see it set against diagnostic accuracy within models. My inference is that the point for asking is that coverage is a property of the question set before any answer is judged.

The construction also has a dependency that a reader should keep in view. The must-ask list is written from the case together with "its confirmed final diagnosis."[^c7] The list is therefore anchored on the answer. An asker who cannot see the diagnosis is scored against items chosen with it in hand, which is a hindsight standard. My reading is that this is what separates inquiry sufficiency from a clinical guideline: it measures coverage of what the known answer needed, not of what a clinician would need to ask without knowing it.

## Limits

- The score is not only a count of questions. The paper's definition covers whether physicians "identify, elicit, and document essential diagnostic information."[^c8] The numerator is taken from the clinical records, so a fact asked but not written down is lost, and a fact written without being asked is not counted as asked. The paper does not split these two failures.
- The list is produced by a language model, and the matching is done by one. In the slices of the text I read, I did not find a comparison of the list or the matches against clinician judgment, so the score's validity rests on the design rather than on a measured agreement. This is my reading of what is missing, not a result the paper reports as absent.
- The patient is an LLM (GPT-OSS-120B is "the patient agent backbone"), and the cases are simulated.[^c9] A coverage score measured against an LLM patient inherits that patient's disclosure policy; the wiki's note on [[progressive-disclosure-fidelity]] states the audit that such a score needs.
- The score says nothing about whether the asked items changed the plan. A full list can be covered and the diagnosis still wrong. The paper scores this as one axis among others; it reports logical coherence (LC) separately, and I read the separation as the authors' design rather than as evidence that the two are independent.
- The number of questions per turn is capped ("You may ask up to" a set number, over a set number of rounds), so the score is conditional on that budget and does not transfer to an open-ended interview without a re-run.[^c10]

## Related

- [[rounds-bench]] — gates each evidence item behind a request, so question selection is scored apart from diagnosis; the same separation by a different gate
- [[progressive-disclosure-fidelity]] — the answerer audit that a coverage score against a simulated patient depends on
- [[closed-loop-standardized-patient-evaluation]] — a whole-encounter scoring of timed rubric items, where an omission in the middle of the dialogue is the failure
- [[dependency-aware-checklist-scoring]] — a checklist credited by flat count versus by prerequisites; the same question of what a flat coverage total hides
- [[gated-socratic-scaffolding]] — the training-side use of a patient agent for history taking

[^c1]: arxiv-2512-10206 — "List all the core and most important information a doctor must ask the patient before making a correct diagnosis"
[^c2]: arxiv-2512-10206 — "identify which of the core information you mentioned has actually been asked by the doctor"
[^c3]: arxiv-2512-10206 — "Only consider information that is a direct match to your core list"
[^c4]: arxiv-2512-10206 — "You only need to answer the questions the doctor asks you. If a question is not asked, you do not need to provide any information."
[^c5]: arxiv-2512-10206 — "thereby reflecting the information asymmetry typical of real-world patient encounters"
[^c6]: arxiv-2512-10206 — "GPT-5 and GPT-OSS-120B extract the most comprehensive patient information through inquiries"
[^c7]: arxiv-2512-10206 — "and its confirmed final diagnosis"
[^c8]: arxiv-2512-10206 — "identify, elicit, and document essential diagnostic information during patient encounters"
[^c9]: arxiv-2512-10206 — "we selected GPT-OSS-120B as the patient agent backbone"
[^c10]: arxiv-2512-10206 — "You may ask up to"
