---
description: "A learner-issued preference query selected to repair the teacher's stale model of what the learner already knows, not to reduce the learner's own uncertainty."
aliases: ["understanding statements", "ToM-2 statement", "second-order theory-of-mind statement"]
sources: ["mirenzi-2026"]
---
# Understanding statement

> In preference-based reward learning, the query that matters is not always
> the one that best resolves the asker's own uncertainty — it can be the one
> that repairs what a *teacher* believes the asker already knows.

## Definition / Mechanism

An understanding statement is a preference-pair query issued by a learner
to its teacher, selected not to reduce the learner's own belief uncertainty
but to reduce the divergence between the teacher's model of the learner's
belief, $\hat B^T_t$, and the learner's true belief $B_t$. Mirenzi & Admoni
formalize it in continuous preference learning as a halfspace constraint
$a\cdot x\ge 0$ chosen by
$a_{\text{ToM2}}=\arg\min_a D(\hat B^T_t \mid a\cdot x\ge 0\;\|\;B_t)$ —
a second-order Theory-of-Mind (ToM-2) computation: the learner reasons
about the teacher's model of the learner, not just its own belief. A
first-order variant reports the belief mean $\bar x_t$ instead, without
reference to the teacher's model.[^c1]

The two policies coincide when the teacher's model error is isotropic, but
separate when the error is anisotropic — concentrated in one direction,
as alternating-teacher staleness produces — where only the second-order
statement targets the stale direction.[^c2]

## Why it matters

The mechanism is proposed to repair a specific failure mode: a teacher who
knows the target reward can construct more efficient queries than any
belief-only rule (see [[target-aware-query-construction]]), but only if
its model of the learner is accurate; multiple alternating teachers each
build a model only from the turns they attended, so it goes stale between
handoffs. In simulation (four alternating teachers, $d=20$, halfspace
particle filter, 50 trials), an Uninformed teacher's advantage over a
learner-guided (EVR) baseline erodes under this drift, a Mean-informed
teacher partially recovers it, and a ToM-2-informed teacher recovers it
further — alignment ordering Ideal > ToM-2 > Mean > EVR at every round,
tracking a model-error ordering measured by Earth Mover's Distance between
$\hat B^T_t$ and $B_t$. Varying the per-turn statement budget $u\in\{1,2,4,6\}$
shows model error decreasing and alignment approaching the no-drift
(Ideal) ceiling even at low $u$, i.e., small communication cost recovers
most of the drift-induced loss.[^c3]

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | Second-order Theory-of-Mind (recursive belief modelling in cognitive science / HRI, via Callaghan et al.'s human-study mechanism) | A selection rule for which preference query a learner sends, scored by the reduction it produces in a teacher's model-error divergence |
| Survives | The nested-belief structure: an agent reasoning about another agent's model of itself, and choosing a communicative act to correct that model | |
| Does not survive | The original linguistic, enumerated-feature form of the statement, and any claim about naturalistic human cognition — here it is a halfspace constraint in a continuous action space, chosen by an explicit divergence-minimizing computation, not a claim about how people actually model each other | |
[^c4]

## Limits

The claim rests on a noiseless-oracle, linear-reward, particle-filter
simulation with synthetic drift from a fixed four-teacher round-robin
protocol at $d=20$ (and $d=40$ for the dimensionality check); no human
teacher is involved, so the "understanding statement" here is validated
as an information-theoretic repair signal in simulation, not (yet) as an
effective communicative act for a real teacher, and the paper describes
its four-condition human study as still under development.[^c5]

## Related

[[target-aware-query-construction]] · [[expected-information-gain]] · [[volume-removal]] · [[value-of-information]]

[^c1]: mirenzi-2026
[^c2]: mirenzi-2026 — "The policies diverge only when Et is anisotropic: when the teacher is wrong in a specific direction, ToM-2 targets that direction while mean statement reports a centroid uninformative for that error"
[^c3]: mirenzi-2026 — "Fig. 3 a (top) shows the alignment ordering Ideal > ToM-2 > Mean > EVR at every round."
[^c4]: mirenzi-2026
[^c5]: mirenzi-2026 — "A four-condition human study (EVR, teacher no statement, teacher + mean statement, teacher + ToM-2 statement) is under development using a table arrangement domain"
