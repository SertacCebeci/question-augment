---
description: "A query is a cloud of embeddings sampled from a conditional generative model, not one point; retrieval by nearness to any sample covers multi-concept queries, at the cost of extra samples."
aliases: ["generative vector search", "stochastic latent matching", "sampled query embeddings", "STHLM"]
sources: ["arxiv-2512-19360"]
---
# Distributional query embedding

In conventional vector retrieval a query is encoded as one point, and documents are ranked by proximity to it. The alternative keeps the query as a distribution. A conditional generative model takes a query embedding and maps random Gaussian noise to several embeddings that represent the semantic spread of that query. Ekvall et al. call this Stochastic Latent Matching: "STHLM trains a conditional flow-matching model (although any generative" model would work) on top of a base encoder.[^c1]

The point of the distribution is coverage. Conventional methods "produce a single embedding", while STHLM "models the full conditional distribution, capturing the" multimodal nature of a query such as "tissue showing inflammation and necrosis."[^c2] A single point for a multi-concept query can sit in an empty region between its concepts, so it is closer to irrelevant documents than to the relevant ones; the paper's argument is that "a single point estimate may lie closer to irrelevant" documents than to "the diverse set of relevant ones."[^c3] Drawing N samples and retrieving by nearness to any of them lets one query reach several concept regions at once.

The sample count is the test-time knob. Each draw is an independent integration of the learned velocity field from noise, and the paper notes that "increasing sample counts (N) requires no additional time since samples are generated in" parallel.[^c4] Latency is therefore traded against recall through N, which the abstract phrases as boosting retrieval "by 10-30% through test-time compute (trading latency for accuracy)".[^c5] The paper's comparison is one point on that curve: "approximately 20% more inference compute to NV-Embed-v2, STHLM boosted its retrieval" by an amount comparable to the gain NV-Embed-v2 gives over a much smaller encoder.[^c6]

The same mechanism is offered as a fix for capacity. In a supplementary toy on histology images, forcing classes into low dimension makes "embeddings from different classes begin to overlap, making retrieval difficult", and the authors report that "a generative approach that samples multiple embeddings per query maintains better" separation.[^c7] The abstract pairs this with dimension reduction: the text-retrieval model was trained on PCA-reduced 384-dimensional NV-Embed-v2 embeddings, and the paper claims "up to a 10-fold compression of embedding dimensions."[^c8]

Where no condition exists, the same family is used differently. For unconditional local sampling, "an existing embedding is perturbed with noise at a given time point t, and then" denoised, so samples land near the original point rather than spanning a query's concepts.[^c9] The mechanism is then a neighbourhood sampler, not a multi-concept query.

## Limits

- The text benchmarks are three: "We evaluated STHLM on three distinct text benchmarks relevant for biomedical RAG."[^c10] The pathology results are classification and retrieval over pathology datasets. Nothing here tests general-domain retrieval, and the paper's claim that the mechanism is general rests on the design, not on a second domain.
- The gains depend on settings tuned per task. Classifier-free guidance was 1.0 in most benchmarks, but "except for the benchmark shown in Fig. 2a, where we used a scaling factor of 0.3."[^c11] The supplement reads low guidance as more diversity and high guidance as fidelity: "excessive class fidelity comes at the cost of diversity."[^c12] The Euler step count shows the same trade: "Results show lower step counts yield better performance with fewer" samples, and higher counts win only as N grows.[^c13]
- The baseline is not augmented the same way. The STHLM training used "synthetic queries for each corpus text with ChatGPT-4o-mini."[^c14] Part of the gain may come from extra query supervision rather than from the distribution itself. The paper does not isolate this.
- The toy and the 3D visualisations show coverage, but no per-sample coverage measure is reported. Whether samples cover the relevant documents or merely spread out is my inference from the aggregate NDCG and accuracy numbers.
- The authors state a conflict: "The authors have a patent application related to Generative Vector Search."[^c15] The benchmarks are reported by the authors, with no independent replication in this text.
- A formalism imported from image generation. What survives the transfer is the idea of sampling a set of answers from a conditional distribution and aggregating retrieval over them. What does not obviously survive is the flow-matching training itself, which was tuned on biomedical data. That transfer to other text domains is untested here.

## Related

- [[embedding-retrieval-literal-token-anchoring]] — embedding retrievers can rank by literal tokens even when the answer is retrievable; a point estimate and a sampled cloud both inherit the encoder's surface bias, which sampling does not remove (my inference).
- [[dispersed-evidence-retrieval-collapse]] — scattered evidence defeats retrieval; a sampled query is one proposed remedy for multi-concept queries, though this paper tests single-document relevance, not dispersed evidence.
- [[semantic-entropy]] — also estimates a property from many sampled outputs at test time; the sampling-based uncertainty there is a signal, here it is the retrieval query itself.

[^c1]: arxiv-2512-19360 — "STHLM trains a conditional flow-matching model (although any generative"
[^c2]: arxiv-2512-19360 — "STHLM models the full conditional distribution, capturing the"
[^c3]: arxiv-2512-19360 — "where a single point estimate may lie closer to irrelevant"
[^c4]: arxiv-2512-19360 — "increasing sample counts (N) requires no additional time since samples are generated in"
[^c5]: arxiv-2512-19360 — "boosting retrieval performance by 10-30% through test-time compute (trading latency for accuracy)"
[^c6]: arxiv-2512-19360 — "approximately 20% more inference compute to NV-Embed-v2, STHLM boosted its retrieval"
[^c7]: arxiv-2512-19360 — "embeddings from different classes begin to overlap, making retrieval difficult"
[^c8]: arxiv-2512-19360 — "while enabling up to a 10-fold compression of embedding dimensions."
[^c9]: arxiv-2512-19360 — "an existing embedding is perturbed with noise at a given time point t, and then"
[^c10]: arxiv-2512-19360 — "We evaluated STHLM on three distinct text benchmarks relevant for biomedical RAG."
[^c11]: arxiv-2512-19360 — "except for the benchmark shown in Fig. 2a, where we used a scaling factor of 0.3."
[^c12]: arxiv-2512-19360 — "excessive class fidelity comes at the cost of diversity."
[^c13]: arxiv-2512-19360 — "Results show lower step counts yield better performance with fewer"
[^c14]: arxiv-2512-19360 — "synthetic queries for each corpus text with ChatGPT-4o-mini."
[^c15]: arxiv-2512-19360 — "The authors have a patent application related to Generative Vector Search."
