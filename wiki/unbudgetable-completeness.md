---
description: "**This wiki's inference, not a result.** An asker can hold an exact Three steps; the middle one is someone else's. **1. Completeness has a count,"
aliases: ["unbudgetable completeness"]
sources: ["distel-2011", "ganter-1984", "guest-2020", "kuznetsov-2004", "kuznetsov-2008", "mitchell-1982", "singh-2015", "wald-1945"]
---
# Unbudgetable completeness

> **This wiki's inference, not a result.** An asker can hold an exact
> completeness stopping rule, or a length it can forecast before starting. On
> the complexity facts the wiki now carries, it cannot hold both — and the
> useful half of that is what happens when the budget bites first.

## The claim

Three steps; the middle one is someone else's.[^s1][^s2][^s3][^s4][^s5][^s6][^s7][^s8]

**1. Completeness has a count, and the count is at least the basis size.**
[[attribute-exploration]] asks **at least one question per premise** of the
[[canonical-implication-basis]] of the final context: a confirmed query retires
one premise, and a refuted query costs a further question, since the
counterexample enters the context and the same premise is re-asked with a
smaller conclusion. The loop is Ganter's (1984); the identification of the
question count with the basis size is this wiki's accounting of it, not a bound
Ganter states — and the slack runs in the direction that makes the count
larger. So "no dependency among the declared attributes remains unasked" is not
a threshold on a statistic; it is an enumeration, and its length is a property
of the answers, not of the asker.

**2. That number is worst-case unbounded, uncountable in advance, and slow to
produce.**

- Kuznetsov (2004) exhibits a context whose basis is exponential in
  $|S| \times |T|$, closing a long-open question about the upper bound.
- Determining the basis size is $\#P$-hard (Kuznetsov 2004), $\#P$-complete
  with the reduction to functional dependencies (Kuznetsov & Obiedkov 2008) —
  so there is no counting the questions without asking them.
- Distel & Sertkaya (2011) show the premises cannot be enumerated in lectic
  order with polynomial delay unless P = NP, that unrestricted enumeration is
  at least as hard as listing the minimal transversals of a hypergraph, and
  that even minimal pseudo-intents are not enumerable in output-polynomial
  time unless P = NP. The gap between two consecutive questions is therefore
  not bounded either.

**3. Therefore (this wiki).** The property the complexity results oppose is not
a fixed length — few stopping rules have one — but **a computable estimator of
the length**. Four of the wiki's rules were read here, and each admits one:

| Rule read | What it admits as a forecast |
|---|---|
| [[sprt]] | the count is a random variable, but once a per-answer evidence rate is fixed, $E(n) = E(Z_n)/E(z)$ (Wald 1945, §4.1) estimates it |
| [[qualitative-saturation]] | a declared base size and [[run-length|run length]]; the stop is reported as $B{+}R$ at $T$, so the run is known up to its lag (Guest, Namey & Chen 2020) |
| the frontier row of [[stopping-rules]] — [[issue-tree]] | the remaining questions **are** the unopened branches, countable the moment the tree is drawn; that count exists because completeness there is relative to the taxonomy in force, not exhaustive over the dependencies among the declared attributes |
| [[version-space]] | the stop is structural ($S = G$), but the boundary sets are on hand and the instance selection is against the surviving set, so the remaining work is inspectable |

Exploration admits none of the four. $\#P$-completeness of the basis size says
there is no cheap estimator of the total to build a forecast from, and the
absence of polynomial-delay enumeration says the distance to the *next*
question is not bounded either — so no statistic of the transcript so far
yields a defensible forecast of how many questions remain. The exclusivity this
note claims is therefore narrow: **exact completeness over the dependencies and
a forecastable length are not held together by any rule read here**, and the
complexity results say why one should not expect a rule that does. A
completeness-seeking interview must carry an external budget *in addition to*
its internal termination, and the two are not reconcilable by better
estimation.

**The consequence worth designing for is the degradation mode.** Every prefix
of an exploration is *sound*: an accepted implication was confirmed and stays
confirmed whatever follows. So a run cut short by a budget returns a partial
basis plus the premise it was about to ask — a correct artifact with a named
frontier. A truncated [[version-space]] returns a set that is compact
(Mitchell 1982 represents it by $S$ and $G$) but not reduced to one world:
choosing a member needs a separately learned ranking the examples never
supplied (Singh & Gulwani 2015), and one erroneous answer empties it with no
way to tell a bad answer from a hypothesis language too poor. This wiki infers,
and no source states, that where the question count cannot be forecast the
right design choice is a procedure whose every prefix is an answer.

**What would refute it.** Exhibit a structural restriction that
question-answer records satisfy — bounded attribute degree, a bounded number
of distinct answer profiles — under which the number of pseudo-intents is
polynomial. The tradeoff would then be an artifact of adversarial contexts,
and a budget could be declared in advance after all.

## Known as

Not a term of art. "Unbudgetable completeness" is this wiki's name for the
composition of the complexity results on the canonical basis with the
question-per-premise structure of attribute exploration; the phrase should not
be searched for in the literature. Its parts are
[[canonical-implication-basis]] and [[attribute-exploration]].

## Transfer

| | |
|---|---|
| **In its home field** | complexity statements about enumerating pseudo-intents of an arbitrary formal context, proved by reduction from CNF satisfiability and hypergraph transversal problems |
| **Here** | read as a statement about the length of an interview that wants to leave no dependency unasked |
| **What survives** | the direction of the failure — the count is an output with no cheap estimator, so an interview length declared in advance is a guess and not a plan |
| **What does not** | the arithmetic. Worst-case hardness over all contexts says nothing about the particular table an interview produces; this note converts a lower bound on the hardest instance into a design rule, which is a weaker move than the theorems support |

## Limits

- **This is a conjecture and is typed as one.** No source composes the
  enumeration complexity with a stopping rule for asking; Kuznetsov and
  Distel & Sertkaya write about formal contexts, not interviews.
- **No exhaustive count of the wiki's stopping rules was made.** Step 3 reads
  four rules, named in the table; Stopping carries more. The
  exclusivity claim reaches exactly those four, and any unread rule that is
  both exhaustive over dependencies and forecastable refutes it.
- **Worst case is doing the work.** An answer record is one instance. If real
  transcripts fall in an easy class, step 3 collapses — which is exactly the
  refutation route above, and it is untested here.
- **"One question per premise" is an accounting, twice over.** It is this
  wiki's reading of Ganter's loop rather than a bound he states, and it is the
  algorithm's unit rather than a human one: a person may need several
  utterances to settle one implication, or may settle several at once.
- **It says nothing about completeness of the attribute set.** The claim is
  about exhausting the dependencies among declared attributes; an axis never
  declared is invisible here, as in [[unknown-unknowns]].
- The soundness-of-every-prefix property is read off the algorithm's
  structure, not taken from a cited theorem.

## Related

[[attribute-exploration]] · [[canonical-implication-basis]] · [[stopping-rules]] · [[qualitative-saturation]] · [[version-space]] · [[sprt]]

[^s1]: distel-2011
[^s2]: ganter-1984
[^s3]: guest-2020
[^s4]: kuznetsov-2004
[^s5]: kuznetsov-2008
[^s6]: mitchell-1982
[^s7]: singh-2015
[^s8]: wald-1945
