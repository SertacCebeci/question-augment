---
description: "**This note's claim, not the literature's.** When the answers stop cohering, Three fields compute something after a clash, and each leaves the same slot empty. The pattern is what this note composes;"
aliases: []
sources: ["alchourron-1985", "doyle-1979", "gardenfors-1988", "istrate-2005", "kilby-2005", "slaney-2001"]
---
# The residue of a contradiction

> **This note's claim, not the literature's.** When the answers stop cohering,
> what still holds is not computable from the answers: every definition that
> uses them alone is degenerate. The criterion for what may be given up is an
> input the asker owes — and therefore something to ask about, not to derive.

## Definition / Mechanism

Three fields compute something after a clash, and each leaves the same slot[^s1][^s2][^s3][^s4][^s5][^s6]
empty. The pattern is what this note composes; no cited source states it.

| Field | What it computes after the clash | What it leaves undeclared |
|---|---|---|
| Belief revision | a consistent set, by contraction then expansion, with a representation theorem pinning the class | the selection function over remainder sets — and, in the interpretable form it was later given, the epistemic entrenchment ordering — taken as given, never derived (Alchourrón, Gärdenfors & Makinson 1985; Gärdenfors & Makinson 1988; [[agm-belief-revision]]) |
| Reason maintenance | the minimal inconsistent sets and exactly which later commitments die with a retraction | the culprit — nothing in the network ranks the responsible assumptions (Doyle 1979; [[truth-maintenance-system]]) |
| SAT / optimisation | the decisions frozen across all minimum-violation repairs ([[max-sat-backbone]]) | the objective — which answers may be dropped, and at what relative cost (Slaney & Walsh 2001) |

The SAT case adds the part the other two do not show: what happens if you
refuse to declare. Applied to a contradictory set with nothing else supplied,
the definitions collapse — every literal is entailed, or none is
([[backbone-of-a-formula|backbone]]-of-an-unsatisfiable-formula). Explosion and paralysis are not
two failure modes of a repair procedure; they are the two things "what
survives" *means* when the constraints are all you have. The one construction
that stays informative without an objective, the spine, buys this with an
existential over coherent subsets and no algorithm ([[spine-of-a-formula]]).

**The conjecture.** The undeclared parameter is constitutive, not missing. A
questioning agent that reaches $\|W\| = 0$ therefore faces a *question* — which
of my answers may be given up, and at what price — of the same kind as the
questions that produced the constraints, and it is answered from the same
sources (Source), not by a repair rule. Nothing in the literature
above is waiting to be completed; the theories are complete and the parameter
is a place where an answer is owed.

## Why it matters

Consistency lists repair as what none of its notes answers, which reads
as a gap in the wiki's coverage. If this note is right, the gap is not
fillable by adding a field: the missing item is not knowledge but a
declaration, and the honest move is to treat "what may be dropped" as an
elicitation target with a cost attached, on a par with the axes themselves.
That changes what an agent does at a clash — it spends a question rather than
running a procedure — and it makes the failure diagnosable: an agent that
repairs silently has declared a default (uniform clause weights, most-recent-
wins) without recording it.

Kilby et al. (2005) close the second direction off: their approximation
hardness result "holds however we define the backbone of unsatisfiable
formulae", so choosing the definition cleverly does not buy back a cheap
computation of the residue either.

## Transfer

| | Home fields | Here |
|---|---|---|
| Object | deductively closed belief sets (AGM); a justification network (TMS); a CNF/optimisation instance (SAT) | the record of questions asked and answers received, read as constraints on $W$ |
| Move | contraction by a selection function or entrenchment order; dependency-directed backtracking; minimising violated constraints | deciding what a contradiction leaves standing |
| What survives | that each formalism reaches a point where an ordering, a culprit or an objective must come from outside it; and the SAT demonstration that the residue is undefined without it | |
| What does not | The equivalence of the three parameters. Entrenchment ranks sentences, a MaxSAT objective prices clause violations, a culprit choice picks one assumption; this note treats them as one slot on the strength of where they sit in each procedure, which is a structural analogy and not a proved correspondence. | |

## Limits

- **The degeneracy premise is inherited, and partly a reading.** The explosion
  branch comes from Kilby et al.'s (2005) one-paragraph summary of Beacham
  (2000), not from the thesis, which was not read; the vacuity branch is
  backbone-of-an-unsatisfiable-formula's own reading of a convention, and
  some authors instead simply declare the backbone of an unsatisfiable formula
  empty. If either branch is rejected, "no non-degenerate reading uses the
  answers alone" weakens to "the standard readings do".
- **The degeneracy is propositional.** It rests on a formula having models or
  not. A numeric belief state ([[bayesian-estimation]]) never reaches
  $\|W\| = 0$ and reweights instead, so the argument says nothing there —
  which is the strongest reason to doubt its generality.
- **"Constitutive, not missing" is weaker than it sounds.** It is not refuted
  by a procedure that fixes the parameter by default; the claim is only that
  the default is a choice with no warrant in the answers.
- **Three cases are not a proof of the pattern**, and they were not chosen at
  random: they are the three fields Consistency already pulled.
- It says nothing about *how* to elicit the criterion, or from whom, or what a
  well-formed answer to it would look like.

## Related

[[max-sat-backbone]] · [[agm-belief-revision]] · [[truth-maintenance-system]] · [[version-space]] · [[constraint-as-information]]

[^s1]: alchourron-1985
[^s2]: doyle-1979
[^s3]: gardenfors-1988
[^s4]: istrate-2005
[^s5]: kilby-2005
[^s6]: slaney-2001
