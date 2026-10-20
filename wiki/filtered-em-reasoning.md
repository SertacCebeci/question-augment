---
description: "Self-taught reasoning as filtered EM: sample rationale-answer pairs, keep only those with the correct answer, fine-tune on them; a Monte Carlo E-step with a reward-filtered gradient M-step."
aliases: ["filtered EM", "FEM", "filtered expectation maximization", "EM-based self-improvement"]
sources: ["arxiv-2512-20169"]
---
# Filtered EM for learning to reason

Rejection-based self-training has a common shape: sample rationale-answer
pairs from the current model, keep those whose answer is correct, and
fine-tune on what was kept. Read against a latent rationale
([[latent-rationale-variable]]), this is expectation maximisation with two
approximations. The E-step is an expectation over the posterior of the
rationale given the observed answer. The M-step maximises the expected
complete-data log-likelihood. The paper's own wording of the two steps is
"The E-step computes the expected complete data log-likelihood given the most
recent model parameter" and the M-step is "maximizing the expected complete
data log-likelihood."[^c1]

The approximations are the algorithm. The paper approximates the E-step "via
a single Monte Carlo sample," and the M-step "using a filtered gradient
update."[^c2] The gradient is weighted by a binary reward, one when the
sampled answer equals the correct one and zero otherwise, so incorrect
rationales contribute nothing. The authors call this filtered EM (FEM) and
describe it as "a filtered gradient update of the classic Monte-Carlo EM."[^c3]
The filter therefore plays the role of the posterior's support. The paper
argues that because the posterior is conditioned on the correct answer, any
draw from it must carry that answer, so "checking whether the generated
answer matches the ground truth is theoretically equivalent to enforcing the
posterior" support.[^c4] The paper adds that a broader proposal is admissible once a consistency
filter is applied: "applying a consistency filter ensures that the update"
touches only answer-consistent samples.[^c9]

The reading also links the method to supervised fine-tuning. The paper says
"each iteration of FEM can be viewed as an epoch in SFT," with the training
data resampled from the current model at each epoch.[^c5] A second reading
ties it to reward-weighted fine-tuning, where the model increases the
reward-weighted log-likelihood of its own samples.

What survives the transfer from statistics is the EM logic and the filter
as a correction. What does not survive is the exactness. The paper's bound
"is tight when" the proposal equals the question-only model, that is, the
proposal q(· | x, y ⋆ ; θ) equal to π(· | x; θ).[^c6] A
proposal that conditions on the answer is by construction not that model.
So the filter is not a free correction for the proposal's bias; the
distance between proposal and posterior is what the choice of sampler
controls, and that is the subject of [[rationale-sampling-distribution]].

## Limits

- The authors state that the approximations are "properly justified" but
  that "we have not formally analyzed FEM."[^c10] The EM reading is a
  reading of the update, not a convergence result.
- The Monte Carlo estimate uses one sample per question. The text says "For
  simplicity of exposition, we assume a batch size of 1,"[^c7] and reports no
  variance of the estimator. (my inference: a single draw per question makes
  the update noisy, and the effect of that noise is not measured here)
- The reward is binary and requires a known correct answer. Where the target
  is a graded rating or an open-ended answer, the filter has to be redefined,
  and the text does not show how the EM reading behaves under that change.
  (my inference)
- The experiments use Llama and Qwen models of 1.5B to 8B parameters, on two
  alignment tasks, for K = 5 iterations. The paper says "we plan to
  experiment with more complex tasks, such as math reasoning,"[^c8] so the
  method has not been tested where reasoning chains are most often studied.

## Related

- [[latent-rationale-variable]] — the latent model this update is run over
- [[rationale-sampling-distribution]] — the E-step sampler the paper finds decisive; the filter does not repair a poor one
- [[verification-weighted-voting]] — a soft tool-verification weight beats a hard filter there; here the filter is hard and binary, so the comparison is the same question in a different setting (my inference)
- [[rubric-guided-trajectory-filtration]] — also gates which self-generated trajectories enter fine-tuning, by a judge's terminal reward rather than an answer match
- [[double-confidence-filtering]] — another pre-training filter on self-generated labels, by a vote margin rather than correctness

[^c1]: arxiv-2512-20169 — "maximizing the expected complete data log-likelihood (M-step)"
[^c2]: arxiv-2512-20169 — "We approximate the Estep via a single Monte Carlo sample and the M-step"
[^c3]: arxiv-2512-20169 — "a filtered gradient update of the classic Monte-Carlo EM"
[^c4]: arxiv-2512-20169 — "checking whether the generated answer matches the ground truth is theoretically equivalent to enforcing the posterior"
[^c5]: arxiv-2512-20169 — "each iteration of FEM can be viewed as an epoch in SFT"
[^c6]: arxiv-2512-20169 — "is tight when"
[^c7]: arxiv-2512-20169 — "For simplicity of exposition, we assume a batch size of 1."
[^c8]: arxiv-2512-20169 — "we plan to experiment with more complex tasks, such as math reasoning"
[^c9]: arxiv-2512-20169 — "applying a consistency filter ensures that the update"
[^c10]: arxiv-2512-20169 — "we have not formally analyzed FEM"
