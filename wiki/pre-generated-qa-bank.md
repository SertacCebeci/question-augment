---
description: "Answers written offline for questions a document is likely to raise, indexed by question embedding; a query above a similarity threshold gets the stored answer, below it generation runs."
aliases: ["pre-generated QA bank", "pre-generated QA base", "offline QA knowledge base", "QA pre-generation", "stored question-answer index"]
sources: ["arxiv-2602-11156"]
---
# Pre-generated question-answer bank

A pre-generated question-answer bank moves part of answering in front of the question. The source is split into chunks, an LLM writes question-answer pairs over those chunks once, and each question is embedded and indexed with its answer. The authors' starting question is "pre-generate plausible question-answer (QA) pairs from these" raw documents and use them at query time.[^c1] At query time the user's question is embedded with the same model and the top three stored questions are retrieved. If the best similarity clears a threshold (0.9 in the main setting), the stored answer is returned with no generation call. Otherwise "the chunks corresponding to the retrieved top-3 QA pairs" are passed to an LLM together with the query, and it writes the answer on the fly.[^c2]

What makes the bank cover a document is the generation step. Each chunk node gets a number of keywords, and "the number of QA pairs generated per chunk was set equal to the number of keywords" for that node.[^c3] Higher layers of a chunk tree, which summarise more text, receive more keywords. The prompt asks for questions that "should represent a plausible inquiry that a person" who has not seen the page might ask, and it adds "constraints to prevent redundancy with previously generated QA pairs".[^c4] The design thus treats the asker's future question as the thing to be anticipated, and stores the answer under that anticipated wording.

The threshold is the single lever that sets how much of the bank is used, and the paper measures both sides of it. "Lowering the threshold increases the proportion of responses directly returned from the pre-generated QA base."[^c5] At 0.9, "stored responses handle 13% of the total test" queries; at 0.7, "this proportion rises significantly to 80%".[^c6] The latency falls with more hits, but the same threshold change brings "simultaneously decreasing the quality of responses".[^c7] So a bank's hit rate and its answer quality are coupled through one number, and a reading of either without the other is incomplete.

Against a standard RAG pipeline with the same LLM, the paper reports that "Overall, the simplified HybridRAG outperforms Standard RAG," where the simplified version stores QA pairs built from plain OCR text only.[^c8] The full version, which adds layout analysis and LLM descriptions of tables and figures, raises answer quality further. The stored pairs were also scored by an LLM judge: "we adopt the LLM-judge approach, specifically G-Eval", because "there is no human-crafted references or ground truth" for them.[^c9] On that judge the generated pairs "demonstrated superior quality w.r.t. all four dimensions" against the benchmark's own pairs.[^c10]

## Limits

- The measured quality of the stored answers is a judge's score, not agreement with correct answers. The answer accuracy numbers (F1, ROUGE-L, BERTScore) are computed against the benchmark's ground-truth pairs for whole responses, and the bank's own pairs were not checked against those labels in the parts read.
- The experiments use one benchmark, OHRBench, and two small generators: "We used Llama3.2" and Qwen2.5 at 3B scale.[^c11] Other domains, chatbot traffic and larger models are not tested.
- The bank costs are paid up front: the authors name "costs during the QA pre-generation" as the limitation, with about 130,000 pairs generated.[^c12]
- A hit returns a stored answer on question similarity alone. The paper does not measure how often a hit is wrong when the user's question differs from the stored one. My inference: this is the failure that answer caches face, and [[evidence-validated-answer-reuse]] shows that a check on current evidence changes that rate.
- The thresholds 0.7 and 0.9 are the two values named in the text. Whether a bank's hit rate on real traffic resembles the benchmark's is not established; the paper does not say how its test questions relate to the generated ones.

## Related

- [[hypothetical-query-context-ranking]] — the same offline move, questions written per context and stored; there the stored questions only rank contexts, while the answer is still generated at query time. Here the stored answer is itself returned.
- [[evidence-validated-answer-reuse]] — a semantic answer cache that reuses an answer only while fresh retrieval supports it; a bank with a similarity threshold alone has no such gate.
- [[unsafe-served-rate]] — the metric that counts wrong reuse over all queries; the bank paper reports no equivalent, so its hit rate cannot be read as a safety rate.

[^c1]: arxiv-2602-11156 — "pre-generate plausible question-answer (QA) pairs from these"
[^c2]: arxiv-2602-11156 — "if the similarity score is below the threshold, the chunks corresponding to the retrieved top-3"
[^c3]: arxiv-2602-11156 — "generated per chunk was set equal to the number of keywords"
[^c4]: arxiv-2602-11156 — "Question should represent a plausible inquiry that a person"
[^c5]: arxiv-2602-11156 — "Lowering the threshold increases the proportion of responses directly returned from the pre-generated QA base."
[^c6]: arxiv-2602-11156 — "stored responses handle 13% of the total test"
[^c7]: arxiv-2602-11156 — "simultaneously decreasing the quality of responses"
[^c8]: arxiv-2602-11156 — "Overall, the simplified HybridRAG outperforms Standard RAG,"
[^c9]: arxiv-2602-11156 — "we adopt the LLM-judge approach, specifically G-Eval"
[^c10]: arxiv-2602-11156 — "demonstrated superior quality w.r.t. all four dimensions"
[^c11]: arxiv-2602-11156 — "We used Llama3.2"
[^c12]: arxiv-2602-11156 — "costs during the QA pre-generation"
