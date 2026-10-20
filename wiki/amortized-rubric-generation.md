---
description: "A rubric generator distilled on-policy from a reference-seeing teacher writes question-only rubrics whose downstream training score nearly matches a larger teacher's direct rubrics."
aliases: ["Stage-I rubric generator", "amortized rubric generator", "on-policy rubric distillation", "learned rubric generator"]
sources: ["doi-10-48550-arxiv-2606-19327"]
---
# Amortized rubric generation

Rubric-conditioned self-distillation needs a rubric for every training question, and a rubric written by hand for each one is expensive. The RCSD pipeline pays that cost once. A first stage trains a standalone generator to produce a rubric from the question alone, and the generator then supplies the rubrics that the second stage's teacher reads.[^c1] In this stage the teacher sees more than the student: the teacher gets "question and a reference answer, while the student must learn to infer an appropriate rubric" from the question alone.[^c1]

The distillation works on the rubric, not on an answer. The student generator samples its own rubric, and the loss compares the teacher's and the student's next-token distributions along that sampled rubric, which the authors call "On-policy rubric distillation."[^c2] The reference answer is not copied into the rubric: it is "to be copied directly; rather, it serves as a privileged context that helps the teacher infer how" to write criteria that fit a correct response.[^c3] The on-policy property is inherited from the answer-level method, so the generator is trained "on its own sampled prefixes rather than teacher-generated ones."[^c4] The reference is thus used once, in training the generator; at test time the generator sees the question only.

In the second stage the generated rubric is handed to the teacher as context. The authors write that "Conditioning the teacher on r allows the training signal to reflect multiple dimensions of response quality," where r is the learned rubric.[^c5] The reference answer does not appear in that stage's teacher input.

## What the amortization buys

On the authors' numbers, the amortized rubrics come close to the directly written ones. On three benchmarks where both are reported, generated rubrics sit slightly below reference rubrics: GPQA-D 64.5 against 65.2, SciBench 70.6 against 71.0, PIQA 90.8 against 91.0 (Table 4). The authors summarise this as "competitive across the benchmark suite, with only small gaps to GT rubrics on GPQA-D."[^c6] The generated rubrics carry slightly more criteria, "(8.4 vs. 7.5)," at similar length, 236.6 against 248.7 tokens.[^c7]

Against prompting a teacher for rubrics directly, the learned generator reaches 70.6 on the average, a 14B teacher prompted directly 70.7, and an 8B teacher prompted directly 69.9 (Table 5). The result is "nearly matching +14b Direct at 70.7 and outperforming +8b Direct at 69.9."[^c8] The authors' case for the generator is cost, not score: "teacher to produce rubrics directly; in contrast, the Stage-I generator provides a scalable" route to task-specific rubrics.[^c9] Training the generator itself took 1000 steps, "The rubric generator is trained for 1000 steps with a" maximum sequence length of 2,048.[^c10]

## Limits

- The experiments measure a rubric by the score of the reasoner trained with it, not by the rubric's correctness. The sections I read contain no human check of the generated criteria; their quality is inferred from downstream accuracy (my inference).
- The generator's training rubrics come from the same families the method is tested on. "For rubric learning, we construct our training set" from RaR-Science and RubricHub, and both also appear in the evaluation suite.[^c11] The test is therefore in-distribution. Rubrics written for a different kind of task are not tested here.
- Table 4 reports only three of the six benchmarks, so the gap to reference rubrics is shown on a subset.
- Degraded rubrics do nearly as well as learned ones. Table 6 gives averages of 69.9 to 70.2 for a generic template, a rubric from another question, a noisy mix and a half-length rubric, against 70.6 for the learned generator and 65.9 for the base model. The authors say "over the base model, suggesting that criterion-style supervision remains useful even with imperfect rubrics."[^c12] So in this setup the generator's question-specific content is worth about 0.6 to 0.7 average points, and the text reports no seed variance for these ablations.
- The authors explain the tolerance to bad rubrics as the teacher "likely by using the reference answer to reconcile rubric errors."[^c13] The Stage-II teacher in the stated objective receives the question and the rubric, not the reference, so the explanation is not the one the stated design supports. The reference could only enter through the rubrics the generator learned from it (my reading).
- The generator is trained on "approximately 10k samples for rubric generation" and the text does not test how the result moves with that data size.[^c14]

## Related

- [[rubric-aware-on-policy-self-distillation]] — the distillation that consumes the generated rubric; this note is the step that makes a rubric available without a hand-written one.
- [[question-specific-rubric]] — a per-question rubric used as a reward; here the per-question rubric is generated rather than written.
- [[co-evolving-rubric-generator]] — another trained rubric generator, rewarded for the spread of scores its criteria give candidate answers in RL, not distilled from a privileged teacher.
- [[soft-versus-hard-privileged-information]] — the reference answer the Stage-I teacher sees is the hard privileged input; the generator keeps from it a question-level rubric.
- [[bootstrap-rubric-generation]] — a policy writing its own rubrics as its reward; here the generator is anchored to a teacher that has seen a reference.

[^c1]: doi-10-48550-arxiv-2606-19327 — "question and a reference answer, while the student must learn to infer an appropriate rubric"
[^c2]: doi-10-48550-arxiv-2606-19327 — "On-policy rubric distillation. Given a sampled rubric rollout"
[^c3]: doi-10-48550-arxiv-2606-19327 — "to be copied directly; rather, it serves as a privileged context that helps the teacher infer how"
[^c4]: doi-10-48550-arxiv-2606-19327 — "trained on its own sampled prefixes rather than teacher-generated ones."
[^c5]: doi-10-48550-arxiv-2606-19327 — "Conditioning the teacher on r allows the training signal to reflect multiple dimensions of response quality,"
[^c6]: doi-10-48550-arxiv-2606-19327 — "competitive across the benchmark suite, with only small gaps to GT rubrics on GPQA-D"
[^c7]: doi-10-48550-arxiv-2606-19327 — "Generated rubrics contain slightly more criteria on average than reference rubrics (8.4 vs. 7.5),"
[^c8]: doi-10-48550-arxiv-2606-19327 — "nearly matching +14b Direct at 70.7 and outperforming +8b Direct at 69.9."
[^c9]: doi-10-48550-arxiv-2606-19327 — "teacher to produce rubrics directly; in contrast, the Stage-I generator provides a scalable"
[^c10]: doi-10-48550-arxiv-2606-19327 — "The rubric generator is trained for 1000 steps with a"
[^c11]: doi-10-48550-arxiv-2606-19327 — "For rubric learning, we construct our training set"
[^c12]: doi-10-48550-arxiv-2606-19327 — "over the base model, suggesting that criterion-style supervision remains useful even with imperfect rubrics"
[^c13]: doi-10-48550-arxiv-2606-19327 — "that the teacher can compensate for imperfect rubric information, likely by using the"
[^c14]: doi-10-48550-arxiv-2606-19327 — "approximately 10k samples for rubric generation and 30k samples for reasoning generation."
