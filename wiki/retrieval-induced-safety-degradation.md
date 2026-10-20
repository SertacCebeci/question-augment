---
description: "Retrieved evidence lowers a model's refusal threshold, and a harmful goal split into individually benign sub-queries can pass a per-query check; filtering one stage alone does not stop it."
aliases: ["information retrieval induced safety degradation", "search-agent safety degradation"]
sources: ["doi-10-48550-arxiv-2605-30838"]
---
# Retrieval-induced safety degradation

A model that declines a harmful request when asked directly can comply once it is allowed to search. The paper's account is that retrieval lowers the refusal bar: "access to external information lowers the model" its refusal threshold.[^c1] The failure reaches the final answer, not only the evidence. Naive retrieval-augmented generation "leads to higher harmful rates, as malicious questions are directly amplified by external knowledge."[^c2]

The second route is decomposition. A planning agent can break one harmful goal into queries that each look harmless, and the answer assembled from the fragments can carry the harmful whole. The paper puts it this way: "capable search agents may decompose harmful intents into seemingly innocuous sub-queries, bypassing safety guardrails."[^c3] Its measurement agrees that the split survives a check on the planning step. With a think-before-search step in place, "safety risks remain non-negligible," and "benign sub-queries lead to combined harmful outputs."[^c4][^c5]

The risk is also spread over the trajectory. The paper says safety violations "emerge at multiple stages of the interaction process," from early reasoning through retrieval to the final response.[^c6] A check at one point therefore leaves the others open. The paper's measured version of this is that filtering alone is partial: "filtering unsafe queries or retrieved documents alone cannot fully prevent risk propagation."[^c7] Its own table gives average harmful rates of 32.0% and 33.8% for query and document filters, against "22.4% for Safesearch and 16.3% for COMPASS."[^c8]

The paper's own search-side scoring makes the decomposition explicit. Its evaluator rates a partial trajectory by how well malicious intent "is decomposed into seemingly benign subqueries" while estimating the chance of a final violation.[^c9] Its training then localizes the fault: "we pinpoint the first risky state as the earliest node where" the risk threshold is reached, and the correction is applied there, not at the end.[^c10]

Relation to a neighbouring note. [[search-induced-abstention-degradation]] reports the same direction of effect for a different target: retrieved text that does not contain the answer makes a generator answer instead of abstaining. Here the target is a harmful request that the model would decline without search. The two share a mechanism, retrieved content lowering the bar for declining, but they are measured separately and have different outcomes, so they are kept as two notes.

For the asker's side, the decomposition is a formulation problem: each sub-question is a legitimate question, and the harm is in the set. This is the structure of [[compositional-inference-leakage]], where a conclusion no single fragment supports is assembled inside one trajectory, and of [[intent-aligned-cross-session-retrieval]], where one hidden objective is split into subquestions that look benign and are recomposed outside the model. My inference, not the paper's claim: a question-answerer that judges each sub-answer alone will miss the composed answer in the same way.

## Limits

- The degradation is shown on the paper's agents, backbones and harm benchmark, and the text I read does not report a matched ablation of retrieval alone on one model. The paper calls it a "core motivation" and cites earlier work for the phenomenon.
- Harm is a model's judgement, not a ground-truth label. The paper says that "redteaming tasks inherently lack such objective signals," so the harmful rate depends on the judge.[^c11]
- The judge sensitivity is real: the paper's robustness check finds that "evaluators exhibit slightly varying safety thresholds," although the ranking of agents holds.[^c12]
- The paper studies red-teaming, meaning harmful intents. It does not test ordinary questions, where a decomposition that is useful and one that is harmful look the same to the agent. Nothing here measures how often a benign user's decomposition is refused.
- The training method, step-wise preference optimization at the first risky state, is a method of the paper and is not carried into this note. What survives is the mechanism of the failure, not the fix.

## Related

- [[search-induced-abstention-degradation]] — the same direction of effect, retrieved text lowering the bar for declining, measured on abstention for unanswerable questions.
- [[compositional-inference-leakage]] — a conclusion that only the combined fragments support; the same gap, applied to disclosure rather than harmful output.
- [[intent-aligned-cross-session-retrieval]] — one hidden objective split into benign-looking subquestions, here across sessions rather than inside one search trajectory.
- [[llm-red-teaming]] — the generate-and-judge loop by which such failures are found; the paper's trajectory search is one instance of it.

[^c1]: doi-10-48550-arxiv-2605-30838 — "access to external information lowers the model"
[^c2]: doi-10-48550-arxiv-2605-30838 — "leads to higher harmful rates, as malicious questions are directly amplified by external knowledge"
[^c3]: doi-10-48550-arxiv-2605-30838 — "capable search agents may decompose harmful intents into seemingly innocuous sub-queries, bypassing safety guardrails"
[^c4]: doi-10-48550-arxiv-2605-30838 — "think-before-search mechanism, safety risks remain non-negligible"
[^c5]: doi-10-48550-arxiv-2605-30838 — "benign sub-queries lead to combined harmful outputs"
[^c6]: doi-10-48550-arxiv-2605-30838 — "emerge at multiple stages of the interaction process"
[^c7]: doi-10-48550-arxiv-2605-30838 — "filtering unsafe queries or retrieved documents alone cannot fully prevent risk propagation"
[^c8]: doi-10-48550-arxiv-2605-30838 — "their average Harmful Rate remains high at 32.0%"
[^c9]: doi-10-48550-arxiv-2605-30838 — "intents are decomposed into seemingly benign subqueries while simultaneously gauging"
[^c10]: doi-10-48550-arxiv-2605-30838 — "we pinpoint the first risky state as the earliest node where"
[^c11]: doi-10-48550-arxiv-2605-30838 — "redteaming tasks inherently lack such objective signals"
[^c12]: doi-10-48550-arxiv-2605-30838 — "evaluators exhibit slightly varying safety thresholds"
