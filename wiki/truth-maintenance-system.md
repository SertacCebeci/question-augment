---
description: "Record *why* each belief is held, and retraction stops being guesswork: the Doyle (1979) built a subsystem that records and maintains **the reasons for a program's beliefs**,"
aliases: ["TMS", "reason maintenance system", "RMS", "dependency network"]
sources: ["dekleer-1986", "doyle-1979", "doyle-1983", "elkan-1990", "stallman-1977"]
---
# Truth maintenance system

> Record *why* each belief is held, and retraction stops being guesswork: the
> machine computes exactly which later commitments die with a withdrawn answer.
> It still will not tell you which answer to withdraw.

## Definition / Mechanism

Doyle (1979) built a subsystem that records and maintains **the reasons for a[^s1][^s2][^s3][^s4][^s5]
program's beliefs**, then uses those reasons to keep the current belief set in
line with new ones, tracing them "to find the consequences of changes in the
set of assumptions" (abstract). The pieces:

- **Node** — one datum the problem solver might believe; status **IN**
  (believed) or **OUT** (not believed).
- **Justification (SL)** — a pair of lists: an *inlist* of nodes that must be
  IN and an *outlist* of nodes that must be OUT for this justification to be
  valid. A node is IN iff it has at least one valid, non-circular justification
  — its **well-founded support**.
- **Assumption** — a node whose supporting justification has a non-empty
  outlist: believed for want of anything to the contrary, hence retractable.
- **Contradiction** — *declared by the problem solver*, not found by the TMS: a
  contradiction node given a valid justification by the conflicting set.
- **Dependency-directed backtracking** (Stallman & Sussman 1977, generalised in
  Doyle 1979) — from the contradiction, walk the justifications back to the
  assumptions actually responsible, choose one (the **culprit**), and make it
  OUT by justifying one of its outlist members. Chronological backtracking
  discards good choices made after the real culprit; DDB "backs up far enough
  to remove the inconsistency" and no further.

De Kleer (1986) inverts the bookkeeping. An **assumption set (environment)**
replaces the single current belief set; a node's **label** is the set of
minimal, consistent environments from which it follows; a **nogood** is a
minimal environment known to be inconsistent. Labels are maintained sound,
complete, consistent and minimal, so all contexts are held at once: retraction
and most backtracking disappear, context switching is free — at the price of
labels that grow with the assumption set.

Doyle (1983) renamed the mechanism **reason maintenance**: the system maintains
reasons, and truth is not its business.

## Why it matters

Consistency records that every field on stall 6 detects a contradiction
and none repairs one. This is the field built for the repair, and what it
actually supplies is narrower than the name suggests, in three parts:

1. **The blast radius is computable, not estimated.** If every commitment
   carries the answers it rests on, withdrawing an answer marks exactly its
   dependents OUT. Without the graph, an agent that retracts either re-derives
   everything or silently keeps orphaned commitments — the second is the common
   failure and is invisible.
2. **A contradiction localises to a set, not a culprit.** A nogood is a
   *minimal* set of commitments that cannot all hold. That is strictly more than
   "$|W| = 0$" ([[constraint-as-information]]) and strictly less than an
   instruction.
3. **Nogoods are cached.** The same inconsistent combination is never explored
   twice — the same move CDCL makes in SAT ([[backbone-of-a-formula]]).

## Transfer

| | Home field | Here |
|---|---|---|
| Object | a node: a datum in a problem solver's database | a commitment: one value fixed on an axis of $W$, whether decided or received |
| Justification | inlist/outlist of nodes making this node IN | the question asked, the answer returned, and the earlier commitments the inference used — recorded at the moment the commitment is made |
| Assumption | node supported by an outlist — believed for lack of contrary | a value the agent fixed without asking (a silent fork / MaxEnt default) |
| Nogood | minimal inconsistent environment of assumptions | minimal set of answers-and-decisions that cannot all hold |
| What survives | the bookkeeping discipline (record the reason with the belief), well-founded support as the retraction rule, the minimal-conflict-set as the output of detection, nogood caching, and the ATMS option of carrying rival readings of an ambiguous answer in parallel instead of committing and undoing | |
| What does not | (a) *Culprit choice.* Doyle's DDB picks a culprit among the responsible assumptions; nothing in the network ranks them. An external preference order is needed and the wiki has none — that is the AGM-entrenchment row still open on Consistency. (b) *Detection.* The TMS never finds a contradiction; a conflicting set is user-designated. Stall 6's detectors still do the finding. (c) *Sound justifications.* The graph is only as good as the recorded reasons; a dependency the agent inferred in prose and did not record leaves a dead commitment IN, which is exactly the bug being fixed. (d) *Free computation:* Elkan (1990) proves implementing a non-monotonic TMS is NP-complete. | |

## Limits

- The claim that question–answer commitments form a dependency network is this
  note's transfer, not a result: no cited source discusses asking. The
  antecedent lists here must be constructed by the agent, whereas in Doyle's
  and de Kleer's setting the problem solver emits them as it infers.
- **Well-founded support presumes discrete beliefs.** A partially informative
  answer that shifts a posterior without settling a variable has no IN/OUT
  status, so a numeric belief ([[bayesian-estimation]]) is outside the
  mechanism.
- **[[np-completeness|NP-completeness]] bites in the direction of the fix.** Adding justifications
  to make retraction exact is what makes labelling expensive; the cheap version
  is an incomplete graph, which fails silently.
- Doyle's own 1983 verdict stands: this maintains reasons, not truth. A
  coherent, fully justified belief set can be wrong about the world.

## Related

[[constraint-as-information]] · [[backbone-of-a-formula]] · [[possible-worlds]] · [[cusum]] · [[goal-refinement-graph]] · [[bayesian-estimation]]

[^s1]: dekleer-1986
[^s2]: doyle-1979
[^s3]: doyle-1983
[^s4]: elkan-1990
[^s5]: stallman-1977
