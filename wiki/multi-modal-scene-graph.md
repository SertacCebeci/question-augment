---
description: "A scene graph whose triplets cover sound as well as image, built without the question, added 1.13 accuracy points to audio-visual QA on MUSIC-AVQA."
aliases: ["audio-visual scene graph", "multi-modal scene graph decoder", "M2SG"]
sources: ["arxiv-2511-23304"]
---
# Multi-modal scene graph

A scene graph decomposes a scene into objects and their pairwise relations, and stores each relation as a triplet. The representation was introduced for image retrieval, and the authors credit it with "richer and more interpretable semantic context than global feature embeddings".[^c1] The multi-modal version extends the vocabulary from image to sound. For each temporal segment the graph is a set of typed edges, "Each edge is represented as a subject–predicate–object triplet".[^c2]

The construction is two-stage and question-blind. A decoder with learnable relation queries, in the query-based style that lets a model "directly predict a set of relation triplets via learnable queries and bipartite matching", is trained to predict each segment's triplets from its audio and visual input.[^c3] The authors exclude the question on purpose: "we intentionally exclude question-related textual features from the model input".[^c4] The question enters afterwards. The selection module "only filters the query-relevant triplets within each individual segment",[^c5] and a classifier then predicts the answer.[^c6]

The claimed value is in relations that visual structure alone cannot state. Existing scene-graph methods "are confined to purely visual scenarios and cannot express auditory relations", such as loudness or activity: "whether an instrument is actually being played rather than merely held."[^c7] The motivating question is "Which clarinet makes the sound first?", which from audio alone "can be ambiguous due to sound blending". The authors argue that "learning from multimodal structural relationships, such as spatial arrangement, can provide clearer cues for accurate identification."[^c8]

The measured effect is modest. On MUSIC-AVQA, adding the graph alone gives "the Multi-Modal Scene Graph alone improves the average accuracy by 1.13% (77.56% vs. 76.43%)".[^c9] The selection step has its own curve, where "when topk is set to 8, the model reaches an accuracy of 77.69%", against 78.14% for the full model at top-k 10.[^c10] The one transfer test is WorldSense, where, with candidates normalized into 36 objects and 13 relations, "our method achieves 31.21% accuracy, outperforming QATIGER by 2.13% (29.08%)."[^c11]

What survives the move from image retrieval is the triplet itself: a relation that a reader can name, check and select among. What does not survive without rework is the predicate vocabulary. The authors fix it to the task, "a compact, task-oriented ontology whose entity and predicate categories" are defined by the dataset.[^c12] My inference is that a triplet is only as checkable as the vocabulary shared by whoever builds the graph and whoever reads it.

## Limits

- The gain is small and comes from one benchmark family. The 1.13-point gain is on MUSIC-AVQA, which is built from musical performance videos. The WorldSense result is a single transfer test. In the slices read I found no variance across runs, so a one-point difference is not shown to exceed run-to-run noise.
- Question-blindness is argued, not tested. The reason for excluding the question is the authors' own: "Incorporating textual information may introduce bias or unintended priors that could interfere with accurate scene graph prediction."[^c13] The text read contains no question-aware graph to compare with, so whether question-blind construction is more accurate, or only cheaper to share across questions, is open here.
- The graph and its selection are not separated. The ablation that isolates the graph compares it with a baseline; selection is varied only as the top-k curve. The authors say the selection step "does not, by itself, perform any temporal localization",[^c14] which fixes its role but not its share of the gain.
- The ground truth is machine-built. The dataset comes from "a cascaded three-stage annotation pipeline with rule-based verification and regeneration";[^c15] the slices read report no human accuracy check of the triplets. The reasoner sees a decoder's predictions, so annotation error and prediction error both reach the answer.
- Vocabulary is the transfer cost. The authors state the framework can be adapted "simply by redefining the underlying vocabulary";[^c16] a redefinition needs labelled data to build the graph, and the paper's transfer claim rests on one additional setting.

## Related

- [[write-time-relevance-commitment]] — the graph is fixed before any question, as a write-time store is; the question then chooses among its triplets, which is the query-time half of that split.
- [[structure-then-select-compression]] — structure first, then query-relevant selection under a budget, applied to text context rather than video.
- [[incremental-structure-retrieval]] — a queryable scene graph read step by step for 3D grounding; here the triplets are precomputed per segment and the answerer does not traverse them.

[^c1]: arxiv-2511-23304 — "richer and more interpretable semantic context than global feature embeddings"
[^c2]: arxiv-2511-23304 — "Each edge is represented as a subject–predicate–object triplet"
[^c3]: arxiv-2511-23304 — "directly predict a set of relation triplets via learnable queries and bipartite matching"
[^c4]: arxiv-2511-23304 — "we intentionally exclude question-related textual features from the model input"
[^c5]: arxiv-2511-23304 — "only filters the query-relevant triplets within each individual segment"
[^c6]: arxiv-2511-23304 — "Finally, a classifier is employed to predict the answer to the question"
[^c7]: arxiv-2511-23304 — "whether an instrument is actually being played rather than merely held"
[^c8]: arxiv-2511-23304 — "learning from multimodal structural relationships, such as spatial arrangement, can provide clearer cues for accurate identification"
[^c9]: arxiv-2511-23304 — "the Multi-Modal Scene Graph alone improves the average accuracy by 1.13% (77.56% vs. 76.43%)"
[^c10]: arxiv-2511-23304 — "when topk is set to 8, the model reaches an accuracy of 77.69%"
[^c11]: arxiv-2511-23304 — "our method achieves 31.21% accuracy, outperforming QATIGER by 2.13% (29.08%)"
[^c12]: arxiv-2511-23304 — "We use a compact, task-oriented ontology whose entity and predicate categories"
[^c13]: arxiv-2511-23304 — "Incorporating textual information may introduce bias or unintended priors that could interfere with accurate scene graph prediction."
[^c14]: arxiv-2511-23304 — "does not, by itself, perform any temporal localization"
[^c15]: arxiv-2511-23304 — "a cascaded three-stage annotation pipeline with rule-based verification and regeneration"
[^c16]: arxiv-2511-23304 — "be readily adapted to other domains simply by redefining the underlying vocabulary"
