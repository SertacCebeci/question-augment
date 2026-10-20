---
description: "When no optimum is known, a solution can be scored on a continuum anchored by a trivial floor and an expert ceiling, so a valid but weak answer earns partial credit instead of a pass or fail."
aliases: ["partial scoring", "open-ended partial scoring", "baseline-and-reference scoring", "continuous quality scoring", "unknown-optimum scoring"]
sources: ["arxiv-2512-15699"]
---
# Two-anchor graded scoring

A pass-or-fail check answers one question: does this answer reach the threshold. It is adequate when the threshold is the whole point, as in a single correct value. It stops being informative when many answers are valid and they differ in quality, and when the best achievable quality is unknown. FrontierCS, a benchmark of 156 open-ended computer-science problems, faces exactly this. It states that "no problem has a universally correct solution, so we cannot use accuracy as an evaluation metric."[^c1]

The replacement is a score on a continuum, placed between two reference points: "the reference solution written by human experts and a trivial baseline solution."[^c2] The two anchors do different jobs. The floor is the most trivial solution the problem admits. A solution that does not reach it gets nothing: "if a solution fails to reach the level of the trivial baseline, it receives a score of zero."[^c3] The ceiling is an expert solution. A solution that clears it, or a nontrivial bound where one exists, "receives a full score. Scores between these two extremes are assigned based on the nature of" the problem.[^c4] So the scale starts where an attempt does something useful and saturates where expert work stops, and the in-between is tailored per problem.

The scale is applied to a problem only after a review in which the problem must show "no known optimal solution or a nearly optimal solution that leaves limited room for improvement."[^c5] Without that condition the top anchor would be the optimum and the scale would reduce to pass-or-fail again. The construction also makes the instance count open. The paper's definition asks for a "Parametric Problem Generator" so that "instances, enabling fresh, unseen test cases to prevent leak and overfitting."[^c6]

A worked case shows what the scale adds. In Polyomino Packing, the task is to pack n polyominoes into the smallest grid, scored by density. "both the human expert and GPT-5 produce valid packings, but the human achieves 87% density while GPT-5 achieves only 47%."[^c7] Under pass-or-fail both answers are the same, and the scale separates them. The paper's general claim is that such problems have "quality [that] spans a continuous spectrum rather than a simple pass-or-fail outcome."[^c8]

The reading is my own, not the paper's: the expert anchor works as a ceiling, not as ground truth. A response is not graded by how closely it matches the expert's solution; it is graded by how far it reaches toward it, and anything beyond is full credit. That is what keeps a better-than-expert answer from being scored as an error, the failure a single-reference rule produces.

## Limits

- The paper reports that "we observe that the model exhibits stochasticity," so one attempt is noisy, and it reports Score@1, Avg@5 and Score@5 side by side.[^c9] The anchors do not remove that variance.
- The floor and ceiling are set by experts for each problem. The paper says that when models approach the human reference, "we can refine the human reference solution, scoring rubric, or" the thresholds.[^c10] The anchors therefore move as progress is made, and a score from one version is not directly comparable to a score from another. This is a consequence of the design, not something the paper measures.
- The review's check that the scoring "is objective and can meaningfully reflect progress" is a reviewer's judgement, and the paper does not test it against an independent measure of quality.[^c12]
- The paper says the scores "can effectively drive reinforcement learning," but it does not train with them here.[^c11] That is a proposal, not a result of this work.
- Evidence is from CS problems only: contest-derived algorithms and six research domains. Whether other fields with no known optimum admit anchors of this kind is not tested.

## Related

- [[single-reference-grading-confound]] — the single expert-reference rule this scheme keeps only as a ceiling, not as the answer to match
- [[valid-versus-optimal-answer-gap]] — the measured gap between a solution that passes the floor and one that scores high on this scale

[^c1]: arxiv-2512-15699 — "no problem has a universally correct solution, so we cannot use accuracy as an evaluation metric."
[^c2]: arxiv-2512-15699 — "points: the reference solution written by human experts and a trivial baseline solution."
[^c3]: arxiv-2512-15699 — "for a test case, if a solution fails to reach the level of the trivial baseline, it receives a score"
[^c4]: arxiv-2512-15699 — "bound, it receives a full score. Scores between these two extremes are assigned based on the nature of"
[^c5]: arxiv-2512-15699 — "the problem has no known optimal solution or a nearly optimal solution that leaves"
[^c6]: arxiv-2512-15699 — "instances, enabling fresh, unseen test cases to prevent leak and overfitting."
[^c7]: arxiv-2512-15699 — "valid packings, but the human achieves 87% density while GPT-5 achieves only 47%."
[^c8]: arxiv-2512-15699 — "quality spans a continuous spectrum rather than a simple pass-or-fail outcome"
[^c9]: arxiv-2512-15699 — "we observe that the model exhibits stochasticity"
[^c10]: arxiv-2512-15699 — "surpass strong human baselines, we can refine the human reference solution, scoring rubric, or"
[^c11]: arxiv-2512-15699 — "The scoring functions can effectively drive reinforcement learning or"
[^c12]: arxiv-2512-15699 — "the scoring policy is objective and can meaningfully reflect progress"
