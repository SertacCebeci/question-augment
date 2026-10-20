---
description: "The cutoff that turns graded relevance scores into positive/negative training labels changes dense-retrieval results, and its best value varies with language resource level."
aliases: ["relevance threshold calibration", "positive/negative boundary for contrastive fine-tuning"]
sources: ["arxiv-2601-04395"]
---
# Graded relevance binarization threshold

Dense retrievers are fine-tuned contrastively, which needs binary positives and negatives, although relevance is graded. When annotators (here LLMs) give scores, a threshold on the scale decides which passages are pulled toward the query and which are pushed away. The paper treats this threshold as a design choice that is usually overlooked.[^c1]

## What was measured

Candidates were retrieved by a baseline model, scored 0 to 3 by LLMs, and binarized at thresholds 1, 2 or 3 before contrastive fine-tuning. Three settings were tested: monolingual, multilingual mixture, and cross-lingual retrieval.[^c2]

- Monolingual: lower-resource languages tended to do better with lower (more inclusive) thresholds, and higher-resource languages with higher (stricter) ones.[^c3]
- Mixture: a single global threshold was found clearly suboptimal. The best value depends on the target language and on which language is mixed in.[^c4]
- Cross-lingual: a well-matched threshold gave fine-tuned models better results than the non-fine-tuned baseline, while an unsuitable one often fell below that baseline. English as the corpus language was an exception that favored higher thresholds.[^c5]

The authors also report that annotators disagreed, especially in lower-resource languages, and that thresholding softens some of this noise.[^c6] Their proposed reading, not a tested mechanism, is that low-resource settings gain from keeping more variability among positives.[^c7]

## Limits

- Only a few retrieval tasks, models, languages, one annotation pipeline and thresholds 1 to 3 were tested; the authors expect threshold behavior to vary elsewhere.[^c8]
- Moving the threshold also changes the positive/negative balance. The authors argue the opposing effects across languages suggest this is not dominant, but it is not isolated.[^c8]
- Why resource level matters (pre-training coverage, benchmark artifacts) is speculation in the paper.
- Candidates came from a baseline retriever before annotation, which shapes what the labels can express.
- The step from this to how a person should ask or judge relevance is my inference and is not tested here.

## Related

- [[llm-filtered-pseudo-relevance-feedback]] — also uses LLM relevance judgments, as a filter on retrieved passages instead of a training label.

[^c1]: arxiv-2601-04395 — "Even when graded relevance is available, the choice of where to place the threshold is often overlooked as a significant design decision"
[^c2]: arxiv-2601-04395 — "monolingual retrieval (§4), multilingual mixture finetuning (§5), and cross-lingual retrieval (§6)"
[^c3]: arxiv-2601-04395 — "Lower-resource languages tend to benefit from lower thresholds, whereas higher-resource languages perform better with higher thresholds."
[^c4]: arxiv-2601-04395 — "in multilingual mixture settings, a single global threshold is clearly suboptimal"
[^c5]: arxiv-2601-04395 — "an unsuitable threshold often leads to underperformance relative to the baseline"
[^c6]: arxiv-2601-04395 — "While thresholding mitigates some annotation noise"
[^c7]: arxiv-2601-04395 — "suggesting that preserving greater variability in relevance pairs is beneficial in such settings"
[^c8]: arxiv-2601-04395 — "Each setting requires its own assessment rather than relying on a single universal threshold."
