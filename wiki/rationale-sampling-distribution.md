---
description: "The rationale proposal, not the number of kept samples, sets how much self-taught learning gains; rationales conditioned on the correct answer beat rejection sampling and STaR in two tasks."
aliases: ["rationale proposal distribution", "E-step sampling distribution", "rationalization sampling", "rationale sampling scheme"]
sources: ["arxiv-2512-20169"]
---
# Rationale sampling distribution

In the filtered-EM view ([[filtered-em-reasoning]]) the E-step needs
rationales drawn from the posterior given the correct answer, and that
posterior cannot be sampled exactly. The method draws instead from a
proposal q(z, ŷ | x, y*) built from the current model. The paper names
what the proposal must do, and the two requirements pull in different
directions. The answer should be correct often enough that many pairs
survive the filter. The rationales should also be good enough that
conditioning on them improves answers to new questions. The paper's thesis
is that the main challenge lies in "designing a sampling distribution of
rationales that justify correct answers."[^c1] A proposal that maximises
acceptance can lose the second requirement while meeting the first.

Three schemes are compared. Rejection sampling with a budget draws from the
question-conditioned model and keeps the correct samples. STaR chains a
rejection step with a second stage that samples when the correct answer is
given as a hint. Prompt posterior sampling (PPS) keeps only that second
stage, "which only keeps the rationalization stage of STaR that conditions
on the correct answer in the prompt."[^c2] The mechanism is simple. Because
the model is conditioned on the answer, it is likely to produce it, which
raises the fraction of accepted pairs.[^c3] The paper notes that this does
not guarantee the answer is correct, and it creates a gap: during training
the rationale is produced with the answer in view, at test time the answer is
not given.[^c4] The gap is the price of the higher acceptance rate, and the
method accepts it.

The results separate acceptance from quality. STaR accepts more pairs per
iteration than either component, but "the increased quantity does not
necessarily translate into quality."[^c5] PPS outperforms the baselines
across all iterations, which the authors attribute to "generating superior
rationales."[^c6] Its accuracy was reached with less training data than
STaR, and its rationales were longer, about 130 words against under 120
for STaR. The authors conclude the gain is "driven by the quality of
reasoning," not by data quantity.[^c7] The scheme is therefore a claim about
where a self-taught learner's gain comes from: the sampler, more than the
number of samples it keeps.

## Limits

- The paper itself says that "we establish that the sampling distribution is
  an important domain-specific hyperparameter."[^c8] A proposal that wins
  on judge calibration and summary feedback is not shown to win elsewhere.
- The tasks are two human-rating alignment tasks, where the "correct answer"
  is a human score. Math reasoning, which the paper names as future work,
  was not tested.[^c9]
- Quality is read from accuracy and from the length of the rationale. In the
  text I read, no independent rating of rationale quality is reported, so
  "quality" is inferred from outcomes. (my inference)
- A rationale conditioned on the answer may be a justification of that answer
  rather than a route to it. Work on answers placed in a prompt as hints
  finds that models follow such hints while rarely acknowledging them, so the
  PPS gap may be a form of this. The paper does not test it. (my inference)
- The train-test gap is named but not measured in the text I read. How much
  of the accuracy gain survives when the answer is withheld at sampling time
  is open. (my inference)

## Related

- [[filtered-em-reasoning]] — the update into which these proposals plug as the E-step sampler
- [[latent-rationale-variable]] — the posterior over rationales that a proposal stands in for
- [[hint-adherence-without-acknowledgement]] — an answer placed in the prompt is followed even when wrong; the same lever that makes PPS answer-consistent is one that can be followed without acknowledgement (my inference of the link)
- [[soft-versus-hard-privileged-information]] — conditioning a sampler on the correct answer is a use of information the learner lacks at test time, which that note treats as a constraint on valid continuations (my inference of the link)

[^c1]: arxiv-2512-20169 — "the main challenge lies in designing a sampling distribution of rationales that justify correct answers"
[^c2]: arxiv-2512-20169 — "which only keeps the rationalization stage of STaR that conditions on the correct answer in the prompt"
[^c3]: arxiv-2512-20169 — "because the correct answer is conditioned on, the model is likely to generate it and in this way increase the fraction of accepted rationale-answer pairs"
[^c4]: arxiv-2512-20169 — "This also introduces a mismatch between training and testing."
[^c5]: arxiv-2512-20169 — "the increased quantity does not necessarily translate into quality"
[^c6]: arxiv-2512-20169 — "PPS outperforms all baselines across all FEM iterations, which we attribute to"
[^c7]: arxiv-2512-20169 — "Instead, it is driven by the quality of reasoning."
[^c8]: arxiv-2512-20169 — "the sampling distribution is an important domain-specific hyperparameter"
[^c9]: arxiv-2512-20169 — "we plan to experiment with more complex tasks, such as math reasoning"
