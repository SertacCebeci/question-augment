---
description: "Relevance feedback refines a query embedding toward top-ranked items and away from others at inference time; for VLM image search, plain pseudo-relevance feedback did not beat no feedback."
aliases: ["Rocchio for VLMs", "vector-space relevance feedback", "embedding-space Rocchio", "relevance feedback for VLM retrieval"]
sources: ["arxiv-2511-17255"]
---
# Embedding-space relevance feedback

Relevance feedback changes the query, not the retrieval model. The paper's phrasing: "Instead of modifying the retrieval model, this paradigm refines query vectors using representations of relevant and irrelevant items at inference time."[^c1] Given a query embedding and the embeddings of the items a first pass ranked highest, the Rocchio rule builds a new query: the original vector, plus a weighted mean of the top-ranked items as positive feedback, minus a weighted mean as negative feedback. Rocchio's original idea is to reinforce relevant document vectors and reduce the influence of non-relevant ones.[^c2]

The adaptation to vision-language models (VLMs) changes two things, both stated by the authors: "applying softmax-weighted averaging for feedback aggregation" and sourcing both positive and negative feedback from top-ranked items.[^c3] The softmax weights come from cosine similarity with a temperature; the paper uses τ = 0.05, so the weights concentrate on the closest candidates.[^c4] The negative weight of each candidate is one minus its positive weight, so the two sets split one pool.[^c4] Because the negative side is drawn from the same top-ranked items, the model "focuses on hard negatives": candidates the VLM already finds relevant that do not match the query.[^c3]

## What transfers and what does not

The arithmetic transfers without words. It needs only a shared space where a query and an item can be compared by cosine, which contrastively trained VLMs provide. My inference: it does not need term statistics, so the sparse-retrieval machinery of [[feedback-term-selection-and-weighting]] (term selection, idf-like weights) has no counterpart here; only the weighting scheme carries over.

Two obstacles to plain Rocchio in VLMs are named in the text. First, "the multimodality gap" of contrastive models, which can make combining visual and textual vectors suboptimal.[^c5] Second, Rocchio "is applied to aggregate global embeddings", so fine-grained patch and word detail is discarded.[^c6] The paper's answer is a learned summarizer and a caption-based feedback signal; the summarizer is a method and is not restated here, and the caption signal has its own note, [[caption-based-relevance-feedback]].

## What was measured

Four feedback strategies were run on Flickr30k and COCO with four VLM backbones. Plain pseudo-relevance feedback (PRF, the top-ranked images as feedback) "does not improve over baseline" retrieval without feedback.[^c6] The other three, including explicit feedback simulated with ground-truth captions as an upper bound, "improve retrieval performance by 3–5% in MRR@5 for smaller VLMs" and by less for larger ones.[^c7][^c8]

Feedback was also iterated over rounds, using the top five items of the previous round. Explicit feedback "continuously improves retrieval performance according to all metrics" in the appendix runs.[^c9] The caption variant "begins to decline starting from the third round of retrieval".[^c10] The paper offers a guess: the decline "may be linked to the query drift phenomenon discussed in the relevance feedback literature."[^c11] The learned summarizer stayed positive across rounds. The mechanism is my reading: the query is pulled toward the centroid of what the model already ranks high, so when those top items are wrong the pull reinforces the error. That is the drift named in [[query-expansion-harm-asymmetry]], in term space.

## Limits

- Only VLM backbones were tested. The claim that the method is "model-agnostic" is the authors'; the text shows no run on a non-VLM retriever.
- The competitor set is narrow: "we do not compare against alternative query adjustment methods" such as LLM query rewriting, so whether feedback beats rewriting is open.[^c12]
- Explicit feedback uses the other human captions of the same image. That is an upper bound on feedback quality, not a measure of what a real user would supply.
- Gains are small (1–3% for larger models) and come from a fixed benchmark with one query per image, not from a user study.
- Only five rounds were run; whether the drift grows beyond that was not measured.
- The multi-turn decline is a hypothesis in the paper, not a tested cause.

## Related

- [[query-expansion-harm-asymmetry]] — the term-space form of the same drift, measured in a user audit.
- [[feedback-term-selection-and-weighting]] — Rocchio weighting over LLM expansions in BM25 term space; the same formula on sparse terms.
- [[llm-filtered-pseudo-relevance-feedback]] — PRF in term space, with an LLM judge filtering the feedback set.
- [[caption-based-relevance-feedback]] — a feedback signal built from precomputed captions, aggregated by this rule.

[^c1]: arxiv-2511-17255 — "Instead of modifying the retrieval model, this paradigm refines query vectors using representations of relevant and irrelevant items at inference time"
[^c2]: arxiv-2511-17255 — "reinforcing relevant document vectors and reducing the influence of non-relevant ones"
[^c3]: arxiv-2511-17255 — "we ensure that the model focuses on hard negatives"
[^c4]: arxiv-2511-17255 — "We use τ = 0.05"
[^c5]: arxiv-2511-17255 — "the multimodality gap"
[^c6]: arxiv-2511-17255 — "PRF does not improve over baseline"
[^c7]: arxiv-2511-17255 — "improve retrieval performance by 3–5% in MRR@5 for smaller VLMs"
[^c8]: arxiv-2511-17255 — "ground-truth captions as an upper-bound baseline"
[^c9]: arxiv-2511-17255 — "captions continuously improves retrieval performance according to all metrics"
[^c10]: arxiv-2511-17255 — "the performance of GRF begins to decline starting from the"
[^c11]: arxiv-2511-17255 — "drift phenomenon discussed in the relevance feedback literature"
[^c12]: arxiv-2511-17255 — "we do not compare against alternative query adjustment methods"
