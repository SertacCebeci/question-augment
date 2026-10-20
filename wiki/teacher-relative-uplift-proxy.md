---
description: "Without labels, a learning harness's gain measured against a stronger teacher's pseudo-labels tracks its gain against gold labels, provided a real capability gap exists between teacher and student."
aliases: ["teacher-relative lift", "label-free harness evaluation", "scaling-hypothesis teacher-student evaluation"]
sources: ["doi-10-48550-arxiv-2608-13608"]
---
# Teacher-relative uplift proxy

A learning harness (an LLM plus retrieval or memory that improves from corrections without retraining) is hard to evaluate when labels are scarce, stale and biased toward hard cases. The proposed substitute is a teacher-student design: score the harness by how much its student converges toward a stronger teacher.[^c1]

## Mechanism

Three models per task: a teacher (stronger, no harness), a student (weaker, no harness) and student* (the student with the harness). The teacher labels every item; those predictions are pseudo-labels. Data is split into five parts: four rounds of continual learning and one held-out test split. In each round up to five "high-impact" misclassifications are fed back as corrections, so student* sees no more than 20 corrections out of hundreds of items.[^c2]

Uplift is computed twice on identical models and items, differing only in reference labels: ΔG against gold and ΔT against teacher labels. Gold is used only at the end, to validate.[^c3]

**Finding a pair without labels.** By the scaling hypothesis, a larger and a smaller model from one family disagree on many unlabeled items; where they disagree, the larger is more often correct, so it is designated teacher.[^c4] The authors checked this: in every family the larger model beat the smaller one on all three tasks.[^c5]

**Result.** Across three tasks (email classification, CVE-to-CWE mapping, ATT&CK tactic), three model families and three harnesses (Memory, Lesson, Few-shot), ΔT correlated strongly with ΔG, and usually had the same sign.[^c6] Sabotaged supervision (deliberately wrong labels) served as a negative control: a faithful harness must lose accuracy.[^c7]

**What governs validity.** The correlation persisted for cross-family pairs, comparable to same-family pairs, provided the teacher beat the student on the base task. The authors read this as a capability gap, not shared family, driving the proxy.[^c8] It weakens where the gap is smallest.[^c9]

**Why the proxy is not an LLM judge.** A judge as strong as the student cannot see gains beyond its own level (see [[llm-judge-biases]]); the teacher's labels carry information the student lacks.

## Limits

- Two failure modes: a small gap, or a teacher that is itself very poor. The correlation drops though still present.[^c10] The authors suggest checking the teacher with a handful of labeled samples; the teacher needs to be correct a clear majority of the time.[^c10]
- The claim that this transfers to human correctors over a frontier model is the authors' conjecture, untested against real operational gold labels; they name it as future work.[^c11]
- Only three security classification tasks and three families; gold exists only for those. Correlations are over few harness configurations (my observation), and sparse correction sets were small.
- Corrections were sampled from the teacher's disagreements; real human feedback is rarer and unevenly shared.

## Related

- [[llm-judge-biases]] — why a same-strength judge is no substitute for this measure
- [[llm-judge-score-instability]] — judge scores vary, a further reason to avoid judge-only evaluation
- [[semantic-self-distillation]] — also uses a model's own or a stronger model's outputs as training signal without labels

[^c1]: doi-10-48550-arxiv-2608-13608 — "We score a harness by how much its student converges toward the teacher over time."
[^c2]: doi-10-48550-arxiv-2608-13608 — "student* has seen no more than 20 corrections out of hundreds of data points"
[^c3]: doi-10-48550-arxiv-2608-13608 — "Notice that gold labels are never used at any point other than this final evaluation."
[^c4]: doi-10-48550-arxiv-2608-13608 — "This lets us designate the larger model as"
[^c5]: doi-10-48550-arxiv-2608-13608 — "the larger model out performs the smaller model on each of the three tasks"
[^c6]: doi-10-48550-arxiv-2608-13608 — "the sign of the"
[^c7]: doi-10-48550-arxiv-2608-13608 — "Sabotage is our negative control"
[^c8]: doi-10-48550-arxiv-2608-13608 — "what governs the proxy’s validity is a capabilities gap between student and teacher"
[^c9]: doi-10-48550-arxiv-2608-13608 — "are precisely those where the gap is smallest"
[^c10]: doi-10-48550-arxiv-2608-13608 — "the teacher needs to be correct a clear majority of the time"
[^c11]: doi-10-48550-arxiv-2608-13608 — "The obvious extension to this work is to validate the human-frontier conjecture"
