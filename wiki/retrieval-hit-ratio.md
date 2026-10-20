---
description: "The share of retrieved contexts containing the gold answer, scored apart from the reader; conditioned on hits, reader accuracy gives an approximate upper bound for retrieval-augmented QA."
aliases: ["hit rate", "hit ratio", "retrieval hit rate", "answer hit rate", "retrieval-side upper bound"]
sources: ["doi-10-48550-arxiv-2305-14283", "arxiv-2601-00841"]
---
# Retrieval hit ratio

In a pipeline where one stage changes what the next stage receives, end-task accuracy mixes the two stages. A retriever can fetch the answer and the reader still miss it, or the reader can be strong and the retriever weak. The hit ratio is a measure on the retrieval side alone. In Ma et al. (2023) it is defined as: "After text normalization, the hit rate is computed to measure whether the retrieved context contains the correct answers."[^c1] It asks whether the gold answer string appears in what was retrieved. It does not ask whether the reader used it.

The paper pairs the hit ratio with a conditional reader score. Take the questions whose standard retrieval already hits the answer, and score the reader on that subset: "The scores show the approximate upper bound ability of the reader with retrieval augmentation."[^c2] The subset is "computed on a selection of the samples whose retrieved contexts hit correct answers," and the selection is made under the standard retrieve-then-read setting, not under each rewritten query.[^c3] The result is a ceiling for what a reader can do with a given amount of retrieval success, which lets a gain be assigned to retrieval or to reading.

## What it showed

On AmbigNQ, the paper compares Bing snippets with pages fetched and filtered by BM25. Content selection with BM25 "recalls better documents than snippets," and query rewriting helps in both settings: "while query rewriting makes progress on both settings."[^c4] The more useful comparison is between stages: "the improvement in the hit rate of the retriever is more significant than the improvement in the reader."[^c5] In this paper, most of the rewrite's effect shows up upstream, and the reader converts only part of it into answer accuracy. The authors say this matches related search findings but do not measure a general law.

The same quantity serves as a training signal. The reward for the trained rewriter includes an indicator that gives credit "if the retrieved content hits the answer and penalize[s] if misses the answer."[^c6] So for that rewriter, hit is both a reward and an evaluation metric.

A higher hit ratio does not guarantee a better end-task result once retrieval is priced. In a per-query RAG controller that chooses retrieval depth and generation mode, the margin-weighted learner under the quality-first profile reached a higher hit rate than the baseline and still scored worse: the author reports a higher retrieval hit-rate but worse reward than the best fixed baseline.[^c7] The explanation offered is that more retrieved context costs tokens and can add distractors: "length can raise costs and introduce distractors."[^c8] So the hit ratio measures what reached the reader, and the reward measures what the reader was charged for. Both are needed, and the first alone can rank a configuration above one that scores better downstream.

## Limits

- The hit is a containment test after text normalization. Whether a passage that contains the answer string also supports it is not measured. My inference, not the paper's claim: a short answer string can occur in passages that do not establish it, so a high hit ratio is an upper limit on evidence, not evidence.
- Only the AmbigNQ analysis in the paper uses this split. The other datasets are reported only by end-task scores, so the retrieval-versus-reader pattern is one dataset's result.
- The upper-bound row conditions on hits of the standard retrieval, not of the rewritten query. The authors call it "approximate" for that reason. A rewriter that retrieves different passages is compared against a subset chosen by a different retriever.
- Where the hit is also the training reward, a rise in hit ratio is partly built in. It cannot by itself show that the reader benefits.
- The retriever is a live web search. My inference: hit rates from such a retriever depend on the date and the index state, so they are not reproducible across time without a frozen snapshot. The paper does not discuss this.
- The routing study's hit rate is computed on answerable questions only, with N = 200 per condition, and the author calls it "a coarse proxy": it does not capture semantic support, multi-hop reasoning, or non-extractive settings.[^c9] The hit-rate gap there is one result, not a measured regularity.

## Related

- rewrite-retrieve-read — the pipeline in which the split between retrieval and reading is used
- [[evidence-forgetting-rate]] — the reader-side complement: among cases where the golden evidence was retrieved, the share still answered wrong
- [[prompted-versus-trained-query-augmentation]] — rewriting methods compared on retrieval outcomes, where a retrieval-side metric is also the training target

[^c1]: doi-10-48550-arxiv-2305-14283 — "After text normalization, the hit rate is computed to measure whether the retrieved context contains the correct answers."
[^c2]: doi-10-48550-arxiv-2305-14283 — "The scores show the approximate upper bound ability of the reader with retrieval augmentation"
[^c3]: doi-10-48550-arxiv-2305-14283 — "computed on a selection of the samples whose retrieved contexts hit correct answers"
[^c4]: doi-10-48550-arxiv-2305-14283 — "while query rewriting makes progress on both settings"
[^c5]: doi-10-48550-arxiv-2305-14283 — "the improvement in the hit rate of the retriever is more significant than the improvement in the reader"
[^c6]: doi-10-48550-arxiv-2305-14283 — "an indicator to reward if the retrieved content hits the answer and penalize if misses the answer"
[^c7]: arxiv-2601-00841 — "hit-rate but worse reward than the best fixed baseline"
[^c8]: arxiv-2601-00841 — "length can raise costs and introduce distractors"
[^c9]: arxiv-2601-00841 — "This is a coarse proxy"
