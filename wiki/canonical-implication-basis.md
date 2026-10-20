---
description: "From a bare binary table of which surviving worlds carry which answers, one A **context** $(S,T,R)$ is a binary incidence: rows $S$, columns $T$, a cross where the row has the trait."
aliases: ["Duquenne-Guigues basis", "Guigues-Duquenne base", "stem base", "canonical basis", "canonical base", "minimal family of informative implications"]
sources: ["babin-2010", "distel-2011", "ganter-1984", "guigues-1986", "kuznetsov-2004", "kuznetsov-2008"]
---
# Canonical implication basis

> From a bare binary table of which surviving worlds carry which answers, one
> distillate is determined: the smallest complete set of implications among
> the answers. It needs no relevance variable, no ranking and no rarity
> cutoff — and it does not reach one world.

## Definition / Mechanism

A **context** $(S,T,R)$ is a binary incidence: rows $S$, columns $T$, a cross[^s1][^s2][^s3][^s4][^s5][^s6]
where the row has the trait. $A' $ is the set of rows carrying every trait in
$A$; $A'' $ is the closure. $A \to B$ **holds** iff $A' \subseteq B'$, i.e.
$B \subseteq A''$ — every row satisfying $A$ satisfies $B$ (Guigues & Duquenne 1986, eq. 1–2).

The set of all implications holding in the table is huge and redundant. Under
the two inference rules Guigues & Duquenne state (a union rule and
transitivity — the Armstrong rules, restated as such by Babin & Kuznetsov 2010), they prove (the theorem, p. 16):

> every minimal subfamily inferring the whole family has the form
> $\{A \to A'' : A \in \mathcal{R}\}$, where $\mathcal{R}$ picks one
> representative per equivalence class of **minimal nodes**, and **all such
> subfamilies have the same cardinality**, equal to the number of minimal
> nodes.

The minimal nodes are today called **pseudo-intents**: $P \neq P''$, and
$Q'' \subseteq P$ for every pseudo-intent $Q \subsetneq P$ (Babin & Kuznetsov
2010, §2). Taking the premises to be the pseudo-intents themselves makes the
family unique; the theorem alone leaves a choice of representative — in the
paper's own example one of the six implications is "$be \to T$ or
$ce \to T$". Ganter's (1984) `NextClosure` produces the closed sets of a
closure operator in lectic order and, on top of that, this minimal family.

Three properties decide what it is worth here:

1. **The input is an incidence and nothing else.** No $Y$, no $p(X,Y)$, no
   cutoff, no declared preference among survivors — contrast
   [[agglomerative-information-bottleneck]], [[specification-mining]],
   [[version-space]].
2. **The output size is not a knob.** The number of implications is a
   property of the table. Kuznetsov (2004) exhibits a context whose basis is
   exponential in $|S| \times |T|$ and proves that determining its size is
   $\#P$-hard; Kuznetsov & Obiedkov (2008) place the counting problem in
   $\#P$-complete and give the reduction to functional dependencies, under
   which the pseudo-intents are the premises of a minimum cover.
3. **Cheapness is not among its properties.** Recognising a pseudo-intent is
   coNP-complete (Babin & Kuznetsov 2010); the premises cannot be enumerated
   in lectic order with polynomial delay unless P = NP (Distel & Sertkaya 2011).

## Known as

| Name | Where | exact / close | Gloss |
|---|---|---|---|
| Duquenne-Guigues basis, Guigues-Duquenne base | formal concept analysis | exact | the usual name for the object of the 1986 theorem |
| stem base (*Stammbasis*) | FCA, Ganter & Wille tradition | exact | same family, German-school name |
| canonical basis / canonical base | FCA | exact | the version fixed by taking pseudo-intents as premises |
| minimal family of informative implications | Guigues & Duquenne 1986 | exact | the authors' own phrase |
| minimum cover of functional dependencies | database theory | close | Kuznetsov & Obiedkov's (2008) reduction identifies the premises; a cover is stated relative to a given dependency set, the basis relative to a table |
| pseudo-intent, pseudo-closed set, minimal node | FCA | *not this concept* | the premise object the basis is indexed by, with its own coNP-complete recognition problem |
| concept lattice, Galois lattice | FCA | *not this concept* | the other artifact computed from the same table — a hierarchy of closed sets, not a rule set |
| association-rule basis | data mining | *not this concept* | computed under support and confidence cutoffs, so a rule with one counterexample may survive; an implication here admits no exception |

## Transfer

| | |
|---|---|
| **In its home field** | a psychology / taxonomy data table: subjects × dichotomous traits, and the dependencies among traits a clinician might want |
| **Here** | rows are the worlds still in $W$ (or the recorded answer episodes), columns are the answers each admits; the basis is the distillate of the record |
| **What survives** | the guarantee itself, which assumes nothing: for *any* binary incidence there is a complete set of implications of provably minimum cardinality, computable without probability, without a declared relevance variable and without a ranking over survivors — so the choice the other stall-8 procedures leave open is simply absent here |
| **What does not** | the reading. An implication of the table says "no recorded row violates it", not "true of $W$"; and the output is a closure system, not a single world — $\lvert W\rvert \to 1$ is not reached, the surviving worlds are the closed sets, which are still many |

## Limits

- **The primary texts were not read verbatim here.** Guigues & Duquenne 1986
  is confirmed as the listed work and as the origin of the theorem via the FCA
  literature, but the page-16 wording, eq. 1–2 and the six-implication example
  ("$be \to T$ or $ce \to T$") are taken from secondary restatements and were
  not extracted from the PDF [?]; likewise the pseudo-intent definition and
  the Armstrong-rule restatement attributed to Babin & Kuznetsov 2010, §2 —
  their coNP-completeness result is directly confirmed, that definitional
  locator is not [?]. If either locator is wrong, the attribution moves, not
  the mathematics: the theorem and the complexity results are uncontested in
  the FCA literature.
- **The claim that no ranking is needed rests on the table being complete and
  two-valued.** There is no cell for "not asked" or "don't know": an
  unanswered question must be coded as absence, and absence manufactures
  implications that the record does not support. Where the record is partial,
  this note's central advantage is gone.
- **Minimum in count, not in length.** The theorem counts implications and
  says nothing about the total size of the premises, so "smallest complete
  set" is not "shortest to read".
- **Uniqueness is a convention, not a consequence.** What the theorem gives is
  equal cardinality plus a choice of representative per class; uniqueness
  comes from stipulating pseudo-intents as premises.
- **Zero noise tolerance.** One erroneous row deletes every implication it
  violates and changes the basis non-locally, with no signal — the same
  fragility as [[version-space]]'s collapse, with the opposite symptom
  (silent shrinkage instead of an empty space).
- **The mapping from answers to attributes is this wiki's**, and no cited
  source makes it; Guigues & Duquenne write about traits of subjects.

## Related

[[version-space]] · [[backbone-of-a-formula]] · [[specification-mining]] · [[attribute-exploration]] · [[distillation-input-debt]] · [[sufficient-statistic]]

[^s1]: babin-2010
[^s2]: distel-2011
[^s3]: ganter-1984
[^s4]: guigues-1986
[^s5]: kuznetsov-2004
[^s6]: kuznetsov-2008
