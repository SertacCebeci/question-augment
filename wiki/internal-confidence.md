---
description: "A training-free query-level score: P(Yes) to a self-assessment question, read at every layer and token of one forward pass, then averaged with decay weights around a decision center."
aliases: ["Internal Confidence", "IC", "layer-token internal confidence", "P(Yes) self-assessment"]
sources: ["doi-10-48550-arxiv-2506-09669"]
---
# Internal confidence

Internal Confidence (IC) is a training-free way to compute a [[query-level-uncertainty]] score. It needs no labels and no generated answer. The starting point is a yes-or-no self-assessment, taken from the P(True) tradition: the model is asked whether it can answer the query accurately, and the probability of the token Yes is read at the last query position. The claim behind it is that the model "can internally self-assess the boundaries of their knowledge through a single forward pass over the given query"[^c1] (the paper's wording, which it presents as a simple assumption).

Reading only the final hidden state is the limit the paper sets out to remove. Its argument is that "the intermediate internal states of LLMs preserve rich knowledge and latent information".[^c2] So the same unembedding readout is applied to the hidden state at every layer and every query token, giving a grid of readings rather than one number. Aggregation is two weighted averages. First, for each token, "a weighted sum of confidence scores across layers"[^c3]; then a second weighted average across tokens. The weights decay with distance from a decision center, which the paper defines as the cell "where the model most effectively separates answerable from non-answerable"[^c4] queries.

The implementation fixes that centre at the last token and the last layer, "since we observe that the decision center tends to be located near the later layers".[^c6] The paper's own grid shows the optimum need not sit there. For Llama-8B on GSM8K, "the representation h5 yields the best AUROC"[^c5], a layer well short of the last. The top-right corner is therefore a convenient default; the decay weights are what let neighbouring layers and tokens contribute. The authors describe the averaging as "an ensemble strategy to enhance calibration and expressivity".[^c7]

On the paper's comparisons, "our proposed Internal Confidence consistently outperforms other baselines in" knowledge-boundary detection.[^c8] It is also "substantially faster than answer-level approaches".[^c9] The applications are efficient retrieval and model cascading: "for RAG and model cascading it reduces inference costs while preserving" overall performance.[^c10]

## Limits

- It needs internal states. The paper says so: the measure "relies on access to a model's internal states", which "is not feasible for fully black-box APIs".[^c11] It does not reach API-only answerers.
- The settings are fixed by hand. The paper uses fixed hyperparameters, and "this choice does not yield optimal performance in all settings".[^c12] Its additional experiments find "the optimal decision center location varies across models".[^c13]
- The prompt protocol is not uniform. "for Phi, we use two shots in the prompt"[^c14], so comparisons across model families may mix prompt formats.
- It is a baseline, not the best measure. "its performance still lags behind answer-level approaches"[^c15]. The training-free property is bought at some accuracy against answer-level methods.
- The evidence covers "Empirical studies on both factual question answering and mathematical reasoning tasks"[^c16]. Nothing is shown for open-ended or subjective queries, and the boundary label is greedy correctness (see [[query-level-uncertainty]]).

## Related

- [[query-level-uncertainty]] — the concept this score measures; its boundary is greedy correctness, a relative and single-model target.
- [[cross-layer-probe-ensemble]] — also pools a readout across layers and tokens, but there the aggregation is over fitted token-level probes; here the weights are fixed without training.
- [[pre-generation-success-probe]] — the trained counterpart: a linear probe on the same pre-generation state, fitted to pass/fail labels.
- [[abstention]] — the other use the paper names for a boundary score: withholding an answer when the query lies beyond the boundary.

[^c1]: doi-10-48550-arxiv-2506-09669 — "internally self-assess the boundaries of their knowledge through a single forward pass over the given"
[^c2]: doi-10-48550-arxiv-2506-09669 — "the intermediate internal states of LLMs preserve rich knowledge and latent information"
[^c3]: doi-10-48550-arxiv-2506-09669 — "a weighted sum of confidence scores across layers"
[^c4]: doi-10-48550-arxiv-2506-09669 — "where the model most effectively separates answerable from non-answerable"
[^c5]: doi-10-48550-arxiv-2506-09669 — "the representation h5 yields the best AUROC"
[^c6]: doi-10-48550-arxiv-2506-09669 — "since we observe that the decision center tends to be located near the later layers"
[^c7]: doi-10-48550-arxiv-2506-09669 — "which serves as an ensemble strategy to enhance calibration and expressivity"
[^c8]: doi-10-48550-arxiv-2506-09669 — "our proposed Internal Confidence consistently outperforms other baselines in"
[^c9]: doi-10-48550-arxiv-2506-09669 — "while being substantially faster than answer-level approaches"
[^c10]: doi-10-48550-arxiv-2506-09669 — "for RAG and model cascading it reduces inference costs while preserving"
[^c11]: doi-10-48550-arxiv-2506-09669 — "which is not feasible for fully black-box APIs"
[^c12]: doi-10-48550-arxiv-2506-09669 — "this choice does not yield optimal performance in all settings"
[^c13]: doi-10-48550-arxiv-2506-09669 — "the optimal decision center location varies across models"
[^c14]: doi-10-48550-arxiv-2506-09669 — "for Phi, we use two shots in the prompt"
[^c15]: doi-10-48550-arxiv-2506-09669 — "its performance still lags behind answer-level approaches"
[^c16]: doi-10-48550-arxiv-2506-09669 — "Empirical studies on both factual question answering and mathematical reasoning tasks"
