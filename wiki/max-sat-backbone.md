---
description: "When the constraints have no model, replace \"satisfies all\" with \"violates **This note carries Slaney & Walsh's (2001) general frozen-decisions construction**;"
aliases: ["MAX-SAT backbone", "optimisation backbone", "backbone of an optimisation problem"]
sources: ["istrate-2005", "janota-2015", "kilby-2005", "monasson-1999", "slaney-2001", "zhang-2001-maxsat"]
---
# MAX-SAT backbone

> When the constraints have no model, replace "satisfies all" with "violates
> fewest": what survives is the set of decisions every *best* repair agrees on.
> It is well defined on both sides of a contradiction — and only relative to
> the cost you declared.

## Definition / Mechanism

**This note carries Slaney & Walsh's (2001) general frozen-decisions[^s1][^s2][^s3][^s4][^s5][^s6]
construction**; MAX-SAT is in the title because it is the case they single out
where "decision just amounts to assignment", and it is the case the SAT
literature measures.

Write $opt(\Phi)$ for the number of constraints left unsatisfied by an optimal
assignment (Istrate, Boettcher & Percus 2005, §2). The backbone in this reading
is

$$B(\Phi) = \{x \in Var(\Phi) \mid \exists W \in \{x,\bar{x}\} : opt(\Phi \cup W) > opt(\Phi)\}$$

(ibid., Eq. 1): $x$ is in the backbone iff *forcing one of its two values makes
the best achievable outcome strictly worse*. If $\Phi$ is satisfiable then
$opt(\Phi)=0$ and this is the ordinary backbone ([[backbone-of-a-formula]]); if
$\Phi$ is unsatisfiable it is still defined, which is why it can be used as an
order parameter across the satisfiability threshold — the use Kilby et al. (2005) and Janota et al. (2015) both attribute to Monasson et al.

Slaney & Walsh (2001) state it for optimisation in general: "The backbone is
defined to be the set of frozen decisions: those with fixed outcomes for all
optimal solutions. In some cases, 'decision' just amounts to 'assignment': for
example, in MAX-SAT, the backbone is simply the set of assignments to variables
which are the same in every possible optimal solution. In general, however, the
relevant notion of decision is obtained by abstraction over isomorphism classes
of assignments" — in graph colouring the decision is whether two nodes share a
colour, not which colour, because the colours permute. The construction is one;
what varies with the problem is which quotient of the assignments counts as a
decision.

**Membership is a sensitivity statement.** For the travelling salesperson they
characterise it directly: "A leg occurs in the backbone iff adding some
distance $\epsilon$ to the corresponding entry in the inter-city distance
matrix increases the length of the optimal tour." The backbone is the set of
decisions the optimum is sensitive to; everything else can be perturbed for
free.

**What was measured.** Slaney & Walsh ran three families. Graph colouring
behaves like a decision problem — hardness positively correlated with backbone
size. For TSP the two costs come apart: over 100 random 20-city Euclidean
instances, normalised backbone size against the log of nodes visited gives
Pearson $r = 0.138$ (Spearman $0.126$) for *finding* the optimal tour and
$r = -0.0615$ (Spearman $-0.0147$) for finding *and proving* it optimal. Both
are weak, and their abstract states the condition for seeing anything at all:
"it is necessary to eliminate some symmetries, perform trivial reductions and
factor out the effective problem size". Zhang (2001), as reported by Kilby et
al. (2005), finds a sharp transition in the backbone size of random MAX-3-SAT,
correlated with the transition in random 3-SAT.

## Known as

| Name | Field | Relation |
|---|---|---|
| MAX-SAT backbone | SAT / MaxSAT | exact — the case Slaney & Walsh describe as "decision just amounts to assignment" |
| optimisation backbone, backbone of an optimisation problem | combinatorial optimisation | exact — the same frozen-decisions construction this note carries, with the decision type left open |
| backbone (unqualified) | SAT | close — coincides with this set exactly when $\Phi$ is satisfiable; [[backbone-of-a-formula]] holds that name |
| spine | random CSP | *not* this concept: a set defined through satisfiable subformulas, measured to behave differently at the transition ([[spine-of-a-formula]]) |
| frozen variables | statistical mechanics of random CSPs | *not* an alias here — [[backbone-of-a-formula]] carries it for the satisfiable case (Janota et al. 2015, §1) |

## Why it matters

At $|W| = 0$ the wiki's own map records the record as unrepaired: the answers
conflict and no world satisfies them all, so nothing is reported. This reading
gives the agent a step there. Declare a cost of dropping an answer, take the
worlds that violate the fewest (or the cheapest) answers, and report the
decisions on which all of them agree: that set is non-empty in cases where the
entailment reading returns everything and the model reading returns nothing.
Membership is then readable as sensitivity — an answer is in the residue iff
perturbing it moves the best achievable outcome — so the same computation also
says which answers are worth re-asking a source about. The declaration is not
optional and it is not free: [[agm-belief-revision]] takes an entrenchment
ordering as given and deletes a sentence; here nothing is deleted, the record
stays contradictory, and the cost function is the one thing the answers
themselves cannot supply.

## Transfer

| | Home field | Here |
|---|---|---|
| Object | a CNF formula or optimisation instance with a declared objective | the constraint set the answers supplied, once it has no model, plus a declared cost of dropping an answer |
| Solution | an assignment minimising unsatisfied constraints | one candidate world among those violating the fewest answers |
| What survives | the residue defined as the decisions frozen across all optima; the sensitivity reading (a held constraint is in the residue iff perturbing it moves the optimum); and that the residue exists *only* relative to the objective | |
| What does not | The objective itself. MAX-SAT counts unsatisfied clauses, so every answer is equally droppable and equally weighted: a mis-transcribed answer and a genuine disagreement cost the same. Weighted MaxSAT restores weights, but those weights *are* the entrenchment ordering [[agm-belief-revision]] already takes as given — the import supplies the shape of a repair objective, not its content. Nor do the correlations survive: they are over random instance families with a size parameter, and an answer record is one instance with no ensemble. | |

## Limits

- **The measured correlations are weak and family-specific** ($|r| \le 0.14$ on
  the TSP experiments, with opposite signs for the two costs), and Slaney &
  Walsh's own precondition is that symmetries be removed and effective size
  factored out before any relationship appears.
- **A countable violation measure is required.** Answers that conflict in
  degree rather than in kind have no clause count, so this residue is undefined
  for a numeric belief state ([[bayesian-estimation]]).
- **It selects nothing.** The residue is by construction the part on which the
  choice among optima does not matter; the remainder is an unattributed choice
  exactly as in [[backbone-of-a-formula]], now with no entailment behind it.
- Zhang (2001) and Monasson et al. are cited through Kilby et al.'s report of
  them; neither was read for this note.
- Kilby et al.'s hardness results apply here: no polynomial procedure returns a
  guaranteed fraction of this set either, since their proof "just computed the
  backbone of satisfiable formulae".

## Related

[[backbone-of-a-formula]] · [[spine-of-a-formula]] · [[agm-belief-revision]] · [[truth-maintenance-system]] · [[constraint-as-information]]

[^s1]: istrate-2005
[^s2]: janota-2015
[^s3]: kilby-2005
[^s4]: monasson-1999
[^s5]: slaney-2001
[^s6]: zhang-2001-maxsat
