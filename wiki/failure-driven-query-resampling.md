---
description: "Reweights an evaluation query pool by the model's verified failures, Q(x)w(x), so second-stage training concentrates on where the model is wrong; it adds no new knowledge."
aliases: ["failure-driven resampling", "failure-region resampling", "failure-driven post-training", "error-indicator query reweighting"]
sources: ["arxiv-2601-01562"]
---
# Failure-driven query resampling

A first-stage fine-tune leaves a model with a proposal distribution over
questions, and that distribution is rarely the one the model will be judged
on. The move described here is cheap: take an evaluation pool Q of
gold-standard tasks (the authors name AIME2025 and MMLU), run the model on it,
and keep a binary failure function w(x) that is 1 when the verified final
answer is wrong.[^f1] The resampled distribution Q_θ1(x) ∝ Q(x)w(x) then
"increases the sampling probability of regions where the current model
performs poorly."[^f2] Nothing in this step generates a question. It only
changes which existing questions get weight in the next round of training.

The reason offered for why this should help is a distribution-matching
argument. The authors frame post-training as moving the model's distribution
toward a target P*, and their informal Theorem 4.1 states that failure-driven
construction makes the stage-2 gradient "better aligned with the target
gradient" than the gradient from the original distribution, so that one
stage-2 step "yields no larger target risk."[^f3] The theorem is stated
under a normalized gradient norm and the assumption that Q approximates P*.
The approximation is assumed, not measured, and the proof lives in an
appendix that I did not read.

The same resampling is carried into reinforcement learning. Stage-2 RLVR
draws prompts from the resampled distribution and gives reward 1 only when
the final answer is verified correct.[^f4] The paper says the RL proof
"follows a similar structure as failure-driven SFT," so the SFT argument is
the one carrying the weight.

Resampling has a built-in ceiling. It only redistributes mass over questions
the model already has, so it cannot supply what the model never learned. The
authors say so directly: "Failure resampling alone does not explicitly provide
missing knowledge."[^f5] That gap is what the retrieval-and-synthesis step in
[[failure-anchored-document-synthesis]] is meant to fill, and the second
stage mixes the two sources rather than using resampling alone.

## Limits

- The failure signal is a single bit per question: the verified final answer
  is wrong or it is not. It does not distinguish a model that is nearly right
  from one that is far off, and it cannot see a correct answer reached by
  luck. The paper uses only this binary form; whether a graded signal would
  do better is not tested here.
- The gain is not isolated. The conclusion credits "failure-driven
  post-training and complementary dynamic sampling" together, and says that
  their integration "leads to substantial improvements in reasoning
  performance."[^f6] I did not find in the read sections an ablation that
  turns resampling off while keeping everything else fixed.
- The evaluation pool used to detect failures is named as gold-standard
  benchmarks. Whether those benchmarks overlap with the ones reported
  afterwards is not established in what I read; my inference is that the
  overlap question has to be checked before reading the numbers as held-out.
- The theorem's assumption Q ≈ P* carries the whole argument. When the
  evaluation pool is a poor stand-in for the target, the weighting points
  at the wrong regions, and nothing in the method detects that.

## Related

- [[failure-anchored-document-synthesis]] — the step that adds knowledge the
  resampling cannot, and the source of most of the stage-2 data.
- [[learnability-posterior-curriculum]] — also steers a question generator
  toward the solver's capability boundary, but through posteriors over topics
  rather than a per-question error indicator.
- [[self-consistency-difficulty-score]] — a difficulty signal that needs no
  gold answer; the failure indicator above needs verified answers.
- [[response-length-difficulty-proxy]] — another difficulty proxy, used in the
  same pipeline for the first-stage data, not for the failure pass.

[^f1]: arxiv-2601-01562 — "which in our implementation is a binary indicator of verified incorrectness"
[^f2]: arxiv-2601-01562 — "which increases the sampling probability of regions where the current model performs poorly"
[^f3]: arxiv-2601-01562 — "better aligned with the target gradient, i.e.,"
[^f4]: arxiv-2601-01562 — "it follows a similar structure as failure-driven SFT, but only show the algorithm"
[^f5]: arxiv-2601-01562 — "Failure resampling alone does not explicitly provide missing knowledge"
[^f6]: arxiv-2601-01562 — "sampling leads to substantial improvements in reasoning performance"
