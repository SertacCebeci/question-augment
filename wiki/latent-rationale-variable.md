---
description: "Treating the reasoning trace as a latent variable makes the correct answer likelier given the rationale than given the question alone, so learning to reason becomes inference over rationales."
aliases: ["latent rationale", "rationale as latent variable", "latent reasoning variable", "reasoning as a latent variable model"]
sources: ["arxiv-2512-20169"]
---
# Latent rationale variable

Put a rationale z between a question x and its correct answer y*. The
predictive structure then factors through z: "With the rationale, the
predictive structure factors as a latent variable model (LVM)." The
rationale is an intermediate reasoning process that is never observed in
the data, only the question and the answer are. The reason to introduce it
is stated in one sentence: conditioned on both the question and the
rationale, the model has a much higher chance of generating the correct
answer than when conditioned on the question alone.[^c1] The mechanism is
therefore a decomposition. Learning x to y* directly is hard when the task
is complex; learning x to z and then z to y* is easier, and the latent z
carries the part of the computation that the observed pair leaves out.

The decomposition has a cost that falls on learning, not on the model's
use. Fitting such a model by maximum likelihood requires the posterior over
rationales given the observed correct answer, and that posterior is the
quantity an expectation-maximisation algorithm needs in its E-step. The
paper says it has no closed form: "The expectation does not have a closed
form, and approximating it via Monte Carlo sampling requires sampling from
the exact posterior."[^c2] The M-step has no closed form either and is
"typically approximated by gradient-based optimization."[^c3] The paper
concludes that neither step can be implemented exactly in LLMs.[^c4]
So the latent view does not hand the learner a rationale. It names the
distribution a good rationale should come from, and leaves open how to
sample from it. That open choice is the subject of
[[rationale-sampling-distribution]], and the EM update that uses it is in
[[filtered-em-reasoning]].

What the transfer from statistics keeps is the factorisation and the EM
logic. What it does not keep is any claim that the latent is the model's
faithful reasoning. In this formalism z is defined by its role in the
likelihood: it is whatever makes the observed answer more probable. Nothing
in the construction says the sampled rationale describes the computation
that produced the answer. (my inference)

## Limits

- The "much higher chance" is offered in words, as the motivation for the
  model. The paper does not bound the gain from conditioning on z, and the
  empirical results come from a different setting (judge calibration and
  summary feedback), not from a measurement of this gap.
- The latent is identified only through the answer. Where no correct answer
  is known, the posterior the formalism needs is not defined. (my inference)
- The paper's approximations are "properly justified", but the authors say
  they have not analysed the resulting algorithm formally; see
  [[filtered-em-reasoning]].
- The model's claim concerns single-answer tasks with a checkable target.
  Open-ended tasks with graded or unverifiable answers are not covered by
  the text I read.

## Related

- [[filtered-em-reasoning]] — the EM update that treats z as latent and
  approximates its E-step by a filtered sample
- [[rationale-sampling-distribution]] — which proposal stands in for the
  posterior over z, and why the choice matters more than sample count
- [[trace-conditioned-answer-consistency]] — also conditions on a reasoning
  trace, but to score an answer's stability, not to learn from the trace
- [[reasoning-trace-behavioral-transfer]] — fine-tuning on traces shifts
  behaviour; the latent view is what makes a trace a training target
  (my inference)

[^c1]: arxiv-2512-20169 — "conditioned on both the question x and rationale z, the model has a much higher chance of generating the correct answer"
[^c2]: arxiv-2512-20169 — "The expectation does not have a closed form, and approximating it via Monte Carlo sampling requires sampling from the exact posterior."
[^c3]: arxiv-2512-20169 — "The M-step also lacks a closed-form solution and is typically approximated by gradient-based optimization"
[^c4]: arxiv-2512-20169 — "Neither of the steps can be implemented exactly in LLMs."
