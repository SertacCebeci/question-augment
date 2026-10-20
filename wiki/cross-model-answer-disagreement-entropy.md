---
description: "Clusters answers sampled from several different LLMs to one query by meaning and computes entropy over the clusters, flagging ambiguous queries with no ground-truth label."
aliases: ["entropy induced by answer disagreement", "entropy-driven uncertainty estimation", "multi-model answer disagreement entropy"]
sources: ["yang-2026-claim"]
---
# Cross-model answer disagreement entropy

> An uncertainty signal for "does this query need clarification at all" built
> from **disagreement between different LLMs**, not resampling of one model —
> the population the [[entropy]] is taken over is what distinguishes it from
> [[semantic-entropy]].

## Definition / Mechanism

Yang, Zhao & Dou (2026), in CLAIM: given a user query
$q$, $k_1$ **different** LLMs each independently generate one candidate
direct answer, $A(q) = \{a_1,\dots,a_{k_1}\}$. The answers are projected into
a shared semantic space and clustered by similarity into $n$ clusters; the
cluster proportions $p_i = c_i/k_1$ give

$$E_1(q) = -\sum_i p_i \log p_i.$$

"Intuitively, when different models generate semantically consistent
answers, the clustering is concentrated and the entropy is low, indicating
that the query is well-specified. In contrast, when answers are divided into
multiple semantically distinct clusters and the distribution becomes more
dispersed, the entropy increases, suggesting that the query may be
ambiguous or lack critical information."[^c1]

A single global threshold $\tau = 0.45$ turns $E_1(q)$ into a binary
clarify/don't-clarify decision, $y_{ent}(q) = \mathbb{1}[E_1(q) \geq \tau]$,
tuned once across all three evaluation datasets.[^c2]

The same computation is reused after a candidate clarifying question and a
simulated answer to get $E_2$; $IG = E_1(q) - E_2(q,cq,A)$ ranks candidate
questions, and an ablation that removes IG-based ranking (keeping the same
judgement mechanism) drops CDA from 55.17 to 43.05 and CQSS from 67.38 to
52.17 on ClariLM-test — the paper's own evidence that this entropy measure,
not just the judgement it feeds, carries the selection signal.[^c3]

## Known as

| Field | Name there | Same thing? |
|---|---|---|
| LLM active clarification (CLAIM) | entropy induced by answer disagreement | exact — the paper's abstract phrase |
| LLM active clarification (CLAIM) | entropy-driven uncertainty estimation | exact — the paper's section name |
| LLM active clarification (CLAIM) | $E_1(q)$ | exact — the paper's symbol |

**Not this concept:** [[semantic-entropy]] (Kuhn 2023; Farquhar 2024)
resamples $N$ times from **one** model on a fixed question and clusters
those resamples; this measure draws **one** answer each from $k_1$
**different** models. Both compute entropy over an entailment/similarity
partition, but the population sampled — one model's own dispersion vs.
disagreement across models — is different, so a query where every model
agrees with itself but the models disagree with each other scores
oppositely under the two measures. Relation here is `close`, not `exact`.

## Why it matters

This is a query-uncertainty signal usable **before** any clarifying
question is asked or answered, with no ground-truth label and no reliance
on a single model's self-consistency — the gap CLAIM's own ablation closes
against an LLM-judgement-only baseline (74.60/53.88 accuracy/CDA vs.
79.60/55.17 for the combined signal on ClariLM-test), which the paper reads
as entropy and LLM judgement "captur[ing] complementary aspects of query
[[efe-planning-as-variational-inference|ambiguity]]."[^c4]

## Transfer

| | |
|---|---|
| **Home field** | information theory (Shannon entropy over a discrete distribution), as already imported into LLM uncertainty estimation by [[semantic-entropy]] (entropy over meaning-clusters of one model's resamples) |
| **Here** | entropy over meaning-clusters of **one answer each from several different models**, no resampling |
| **What survives** | the cluster-then-entropy computation and the low-entropy = agreement / high-entropy = disagreement reading |
| **What does not** | the same-model-resampling assumption and the confabulation-style validation against a correctness label; CLAIM validates $E_1$ only against downstream clarification-accuracy metrics, not against ground-truth ambiguity |

## Limits

- One paper, three benchmarks (ClariLM-test, IN3, CLAMBER), one base model
  family (Llama-3.1-8B) for the trained model; $k_1$ and the model pool used
  to sample $A(q)$ are not stated in the slice read here.
- $\tau = 0.45$ is a single global threshold tuned once across all three
  datasets; the paper itself notes entropy alone disagrees with the
  LLM-based judgement on a non-trivial fraction of samples (27.8–52.4%
  across the reported datasets), which is why CLAIM never uses $E_1$ alone.
- The clustering step needs a semantic-similarity model whose errors
  propagate into $E_1$, the same dependency [[semantic-entropy]] has on its
  entailment model.

## Related

[[semantic-entropy]] · [[expected-information-gain]] · [[entropy]] · [[uncertainty-driven-synthetic-clarification-training]]

[^c1]: yang-2026-claim — "Intuitively, when different models generate semantically consistent answers, the clustering is concentrated and the entropy is low, indicating that the query is well-specified. In contrast, when answers are divided into multiple semantically distinct clusters and the distribution becomes more dispersed, the entropy increases, suggesting that the query may be ambiguous or lack critical information."
[^c2]: yang-2026-claim — "We use a single global threshold 𝜏 = 0.45 for all datasets and discuss its rationale in Appendix A."
[^c3]: yang-2026-claim
[^c4]: yang-2026-claim — "This gap indicates that entropy-based uncertainty estimation and LLM-based semantic judgement capture complementary aspects of query ambiguity, and that relying on either signal alone is insufficient for robust clarification decisions."
