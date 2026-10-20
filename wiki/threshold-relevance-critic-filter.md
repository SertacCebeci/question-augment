---
description: "A pointwise relevance critic keeps only the passages whose 'yes' probability clears a threshold, cutting a wide retrieval set from about 129 to about 6 passages before generation, with recall held."
aliases: ["relevance critic filter", "critic-filtered retrieval", "yes-probability passage filter", "probability-threshold context filter", "critic model for RAG passages"]
sources: ["arxiv-2511-22715"]
---
# Threshold relevance critic filter

A retrieval-augmented answerer gets a set of candidate passages and must decide which of them enter its context. One way to make that decision is a separate critic that reads each passage against the question and answers a binary question: could this passage help answer it? The critic's probability of a "Yes" is then compared with a threshold, and only passages above it reach the generator.[^c3] The rule is a cut on content, not on rank. A passage is dropped because the critic is confident it is irrelevant, not because it sits below position k.

The mechanism runs in two halves. First the retriever is made wide on purpose. Coarse retrieval gives high recall when many documents are kept, but it "suffers from low precision due to noise."[^c1] Widening k improves recall and "this typically comes at the cost of a lower precision," because more noisy passages enter.[^c2] The critic is the second half. It is a fine-tuned multimodal model asked "to determine whether p contains any information that could help answer the question."[^c4] It runs over every passage the wide retrieval produced, so recall is set by the retriever and precision by the critic.

The paper reports what this does to the context size. At k = 20 the average number of passages fed to the generator falls "from an average of 128.6 to 5.7," which is the mechanism working as designed: most of the noise is discarded and a small evidence set remains.[^c5] Where the critic is judged by recall (retained relevant evidence) and specificity (rejected irrelevant passages), the paper says its critic keeps "higher recall while filtering irrelevant passages with higher" specificity than the compared filter.[^c9] In the zero-shot ablation, adding the critic to the coarse retriever gives "more than a twofold gain" in accuracy, and the full retrieval pipeline with a fine-grained retriever reaches 40.2 on E-VQA and 27.1 on InfoSeek with no fine-tuning of the generator.[^c7][^c11] Those numbers belong to the whole pipeline, so the critic's share is the twofold figure only, and that figure is the paper's own reading of its Table 4.

Two design choices follow from the threshold form. The threshold is a dial. Reading the sweep, the paper picks a low value, 0.1, because it "yields the best trade-off between precision and recall in" retrieving relevant passages.[^c6] A low threshold keeps more passages and so protects recall; a high one trades recall for a cleaner context (my reading of the threshold form). The second choice is what happens when every passage is rejected. The paper provides "no fallback context, avoiding the risk of conditioning" the generator on misleading text, and the generator then sees only the question and the image.[^c8] A rival pipeline "inserts a random" passage in that case, and the paper argues against it.[^c12] An empty context is therefore a legitimate output of the filter, and the answerer must be trained to work with it.

A rank cut, by contrast, keeps the top n whatever their content. A per-question depth set by a classifier is a rank cut with a predicted n (my reading; see [[dynamic-retrieval-depth]]). The threshold filter instead lets the number of kept passages vary with the content, and the paper shows it keeps very few on average. Whether that is a better cut than a well-chosen rank cut is not what the paper tests; it compares against a pipeline without the critic and against another critic, not against a tuned rank cut.

## Limits

- The critic was tested on Encyclopedic-VQA and InfoSeek, with a retriever the authors built and, in an appendix, with the Wikipedia pages returned by Google Lens. The text calls the critic "agnostic to the retrieval backbone, making it seamlessly" applicable to any retriever,[^c10] but no retriever beyond these was run.
- The threshold of 0.1 was chosen from a sweep on the same benchmarks that report the final numbers. The text does not say whether a separate validation split was used for it.
- The gains are reported as accuracy on E-VQA and InfoSeek. The text does not separate how much of the gain comes from better evidence and how much from the generator's reasoning training. The paper's own reading is that "a significant portion of the improvements stems from higher-quality evidence selection," which is a reading, not a decomposition.
- The critic was trained on a dataset of image-question-passage tuples whose relevance labels come from earlier work. Its errors on passages outside that label distribution are not measured here.
- No significance test or variance across seeds appears in the text read. The twofold figure is a single run in the ablation table.
- The filter removes passages; it cannot add evidence the retriever missed. Recall is therefore capped by the wide retrieval, the same structure as a verifier that only filters a list (my inference from the design; see [[generate-then-verify-candidate-pipeline]]).

## Related

- [[reranker-as-relevance-judge]] — the same kind of binary relevance judge, studied for agreement with human or LLM labels; here the judge is used as a filter inside an answering pipeline
- [[dynamic-retrieval-depth]] — the rank-based alternative: choose how many ranked passages to keep per question, with a cut that drops relevant passages below it
- [[parametric-knowledge-gates-retrieval-noise-damage]] — how much irrelevant context hurts depends on what the model already knows, which bears on how much a filter buys
- [[generate-then-verify-candidate-pipeline]] — the same recall-then-filter shape in a list-generation setting, where the verifier can only remove items

[^c1]: arxiv-2511-22715 — "high recall when retaining many documents but suffers from"
[^c2]: arxiv-2511-22715 — "this typically comes at the cost of a lower precision"
[^c3]: arxiv-2511-22715 — "only passages yielding a positive prediction with probability above a threshold are kept"
[^c4]: arxiv-2511-22715 — "to determine whether p contains any information that could"
[^c5]: arxiv-2511-22715 — "from an average of 128.6 to 5.7 at k = 20"
[^c6]: arxiv-2511-22715 — "yields the best trade-off between precision and recall in"
[^c7]: arxiv-2511-22715 — "yielding more than a twofold gain"
[^c8]: arxiv-2511-22715 — "our method provides no fallback context, avoiding the risk of conditioning"
[^c9]: arxiv-2511-22715 — "higher recall while filtering irrelevant passages with higher"
[^c10]: arxiv-2511-22715 — "agnostic to the retrieval backbone, making it seamlessly"
[^c11]: arxiv-2511-22715 — "on E-VQA and 27.1 on InfoSeek"
[^c12]: arxiv-2511-22715 — "which inserts a random"
