---
description: "Questionnaire items can be clustered by embedding their text alone, recovering factor-like groups and a short form cut by about 60% without any respondent data."
aliases: ["semantic latent structure for scale simplification", "text-first questionnaire reduction", "topic-modeling scale simplification"]
sources: ["arxiv-2602-12575"]
---
# Response-free semantic scale reduction

A psychological scale is a set of item texts. This work treats the texts alone as the input and says that "No respondent data, item scores, or empirical covariance information are required at any stage of item reduction."[^c1] The pipeline has five steps. Items are embedded with a pretrained sentence encoder, projected to about 5-15 dimensions with UMAP, and clustered with a density-based method (HDBSCAN) so the number of factors is not fixed in advance.[^c2] Each cluster is labelled by class-based term weighting (c-TF-IDF) keywords. Clusters whose keyword representations have cosine similarity of 0.9 or higher are merged, which "prioritizes conceptual coherence over maximal partitioning".[^c3] Within each final cluster, items are ranked by membership probability, and those above roughly 0.85 are kept as representatives.[^c4]

The reported result, on three instruments (DASS, IPIP, EPOCH-CN), is that density clustering recovered groupings aligned with the established factors. The selected items cut item counts by 60.5% on average, and the short forms kept factor congruence and inter-factor correlations.[^c5] The mechanism is an assumption that semantic proximity of wording stands in for covariance of responses. Where factors are worded distinctly (EPOCH-CN) this works most straightforwardly. Where constructs overlap (DASS), deviations are informative: two anxiety items about bodily sensations (dry mouth, difficulty swallowing) split into their own somatic topic.[^c6]

For asking, the point is that the structure of a question set is partly readable from its wording before anyone answers it. The work also proposes using the pipeline to fix candidate short forms before looking at responses, which reduces researcher freedom in item selection.[^c7] My own inference: the same text-only clustering could flag redundant questions in any question set, though this was tested only on psychometric scales.

## Limits

- The output is a candidate short form. The authors require CFA fit, reliability, and full-versus-short score correspondence before it is accepted.[^c8]
- The semantic space "inevitably reflects its training data and inductive biases", so topics may vary with embedding model and language; only English and Chinese scales, three instruments, and no formal measurement invariance were tested.[^c9]
- Semantic closeness is not equivalence of response process: items can differ in difficulty, extremity or framing, and negation creates method cues. IPIP reverse-keyed items were rewritten to the same direction before embedding, so the pipeline was not tested on raw reverse-worded items.[^c10]
- Clustering hyperparameters and the selection rule are tunable choices, and very short forms are hard to keep broad and stable.[^c11]
- The 60.5% figure is a mean over three scales, not a general rate.

## Related

- [[reverse-worded-items]] — wording style creates method clusters that text embeddings can mistake for content factors
- [[item-writing-guidelines]] — the item wording that determines what the embedding sees
- [[semantic-token-clustering]] — a different use of semantic clustering, on tokens rather than questionnaire items

[^c1]: arxiv-2602-12575 — "No respondent data, item scores, or empirical covariance information are required at any stage of item reduction."
[^c2]: arxiv-2602-12575 — "Density-based clustering via HDBSCAN (hierarchical density-based"
[^c3]: arxiv-2602-12575 — "prioritizes conceptual coherence over maximal partitioning."
[^c4]: arxiv-2602-12575 — "Items were ranked according to their"
[^c5]: arxiv-2602-12575 — "selected through semantic membership probabilities reduced item counts by 60.5% on"
[^c6]: arxiv-2602-12575 — "isolated into a separate"
[^c7]: arxiv-2602-12575 — "thereby reducing researcher degrees of"
[^c8]: arxiv-2602-12575 — "The pipeline outputs candidate short forms whose"
[^c9]: arxiv-2602-12575 — "The semantic space induced by an"
[^c10]: arxiv-2602-12575 — "Items that are"
[^c11]: arxiv-2602-12575 — "Topic modeling"
