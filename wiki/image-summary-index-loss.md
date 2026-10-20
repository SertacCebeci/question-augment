---
description: "An LLM summary of each slide, as the only retrieval key, ranked below the slide's native image embedding: mAP@5 0.40 against 0.52 on a 40-question earnings-call set."
aliases: ["LLM-summary-based retrieval", "text-surrogate indexing", "summarize-then-embed retrieval", "caption-indexed retrieval", "text-based image retrieval"]
sources: ["arxiv-2511-16654"]
---
# Image-summary index loss

When a multimodal RAG system stores only a text description of each image, that description is the only thing the retriever can match a question against. The image contributes what the description wrote down and nothing else. The Lumer et al. comparison sets this text-only arm against a native arm and measures the difference in ranking.

In the text-only arm, each slide image is passed to GPT-5 to produce a textual description, and "These text descriptions serve as surrogates for the original images."[^m1] The transcript chunks and these descriptions are then embedded with one text model, so the slide's content reaches the index only through the description. The paper names what a description cannot carry: the text conversion "may omit spatial structure, layout, or numeric precision present in the original image."[^m2]

The native arm keeps each slide as an image. Jina Embeddings v4 "maps both text and images into a shared semantic vector space", so a text query is compared with the slide directly.[^m3] Each slide is "treated as a distinct retrievable unit", which makes the two arms index the same units at the same granularity.[^m4] On 40 question-answer pairs with page-number relevance labels, the native arm reached "mAP@5 of 0.5234 compared to 0.3963" and "nDCG@5 of 0.6543 compared to 0.5448" for the summary arm.[^m5] Precision@5 moved from 0.480 to 0.540, while Recall@5 moved only from 0.5362 to 0.5529.[^m6] The gap is therefore mostly in ordering, not in whether a relevant document is found at all. The paper reads it that way: the native arm places "the most relevant documents higher in" the list.[^m7]

The same gap appears downstream. In pairwise judging, the native-image answers won an "average win rate of 0.612 compared to 0.388" against the summary-based answers.[^m8] On the hallucination criterion, "the multimodal approach prevents unsupported additions 90% of the time".[^m9] The authors read the summary arm as producing "fabricated details that propagate to downstream generation."[^m10] That is their reading of the gap, not a mechanism they isolate.

The cost of the native arm is in preprocessing. The paper notes that "multimodal embedding pipelines require explicit image detection, extraction, and format conversion steps", where the text route needs only one LLM call per image.[^m11]

What transfers, as my reading: the summary is a second, lossy encoder placed before the retriever. A question can be answerable from the image, and the caption can carry most of that answer, yet the retriever ranks the item by the caption's words alone. The answer-side measure of the same surrogate is in [[caption-utility-gap]]. This note measures the surrogate at the ranking step, which that note does not.

## Limits

- The two arms differ in embedding model as well as in representation. The text arm used "with OpenAI text-embedding-ada-002 for text-only", and the native arm "Jina Embeddings v4 for multimodal".[^m12] The paper also states that "the embedding models remains constant while the" downstream LLM varies.[^m13] These two statements do not match, and the sections read do not resolve it. The gap cannot be credited to representation alone.
- The benchmark is 40 questions from one company's earnings calls, "a newly created financial earnings call" set.[^m14] Results are macro-averaged. No confidence interval or significance test appears in the parts read, although the paper speaks of "stronger evidence".
- The answer judge is GPT-5, which is also one of the six answering models.[^m15] Whether that favours the GPT-5 answers in either arm is not tested here; this is my inference, not a finding.
- The answer comparison also changes what the answering model sees. The native arm passes the retrieved images themselves to the vision model, the text arm passes summaries, so the answer gap includes the generator's input, not only the retrieval.
- One summarizer and one prompt were used. A richer description might close part of the ranking gap; that was not tested.
- The text-only arm's relevance is judged by exact page match. The paper does not show how many near-miss pages each arm returns.

## Related

- [[caption-utility-gap]] — the same surrogate, measured by how well a text-only reader answers from it rather than by how it ranks
- [[page-image-evidence-unit]] — the slide or page kept as an image and used as the retrieval unit, with no text intermediate; this paper's native arm is that choice, measured against summaries
- [[modality-wise-retrieval]] — a shared multimodal space can misplace cross-modal items; the native arm depends on that space, and this paper does not test calibration

[^m1]: arxiv-2511-16654 — "These text descriptions serve as surrogates for"
[^m2]: arxiv-2511-16654 — "may omit spatial structure, layout, or numeric precision present in the original image"
[^m3]: arxiv-2511-16654 — "maps both text and images into a shared semantic vector space"
[^m4]: arxiv-2511-16654 — "each slide treated as a distinct retrievable unit"
[^m5]: arxiv-2511-16654 — "mAP@5 of 0.5234 compared to 0.3963"
[^m6]: arxiv-2511-16654 — "Precision@5 improves from 0.480 to 0.540"
[^m7]: arxiv-2511-16654 — "placing the most relevant documents higher in"
[^m8]: arxiv-2511-16654 — "average win rate of 0.612 compared to 0.388"
[^m9]: arxiv-2511-16654 — "the multimodal approach prevents unsupported additions 90% of the time"
[^m10]: arxiv-2511-16654 — "fabricated details that propagate to downstream generation"
[^m11]: arxiv-2511-16654 — "multimodal embedding pipelines require explicit image detection, extraction, and format conversion steps"
[^m12]: arxiv-2511-16654 — "with OpenAI text-embedding-ada-002 for text-only"
[^m13]: arxiv-2511-16654 — "the embedding models remains constant while the"
[^m14]: arxiv-2511-16654 — "a newly created financial earnings call"
[^m15]: arxiv-2511-16654 — "OpenAI GPT-5 performs pairwise comparisons"
