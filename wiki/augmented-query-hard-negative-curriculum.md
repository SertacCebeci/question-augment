---
description: "Hard negatives are mined by retrieving with queries augmented from a knowledge graph's answer-relevant neighborhood, then staged so rejections grow harder."
aliases: ["KG-driven hard-negative curriculum", "augmented-query negative mining", "answer-centric curriculum learning", "progressively challenging hard negatives"]
sources: ["arxiv-2511-16326"]
---
# Augmented-query hard-negative curriculum

A retriever learns to reject what it wrongly accepts, so the quality of its training depends on which wrong chunks it is shown. This mechanism builds those chunks on purpose. The negatives are the chunks that a deliberately augmented query brings up, and the augmentations are staged so the rejections become harder over training.

The source of the augmentation is a knowledge graph built by an LLM over the training corpus. The abstract states the logic: the curriculum "leverages LLM-constructed Knowledge Graphs (KGs) to generate augmented queries, which in turn mine progressively challenging hard negatives."[^c1] The graph is used as a generator of negatives, not as a retrieval source. The paper runs Personalized PageRank over the graph to extract a query-specific, answer-relevant subgraph, and that subgraph "guide[s] the creation of augmented queries" — the wording in the text is "which in turn guide the creation of augmented queries."[^c2] Neighbors that co-occur near the gold entities are injected into the query, so that the retriever is drawn toward "false positives—highly related yet insufficient" evidence.[^c3]

The mining step is concrete. For each augmented query, the retriever of the previous stage returns its top-K chunks. Chunks in the positive set are removed, and "the remaining chunks constitute the hard negative" set for that query.[^c4] The positives are the sufficiency-selected chunks described in [[answer-sufficiency-chunk-score]]; the negatives are whatever the augmented query pulls in that is not among them.

The curriculum has three stages. Stage 1 aligns the retriever to the answer-sufficient positives, with the other positives in the mini-batch as negatives. Stage 2 adds the KG-derived negatives: the stage-1 retriever is used "to retrieve the top-K chunks for each complex query."[^c5] Stage 3 uses simpler augmentations, "minor perturbations of the original query (e.g., with only distracting covariates added)," and filters the golden positives out of the result.[^c6] The authors' design principle is that "the difficulty of the discrimination task increases at each" stage.[^c7] The objective stays InfoNCE in every stage; what changes is the set of negatives it is given.

The paper also reports an effect of the curriculum on generalization. Training uses "200 cases each from the" Finance and Legal domains, and the authors say the retriever keeps "robust performance on unseen datasets."[^c8][^c9] The introduction also claims that this mining "yields harder, more calibration-relevant negatives than" random or keyword-based baselines.[^c10]

## Limits

- Hardness is relative to the retriever that mined it. A chunk outside the positive set can still contain the answer, and then it is a false negative. The text read does not measure how often this happens. (My inference from the construction: the positive set is only the top-M by the sufficiency score, so a sufficient chunk that the score missed is labelled as a negative.)
- The graph is built by an LLM, and the paper itself describes community-curated graph clusters as "noisy and insufficiently filtered."[^c11] Noise in the graph reaches the augmented queries, and the text read does not quantify how much.
- The claim that KG-mined negatives beat random or keyword-based negatives is made in the introduction. The ablation the paper describes covers "the three alignment" strategies and the curriculum stages, not the source of the negatives.[^c12] So the parts read do not isolate the value of the KG-based construction from the value of staging.
- Only two training domains, each with 200 cases. The generalization claim rests on the evaluation sets the authors chose; it is not tested on a domain where the graph would be built differently.
- The method depends on a base retriever that is already reasonable. Stage 2 and 3 negatives are retrieved by a model that stage 1 has trained, so an early error in the positives propagates into every later negative set. The text read gives no analysis of this compounding.

## Related

- [[answer-sufficiency-chunk-score]] — selects the positives this curriculum contrasts against; the two are one training pipeline in the paper.
- [[counterfactual-hard-negative]] — builds hard negatives by editing a correct answer into a plausible wrong one; here the negatives are real chunks found by augmented queries, and no answer is edited.
- [[max-distractor-similarity-difficulty]] — orders closed-choice items by distractor similarity into a curriculum before training; here the stages follow the retriever's own state, not an item-level score.
- [[distractor-similarity-reasoning-inflation]] — hard distractors placed in the input at inference; the same kind of difficulty, used at a different point in the pipeline.
- [[answer-supervised-retrieval]] — a different route to retrieval training, where the answer loss rather than a mined contrast shapes the ranking.

[^c1]: arxiv-2511-16326 — "leverages LLMconstructed Knowledge Graphs (KGs) to generate augmented queries, which in turn mine"
[^c2]: arxiv-2511-16326 — "which in turn guide the creation of augmented queries"
[^c3]: arxiv-2511-16326 — "to false positives—highly related yet insufficient"
[^c4]: arxiv-2511-16326 — "The remaining chunks constitute the hard negative"
[^c5]: arxiv-2511-16326 — "Using the retriever fine-tuned in Stage 1, we retrieve the top-K chunks for each complex query"
[^c6]: arxiv-2511-16326 — "minor perturbations of the original query (e.g.,"
[^c7]: arxiv-2511-16326 — "where the difficulty of the discrimination task increases at each"
[^c8]: arxiv-2511-16326 — "sample 200 cases each from the"
[^c9]: arxiv-2511-16326 — "maintaining robust performance on unseen datasets"
[^c10]: arxiv-2511-16326 — "harder, more calibration-relevant negatives than"
[^c11]: arxiv-2511-16326 — "noisy and insufficiently filtered"
[^c12]: arxiv-2511-16326 — "we conduct ablations over the three alignment"
