---
description: "A collective belief state must separate agnosticism (no reason either way) from conflict (reasons both ways); modular, transitive strict-likelihood relations do this and total preorders cannot."
aliases: ["generalized belief state", "modular transitive relation", "indifference versus conflict"]
sources: ["maynardzhang-2003"]
---
# Conflict versus agnosticism in a collective belief state

A group that has no opinion about options a and b and a group split over a and b look identical in a total preorder or any quasi-transitive relation, yet they should be treated differently. The paper's example: if everyone is indifferent between two movies, a passerby's preference for one can be adopted; if the group was already divided, one should hesitate to let one new supporter decide.[^c1] The underlying cause is the totality assumption, which the authors read as an assumption that conflicts do not exist.[^c2]

## The representation

Take strict likelihood as primitive: a ≺ b means "there is reason to consider a as strictly more likely than b." Then agnosticism (x ~ y) holds when neither x ≺ y nor y ≺ x, and conflict holds when both do. A generalized belief state is a relation over possible worlds that is transitive and modular (x ≺ y implies x ≺ z or z ≺ y for every z).[^c3]

Why modularity: transitivity of strict likelihood alone does not make agnosticism transitive (W={a,b,c}, ≺={(a,c)} gives a~b and b~c but not a~c). Given transitivity, agnosticism is transitive exactly when ≺ is modular (Proposition 5).[^c4]

Structure theorem (Proposition 7): a relation is a belief state iff the worlds partition into ordered blocks, each block either fully connected (all pairs in conflict) or fully disconnected (all pairs agnostic), with blocks strictly ordered against each other.[^c5] Total preorders are exactly the reflexive belief states, and their asymmetric restrictions (conflict-free states) the irreflexive ones. Conflicts are themselves transitive, because they are inferred from cycles of opinions, not just from pairwise disagreement.[^c6]

Consequence for conditional beliefs: a state can be agnostic about a conditional belief (the choice set of p-worlds is fully disconnected) or in conflict about it (fully connected), which are different states of knowledge.[^c7]

## Limits

- Conflict here is purely structural (a cycle of strict opinions); it carries no weights, so it cannot say how strong or how numerous the opposition is. The paper handles quantity only through a separate voting extension.
- Worlds are finite; belief states are ordinal, not probabilistic.
- Source reliability enters only through the aggregation operator, not the representation.
- The claim that this is the "right" semantics rests on the paper's argument and examples, not an empirical test.

## Related

- [[agm-belief-revision]] — the total-preorder semantics over worlds that this generalizes
- [[possible-worlds]] — the objects the relation orders
- [[belief-base-revision]] — a neighbouring revision setting
- [[rank-lexicographic-source-aggregation]] — how such states are built from sources of unequal reliability

[^c1]: maynardzhang-2003 — "However, if the group was already divided over the relative merits of a and b, we would be"
[^c2]: maynardzhang-2003 — "is essentially an assumption that conflicts do not exist."
[^c3]: maynardzhang-2003 — "Definition 6 A generalized belief state ≺ is a modular, transitive relation over W. The"
[^c4]: maynardzhang-2003 — "Proposition 5 Suppose a relation ≺ is transitive and ∼ is the corresponding agnosticism"
[^c5]: maynardzhang-2003 — "Every Wi is either fully connected"
[^c6]: maynardzhang-2003 — "Proposition 8 T ⊂ B and is the set of reflexive relations in B."
[^c7]: maynardzhang-2003 — "about this belief, written Con(p?q), if the choice set is fully connected."
