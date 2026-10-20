---
description: "An evidence unit is decision-critical when some allowed edit to it, rules and other evidence held fixed, changes the decision; a missing intervention does not show it is not."
aliases: ["decision-critical evidence", "evidence criticality", "counterfactual evidence criticality", "decision-sensitive evidence"]
sources: ["doi-10-48550-arxiv-2609-39608"]
---
# Evidence decision-criticality

Evidence is decision-critical for a case when an allowed change to it would alter the decision the rule returns. The construction fixes the governing rule, the decision query, the condition descriptions, the aggregation function and all non-target evidence, and then asks whether an intervention on the target evidence unit changes the decision: "intervention can change the decision, the target evidence unit is decision-critical."[^c1] The property is existential over interventions. One decision-changing edit is enough for a positive label, and the set of edits is fixed by the kinds of change allowed, "specified independently of their outcomes."[^c2]

The property belongs to a case and an evidence unit together, not to the evidence alone. The same wrong judgment can be harmless in one case and reversing in another, because the other conditions decide whether the change reaches the outcome. The paper's example is a residency condition under an AND rule: a mistaken residency judgment "can reverse approval when" employment is satisfied, and it "leaves rejection unchanged when employment fails."[^c3] Criticality is therefore a fact about the pair (case, evidence), and it cannot be read off a single judgment in isolation.

The negative side is asymmetric. A decision-changing intervention settles a positive. A negative needs more: "a negative label requires either a complete mapping that rules out a change" or a review of the rule and case evidence. "Missing interventions alone do not establish a negative label."[^c4] So trying a few edits and seeing no change does not show that the evidence is non-critical. My inference is that the question "is this decisive?" can be settled "yes" by one example, while "no" needs a closed argument about all allowed edits.

The paper also trains a direct version of the question. The trained model receives the original case and the target evidence, and is asked whether changing that evidence "could change the decision under the governing rule."[^c5] No edited case and no condition labels are in the prompt. On adapted ContractNLI and ShARC cases this direct judgment "achieves 68.28% accuracy, outperforming all six baselines."[^c6] The table reports the spread across runs as "68.28 ± 2.01",[^c7] so the gap to the baselines is a few points, not a large margin.

## Limits

The setting is narrow. "Our experiments study evidence criticality in a controlled setting with textual evidence" and three-valued conjunction or disjunction rules.[^c8] Nothing here shows the notion carries to other aggregation rules, to several evidence units changed together, or to evidence that is not text. The paper lists these as future work.

The labels are only as complete as the allowed edit set. A negative label depends on the constructor having covered the relevant edits, or on a complete mapping that rules changes out. The paper says offline construction "uses annotated condition states and decisions" for the original cases,[^c9] so the reference labels inherit the annotation. My inference: in a new domain without such annotation, the negative class is the hard part to establish.

Accuracy does not measure balance. The paper notes that "Higher accuracy alone therefore does not ensure more balanced criticality judgments."[^c10] A reader should check the balanced accuracy and the class counts before taking an accuracy figure as evidence that criticality is being detected.

## Related

- [[condition-absorption-of-evidence-error]] — the mechanism that makes criticality case-dependent: an evidence change reaches the decision only through the condition it changes, and a change to a condition does not always change the outcome.
- [[structural-versus-parametric-evidence]] — also asks which evidence a given reasoner can actually use for an answer; there the test is where the fact lives, here it is whether an allowed change to the fact matters.

[^c1]: doi-10-48550-arxiv-2609-39608 — "intervention can change the decision, the target evidence unit is decision-critical"
[^c2]: doi-10-48550-arxiv-2609-39608 — "Allowed interventions are specified independently of their outcomes"
[^c3]: doi-10-48550-arxiv-2609-39608 — "A mistaken residency judgment can reverse approval when"
[^c4]: doi-10-48550-arxiv-2609-39608 — "a negative label requires either a complete mapping that rules out a change"
[^c5]: doi-10-48550-arxiv-2609-39608 — "It asks whether changing eg could change the decision under the governing rule"
[^c6]: doi-10-48550-arxiv-2609-39608 — "achieves 68.28% accuracy, outperforming all six baselines"
[^c7]: doi-10-48550-arxiv-2609-39608 — "68.28 ± 2.01"
[^c8]: doi-10-48550-arxiv-2609-39608 — "Our experiments study evidence criticality in a controlled setting with textual evidence"
[^c9]: doi-10-48550-arxiv-2609-39608 — "Offline construction uses annotated condition states and decisions"
[^c10]: doi-10-48550-arxiv-2609-39608 — "Higher accuracy alone therefore does not ensure more balanced criticality"
