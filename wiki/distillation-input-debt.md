---
description: "**This wiki's inference, not a result.** Stall 8 reads as a missing Three steps; only the middle one is someone else's. **1."
aliases: ["distillation input debt"]
sources: ["bond-2008", "bond-2010", "paninski-2003", "slonim-1999", "tishby-1999"]
---
# Distillation's input debt

> **This wiki's inference, not a result.** Stall 8 reads as a missing
> algorithm. On the notes the wiki actually holds it is a missing *input*, and
> the two inputs the information-bottleneck family needs now have measured
> prices: the relevance variable arrives about half complete, and a
> transcript-sized count table falls in the regime where information estimates
> stay biased however long you wait.

## The claim

Three steps; only the middle one is someone else's.[^s1][^s2][^s3][^s4][^s5]

**1. Every distillation procedure in the wiki consumes a declaration made
elsewhere.** Six notes were inspected — the ones with a row in
Distillation that produce an artifact. **No exhaustive count was
made**; this is a survey.

| Procedure | Input it does not produce |
|---|---|
| [[sufficient-statistic]] | the parameter $\theta$ that sufficiency is relative to |
| [[information-bottleneck]] | the relevance variable $Y$, and the joint $p(X,Y)$ |
| [[agglomerative-information-bottleneck]] | $Y$, and a count table dense enough to estimate $p(y\mid x)$ |
| [[version-space]] | the hypothesis language, fixed before the first answer |
| [[specification-mining]] | an equivalence relation on records, plus a rarity cutoff |
| [[goal-refinement-graph]] | the goal set the distillate must entail |

The declarations differ in type, and each relocates the stall rather than
closing it — mostly onto stall 1.

**2. Two of these declarations have been measured.**

- *The relevance variable.* Bond, Carlson & Keeney (2008) find that people
  listing objectives for a decision they are making produce roughly half of
  what they endorse from a checklist minutes later, with the omitted half
  rated nearly as important; 12 motivated executives averaged 36% of the
  aggregate list ([[objectives-generation-deficit]]). Bond et al. (2010) find
  the shortfall is partly recoverable, but only by a request that asserts
  incompleteness and names a target — a bare re-ask added 0.55 objectives
  against 4.87 ([[quantified-challenge]]).
- *The count table.* Paninski (2003) shows the plug-in estimator is consistent
  when the joint cell count is $o(N)$ and, when $N/m$ stays bounded, remains
  biased as $N \to \infty$ while its variance stays under $(\log N)^2/N$
  ([[information-estimation-bias]]).

**3. Therefore (this wiki).** The stall-8 gap is an *input* gap with two
prices, and a derived procedure inherits three obligations that none of the
distillation notes states:

- **Elicit $Y$ before distilling, and by recognition plus a quantified second
  request, not by one open question.** On the measured sizes, a $Y$ obtained
  the usual way omits about half of what it should contain — and every
  quantity downstream ($\beta$, the merge price, the retained-information
  curve) is defined *relative to that $Y$*. The loss caused by an omitted
  relevance dimension does not appear anywhere on the IB curve; it is invisible
  to the very instrument that is supposed to price the compression.
- **Coarsen the table until its cells are well under the number of answers,
  and record the coarsening as the first compression decision.** Below that,
  merge prices are biased in a fixed direction with small variance — confident
  and wrong.
- **Report both debts with the distillate.** A distillate is then three
  things: the artifact, the $Y$ it was optimised against, and the coarsening
  that made the table estimable.

**What would refute it.** Elicit $Y$ from the same respondent by both
protocols (one open question; recognition plus an add-$n$ challenge), build
both tables from the same transcript, and run
[[agglomerative-information-bottleneck]]. If the two hierarchies agree on
their merges and prices, the first debt does not bind for distillation even
though it binds for the objective list.

## Known as

Not a term of art. "Input debt" is this wiki's name for the composition of two
measured shortfalls with the wiki's own distillation notes; no field known to
this note carries the composition, and the phrase should not be searched for
in the literature. The halves are [[objectives-generation-deficit]],
[[quantified-challenge]] and [[information-estimation-bias]].

## Transfer

| | |
|---|---|
| **In its home field** | two unrelated results: a behavioural shortfall in listing objectives for a personal decision, and an asymptotic statement about binned i.i.d. samples |
| **Here** | both are read as prices on the two declared inputs of one compression procedure |
| **What survives** | that each input is obtainable in principle, and that each has a known failure direction — short (objectives) and biased (counts) |
| **What does not** | the arithmetic. Neither ~50% nor $m = o(N)$ composes into a bound on the distillate's error; the two prices are stated in incommensurable units and this note does not combine them into a number, only into an order of operations |

## Limits

- **This is a conjecture and is typed as one.** No source composes these
  results; Bond et al. write about decision makers, Paninski about spike
  trains, and neither mentions distillation from a transcript.
- **Step 1 is a survey of six notes, not a census** of the wiki's
  distillation procedures. How general the pattern is is exactly what the
  unmade count would decide.
- **Both measurements are imported outside their conditions.** The objectives
  studies use humans deciding for themselves with a domain master list
  available; the estimation theorems assume i.i.d. samples and a binning fixed
  before the data. A questioning session violates the last two outright, so
  the second price is a best case (see [[information-estimation-bias]]).
- **The first obligation is untested here.** Nothing in this wiki or its
  sources has run a distillation twice against two differently elicited
  relevance variables; the claim that the distillate moves is an inference
  from the size of the omission, not a measurement of its effect.
- It does not supply $Y$ either. It says how to ask for $Y$ and what the
  asking is worth — which relocates the stall-1 problem again rather than
  dissolving it.

## Related

[[objectives-generation-deficit]] · [[quantified-challenge]] · [[information-estimation-bias]] · [[agglomerative-information-bottleneck]] · [[information-bottleneck]] · [[sufficient-statistic]]

[^s1]: bond-2008
[^s2]: bond-2010
[^s3]: paninski-2003
[^s4]: slonim-1999
[^s5]: tishby-1999
