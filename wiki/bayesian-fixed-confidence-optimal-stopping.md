---
description: "Bayesian fixed-confidence questioning reduces, via a Lagrange multiplier, to optimal stopping where stopping is one more action; the best answer is the posterior-most-likely epsilon-optimal point."
aliases: ["Bayesian fixed-confidence pure exploration", "stopping as an absorbing action", "C-ICPE", "in-context pure exploration"]
sources: ["arxiv-2602-17976"]
---
# Bayesian fixed-confidence optimal stopping

A learner asks queries A_t, sees noisy answers, and must stop and return a recommendation x that is epsilon-optimal (loss L_theta(x) <= epsilon) for a latent task theta drawn from a prior. The goal is to minimize the expected number of queries subject to success probability at least 1 - delta, averaged over the prior.[^c1] The learner is a triple: a sampling policy, a stopping time, and an inference rule.[^c2]

**Posterior success.** What matters at any history h is q_t(h,x), the posterior probability that x is epsilon-optimal, and r_t(h), its maximum over x. An optimal inference rule returns the argmax of q_t.[^c3]

**Lagrangian reduction.** A multiplier lambda on the correctness constraint turns the problem into maximizing lambda times the terminal success probability minus the number of queries. Stopping can be embedded as an absorbing action a_stop, so the fixed-lambda problem is optimal-stopping control over the actions plus "stop".[^c4]

**Bellman structure.** The value of a history is the max of stopping (worth lambda r_t(h)) and the best continuation (cost 1 plus expected next value under the posterior predictive). A deterministic greedy policy is optimal: stop when stopping is worth at least the best continuation, otherwise take the best query.[^c5] The paper says that over continuous actions, attainment of the supremum needs a semicontinuity argument and does not follow from the finite case.[^c6]

**Exactness of the relaxation.** With time-sharing (randomizing between two policies is allowed) and strict feasibility, the duality gap is zero. If a closedness condition holds on the near-optimal set of cost-success pairs, some dual-optimal policy is primal optimal and meets the 1 - delta guarantee.[^c7] This weakens an earlier uniqueness assumption for the finite case.[^c8]

**Learned version.** C-ICPE meta-trains sequential networks over the task prior to learn exploration, stopping and recommendation jointly, and at test time gathers evidence with no parameter updates.[^c9] The recommendation is the mean of a learned Gaussian over the optimum, a moment projection of the posterior, hence only an approximation of the argmax of q_t; the paper shows it is near-optimal when posterior uncertainty is small relative to the epsilon margin.[^c10] The framework covers cases where the answer space differs from the query space, such as returning an optimal value.[^c11]

My inference: the same split applies to any asker, namely a rule for what to ask next and a separate price on being wrong that decides when to stop. The price lambda, not a fixed budget, sets how long to keep asking.

## Limits

I read the introduction, setting and theorem statements, not the appendix proofs or most experiments. The guarantees hold in expectation under the prior, not per task, and need regularity, time-sharing and closedness assumptions the paper states but does not verify for the learned networks. The deployed Gaussian recommendation is justified most directly for localization losses. Transfer to open-ended human question asking is untested; the tasks are noisy binary search, bandits on a sphere, Ackley minimization, Gaussian-process value estimation and a soil-copper task.

## Related

- [[exploration-certification-trade-off]] — frequentist fixed-confidence cost split into finding and confirming
- [[pac-best-arm-sample-complexity-lower-bound]] — the finite-arm frequentist lower bound this Bayesian setting contrasts with
- [[plug-in-glr-stopping-rule]] — a model-specific stopping rule; here stopping is learned
- [[active-testing]] — the sequential hypothesis-testing setting
- [[odds-theorem]] — another optimal-stopping result

[^c1]: arxiv-2602-17976 — "Pπθ∼ν (x̂τ ∈ Xϵ (θ)) ≥ 1 − δ. (1)"
[^c2]: arxiv-2602-17976 — "A learner is defined by the triplet"
[^c3]: arxiv-2602-17976 — "an optimal inference rule is any"
[^c4]: arxiv-2602-17976 — "Stopping can also be embedded as an"
[^c5]: arxiv-2602-17976 — "Theorem 3.1 (Bellman equation and greedy deterministic"
[^c6]: arxiv-2602-17976 — "the continuous setting requires verifying that the"
[^c7]: arxiv-2602-17976 — "Theorem 3.2 (Zero duality gap and (ϵ, δ)-correctness)."
[^c8]: arxiv-2602-17976 — "we replace the"
[^c9]: arxiv-2602-17976 — "At inference time, it actively gathers evidence on tasks and identifies an"
[^c10]: arxiv-2602-17976 — "than as an exact maximizer of qt ."
[^c11]: arxiv-2602-17976 — "include optimal-value identification, where the learner"
