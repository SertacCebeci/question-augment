---
description: "Compensatory leakage: lower-priority gains overturn a decision an earlier criterion fixed, a flaw of scalar combination that accurate component predictions cannot reveal; testable by stress."
aliases: ["priority-violation rate", "ordinal fidelity violation", "unauthorized compensation"]
sources: ["arxiv-2601-12547", "doi-10-48550-arxiv-2605-30244", "doi-10-48550-arxiv-2609-38847"]
---
# Compensatory leakage

Defined by Sengupta and Panda for clinical decision models. A decision rule has ordinal fidelity when its recommendation respects the first resolved criterion that separates the surviving alternatives: if that criterion favors a over b, the rule must not pick b unless the order is explicitly revised.[^c1] Leakage is the violation.

## Mechanism

Compensatory leakage is an unauthorized reversal: lower-priority gains overturn a decision already determined by an earlier criterion, with no explicit revision of the ordering.[^c2] It lives in how components are combined, so a scalar score can leak even when each component prediction is accurate; the paper says the error "lies in the semantics of combination rather than the calibration of individual outcomes".[^c3] Calibration metrics on each outcome therefore cannot detect it.

The proposed stress test holds an early threshold distinction fixed and progressively improves lower-priority features of the losing action. If the unconstrained score eventually flips the recommendation, the model has introduced a compensation the ordered program did not authorize.[^c4] Over a suite of cases the flips are summarized as a priority-violation rate. The same logic motivates implementing a priority as a hard or ordered constraint rather than a finite penalty, since with a soft penalty enough gains elsewhere can overturn it.

The reference for fidelity is the currently justified ordered program, not historical clinician behavior; past choices are evidence about structure, not ground truth.[^c5]

An RL reward built to this prescription is one case. RLR3 keeps the essential criteria as a multiplicative gate on the weighted sum of the rest, so no gain on additional criteria can lift a response past a failed essential one. The authors give the same reason: additional criteria should "refine the score only after the essential criteria are satisfied."[^c6] The gate is a hard constraint in the sense above; the paper reports its effect only jointly with other components, so it does not measure leakage itself (see essential-gated-reward-aggregation).

The same flaw shows up without any stated ordering when a policy is trained against a weighted sum of rubric verdicts. Under such a sum every criterion pays a fixed share of the weight, so a policy can buy back a missed critical criterion with easier ones. In clinical consultation, the trained policy's coverage rose while its appropriateness on held-out physician criteria fell: "The policy that results scores higher and answers worse."[^c7] With the criterion text fixed, changing only the aggregation moved that collapse in medicine and dialogue: "With the criterion text fixed, changing only the aggregation moves the collapse in medicine and dialogue".[^c8] Whether this is leakage in the Sengupta and Panda sense is my inference: a rubric has no ordered program, so there is no authorized order for a reversal to violate. The repair the paper proposes, grouping criteria so that a unit pays only when all its parts hold, is in conjunctive-criterion-grouping.

## Limits

- The test and the rate are proposed, not run: the paper reports no measured violation rates for any model.
- It presupposes an explicit ordered program. Where trade-offs are legitimately cardinal, "leakage" is just ordinary trading off and not an error.
- The paper concedes that ordered priority is not a universal descriptive model of human judgment; compensatory integration also occurs.
- The rubric-RL evidence is one clinical setting with an LLM judge and no flip test: it shows a drop in held-out appropriateness under compensation, not a measured priority-violation rate (my inference).

## Related

- [[threshold-sufficient-abstraction]] — the ordered-threshold framework that supplies the reference order.
- [[rank-lexicographic-source-aggregation]] — a lexicographic aggregation that is leak-free by construction.
- [[action-sufficient-compression]] — shows a scalar summary can hide an action-relevant distinction, a parallel failure.
- conjunctive-criterion-grouping — the rubric-RL case of this flaw, and a remedy that groups criteria into units that must all hold

[^c1]: arxiv-2601-12547 — "A decision rule has ordinal fidelity to Qx when its recommendation respects the first resolved threshold that distinguishes the surviving alternatives."
[^c2]: arxiv-2601-12547 — "gains overturn a decision already determined by an earlier criterion without explicit revision of that ordering."
[^c3]: arxiv-2601-12547 — "because the error lies in the semantics of combination rather than the calibration of individual outcomes."
[^c4]: arxiv-2601-12547 — "If an unconstrained score eventually flips the recommendation, the model"
[^c5]: arxiv-2601-12547 — "Historical choices are evidence about structure, not ground truth."
[^c6]: doi-10-48550-arxiv-2605-30244 — "after the essential criteria are satisfied"
[^c7]: doi-10-48550-arxiv-2609-38847 — "The policy that results scores higher and answers worse"
[^c8]: doi-10-48550-arxiv-2609-38847 — "With the criterion text fixed, changing only the aggregation moves the collapse in medicine and dialogue"
