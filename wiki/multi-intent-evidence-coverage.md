---
description: "When a question has several correct answers, retrieval is scored by distinct gold facts recovered, not by one target found; the same benchmark separates query, passage and answer stages."
aliases: ["IRR", "information recall rate", "multi-intent coverage", "distinct-fact recall", "multi-intent retrieval evaluation"]
sources: ["arxiv-2511-16283"]
---
# Multi-intent evidence coverage

A single-answer retrieval benchmark asks whether the system found the one passage that holds the one gold answer. A multi-intent question does not have one target. "What are ALB gene mutations and their related diseases?" has several correct answers, each supported by a different document, and a system can answer one intent well and leave the others unsupported. The MuISQA paper's claim is that the standard measures cannot see this. For multi-intent questions, it says, "conventional metrics such as Exact Match (EM) or Recall" are "inadequate for capturing system performance."[^m1]

The proposed passage-level measure is the information recall rate. IRR "extracts all heterogeneous factual units within the retrieved set that align with the gold answers".[^m2] The numerator is the number of distinct gold units recovered; the denominator is the total number of gold units. Because the denominator is the set of gold facts, a passage that repeats a fact already found adds nothing. The paper says what this rewards: IRR "reflects how effectively a retrieval method captures complementary evidence for multiple intents, rather than repeatedly retrieving redundant fragments for a single one."[^m3]

The benchmark splits scoring into three stages, so that a gain can be placed. Query formulation is scored by a vector entropy over the embedding of the query sentences, which the paper uses as a proxy for the diversity of intents. Passage retrieval is scored by IRR. Answer generation is scored by answer accuracy (AA) and answer coverage (AC), the share of generated answers that match gold and the share of gold answers that were generated.[^m4] The paper's conclusion is that its method improves all of this together, but the stage split is what makes the claim checkable.

Where the denominator comes from. IRR is only as complete as the gold set. Here the gold units come from annotated answers to each question, so the measure says how much of an annotated inventory was recovered. A different route is taken by [[question-aspect-coverage]], which builds one aspect list from the question alone and needs no reference answer; that changes what a coverage score can mean, because the denominator is then the question's own reading, not an answer key.

What the measure separates. On the paper's table, IRR moves by several points between naive RAG and the intent-aware method, while the query-side vector entropy hardly moves at all (my reading: values between 8.06 and 8.18 across methods). A retrieval gain registered by IRR is therefore not a query diversity gain as the paper's own query metric defines it. The two measures disagree about where the improvement lives, and the paper does not reconcile them.[^m5]

## Limits

- IRR is recall over gold units. It divides by the gold set and never subtracts for extra retrieved material, so a system that retrieves more text raises it without any penalty for the surplus. The text read reports no precision-side counterpart. This is the one-sided behaviour that [[recall-only-partial-credit]] describes for multi-answer scoring. My inference, not the paper's claim.
- The gold units are LLM pre-annotations that humans corrected. The annotation model, DeepSeek-V3, is also one of the models whose hypotheses are evaluated, so a shared blind spot would inflate the coverage numbers. The paper reports the pipeline but not an agreement check between the annotator and the other generators.[^m6]
- The text read describes "align with the gold set" in one line and does not give the matching procedure, the unit definition, or inter-annotator agreement on units. A score whose unit is not defined in the text cannot be reproduced from it.
- Scale and construction: 500 questions in five domains, each paired with 20 keyword-retrieved arXiv articles and no manual filtering. The noise is realistic, but the set of intents is whatever the keyword search and the annotators found, not a sample of all intents a domain has.
- IRR and AC are both recall-type scores. The paper's AA is the precision-type counterpart at the answer stage only; no passage-level precision of the same kind is reported.

## Related

- [[recall-only-partial-credit]] — the one-sided multi-answer score; IRR has the same asymmetry at the passage level
- [[question-aspect-coverage]] — a coverage denominator built from the question alone, with no gold answers
- [[stage-disentangled-evaluation]] — scoring each stage against its own gold, so a failed plan is not confused with a failed search; the reason for MuISQA's three-stage split
- [[single-answer-training-prior]] — the same failure in detection: one correct answer per training query caps multi-answer recall
- [[answer-set-complementarity]] — two answerers with equal scores can cover different answers; the coverage question asked of systems rather than of one system's passages
- [[intent-decomposed-hypothetical-queries]] — the retrieval method whose gain this measure is used to report

[^m1]: arxiv-2511-16283 — "conventional metrics such as Exact Match (EM) or Recall inadequate for capturing system performance"
[^m2]: arxiv-2511-16283 — "extracts all heterogeneous factual units within the retrieved set that align with the gold answers"
[^m3]: arxiv-2511-16283 — "captures complementary evidence for multiple intents, rather than repeatedly retrieving redundant"
[^m4]: arxiv-2511-16283 — "Answer Accuracy (AA) and Answer Coverage (AC)"
[^m5]: arxiv-2511-16283 — "to quantify the informational complexity of query representations"
[^m6]: arxiv-2511-16283 — "adopted DeepSeek-V3 as the sole model for pre-annotation"
