---
description: "A frozen teacher that sees the user's rubric aspects scores a rubric-free student's own rollouts token by token, so the rubric's steering moves into the student's weights."
aliases: ["GRASP", "rubric-informed on-policy self-distillation", "rubric-privileged self-distillation", "rubric-aware OPSD", "RGSD", "rubric-guided self-distillation"]
sources: ["doi-10-48550-arxiv-2609-35262", "doi-10-48550-arxiv-2608-02948", "doi-10-48550-arxiv-2606-12507", "doi-10-48550-arxiv-2606-19327"]
---
# Rubric-aware on-policy self-distillation

A user's rubric aspects say what a satisfactory personalized answer must cover, but they are not available at inference. This scheme keeps them out of the deployed model and gives them to a second copy of the same model during training only. The student is trainable and sees the question and the user profile. The teacher is the same backbone, frozen, and additionally sees the target rubric aspects.[^c1] The rubric is therefore privileged information in the sense used by on-policy self-distillation: the teacher knows something the student cannot see, and training is what moves that knowledge across.[^c2]

For each training question the student writes a response by sampling from its own policy. At every position of that response, both models predict the next token given the same student-generated prefix. The student is trained to minimize the forward KL divergence from the teacher's next-token distribution to its own, averaged over the response.[^c3] Because the prefix is the student's own, the supervision lands on the states the student actually reaches, "at the generation states it actually encounters."[^c4] The teacher's distributions are fixed targets, and gradients go only into the student.[^c5] At inference the student gets the question and profile alone, which is the same information it had in training.

## What the transfer consists of

The authors' central check is about the mechanism, not the score. On Qwen2.5-7B, using 90 held-out responses, they fed each sampled prefix to three models: the student before training, the student after training, and the rubric-conditioned teacher.[^c6] The rubric-induced shift and the training-induced shift agree in direction on 79.2% of 14,216 tokens, with correlation r = 0.71.[^c7] The response-level forward KL from teacher to student falls from 1.101 to 0.444 on average.[^c8] In their representative example, training moves the observed token toward the teacher's probability, "teacher probability of 0.99, while generic alternatives are suppressed."[^c9] So the student is not learning the rubric's content as text; it is learning to put probability where a rubric-conditioned model would.

The gain depends on the rubric being the right one. Shuffling rubrics across training instances, which keeps their overall distribution and breaks their alignment with each question, "shuffled rubrics lead to a substantial performance drop."[^c10] The authors conclude that the benefit does not come from extra teacher context: it "stems not from exposing the teacher to arbitrary" additional context, but from question-specific semantic targets.[^c11] A larger teacher did not help: "using a larger teacher in GRASP provides no clear advantage over" self-distillation.[^c12]

On LaMP-QA, across four backbones, the method reports the highest average score on every backbone, with a relative gain of 14% over the strongest baseline on Gemma2-9B.[^c13][^c14]

A parallel study on HealthBench, with physician-written rubrics used as privileged information on a Qwen2.5-7B-Instruct student, reports the same on-policy effect from a different angle. On the base model's own rollouts, rubric conditioning gives more per-token KL than reference-completion conditioning.[^c19] The authors also find that offline fine-tuning on the same rubric content does not reproduce the gain, so the on-policy KL is part of the mechanism and not only the information.[^c20] How strongly a privileged text constrains the teacher is the separate question taken up in [[soft-versus-hard-privileged-information]].

A fourth study, rubric-guided self-distillation (RGSD), keeps this skeleton with two changes. The teacher is the base model itself, frozen: "the base policy, conditioned on the rubric, serves as the teacher for the unconditioned student."[^c21] The loss is a clipped Jensen–Shannon divergence, with "we use β = 0.5 throughout," midway between forward and reverse KL.[^c22] On medical and science the abstract reports that RGSD "achieves rubric satisfaction comparable to judge-based" GRPO, with one rollout per prompt and no training-time verifier calls, where GRPO "requires 80 judge calls per training prompt" over five epochs.[^c23][^c24] For thinking models the teacher's trace may name rubric criteria "even when the system prompt explicitly asks it not to," so the paper masks thinking tokens from the loss, which it reports as an "improvement on Qwen3-Thinking after masking" of 2–4 points.[^c25][^c26] Which rubric-conditioned teacher context carries the most signal is taken up in [[soft-versus-hard-privileged-information]].

A fifth study, RCSD, keeps the rubric as the teacher's privileged context and drops the reference answer from the second stage. Its abstract describes the teacher as conditioned "on criterion-level rubrics," and the authors state the change as "instead of conditioning the privileged teacher on a single reference trajectory, we condition" it on a rubric.[^c31][^c32] On Qwen3-8B the average is 70.6, against 69.7 for reference-conditioned OPSD, the strongest baseline in their table.[^c33] The introduction and the abstract give different margins over GRPO (1.4 and 1.0 points), which matches two different GRPO rows in the table (69.2 and 69.6).[^c39] The rubric itself can come from a question-only generator trained by distilling a reference-seeing teacher; that step is treated in [[amortized-rubric-generation]].

The same paper tests the loss direction that the limits below call untested. On the Qwen3-8B backbone the averages are 70.6 for forward KL, 69.9 for reverse KL and 69.6 for JSD, and the authors conclude that "results suggest that Forward KL is the most effective objective for RCSD in this setting."[^c34] Their training curves show "student entropy increases steadily" under forward KL, while reverse KL "reduces entropy, reflecting its more mode-seeking tendency."[^c35][^c36] The argument is the mass-covering one given above, and the paper reports no seed variance for the 0.7-point gap.

## Limits

- The rubric aspects are per-question semantic specifications written for the benchmark, derived "from the question narrative" rather than from observed behaviour.[^c15] Whether a rubric written by a person, or one inferred from a user's history, carries the same signal is not tested here.
- The evaluation is one benchmark (LaMP-QA, three categories) scored by an LLM judge on a 0–2 scale: "normalized scores averaged to obtain the final score."[^c16] The judge that defines the target is also the judge that scores the output, so the score measures agreement with the rubric-judge's view. I did not find a human check in the sections I read.
- Training is one epoch with checkpoint selection on validation: "We train GRASP for 1 epoch."[^c17] Longer training or a different stopping rule is not explored in what I read.
- The mechanism analysis uses one backbone and 90 responses. The token-level agreement figure says nothing about how far the student generalizes beyond that sample.
- Only forward KL is used. The sections I read do not compare it with reverse KL or other divergences; the choice is asserted, not tested (my inference).
- The claim that the student "internalizes" the rubric is the authors' reading of a distribution shift. It is consistent with the measurements but does not show that the student represents the aspects.
- The RGSD comparison is mostly single-seed: "most main-table runs are single-seed," so the authors "interpret small margins as parity" rather than as wins.[^c27][^c28]
- The ordering can flip with a stronger judge. On science a gpt-oss-120b judge reaches "39.2 versus 35.9 at peak on RubricHub-sci," so RGSD "should not be read as dominating the best attainable judge-based GRPO configuration."[^c29][^c30]
- The RCSD study also tests the rubric's content. Replacing the learned rubric with one from another question ("Random samples a rubric from another") gives 70.0 on the average, against 70.6 for the learned rubric, and every degraded variant still beats the base model at 65.9.[^c37][^c40] This is a small drop, not the "substantial" one reported for shuffled rubrics above, though the teacher setting differs.
- The comparisons are not at equal training length. The authors train GRPO for more steps than the self-distillation methods, "following prior work's implementation."[^c38]

Training cost is reported as practical, and the method adds no inference cost over RAG: "no additional inference cost over standard RAG."[^c18] That is a cost statement about this setup, not a general one.

## Related

- [[rubric-based-teacher-validation]] — the filter that keeps only teacher rollouts covering every aspect before this distillation runs.
- [[qcp-guided-self-distillation]] — another privileged-information self-distillation; its privileged signal is a by-product of question generation, not a hand-written rubric.
- [[knowledge-boundary-aware-self-distillation]] — same-policy privileged self-distillation that switches KL direction per quadrant; here the direction is fixed at forward KL.
- [[socraticpo]] — teacher guidance in RL that is text, not token distributions, and is decayed to deny free reward.
- [[soft-versus-hard-privileged-information]] — how strongly a rubric or reference constrains the teacher, and why a soft rubric spreads the signal where a reference concentrates it.
- [[rubric-conditioning-gap]] — the score lift a rubric gives the base teacher before training; RGSD reads it as a cheap pre-check on how much signal the teacher can offer.
- [[rubric-reward-on-policy-distillation]] — the text-only alternative: the rubric is not given to a teacher's logits but scores the student's rollouts as the reward, so no teacher distributions are needed.
- [[amortized-rubric-generation]] — how RCSD obtains the rubric at training time from a question-only generator distilled from a reference-seeing teacher.

[^c1]: doi-10-48550-arxiv-2609-35262 — "model conditioned on the user-specific rubric aspects serves as the teacher."
[^c2]: doi-10-48550-arxiv-2609-35262 — "By restricting rubric access to the teacher during training, GRASP distills this privileged guidance"
[^c3]: doi-10-48550-arxiv-2609-35262 — "we instantiate d as the forward KL divergence:"
[^c4]: doi-10-48550-arxiv-2609-35262 — "receiving dense, rubric-conditioned supervision at the generation states it actually encounters."
[^c5]: doi-10-48550-arxiv-2609-35262 — "The teacher distributions are treated as fixed targets, with gradients propagated exclusively through the"
[^c6]: doi-10-48550-arxiv-2609-35262 — "We conduct this analysis on Qwen2.5-7B using 90 held-out responses."
[^c7]: doi-10-48550-arxiv-2609-35262 — "The two shifts agree in direction for 79.2% of 14,216 tokens, with a correlation of r = 0.71, indicating"
[^c8]: doi-10-48550-arxiv-2609-35262 — "student decreases from 1.101 to 0.444 on average after training, with all 90 responses moving closer"
[^c9]: doi-10-48550-arxiv-2609-35262 — "teacher probability of 0.99, while generic alternatives are suppressed."
[^c10]: doi-10-48550-arxiv-2609-35262 — "shuffled rubrics lead to a substantial performance drop."
[^c11]: doi-10-48550-arxiv-2609-35262 — "that the benefit of rubric-aware self-distillation stems not from exposing the teacher to arbitrary"
[^c12]: doi-10-48550-arxiv-2609-35262 — "using a larger teacher in GRASP provides no clear advantage over"
[^c13]: doi-10-48550-arxiv-2609-35262 — "highest average score on all four backbones with diverse model families and scales."
[^c14]: doi-10-48550-arxiv-2609-35262 — "on the Gemma2-9B backbone, GRASP achieves an average relative improvement of 14% over"
[^c15]: doi-10-48550-arxiv-2609-35262 — "These aspects are derived from the question narrative"
[^c16]: doi-10-48550-arxiv-2609-35262 — "normalized scores averaged to obtain the final score."
[^c17]: doi-10-48550-arxiv-2609-35262 — "We train GRASP for 1 epoch"
[^c18]: doi-10-48550-arxiv-2609-35262 — "no additional inference cost over standard RAG."
[^c19]: doi-10-48550-arxiv-2608-02948 — "rubric conditioning produces 1.7× more per-token KL than reference conditioning"
[^c20]: doi-10-48550-arxiv-2608-02948 — "the onpolicy dense-KL mechanism, along with the rubric content, is what makes RuPI work"
[^c21]: doi-10-48550-arxiv-2606-12507 — "the base policy, conditioned on the rubric, serves as the teacher for the unconditioned student."
[^c22]: doi-10-48550-arxiv-2606-12507 — "we use β = 0.5 throughout."
[^c23]: doi-10-48550-arxiv-2606-12507 — "RGSD achieves rubric satisfaction comparable to judge-based"
[^c24]: doi-10-48550-arxiv-2606-12507 — "requires 80 judge calls per training prompt"
[^c25]: doi-10-48550-arxiv-2606-12507 — "even when the system prompt explicitly asks it not to."
[^c26]: doi-10-48550-arxiv-2606-12507 — "improvement on Qwen3-Thinking after masking vs. when the loss is applied to the entire trace."
[^c27]: doi-10-48550-arxiv-2606-12507 — "most main-table runs are single-seed"
[^c28]: doi-10-48550-arxiv-2606-12507 — "We therefore interpret small margins as parity rather than as statistically significant wins."
[^c29]: doi-10-48550-arxiv-2606-12507 — "39.2 versus 35.9 at peak on RubricHub-sci."
[^c30]: doi-10-48550-arxiv-2606-12507 — "dominating the best attainable judge-based GRPO configuration."
[^c31]: doi-10-48550-arxiv-2606-19327 — "Our method conditions the teacher model on criterion-level rubrics and"
[^c32]: doi-10-48550-arxiv-2606-19327 — "instead of conditioning the privileged teacher on a single reference trajectory, we condition"
[^c33]: doi-10-48550-arxiv-2606-19327 — "outperforming the strongest baseline, OPSD,"
[^c34]: doi-10-48550-arxiv-2606-19327 — "results suggest that Forward KL is the most effective objective for RCSD in this setting."
[^c35]: doi-10-48550-arxiv-2606-19327 — "student entropy increases steadily, suggesting that the model preserves a broader rubric-conditioned output"
[^c36]: doi-10-48550-arxiv-2606-19327 — "reduces entropy, reflecting its more mode-seeking tendency"
[^c37]: doi-10-48550-arxiv-2606-19327 — "over the base model, suggesting that criterion-style supervision remains useful even with imperfect rubrics"
[^c38]: doi-10-48550-arxiv-2606-19327 — "GRPO is trained for 500 steps while self-distillation based methods are trained for"
[^c39]: doi-10-48550-arxiv-2606-19327 — "surpassing GRPO by 1.4 points and OPSD by 0.9"
[^c40]: doi-10-48550-arxiv-2606-19327 — "Random samples a rubric from another"
