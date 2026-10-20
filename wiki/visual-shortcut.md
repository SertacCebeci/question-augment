---
description: "A query image showing the target document's own main entity lets retrieval succeed without the question's text, and models trained on such pairs learn to lean on the picture."
aliases: ["visual shortcuts", "image-entity shortcut", "shortcut-prone MKB-VQA benchmark"]
sources: ["arxiv-2511-22843"]
---
# Visual shortcut

A visual shortcut is a property of how a benchmark pairs its inputs. In multimodal knowledge-based visual question answering, each target is a document about one main entity, and the query image usually shows that same entity. The picture then finds the document by itself, and the question's words add little. The paper's preliminary check is a retrieval result: a model trained without the query's text "achieved comparable" retrieval performance, which the paper reads as showing "retrieval performance using only the query image, indicating that existing MKB-VQA benchmarks are largely solvable through visual shortcut exploitation."[^c1][^c2]

The shortcut comes from the pairing rule, not from a model's weakness alone. The existing benchmarks are built so that the target's main entity is the entity in the picture: the paper describes them as biased toward scenarios where the main entity "document typically has the same entity as the query image."[^c3] A learner trained on such pairs can match picture to document and never needs the question. The paper calls the result "these superficial visual correlations."[^c4]

The mechanism of harm is overfitting to the cue. The paper says that multimodal models with a single image per document "tend to overfit to shortcut cues and fail to effectively integrate visual and textual information when such cues are" absent.[^c5] The shortcut is not a bug that a fixed model escapes: on the same paper's RETINA benchmark, where the query image shows a related entity instead of the main one, models "trained on shortcut-prone benchmarks" show "a substantial performance drop."[^c6] On the older benchmarks, single-image multimodal models beat text-only ones; on RETINA the order reverses, and text-only models retrieve better.[^c7]

The paper also measures the cue directly. Documents whose main entity matches the query image, but which are not the target, are called distractors; they are "non-target documents whose main entity corresponds to the query image."[^c8] The single-image retriever is "easily confused by visually similar document images," and the gap between its recall on the target and on distractors stays narrow at larger k.[^c9] The retriever that the paper compares against "is biased toward visual shortcuts and often retrieves documents containing images similar to the query."[^c14]

RETINA removes the cue by construction. The generator makes the document's main entity the answer, and that entity may not be the one depicted in the query image, so the picture is drawn from a related entity instead.[^c10] The same paper also filters generated questions that a lexical search can match: questions "can be retrieved by BM25" in the top five are dropped.[^c11] That filter is the text-side counterpart of the image-side rule, although the paper does not frame it as such. My inference: the text side is handled by a lexical filter, not by a check on the picture.

The shape matches other cases in the wiki where an answer is reachable without the knowledge a question is meant to test. In multiple-choice items the keyed option can be picked from its surface, [[answer-option-surface-cue]]; in a vision-language setting a vision-only baseline can answer from visual cues, which weakens [[cross-modal-aggregation-gap]]. The paper's shortcut is the retrieval version of the same problem: a cue outside the question's content carries the answer.

## Limits

- The preliminary experiment is one model in the sections read, and the figure values were not read. "Comparable" is the paper's word, not a measured gap.[^c2]
- RETINA changes two things at once: the image shows a related entity, and the questions are harder. A drop after the change may partly reflect difficulty. The paper does not separate the two. This is my inference.
- Models were trained on mixed data: the paper says "trained on datasets containing both shortcut and nonshortcut samples."[^c13] So the drop shows how far mixed training leaves the cue in place. It does not show what training with no shortcut would give.
- Only the image path is tested for the cue. The lexical filter addresses lexical overlap between question and document. Other text-side shortcuts, such as a question answerable from world knowledge, are not tested here.
- The paper's own limitations section names inference cost: "This leads to higher inference latency" for multi-image documents.[^c12] It does not discuss shortcut leakage in RETINA's training set.

## Related

- [[answer-option-surface-cue]] — the same structure in multiple-choice items: the keyed option is reachable from its surface, not from the knowledge tested.
- [[cross-modal-aggregation-gap]] — a vision-only baseline can carry part of the answer, so a flat joint result is harder to read.
- [[reverse-constructed-indirect-question]] — the text-side counterpart: a check that a question cannot be answered without its source.
- [[spreading-activation-retrieval]] — multi-hop retrieval reaches documents the query never names, the situation the RETINA queries create on purpose.
- [[conjunctive-masked-criteria]] — a second constraint that narrows a question to one answer, the uniqueness device this paper also uses.

[^c1]: arxiv-2511-22843 — "retrieval performance using only the query image, indicating that existing MKB-VQA benchmarks are largely solvable through visual shortcut exploitation."
[^c2]: arxiv-2511-22843 — "without using the textual component of the query was conducted."
[^c3]: arxiv-2511-22843 — "document typically has the same entity as the query image"
[^c4]: arxiv-2511-22843 — "these superficial visual correlations"
[^c5]: arxiv-2511-22843 — "tend to overfit to shortcut cues and fail to effectively integrate visual and textual information when such cues are"
[^c6]: arxiv-2511-22843 — "which were trained on shortcut-prone benchmarks, we observe a substantial performance drop on RETINA"
[^c7]: arxiv-2511-22843
[^c8]: arxiv-2511-22843 — "whose main entity corresponds to the query image"
[^c9]: arxiv-2511-22843 — "suggesting that the model is easily confused by visually similar document images"
[^c10]: arxiv-2511-22843 — "main entity cannot serve as the concept"
[^c11]: arxiv-2511-22843 — "can be retrieved by BM25"
[^c12]: arxiv-2511-22843 — "This leads to higher inference latency"
[^c13]: arxiv-2511-22843 — "trained on datasets containing both shortcut and nonshortcut samples"
[^c14]: arxiv-2511-22843 — "is biased toward visual shortcuts and often retrieves documents containing images similar to the query"
