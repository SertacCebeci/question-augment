---
description: "Benign-looking subqueries split across sessions reveal a hidden goal only if retrieval clusters them by shared goal, not by topical similarity; a 22M contrastive encoder does this."
aliases: ["intent-aligned retrieval", "retrieve-then-classify", "cross-session decomposition attack defense", "latent-objective matching"]
sources: ["doi-10-48550-arxiv-2608-27945"]
---
# Intent-aligned cross-session retrieval

A question's intent can be invisible in the question itself. In a cross-session decomposition attack, an asker splits one hidden objective into subquestions that each look benign, poses them in disconnected interactions, and recomposes the answers outside the model.[^c1] So the problem is to recover which disconnected queries express parts of the same hidden objective, not only to classify an isolated query.[^c2]

## Why topical similarity fails

The paper's example is a hidden intent of selling fake concert tickets. Its subqueries concern ticket security features, home image printing, online-listing photos and resale marketplaces. These are semantically different, yet they jointly support one task.[^c3] Off-the-shelf embedding models are trained for semantic similarity, generic retrieval, clustering or reranking, so they do not target this latent-objective matching.[^c4] The authors' own benign analogy is a robotics project split into battery chemistry, motor torque and sensor calibration questions. These are not paraphrases, but the answers compose into one task.[^c5]

## The mechanism

The defense keeps a bank of historical queries. A new query is embedded and its top-K nearest cross-session neighbours are retrieved by cosine similarity. A frozen guardrail LLM then classifies the query together with those neighbours, inferring the most likely underlying task, instead of classifying the query alone.[^c6]

The encoder is a MiniLM fine-tuned with an all-directions contrastive loss. Each batch takes two decomposed queries from the same latent intent as positives and treats other intents in the batch as negatives. This clusters same-intent subqueries rather than surface-similar phrasings.[^c7]

## What was measured

Evaluation is leave-one-out. Each query is a probe, it is removed from the bank, and a retrieved neighbour counts as correct only if it comes from the same latent intent. The metric therefore measures intent recovery rather than ordinary semantic similarity.[^c8] On paraphrase-shifted queries, the tuned encoder raised Recall@10 from .588 to .649 over Qwen3-Embedding-0.6B, a larger embedding model.[^c9] The abstract also reports the best learned-retriever harmful recall across all tested guardrails.[^c10]

## Limits

- The authors say the experiments show decomposition can occur in the studied pipelines, but do not establish its prevalence in deployment.[^c11]
- Deployment needs retained, searchable cross-session histories, which raises privacy and consent problems. Fragmented identities across accounts leave coverage gaps.[^c12]
- Attackers could evade retrieval by spreading fragments across accounts or adding unrelated queries. The authors call it a monitoring and triage algorithm, not a deployable end-to-end defense.[^c12]
- Labels come from curated decomposition data. In deployment, labels would have to come from prior moderation or human review.[^c13]
- My inference, not the paper's: the same retrieval problem arises for benign answering. A system that wants a user's real goal across sessions faces the same gap between topical and goal-level similarity, but this was not tested here.

## Related

- [[history-conditioned-intent-reconstruction]] — reconstructs intent from visible history; this note covers history that is fragmented across sessions
- [[session-persistent-preference-state]] — carries state across sessions, the same substrate a cross-session monitor needs

[^c1]: doi-10-48550-arxiv-2608-27945 — "benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective"
[^c2]: doi-10-48550-arxiv-2608-27945 — "to recover which disconnected queries express parts of the same hidden objective"
[^c3]: doi-10-48550-arxiv-2608-27945 — "are semantically different, but may jointly"
[^c4]: doi-10-48550-arxiv-2608-27945 — "Standard embedding benchmarks do"
[^c5]: doi-10-48550-arxiv-2608-27945 — "Those queries are not paraphrases, but"
[^c6]: doi-10-48550-arxiv-2608-27945 — "retrieve an intent neighborhood, then classify the"
[^c7]: doi-10-48550-arxiv-2608-27945 — "so the retriever is trained to cluster"
[^c8]: doi-10-48550-arxiv-2608-27945 — "Thus the retrieval metric measures intent recovery rather than ordinary"
[^c9]: doi-10-48550-arxiv-2608-27945 — "it raises Recall@10 from .588"
[^c10]: doi-10-48550-arxiv-2608-27945 — "yields the best learnedretriever harmful recall across tested guardrails"
[^c11]: doi-10-48550-arxiv-2608-27945 — "do not establish its prevalence in deployment"
[^c12]: doi-10-48550-arxiv-2608-27945 — "We therefore present the method as a monitoring and triage algorithm, not a deployable end-to-end defense."
[^c13]: doi-10-48550-arxiv-2608-27945 — "would have to"
