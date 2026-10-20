---
description: "A repair may add missing facts as well as delete wrong ones once a constraint can be violated by an absence; for denial constraints deletion alone suffices, so the notions coincide."
aliases: ["delta-repair", "∆-repair", "symmetric difference repair", "subset repair"]
sources: ["doi-10-48550-arxiv-2306-03523"]
---
# Symmetric-difference repair

The usual repair of an inconsistent database is a subset repair: keep the stored facts, remove some of them until the constraints hold, and remove as little as possible. This is enough when the constraints are denial constraints, such as functional dependencies. The paper states the limit of that setting: "consistency can be restored only by removing information".[^c1]

A symmetric-difference repair, or ∆-repair, drops the restriction to deletion. The definition is "A symmetric difference repair, or ∆-repair, of D" with the closeness measured as the symmetric difference of the repair and the original: a repair R satisfies the constraints and no consistent database has a strictly smaller symmetric difference with D.[^c2] Closeness counts both kinds of change, and the paper argues that this is the sensible choice: "it makes sense to consider symmetric difference repairs obtained using both fact additions and deletions".[^c3]

The mechanism that needs additions is that a universal constraint can require a fact to be present when another fact is. The paper's example is a rule that a patient "cannot receive a certain treatment without a positive test for a given mutation". A violation of such a rule may come from an erroneous treatment record or from a missing test result, and the two call for opposite repair actions: delete the record, or add the test.[^c4] A subset repair can only do the first. The paper gives the reason: "contribute to the violation of a universal constraint" applies to the absence of a fact, so conflicts must include negated facts, where "¬P (c) indicates that P (c) is absent".[^c5]

The two notions coincide for denial constraints, because "adding facts cannot resolve a violation of a denial constraint".[^c6] The difference appears only when the constraints can be violated by absence. A second difference is existence. An empty database satisfies any set of universal constraints, so a subset repair always exists, whereas a superset repair may not: "the case that no ⊇-repair exists".[^c7]

What survives the move to asking and answering is that "closest consistent version" can be closer in more than one direction: a question about a record can be resolved by discarding the record or by supplying what it lacks, and these are different repairs. What does not survive is the formal metric. The paper's closeness is a symmetric count of facts, not a judgment about which correction is plausible, and it does not model the cost of inventing a fact the source never held (my inference).

## Limits

- The ∆ closeness is a choice of metric. The paper's motivation is expressiveness: universal constraints "can be used to express data completeness assumptions and other kinds of domain knowledge".[^c8] That is an argument that the notion is needed, not a test that people reason with it.
- Additions are weighted the same as deletions in the definition. Nothing in the definition says that adding a fact is less credible than removing one; that asymmetry, if wanted, has to come from a priority, which is a separate notion (see [[prioritized-optimal-repair]]).
- Repairs can be numerous and their intersection need not be consistent, which the paper notes for the optimal repairs.[^c9] The notion of repair alone does not tell an answerer which repair to trust.
- The text read here gives the definitions and the example, not an empirical comparison of subset and ∆-repairs on real data.

## Related

- consistent-query-answering — the readings (brave, CQA, intersection) that quantify over ∆-repairs.
- [[prioritized-optimal-repair]] — a preference over facts, including negated facts, that selects among ∆-repairs.
- [[evidence-conflict-type]] — conflicting sources differ in kind, and a missing fact and a false one call for different corrections (my inference from the same distinction).

[^c1]: doi-10-48550-arxiv-2306-03523 — "consistency can be restored only by removing information"
[^c2]: doi-10-48550-arxiv-2306-03523 — "A symmetric difference repair, or ∆-repair, of D"
[^c3]: doi-10-48550-arxiv-2306-03523 — "it makes sense to consider symmetric difference repairs obtained using both fact additions and deletions"
[^c4]: doi-10-48550-arxiv-2306-03523 — "a certain treatment without a positive test for a given mutation, with violations indicating either an erroneous treatment"
[^c5]: doi-10-48550-arxiv-2306-03523 — "contribute to the violation of a universal constraint"
[^c6]: doi-10-48550-arxiv-2306-03523 — "adding facts cannot resolve a violation of a denial constraint"
[^c7]: doi-10-48550-arxiv-2306-03523 — "the case that no ⊇-repair exists"
[^c8]: doi-10-48550-arxiv-2306-03523 — "which can be used to express data completeness assumptions and other kinds of domain knowledge"
[^c9]: doi-10-48550-arxiv-2306-03523 — "the intersection of the optimal ∆-repairs may be inconsistent w.r.t. C"
