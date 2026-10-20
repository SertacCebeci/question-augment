---
description: "Situational safety and incentive conditions that gate how much communicative effort (expression or listening) an embodied agent should invest, independent of the information content on offer."
aliases: ["expression affordance", "listening affordance"]
sources: ["li-2026-pride"]
---
# Communication affordance

> Whether it is worth expressing intent or listening for it is a function of
> the physical situation, not of the information available — a gate applied
> before any information term is scored.

## Definition / Mechanism

Li, Xu & Feng model two gating terms for a lane-changing vehicle's
communication rewards. The **listening affordance** scales how much the ego
should invest in probing a partner's hidden intent. "The listening
affordance $C_{LI}$ describes how much the ego needs to listen. The model
is also constructed with safety parameters $C_{CF}$ and $C_{LC}$, while
being influenced by the incentive factor as well."[^c1]

Its direction is stated explicitly: "with more desperation for incentives
comes less listening motive... the longitudinal advantage leads to better
listening quality, while lateral achievement may lead to a certain future
with less need to listen."[^c2]

The **expression affordance** is the mirror term for how legible the ego
should make its own intent to the other vehicle. "The expression affordance
$C_{EX}$ describes how much the object would like to listen at the end of
the trajectory selected. It integrates the two parts of safety conditions
$C_{CF}$ and $C_{LC}$ differently."[^c3]

Both terms multiply the corresponding communication reward (inquiry or
pride) rather than replacing it, so they act as a situational discount on
an information-theoretic score computed separately.

## Why it matters

On the selection stall, this is a second factor besides information
content: an axis can be maximally informative to probe and still not worth
probing if the situation (safety margin, incentive to act) does not afford
it. "We also model communication affordances as adaptive preferences shaped
by environmental conditions, and validate the framework with naturalistic
driving data and DIL experiments."[^c4]

## Transfer

| | |
|---|---|
| **Home field** | the paper attributes the term "affordance" to earlier work on environment-perception (its own citation, not independently verified here) — a property of the environment that supports or invites an action |
| **Here** | two scalar multipliers built from lane-change safety margins (distances to leading/following vehicles) and an IDM-style speed-incentive ratio |
| **What survives** | the qualitative idea that communicative effort should be gated by what the current situation supports, not by information content alone |
| **What does not** | generality: the gating formulas are specific to two-vehicle longitudinal/lateral lane-change geometry, with no claim to transfer to another interaction domain without redefining what "safety" and "incentive" mean there |

## Limits

- The affordance functions are hand-designed, not learned; they are
  calibrated only indirectly, through the downstream inverse-RL fit to
  NGSIM trajectories, so there is no direct check that $C_{LI}$ and
  $C_{EX}$ individually track human listening or expression, only that the
  combined reward model fits recorded trajectories and correlates with a
  separate subjective questionnaire on pride and prejudice, not on the
  affordance terms themselves.
- The origin claim for "affordance" is the source paper's own citation and
  is not verified here; no source key is added for it.

## Related

[[affordance-gated-inquiry-reward]] · [[mutual-information]] · [[value-of-information]]

[^c1]: li-2026-pride
[^c2]: li-2026-pride
[^c3]: li-2026-pride
[^c4]: li-2026-pride — "We also model communication affordances as adaptive preferences shaped by environmental conditions, and validate the framework with naturalistic driving data and DIL experiments."
