---
description: "Chunk boundaries learned from sentence pairs labelled by human section structure beat cosine-threshold semantic splits on PubMed retrieval; generation gains were not clearly separated."
aliases: ["Projected Similarity Chunking", "Metric Fusion Chunking", "PSC and MFC chunkers", "trained boundary chunking"]
sources: ["arxiv-2512-00367"]
---
# Learned-boundary semantic chunking

A retrieval-augmented system has to cut each document into chunks before indexing, and where the cuts fall limits what the retriever can return. The common semantic method cuts where the cosine similarity between adjacent sentences drops below a threshold. The learned variant replaces that rule with a trained scorer. The paper's premise is that a raw distance is the wrong target, so the models are trained "to be able to amplify the distances and give us scores" that the chunker then cuts on.[^c1]

The supervision is what changes. Positive pairs are consecutive sentences that a human author grouped under one section: "sentences grouped by the human author within the same section".[^c2] Negative pairs are "randomly selecting sentences from different sections within the same document that never co-occur in any section".[^c3] The training set is built from full-text PubMed Central articles, with "93M sentence" pairs in total.[^c4] The model therefore learns when two sentences belong together by the document's own structure, not by embedding distance alone.

Two scorers are proposed. Projected Similarity Chunking (PSC) takes the dot product of two linearly transformed embeddings as its score. Metric Fusion Chunking (MFC) combines dot product, Euclidean and Manhattan distance with equal weight and passes them through one neural layer. A sigmoid turns the score into a probability, and a boundary is placed where it falls below 0.5, a threshold the paper reports as "(determined emperically)".[^c5] Each embedding model (MiniLM, mpnet, e5) gets its own chunker.

What the paper reports. On PubMedQA with gold context sentences, retrieval rose sharply: "MRR improves from 0.0086 (recursive) to 0.2914 (PSC in e5)".[^c6] The library cosine-threshold semantic chunker performed worse in the same setup, which the authors attribute to "due to its reliance on cosine similarity for chunk boundary detection".[^c7] The conclusion puts the best case at "increase of up to 24 times over baseline methods", for MFC on e5.[^c8] The authors' account of why is that the chunks "align with human-authored section boundaries".[^c9]

Generation moved less. The paper says PSC and MFC perform "competitively and often surpassing baselines",[^c10] yet its own table caption says "Character chunking with miniLM, MFC with mpnet and E5 perform the best",[^c11] so the fixed-length baseline wins in one configuration. The PSC-versus-Char p-values are reported only as "less than 0.3 and t-test values around than 1".[^c12] The paper's own confidence statement is "a confidence of 99.9% for retrieval, and 90% for generation".[^c13] The authors explain the weak generation signal by metric blindness: "Standard metrics like BLEU, ROUGE, and BERTScore prioritize" lexical overlap, which they say fails to show their chunkers' advantage.[^c14] That explanation is the authors' own and is not tested in the text.

Out of domain, the chunkers were trained only on PubMed. For RAGBench, "we evaluate only generated answers",[^c15] and the authors report "a clear improvement in the performance across all datasets with our chunkers".[^c16] Those are generation metrics, the same kind that showed little separation in-domain.

Cost is modest. Indexing time rose by "a slight increase of 0.7s against Character chunker",[^c17] and training took "under 12 hours" per model combination.[^c18] The authors stress that indexing is a one-time offline step.

## Limits

- Chunk length is confounded with boundary placement. The learned chunkers produce "PSC and MFC produce naturally variable chunk lengths",[^c19] "averaging 471 tokens",[^c20] against fixed chunks of "1000-token chunk size with 200-token overlap".[^c24] The paper credits variable length as part of the gain, but it never separates length from where the cuts fall. The comparison changes both at once.
- The retrieval gold is the abstract's context sentences, which "were used to evaluate retriever performance".[^c21] Training and evaluation both draw on PubMed article structure, so the test is close to the training distribution. (My inference; the text does not discuss it.)
- The in-domain test set is small: the PQA-L subset "comprising 115 documents".[^c22] The generator is one model fed the top-5 chunks, and the authors state that "ensures all performance differences arise solely from the chunking".[^c23] The top-5 setting interacts with chunk length, so the two effects are not separated here. (My inference.)
- The 0.5 threshold is set empirically on this data, and the paper picks the checkpoint from epoch 4 of 5 by its evaluation results. No sensitivity sweep over either choice is reported.
- The positive class exists only where a human author marked sections. Documents without that structure yield no such labels, and the paper does not test them. (My inference from the training design.)
- Only one library baseline is used for semantic chunking, and its weak showing is partly the authors' argument that cosine boundaries are poor. The paper does not test a cosine-based chunker tuned to the same data.

## Related

- [[decoupled-search-context-chunk-size]] — the same tension between small search units and larger answer context; that note fixes the size split, while this one is about where the cuts go. Neither tests the other's choice.
- [[page-image-evidence-unit]] — argues that the page should be the retrieval unit and text segmentation can be skipped; it has no chunked-text baseline, so it does not bear on whether learned cuts beat fixed ones.

[^c1]: arxiv-2512-00367 — "we train our models to be able to amplify the distances and give us scores"
[^c2]: arxiv-2512-00367 — "sentences grouped by the human author within the same section"
[^c3]: arxiv-2512-00367 — "randomly selecting sentences from different sections within the same document that never co-occur in any section"
[^c4]: arxiv-2512-00367 — "The final dataset contained 93M sentence"
[^c5]: arxiv-2512-00367 — "(determined emperically)"
[^c6]: arxiv-2512-00367 — "MRR improves from 0.0086 (recursive) to 0.2914 (PSC in e5)"
[^c7]: arxiv-2512-00367 — "due to its reliance on cosine similarity for chunk boundary detection"
[^c8]: arxiv-2512-00367 — "increase of up to 24 times over baseline methods"
[^c9]: arxiv-2512-00367 — "align with human-authored section boundaries"
[^c10]: arxiv-2512-00367 — "competitively and often surpassing baselines"
[^c11]: arxiv-2512-00367 — "Character chunking with miniLM, MFC with mpnet and E5 perform the best"
[^c12]: arxiv-2512-00367 — "less than 0.3 and t-test values around than 1"
[^c13]: arxiv-2512-00367 — "a confidence of 99.9% for retrieval, and 90% for generation"
[^c14]: arxiv-2512-00367 — "Standard metrics like BLEU, ROUGE, and BERTScore prioritize"
[^c15]: arxiv-2512-00367 — "we evaluate only generated answers"
[^c16]: arxiv-2512-00367 — "a clear improvement in the performance across all datasets with our chunkers"
[^c17]: arxiv-2512-00367 — "there is a slight increase of 0.7s against Character chunker"
[^c18]: arxiv-2512-00367 — "Training time for each model combination was under 12 hours"
[^c19]: arxiv-2512-00367 — "PSC and MFC produce naturally variable chunk lengths"
[^c20]: arxiv-2512-00367 — "averaging 471 tokens"
[^c21]: arxiv-2512-00367 — "were used to evaluate retriever performance"
[^c22]: arxiv-2512-00367 — "comprising 115 documents"
[^c23]: arxiv-2512-00367 — "ensures all performance differences arise solely from the chunking"
[^c24]: arxiv-2512-00367 — "We adopt a 1000-token chunk size with 200-token overlap"
