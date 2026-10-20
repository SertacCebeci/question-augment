---
description: "An embodied probing reward scoring an agent's action by the mutual information it would gain about a partner's hidden preference, discounted by a situational listening affordance."
aliases: ["inquiry reward", "Pride-Inquiry inquiry term"]
sources: ["li-2026-pride"]
---
# Affordance-gated inquiry reward

> A driving agent's reward for actively probing a partner's hidden intent —
> scored as mutual information, but only paid out when the situation makes
> listening worthwhile.

## Definition / Mechanism

Li, Xu & Feng model a lane-changing vehicle ("ego") that must infer another
vehicle's ("object") hidden, unyielding preference before committing. They
define **inquiry** as the reward component for actions that reduce that
uncertainty. "Inquiry is proposed for expected prejudice correction in
communication. It measures the ego's ability to actively probe for
knowledge about the object's perseverance."[^c1]

Concretely, inquiry is the mutual information between the object's realized
trajectory distribution and its hidden preference parameter, conditioned on
the ego's own hidden preference, computed as a [[kl-divergence|KL divergence]] between the
trajectory-conditioned posterior and the prior over hypotheses (their Eq.
25). Unlike a plain mutual-information score, the term is multiplied by a
**[[communication-affordance|listening affordance]]** before it counts toward the reward. "The listening
affordance $C_{LI}$ describes how much the ego needs to listen. The model
is also constructed with safety parameters $C_{CF}$ and $C_{LC}$, while
being influenced by the incentive factor as well."[^c2]

The whole reward is folded into a hierarchical multi-agent inverse-RL fit
(C-MIRL) against naturalistic trajectories.

## Why it matters

This is a concrete, embodied instance of "which axis to probe first":
instead of a free-standing query, the probe *is* the agent's own physical
action (a trajectory), and the criterion combines an information term with
a physical-context gate rather than information alone.

## Transfer

| | |
|---|---|
| **Home field** | information theory / [[bayesian-experimental-design|Bayesian experimental design]]: mutual information between a latent state and an observation, maximised over a design (see [[mutual-information]], [[expected-information-gain]]) |
| **Here** | mutual information between a partner's hidden preference and its observed future trajectory, under a two-agent Bayesian-persuasion driving game |
| **What survives** | the core selection logic — score a probing action by the posterior contraction it induces about the unknown, exactly as EIG scores a query |
| **What does not** | task-independence: the reward is multiplied by a hand-built, driving-specific affordance term, so "worth probing" is not read off [[surprisal|information content]] alone, and no optimality or regret bound is proved for the combined score — only an empirical [[calibration]] |

## Limits

- Calibrated on one dataset, one metric. "Verified on the NGSIM dataset
  with C-MIRL, the training results for the mandatory-lane-change driver
  behavior model are improved by 19.908%, while the testing results are
  improved by 14.694%."[^c3]
- That figure is against the paper's own non-communicative calibration
  baseline, not against a plain-mutual-information (ungated) ablation, so
  how much of the gain is the affordance gate versus the information term
  alone is not isolated.
- The model assumes a level-k Bayesian-persuasion game, a discretized
  (histogram) [[possible-worlds|hypothesis space]] over the hidden preference, and a Boltzmann
  noisily-rational trajectory-choice model with rationality fixed at
  $\beta=1$ — not a general-purpose active-inquiry criterion.
- The inquiry term itself is left unnormalized (unlike the paired pride
  term, which is scaled to $[0,1]$), so it cannot be compared in scale to
  other reward terms without further calibration.

## Related

[[mutual-information]] · [[expected-information-gain]] · [[value-of-information]]

[^c1]: li-2026-pride
[^c2]: li-2026-pride
[^c3]: li-2026-pride — "Verified on the NGSIM dataset with C-MIRL, the training results for the mandatory-lane-change driver behavior model are improved by 19.908%, while the testing results are improved by 14.694%."
