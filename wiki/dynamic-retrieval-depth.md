---
description: "Query-specific retrieval depth predicts how many passages a question needs; a hop-count classifier alone lost recall, and gains came only when an LLM reranker trimmed a wider list."
aliases: ["dynamic k", "adaptive k", "classifier-k", "query-specific top-k", "dynamic context selection"]
sources: ["arxiv-2512-14313", "openalex-org-w7203956628"]
---
# Dynamic retrieval depth

A retrieval-augmented pipeline has to decide how many passages it hands to the generator. The usual answer is a fixed k, the same for every question. The alternative sets [[retrieval-depth-relative-to-relevant-count|the depth]] per question. Iratni et al. build one such alternative for multi-hop question answering. A RoBERTa classifier reads the question alone and predicts its hop type, 2, 3 or 4, and "The output class is then mapped to a corresponding k value for retrieval."[^c1] The target is a sensible proxy in that dataset: in MuSiQue, "2-hop questions are provided with two gold documents, 3-hop with three, and 4-hop" with four, so the hop count fixes how many passages a complete answer needs.[^c2]

The trade-off that motivates a per-question depth is the one a fixed k has to accept. "Increasing k generally improves recall, so fewer relevant passages are missed."[^c3] The cost is that a larger k also "decreases the precision by including more irrelevant context, diluting relevant documents and degrading generation quality."[^c4] A per-question depth tries to avoid both.

The paper tests two forms. In the classifier-k form, the predicted k is the number of passages the retriever returns. In the classifier-LLM form, the retriever first fetches a fixed set of five candidates, and an LLM is asked to keep the predicted number: it "is prompted to select the top classifier-k passages from the candidate set based on their relevance to the query."[^c5] The generator then reads only the kept passages.

## What was measured

The classifier is an imperfect predictor. The MuSiQue-only version "scored a 77.8% accuracy on MuSiQue queries."[^c6]

Taken alone, the classifier-k form did not help. The paper reports that the Baseline "outperformed the Classifier pipeline ... in both the MuSiQue and 2WikiMultiHopQA datasets, with all retrieval configurations."[^c7] Even an ideal classifier lost to the fixed-k baseline with a real retriever: "the fixed k (Baseline) approach outperforms the classifierk approach, even when the classifier is ideal."[^c8] The authors locate the loss in recall: "the recall significantly decreases", and the approach "cuts-off relevant contexts, which decreases generation performance."[^c9]

The same comparison with an ideal retriever reverses the order. The best setup is the ideal k, followed by the classifier-k, and "This shows that with an ideal retriever, the classifier outperforms the fixed-k baseline."[^c10] So a per-question depth helps when the ranking already puts the needed passages near the top. A simulated ideal reranker also favours the classifier: "an ideal reranking module with the classifier produces better results than the fixed-k pipeline."[^c11]

The LLM reranker is what turned the result positive. "the Classifier-LLM configuration outperformed the baseline with every retrieval method."[^c12] The significance test was run on the BGE configuration only: "The test yielded a p-value <0.01 on all three datasets."[^c13] The authors' reading of the earlier failure is that "the issue likely stems from retrieval quality rather than the classifier, highlighting the need for a stronger reranker."[^c14]

The mechanism, as the numbers show it, is a cut at a predicted depth. A cut on a ranked list discards any relevant passage that ranks below it. A wider candidate list, reordered by relevance before the cut, keeps those passages and still drops the rest. This reading is mine; the paper states the recall loss and the reranker result but not this decomposition.

A depth can also be set from the retrieval scores, with no question classifier. A 2026 master's thesis on hallucination-aware RAG tests one: "it applies a reranker-based score-gap strategy to dynamically determine how many chunks should be passed to the generator."[^c20] The range was 3 to 15 chunks, and the average depth was small: "Qwen retrieved 4.24 chunks on average, BGE retrieved 5.39, and MPNet retrieved 3.98."[^c21] For BGE, recall is "substantially higher than the BGE baseline" at a fixed top-5.[^c22] The thesis's summary is that dynamic retrieval "provided a strong trade-off between retrieval quality and context size by selecting a variable number of chunks while maintaining competitive performance."[^c23] This is a score-based depth rule of the kind the paragraph above notes was not run in the first paper, so on this one corpus the open question above is answered in the score's favour, though only against a fixed top-5, not against a question-only predictor, which the thesis did not run (my reading).

## Limits

- Hop count stands in for the number of needed passages. On MuSiQue it equals the gold count by construction, so the classifier predicts that count. Outside a dataset built this way, nothing in the paper says what the predicted quantity would be.
- The classifier's errors have a known direction and cost. An underestimate loses evidence: "classifier mislabels a 3-hop question as 2-hop, only two relevant contexts are" retrieved.[^c15] The paper reports the accuracy but does not separate the answer loss caused by misclassification from the loss caused by retrieval.
- Only one dataset, MuSiQue, carries the depth result. For 2WikiMultiHopQA, "No retrieval component was applied for this dataset."[^c16] Its numbers are reranking over ten given candidates, not dynamic depth over a retriever.
- The reranker is a second, 12.2B model, "Mistral Nemo Instruct", prompted zero-shot, and the generator is Flan-T5-XL.[^c17] The gain depends on that model. I found no cost comparison in the text.
- The comparison with Adaptive-RAG uses that paper's reported numbers, "which addresses a related task using a different retrieval method."[^c18] It is not a controlled comparison.
- The paper does not test a depth predictor that reads retrieval scores. Taguchi et al. choose the number of passages "based on similarity score distribution," and the paper cites this but does not run it.[^c19] That leaves open whether a question-only predictor is needed at all.
- The paper's own framing is that the ideal-k result is an upper bound: it uses gold hop labels as k, so it does not show what a learned predictor achieves.
- The score-gap result is one prototype on one research-paper corpus, with one reranker-based rule and a 3–15 range. The thesis itself reports that "stronger retrieval metrics did not always lead to proportional improvements in answer correctness or faithfulness."[^c24] A depth rule can therefore raise retrieval numbers without a matching gain in answers; the thesis does not separate the two causes (my reading).

## Related

- [[retrieval-depth-relative-to-relevant-count]] — the depth regime is defined by the relevant count N_p; here a question-only classifier stands in for N_p on MuSiQue, which the other note records no procedure for
- [[two-stage-reranking]] — the LLM step that trims a wider list to the predicted k is a second stage over a cheap first pass
- [[calibrated-retrieval-budget-allocation]] — the other per-query decision about how much retrieval to do, made by thresholding a confidence rather than predicting a count
- [[parametric-knowledge-gates-retrieval-noise-damage]] — the cost side of a deep k: irrelevant passages can hurt, and how much depends on what the model already knows

[^c1]: arxiv-2512-14313 — "The output class is then mapped to a corresponding k value for retrieval"
[^c2]: arxiv-2512-14313 — "2-hop questions are provided with two gold documents, 3-hop with three, and 4-hop"
[^c3]: arxiv-2512-14313 — "Increasing k generally improves recall, so fewer relevant passages are missed"
[^c4]: arxiv-2512-14313 — "by including more irrelevant context, diluting relevant documents and degrading generation quality"
[^c5]: arxiv-2512-14313 — "is prompted to select the top classifier-k passages from the candidate set based on their relevance to the query"
[^c6]: arxiv-2512-14313 — "scored a 77.8% accuracy on MuSiQue queries"
[^c7]: arxiv-2512-14313 — "in both the MuSiQue and 2WikiMultiHopQA datasets, with all retrieval configurations"
[^c8]: arxiv-2512-14313 — "the fixed k (Baseline) approach outperforms the classifierk approach, even when the classifier is ideal"
[^c9]: arxiv-2512-14313 — "it cuts-off relevant contexts, which decreases generation performance"
[^c10]: arxiv-2512-14313 — "This shows that with an ideal retriever, the classifier outperforms the fixed-k baseline"
[^c11]: arxiv-2512-14313 — "an ideal reranking module with the classifier produces better results than the fixed-k pipeline"
[^c12]: arxiv-2512-14313 — "the Classifier-LLM configuration outperformed the baseline with every retrieval method"
[^c13]: arxiv-2512-14313 — "The test yielded a p-value <0.01 on all three datasets"
[^c14]: arxiv-2512-14313 — "the issue likely stems from retrieval quality rather than the classifier, highlighting the need for a stronger reranker"
[^c15]: arxiv-2512-14313 — "classifier mislabels a 3-hop question as 2-hop, only two relevant contexts are"
[^c16]: arxiv-2512-14313 — "No retrieval component was applied for this dataset"
[^c17]: arxiv-2512-14313 — "Mistral Nemo Instruct"
[^c18]: arxiv-2512-14313 — "which addresses a related task using a different retrieval method"
[^c19]: arxiv-2512-14313 — "a retrieval method that dynamically selects the number of passages to retrieve based on similarity score distribution"
[^c20]: openalex-org-w7203956628 — "it applies a reranker-based score-gap strategy to dynamically determine how many chunks should be passed to the generator"
[^c21]: openalex-org-w7203956628 — "Qwen retrieved 4.24 chunks on average, BGE retrieved 5.39, and MPNet retrieved 3.98"
[^c22]: openalex-org-w7203956628 — "This is substantially higher than the BGE baseline"
[^c23]: openalex-org-w7203956628 — "Dynamic retrieval provided a strong trade-off between retrieval quality and context size by selecting a variable number of chunks while maintaining competitive performance"
[^c24]: openalex-org-w7203956628 — "stronger retrieval metrics did not always lead to proportional improvements in answer correctness or faithfulness"
