---
description: "Splits total search uncertainty into independent spatial and semantic entropy, then picks the next action by a tunable weighted sum of their expected information gains."
aliases: ["spatial-semantic EIG", "spatial-semantic expected information gain"]
sources: ["srivastava-2026"]
---
# Spatial-semantic EIG decomposition

> When a search agent must both find candidates and tell which one is the
> target, split "which axis first" into two named axes and let a weight
> decide how much of each question to ask.

## Definition / Mechanism

A robot searching for a described target faces two different unknowns: where
candidate objects are (spatial) and which discovered candidate is the target
(semantic identity). Because candidate placement is modelled as independent
of target identity, the joint [[entropy]] factors additively: $H(M, C^\star) =
H(M) + H(C^\star)$, so the two axes can be tracked as separate beliefs
instead of one conflated uncertainty.[^c1]

For each candidate path $\tau$, the [[planner-dynamic-stopping|planner]] computes an [[expected-information-gain|EIG]]
for each axis separately — $I^{sp}_t(\tau)$ over occupancy, $I^{sem}_t(\tau)$
over a global target-identity posterior built from calibrated
vision-language-model (VLM) evidence — and selects the path maximising a
weighted sum: $\tau_t^\star = \arg\max_\tau [\alpha I_t^{sp}(\tau) + \beta
I_t^{sem}(\tau)]$, with $\alpha,\beta \geq 0$ set by the operator to trade
broader exploration against earlier identification.[^c2]

## Why it matters

This is a concrete answer to "which axis first" when the axes are not
interchangeable in kind: rather than forcing one EIG over a merged
[[possible-worlds|hypothesis space]], the two entropies are computed and combined after the
fact, so the trade-off is an explicit, tunable knob instead of an artifact
of how the state space was built.

Emphasising the semantic axis measurably changes agent behaviour: as
semantic weight increases from Pure-Spatial ($\alpha=1,\beta=0$) to
Pure-Identity ($\alpha=0,\beta=1$), the mean number of candidates
discovered before commitment drops from 8.0 to 6.0 and mean VLM queries
drop from 16.2 to 12.9, with comparable identification accuracy once a
decision is reached.[^c3]

Any weighting that uses semantic EIG at all reaches a confident decision
far more often than undirected search: EIG-based planners converge in
75.0%–92.5% of trials against 20.0% for random search and 72.7% for
deterministic coverage.[^c4]

## Transfer

| | |
|---|---|
| **Home field** | [[bayesian-experimental-design|Bayesian experimental design]]: [[expected-information-gain]] as a single selection criterion over one hypothesis space |
| **Here** | embodied VLM-based search: the hypothesis space is split into two independent axes (location, identity), each scored by its own EIG |
| **What survives** | the greedy, before-answering EIG scoring logic, and the additive entropy decomposition wherever the axes are genuinely independent |
| **What does not** | any optimality guarantee for the combination — $\alpha,\beta$ are hand-set constants, not derived from a task utility or bounded the way [[adaptive-submodularity]] bounds [[generalized-binary-search|greedy EIG]] on one axis |

## Limits

- The decomposition's additivity rests on candidate placement being
  independent of target identity ($p(M,C^\star)=p(M)p(C^\star)$) — see
  ## Definition / Mechanism; it does not hold where location correlates
  with identity.
- The total candidate count $N$ is assumed known a priori; only locations
  are discovered incrementally — an open, unbounded candidate set is out of
  scope for this formulation.
- Evaluated only in a controlled synthetic 20×20-grid environment with
  GPT-4o-mini as the VLM, not on physical robots.
- $\alpha,\beta$ are fixed per run, not adapted online, so the "trade-off"
  is a designer choice, not a learned or task-derived weighting.

## Related

[[expected-information-gain]] · [[mutual-information]] · [[adaptive-submodularity]] · [[value-of-information]]

[^c1]: srivastava-2026 — "Since candidate placement is independent of target identity, p(M, C ⋆ ) = p(M)p(C ⋆ ), (4) which yields the additive decomposition H(M, C ⋆ ) = H(M) + H(C ⋆ )."
[^c2]: srivastava-2026 — "τt⋆ = arg max [α Itsp (τ ) + β Itsem (τ )] , τ ∈T (rt ) (15) where α, β ≥ 0 determine the relative emphasis on spatial exploration and semantic target identification."
[^c3]: srivastava-2026 — "the mean number of candidates discovered before commitment decreases from 8.0 for pure Spatial-EIG to 6.0 for Pure-Identity, and the mean number of VLM queries decreases from 16.2 to 12.9"
[^c4]: srivastava-2026 — "EIG-based planners reach a confident decision in 75.0%–92.5% of trials, compared with 20.0% for Random and 72.7% for Coverage."
