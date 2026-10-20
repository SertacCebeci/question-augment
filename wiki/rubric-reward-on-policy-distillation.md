---
description: "On-policy distillation can run on teacher text alone: rubric criteria induced from teacher-student contrast score the student's rollouts, and the weighted pass rate replaces teacher logits."
aliases: ["ROPD", "rubric-based on-policy distillation", "rubric-based OPD", "black-box on-policy distillation with rubric rewards"]
sources: ["doi-10-48550-arxiv-2605-07396"]
---
# Rubric-reward on-policy distillation

On-policy distillation (OPD) trains a student on trajectories it samples itself, with a teacher supplying the supervision. The common form is white-box: the teacher's next-token distribution is the dense signal at each position of the student's sequence. The paper's diagnosis is that this "reliance on teacher logits restricts its application to white-box scenarios."[^c1] The variant described here keeps the on-policy part and replaces the logit signal with a reward computed from teacher text, "using only teacher-generated responses."[^c2]

The mechanism has two stages. For each prompt, teacher and student each produce responses, and a rubricator contrasts them to write a set of weighted criteria; the paper's rubric induction "induces prompt-specific rubrics from teacher-student contrasts."[^c3] Then a verifier marks each student rollout against each criterion as satisfied or not, and the response's reward is a weighted pass rate, "computed as the weighted pass rate." That verified score is "utilized ... to score the student rollouts for on-policy optimization," so the policy update is driven by how many weighted criteria a rollout satisfies rather than by a token-level divergence.[^c4] The rubric is shared by all rollouts of the same prompt, so the reward is comparable within a group, which suits group-relative policy optimization (see [[teacher-contrast-rubric-induction]]). The paper frames the result as a reward that is "simultaneously teacher-grounded and rollout-conditioned."[^c5]

In the authors' setup the teacher usually plays both the rubricator and the verifier. They report that swapping in an auxiliary model "has a marginal impact on final results, demonstrating the flexibility of our paradigm."[^c6]

What was measured. On AIME24, with a Qwen3-4B student and a Qwen3-30B-A3B teacher in non-thinking mode, the rubric reward reaches LOPD's best level "with an order of magnitude fewer samples (1.6k vs. 15.4k)."[^c7] In white-box comparisons the same paper reports that "while LOPD bridges only 42.1% of the student-teacher gap, ROPD closes 74.1% of the same interval."[^c8] The authors' explanation is that a logit-matching signal "measures distributional similarity rather than correctness," while criteria give outcome-oriented feedback.[^c9] Read as a claim about the mechanism, the paper says the reward carries task-level reasoning principles, not phrasing.

## Limits

- The efficiency figures come from one student-teacher pair on math-heavy benchmarks. The authors say their "evaluation mainly focuses on formal reasoning, such as Mathematics, Medicine, and Science."[^c10] "the performance of rubric-based OPD in subjective or creative tasks remains to be" established.[^c11]
- Robustness to the judge is asserted from preliminary results: "ROPD depends on the instruction-following of the Rubricator and Verifier."[^c12] The reward is only as good as the criteria, and the paper's evidence that a different rubricator is harmless is a single sentence of preliminary results.
- The sample-efficiency claim is a comparison with one logit-based baseline family. Whether a well-tuned logit method with a different teacher closes the gap is not tested here.
- The headline "10×" is a ratio of sample counts on one setting, not a general speedup. The wall-clock gain is reported for the same hardware and teacher, and the rubric-scoring overhead per step is larger.
- Each measured quantity is a single run of a v1 preprint. I did not find variance across seeds in the sections I read; treat the gaps as indicative (my inference).
- The method is a reward, so it inherits the weaknesses of rubric rewards: criteria that are credited partially, or matched at the wrong level of specificity (see [[rubric-verifier-failure-modes]]).

## Related

- [[rubric-aware-on-policy-self-distillation]] — keeps the teacher's logits and gives the rubric to the teacher as privileged context; this note drops the logits and makes the rubric the reward.
- [[teacher-contrast-rubric-induction]] — how the criteria are written from several teacher answers and the student's rollouts, and why the teacher count matters.
- [[identity-blind-verification]] — why the verifier scores teacher and student rollouts together without knowing which is which.
- [[question-specific-rubric]] — per-question rubrics used as an RL reward, without the teacher-distillation framing.
- [[rubric-verifier-failure-modes]] — the verifier errors that a rubric reward is exposed to.

[^c1]: doi-10-48550-arxiv-2605-07396 — "its reliance on teacher logits restricts its application to white-box scenarios."
[^c2]: doi-10-48550-arxiv-2605-07396 — "enabling OPD using only teacher-generated responses."
[^c3]: doi-10-48550-arxiv-2605-07396 — "ROPD induces prompt-specific rubrics from teacher-student contrasts,"
[^c4]: doi-10-48550-arxiv-2605-07396 — "and then utilizes these rubrics to score the student rollouts for on-policy optimization."
[^c5]: doi-10-48550-arxiv-2605-07396 — "the resulting reward is simultaneously teacher-grounded and rollout-conditioned."
[^c6]: doi-10-48550-arxiv-2605-07396 — "auxiliary LLM has a marginal impact on final results, demonstrating the flexibility of our paradigm."
[^c7]: doi-10-48550-arxiv-2605-07396 — "an order of magnitude fewer samples"
[^c8]: doi-10-48550-arxiv-2605-07396 — "42.1% of the student-teacher gap, ROPD closes 74.1% of the same interval"
[^c9]: doi-10-48550-arxiv-2605-07396 — "this signal measures distributional similarity rather than correctness"
[^c10]: doi-10-48550-arxiv-2605-07396 — "our evaluation mainly focuses on formal reasoning, such as Mathematics, Medicine, and Science."
[^c11]: doi-10-48550-arxiv-2605-07396 — "the performance of rubric-based OPD in subjective or creative tasks remains to be"
[^c12]: doi-10-48550-arxiv-2605-07396 — "ROPD depends on the instruction-following of the Rubricator and Verifier."
