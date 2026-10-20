---
description: "A neural evaluation metric can be fooled by one input-independent text that sits near many inputs in its embedding space and scores high whatever the source and reference are."
aliases: ["hubness", "hub text", "adversarial hub", "hubness problem"]
sources: ["arxiv-2512-16323", "arxiv-2511-18808"]
---
# Hubness in neural evaluation metrics

In high-dimensional spaces some points become hubs: they "frequently appear among the nearest neighbors of many examples."[^c1] The phenomenon is old in retrieval, where it returns irrelevant items. The transfer to evaluation is direct. An embedding-based metric scores a hypothesis through its embedding and its similarity to the input and reference.[^c2] If one hypothesis embedding lies close to the embeddings of many sources and references, it gets a high score for whatever pair it is paired with. The score then does not reflect the match between this output and this input.

The paper states the target as an object of the metric itself: a text that "always receives a high score regardless of the input and reference text."[^c3] For COMET it finds such texts in discrete text space, which is harder than in vector space. Continuous hubs "can be searched via gradient descent," whereas for text "we need to search in a discrete space, i.e., NP-hard."[^c4] The procedure trains a hub embedding against the metric's score, decodes it into tokens with an inversion model, and then refines the tokens by local search. The resulting single text reaches 79.1 COMET% on WMT'24 English-to-Japanese,[^c5] above the translations M2M100 produced individually for each source sentence.[^c6] The authors report that scores stay high across test cases,[^c7] and that the steps of the search have low spread compared with M2M100's translations.[^c17]

What it does to evaluation is that a metric's verdict may be decided by a property of the metric rather than by the output. The paper notes that in WMT, where automatic scores decide which systems go to human evaluation, "the hub text can affect the evaluation of other translation systems on the leaderboard."[^c8] The authors draw the lesson that "relying on a single evaluation metric is unreliable,"[^c9] and that the case points to "the necessity of using sanity checks or multiple metrics."[^c10] The mechanism is a reason a high score can be unrelated to the pair it was computed on. A hub is not an error of the training data; it is a geometric property of the score's embedding space.

The same phenomenon is claimed for retrieval over a graph of passages and entities, where it is a fault of the retriever rather than of the evaluator. The HyperbolicRAG paper states that "This behavior arises from the hubness inherent in high-dimensional Euclidean embedding spaces,"[^c18] and its conclusion says the hyperbolic embedding "effectively alleviates the hubness bias inherent in Euclidean embeddings."[^c19] The retrieval side is a geometry with a radial coordinate for specificity, described in [[radial-depth-specificity]]. There the hub is a broad node that lies near many queries, and the claimed cost is retrieval that drifts toward generic evidence.

## Limits

- One metric, one model. The authors use COMET with the Unbabel/wmt22-comet-da3 model as the target, on translation only.[^c11] They claim the method "can be applied to other neural evaluation metrics,"[^c12] but "identifying hub texts across all existing metrics and languages is out of our scope."[^c13] Whether other embedding metrics, or tasks beyond translation, are equally vulnerable is not shown here.
- White-box search. The procedure uses "the contextualized embedding space of the target metric"[^c14] and the score's output layer, so it needs access to internals. Whether a black-box metric can be attacked this way is not reported (my inference: the search as described cannot run without them).
- Cost. Local search "is time-consuming because it has four nested loops."[^c15]
- Retrieval side not counted. The retrieval paper's hubness is a premise, tested only through downstream QA gains; the slices I read give no count of hub nodes. The two cases share a geometry, not a mechanism of attack (my reading).
- Defence not tested. The paper recommends sanity checks and multiple metrics, but does not test either as a remedy; that is my reading of its conclusion.
- Generalisation across language pairs is reported for a hub found in English-Japanese: the text "generalizes across multiple language pairs such as Ja–En and De–En."[^c16] How many hub texts exist, and how they vary across runs, is not characterised in the work.

## Related

- [[prototypicality-bias-in-metrics]] — another way an evaluator's score tracks something other than the pair: typicality rather than an input-independent point.
- [[adversarial-metric-self-review]] — checking a candidate metric's validity before trust; a hub is one reason such checks are needed.
- [[llm-judge-validation-gap]] — judges must be validated against humans; a single text that scores high on a metric shows why a metric's score alone is weak evidence.
- [[radial-depth-specificity]] — a hyperbolic embedding proposed as the retrieval-side remedy for hubs; the same geometry, used to rank evidence by specificity rather than to score outputs.

[^c1]: arxiv-2512-16323 — "hub embeddings frequently appear among the nearest neighbors of many examples"
[^c2]: arxiv-2512-16323 — "calculate similarity with the input and/or reference"
[^c3]: arxiv-2512-16323 — "regardless of the input and reference text"
[^c4]: arxiv-2512-16323 — "which can be searched via gradient descent"
[^c5]: arxiv-2512-16323 — "found with our method achieved 79.1 C OMET%"
[^c6]: arxiv-2512-16323 — "outperforming translations generated individually for each"
[^c7]: arxiv-2512-16323 — "high C OMET scores, regardless of test cases"
[^c8]: arxiv-2512-16323 — "the hub text can affect the evaluation of other translation systems on the leaderboard"
[^c9]: arxiv-2512-16323 — "relying on a single evaluation metric is unreliable"
[^c10]: arxiv-2512-16323 — "necessity of using sanity checks or multiple metrics"
[^c11]: arxiv-2512-16323 — "with a model of Unbabel/wmt22-comet-da3 for"
[^c12]: arxiv-2512-16323 — "our method can be applied to other neural evaluation metrics"
[^c13]: arxiv-2512-16323 — "Exhaustively identifying hub texts across all existing metrics and languages is out of our scope."
[^c14]: arxiv-2512-16323 — "the contextualized embedding space of the target metric"
[^c15]: arxiv-2512-16323 — "is time-consuming because it has four nested loops"
[^c16]: arxiv-2512-16323 — "text generalizes across multiple language pairs such"
[^c17]: arxiv-2512-16323 — "have low SD compared with M2M100’s translations"
[^c18]: arxiv-2511-18808 — "This behavior arises from the hubness inherent in high-dimensional Euclidean embedding spaces"
[^c19]: arxiv-2511-18808 — "effectively alleviates the hubness bias inherent in Euclidean embeddings"
