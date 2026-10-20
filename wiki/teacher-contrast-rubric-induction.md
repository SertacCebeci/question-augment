---
description: "Criteria induced from several teacher answers contrasted with student rollouts, shared across a prompt's group, carry the signal; one teacher answer collapses them."
aliases: ["teacher-student contrast rubric", "rubric induction from teacher and student responses", "multi-teacher rubric seeding", "contrastive rubric induction", "rubricator"]
sources: ["doi-10-48550-arxiv-2605-07396"]
---
# Teacher-contrast rubric induction

A rubric is usually written before training, from the question or from a reference answer. The induction studied here writes it during training, from the responses themselves. For one prompt the procedure collects several teacher responses and the student's rollouts, and a rubricator reads both sets together to produce a list of criteria. Each criterion is a text statement with a weight. "Here, YxT provides high-level evidence of desirable solution strategies," the authors write, and the rubricator turns that evidence, together with the student's own rollouts, into the criteria.[^c1] The contrast is the point: the criteria are meant to name what the student does and the teacher's answers do differently, which a single reference cannot show. The paper states the design as "ROPD instead induces rubrics from the contrast between" multi-teacher answers and on-policy student rollouts.[^c2]

Two design choices are measured in the paper's leave-one-out ablation on AIME24. The first is how many teacher answers seed the rubric. The second is whether one rubric is shared across a prompt's rollouts. "Crucially, Cx is shared across all n student rollouts for the same prompt," which keeps the reward consistent within the group that group-based optimization compares.[^c3]

Multi-teacher seeding is the larger effect. Dropping to a single teacher answer lowers Pass@1 from 65.02 to 47.08, which the authors summarise as "m = 1 causes a catastrophic 17.9 point drop in Pass@1."[^c4] Their account of the mechanism is that "A single teacher answer over-anchors the rubric to a specific solution trajectory, causing criteria to collapse into" matching a path rather than checking correctness; several teacher strategies instead "empower the Rubricator to induce" criteria that hold regardless of route.[^c5]

Sharing is the smaller one. The authors' phrase is "Sharing aggregates cross-rollout contrast." Using one shared rubric per prompt, rather than one per teacher-student pair, "yields a +3.75 point gain" on the full method; on their reading a shared rubric can "surface systematic reasoning gaps shared across the rollout distribution."[^c6][^c8]

The criteria carry weights, and these are set by the model, not by the authors: "are dynamically assigned by the Rubricator."[^c7] The verifier then scores each rollout's satisfaction of each criterion, which is the reward described in [[rubric-reward-on-policy-distillation]].

## Limits

- Every ablation number comes from one benchmark (AIME24) and one student-teacher pair. Components are removed one at a time, not jointly, and no interval is reported.
- The cost of multi-teacher seeding is not isolated. With m = 4 the teacher produces four answers per prompt; the wall-clock comparison in the paper is for the whole run, so the price of the extra teacher calls is my inference, not a measurement.
- The criteria are the rubricator's output and are not checked for correctness in the sections I read. A criterion that is wrong but consistent across rollouts is rewarded without any test of it.
- The "path-matching" explanation is the authors' reading of why m = 1 hurts. The paper gives example rubrics, but I did not find a count of how many criteria collapse onto one path.
- The shared-versus-per-pair comparison is a single gap of 3.75 points on one benchmark.

## Related

- [[rubric-reward-on-policy-distillation]] — the reward this induction feeds, and the verifier that scores rollouts against it.
- [[question-specific-rubric]] — rubrics written per question from the question alone, without any response contrast.
- [[shift-labelled-rubric-contrast]] — labels existing rubrics by how they move a verifier; this note is about generating the criteria from response contrast.
- [[single-reference-grading-confound]] — one reference answer as the grading target; the m = 1 result is the same failure showing up in distillation.
- [[zero-variance-group-waste]] — why a reward that is comparable within a rollout group matters for group-relative optimization.

[^c1]: doi-10-48550-arxiv-2605-07396 — "Here, YxT provides high-level evidence of desirable solution strategies."
[^c2]: doi-10-48550-arxiv-2605-07396 — "ROPD instead induces rubrics from the contrast between"
[^c3]: doi-10-48550-arxiv-2605-07396 — "Crucially, Cx is shared across all n student rollouts for the same prompt"
[^c4]: doi-10-48550-arxiv-2605-07396 — "m = 1 causes a catastrophic 17.9 point drop in Pass@1."
[^c5]: doi-10-48550-arxiv-2605-07396 — "rubric to a specific solution trajectory, causing criteria to collapse into"
[^c6]: doi-10-48550-arxiv-2605-07396 — "yields a +3.75 point gain."
[^c7]: doi-10-48550-arxiv-2605-07396 — "are dynamically assigned by the Rubricator."
[^c8]: doi-10-48550-arxiv-2605-07396 — "to surface systematic reasoning gaps shared across the rollout distribution"
