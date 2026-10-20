---
description: "A claim is a hallucination only relative to an explicit reference world, view function and conflict policy; unknown claims and planning or reward errors are not hallucinations."
aliases: ["reference world", "reference world model W", "hallucination as inaccurate world modeling", "view function and conflict policy"]
sources: ["arxiv-2512-21577"]
---
# Reference world model

An output hallucinates only relative to a stated reference. The definition is that hallucination is "defining it as simply inaccurate (internal) world modeling, in a form where" the error is observable to the user.[^c1] Concretely, an output hallucinates when the world it implies disagrees with a reference on at least one observable atomic claim: "hallucination occurs when the world implicitly described by the" output "disagrees with the reference world model W on at least one observable claim."[^c2]

Three components have to be fixed before that disagreement means anything. The first is the reference world model W, which "may define valid states S, transition or consistency rules" and what the truth check needs.[^c3] It can be a knowledge base, a source document, a simulator, a state machine or an executable program; what matters is that it is "the specified structure against which claims are evaluated." The second is the view function V, "that determines which parts of W the model is supposed to have access to for a given input."[^c4] The third is the conflict policy P, which says how contradictory sources resolve. Together they define a truth function that maps each atomic claim to true, false or unknown, "to evaluate whether a claim is true, false, or unknown under" the policy.[^c5]

The consequence is that the same text can be a hallucination under one reference and not another. The paper's example is a model that answers that Sherlock Holmes has no real address, given a passage saying he lives at 221B Baker Street. A summarization researcher would call that a hallucination, since it contradicts the source; an open-domain QA researcher would not, since it is true that the fictional character has no real-world address.[^c6] The two verdicts concern one output and differ only in the reference. The label is a function of (W, V, P), not of the sentence alone.

The definition is narrow on purpose. It covers world-modelling errors only. A correct picture of the world with a poor plan is a planning error, and a model that is uncertain but trained to sound confident is an incentive or reward error. "Our definition intentionally targets only the first category."[^c7] A claim that cannot be checked is not counted either: "a claim cannot be evaluated, it should be marked as unknown or ambiguous rather than automatically treated as hallucination."[^c8]

The framework also says what retrieval does. Retrieval-oriented mitigations "work by changing V (the view function), providing the model with access to much more world information" at inference time.[^c9] The same passage notes that retrieval does not help when the answer must be inferred, "as in examples requiring compositional reasoning or counterfactuals."[^c10]

For someone writing an evaluation, the paper's advice is to "State what your reference world is," what the model observes, and how conflicts are resolved, because that makes the truth function reproducible.[^c11] My inference, not a claim the paper makes: a question put to a model is answerable as true or false only once the reference it is checked against is named, so a question that leaves W open leaves its own verdict open.

## Limits

- This is a position paper. The text I read gives a definition, four worked examples and a call to action; it reports no measured hallucination rates. The companion benchmark, HalluWorld, is cited for fully specified worlds, but its results are not in the text I read.
- The framework does not decide which claims an output contains. Claim extraction "remains a benchmark-design choice."[^c12]
- Open-domain settings lack a single complete reference. W is "a bounded, task-specific, and versioned reference source," and the goal shifts "from judging absolute truth" to referential consistency with respect to a specified W.[^c13]
- Conflict policies may be subjective. "We do not claim that every task admits a unique" source-precedence rule; the paper asks only that the choice be stated.[^c14]
- Hedged or probabilistic statements fall outside the scope unless they are falsifiable. The paper treats them as needing separate rules for epistemic status and calibration.

## Related

- [[possible-worlds]] — W's admissible states resemble a possible-worlds support, but a reference model is a fixed standard for judging claims, not the asker's open set of unresolved alternatives. This contrast is my inference from the two definitions.
- [[single-reference-grading-confound]] — the same hazard of one fixed reference. There a single expert solution is taken as ground truth; here the reference is named, and the paper's remedy is to state it rather than to average over experts.

[^c1]: arxiv-2512-21577 — "defining it as simply inaccurate (internal) world modeling, in a form where"
[^c2]: arxiv-2512-21577 — "hallucination occurs when the world implicitly described by the"
[^c3]: arxiv-2512-21577 — "W may define valid states S, transition or consistency rules"
[^c4]: arxiv-2512-21577 — "V that determines which parts of W the model is supposed"
[^c5]: arxiv-2512-21577 — "to evaluate whether a claim is true, false, or unknown under"
[^c6]: arxiv-2512-21577 — "as the model contradicted the source. An open-domain QA researcher might say no, as it is true that Sherlock Holmes"
[^c7]: arxiv-2512-21577 — "Our definition intentionally targets only the first category."
[^c8]: arxiv-2512-21577 — "a claim cannot be evaluated, it should be marked as unknown or ambiguous rather than automatically treated as"
[^c9]: arxiv-2512-21577 — "they work by changing V (the view function), providing the model with access to much more world information"
[^c10]: arxiv-2512-21577 — "as in examples requiring compositional reasoning or counterfactuals"
[^c11]: arxiv-2512-21577 — "State what your reference world is"
[^c12]: arxiv-2512-21577 — "remains a benchmark-design choice"
[^c13]: arxiv-2512-21577 — "This shifts the goal from judging absolute truth"
[^c14]: arxiv-2512-21577 — "We do not claim that every task admits a unique"
