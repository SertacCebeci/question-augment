---
description: "An exact dynamic program over a decision tree built by hypothesis-augmented A* search picks the query order that minimizes expected interaction-plus-verification cost."
aliases: ["cost-optimal querying policy", "uncertainty-mitigation joint planning", "hypothesis-augmented A* search"]
sources: ["fang-2026"]
---
# Cost-optimal query policy

> When the number of uncertain objects is small enough to enumerate, a robot
> does not need a myopic rule to decide what to ask next — it can compute the
> exactly optimal query order by dynamic programming over the decision tree
> its own path [[planner-dynamic-stopping|planner]] already built.

## Definition / Mechanism

Fang et al. (2026) build a human-robot planner that first turns
obstacle uncertainty into a decision tree: an A* search whose state carries,
alongside position, the set of uncertain objects assumed passable so far —
so each node is `⟨v, H⟩`, not just `v`. The resulting tree maps every
possible truth assignment of $n$ uncertain objects to one of $m$ candidate
paths. Treating each object's unknown traversability as a belief
$b(o_i)\in\{0,1\}$ with prior $p_i$, the robot then asks only what changes
this mapping: it computes the exact minimum-expected-cost query set by
recursing on the Bellman equation
$V(s)=\min_U\big[\lambda_1+|U|\lambda_2+\mathbb E_{b(U)}[V(s\cup b(U))]\big]$,
$V(s_0)=0$ once $s_0$ pins down a single path, where $\lambda_1$ is a
per-query interaction cost and $\lambda_2$ a per-object verification cost.
Because $n$ is kept small by construction, this is solved exactly by
memoized dynamic programming over the belief-[[possible-worlds|state space]]
$\{0,1,\text{unknown}\}^n$, not approximated. "The framework derives an
[[elicitation-burden-tradeoff|optimal querying policy]] π, which guarantees that the robot identifies the
definitive safe path with the absolute minimum expected interaction
cost."[^c1]

## Why it matters

The map's default for stall 2 is myopic greedy ([[expected-information-gain]],
one step at a time) because the exact optimum is NP-hard in general
([[optimal-decision-tree]]). This system is the case where that trade-off
does not have to be made: once the candidate space is a small, enumerated
decision tree — here, produced by the robot's own hypothesis-augmented
search rather than given — exact backward induction is cheap enough to run,
and the resulting policy defers low-value questions (e.g. an obstacle with
high prior probability of being passable) even when two objects affect the
plan equally. In a Gazebo/real-UAV evaluation against a no-query baseline
and an exhaustive-verification baseline, the policy "reduc[ed] the number of
queries by 51.9%" while the system "maintain[ed] a 100% task success rate."[^c2]

## Transfer

| | In its home field | Here |
|---|---|---|
| Objects | A* search and Bellman dynamic programming over an enumerated, finite state space (search/planning, operations research) | the same machinery applied to which clarification questions a robot asks a human |
| What survives | exact optimality of the query order, and the guarantee that it holds whenever the state space is small enough to enumerate | |
| What does not | scalability — the belief-state space is $3^n$ (ternary per object); the paper relies on the perception+LLM front end keeping $n$ small, not on any bound proven for open-ended question generation | |

## Limits

- Validated in one domain (search-and-rescue UAV navigation) with a small,
  bounded number of uncertain objects per episode; the exactness result
  rests on $n$ staying small enough for $\{0,1,\text{unknown}\}^n$ to be
  enumerated, which the paper arranges by construction rather than proves
  in general.
- The 51.9% figure is measured against the paper's own no-query and
  exhaustive-verification baselines, not against a myopic-[[generalized-binary-search|greedy EIG]] or
  generalized-binary-search competitor, so it does not show this beats
  greedy — only that it beats not adapting the query set at all.
- `fang-2026` is a single, unreplicated study read from its own text extract.

## Related

[[optimal-decision-tree]] · [[value-of-information]] · [[generalized-binary-search]] · [[adaptive-submodularity]]

[^c1]: fang-2026 — "The framework derives an optimal querying policy π, which guarantees that the robot identifies the definitive safe path with the absolute minimum expected interaction cost."
[^c2]: fang-2026 — "the interaction cost by 51.9% while maintaining a 100% task success rate"
