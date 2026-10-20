---
description: "Single-generation uncertainty: sum next-token probability over tokens in the same offline embedding cluster or prefix-matched to the output, giving semantic scores without sampling or NLI."
aliases: ["STC", "clustered token probability", "cluster-aggregated token probability"]
sources: ["arxiv-2603-20161"]
---
# Semantic token clustering

Sampling-based uncertainty such as [[semantic-entropy]] groups whole answers by meaning, which needs many generations and an entailment model. Semantic token clustering (STC) moves the grouping to the token level. At each decoding step the probability of the chosen token understates confidence when mass is split across equivalent tokens (for example "TV" and "television").[^c1] STC therefore replaces the chosen token's probability with the mass of its whole semantic set.

## Mechanism

Two parts build the set of tokens treated as "the same as what was generated".

1. Offline: token embeddings (input and output embeddings, concatenated) are clustered once per model with agglomerative clustering, so that inference needs no extra model.[^c2] The clustering is done in pre-computation, so the clusters can be used at inference without additional computational overhead.[^c3]
2. Online: a prefix-matching set. A candidate token counts if it is a prefix of the text that follows, after case- and space-normalization. "television", "tele" and "televis" all match whether the output tokenizes as one token or as "tele"+"vision".[^c4] This repairs tokenizations that split a word into pieces carrying little meaning alone.

The step probability is the sum of p(t | context) over the union of the two sets, and these clustered masses are aggregated across the decoding steps into the response score.[^c5] Only one generation is scored.

## What was measured

On TriviaQA, Natural Questions and WebQuestions with Llama-2-7B, Llama-3-8B, Mistral-7B and Qwen2.5 (3B, 7B, 14B), the authors report performance comparable to state-of-the-art baselines. Against the NLI-based single-sample method CCP, the reported saving is "competitive performance while reducing inferencetime overhead by an average of 98%."[^c6]

Ablation: the two parts are complementary. Embedding clustering captures semantic similarity and prefix matching captures surface-form consistency. Removing either gives moderate degradation, and removing both reduces the method to the probability of the generated response and costs substantially more.[^c7]

## Limits

- Needs token logits and embeddings, so it does not apply to closed-source models.[^c8]
- Static embeddings are context-free, so polysemous tokens can land in one cluster; the authors argue low probabilities on incompatible meanings partly mitigate this, but did not test contextual embeddings.[^c9]
- Calibration is not addressed; the authors say it could be post-calibrated.[^c10]
- Evaluated on short-form factual QA; "comparable" to baselines is not "better", and the note's reading that it fails on long-form or reasoning outputs is my inference, untested here.
- It inherits the failure that token mass cannot see a confidently wrong model (my inference).

## Related

- [[semantic-entropy]] — the sampling-plus-NLI approach STC approximates from one pass
- [[uncertainty-hallucination-relevance-gap]] — compares single-pass scores such as CCP with others
- [[confidently-wrong-low-entropy-regime]] — a regime where any probability-mass score is blind
- [[logit-magnitude]] — another logit-based uncertainty signal

[^c1]: arxiv-2603-20161 — "of a single token may underestimate the model’s"
[^c2]: arxiv-2603-20161 — "we group tokens into semantically consistent clusters based on their embeddings using an unsupervised clustering algorithm, such as Agglomerative Clustering (Müllner, 2011) (implementation"
[^c3]: arxiv-2603-20161 — "clusters to be directly used during inference without introducing additional computational overhead."
[^c4]: arxiv-2603-20161 — "check whether a candidate token serves as a prefix"
[^c5]: arxiv-2603-20161 — "At each decoding step, the clustered probability"
[^c6]: arxiv-2603-20161 — "competitive performance while reducing inferencetime overhead by an average of 98%."
[^c7]: arxiv-2603-20161 — "When both components are removed, the method reduces to computing the probability of the generated response,"
[^c8]: arxiv-2603-20161 — "First, the proposed method requires access to token logits and token embeddings, which are typically unavailable in closed-source models."
[^c9]: arxiv-2603-20161 — "derived from the LLM’s vocabulary. Although"
[^c10]: arxiv-2603-20161 — "the proposed method does not explicitly address"
