---
description: "Queries written after seeing the answer are over-specific; real users ask general queries that match several answers, and models trained on the former degrade sharply on the latter."
aliases: ["caption-based versus search queries", "visual bias in query annotation", "language gap and multi-moment gap"]
sources: ["doi-10-48550-arxiv-2603-02363"]
---
# Caption-to-search query shift

Benchmarks for video moment retrieval (VMR: find the time segments of a video that match a text query) take their queries from captions that annotators wrote after watching the video. Pujol-Perich et al. (2026) argue this "induces a visual bias, leading to overly descriptive and fine-grained queries."[^c1] Real users usually ask without having watched the video, so their queries are more general. Their example contrasts "a man in a yellow jersey intercepts a loose pass ... and scores a powerful volley" with "when are goals being scored?"[^c2] The general query is under-specified, and the shift has two separate parts.

**Language gap.** The wording itself is less specific. The authors build benchmarks by progressively removing detail from captions, for example "Pick up a tissue from inside the plate on the countertop using the right hand" becomes "Pick up a tissue" and then "Pick up something". A second LLM agent checks each rewrite, and humans fix the ones it flags.[^c3] A model trained on captions and tested on these rewrites degrades more as the query gets vaguer. Single-answer queries on HD-EPIC show the language gap alone, and the loss grows as specificity drops.[^c4]

**Multi-answer gap.** A vague query fits several fine-grained situations. The authors state that "it can correspond to multiple valid moments in" the video.[^c5] They group fine-grained captions that collapse to the same vague query (by sentence-encoder similarity) into one query with several ground-truth moments. Combined with the language gap, this yields the worst results. On the most vague HD-EPIC variant the degradation reached "73.8% compared to the original mAPm @0.3."[^c6] So the multi-answer gap adds a large loss on top of the language gap.

The two gaps need different fixes. The authors leave the language gap to better vision-language models and attack the multi-answer gap architecturally (see [[single-answer-training-prior]]).

## Why the distinction matters

Standard metrics hide the second gap. Top-1 recall or mAP over a query's pooled moments can stay high when a model finds three of four valid moments, so the authors introduce per-moment variants (Rm, mAPm) that score each ground-truth moment on its own.[^c7] This is the paper's measurement, not a general law. It shows that a benchmark whose queries come from the answer-writer's vantage point can misstate how a system behaves under the asker's vantage point.

## Limits

- The search queries are synthetic: LLM rewrites of captions, not logs of real users. Whether they match real search distributions is not tested.
- Multi-moment grouping depends on the datasets' dense annotations and on embedding similarity. Valid matches left unlabelled would count as errors.
- Only video moment retrieval is studied (HD-EPIC, YouCook2, ActivityNet-Captions). Transfer to text question answering is my inference, not a result here.
- The language gap is measured but not mitigated. The work shows no fix for it.

## Related

- [[under-specification-severity-asymmetry]] — a different domain (code generation) where removing detail from a request also costs more than surface wording changes
- [[underspecified-question-eager-answering]] — models answering vague requests as if they were fully specified
- [[ambiguity-taxonomy]] — one vague query mapping to several valid targets is a kind of ambiguity
- [[single-answer-training-prior]] — the training-side cause of the multi-answer gap

[^c1]: doi-10-48550-arxiv-2603-02363 — "overly descriptive and fine-grained queries, which significantly differ from the more general search queries that"
[^c2]: doi-10-48550-arxiv-2603-02363 — "when are goals being scored?"
[^c3]: doi-10-48550-arxiv-2603-02363 — "Pick up something"
[^c4]: doi-10-48550-arxiv-2603-02363 — "the language gap (performance on single) increases as we progressively evaluate"
[^c5]: doi-10-48550-arxiv-2603-02363 — "it can correspond to multiple valid moments in"
[^c6]: doi-10-48550-arxiv-2603-02363 — "73.8% compared to the original mAPm @0.3."
[^c7]: doi-10-48550-arxiv-2603-02363 — "Multi-moment recall (Rm ): Rm generalizes the R1 metric"
