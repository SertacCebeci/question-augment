---
description: "Questions that gather facts scattered across documents and compute over them are answered worse than single-document extraction, even by models that extract well from one document."
aliases: ["cross-document aggregation gap", "single-document versus aggregation accuracy", "multi-document aggregation deficit"]
sources: ["arxiv-2601-08847"]
---
# Aggregation-extraction gap

Asking a question about one document and asking one that must gather facts across several are different tasks, and the second is harder even when the first is done well. RIKER separates the two in its taxonomy: single-document questions (L01 to L04) against aggregation questions (L05 to L10, such as counting, summation, comparison and multi-hop). The paper says aggregation needs three things at once: the model must "identify all relevant documents", "extract the relevant facts from each, and (3) perform the required computation correctly".[^c1]

The finding is that the two accuracies come apart. "Single-document extraction and cross-document aggregation appear to require fundamentally different capabilities".[^c2] Across the models tested, "aggregation accuracy consistently lags" extraction accuracy, and the paper reads this as a reason benchmarks that test only single-document retrieval "may overestimate model capability" for enterprise work.[^c3] The gap widens with context: "Aggregation degrades faster with context".[^c4]

The paper reports aggregation as a capability metric, not as a hallucination metric, because its errors mix causes: "Aggregation errors conflate multiple failure" modes, including incomplete retrieval of documents, computation errors and limits of working memory.[^c5] So the gap is a measured difference in accuracy between two question classes. It is not a decomposition of why the second class is harder.

The mechanism the paper points to is a sequence. Each stage can fail, and a single missed document or wrong arithmetic step makes the whole answer wrong. A model that reads any one document correctly can still fail the composed answer. This sequential reading is the paper's account; the passages read do not isolate each stage separately.

## Limits

The gap is established on one synthetic enterprise corpus, in English, with the entire corpus placed in the prompt. The paper states that "we evaluate pure context-stuffing", so whether retrieval narrows or widens the gap is untested here.[^c6]

The two question classes differ in more than the number of documents: the aggregation tier also changes the operation (counting, averaging, comparing, temporal filtering). The paper does not separate hop count from operation type, so the gap cannot be attributed to one of them; that separation is my inference about what a clean test would need.

Per-model results are reported at several context sizes, and the paper's aggregation numbers for individual models are not restated here. The claim is the consistent ordering, not a fixed size of the gap.

## Related

- [[shared-entity-pool-coherence]] — the generator that makes cross-document relations exist, so that aggregation questions are well-posed.
- [[dispersed-evidence-retrieval-collapse]] — the retrieval side of the same difficulty: top-k retrieval fails sharply with scale when the evidence is scattered.
- [[evidence-scope-gradient]] — the same falling accuracy as the evidence a question needs spreads from one concept to a whole history.
- [[evidence-chain-question-generation]] — building an explicit cross-document evidence chain before writing a question raised true multi-hop yield.

[^c1]: arxiv-2601-08847 — "(2) extract the relevant facts from each, and (3) perform the required computation correctly"
[^c2]: arxiv-2601-08847 — "Single-document extraction and cross-document aggregation appear to require fundamentally different capabilities"
[^c3]: arxiv-2601-08847 — "only single-document retrieval may overestimate model capability"
[^c4]: arxiv-2601-08847 — "Aggregation degrades faster with context"
[^c5]: arxiv-2601-08847 — "Aggregation errors conflate multiple failure"
[^c6]: arxiv-2601-08847 — "we evaluate pure context-stuffing"
