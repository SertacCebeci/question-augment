---
description: "With a frozen in-context predictor, active querying optimizes the labeled context, not weights; on 20 tabular tasks no acquisition rule dominates and random often ties in the 0-100 label cold start."
aliases: ["Tab-AICL", "Tabular Active In-Context Learning", "active learning with in-context predictors"]
sources: ["arxiv-2603-27385"]
---
# Active in-context learning

Classical active learning chooses which points to label by the uncertainty of a model that is retrained after each query. With very few labels that uncertainty is unreliable, so cold-start gains are small.[^c1] Active in-context learning (Tab-AICL, Treerath and Pittorino 2026) removes the retraining: the predictor (TabPFN) is fixed, and "learning proceeds by expanding the labeled context given at inference time."[^c2] What the questioner optimizes is the set of labeled examples the predictor conditions on; the questions are the queries that grow it.

## Mechanism

A pool U of unlabeled points and a small labeled set L; at each round a rule picks a batch Q, an oracle labels it, and L grows. Four rules were compared:

- Margin: query the points with the smallest gap between the top two class probabilities.[^c3]
- Coreset: greedy k-center, pick the point farthest from the labeled set in feature space (pure diversity, no model).[^c4]
- Hybrid: take the highest-entropy candidates, run k-means with k = batch size, query the point nearest each centroid (uncertainty filter, then diversity).[^c5]
- Proxy-Hybrid: a cheap logistic-regression proxy shortlists by entropy, TabPFN scores only the shortlist, then the hybrid step runs. This cuts expensive pool evaluations "by approximately a factor 1/α" (α = 0.05).[^c6]

The cost motive is concrete: in-context inference scales quadratically with context length, so scoring a whole pool with the foundation model is expensive.[^c7]

## What was measured

On 20 classification benchmarks, 10 seeds, up to 100 labels, the metric was normalized area under the learning curve (average Cohen kappa over the trajectory). TabPFN-based methods attained the best AULC on 15 of 20 datasets against retrained CatBoost and XGBoost with margin querying.[^c8] After Benjamini-Hochberg correction, TabPFN-Hybrid beat CatBoost-Margin significantly on 8/20 datasets, and CatBoost-Margin beat it on none.[^c9]

The effect of the query rule is regime dependent: "no single acquisition rule is consistently best", and "on several datasets TabPFN-Random matches or exceeds the active rules in the 0–100 label regime."[^c10] Qualitatively, margin sampling converges fast on clean, structured data; hybrid does well on clustered geometry; proxy-hybrid shows tighter variance on noisy data, which the authors read as the proxy stage reducing sensitivity to atypical points (their interpretation, not isolated by an ablation).[^c11]

## Failure modes named by the authors

Uncertainty-based selection "can over-focus on atypical or noisy points"; diversity-only selection can waste labels away from informative regions; the proxy adds a modeling assumption that may be lossy.[^c12] The very first labels are also sensitive to initialization and class imbalance.[^c12]

## Limits

- Simulated oracle with noise-free ground-truth labels; no human answerer error, cost variation, or ambiguity in the questions.
- Small-data only: bounded by the model's context window and quadratic cost; the authors suggest handing off to gradient-boosted trees as labels accumulate.[^c13]
- Pool size was capped at 10,000 and the budget at 100 labels; behavior beyond is untested.
- The explanation of why each rule wins on each data geometry is observational (learning-curve inspection), not tested causally. My inference: because random often ties, the value of a query rule here is mostly variance reduction on specific geometries, not a general gain.
- Baselines use fixed hyperparameters, so the comparison favors no tuning; tuned baselines could narrow the gap.

## Related

- [[cold-start-value-of-information]] — also about querying before the answerer model is reliable; there the response model is unknown, here the predictor's uncertainty is unstable
- [[expected-information-gain]] — the model-based uncertainty criterion that margin and entropy rules approximate
- [[generalized-binary-search]] — an alternative query-selection formalism with guarantees, which this empirical work lacks

[^c1]: arxiv-2603-27385 — "its cold-start gains are often limited because uncertainty estimates are unreliable when models are trained on very few labels"
[^c2]: arxiv-2603-27385 — "learning proceeds by expanding the labeled context given at inference time"
[^c3]: arxiv-2603-27385 — "we query the B points with smallest αmargin (x)"
[^c4]: arxiv-2603-27385 — "we pick x∗ = arg maxu∈U minl∈L"
[^c5]: arxiv-2603-27385 — "run k-means (k = B) on their preprocessed feature vectors"
[^c6]: arxiv-2603-27385 — "reducing the number of expensive TabPFN pool evaluations"
[^c7]: arxiv-2603-27385 — "TabPFN inference scales quadratically with context length"
[^c8]: arxiv-2603-27385 — "attains the best AULC on 15/20 datasets"
[^c9]: arxiv-2603-27385 — "TabPFN-Hybrid is significantly better on 8/20"
[^c10]: arxiv-2603-27385 — "no single acquisition rule is consistently best"
[^c11]: arxiv-2603-27385 — "consistent with the proxy stage reducing sensitivity to atypical points"
[^c12]: arxiv-2603-27385 — "can over-focus on atypical or noisy points"
[^c13]: arxiv-2603-27385 — "then hand off to scalable"
