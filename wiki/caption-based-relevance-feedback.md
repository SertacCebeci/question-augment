---
description: "Offline captions of top-ranked images can serve as relevance feedback with no generative model at query time; in VLM image search they helped one round and declined later."
aliases: ["caption feedback", "synthetic-caption relevance feedback", "GRF over captions (not query rewriting)"]
sources: ["arxiv-2511-17255"]
---
# Caption-based relevance feedback

Relevance feedback needs a signal that says what the top-ranked results are about. In text search, generative relevance feedback (GRF) uses a large language model "to expand or rewrite queries".[^c1] The model writes new query text at search time, and that text is fed back. The VLM paper reuses the name for a different mechanism: "we do not create multiple versions of the user query but rather caption the candidate images."[^c2]

The captioner (LLaVA 1.5 in the paper) runs over every candidate image in the collection ahead of time. The captions are encoded by the same VLM, and at query time the captions of the retrieved images are aggregated with the Rocchio rule described in [[embedding-space-relevance-feedback]]. The feedback is therefore text, but text fixed before any query arrives: "can be precomputed offline."[^c3] Nothing is generated per query; the paper says its approach "does not require using large generative" models at inference.[^c10]

Why text helps where the image vector falls short: "aspects that are not evident from the visual representations" are carried by the caption.[^c4] A caption names things a contrastive image embedding may encode weakly, so the feedback can add content the visual vector did not supply. This is the paper's account; the text does not isolate which caption content does the work.

## What was measured

On Flickr30k and COCO, the caption variant is one of three strategies, with AFS and explicit feedback, that the paper reports as improving MRR@5 by 3–5% for smaller VLMs.[^c5] In the multi-turn runs, it declined from the third round: "the performance of GRF begins to decline starting from the third round of retrieval."[^c6] The paper suggests this may come from query drift, as a hypothesis.[^c7] The learned summarizer, by contrast, showed "gradually converging in rounds 3-5, avoiding query drift" in the appendix runs.[^c11]

The overhead is offline: "GRF and AFS strategies introduce some additional overhead. GRF requires running an image captioning" pass.[^c8] My inference: because captions are made for all candidates, the up-front cost scales with collection size, not with the number of queries.

## Limits

- The name collides. The paper's GRF is not the text-search GRF of its reference [15]; a reader must not assume query rewriting here.
- Only one captioner, LLaVA 1.5, is named in the text read. Whether caption quality bounds the gain was not measured in that text; the caption's share of the result is unknown.
- The decline over rounds is a hypothesis. Only five rounds were run.
- The paper "do[es] not compare against alternative query adjustment methods" such as LLM rewriting, so caption feedback versus rewriting is untested.[^c9]
- It is not free of generative models: a captioner runs over the whole collection. "No generative model at inference" is true only at query time.
- Two benchmarks, both with human captions; the feedback is simulated by the paper, not produced by a user.

## Related

- [[embedding-space-relevance-feedback]] — the Rocchio aggregation that consumes these caption embeddings.
- [[reformulation-pattern-library]] — the text-space alternative: an LLM reformulates the query, the reverse of feeding captions back.
- [[query-expansion-harm-asymmetry]] — the term-space drift that the multi-turn decline may share.

[^c1]: arxiv-2511-17255 — "using large language models (LLMs) to expand or rewrite queries"
[^c2]: arxiv-2511-17255 — "create multiple versions of the user query but rather caption"
[^c3]: arxiv-2511-17255 — "can be precomputed offline"
[^c4]: arxiv-2511-17255 — "aspects that are not evident from the visual representations"
[^c5]: arxiv-2511-17255 — "improve retrieval performance by 3–5% in MRR@5 for smaller VLMs"
[^c6]: arxiv-2511-17255 — "the performance of GRF begins to decline starting from the"
[^c7]: arxiv-2511-17255 — "drift phenomenon discussed in the relevance feedback literature"
[^c8]: arxiv-2511-17255 — "GRF and AFS strategies introduce some additional overhead"
[^c9]: arxiv-2511-17255 — "we do not compare against alternative query adjustment methods"
[^c10]: arxiv-2511-17255 — "does not require using large generative"
[^c11]: arxiv-2511-17255 — "gradually converging in rounds 3-5, avoiding query drift"
