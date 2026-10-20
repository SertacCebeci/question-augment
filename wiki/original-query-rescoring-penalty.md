---
description: "Scoring an expansion-based retriever by similarity to the original query penalises the candidates that expansion was meant to add, so fusion can trail single-query search on that score alone."
aliases: ["original-query metric penalty", "anchor-metric penalty", "re-scoring against the seed query"]
sources: ["arxiv-2512-12694"]
---
# Original-query re-scoring penalty

Query expansion writes several reformulations of a question, retrieves for each one, and fuses the ranked lists. The fused list can then hold passages that the original wording alone would rank low. If those candidates are graded by their similarity to the original query, the grading is done against the very wording the expansion was built to move away from. The measured outcome depends on which query the score is taken against, not only on what was retrieved.

The MTRACE paper gives this as its own account of a negative result. Under a similarity re-scoring protocol across four embedding models, multi-query fusion did not outperform single-query dense retrieval.[^c1] Query expansion "did not improve re-scored similarity for any retriever", and the paper reads the result as a property of the scoring rather than of the retriever: expansion lowered re-scored similarity for dense, sparse and fused retrieval alike.[^c2][^c3] Its stated mechanism is that reciprocal rank fusion "retains reformulation-favoured candidates that the original-query metric then penalises."[^c4]

Fusion here is rank-only. Reciprocal rank fusion "operates solely on document ranks", so it does not need the similarity scores of different query variants to share a scale.[^c5] That removes one problem, the calibration of scores across variants. It does not remove the anchor problem: the ranks are fused, but the yardstick that judges the fused list is still the original query.

The paper also says what the metric cannot see. Fusion is designed to raise evidence coverage against gold answers, and the authors state that this "cannot be measured with 50 qualitative queries."[^c6] So the protocol measures closeness to the original query, while the intended gain is coverage of the answer. The two can disagree by construction.

What transfers. The concept does not depend on reciprocal rank fusion or on the particular LLM expansion. Any setup that expands a query and then scores the result by similarity to the unexpanded query has the same structure: the score rewards staying near the seed, and the expansion's purpose is to leave it. Whether that matters depends on whether the target is near the seed or away from it. When the answer shares the question's wording, the anchor metric and the coverage target agree and the penalty is small. My inference, not tested here.

## Limits

- The mechanism is the authors' account. The text read does not run a test that separates "the anchor metric penalises expansion-pulled candidates" from "expansion adds noise to the candidate pool," which is the explanation given for a different multi-query result in [[multi-query-expansion-precision-penalty]]. Both readings fit the same flat outcome.
- Gold-label recall, the quantity the fusion is meant to improve, is not measured; the paper lists it as future work, and so does not show the penalty is the reason for the gap.[^c7]
- The evaluation is 50 queries written by the authors, on the French and English subsets of one corpus, and "we report no significance tests."[^c8] The "property of the protocol" reading rests on that one small set.
- Re-scoring against the original query may also reward lexical overlap with the question's wording. That bias sits in the metric itself and was not separated from the anchor effect. My inference.
- Nothing here tests a different anchor, such as the mean over all reformulations, or a reranker applied after fusion.

## Related

- [[query-anchored-expansion-integration]] — keeping the query as an anchor inside the encoder bounds the expansion's pull; this note is the evaluation-side version of the same anchor, which also serves as the yardstick.
- [[multi-query-expansion-precision-penalty]] — another multi-query result that ran against its design intent, measured by precision rather than similarity; the two explanations are not separated by either study.
- [[query-expansion-harm-asymmetry]] — expansion's harm concentrated in a few queries and hidden by averages, the same caution about what an aggregate score can hide.

[^c1]: arxiv-2512-12694 — "multi-query fusion does not outperform single-query dense retrieval"
[^c2]: arxiv-2512-12694 — "Query expansion did not improve re-scored similarity for any retriever"
[^c3]: arxiv-2512-12694 — "expansion lowers re-scored similarity for dense, sparse and fused retrieval alike"
[^c4]: arxiv-2512-12694 — "that the original-query metric then penalises"
[^c5]: arxiv-2512-12694 — "operates solely on document ranks"
[^c6]: arxiv-2512-12694 — "cannot be measured with 50 qualitative queries"
[^c7]: arxiv-2512-12694 — "gold-label recall remain future work"
[^c8]: arxiv-2512-12694 — "we report no significance tests"
