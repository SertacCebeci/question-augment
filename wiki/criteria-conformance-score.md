---
description: "A reasoning trace is graded 0 to 3 for whether its step-by-step application of encoded diagnostic criteria is logically sound, and a correct conclusion alone does not earn the top grade."
aliases: ["LCS", "Logic Consistency Score", "rule-conformance grade", "step-wise criteria application score"]
sources: ["arxiv-2511-17947"]
---
# Criteria-conformance score

A diagnostic criterion is a rule with parts: a count of symptoms, a required core symptom, and an exclusion. The paper encodes each DSM-5 disorder criterion "is encoded as an executable function that" captures the required symptom count, the presence of core symptoms and any exclusionary conditions.[^c1] The function is not run by a program over the dialogue. The language model is "prompted to execute a step-wise application of these diagnostic rules over its reasoning trace."[^c2] So the thing that applies the rule is the same kind of model whose reasoning is being graded. The rule is a checklist the model has to walk through, and the trace is scored by how closely it follows that checklist.

The grade is ordinal. It is 0 when the reasoning "Contradicts DSM-5 diagnostic logic", 1 for "Partially correct logic, incorrect conclusion", 2 for partially correct logic with a correct conclusion, and 3 for fully correct logic and conclusion.[^c3] The score "is then assigned" by "how closely the reasoning conforms to the structured diagnostic criteria".[^c4] The scale has two axes folded into one number. The logic is judged on whether the criteria were applied, and the conclusion on whether the diagnosis is right. Level 2 is the case the scale is built to show: the conclusion is right and the path to it is not fully right. A correct answer reached by skipping a criterion gets less than the top grade.

The grade is one of two parts of the paper's combined score. It is rescaled to [0, 1] and mixed with the claim-level part by a weight λ. The authors write that "The final DCS combines KAS and LCS, using a normalized" LCS scaled to the unit interval.[^c5] The mix is a fixed linear combination. The paper's aim in combining them is a single number from 0 (invalid) to 1 (fully valid). The claim-level part, [[knowledge-attribution-score]], asks whether each statement is supported; this part asks whether the procedure was followed.

The transfer to other settings is in the shape. A narrated rationale is checked against an executable statement of the rule, and the rule is the reference, not the answer. [[execution-trace-rationale-verification]] does the same with a real program trace as the reference. What does not transfer is the independence of the reference: here nothing is executed independently, and the rule is applied by a model.

## Limits

- The sections I read do not say who assigns the 0 to 3 grade. If a language model assigns it, the grade inherits the kind of error it is meant to catch. This is my inference from the text, which is silent on the assessor.
- The "executable function" is a prompt the model reads, not code. No test in the sections read shows that the model counts symptoms or applies exclusions reliably, and the criteria are applied to symptoms the model itself extracted from the dialogue.
- The paper's headline numbers are for the combined DCS, so the sections I read do not isolate what the logic grade adds on its own.
- The criteria are DSM-5 criteria for depression-related disorders as the paper uses them. Whether the same encoding works for criteria with richer temporal or contextual conditions is not tested in the text read.
- A grade of 2 versus 3 depends on what counts as a "correct" conclusion, and the reference for that conclusion is the pseudo-label discussed in [[knowledge-attribution-score]]. The logic grade therefore does not escape the label question.

## Related

- [[knowledge-attribution-score]] — the claim-level half of the same combined score; it checks each statement against triplets rather than the procedure against the criteria.
- [[execution-trace-rationale-verification]] — the closest shape: a narrated rationale checked against an executable spec, where the spec is a program's real trace and not a model's own application of a rule.
- [[rule-compliance-question]] — asks whether an actor's behaviour complies with a rule; this grades whether a model's reasoning applies one.
- [[checklist-diagnostic-decomposition]] — answers fixed predicate questions to classify; here the same kind of predicates is used to grade a trace.

[^c1]: arxiv-2511-17947 — "is encoded as an executable function that"
[^c2]: arxiv-2511-17947 — "prompted to execute a step-wise application of these diagnostic"
[^c3]: arxiv-2511-17947 — "Contradicts DSM-5 diagnostic logic"
[^c4]: arxiv-2511-17947 — "The LCS score is then assigned"
[^c5]: arxiv-2511-17947 — "The final DCS combines KAS and LCS, using a normalized"
