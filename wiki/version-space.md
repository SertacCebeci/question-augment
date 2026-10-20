---
description: "A family that computes a distillate from a pile of recorded answers by Fix a hypothesis language $H$ before any answer arrives. Given examples $D$,"
aliases: ["version space", "candidate elimination", "version space algebra", "VSA"]
sources: ["gulwani-2011", "haussler-1988", "lau-2003", "mitchell-1982", "singh-2015", "arxiv-2512-03971"]
---
# Version space

> A family that computes a distillate from a pile of recorded answers by
> consistency alone — the price is that the answer space must be declared as a
> language first, and that what it computes is still a **set**, not a
> specification.

## Mechanism

Fix a hypothesis language $H$ before any answer arrives. Given examples[^s1][^s2][^s3][^s4][^s5]
$D$, the **version space** is $\{h \in H : h$ consistent with every example
in $D\}$ — exactly the surviving $W$, restricted to what $H$ can say.
Mitchell (1982) showed it is representable by two boundary sets, $S$ (the
most specific consistent hypotheses) and $G$ (the most general), and gave
**candidate elimination**: each new example specialises $G$ or generalises
$S$; the intervening hypotheses need never be enumerated. Three properties
are load-bearing here:

1. **A stopping test that is not a threshold.** The target is determined when
   $S = G$ and contains one element — $|W| = 1$, decidable from the data
   structure, unlike every rule in [[stopping-rules]].
2. **Collapse is ambiguous.** A single erroneous example empties the version
   space, and the collapse does not distinguish a bad example from a
   hypothesis language too poor to hold the target. The framing originates
   with Mitchell (1982); the compact wording used here follows its standard
   textbook restatement (Mitchell, *Machine Learning*, McGraw-Hill 1997,
   ch. 2 — not a keyed source in this wiki) — see Limits.
3. **Next-question selection falls out.** When the learner picks the
   instance, the optimum is the one matching about half of the surviving
   hypotheses (Mitchell 1982, restated in the 1997 textbook, ch. 2;
   [[generalized-binary-search]]).

Lau et al. (2003) turned the representation into an algebra: version spaces
over arbitrary functions, composed by **union** and **join**, so a compact
space of *programs* — not just conjunctive concepts — can be intersected
against each demonstration (SMARTedit). Gulwani (2011) replaced the lattice
with a graph in which every path is a consistent program, which is what makes
FlashFill synthesise from one or two examples.

## Why it matters

Stall 8 asks how thousands of question–answer pairs become one written
artifact. This is the field that answers, and its answer refuses the framing:
**consistency computes the set; it never computes the one.** Singh & Gulwani (2015) state the residue plainly — few examples leave many consistent
programs, and picking one requires a *separately learned ranking function*
that no example supplied. So a distillation procedure has two components with
different warrants: an elimination step entailed by the answers, and a
selection step that is a choice owing an attribution — structurally the same
split [[backbone-of-a-formula]] finds inside a solved constraint set,
reached from the machine-learning side. (Structural only: the backbone is a
property of the models of a constraint set, not a surviving $W$ under a
declared language, so the relation here is `analogy`, not `close`.)

The second consequence is a precondition, not a technique: no hypothesis
language, no version space. The algorithm exists; what it consumes is not
free text. That relocates the gap on stall 8 from "we lack an algorithm" to
"we lack the declared $H$" — which is stall 1.

## Known as

| Name | Where | exact / close | Gloss |
|---|---|---|---|
| candidate elimination | Mitchell 1982 | close | the maintenance algorithm, not the set; kept as an alias because the literature uses the two names interchangeably |
| version space algebra (VSA) | Lau et al. 2003 | close | generalisation of the representation to arbitrary functions composed by union and join, not the same object |
| programming by example / by demonstration | Gulwani 2011 | not this object | a *task*; the version space is one representation used for it — not claimed as an alias |

## Transfer

| | Home field | Here |
|---|---|---|
| Data | labelled instances | the question–answer record |
| $H$ | a designer-declared concept or DSL | not declared; free text is not a language |
| Output | $S$, $G$, and a ranking | the written specification |
| What survives | not a computation but a requirement on the procedure: a distillation step must (i) declare its hypothesis language before the first answer, (ii) separate what the answers entail from what a ranking chose, and (iii) treat an emptied space as evidence against the declared language as much as against any answer | |
| What does not | the algorithm itself, and every efficiency claim with it — both need $H$ | |

## Limits

- **Everything rests on $H$ being declared in advance and containing the
  target.** Outside that assumption candidate elimination has no guarantees
  and no defined output; this is the assumption the wiki's setting violates.
- The compact representation is not free: Haussler (1988) showed boundary
  sets can grow exponentially in the number of instances processed, so "you
  need not enumerate the space" is not a complexity claim.
- Noise-intolerance is total in the basic form — one wrong answer empties the
  space, and the diagnosis is undecidable from inside (mitchell-1982). Where
  [[truth-maintenance-system]] returns a minimal inconsistent set of answers,
  a collapse returns nothing to blame.
- Mechanism points 2 and 3 are attributed to mitchell-1982 as the origin of
  the framing; the section/page locator inside the 1982 paper is unconfirmed
  here, and the wording follows the later textbook restatement, which is not
  a keyed source in `wiki/meta/sources.json` and was not verified this pass.
- Singh & Gulwani's ranker is learned from a corpus of solved tasks. A
  one-session questioning agent has no such corpus, so the selection step is
  named, not solved.
- Nothing here reads free text. The claim that this family bears on stall 8
  is the wiki's, resting on treating an answer as an example and a
  specification as a hypothesis; no cited source makes that mapping. Nor is
  this the only literature producing a formal artifact from a corpus of
  recorded behaviour — [[specification-mining|specification mining]] is an uncompared alternative that
  needs no labels and no declared $H$.
- **The stopping test $|W| = 1$ is a test on representations.** Mechanism point 1 ends the search when one hypothesis is left. Where one function has many representations, a set of surviving hypotheses can name a single function while holding several members. arxiv-2512-03971 (decision trees, membership queries) adds a semantic test: when the approximate count stalls, a SAT check asks whether the survivors can disagree on any input, and they are collapsed to one function if not.[^s6] Whether this carries to a language with no such check is not shown there; see [[model-counting-query-selection]].

## Related

[[possible-worlds]] · [[backbone-of-a-formula]] · [[sufficient-statistic]] · [[truth-maintenance-system]] · [[generalized-binary-search]] · [[stopping-rules]]

[^s1]: gulwani-2011
[^s2]: haussler-1988
[^s3]: lau-2003
[^s4]: mitchell-1982
[^s5]: singh-2015
[^s6]: arxiv-2512-03971 — "to verify that all remaining hypotheses are functionally identical"
