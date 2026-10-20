---
description: "An ensemble of RNN hypotheses picks the next experiment by ensemble disagreement (an EIG proxy), cutting behavioral experiments 5-10x versus random probing."
aliases: ["ATLAS", "Active Theory Learning for Automated Science"]
sources: ["elteto-2026"]
---
# ATLAS (Active Theory Learning for Automated Science)

> A closed loop that generates a diverse ensemble of mechanistic hypotheses
> and then designs the next experiment to make them disagree as much as
> possible — a measured answer to "which axis to probe next" when the
> [[possible-worlds|hypothesis space]] is a space of computational models, not a scalar
> parameter.

## Mechanism

Each cycle: a Hypothesis Generator fits an ensemble of Disentangled RNNs
(DisRNNs) to the data collected so far — a sparsity constraint of varying
strength keeps members qualitatively distinct rather than differing only in
initialization; an Experiment Optimizer searches binary experiment-design
matrices $D$ for the one maximizing an ensemble-disagreement score; an
Experiment Runner executes the winning design on the ground-truth agent and
appends the trajectory to the dataset. ATLAS iterates between generating
mechanistic hypotheses—instantiated as a diverse ensemble of sparse neural
networks (Disentangled RNNs)—and designing experiments that optimally
distinguish between them.[^c1]

The disagreement score is optimized by iterative bit-flip hill-climbing over
$D$ (128 random restarts, keeping the best on a held-out rollout batch). The
[[expected-information-gain|expected information gain (EIG)]] from an experiment design D is approximated
by the ensemble disagreement – that is, by how much more likely each model
considers its own trajectories compared to the trajectories of the other
models. Analogous to the BALD [27] objective, this score quantifies the
expected information gain about the true identity of the generative model
given the experimental outcome.[^c3]

Applied to recovering Q-learning and leaky actor-critic bandit agents from
behavior, ATLAS achieves a 5–10× improvement in sample efficiency across all
metrics compared to random experimentation, and its performance is further
validated against expert-designed experiments derived from literature.[^c2]

## Why it matters

For stall 2 (which axis first), ATLAS is an existence proof that the
score-then-pick move of [[bayesian-experimental-design]] survives being
applied to a *hypothesis space over computational models* rather than a
scalar parameter, once the hypotheses are instantiated as a literal ensemble
that can be simulated and scored. The resulting probes are not
recognisable hand-designed schedules: ATLAS-designed experiments often have
interpretable structure: they exhibit a combination of regular and
irregular structure on different timescales that make them effective at
uncovering behavior, but quite unlike what researchers tend to design.[^c4]

## Transfer

| | |
|---|---|
| **Home field** | active learning / Bayesian experiment design applied to reinforcement-learning agent identification in cognitive science |
| **Here** | any asking loop that must pick the next probe among questions distinguishing competing generative accounts of a process, not a single scalar unknown |
| **What survives** | the score-before-asking move — rank candidate probes by an EIG-shaped disagreement score before seeing the outcome — and the finding that a literal ensemble of structurally diverse candidate models makes that score computable without a hand-written likelihood over every hypothesis |
| **What does not** | the guarantee. The 5–10× figure is measured in silico, on a known, bounded family of RL-agent architectures — see Limits below for the source's own caveat about when random experiments can win. |

## Limits

- All results are in silico: a known ground-truth agent, a bounded family of
  RL-agent architectures, and simulated (not human or animal) experiments —
  no claim is made yet for real data collection.
- The disagreement score is only as good as the ensemble: as Rainforth et
  al. note (quoted in the source), "experiment design is only ever as good
  as the underlying model" — and the source itself observes that "complex
  ground-truth models and/or restrictive model classes sometimes result in
  situations where random experiments outperform those selected by active
  learning" — so if the hypothesis generator's models share a structural
  bias, their disagreement misses the true axis of uncertainty.[^c5]
- The bit-flip hill-climbing optimizer is a heuristic (128 restarts, no
  global-optimality guarantee) over a large discrete design space.

## Related

[[bayesian-experimental-design]] · [[expected-information-gain]] · [[adaptive-submodularity]] · [[generalized-binary-search]]

[^c1]: elteto-2026 — "ATLAS iterates between generating mechanistic hypotheses—instantiated as a diverse ensemble of sparse neural networks (Disentangled RNNs)—and designing experiments that optimally distinguish between them."
[^c2]: elteto-2026 — "ATLAS achieves a 5–10× improvement in sample efficiency across all metrics compared to random experimentation, and its performance is further validated against expert-designed experiments derived from literature."
[^c3]: elteto-2026 — "The expected information gain (EIG) from an experiment design D is approximated by the ensemble disagreement – that is, by how much more likely each model considers its own trajectories compared to the trajectories of the other models"
[^c4]: elteto-2026 — "ATLAS-designed experiments often have interpretable structure: they exhibit a combination of regular and irregular structure on different timescales that make them effective at uncovering behavior, but quite unlike what researchers tend to design."
[^c5]: elteto-2026 — "as Rainforth et al. [29] note, “experiment design is only ever as good as the underlying model.”"
