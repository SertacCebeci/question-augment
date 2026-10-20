---
description: "An answer can fail by asserting a wrong action or by leaving out a right one; in clinical LLM advice severe failures were mostly omissions, and trust can hide them."
aliases: ["errors of omission and commission", "omission versus commission", "commission-omission split", "harm of omission"]
sources: ["arxiv-2512-01241"]
---
# Omission and commission as two directions of error

An answer that recommends actions can fail in two directions. It can commit: recommend an action that should not be taken. It can omit: leave out an action that should have been taken. The NOHARM benchmark scores both against expert-rated clinical options and defines them as "both harm of omission (omitting an appropriate action) and commission (implementing an inappropriate action)."[^c1] Because each option is rated on its own, the split becomes two measurable quantities. Precision, the share of recommended actions that are correct, carries the commission side. Recall, the share of critical actions that are included, carries the omission side. The paper states the mapping directly: "Precision measures correctness of recommended actions (avoiding errors of commission), while recall measures adequate inclusion of critical actions (avoiding errors of omission)."[^c2]

The two directions do not weigh the same. Across the evaluated models, "Potentially severe errors ranged from 2.9% to 24.6% of cases for individual models."[^c3] Within those errors, "severe errors were dominated by omission (Extended Data Fig. 3a-b)."[^c4] The abstract puts the share at "errors of omission accounting for more than 80% of" severe errors.[^c5] The ranking metrics agree in direction: "recall was worse than precision (Fig. 3b)."[^c6] So, for these models, the failure that carries severe harm is more often a missing right action than a wrong one. This is a measured pattern on one benchmark, not a general law.

The silent answer gives the scale. The authors add a "do nothing" reference to every case, and it "had potential for severe harm in 37% of cases."[^c7] Every individual model in the 2.9% to 24.6% range sits below that reference, which is my arithmetic from the two figures. Declining to advise is therefore not a neutral baseline for this kind of task; it is itself a source of potential omission. This connects to [[abstention]], where silence is chosen deliberately and then priced.

The authors argue that trust is what hides the omission. "Generally accurate systems engender trust, and a trusted answer that is incomplete"[^c8] reads the same as a comprehensive one, the paper continues. The mechanism beyond that sentence is my inference. A commission leaves a sentence a reader can check against the case. An omission leaves no sentence at all, so a check on what was said cannot see it. An answer that is right in what it contains can therefore pass review while the missing action goes unnoticed.

Omission also enters on the receiver's side. In a "crossover study of 101 board-certified attending physicians", physicians given an AI chat tool did not simply inherit its advice. "AI-assisted physicians frequently omitted valuable AI-generated recommendations and still" scored below many AI systems alone.[^c9][^c10] Review of the transcripts found that "appropriate recommendations were surfaced by the AI but not included in the physician" response.[^c11] The counterfactual is that "had physicians incorporated every recommendation surfaced" by the assistant, they "would have outscored both their own" responses and the assistant as used.[^c12] That comparison is a simulation on the recorded outputs, not an observed arm. The two sites differ: an omission can be produced by the answerer, or by the receiver who drops advice that was given. A single count of omissions does not say which occurred.

## Limits

- The 80% figure is for one benchmark of 1,100 tasks built from primary-care-to-specialist electronic consults, scored by a panel of 29 physicians.[^c17][^c18] The authors warn that "Our findings may not generalize to" inpatient or straightforward visits.[^c13]
- The omission count depends on the grader. The paper reports that "the autograder was very strict in its" reading of omission, and that "actions that may be implied but not explicitly stated are often" scored as omissions.[^c14] The authors add that counting these as model errors "may be less appropriate than acknowledging the human error if clinicians were to blindly follow model-generated plans."[^c15]
- The authors offer a plausible account of why counseling and follow-up actions dominate the omissions, that clinicians and models "do not consider it part of their responsibility" to cover every attribute of consultative care.[^c16] This was not tested; it is the paper's conjecture.
- The silent-answer reference is hypothetical. Treating an empty plan as scored by the same rubric is an assumption of the design.
- Severity is a WHO-based tier attached to each rated action, so the severe share moves with that tiering. The study does not show how the ranking of models changes under a different weighting.
- Potential harm is what is measured. No patient outcome was observed, and nothing here shows that the omitted actions would have changed what happened to a patient.

## Related

- [[three-state-criterion-scoring]] — the same split used as a reward: an omitted criterion scores zero, an asserted error scores negative.
- [[recall-only-partial-credit]] — recall alone cannot register over-selection, so precision has to sit beside it; that is the commission half of this split.
- [[severity-weighted-omission-risk]] — the asymmetry priced for the asker: a question's value rises with the severe disease mass its set still leaves out.
- [[abstention]] — the "do nothing" reference is a silent answer, which abstention would choose on purpose.
- [[retrieval-utilization-gap]] — the receiver-side omission above is the human form of a surfaced-but-unused answer.

[^c1]: arxiv-2512-01241 — "both harm of omission (omitting an appropriate action) and commission (implementing an inappropriate action)"
[^c2]: arxiv-2512-01241 — "Precision measures correctness of recommended actions (avoiding errors of commission), while"
[^c3]: arxiv-2512-01241 — "Potentially severe errors ranged from 2.9% to 24.6% of cases for individual models"
[^c4]: arxiv-2512-01241 — "errors were dominated by omission (Extended Data Fig. 3a-b)"
[^c5]: arxiv-2512-01241 — "with errors of omission accounting for more than 80% of"
[^c6]: arxiv-2512-01241 — "recall was worse than precision (Fig. 3b)"
[^c7]: arxiv-2512-01241 — "which had potential for severe harm in 37% of cases"
[^c8]: arxiv-2512-01241 — "generally accurate systems engender trust, and a trusted answer that is incomplete"
[^c9]: arxiv-2512-01241 — "crossover study of 101 board-certified attending physicians"
[^c10]: arxiv-2512-01241 — "AI-assisted physicians frequently omitted valuable AI-generated recommendations and still"
[^c11]: arxiv-2512-01241 — "appropriate recommendations were surfaced by the AI but not included in the physician"
[^c12]: arxiv-2512-01241 — "they would have outscored both their own"
[^c13]: arxiv-2512-01241 — "Our findings may not generalize to"
[^c14]: arxiv-2512-01241 — "actions that may be implied but not explicitly stated are often"
[^c15]: arxiv-2512-01241 — "than acknowledging the human error if clinicians were to blindly follow model-generated plans"
[^c16]: arxiv-2512-01241 — "do not consider it part of their"
[^c17]: arxiv-2512-01241 — "of 1,100 items (100 clinical cases with 1,000 physician-perturbed variants)"
[^c18]: arxiv-2512-01241 — "by a panel of 29 board-certified physicians"
