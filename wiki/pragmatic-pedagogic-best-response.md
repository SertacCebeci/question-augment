---
description: "An algorithm that checks whether a goal-uncertainty game is action-separable and, if so, returns the pedagogic leverage map at the same asymptotic cost as solving the goal-known problem."
aliases: ["PPBR", "Pragmatic-Pedagogic Best Response", "Algorithm 1 (Lazarski & Fisac 2026)"]
sources: ["lazarski-2026"]
---
# Pragmatic-Pedagogic Best Response

> A checkable procedure: test whether a goal-uncertainty problem has the
> structure that lets one action fully disambiguate it, and if so, read off
> which action does it for each hypothesis.

## Definition / Mechanism

Pragmatic-Pedagogic Best Response (PPBR) computes, for a state $s$ and
prior $b$, whether the assistance game is
[[action-separable-assistance-game|action-separable]] and, if so, the
pedagogic leverage map $L$: for each candidate goal, the set of human
actions that a pragmatic human would use to signal it. It does this by (1)
computing the naive-rational human policy, (2) the literal (level-1) robot's
posterior after each candidate action, (3) each goal's best pragmatic-human
action under that posterior, and (4) rejecting the game as not
action-separable if any two goals are assigned the same leveraging action,
or if any leveraging action fails to reach the oracle (goal-known) value.[^c1]

Where it succeeds, the induced pragmatic human and robot policies are read
off in closed form from the inverse leverage map, with no further search:
"The runtime of Algorithm 1 is linear in the size of the goal set and
action sets: $O(|\Theta||A^H||A^R|)$, which is as efficient as solving the
oracle MDP."[^c2]

## Why it matters

It replaces the intractable general assistance-game solution — planning in
a POMDP over the robot's belief — with a linear-time check plus a
closed-form policy, but only on the structural class the check accepts;
where the game is not action-separable, PPBR reports failure rather than
degrading gracefully to a partial answer.

## Transfer

| | |
|---|---|
| **Home field** | Human-robot interaction: checking a specific finite goal set and finite action sets against a known MDP for structural separability |
| **Here** | A candidate test for whether a fixed batch of possible next actions/questions can be scored, offline, for whether any one of them would fully resolve the live hypothesis set |
| **What survives** | The idea of a cheap, linear *precondition check* run before committing to a one-shot resolution strategy, rather than assuming one-shot disambiguation always works |
| **What does not** | The closed-form policy itself, which is read off an enumerated leverage map; a natural-language question space has no such enumerable, checkable map to search |

## Limits

PPBR's guarantee is inherited entirely from
[[action-separable-assistance-game|Theorem 1]]: it is exact only under the
rational-agent limit and a game already known to be, or checked to be,
action-separable at the current state and prior; the paper states the
extension to partially overlapping ("split leverage") cases explicitly as
future work, not something Algorithm 1 currently handles. Reported only in
one 2026 arXiv preprint (`lazarski-2026`), validated on a single small
block-building domain, with no independent replication.

## Related

[[action-separable-assistance-game]] · [[ioc-inference-ceiling]] · [[mutual-information]]

[^c1]: lazarski-2026 — "Pragmatic–Pedagogic Best Response (PPBR) provides a simple procedure for computing an optimal equilibrium solution to an action-separable assistance game (Definition 4)."
[^c2]: lazarski-2026 — "The runtime of Algorithm 1 is linear in the size of the goal set and action sets: O(|Θ||AH ||AR |), which is as efficient as solving the oracle MDP."
