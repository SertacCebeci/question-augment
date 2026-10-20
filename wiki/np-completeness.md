---
description: "A problem is NP-complete when it is in NP and every NP problem reduces to it; Cook's 1971 theorem shows satisfiability is, so deciding whether a constraint set has any model is that hard."
aliases: ["NP-complete", "NP-complete problem", "Cook's theorem", "SAT is NP-complete", "NP-completeness of satisfiability"]
sources: ["cook-1971"]
---
# NP-completeness

> Deciding whether a set of answers, read as a propositional constraint set,
> has *any* consistent world at all is — in the worst case — as hard as
> hundreds of other problems that look nothing alike. Cook's 1971 theorem is
> where that fact was first proved.

## Definition / Mechanism

A set of strings is **NP-complete** (the term is later than this paper) when
it is accepted by some polynomial-time nondeterministic Turing machine and
every set so accepted reduces to it in polynomial time; Theorem 1 below
supplies the second half for {DNF tautologies}, hence for satisfiability.[^c7]

Cook defines one decision problem being no harder than another: $S$ is
**P-reducible** to $T$ iff a polynomial-time oracle ("query") machine decides
membership in $S$ given free yes/no answers about membership in $T$ — "there
is some query machine $M$ and a polynomial $Q(n)$ such that for each input
string $w$, the $T$-computation of $M$ with input $w$ halts within $Q(|w|)$
steps ... and ends in an accepting state iff $w \in S$"
(Cook (1971), Def. p.152).[^c3]

This is an oracle reduction, not the many-one form later hardness proofs
use. Mutual P-reducibility is an equivalence relation whose classes Cook
names: "The equivalence class containing a set S will be denoted by deg (S)
(the polynomial degree of difficulty of S)"
(Cook (1971), p.152).[^c9]

**Theorem 1**: "If a set S of strings is accepted by some nondeterministic
Turing machine within polynomial time, then S is P-reducible to {DNF
tautologies}" (Cook (1971), Thm. 1).[^c1]

Cook's proof: "Given an input w for M, we will construct a proposition
formula A(w) in conjunctive normal form such that A(w) is satisfiable iff M
accepts w. Thus ¬A(w) is easily put in disjunctive normal form (using De
Morgan's laws), and ¬A(w) is a tautology if and only if w ∉ S" — built in
time polynomial in $|w|$, $A(w)$ is a conjunction of clauses asserting a
valid accepting trace of $M$ on $w$
(Cook (1971), proof of Thm. 1).[^c8]

This wiki's reading of that proof: the query machine asks one question — is
$A(w)$ satisfiable — and returns the answer, so the construction is a
many-one (single-query) reduction to satisfiability; the modern restatement
"SAT is NP-complete" follows even though Cook's *definition* of
P-reducibility permits more.[^c10]

**Theorem 2**: "The following sets are P-reducible to each other in pairs
(and hence each has the same polynomial degree of difficulty): {tautologies},
{DNF tautologies}, D3 , {subgraph pairs}" (Cook (1971), Thm. 2).[^c2]

The first demonstrated family of what are now called NP-complete problems.

## Known as

| Name | Field | Relation |
|---|---|---|
| NP-complete / NP-complete problem | complexity theory (post-1970s usage) | exact — the class property this note defines (c7); the adjective applied to a set is the same object as the note's title |
| Cook's theorem | complexity theory | exact — this paper's own result, the theorem that first exhibits a member of the class |
| SAT is NP-complete / NP-completeness of satisfiability | complexity theory (post-1970s usage) | exact — restated in P/NP vocabulary this paper never uses (it names polynomial time $L^*$); the identity holds because the Theorem 1 construction is a many-one reduction (c10), not merely because Cook's oracle definition would allow one |

[^c4.1][^c4.2][^c4.3][^c4]

"P-reducible" and "polynomial degree of difficulty" are Cook's apparatus,
not names for the theorem, and are not aliases. "Cook–Levin theorem" is
under Limits.

## Why it matters

Read the held answers as a CNF formula and its models as the surviving $W$
([[possible-worlds]]); "do the constraints cohere?" (Consistency) is
then, on this note's reading, exactly deciding satisfiability, and no known
algorithm answers that in polynomial time in general — the same wall is
shared by every problem P-reducible to it.[^c11]

Cook named the open half himself: "{tautologies} is a good candidate for an
interesting set not in $L^*$, and I feel it is worth spending considerable
effort trying to prove this conjecture. Such a proof would be a major
breakthrough in complexity theory"
(Cook (1971), Discussion).[^c6]

That conjecture is P $\neq$ NP, still open. This wiki reads
[[backbone-of-a-formula]]'s hardness of separating forced from chosen
content and [[optimal-decision-tree]]'s hardness of exact tree construction
as downstream of exactly this fact: each is a reduction from a problem in
Theorem 1's class.[^c12]

## Transfer

| | Home field | Here |
|---|---|---|
| Object | a decision problem over strings, decided by a Turing machine | whether the answer record, read as a CNF constraint set, has any consistent world |
| What survives | worst-case intractability of the base decision, transferred along any P-reduction | |
| What does not | the machine/alphabet encoding; the asymptotic reading over a whole language rather than one transcript (single instances are often easy — [[backbone-of-a-formula]]'s Limits); Cook's *definition* of P-reducibility (oracle) is more permissive than the many-one reduction most later hardness citations here rely on, so a P-reduction in Cook's sense is not automatically many-one — only Theorem 1's own construction is (c10) | |

[^c5.1][^c5.2][^c5]

## Limits

- **No lower bound.** Cook proves hardness, not that {tautologies} is
  outside $L^*$; P vs NP is the unproven half, by Cook's own words above.
- **Worst case, not this transcript.** The theorem bounds the whole
  language, not any one formula; a real consistency check can be easy even
  when the general problem is provably hard.
- **This note's own readings.** c7, c10, c11 and c12 are this wiki's
  inferences, not statements in the source; c11 rests on reading the answer
  record as a CNF formula, which holds only when answers are propositional
  constraints.
- **Naming beyond this source is unverified.** The result is usually called
  the **Cook–Levin theorem**, crediting Leonid Levin's independent 1973
  proof; Levin's paper is not a source here, so that credit is unverified
  (see `new_gaps`). The many-one reduction standard for later proofs traces
  to Karp (1972), also not archived here.
- **Extract quality [?].** The archived `cook-1971` PDF (a scan) has no
  machine-readable text (0-character extract); quotes above come from a
  widely used retyped transcription of the same STOC 1971 paper (Tim
  Rohlfs, inf.unibz.it), matched to the ACM page range 151–158 but not
  checked page-by-page against the scan. Claims c1, c2, c3, c4.1, c6, c8
  and c9 are unverified — their quotes could not be located in a wiki
  extract for `cook-1971` — until the scan is OCR'd (`archive.py extract`)
  or the transcription is archived under that key, and the claims
  re-located.

## Related

[[backbone-of-a-formula]] · [[conflict-driven-clause-learning]] · [[optimal-decision-tree]] · [[possible-worlds]] · [[constraint-as-information]] · Consistency

[^c7]: cook-1971
[^c3]: cook-1971
[^c9]: cook-1971
[^c1]: cook-1971
[^c8]: cook-1971
[^c10]: cook-1971
[^c2]: cook-1971
[^c4.1]: cook-1971
[^c4.2]: cook-1971
[^c4.3]: cook-1971
[^c11]: cook-1971
[^c6]: cook-1971
[^c12]: cook-1971
[^c5.1]: cook-1971
[^c5.2]: cook-1971
[^c4]: cook-1971
[^c5]: cook-1971
