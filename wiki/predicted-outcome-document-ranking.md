---
description: "An LLM predicts the score a candidate built on each retrieved document would reach, and ranks documents by it without evaluating any candidate; the predictions tracked real scores."
aliases: ["hypothetical evidence scoring", "predicted-score document ranking", "predicted child score ranking"]
sources: ["doi-10-48550-arxiv-2609-40340"]
---
# Predicted-outcome document ranking

A retrieved document is usually ranked by how relevant it looks to the query. This method ranks it by what it would do to the solution. For each new document, one call to the LLM predicts the evaluator score that a candidate improved from the current parent with that document alone would reach; the paper calls this hypothetical evidence scoring. The score is "on the evaluator’s scale and provide[s] a surrogate signal for the inner objective."[^c1] Each document is scored once per inner loop and the score is reused: "Each document is scored only once within the inner loop, and its score is reused in later rounds."[^c2] The top-ranked documents are retained, and "the retained documents and their predicted scores" steer the next round of query construction.[^c3]

The reason for the detour is that the real objective cannot be read off a query. The inner loop is meant to pick the query whose retrieved documents yield the best candidate, but that candidate exists only after it has been generated and scored. "Repeating this process for every query within the inner loop would be costly."[^c4] The prediction stands in for the evaluated score, so many queries and documents can be compared without generating a candidate for each.

The predictor has to be checked before its ranking is used, and the paper checks it on its own runs. Across 4,324 retrievals, the predicted scores "correlate strongly with the selected candidates’ evaluated scores", with a Spearman correlation of +0.86.[^c5] The correlation is positive on all 21 tasks, with a median of +0.74.[^c6] The check that matters for use is whether a promising document leads to a better solution. When a retrieval keeps at least one document whose predicted score exceeds the parent's actual score, "the selected candidate improves on its parent in 67.1% of iterations", against 52.1% under no retrieval.[^c7] The effect is real but not large, and it is not present in every case: "36.5% of retrievals yield no promising document; the parent improvement rate in these cases is only 38.3%."[^c8]

## Limits

- The evidence is correlational. A high rank correlation says the predictions order candidates similarly to the evaluator. It does not show that choosing a document for its predicted score causes the better child. The paper's own counter-case is that "documents predicted to help can also yield much worse candidates (29 of 82 runs)".[^c9]
- Each prediction is made for one document alone: "Each prediction assumes one document".[^c10] Documents that work together, or that conflict, are not scored as a set. The text I read does not test that case (my inference).
- The predictor is the same model whose knowledge the method is meant to supplement. A model that misjudges how a document applies will produce a confident wrong score, and the ranking inherits that error. The paper's correlations are measured on runs where the predictions were later checked against evaluation, which is the only check available in the loop (my inference).
- The text I read does not isolate this ranking from the gate and the query loop. The gains reported for the whole method cannot be assigned to the ranking alone from what I read.
- Tasks here are optimization problems with a numeric evaluator. Where the evaluator is slow, noisy, or absent, the surrogate's value is untested.

## Related

- [[hypothetical-query-context-ranking]] — an LLM also writes something about a context before retrieval, but it writes the questions the context answers and ranks by query similarity, with no solution score
- [[knowledge-gap-reuse-gate]] — the gate that decides whether new documents are retrieved at all; this ranking runs on what the RETRIEVE branch returns
- [[search-saturation-under-fixed-queries]] — the failure that the query loop, fed by these scores, is meant to avoid

[^c1]: doi-10-48550-arxiv-2609-40340 — "scale and provide a surrogate signal for the inner objective"
[^c2]: doi-10-48550-arxiv-2609-40340 — "Each document is scored only once within the inner loop, and its score is reused in later rounds."
[^c3]: doi-10-48550-arxiv-2609-40340 — "the retained documents and their predicted scores"
[^c4]: doi-10-48550-arxiv-2609-40340 — "Repeating this process for every query within the inner loop would be costly."
[^c5]: doi-10-48550-arxiv-2609-40340 — "scores correlate strongly with the selected candidates’ evaluated scores"
[^c6]: doi-10-48550-arxiv-2609-40340 — "Correlations are positive on all 21 tasks, with a median of +0.74."
[^c7]: doi-10-48550-arxiv-2609-40340 — "the selected candidate improves on its parent in 67.1% of iterations"
[^c8]: doi-10-48550-arxiv-2609-40340 — "36.5% of retrievals yield no promising document; the parent improvement rate in these cases is only 38.3%"
[^c9]: doi-10-48550-arxiv-2609-40340 — "documents predicted to help can also yield much worse candidates (29 of 82 runs)"
[^c10]: doi-10-48550-arxiv-2609-40340 — "Each prediction assumes one document"
