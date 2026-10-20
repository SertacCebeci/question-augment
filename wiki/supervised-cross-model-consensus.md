---
description: "A supervised meta-learner over agreement features of several LLMs' answers beat the best model and majority vote, by learning when a small coherent minority cluster is the correct one."
aliases: ["multi-model consensus reasoning engine", "learned LLM consensus", "graph-attention consensus over answers"]
sources: ["arxiv-2601-07245"]
---
# Supervised cross-model consensus

Majority vote treats agreement as truth. Kallem (2026) instead trains an ordinary model (gradient-boosted trees, a listwise ranker, or a graph attention network, GAT) to predict which of several heterogeneous LLMs' answers is correct. Its inputs are features of the answer set: embedding similarity, cluster structure, lexical overlap, reasoning-quality scores, confidence, and per-model priors. The base LLMs are not updated. The learner is deliberately not another LLM judge (see [[llm-judge-biases]]).

## What was measured

Three open-weight models (Llama-3-8B, Mistral-7B, Qwen2-7B) were run on small subsets of GSM8K, ARC-Challenge, HellaSwag and TruthfulQA. Macro-averaged accuracy was: "achieves 55.6% accuracy, majority voting 52.2%, and selfconsistency 54.6%" for the best single model, majority vote and self-consistency.[^c1] The best consensus model (GAT) reached 60.3%, "a 4.6 point gain over the best single model and"[^c2] 8.1 points over majority vote.

Feature ablation with the tree model gave the main mechanism claim. Removing similarity and clustering features cost the most: "largest drop in accuracy (5.1 points), confirming that agreement in embedding space and cluster structure are central"[^c3]. Dropping confidence and model priors cost 3.8 points, reasoning-quality scores 2.1, lexical features 1.4 (Table II).

## Why a learned rule can beat a vote

The paper's explanation is that agreement is informative but neither necessary nor sufficient. Models with similar training data can share a falsehood (TruthfulQA myths). Correct answers may come from only a subset of models. A learned function can therefore trust uniform agreement in easy domains and a high-quality minority in hard ones.[^c4] On hard, high-disagreement items the GAT attends to tightly connected subgraphs, so it "amplifies minority-but-correct opinions."[^c5] When models mostly agree (easy HellaSwag) the similarity graph is nearly complete, graph propagation adds little and the tree model nearly matches it.[^c6]

On TruthfulQA items with a plausible false option and an "I don't know" option, the false option was chosen by majority vote on 36.4% of questions and by the best single model on 33.7%. The consensus GAT chose it on 26.1%.[^c7] The authors also report better calibration: the best model's 0.8 to 0.9 confidence bin was right about 65% of the time, and the consensus's same bin about 78%, with Brier score about 10% better in relative terms.

The authors say heterogeneity is a precondition: "If all models were nearly identical, multimodel consensus would offer little beyond self-consistency."[^c8] This links to the independence problem in [[effective-independent-votes]].

## Limits

- Tiny scale: three 7-8B models, compact benchmark subsets, a few thousand labelled examples. Gains of a few points may not carry to stronger or closed models.
- It needs ground-truth labels and may fail where agreement patterns differ from training: "may degrade on out-of-distribution tasks where patterns of"[^c9] agreement differ. The learned weights are tied to the specific model set and must be retrained when models change.
- Shared bias is not fixed: "consensus may amplify rather than mitigate them."[^c10]
- It roughly triples inference cost. The paper does not test cost-aware querying.
- The paper's account of why the GAT works (minority clusters, structured disagreement) is interpretation from ablations and three case studies, not an isolated test. The reasoning-quality scores that help here are themselves model-derived, and the paper does not say how independent they are of the answerers.
- It was not compared against LLM-judge selection or verifier-based voting on the same data.

## Related

- [[verification-weighted-voting]] — also escapes a wrong majority, using external tool checks instead of learned features
- [[surprisingly-popular-algorithm]] — another rule that trusts a minority over the popular answer
- [[effective-independent-votes]] — correlated models give fewer independent votes, the reason diversity matters here
- [[llm-judge-biases]] — the alternative this design avoids
- [[vote-margin-gate]] — a simple agreement-based gate that this learned rule generalizes

[^c1]: arxiv-2601-07245 — "achieves 55.6% accuracy, majority voting 52.2%, and selfconsistency 54.6%."
[^c2]: arxiv-2601-07245 — "a 4.6 point gain over the best single model and"
[^c3]: arxiv-2601-07245 — "largest drop in accuracy (5.1 points), confirming that agreement in embedding space and cluster structure are central"
[^c4]: arxiv-2601-07245 — "First, agreement carries signal, but it is neither necessary"
[^c5]: arxiv-2601-07245 — "amplifies minority-but-correct opinions."
[^c6]: arxiv-2601-07245 — "such as GBDT achieve performance close to GNNs."
[^c7]: arxiv-2601-07245 — "36.4% of such questions, the best single model in 33.7%, and"
[^c8]: arxiv-2601-07245 — "If all models were nearly identical, multimodel consensus would offer little beyond self-consistency."
[^c9]: arxiv-2601-07245 — "may degrade on out-of-distribution tasks where patterns of"
[^c10]: arxiv-2601-07245 — "consensus may amplify rather than mitigate them."
