---
description: "When the space of possibilities grows rather than shrinks, one rule still Karni & Vierø (2013) established the rule; Karni & Vierø (2017) generalise it to an agent who anticipates the expansion."
aliases: ["reverse Bayesianism", "reverse Bayesian updating", "updating over an expanding state space"]
sources: ["karni-2013", "karni-2017"]
---
# Reverse Bayesianism

> When the space of possibilities grows rather than shrinks, one rule still
> pins the new beliefs down: everything that was describable before keeps its
> *relative* likelihoods, and the newly describable states are paid for out of
> the residual.

## Definition / Mechanism

Karni & Vierø (2013) established the rule; Karni & Vierø (2017) generalise it[^s1][^s2]
to an agent who anticipates the expansion. Awareness grows when a consequence
$c' \notin C_0$ is discovered, so $C_1 = C_0 \cup \{c'\}$ and the catch-all
becomes $x_1 = \neg C_1$ ([[catch-all-consequence]]). The [[possible-worlds|state space]] refines
in a specific way: **every prior fully describable state survives unchanged**,
while each prior *imperfectly* describable state splits into one fully
describable state and one or more new imperfectly describable states. Both
parts of the partition grow.

Three axioms link the agent's preference relation before ($\succ_0$) and after
($\succ_1$): **invariant risk preferences** (the ranking of lotteries over old
consequences does not depend on the level of awareness), **awareness
consistency I** (discovery does not alter preferences conditional on events
made of a-priori fully describable states) and **awareness consistency II**
(the ranking of a-priori measurable acts is independent of the detail with
which their sub-events can now be described).

Karni & Vierø's Theorem 2 shows these hold exactly when the two subjective
[[expected-utility|expected utility]] representations, with priors $\pi_0$ on $\hat C_0^A$ and
$\pi_1$ on $\hat C_1^A$, satisfy

$$\frac{\pi_0(s)}{\pi_0(s')} = \frac{\pi_1(s)}{\pi_1(s')} \quad \text{for all } s,s' \in C_0^A$$

$$\frac{\pi_0(s)}{\pi_0(s')} = \frac{\pi_1(E'(s))}{\pi_1(E'(s'))} \quad \text{for all } s,s' \in \hat C_0^A \setminus C_0^A$$

where $E'(s)$ is the event the old partially describable state $s$ became —
and the utilities agree on the old consequences, $U_0(p) = U_1(p)$ for
$p \in \Delta(C_0)$. The earlier model of Karni & Vierø (2013) is the nested
special case $\pi_i(C_i^A) = 1$: an agent who, at every level of awareness,
acts as if she assigns probability zero to any future expansion of it.

## Why it matters

A questioner who discovers an axis value that was not in its model faces an
underdetermined problem: infinitely many distributions on the new space agree
with the old one on old events. This theorem removes almost all of that
freedom without any new elicitation. Everything that was already comparable
stays comparable in the same ratios; the only quantity that has to be supplied
is how much total mass leaves the residual, which is [[sense-of-ignorance]].
It is the opposite discipline to [[maximum-entropy-principle]]: MaxEnt
re-derives the whole distribution on the enlarged space, reverse Bayesianism
forbids touching the part that was already there.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Decision theory (Karni & Vierø 2013) | reverse Bayesianism | exact |
| Decision theory | reverse Bayesian updating | exact |
| Statistics / probability | **Bayesian updating, conditioning** | **not this concept.** Conditioning removes states from a *fixed* space and renormalises what is left; this relates two priors defined on *different* spaces and is not derived from Bayes' rule — the name records a resemblance in flavour, not an instance |

## Transfer

| | |
|---|---|
| **In its home field** | Two subjective expected utility representations of one decision maker's preferences over acts, at two levels of awareness, with finite action and consequence sets |
| **Here** | The asker's distribution over $W$ before and after an answer reveals a value the model did not contain — the case where an answer *adds* an axis value instead of eliminating worlds |
| **What survives** | The constraint shape: old relative likelihoods invariant, new mass drawn from the residual cell, old comparisons not re-elicited. This is directly usable as a bookkeeping rule when a model of $W$ is extended mid-inquiry |
| **What does not** | Its force as a *theorem*. The equalities are equivalent to axioms about a preference relation over settleable acts; an asker with no such preference relation gets a convention, not a representation result. Nor does it cover an answer that redescribes the old consequences rather than adding to them |

## Limits

- **It fixes ratios, not levels.** The theorem says nothing about the absolute
  probability of any event; the total mass on the residual is free and is the
  subject of a separate theorem ([[sense-of-ignorance]]).
- **$C_0 \subset C_1$ is an assumption.** The old consequence set must survive
  intact inside the new one. A discovery that makes an old distinction
  incoherent — a reframing rather than an addition — is outside the model.
- **Consequences, not actions.** The paper treats discovered consequences;
  discovery of new basic actions refines the space differently and is not
  covered by Theorem 2.
- **The linking axiom is empirically contested.** Karni & Vierø (2017, n. 19)
  report that Ma & Schipper (2016) test invariant risk preferences
  experimentally and cannot reject it, while Mengel, Tsakas & Vostroknutov
  (2016) find risk preferences are affected by exposure to an environment with
  imperfect knowledge of the state space. Both are cited here from that
  footnote; the primary texts were not inspected.
- **Normative, not descriptive.** The result characterises a coherent agent's
  pair of preference orders. It is not evidence that people, or models, revise
  this way.

## Related

[[catch-all-consequence]] · [[sense-of-ignorance]] · [[agm-belief-revision]] · [[bayesian-estimation]] · [[maximum-entropy-principle]] · [[version-space]]

[^s1]: karni-2013
[^s2]: karni-2017
