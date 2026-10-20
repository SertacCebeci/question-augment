---
description: "A generalist model re-ranks a discriminative expert's top-k shortlist with exemplars and confidence scores; the true class sits in that shortlist far more often than at top-1."
aliases: ["post-hoc correction", "POC", "top-k recovery", "shortlist re-ranking", "expert-generalist complementarity"]
sources: ["arxiv-2512-15748"]
---
# Expert-shortlist correction

A discriminative expert is wrong at top-1 long before it is wrong at top-k. In visual species recognition, a few-shot finetuned vision encoder often misses the true species at rank one, yet its top-k predictions, "even for small k =3", often contain it.[^c1] The expert's ranking is therefore a shortlist whose recall the top-1 hides. The correction move hands that shortlist to a second model that chooses among the candidates, not over the whole label space.

The paper's first evidence concerns label-space size. The authors read the gap between open naming and candidate-restricted naming as showing that "set of candidate species, rather than the entire label space, may" help a large model, and that the advantage shrinks as the number of classes grows.[^c2]

The second stage is a multimodal prompt. It receives the k candidates with scientific and common names, the expert's confidence for each, and the few-shot training images of those candidates stitched into one picture. It is asked to re-rank the candidates against the test image, and the top re-ranked item is the answer.[^c3][^c4] The authors prefer re-ranking to picking one: "Reranking promotes a CoT-like reasoning process".[^c5]

The shortlist alone is not the mechanism. The same top-k names, given with a select-one instruction and no exemplars, lowered mean accuracy from 59.2% to 49.7% on the five benchmarks, and the authors conclude that such prompting is "insufficient to effectively exploit the complementary" strengths of the two models.[^c6][^c7] With the exemplars, the confidence scores and the re-ranking, the paper reports a mean gain of 6.4 accuracy points over the expert, averaged across five benchmarks.[^c8]

The gain has a ceiling. With a fixed LMM, the final accuracy "is upper-bounded by the top-5 accuracy of the expert models", so a true class that falls outside the shortlist cannot be recovered.[^c9] Enlarging the shortlist helps only up to a point: "gains plateau beyond around k = 10 across all datasets".[^c10] The correction is not free of new errors; POC can "correct these misclassifications while occasionally introducing" mistakes of its own.[^c11]

My reading, not the paper's claim: the split of labour is what carries the gain. The expert supplies a narrow set and an ordering with confidence, which the generalist can weigh; the generalist supplies a comparison of the query against reference exemplars for the few confusable candidates. An answerer whose first commitment is uncertain can thus benefit from a short ranked list with its scores, re-examined by a source that does not share the first one's errors. That generalisation is mine and is not tested in the paper.

## Limits

- The gains are measured on five visual species benchmarks, with one expert family (few-shot finetuned CLIP-style encoders) and mainly one LMM family (Qwen-2.5-VL-7B, with GPT5-Mini and others in supplementary tables). The text I read does not test other domains or non-visual shortlists.
- The prompt was built by iteration: "we progressively improve prompts to instruct the LMM".[^c12] Whether that iteration touched held-out data is not established in the text I read, so the benchmark gain may be an optimistic figure (my inference).
- The method is described as "training-free, validation-free," and model-agnostic.[^c13] Those are the authors' words for their own benchmarks; a cost per item, and behaviour on classes without exemplar images, are not reported in the part I read.
- The mean gain hides spread: the abstract reports an average, and the per-dataset changes in the table vary in sign.
- The ceiling is structural: a true species outside the top-k is lost before the LMM sees the image.

## Related

- [[two-stage-reranking]] — the same cheap-then-costly shape; this note adds that the second stage is a multimodal model given exemplars and the first stage's confidences
- [[candidate-selection-gap]] — the same gap between what a candidate list contains and what a selector picks, measured on SQL candidates
- [[candidate-constrained-entity-identification]] — the same finding that naming from a candidate list beats open naming; this note adds a case where a bare shortlist prompt hurt

[^c1]: arxiv-2512-15748 — "its top-k predictions (e.g., even for small k =3) often"
[^c2]: arxiv-2512-15748 — "set of candidate species, rather than the entire label space, may"
[^c3]: arxiv-2512-15748 — "by additionally providing their confidence scores"
[^c4]: arxiv-2512-15748 — "The top-1 re-ranked species is chosen as the final prediction"
[^c5]: arxiv-2512-15748 — "Reranking promotes a CoT-like reasoning process"
[^c6]: arxiv-2512-15748 — "the mean accuracy drops from 59.2% to 49.7%"
[^c7]: arxiv-2512-15748 — "predictions is insufficient to effectively exploit the complementary"
[^c8]: arxiv-2512-15748 — "improve FSL expert models by 6.4 accuracy points, averaged over five VSR benchmarks"
[^c9]: arxiv-2512-15748 — "is upper-bounded by the top-5 accuracy of the expert models"
[^c10]: arxiv-2512-15748 — "gains plateau beyond around k = 10 across all datasets"
[^c11]: arxiv-2512-15748 — "correct these misclassifications while occasionally introducing"
[^c12]: arxiv-2512-15748 — "we progressively improve prompts to instruct the LMM"
[^c13]: arxiv-2512-15748 — "POC is training-free, validation-free,"
