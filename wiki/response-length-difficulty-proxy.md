---
description: "A teacher model's response token length is the difficulty proxy for stratified sampling; it beat annotated education level, yet sampling on length alone degraded elementary reasoning."
aliases: ["length-based difficulty proxy", "token-length stratified sampling", "response length as question difficulty"]
sources: ["arxiv-2601-01562"]
---
# Response length as a difficulty proxy

Large reasoning corpora are too big to train on whole, so they have to be
sampled, and a sampler needs a difficulty score per question. One cheap
score is the length of the answer a strong model writes to the question: a
question that needs a long chain of reasoning is treated as a hard one. The
Logics-STEM pipeline uses this as its difficulty measure for weighted
stratified sampling on STEM data, stating that "token length of the response
is adopted as a natural and effective proxy for question
difficulty."[^l1] The length is that of the response a teacher model
generates, not of any answer the student produces.

The choice was tested against the obvious alternative. The authors compared
two ways of stratifying the same pool: by the token length of the teacher's
response, and by the annotated education level of the question. Their
conclusion is that "the former serves as a natural and more effective proxy
for question difficulty."[^l2] So the length signal, which costs nothing but
a generation the pipeline already has, beat a label that is a human or model
judgment about the question itself.

The proxy has a cost when used alone. The authors sampled 200K records under
each strategy and trained for one epoch. Length-only sampling gave gains on
AIME2024, AIME2025 and HMMT2025, but "incurs significant performance drops on
MATH500, MMLU-Pro-Math, and GPQA-Diamond."[^l3] The authors read this as
catastrophic forgetting of elementary reasoning, and so the adopted recipe is
stratified by length, scaled up, to strengthen the advanced reasoning while
keeping the basic. In my reading, length decides how the pool is split into
strata, and the strata are then weighted, rather than length deciding alone
which questions survive.

What transfers from this is a narrow claim. Long answers mark questions that
need more steps, which is a signal of how much reasoning a question demands.
It does not mark how much a particular model struggles with it. A question
can be long to answer and easy for the model, and a short one can be hard
for it. The paper measures difficulty only as a property of the data, which
is why the same signal can improve the distribution's coverage of advanced
problems and still erode the basics.

## Limits

- The comparison is against one alternative, the annotated education level.
  The text does not test length against a solver-based difficulty measure, so
  whether length is a better proxy than model-specific difficulty is not
  established here.
- The ablation used a 200K-record subset, one epoch, and the Qwen3-8B model
  (the caption of the sampling table names it). Whether the ranking holds at
  full scale or for other bases is not shown.
- Response length depends on the teacher model and on how it was prompted.
  The teacher used is not named in the text I read; the footnotes point to
  Qwen3-235B models. My inference is that a different teacher would reorder
  the strata; this was not tested.
- Length is confounded with verbosity and with style. The text does not
  separate a question that needs many steps from a question that elicits a
  wordy answer, so the proxy may partly track the teacher's habits.
- The stratification was adopted for the final recipe, but the paper does not
  report a standalone measure of how much of the final gain comes from length
  as opposed to the other filters and sampling steps.

## Related

- [[self-consistency-difficulty-score]] — the solver's own answer agreement as
  a difficulty signal; it measures the model's uncertainty rather than the
  length of a teacher's output.
- [[failure-driven-query-resampling]] — a difficulty signal from the model's
  verified errors on gold-standard tasks, used for second-stage training
  rather than for the first-stage sampling.
- [[moderate-adaptive-reasoning-length]] — length as a control on reasoning
  effort at inference, where longer is not uniformly better; here length is
  read as a property of the question instead.

[^l1]: arxiv-2601-01562 — "natural and effective proxy for question difficulty"
[^l2]: arxiv-2601-01562 — "the former serves as a natural and more effective proxy for question difficulty"
[^l3]: arxiv-2601-01562 — "incurs significant performance drops on MATH500, MMLU-Pro-Math, and GPQA-Diamond"
