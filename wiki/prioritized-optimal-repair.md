---
description: "Facts carry a priority; among symmetric-difference repairs, only those no preferred swap can improve count as optimal, in three nested kinds: Pareto, global and completion."
aliases: ["preferred repairs", "optimal repairs of prioritized databases", "Pareto-optimal repair", "globally-optimal repair", "completion-optimal repair"]
sources: ["doi-10-48550-arxiv-2306-03523"]
---
# Prioritized optimal repair

A prioritized database is a database, its constraints, and a priority relation: "preferred repair actions are specified via a binary priority relation over (negated) facts."[^c1] Two facts can be in conflict, and the priority says which one should be kept when the constraints force one to go. The priority does not change which databases count as repairs. It selects among them, so it removes candidates before any query is asked.

Three optimal families follow from the priority, and each is stricter than the one before. A Pareto improvement of a repair R is a consistent database B such that some fact B gains is preferred to every fact B loses: "A Pareto improvement of R is a database B consistent". A repair is Pareto-optimal when it has no Pareto improvement.[^c2] A global improvement relaxes the condition: every lost fact must be beaten by some gained fact. The paper notes that "A Pareto improvement is also a global improvement", so the globally-optimal repairs are a subset of the Pareto-optimal ones.[^c3] A completion-optimal repair is a globally-optimal repair for some completion of the priority to a total order, and the paper shows that "there always exists at least one completion" optimal repair, so the family is never empty.[^c4]

The total case is the sharp one. "Proposition 4. If ≻ is total, then" the set of Pareto-optimal repairs has exactly one member, so the three families collapse and a single repair is the basis for answering.[^c5] This is the mechanism by which a complete ranking of reliability removes the choice that the other readings must handle; a partial priority leaves several repairs standing.

The paper's main computational finding is that the priority does not make answering harder. Checking whether a candidate is a repair is "Theorem 1. X-repair checking is coNP-complete in data", for the Pareto and global families.[^c6] The abstract states the consequence for answering: "that adopting optimal repairs does not increase the complexity of inconsistency-tolerant query answering".[^c7] The readings applied to these repairs are those of consistent-query-answering.

What survives the transfer is the operation itself: a preference over items that conflict can prune the admissible versions of the information before any answer is read. What does not survive is the input. The priority is a pairwise relation over facts that share a violation, and the paper treats it as given. A source's reliability is rarely offered as such a relation; where a ranking of sources exists, as in [[source-credibility-hierarchy-in-knowledge-conflicts]], it is a ranking of kinds of source, not of the specific facts they contribute (my inference).

## Limits

- The priority is an input, and the paper does not say how to obtain one. For a question about which source to believe, the relation would have to be elicited and justified. Nothing in the text supplies that step.
- The results are data complexity, in the worst case over databases, with constraints and queries fixed. They do not measure the cost on any particular instance.
- The paper also identifies Pareto-optimal repairs with founded, grounded and justified repairs of active integrity constraints: "Pareto-optimal repairs in our setting correspond to founded,".[^c8] That is a second name for the same objects in another field and is not evidence that the notion matches how people revise beliefs.
- The published version misreported a row of Table 1 for denial constraints under brave and intersection semantics; the correction is noted in consistent-query-answering, and this note's complexity figures follow the corrected version.
- Completion-optimality depends on the existence of completions, and the paper's greedy construction for one of them "does not run in polynomial time" in general, so the family is defined but not cheap to compute.[^c9]

## Related

- consistent-query-answering — the brave, CQA and intersection readings applied to the preferred repairs.
- [[symmetric-difference-repair]] — the repair set the priority acts on, including fact additions.
- [[source-credibility-hierarchy-in-knowledge-conflicts]] — an LLM's ranking of conflicting sources by institution; a priority of this kind, if elicited, is the input the formalism needs (my inference).

[^c1]: doi-10-48550-arxiv-2306-03523 — "preferred repair actions are specified via a binary priority relation over (negated) facts"
[^c2]: doi-10-48550-arxiv-2306-03523 — "A Pareto improvement of R is a database B consistent"
[^c3]: doi-10-48550-arxiv-2306-03523 — "A Pareto improvement is also a global improvement"
[^c4]: doi-10-48550-arxiv-2306-03523 — "there always exists at least one completion"
[^c5]: doi-10-48550-arxiv-2306-03523 — "Proposition 4. If ≻ is total, then"
[^c6]: doi-10-48550-arxiv-2306-03523 — "Theorem 1. X-repair checking is coNP-complete in data"
[^c7]: doi-10-48550-arxiv-2306-03523 — "that adopting optimal repairs does not increase the complexity of inconsistency-tolerant query answering"
[^c8]: doi-10-48550-arxiv-2306-03523 — "Pareto-optimal repairs in our setting correspond to founded,"
[^c9]: doi-10-48550-arxiv-2306-03523 — "does not run in polynomial time"
