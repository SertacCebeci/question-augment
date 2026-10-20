---
description: "In federated active learning, which model picks the queries matters less than which one samples minority classes more evenly; global wins only when imbalance is severe and clients are alike."
aliases: ["query-model selection in federated active learning", "FairFAL adaptive model selection", "global vs local query model"]
sources: ["arxiv-2603-10341"]
---
# Class-balanced query-model selection

In federated active learning (FAL) two models can choose what to label: the aggregated global model and each client's own local model. The study behind FairFAL found that the right choice is decided by one quantity: how class-balanced the queried set is, above all for rare classes.[^c1]

## What was found

Three empirical observations drive the design.

1. For uncertainty-based querying the local model usually beats the global one. The exception is severe global class imbalance with relatively homogeneous clients, where the global model is better.[^c2] When the global distribution is balanced and clients are very heterogeneous, the union of client-specific queries is already globally balanced, so local querying suffices.[^c3]
2. The advantage of one model over the other tracks which one acquires more minority-class samples, and that tracks final accuracy. Under severe imbalance the gap in minority samples and the accuracy gap grow and stabilise together. Under a balanced global distribution minority counts are similar for both models, yet the local model still wins because its queried set is more balanced across the whole label space.[^c4]
3. For diversity-based sampling the global model consistently beats the local one, because aggregated updates give it more globally aligned embeddings.[^c5]

## How the selection is made operational

Each client upsamples its first-round (random, hence roughly IID) labeled set to a class-balanced subset and averages the global model's predictions on it. The ratio of the smallest to the largest predicted prior is a per-client imbalance coefficient. Only this scalar is uploaded, and the server averages it once and keeps it fixed.[^c6] Each round the client also computes a normalised divergence between global and local predictive priors.[^c7] A score s_k = 1 - (d_k + γ̄)/2 is high when the global distribution is skewed and the client resembles it. The global model queries when s_k exceeds a fixed threshold of 0.75, otherwise the local model does.[^c8]

Two companion steps push balance further. Pseudo-labels for the unlabeled pool come from cosine similarity to class prototypes built on global-model features, instead of from a classifier biased toward head classes.[^c9] Then high-uncertainty samples are pooled per pseudo-class, and k-center selection in a gradient-embedding space removes near-duplicates.[^c10]

The abstract reports that FairFAL beats state-of-the-art FAL baselines on five benchmarks under long-tailed, non-IID settings.[^c1]

## Limits

- The three observations come from the authors' own sweeps over a heterogeneity parameter α and an imbalance ratio ρ on image benchmarks. The note's reading that "balance of the queried set causes accuracy" is correlational in the paper's own evidence (alignment of curves), not an intervention.
- The threshold δ = 0.75 and the linear score are heuristics, and I did not check their sensitivity.
- The imbalance estimate assumes the first-round labeled set is a random sample, and it is never refreshed.
- Nothing here tests language-model questioning. Carrying the idea over to deciding who or what should ask is my inference, not a result.

## Related

- [[mondrian-conformal-prediction]] — also treats the minority class as the place where a pooled method fails
- [[atom-stratified-federated-conformal-calibration]] — another federated setting where heterogeneity across clients must be handled per stratum
- [[active-testing]] — chooses which items to label under a budget

[^c1]: arxiv-2603-10341 — "the model that achieves more classbalanced sampling, especially for minority classes, consistently leads to better final performance."
[^c2]: arxiv-2603-10341 — "For uncertainty-based sampling, the local model generally outperforms the global model, except in cases where global class imbalance is severe while client distributions remain relatively homogeneous."
[^c3]: arxiv-2603-10341 — "the aggregation of diverse client-specific queries naturally produces a globally balanced query set."
[^c4]: arxiv-2603-10341 — "models that acquire more minority-class instances invariably achieve higher performance."
[^c5]: arxiv-2603-10341 — "For diversity-based sampling, the global model consistently outperforms the local model."
[^c6]: arxiv-2603-10341 — "each client uploads only the scalar γk to the server."
[^c7]: arxiv-2603-10341 — "dk is recomputed at every AL round"
[^c8]: arxiv-2603-10341 — "where δ is a fixed threshold (set to 0.75)."
[^c9]: arxiv-2603-10341 — "we replace direct classifier predictions with a prototype-based assignment"
[^c10]: arxiv-2603-10341 — "then perform k-center sampling in a gradient-embedding space to obtain the final, diverse query set."
