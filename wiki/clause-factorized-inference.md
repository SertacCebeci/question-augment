---
description: "Splitting a conjunctive logic query into independent clauses, each scored only over the detections it names, cuts the hypothesis count from N^M to a sum of smaller products."
aliases: ["clause-level factorization", "conditional clause computation", "factorized logic inference"]
sources: ["arxiv-2512-14102"]
---
# Clause-factorized inference over conditioned subsets

Scoring a logic query against an image means deciding which detection plays which role in the query. "Given N object detections and a query involving M entities, the total number of possible hypotheses corresponding" to assignments of entities to detections follows directly from that setup.[^f1] Written out, that is N to the power M candidate assignments. With a hundred detections and ten entities the count is 10^20, which the authors call intractable: "rendering exhaustive inference computationally intractable due to the exponential growth of the hypothesis space."[^f2]

Two moves reduce the cost, and they are separate. The first is structural. The FOL expression is split into clauses that can be scored on their own: the method factorizes "the logic in clauses that can be computed independently of each other, and then combined at the end of the computation."[^f3] The example is that "a clause expressing that a bridge is left of a storage tank can be evaluated separately" from a clause about two harbors being close.[^f4]

The second is conditioning. Each clause is evaluated only over the detections of the categories it names, not over all detections. The paper works one example with 100 detections: 10 bridges, 5 storage tanks, 4 harbors, 10 ships, and the rest. The bridge-left-of-tank clause then needs 10 times 5 hypotheses, a ternary ship clause needs 10 times 10 times 10, and a harbor-near-harbor clause needs 4 times 4. The total is 1,066 hypotheses (50 + 1,000 + 16), which the authors set against the 10^20 combinations: the total is "many orders of magnitude smaller than the 1020 combinations."[^f5] The summary claim is that "detection-level filtering enables tractable inference over rich and expressive queries."[^f6]

Why the split can be exact: in the probabilistic semiring that the retrieval method uses (see [[neurosymbolic-text-to-logic-retrieval]]), conjunction is a product and each predicate takes a maximum over object tuples. When two clauses share no entity, their maxima multiply to the same score as a joint evaluation, so the per-clause work is not an approximation. My inference: the paper's examples are entity-disjoint clauses. The text does not say how a clause that shares a query entity with another is handled, and that is the case where a naive split would stop being exact.

## Limits

- The worst case stays exponential. A single clause can still be large: "Sometimes a logical clause can still have seven entities for instance when seven ships are arranged in a column," and "detections, this will still lead to a huge number of hypotheses, even with the proposed strategy."[^f7]
- The 1,066 figure is the authors' worked example on a hypothetical scene. It is a count of hypotheses, not a measured runtime. The paper's execution-time claim rests on precomputed predicates: "in case in which the predicates are precomputed, execution time is reduced at the level of" neural approaches.[^f8]
- The candidate count is not reduced by the detector. The text says that "a low detection threshold is applied" to minimise false negatives, so the detector does not shrink the candidate pool much.[^f9]
- Parallelism is proposed, not tested: the authors name "parallelizing the reasoning process across different groups of objects" as a remedy for large clauses.[^f10]
- The benefit is shown for query size and detection count. The text does not report how the count or the runtime scales beyond the examples it gives.

## Related

- [[neurosymbolic-text-to-logic-retrieval]] — the retrieval pipeline whose inference this factorization makes tractable
- [[possible-worlds]] — the general notion of a hypothesis space; here the space is a finite set of entity-to-detection assignments, and nothing is believed about it

[^f1]: arxiv-2512-14102 — "Given N object detections and a query involving M entities, the total number of possible hypotheses corresponding"
[^f2]: arxiv-2512-14102 — "rendering exhaustive inference computationally intractable due to the exponential growth of the hypothesis space"
[^f3]: arxiv-2512-14102 — "logic in clauses that can be computed independently of each other, and then combined at the end of the computation"
[^f4]: arxiv-2512-14102 — "a clause expressing that a bridge is left of a storage tank can be evaluated separately"
[^f5]: arxiv-2512-14102 — "which is many orders of magnitude smaller than the 1020 combinations"
[^f6]: arxiv-2512-14102 — "detection-level filtering enables tractable inference over rich and expressive queries"
[^f7]: arxiv-2512-14102 — "detections, this will still lead to a huge number of hypotheses, even with the proposed strategy"
[^f8]: arxiv-2512-14102 — "in case in which the predicates are precomputed, execution time is reduced at the level of"
[^f9]: arxiv-2512-14102 — "a low detection threshold is applied"
[^f10]: arxiv-2512-14102 — "parallelizing the reasoning process across different groups of objects"
