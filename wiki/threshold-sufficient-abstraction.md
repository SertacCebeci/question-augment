---
description: "Order a decision objective as repeating threshold propositions and refine the model only until the survivor set is a single action; unreached later thresholds need no added resolution."
aliases: ["ordered threshold refinement", "decision-sufficient abstraction", "ordinal-first objective", "purpose before fidelity"]
sources: ["arxiv-2601-12547"]
---
# Threshold-sufficient abstraction

A position paper on clinical AI (Sengupta and Panda) argues that what a model must represent is set by the decision's objective, not by completeness. Every finite model maps the world many-to-one, so the question is which distinctions may be collapsed "without changing the intended decision".[^c1]

## Mechanism

The primitive objects are objective-threshold propositions, not variables with a fixed rank. One dimension can recur at progressively finer thresholds: mortality below 10% early, below 5% later; cost below INR 1000 as feasibility, below INR 100 as a later preference. The objective is an ordered list q1, q2, ..., qm over such propositions.[^c2] A late threshold is "not a tiny coefficient": it contributes nothing while an earlier criterion discriminates, and can decide the case when all earlier ones tie.[^c3]

Execution is sequential set reduction. Start with all actions; at each criterion keep those with the best threshold status. If one action survives, the choice is resolved and later criteria are never reached.[^c4] An abstraction is threshold-sufficient through criterion k if it preserves the survivor set after the first k thresholds.[^c5] Representation therefore refines only when the decision reaches a threshold that needs finer discrimination.

Uncertainty is handled by a third status. A threshold may be met, unmet or "?" (evidence or resolution does not establish it); a potentially decisive "?" pauses reduction and is not ranked between 0 and 1.[^c6] Effort (data, preference question, submodel refinement) is aimed at that threshold instead of added globally. Lower-priority gains may not quietly turn it into a soft penalty.

The paper pairs relevance with evidence: justified model detail requires both decision relevance and evidential support.[^c7] A latent variable needed to estimate an already-reached threshold must still be modeled; the rule only forbids raising resolution to separate alternatives on an unreached objective.

## Limits

- It is a position paper with a conceptual sufficiency condition; no experiment shows that models built this way decide better. The paper itself calls the exact definition idealized and suggests a probabilistic or robust version, which it does not develop.
- The advantage depends on a correct ordered program. A factor missing from the knowledge, evidence, objective or model can still flip an early threshold; the paper claims only that such failures are easier to localize.
- It does not claim ordinal rules beat expected utility when cardinal trade-offs are well specified. Local cardinal models remain for tied survivors.
- The clinical-reasoning literature it cites shows selective, compressed representations in experts, not that clinicians reason lexicographically (the paper says this).
- Who builds and orders the thresholds is left to a clinician-patient-AI specification loop that is described, not tested.

## Related

- [[action-sufficient-compression]] — the same sufficiency idea as a policy-equivalence quotient; here the equivalence is induced by ordered thresholds.
- [[compensatory-leakage]] — the failure that the ordered semantics is meant to prevent.
- [[rank-lexicographic-source-aggregation]] — another lexicographic ordering, over sources rather than outcomes.
- [[ignorance-preserving-belief-mass]] — a comparable refusal to collapse "unknown" into a number.

[^c1]: arxiv-2601-12547 — "The scientific problem is to decide which distinctions may be collapsed"
[^c2]: arxiv-2601-12547 — "The primitive objects in this framework are objective-threshold propositions, not raw dimensions with one permanent rank."
[^c3]: arxiv-2601-12547 — "A low-priority price threshold is not a tiny coefficient."
[^c4]: arxiv-2601-12547 — "If |Sk | = 1, the choice is resolved and later criteria are not reached."
[^c5]: arxiv-2601-12547 — "Call an abstraction threshold-sufficient through criterion k if it preserves"
[^c6]: arxiv-2601-12547 — "A potentially decisive “?” pauses ordered"
[^c7]: arxiv-2601-12547 — "Justified model detail = decision relevance AND evidential support."
