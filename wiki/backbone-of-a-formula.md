---
description: "The part of a solution that every solution agrees on. It splits a distillate \"The backbone of a satisfiable SAT problem is the set of literals which are true in every satisfying truth assignment\" (…"
aliases: ["backbone", "backbone literals", "backbone variables", "frozen variables", "necessary assignments", "necessary variables", "bound literals", "fixed assignments", "unary prime implicates"]
sources: ["davis-1962", "janota-2015", "kilby-2005", "parkes-1997"]
---
# Backbone of a formula

> The part of a solution that every solution agrees on. It splits a distillate
> into what the answers forced and what the distiller chose — and proves that
> telling the two apart is as hard as the whole problem.

## Definition / Mechanism

"The backbone of a satisfiable SAT problem is the set of literals which are[^s1][^s2][^s3][^s4]
true in every satisfying truth assignment" (Kilby, Slaney, Thiébaux & Walsh 2005, p. 1368). Equivalently it is the set of *necessary* assignments: if
literal $l$ is in the backbone of $\phi$, every assignment satisfying $\phi$
must set $l$ true (Janota, Lynce & Marques-Silva 2015, §1).

Read $\phi$ as the constraints the answers supplied and its models as the
surviving $W$ ([[possible-worlds]]). Then any single model — one distillate —
decomposes into two kinds of content:

- **backbone literals**: agreed by all of $W$, so writing them adds nothing;
- **the rest**: a commitment the distiller made where $W$ was still split.

DPLL already runs on this split: unit propagation derives what the clauses
force, branching picks where they do not (Davis, Logemann & Loveland 1962).
Unit propagation is a *sound under-approximation* of the backbone — everything
it derives is backbone, not everything backbone is derived.

**The cost is not asymmetric in your favour.** Kilby et al. 2005: computing the
backbone is both NP-hard and NP-easy, hence "polynomial if and only if P=NP".
Worse, *Theorem 1*: if P $\neq$ NP, no sound approximation procedure can return
a fixed fraction $\alpha$ or more of the backbone in polynomial time.
*Theorem 2* extends this to unsound "majority-approximation" procedures — ones
allowed to return some literals falsely. Isolating the forced part of a
distillate is not a cheap post-processing pass over a solution.

**Backbones are typically large.** Parkes (1997) found a subclass emerging at
the satisfiability phase transition with "about 85–95% of their variables
occurring in unary prime implicates", whose models therefore all lie in one
exponentially large but simply describable cluster. Janota et al. (2015) report
that large instances from practical applications often have backbones close to
90% of variables.

## Known as

| Name | Field | Relation |
|---|---|---|
| backbone | SAT, statistical physics of computation | exact — the standard term |
| frozen variables | statistical mechanics of random CSPs | exact (Janota et al. 2015, §1) |
| necessary assignments / necessary variables | constraint reasoning | exact (ibid.) |
| bound literals, fixed assignments, units | SAT preprocessing literature | exact (ibid.) |
| unary prime implicates (UPIs) | prime-implicate theory | exact — $\phi \models l$ is a unit prime implicate (Parkes 1997) |

Janota et al. 2015 §1 collect the first four as the literature's variant names
for one object; the entry ASP calls a *cautious consequence* is the same
construction under answer-set rather than classical semantics and is not
claimed here as the same object.

## Why it matters

Distillation records that stall 8 has a definition and no algorithm.
This does not supply the algorithm; it supplies the **partition the algorithm
must respect**. [[data-processing-inequality]] says distillation may add no
information and [[sufficient-statistic]] says it may lose none — both are
constraints on the whole artifact. The backbone says the artifact is not
homogeneous: a fraction of it is entailed by the answers and the remainder is
an unattributed choice, and only the first fraction is licensed by anything
that was asked. An item resting on no question ([[constraint-as-information]])
is precisely a non-backbone literal that got written without a marker.

The theorems then say the audit is not free. "Which lines of this
specification did my answers actually force?" is NP-hard, and no polynomial
procedure will even give you a guaranteed fixed fraction of them. What is
available is the sound under-approximation: propagate, mark what propagates as
forced, and treat everything else as owing an attribution.

## Transfer

| | Home field | Here |
|---|---|---|
| Object | a CNF formula $\phi$ over a fixed finite variable set | the question–answer record read as constraints |
| Model | a satisfying assignment | one candidate world, i.e. one distillate |
| What survives | the forced/chosen partition of a solution; unit propagation as a sound under-approximation; the hardness of separating the two | |
| What does not | CNF-ness and the fixed variable set. Answers arrive as prose, and which variables exist is stall 1, unsolved. SAT also treats all models as equal, so nothing here selects *which* model — that is [[bayesian-estimation]]'s question, not this one. | |

## Limits

- **Satisfiable formulae only.** Kilby et al. restrict to satisfiable
  $\phi$ precisely because several rival definitions exist for unsatisfiable
  ones. If the answers contradict, there is no backbone in this sense — the
  contradiction is stall 6's problem first.
- **Forced is not correct.** The backbone is relative to the constraint set. A
  wrong answer produces backbone literals exactly as a right one does; this
  measures entailment, not truth.
- **Worst-case hardness is not a practical veto.** Janota et al. 2015 compute
  backbones of large industrial instances with a few hundred SAT calls; the
  theorems forbid a general guarantee, not a working tool.
- **The application to distillation is this note's inference.** No cited source
  discusses question-asking; they discuss propositional formulae. The claim
  that a distillate's non-backbone content is an unattributed choice is an
  argument by transfer, and the row above names what did not come with it.

## Related

[[sufficient-statistic]] · [[data-processing-inequality]] · [[constraint-as-information]] · [[possible-worlds]] · [[goal-refinement-graph]] · [[rate-distortion-theory]]

[^s1]: davis-1962
[^s2]: janota-2015
[^s3]: kilby-2005
[^s4]: parkes-1997
