---
description: "The residue that needs neither a model nor an objective: what some *coherent For a formula $\\Phi$, (Istrate, Boettcher & Percus 2005, Eq. 3; the parameter was introduced by Bollobás, Borgs, Chayes,"
aliases: ["spine", "spine order parameter"]
sources: ["bollobas-2001", "istrate-2005", "kilby-2005"]
---
# Spine of a formula

> The residue that needs neither a model nor an objective: what some *coherent
> part* of the constraints already rules out. For random CSPs its jump at the
> threshold is provably the same event as minimal contradictions growing to
> linear size — and as refutation becoming exponential.

## Definition / Mechanism

For a formula $\Phi$,[^s1][^s2][^s3]

$$S(\Phi) = \{x \in Var(\Phi) \mid \exists W \in \{x,\bar{x}\},\ \Xi \subseteq \Phi : \Xi \in \mathrm{SAT},\ \Xi \wedge W \in \overline{\mathrm{SAT}}\}$$

(Istrate, Boettcher & Percus 2005, Eq. 3; the parameter was introduced by
Bollobás, Borgs, Chayes, Kim & Wilson (2001) to prove that random 2-SAT has a
second-order transition). Istrate et al. call it "a 'monotonic version' of the
backbone" and stress that "unlike the backbone, the spine is defined in terms
of the decision problem".

Read against a record of answers: a value is in the spine when **some subset of
the answers that is coherent by itself already excludes it** — whether or not
the whole record is coherent. Nothing has to be dropped and no cost of dropping
has to be declared, which is what distinguishes it from [[max-sat-backbone]].
For a satisfiable $\Phi$ the spine contains the backbone: take $\Xi = \Phi$
(immediate from the two definitions).

**The theorems.** Istrate et al. (2005) establish, for random constraint
satisfaction problems in Molloy's model:

- a discontinuity of the relative spine size at the threshold is tied to an
  $\Omega(n)$ lower bound on the size of *minimally unsatisfiable subformulas*
  of a random unsatisfiable subformula; standard proof-complexity methods then
  give $2^{\Omega(n)}$ resolution complexity, hence $2^{\Omega(n)}$ DPLL
  complexity on random instances. The two phenomena "have a common underlying
  cause: the emergence of 'large' (linear size) minimally unsatisfiable
  subformulas of a random formula at the satisfiability phase transition";
- conversely (their Theorem 1), for any generalized satisfiability problem a
  second-order transition in the spine implies, in the region where most
  formulas are unsatisfiable, resolution complexity below any exponential:
  $O(2^{\epsilon n})$ for every $\epsilon > 0$;
- a sufficient condition for a discontinuous jump (Theorem 2), met by every
  problem whose constraints have no implicates of size two or less (Theorem 3)
  — so "all satisfiability problems with a continuous phase transition in the
  spine are '2-SAT-like'";
- experimentally, backbone and spine can behave differently (graph
  bipartitioning) though they look alike for random 3-colouring.

## Known as

| Name | Field | Relation |
|---|---|---|
| spine | random CSP, statistical physics of computation | exact — the standard term |
| spine order parameter | random CSP | exact — the same set, named for its role in the phase-transition analysis |
| frozen development | graph colouring (Culberson & Gent) | *not* this concept: an "effective" version amenable to experiment, which Istrate et al. record (footnote to Eq. 5) as a *subset* of the spine |
| backbone | SAT, optimisation | *not* this concept: a different set, and the paper's point is that the two can diverge — see backbone-of-an-unsatisfiable-formula |

## Why it matters

Two things the spine gives this stall, one cited and one inferred.

**Cited.** It supplies the one residue here that survives a contradiction
without a declared objective: an answer subset that hangs together still
excludes things, and those exclusions are the part of $W$'s reduction that a
clash elsewhere does not undo. Unlike [[max-sat-backbone]] it asks for no cost
of dropping an answer, and unlike the entailment reading in
backbone-of-an-unsatisfiable-formula it does not go degenerate when the
record contradicts itself.

**This note's reading, not a theorem of Istrate et al.**
[[truth-maintenance-system]] returns a *minimal inconsistent set* as the output
of detection, and its practical value rests on that set being small enough to
inspect: a nogood of two answers names a culprit pair, a nogood of half the
record names nothing. Istrate et al. tie the *regime* in which those sets grow
to linear size to the *regime* in which refuting a random instance costs
$2^{\Omega(n)}$ — both consequences of one underlying event. Read across to a
single record, that suggests "my conflicts are diffuse" and "I cannot certify
the conflict cheaply" are one diagnosis rather than two problems, and that an
agent watching its minimal conflicts grow has weak grounds for expecting a
cheaper localisation procedure to turn up. The step from an ensemble statement
to one record is the wiki's, and it is a heuristic expectation, not a bound —
see Limits.

## Transfer

| | Home field | Here |
|---|---|---|
| Object | a random CNF/CSP instance at constraint density $c$, asymptotics in $n$ | one finite record of answers read as constraints |
| Quantity | the spine fraction $f_S(\Phi) = \|S(\Phi)\|/n$ and its continuity at the threshold | the values excluded by some self-consistent subset of the answers |
| What survives | the definition (it requires neither models nor an objective); the containment of the backbone for satisfiable $\Phi$. The coupling of large minimal conflicts with expensive refutation does *not* survive as a result: it survives only as this note's reading of an ensemble statement, and no bound on any one record follows from it | |
| What does not | Everything asymptotic — the threshold, the order of the transition, "with high probability" — because a record of answers is a single instance with no ensemble and no $n \to \infty$. And resolution complexity presupposes a proof system over CNF: an agent that explains a contradiction in prose has no resolution proof and inherits no bound. | |

## Limits

- **The results are about random instances from a specified ensemble.** Nothing
  about any particular formula follows from a statement about the phase
  transition, and the wiki's setting has no ensemble at all.
- **The diagnosis in *Why it matters* is this note's inference.** That diffuse
  conflicts and expensive certification are one event *on a single answer
  record* is a reading of an asymptotic result about random instances, not a
  theorem of Istrate et al.; on the model of [[backbone-of-a-formula]]'s last
  limit, the transfer row above names what did not come with it. Nothing here
  licenses a lower bound on the cost of localising any particular conflict.
- **No algorithm is claimed.** The definition quantifies over all subformulas;
  Istrate et al. analyse the spine as an order parameter and give no procedure
  for computing it, so "compute your spine" is not an available move. Kilby et al.'s (2005) approximation result closes with the remark that it "holds
  however we define the backbone of unsatisfiable formulae", which removes the
  hope that a redefinition buys tractability.
- **The containment of the backbone is stated here for satisfiable $\Phi$
  only** and is this note's one-line derivation, not a cited theorem.
- Bollobás et al. (2001) is cited as the origin of the parameter on Istrate et
  al.'s attribution; only the definition as restated by them was read.

## Related

[[max-sat-backbone]] · [[truth-maintenance-system]] · [[conflict-driven-clause-learning]] · [[backbone-of-a-formula]] · [[possible-worlds]]

[^s1]: bollobas-2001
[^s2]: istrate-2005
[^s3]: kilby-2005
