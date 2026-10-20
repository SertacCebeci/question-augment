---
description: "An assistance game is action-separable when every goal has a human action that fully reveals it at no task-value cost, so one round of best responses reaches the optimal equilibrium."
aliases: ["action-separable assistance game", "action-separability", "zero-cost pedagogy"]
sources: ["lazarski-2026"]
---
# Action-separable assistance game

> A condition on a human-robot goal-uncertainty game under which a single
> observed human action, chosen well, collapses the robot's uncertainty about
> the goal completely — no further interaction needed.

## Definition / Mechanism

In an assistance game the human knows the true goal $\theta$; the robot must
infer it while acting to help. Lazarski & Fisac (2026) define a **pedagogic leverage
map** $L$ assigning to each candidate goal the human actions that a
level-2 "pragmatic" human (reasoning about a level-1 robot that reasons about
a level-0 literal human) would use to signal it. The game is
**action-separable** at a state and prior when this map is *fully
populated* — some leveraging action exists for every goal — and achieves
**zero-cost pedagogy**: taking that action loses no value under the oracle
(goal-known) policy.[^c1]

Their central result: when a game is action-separable, a single round of
best responses — a "pragmatic" human policy against a naive robot, then a
"pragmatic" robot best-responding to the resulting posterior — is provably
an optimal equilibrium of the full multi-step game, matching the value an
oracle that already knew the goal would achieve. No further rounds of
recursive reasoning or replanning are needed.[^c2]

## Why it matters

This is a sufficient condition for **when one well-chosen informative act
substitutes for iterative elicitation**: not every axis of an action space
disambiguates a hypothesis set in one step, but when the leverage map is
fully populated and free, it does. It gives a checkable, structural test
(Algorithm 1 in [[pragmatic-pedagogic-best-response]]) for whether a
selection problem has this property, rather than a general claim that
acting once is always enough.

## Transfer

| | |
|---|---|
| **Home field** | Human-robot interaction / assistance games (cooperative inverse reinforcement learning): a Boltzmann-rational, level-$k$ human-robot pair sharing a known MDP and goal set $\Theta$ |
| **Here** | Whether a single question (or exploratory act) can substitute for a sequence of constraint-gathering questions on stall 2 — which axis to act on first |
| **What survives** | The structural diagnostic: uncertainty collapses in one step only when the action space contains, for every live hypothesis, a distinct act that both signals it and costs nothing against the hypothesis-known optimum — not a general one-shot guarantee |
| **What does not** | The rational-agent limit ($\beta^H,\beta^R \to \infty$) and the assumption that both sides already share a known [[possible-worlds|state space]] and value function; a free-text question has no such enumerated, shared action set, so the test cannot be run as stated |

## Limits

The guarantee (Theorem 1) is a large-$\beta$ limit of two perfectly rational,
mutually-modelling agents in a common-payoff game with a known finite goal
set $\Theta$ and known MDP — it says nothing about noisy-rational regimes
away from that limit, and the paper's own extension ("split leverage," where
one action is optimal for more than one goal) is left as future work, so the
one-round guarantee does not cover partially separable games. `lazarski-2026`
is a single, recent (2026) arXiv preprint with no independent replication
found.

## Related

[[pragmatic-pedagogic-best-response]] · [[ioc-inference-ceiling]] · [[value-of-information]] · [[mutual-information]]

[^c1]: lazarski-2026 — "An assistance game G is action-separable at (s, b) if LH2 s,b is fully populated and achieves zero-cost pedagogy (Definition 3)."
[^c2]: lazarski-2026 — "Then, the limiting rational (β H , β R → ∞) R3– H2 policies (π R3⋆ , π H2⋆ ) constitute an optimal pragmatic–pedagogic equilibrium of the assistance game at (s, b)."
