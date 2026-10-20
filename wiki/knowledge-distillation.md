---
description: "A student model is trained to match a teacher's softened output distribution; because imitation can be too rigid, a contrastive term can let the student deviate where the teacher is wrong."
aliases: ["teacher-student distillation", "soft-target distillation", "model distillation", "distillation"]
sources: ["arxiv-2512-16236", "arxiv-2602-11157"]
---
# Knowledge distillation

Knowledge distillation moves what a large model does into a smaller one. The seminal formulation uses "soft targets," the teacher's softmax probabilities, "often with a temperature parameter T," together with a modified cross-entropy loss.[^k1] The survey says the loss can also be read as matching logits, a special case of the same transfer.[^k2] Training on the teacher's full distribution, not only its top answer, is the point of the method. My reading, not the text's: the soft distribution carries how the teacher ranks the wrong options, and that ordering is what a small student cannot easily learn from hard labels.

The survey names a failure of the standard form: "this standard approach can suffer from over-calibration,"[^k3] "where the student too rigidly imitates an imperfect teacher."[^k4] The student inherits the teacher's errors at full strength.

The correction the survey reports is a contrastive term added to the usual KL divergence. It "allows the student model to more conservatively and adaptively learn from the" teacher, so the student can depart from guidance that is suboptimal for a given example.[^k5] The survey says this improves re-ranking "by making the knowledge transfer more robust to teacher errors."[^k6]

In reranking the survey separates two kinds of supervision: "Label Distillation & Rationale-Enhanced Distillation."[^k7] Label distillation transfers scores; rationale distillation transfers the teacher's reasoning text. One reported result is that a "KARD-trained 250M T5 model surpassed a fine-tuned 3B T5 model."[^k8] That is the cited work's claim. The survey's comparison of the two kinds is hedged: explicit knowledge augmentation "might be advantageous for tasks" that need knowledge synthesis beyond the documents.[^k9]

Distilled open models do not close the gap in every case. A LLaMA-based listwise reranker trained with "RankGPT_3.5 as a teacher model" "still lags behind the state-of-the-art RankGPT4."[^k10][^k11] A later model is said to close it, "in a few cases, outperform[ing]" the larger teacher with far fewer parameters.[^k12]

## Limits

Every effectiveness figure in this survey is reported from a cited work. The text read gives no numbers for the contrastive correction, only the claim that it is "demonstrably" helpful.

The survey does not test whether a rationale-distilled student generalizes beyond the datasets of its source paper. The benefit of the explicit knowledge route is stated as possible, not shown.

The text's distillation is about rerankers. Transfer to other tasks is my inference, not in the text: whether the over-calibration failure holds for generation, or for judging, is not established here.

The soft-target form is not the only one. In response-based distillation the student sees only the teacher's final text, because the teacher exposed no logits, a setting the paper calls infeasible: "is infeasible in our study since the proprietary teacher model o1-mini does not".[^k14] With hard labels from a safe teacher, standard fine-tuning on its refusals increases jailbreak success for all student models tested.[^k13] The paper's attribution for this case points to what the refusal set contains, including boundary material, and to forgetting, rather than to the over-calibration named above; see [[boundary-refusal-data]]. That attribution is the paper's own, and the text read tests only the boundary part of it.

## Related

- [[two-stage-reranking]] — the reranker that the survey's distillation methods make cheaper
- [[pointwise-pairwise-listwise-ranking]] — the unit a distilled reranker is trained over
- [[knowledge-boundary-aware-self-distillation]] — the same teacher-supervises-student setup, applied to the student's own rollouts
- [[boundary-refusal-data]] — the response-based case: the teacher's safe refusals, some of them boundary material, still raised student jailbreak success

[^k1]: arxiv-2512-16236 — "often with a temperature parameter T"
[^k2]: arxiv-2512-16236 — "shows is a special case) to transfer knowledge"
[^k3]: arxiv-2512-16236 — "this standard approach can suffer from over-calibration,"
[^k4]: arxiv-2512-16236 — "where the student too rigidly imitates an imperfect teacher"
[^k5]: arxiv-2512-16236 — "allows the student model to more conservatively and adaptively learn from the"
[^k6]: arxiv-2512-16236 — "performance by making the knowledge transfer more robust to teacher errors"
[^k7]: arxiv-2512-16236 — "We delineate two primary categories - Label Distillation & Rationale-Enhanced"
[^k8]: arxiv-2512-16236 — "claims a KARD-trained 250M T5 model surpassed a fine-tuned 3B T5"
[^k9]: arxiv-2512-16236 — "might be advantageous for tasks"
[^k10]: arxiv-2512-16236 — "using RankGPT_3.5 as a teacher model using 100K queries from the MS"
[^k11]: arxiv-2512-16236 — "still lags behind the state-of-the-art RankGPT4"
[^k12]: arxiv-2512-16236 — "in a few cases, outperforms RankGPT_4 with orders"
[^k13]: arxiv-2602-11157 — "standard fine-tuning on the teacher’s “safe” refusal data inadvertently increases"
[^k14]: arxiv-2602-11157 — "is infeasible in our study since the proprietary teacher model o1-mini does not"
