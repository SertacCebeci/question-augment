---
description: "Treating a frozen model's guiding questions as learnable text parameters, refined by an optimizer model from labeled errors, beat hand-written and absent questions on video anomaly detection."
aliases: ["verbalized learning of questions", "learnable guiding questions", "VERA"]
sources: ["doi-10-48550-arxiv-2412-01095"]
---
# Learned guiding questions

Instead of tuning a model's weights, VERA (Ye et al. 2024) tunes the *questions* placed in its prompt. A small set of guiding questions Q is the only learnable parameter. A frozen vision-language model acts as learner and answers with Q in its prompt. A second role of the same frozen model acts as optimizer, reads the learner's batch predictions against the ground truth, and rewrites Q. The paper describes this as "optimize them through data-driven verbal interactions between learner and optimizer VLMs".[^c1]

## Mechanism

The starting point is an abstract question such as "is there any anomaly?". The stated intuition is that reasoning improves "if we find questions with suitable and concrete description of abnormal patterns rather than with abstract and general words".[^c2] Iteration pushes the questions from the abstract toward concrete, recognizable patterns. Each question captures a distinct abnormal pattern, so a hard judgment is decomposed into several simpler ones.

The supervision is coarse: video-level normal or abnormal labels, with no frame annotations. The questions are plain language. That makes them portable across datasets and across models, which the paper reports as generalization.

## What was measured

On UCF-Crime with InternVL2-8B, the way Q was obtained changed AUC substantially (Table 5):

- No questions in the prompt: 78.81.
- Questions written by a human: 81.15.
- Learned questions, with the optimizer denied the video frames: 78.06.
- Iteratively learned questions, with the optimizer shown the frames: 86.55.

The paper's reading is that no questions at all is poor, and that "if we use manually written questions (Q0 ), the performance is suboptimal with an 81.15% AUC".[^c3]

Two further findings bear on asking. First, the optimizer must see the evidence. Updating Q from predictions and labels alone "will dumb the VLMs", so the revision signal has to include the underlying input.[^c4] Second, the number of questions matters up to a point. One question limits reasoning to a single perspective, AUC rises up to about five questions, and "increasing m beyond 5 yields no significant gains".[^c5]

## Limits

- Everything is video anomaly detection with a binary, coarsely labeled task. Whether learned questions help open-ended or conversational asking is untested.
- The optimizer and learner are the same frozen model family, and the paper compares against a single handwritten set Q0, not against skilled human question writers or other prompt-optimization methods in the same table.
- The "decomposition into simpler questions" account of why it works is the authors' intuition. The ablations show the questions matter, not that decomposition is the mechanism.
- The five-question plateau was measured on one dataset and model.
- Labels are required, so this is learning from feedback, not unsupervised question improvement.

## Related

- [[reinforcement-prompt-selection]] — also learns how to prompt from reward, but picks among a fixed pool of styles rather than rewriting question text
- [[preference-optimization-for-questions]] — optimizes the questioner's weights, where this optimizes the question text of a frozen model
- [[question-as-partition]] — a set of focused questions as a decomposition of one hard judgment
- [[prompt-coach]] — improving prompts by feedback

[^c1]: doi-10-48550-arxiv-2412-01095 — "optimizes them through data-driven verbal"
[^c2]: doi-10-48550-arxiv-2412-01095 — "find questions with suitable and concrete description of abnormal patterns rather than with abstract and general words"
[^c3]: doi-10-48550-arxiv-2412-01095 — "if we use manually written questions (Q0 ), the performance is suboptimal with an 81.15% AUC"
[^c4]: doi-10-48550-arxiv-2412-01095 — "will dumb the VLMs and make it have a"
[^c5]: doi-10-48550-arxiv-2412-01095 — "increasing m"
