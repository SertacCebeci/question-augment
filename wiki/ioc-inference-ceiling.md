---
description: "Inverse optimal control has a provable posterior-belief ceiling strictly below certainty whenever two goals share an optimal action, which blocks one-step alignment however confident the inference."
aliases: ["IOC inference ceiling", "incorrigibility bound"]
sources: ["lazarski-2026"]
---
# IOC inference ceiling

> Watching a human act "as if rational" cannot always reveal their goal, no
> matter how confidently that rationality is assumed — a hard bound on
> what a naive best-response can infer from one act.

## Definition / Mechanism

Lazarski & Fisac (2026) show that when a naive robot infers a goal by inverse
optimal control (IOC) / inverse reinforcement learning (IRL) — treating an
observed action as evidence via Bayes' rule under an increasingly
rationality-confident human model — an **inference ceiling** appears
whenever one goal's optimal-action set is a subset of another goal's: "an
IOC inference ceiling appears whenever one goal's H0-optimal action set is a
subset of the H0-optimal action set for another goal."[^c1]

For two goals $\theta^\star,\theta'$ sharing an optimal action $a^\dagger$
with $|A^\star(\theta^\star)|=k \le m=|A^\star(\theta')|$, the posterior
in $\theta^\star$ converges, as the assumed human rationality
$\beta^H\to\infty$, to $m\,b(\theta^\star)/(m\,b(\theta^\star)+k\,b(\theta'))$
— a value strictly below 1 for any nonzero prior on $\theta'$. No amount of
assumed rationality pushes it past that ceiling, and if the robot's prior
already favours the wrong goal enough, "even in simple assistance games, the
IOC robot strategy is short-term incorrigible from seemingly benign initial
conditions" — the human has no available action that can still redirect it.[^c2]

## Why it matters

This bounds a common selection strategy — "infer intent by watching what an
agent does, assuming it's rational" — and names exactly when it fails: not
from noise, but from an unavoidable structural overlap in what the
different candidate goals would make the agent do anyway. It is the
negative result [[action-separable-assistance-game]] is defined against:
action-separability is the condition under which *pragmatic* (rather than
naive-IOC) reasoning breaks this ceiling.

## Limits

The bound is derived for a specific inference model — a Boltzmann-rational
(softmax) human observed once by a level-0/level-1 (naive) Bayesian
updater — and the large-$\beta^H$ limit; it is a property of that inference
procedure, not a universal fact about all action-inference methods. It is
one preprint's result (`lazarski-2026`, 2026, arXiv, not independently
replicated) and is demonstrated formally only for the finite, fully known
goal-and-action-set case used throughout the paper (an "action set subset"
condition rather than continuous or unbounded action spaces).

## Related

[[action-separable-assistance-game]] · [[pragmatic-pedagogic-best-response]] · [[value-of-information]]

[^c1]: lazarski-2026 — "an IOC inference ceiling appears whenever one goal’s H0-optimal action set is a subset of the H0-optimal action set for another goal."
[^c2]: lazarski-2026 — "even in simple assistance games, the IOC robot strategy is short-term incorrigible from seemingly benign initial conditions."
