---
description: "From an inconsistent base, accept a conclusion iff some consistent minimal argument supports it and none supports its negation: between cautious and credulous, never pairwise contradictory."
aliases: ["argumentative inference", "argumentative consequence relation", "inconsistency-tolerant inference"]
sources: ["benferhat-1993"]
---
# Argumentative consequence

Reasoning from an inconsistent knowledge base can restore consistency, which throws information away and admits several different repairs, or cope with the inconsistency by a consequence relation that still says something.[^c1] Benferhat, Dubois and Prade define one such relation, built on arguments in the sense of Toulmin.

## Definition

An argument for a formula is a consistent sub-base that entails it and loses that entailment if any member is removed.[^c2] A formula is an argumentative consequence if the base contains an argument for it and none for its negation.[^c3] So a base holding only a statement and its negation does not yield everything: the relation rejects ex absurdo quodlibet, as paraconsistent logics do.[^c4] It is non-monotonic, but only when the base is inconsistent; on a consistent base it equals classical entailment.[^c5]

## Place among the alternatives (flat bases)

Four relations were compared on a base with no priorities:

- Free consequence: entail from the formulas involved in no minimal inconsistency. Very conservative.
- Universal (Rescher-Manor): entailed by every maximal consistent sub-base. Every free consequence is universal, not conversely.[^c6]
- Argumentative: some maximal consistent sub-base entails it and none entails its negation. Every universal consequence is argumentative, not conversely.[^c7]
- Existential: some maximal consistent sub-base entails it. Most adventurous; it can deliver both a formula and its negation.[^c8]

The authors call the universal relation "very conservative hence rather unproductive" and the existential one too permissive; the argumentative relation is the middle path that is more productive than the first and never pairwise contradictory.[^c9] The lexicographic selection (keep only the largest maximal consistent sub-bases) is not comparable with it: on the paper's example it infers a formula the argumentative relation refuses, because a rival argument exists, and misses one the argumentative relation accepts, since the selection deleted the premise that supports it.[^c10]

## Properties

- The AND rule fails: two conclusions can each be argued for, yet their conjunction has no argument. The authors present this as wanted, for cases where two compatible properties are believed for conflicting reasons.[^c11]
- Right weakening holds.[^c12]
- Conclusions group into "prime implicates", each coming from a different maximal consistent sub-base; these are distinct points of view that should not be mixed even when compatible.[^c13]
- Hidden contradictions survive: no two consequences are directly inconsistent, but three together can be. The authors call this a weakness: the relation "avoids obvious direct contradictions, but does not escape hidden ones".[^c14]

## For answering questions

A bare yes or no from the relation is "not really informative enough"; the system should also supply the argument, so the user can decide whether the plausible conclusions can be accepted together.[^c15]

## Limits

The paper gives results without proofs (they are deferred to a full report). It treats only finite propositional language, where all relations are syntax-sensitive because the base is not deductively closed. Computing every maximal consistent sub-base grows exponentially with the number of conflicts, as the paper itself notes. Nothing here tests whether human or model answerers benefit from this rule; that application is my inference. The later sections on prioritized (possibilistic) bases and source combination were not read here and are not claimed.

## Related

- [[consistent-answer-over-repairs]] — the database analogue of the universal relation: answer only what every repair supports
- [[truth-maintenance-system]] — the paper compares arguments to ATMS environments and nogoods
- [[agm-belief-revision]] — the restore-consistency alternative that this relation avoids
- [[conflict-versus-agnosticism-belief-state]] — a belief state that separates conflict from ignorance

[^c1]: benferhat-1993 — "There are two attitudes in front of inconsistent knowledge."
[^c2]: benferhat-1993 — "Def. 2: A sub-base Li of L is said to be an argument"
[^c3]: benferhat-1993 — "(i) there exists an argument for <1> in I., and"
[^c4]: benferhat-1993 — "paraconsistent logics [6], where they reject the principle"
[^c5]: benferhat-1993 — "means that the non-monotonicity only appears in the"
[^c6]: benferhat-1993 — "Proposition 1: Each Free-consequence is also a Me"
[^c7]: benferhat-1993 — "Proposition 3: Each Me-consequence of I. is also an"
[^c8]: benferhat-1993 — "drawback, since this approach may lead to inconsistent set"
[^c9]: benferhat-1993 — "conservative hence rather unproductive while the latter is"
[^c10]: benferhat-1993 — "not comparable as we see in the following example:"
[^c11]: benferhat-1993 — "Proposition 5 (failure of AND)"
[^c12]: benferhat-1993 — "Proposition 6: f- 9t, satisfies the property of Right"
[^c13]: benferhat-1993 — "express different points of views on what is the actual"
[^c14]: benferhat-1993 — "This result can be viewed as a weakness of the"
[^c15]: benferhat-1993 — "The system must also supply the argument for cj>."
