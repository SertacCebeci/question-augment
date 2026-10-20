---
description: "In a rule that combines condition judgments, a wrong reading of one evidence unit reaches the decision only if it flips a condition the rule's aggregation can pass on; otherwise the error is absorbed."
aliases: ["absorbed evidence error", "condition-mediated decision change", "local error absorption", "propagation of condition errors"]
sources: ["doi-10-48550-arxiv-2609-39608"]
---
# Condition absorption of evidence error

A rule-governed decision is built in layers: evidence bears on each condition, each condition takes a state, and an aggregation maps the states to the decision. The paper's stages are "Evidence→Condition→Aggregation→Decision".[^a1] An error in reading one evidence unit therefore has to pass through a condition before it can touch the decision. The mechanism is that passage, and it can fail at either step.

The first step is the condition state. The paper's states are satisfied, not satisfied and unknown, and an edit to the evidence changes the target condition only in some cases. "Even a local omission may leave a condition unchanged if other evidence still supports it."[^a2] A wrong reading of one unit is an error only for the condition it bears on, and a second unit may still hold that condition in place.

The second step is the aggregation. A changed condition changes the decision only if the rule lets it. The paper's example uses a conjunction of residency and employment: "leaves rejection unchanged when employment fails."[^a3] With a conjunction, a residency flip reverses the outcome only when the other condition already holds. The paper names the general pattern: "in the target condition state does not always change the decision."[^a4] The error is absorbed when the rule's aggregation does not pass it on. Two consequences follow. A correct decision can rest on wrong condition judgments, and a condition judgment that is wrong may be harmless for this decision.

The paper turns this into a computation. For a target evidence unit, the model predicts a decision for each possible target state, with the rest of the case fixed. Those rows are then weighted by the probabilities of the states: "Propagation composition weights the three rows of RiH by qia to obtain the decision distribution pi after the intervention."[^a5] The decision-change probability is one minus the probability of the original decision under that mixture. The weights come from a frozen condition estimator; the composition itself has no trainable parameters. Where the rule's aggregation is known, the mixture says how much of the condition uncertainty reaches the outcome. This is the paper's construction, and I read it as a way of making the absorption explicit rather than as a general law.

What this implies, in my inference and not the paper's claim: a misreading matters to the decision only through the condition it moves, and only if the rule, given the other conditions, lets that move reach the answer. Whether a unit was misread is a different question from whether the misreading is consequential. The paper's ablation supports the claim that the second part is learnable and matters: "lowers balanced accuracy by 9.76 pp, supporting its contribution beyond branch supervision" when the composition is removed.[^a6]

## Limits

The setting is three-valued conjunction or disjunction over textual evidence.[^a7] The absorption argument, as the paper states it, relies on that aggregation. A rule with counts, weights or ordering may pass or absorb errors in other ways, and the paper does not test them.

The composition only corrects what the estimator and the complete mapping provide. "Hard Warrant preserves the known relation but cannot correct errors in condition estimation" — the paper's own caveat — so a wrong condition probability still propagates into the decision mixture.[^a8]

Absorption is about decisions, not about evidence quality. A condition judged wrongly and absorbed is still a wrong judgment. The paper's rule-level result does not say that such errors are harmless to the record, only that they may leave this decision unchanged.

Decision-change detection has a false-positive side. On control edits the verifier "incorrectly predicts decision changes" more often than a baseline, and "false changes on controls remain a limitation."[^a9]

## Related

- [[evidence-decision-criticality]] — the question that absorption makes case-dependent: whether an allowed change to one evidence unit can change the decision for this case.
- [[aggregation-extraction-gap]] — combining several local readings into one answer; here the combination is a rule over condition states, and the question is which single change survives it.

[^a1]: doi-10-48550-arxiv-2609-39608 — "Evidence→Condition→Aggregation→Decision"
[^a2]: doi-10-48550-arxiv-2609-39608 — "Even a local omission may leave a condition unchanged if other evidence still supports it"
[^a3]: doi-10-48550-arxiv-2609-39608 — "leaves rejection unchanged when employment fails"
[^a4]: doi-10-48550-arxiv-2609-39608 — "in the target condition state does not always change the decision"
[^a5]: doi-10-48550-arxiv-2609-39608 — "Propagation composition weights the three rows of RiH by qia to obtain the decision distribution pi"
[^a6]: doi-10-48550-arxiv-2609-39608 — "lowers balanced accuracy by 9.76 pp, supporting its contribution beyond branch supervision"
[^a7]: doi-10-48550-arxiv-2609-39608 — "Our experiments study evidence criticality in a controlled setting with textual evidence"
[^a8]: doi-10-48550-arxiv-2609-39608 — "known relation but cannot correct errors in condition estimation"
[^a9]: doi-10-48550-arxiv-2609-39608 — "false changes on controls remain a limitation"
