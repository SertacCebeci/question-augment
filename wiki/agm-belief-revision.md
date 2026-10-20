---
description: "The one field on stall 6 that *repairs*: it says exactly what a consistent Alchourrón,"
aliases: ["AGM", "AGM postulates", "AGM theory of theory change", "partial meet revision", "Levi identity", "epistemic entrenchment"]
sources: ["alchourron-1985", "darwiche-1997", "eiter-1992", "gardenfors-1988", "katsuno-1991"]
---
# AGM belief revision

> The one field on stall 6 that *repairs*: it says exactly what a consistent
> retraction must satisfy, and then hands the choice of what to drop back to
> you.

## Definition / Mechanism

Alchourrón, Gärdenfors and Makinson (1985) fix a belief set $K$ (closed under[^s1][^s2][^s3][^s4][^s5]
consequence) and three operations: expansion $K+p$, contraction $K \div p$
(give up $p$), revision $K * p$ (take in $p$ and stay consistent). Revision is
constrained by six basic postulates — **closure**, **success** ($p \in K*p$),
**inclusion** ($K*p \subseteq K+p$), **vacuity** (if $\neg p \notin K$ then
$K*p = K+p$), **consistency**, **extensionality** — and is defined from
contraction by the **Levi identity**:

$$K * p \;=\; (K \div \neg p) + p$$

Repair is therefore *drop the negation of the new input first, then add it*.
Which beliefs get dropped is the content of contraction. Partial meet
contraction takes the maximal subsets of $K$ not implying $p$, has a
**selection function** $\gamma$ pick some of them, and intersects. The
**representation theorem** is the load-bearing result: an operation satisfies
the basic contraction postulates *iff* it is partial meet contraction for some
$\gamma$ — the axioms and the construction pin down the same class.

Gärdenfors and Makinson (1988) give the selection an interpretable form:
an ordering of **epistemic entrenchment** over sentences, contraction removing
the least entrenched, corresponding exactly to transitively relational partial
meet contraction.

Two boundaries the theory draws for itself. Katsuno and Mendelzon (1991)
separate **revision** (the world is fixed, the description was wrong) from
**update** (the world changed) and show they satisfy different postulate sets.
Darwiche and Pearl (1997) show the AGM postulates are too weak to constrain
*iterated* revision — they do not preserve conditional beliefs across a
sequence of inputs — and add C1–C4 defined over epistemic states rather than
belief sets.

## Why it matters

Every other note on stall 6 stops at detection. This one continues: it names a
shape for the repair itself, and the representation theorem shows that the
axioms one would write down by hand have exactly one family of
implementations, so there is nothing left to choose at the level of the
operator. What is left to choose sits one level down, in $\gamma$ — and
Gärdenfors and Makinson's entrenchment result says that choice *is* an
ordering over sentences, nothing more exotic.

The negative results are as usable as the positive ones. Success means the
newest input wins unconditionally, so the framework simply has no state in
which the incoming sentence is the doubtful one. And revision is not cheap —
Eiter and Gottlob (1992) show entailment from a revised propositional
knowledge base is $\Pi_2^p$-complete, one level of the polynomial hierarchy
above ordinary propositional entailment.

Against [[truth-maintenance-system]], the other stall-6 note that acts after
detection, the division is clean: AGM supplies the ranking and the postulates
a repair must satisfy, TMS supplies the dependency graph that says what dies
with the retracted item, and neither supplies the other.

## Transfer

| | Home field | Here |
|---|---|---|
| Object | a sentence in a deductively closed belief set $K$ over a fixed logical language | one constraint fixed on an axis of $W$, arriving from an answer or from a decision |
| Input $p$ | a sentence accepted for revision | a later answer that contradicts an earlier constraint |
| What survives | contract-then-expand as the shape of repair (the Levi identity); the representation theorem's guarantee that the six postulates and partial meet contraction pin down the same class, so writing down the axioms is already choosing the construction; and the reduction of "what to drop" to a prior ordering question — a question that can in principle be asked before the clash | |
| What does not | **closure** (a questioner's constraints are what was actually asserted, not their consequences — hence the open belief-base gap); the assumption that answers arrive as $p$/$\neg p$ in one shared language; **success** (a late answer may be the doubtful one, and AGM cannot represent that); and the $\Pi_2^p$ figure, which is for propositional knowledge bases and says nothing about the cost of reconciling natural-language answers | |

The application of this transfer *inside* the $|W| \to 1$ loop — what an
entrenchment ordering over asked-for constraints would actually be, and which
postulates survive when constraints carry sources and costs — is a separate
conjecture, not a claim of this note.

## Limits

- **The entrenchment ordering is stipulated, not derived.** AGM says a
  selection function exists and constrains its behaviour; nothing in the
  theory says where the ordering comes from or how a questioner would elicit
  it. The theorem transfers the whole repair decision into an input the wiki
  does not yet have a note for.
- **Belief sets, not belief bases.** $K$ is deductively closed, so the theory
  cannot distinguish a constraint that was *answered* from one merely
  entailed by answers — precisely the distinction a questioning agent needs
  when deciding what to re-ask. [[belief-base-revision|Base revision]] drops [[recovery-postulate|the recovery postulate]] for
  this reason and is a different object, not an alias of this note.
- **Success is an assumption, not a result.** Its unconditional form is
  contested inside the field itself; a revision operator that may reject the
  input is a separate construction.
- **One agent, one language.** The contradiction must be expressible as
  $p$ and $\neg p$ in a shared logic, which leaves the map's second open
  problem — clash across incommensurable axes — untouched.
- **Static.** Katsuno–Mendelzon means the operator is wrong whenever the
  answer changed because the world changed rather than because the earlier
  answer was mistaken; the questioner must know which case it is in, and AGM
  does not tell it.
- **Nothing about consequences.** Even granted a culprit, AGM says only that
  the resulting set is closed and consistent; which downstream commitments
  rested on the retracted sentence is [[truth-maintenance-system]]'s object,
  not this one's.

## Related

[[constraint-as-information]] · [[truth-maintenance-system]] · [[possible-worlds]] · [[backbone-of-a-formula]] · [[bayesian-estimation]] · [[cusum]]

[^s1]: alchourron-1985
[^s2]: darwiche-1997
[^s3]: eiter-1992
[^s4]: gardenfors-1988
[^s5]: katsuno-1991
