---
description: "A multi-term score (information gain minus a redundancy penalty plus a coverage bonus) for choosing a subset of follow-up questions per round, maximised approximately by a genetic algorithm."
aliases: ["information-gain-driven proactive questioning strategy", "information-gain follow-up selection"]
sources: ["wang-2026-evidence"]
---
# Information-gain / redundancy / coverage question utility

> Chooses the next *subset* of follow-up questions per dialogue round by a
> weighted sum of three terms, not by information gain alone, and searches
> that subset space with a genetic algorithm because exhaustive search over
> it is infeasible.

## Definition / Mechanism

At each round the system scores a candidate symptom-question subset $Q_t$
against the current candidate-syndrome set: "the system selects a
discriminative symptom subset $Q_t$ from the unasked symptom space to
reduce uncertainty over the current candidate syndrome set" Wang et al. (2026).[^c1]

The score combines three terms: information gain of the subset, a penalty
for asking symptoms that correlate with each other, and a bonus for
spreading the subset across distinct discriminative features: "IG measures
[[entropy]] reduction in the candidate syndrome set after asking $Q_t$,
$R(Q_t)$ penalizes highly correlated symptom questions, and $C(Q_t)$
encourages symptoms that cover discriminative features across candidate
syndrome types".[^c2]

Because the candidate symptom space makes exhaustive search over subsets
infeasible, the maximiser is not exact: "the system uses a genetic
algorithm for approximate optimization, with $U(Q_t)$ as the fitness
function".[^c3]

This differs from plain [[expected-information-gain]] in two ways at once:
the unit chosen is a *subset* per round rather than a single question, and
the objective is not information gain alone — a redundancy term and a
coverage term are added on top and traded off by hand-set weights
$\alpha,\beta,\gamma$.

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| This paper (health informatics, TCM dialogue) | "information gain–driven proactive questioning strategy" | exact — the paper's abstract-level name for the mechanism |
| This paper | "information-gain follow-up selection" | exact — the paper's section-heading name for the same mechanism |

## Transfer

| | |
|---|---|
| **Home field** | genetic algorithms / evolutionary computation: approximate maximisation of an arbitrary fitness function over a combinatorial search space with no assumed structure (no convexity, no submodularity) |
| **Here** | the fitness function is the three-term question-subset utility $U(Q_t)$; the search space is subsets of the unasked symptom set |
| **What survives** | the GA's only real requirement — that $U$ can be evaluated on a candidate subset — so it applies without proving $U$ has any special structure |
| **What does not** | any optimality guarantee or convergence rate; unlike the $(1-1/e)$ bound available when an objective is proven [[adaptive-submodularity|adaptive submodular]], nothing here bounds how far the GA's output is from the best subset, and the paper reports no such analysis |

## Limits

The paper states its own limitation directly: "The follow-up strategy
driven by information gain is demonstrated in a case walkthrough only.
Convergence efficiency (rounds to convergence, candidate-space reduction
per round) was not measured, so its contribution cannot be separated from
that of the knowledge graph constraint evaluated under RQ1".[^c4]

The measured trust (Cohen's d = 1.82) and cognitive-load effects reported
elsewhere in the same paper test knowledge-graph visualisation and
multimodal treatment plans respectively — neither isolates this selection
rule, so this note's claim rests only on the mechanism's stated design,
not on a measured outcome of using it. The weights $\alpha, \beta, \gamma$
are not reported as learned or tuned in the extract read, and no formula
for $R(Q_t)$ or $C(Q_t)$ is given in the sections read; their sensitivity
is unknown.

## Related

[[expected-information-gain]] · [[adaptive-submodularity]] · [[generalized-binary-search]] · [[value-of-information]]

[^c1]: wang-2026-evidence — "the system selects a discriminative symptom subset Qt from the unasked symptom space to reduce uncertainty over the current candidate syndrome set"
[^c2]: wang-2026-evidence
[^c3]: wang-2026-evidence
[^c4]: wang-2026-evidence — "The follow-up strategy driven by information gain is demonstrated in a case walkthrough only. Convergence efficiency (rounds to convergence, candidate-space reduction per round) was not measured, so its contribution cannot be separated from that of the knowledge graph constraint evaluated under RQ1"
