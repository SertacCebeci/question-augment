---
description: "The gradient of the pass@k objective is the pass@1 gradient times a per-prompt scalar k(1−p)^(k−1), so it adds no new direction and vanishes where the model always or never succeeds."
aliases: ["pass@k objective", "pass@k as a surrogate objective", "pass@k scaling factor", "pass@k as a reward"]
sources: ["arxiv-2511-16231"]
---
# Pass@k gradient reweighting

Pass@k scores a prompt by the chance that at least one of k independent samples is correct. Used as a training target rather than as a score, it turns out not to point the policy anywhere new. For one fixed prompt, the chain rule gives the pass@k gradient as the pass@1 gradient times a positive scalar. With p the single-sample success probability, that scalar is k(1−p)^(k−1). The paper's reading is that "optimizing pass@k does not introduce a new search direction in"[^p1] the parameter space: "Instead, it dynamically reweights the standard pass@1 gradient"[^p2] according to how well the model already does on that prompt.

The arithmetic is short. Pass@k is 1 − (1−p)^k, and its derivative in p is k(1−p)^(k−1). Within a prompt, a pass@k update therefore moves in the same direction as the pass@1 update; only its length changes. The length is large where p is small, reaching k as p goes to 0, and it falls to 0 as p goes to 1. The paper reads these two ends as the two situations that matter. At low p the weight is at its largest, and the paper says the gradient "should be amplified."[^p3] At high p the objective saturates: "The objective saturates, and the learning signal vanishes."[^p4]

The low-p end is where the mechanism fails in practice. The pass@1 gradient is itself estimated from samples (the paper names REINFORCE), and if no sampled trajectory is correct the estimate is zero whatever the weight. The paper says so directly: "the empirical gradient estimate is zero", and the pass@k objective "fails to provide a learning signal exactly when" the model needs it most.[^p5] So the factor k multiplies a quantity that the sampler often cannot see.

The paper draws two conclusions from this. The first is that pass@k should not be the direct training objective. Its analysis of "using pass@k as a surrogate objective for standard policy gradient methods" finds that the gradient of the expected pass@k "is strictly collinear with that of" pass@1, so it carries no separate direction for the optimiser to follow.[^p6] The second is that high pass@k is better read as an outcome than as a cause: "high pass@k is a downstream consequence of effective exploration."[^p7] The paper therefore keeps pass@k as a measure, "as an inference-time diagnostic," and asks for training mechanisms that act on exploration directly.[^p8]

Methods that try to optimise pass@k anyway differ in one respect the paper singles out. Those that treat the k samples jointly do not inherit the independence of the single-sample reweighting. The paper cites one such line as deriving "estimators for the pass@k gradient that consider the set of k samples jointly."[^p9] That work is not read here.

## Limits

- The per-example relation is proved for a fixed input x. Over a dataset, the batch gradient is a sum of per-prompt pass@1 gradients with different weights α_k(x, θ). Equal directions per prompt do not make the summed direction equal to the pass@1 direction unless the weights agree. The conclusion's "strictly collinear" statement for the expected objective is therefore stronger than the per-prompt result as stated, and I read it as the paper's claim, not a checked step (my reading).
- The paper calls itself "primarily a theoretical analysis of optimization objectives in reinforcement learning for LLMs."[^p10] The text read contains no experiment that trains with pass@k and measures the reweighting's effect.
- The analysis treats the k samples as independent draws from one policy. It does not cover joint estimators of the kind the paper cites, and it does not cover the zero-signal case under a sampler that is more or less exploratory than the one assumed.
- The scalar's range is [0, k], reaching k at p = 0. For k = 1 the scalar is 1 for every p, so pass@1 is the case with no reweighting (my arithmetic from the formula). The text does not discuss intermediate k beyond the formula.
- The "vanishes at p near 1" statement is about the expected gradient. A finite batch can still show a non-zero sample gradient on a prompt with p near 1, because the sampled wrong answers contribute terms; the analysis does not account for that finite-sample effect (my inference).

## Related

- [[rlvr-entropy-collapse]] — the same RLVR setting; the collapse of the sampling distribution is what pass@k depends on, and the paper's gap argument is recorded there
- [[edge-of-competence-selection]] — reads the same pass@k curve to choose prompts; the zero-signal and saturated regimes here match its "no correct trajectory" and "already solved" regimes (my reading)
- [[selection-reinforcement-bias]] — a separate account of RL narrowing the correct set toward high base-probability answers, not a gradient reweighting
- [[candidate-selection-gap]] — the pass@K versus pass@1 gap as measured across a candidate pool at inference, a different object from a training gradient

[^p1]: arxiv-2511-16231 — "optimizing pass@k does not introduce a new search direction in"
[^p2]: arxiv-2511-16231 — "Instead, it dynamically reweights the standard pass@1 gradient"
[^p3]: arxiv-2511-16231 — "Theoretically, the gradient signal should be amplified"
[^p4]: arxiv-2511-16231 — "The objective saturates, and the learning signal vanishes."
[^p5]: arxiv-2511-16231 — "empirical gradient estimate is zero"
[^p6]: arxiv-2511-16231 — "the gradient of the expected pass@k is strictly collinear with that of"
[^p7]: arxiv-2511-16231 — "high pass@k is a downstream consequence of effective exploration"
[^p8]: arxiv-2511-16231 — "we advocate for retaining pass@k as an inference-time diagnostic"
[^p9]: arxiv-2511-16231 — "estimators for the pass@k gradient that consider the set of k samples jointly"
[^p10]: arxiv-2511-16231 — "This work is primarily a theoretical analysis of optimization objectives in reinforcement learning for LLMs"
