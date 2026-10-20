---
description: "Casting sequential experiment choice as a finite-horizon MDP and training a policy offline, so each next experiment is proposed from history without re-solving a design optimization online."
aliases: ["amortized sequential Bayesian optimal experimental design", "policy-gradient experimental design", "SBOED via PGRL"]
sources: ["arxiv-2601-05868"]
---
# Amortized sequential design policy

Sequential [[bayesian-experimental-design]] is hard because after each experiment the posterior becomes the next prior, so the choice must trade feedback against planning under future uncertainty. The work formulates this as a finite-horizon Markov decision process and learns a policy by policy-gradient reinforcement learning. Training happens offline. Once trained, the policy proposes each new experiment online from the experiment history, without repeatedly solving an optimization problem.[^c1]

## Mechanism

At each stage n the policy picks a design vector (sensor placements), data arrive, and the posterior is updated. The reward is information gain, here a Laplace-based D-optimality criterion; the authors note that other [[expected-information-gain]] utilities such as KL divergence fit the same framework.[^c2] Training needs many simulated episodes, so each reward must be cheap. Two devices make it so: a derivative-informed neural-operator surrogate that predicts both the solution and its Jacobian, and an evaluation strategy that computes posterior-covariance eigenvalues at a prior sample and treats that sample as a stand-in for the maximum a posteriori point. This avoids a MAP solve inside every environment step.[^c3]

The proxy was checked on 5 prior parameter fields and 200 sensor placements: relative RMSE 0.44% and correlation 0.99 against the standard solve-MAP-first computation.[^c4] The authors attribute this to the MAP estimates having spatial structure similar to the prior sample, so local curvature is similar (their qualitative argument, from figures).

## What was measured

On contaminant source tracking with sequential multi-sensor placement, the surrogate workflow gave about 100x speedup over a finite element baseline, and the learned policy beat random designs with a win rate above 97%.[^c5] The 100x figure is mostly from eigenvalue computation (0.14 s versus 13.46 s); MAP acceleration by the surrogate was small (5.65 s versus 8.93 s).[^c6]

The policy was also interpretable: sensors moved upstream against the flow, which the authors explain as reducing diffusive blurring. With the velocity field reversed, the retrained policy moved sensors in the new upstream direction, evidence that it encoded the transport physics.[^c7]

## Limits

- Amortization shifts cost: the offline training and surrogate construction are paid up front; the break-even against online optimization was not established in the text I read.
- Comparison is against random placement, not against greedy or lookahead designs, so whether the policy beats a myopic baseline is not shown here (my reading of the baselines reported).
- The reward depends on a Laplace/Gaussian approximation and a prior-as-MAP proxy validated on one problem class; the authors list non-Gaussian priors and likelihoods and nonlinear multiphysics as future work.[^c8]
- Nothing here concerns natural-language questions; the transfer to a questioner with no likelihood is my inference. What plausibly carries is the idea of learning a history-conditioned choice rule offline rather than re-ranking candidates each turn. The Jacobian, Hessian and D-optimality machinery does not carry without a parametric model.

## Related

- [[bayesian-experimental-design]] — the framework whose sequential case this amortizes
- [[expected-information-gain]] — the utility; here replaced by a Laplace D-optimality proxy
- [[adaptive-submodularity]] — a guarantee for greedy sequential selection; this work gives no such guarantee
- [[value-of-information]] — the decision-theoretic alternative to information-gain rewards

[^c1]: arxiv-2601-05868 — "once trained, it proposes new experiments online without repeatedly solving an SBOED optimization problem"
[^c2]: arxiv-2601-05868 — "other expected-information-gain utilities such as KL divergence can also be used within the same framework"
[^c3]: arxiv-2601-05868 — "thereby avoiding expensive iterative MAP optimization inside the RL environment while retaining accurate information-gain estimates"
[^c4]: arxiv-2601-05868 — "The relative RMSE and correlation across all test cases are 0.44% and 0.99, respectively"
[^c5]: arxiv-2601-05868 — "the learned sensor-placement policy consistently outperformed random designs (win rate > 97%)"
[^c6]: arxiv-2601-05868 — "which takes only 0.14 seconds compared to 13.46 seconds using FEM, about 100× speedup"
[^c7]: arxiv-2601-05868 — "the policy adapts accordingly, shifting sensors in the new upstream direction"
[^c8]: arxiv-2601-05868 — "Future work includes extending the approach to more complex nonlinear and multiphysics models, non-Gaussian priors and likelihoods"
