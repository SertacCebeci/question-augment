---
description: "A question's answer source, the place its answer sits in the evidence (verbatim span, option, several spans, computed number, cross-image synthesis), sorts how well VLMs answer it."
aliases: ["answer source", "answer-source category", "answer location in evidence", "span versus non-extractive answer"]
sources: ["arxiv-2512-12424"]
---
# Answer source

A question can be labelled by where its answer sits in the evidence. The label is a property of the question, fixed before any model answers it: the answer is a verbatim span of the image, one option from a printed list, several spans joined together, a number computed from the image, or a conclusion built across several images. ViInfographicVQA defines the single-image categories this way. Image-span is "a single, contiguous verbatim span in the image".[^c1] Question-span is a multiple-choice answer where "the answer is exactly one option, verbatim".[^c2] Multi-span joins "two or more non-contiguous verbatim" spans with commas.[^c3] Non-extractive is "numeric reasoning such as counting, arithmetic, or computing a rank/percentage".[^c4] The multi-image set adds Multi-image span, Cross-image synthesis ("across images to reach a new conclusion"), and Non-span numerical computation over values drawn from different images.[^c5]

The category is also a design input, not only an annotation. The builders "pair element types with answer-source categories" in rule-based prompt templates, so a question is written to fit a source before it is generated.[^c6] The answer source is one of three dimensions the abstract names for each question, with the supporting evidence type and the required operation.[^c7]

What the label predicts is an ordering in measured accuracy. Across the single-image models, the authors find that "VLMs handle span extraction reliably", while numerical and multi-step reasoning remains hard, and that "Non-extractive reasoning is consistently lower across models".[^c8][^c9] On the multi-image task the largest errors fall on questions "that involve cross-image integration" and non-span reasoning, and the authors name "cross-image synthesis as a key bottleneck".[^c10][^c11]

The same label therefore does two jobs for someone asking or answering. When formulating, it says which kind of evidence the question will draw on and how the answer must be assembled. When evaluating, it says where a score is likely to fall (my inference from the ordering above, not a result the paper tests): a span answer is checked against text that is already in the image, while a non-extractive or cross-image answer requires computation and integration that the image alone does not give.

## Limits

The labels are the benchmark authors' own. Candidates were generated with a vision-language model and then filtered and refined by humans, so a category records what the builders wrote, not an independent measure of how hard the answer is. The paper reports per-category scores but does not test whether the category itself, with the operation held fixed, is what produces the gap.

The Non-extractive category merges every numeric operation. The authors say they "maintain separate labels for operations (counting, arithmetic, sorting)",[^c12] so the label cannot say which operation fails. Comparative picks such as maximum or top-k inside a span question are "question semantics, not additional operation tags",[^c13] which means the same comparison can sit in a span category or a numeric one depending on its wording. That boundary is a design choice, not a finding.

The score behind the ordering is ANLS, a normalised string-similarity measure. The authors say it "does not fully capture semantic correctness, numerical exactness, grounding faithfulness, or calibration".[^c14] So part of the gap between span and non-extractive categories may be a property of the metric, since a near-miss number scores differently from a near-miss span. This is my inference; the paper does not separate it.

The result covers one Vietnamese infographic benchmark and a handful of open vision-language models, with one fine-tuning setup. Whether the ordering holds for other languages, natural images or other models is not tested in the work.

## Related

- [[aggregation-extraction-gap]] — the same ordering between single-source extraction and multi-part computation, measured earlier on text documents
- [[ocr-answer-token-coverage]] — a span answer can only be returned if the reader recovers its tokens, which bounds span-category accuracy
- [[textual-annotation-dependence]] — numerical chart answers that rest on printed labels rather than the plotted marks
- [[extractive-abstractive-verifiability-tradeoff]] — answer form on a different axis: how far a cited answer departs from its quotes

[^c1]: arxiv-2512-12424 — "a single, contiguous verbatim span in the image"
[^c2]: arxiv-2512-12424 — "the answer is exactly one option, verbatim"
[^c3]: arxiv-2512-12424 — "two or more non-contiguous verbatim"
[^c4]: arxiv-2512-12424 — "numeric reasoning such as counting, arithmetic, or computing a rank/percentage"
[^c5]: arxiv-2512-12424 — "across images to reach a new conclusion"
[^c6]: arxiv-2512-12424 — "rule-based prompt templates that pair element types with"
[^c7]: arxiv-2512-12424 — "answer source, supporting evidence type, and required operation"
[^c8]: arxiv-2512-12424 — "VLMs handle span extraction reliably"
[^c9]: arxiv-2512-12424 — "Non-extractive reasoning is consistently lower"
[^c10]: arxiv-2512-12424 — "the most significant errors occurring on Multiimage questions that involve cross-image integration"
[^c11]: arxiv-2512-12424 — "highlighting cross-image synthesis as a key bottleneck"
[^c12]: arxiv-2512-12424 — "maintain separate labels for operations (counting, arithmetic, sorting)"
[^c13]: arxiv-2512-12424 — "question semantics, not additional operation tags"
[^c14]: arxiv-2512-12424 — "capture semantic correctness, numerical exactness, grounding faithfulness, or calibration"
