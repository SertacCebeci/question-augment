---
description: "Letting an LLM judge the top-k documents and estimating RM3 expansion only from accepted ones denoises feedback, keeps terms corpus-grounded, and beats blind PRF; richer context sharpens the judge."
aliases: ["LLM-filtered RM3", "LLM-assisted pseudo-relevance feedback", "judge-then-expand"]
sources: ["arxiv-2601-11238"]
---
# LLM-filtered pseudo-relevance feedback

Pseudo-relevance feedback (PRF) assumes the top-k documents of a first retrieval pass are relevant and mines them for expansion terms. RM3 interpolates the original query model with a relevance model estimated from those documents. Its weakness is that noisy documents in the top-k cause topic drift: the expanded query no longer represents the user's intent.[^c1]

The intervention is to put an LLM judge between retrieval and estimation. The LLM gives each query-document pair a binary label, and RM3 is computed only over documents labelled relevant.[^c2] The LLM generates no text. Every expansion term therefore comes from real corpus documents, so hallucinated or collection-foreign terms cannot enter.[^c3] This differs from generative expansion, where the model's own output is the evidence. The LLM is used as a discriminator of evidence rather than a source of it.

A second variant keeps the filter and also replaces the query-likelihood factor in the relevance model with the LLM's probability of the token "true". Documents then count in proportion to the judge's confidence rather than equally.[^c4]

## What was measured

On AP88-89, ROBUST04, WT10G and DL-20, with hyperparameters tuned on separate training topics, filtering the PRF set with a fine-tuned MonoT5 judge consistently lifted AP and NDCG over plain RM3, with the largest gains on ROBUST04 and WT10G. A generic Llama 3.1-8B-Instruct judge also helped but lagged MonoT5, which the authors attribute to MonoT5 being fine-tuned for relevance.[^c5] An oracle that applies RM3 to the truly relevant documents in the top-k showed substantial headroom, so filter quality is the limiting factor.[^c6]

The judge's input matters. Adding the TREC topic narrative to the judging prompt, while RM3 still got only the title, improved the LLM-filtered variants over title-only judging on AP88-89 and ROBUST04. The authors say the title alone makes relevance ambiguous.[^c7] They also report a severe drop in the number of damaged queries, but the Robustness Index is not shown in the paper.[^c8] In effect, a better-specified question makes the judge's answers better, while the downstream estimator is unchanged.

## Limits

- Only RM3 on lexical first-stage retrieval was tested. Whether the filter helps other PRF estimators or dense retrievers is not shown.
- The 8B Llama judge is the only generic LLM; stronger or reasoning models were left to future work.[^c9]
- Narratives exist for the TREC topics but not for DL-20 and not for real user queries. The gain from richer context is shown only where an assessor-written narrative exists.
- Compute overhead of judging up to k documents is asserted to be moderate but was not analysed.[^c10]
- The Robustness Index claim is reported in prose only; I treat it as unverified.
- The tables are garbled in the text extract, so I cite only the prose summaries of the results.
- PRF parameters (k, e, lambda) were tuned per method and dataset, which may favour methods with more freedom.

## Related

- [[corpus-grounded-one-shot-query]] — also keeps the query tied to corpus evidence rather than model imagination.
- [[query-anchored-expansion-integration]] — RM3's interpolation with the original query is an instance of anchoring.
- [[reformulation-pattern-library]] — compares RM3 and Rocchio with unconstrained LLM reformulation.
- [[evidence-admission-gate]] — the same shape: a judge admits or rejects evidence before it is used.

[^c1]: arxiv-2601-11238 — "noisy documents in the top-k can casuse topic drift."
[^c2]: arxiv-2601-11238 — "For each d ∈ Dk , obtain an LLM binary judgement yd ∈ {0, 1} from the"
[^c3]: arxiv-2601-11238 — "we do not generate any text, greatly reducing the risk of hallucinations."
[^c4]: arxiv-2601-11238 — "the token probability that the LLM assigned to the"
[^c5]: arxiv-2601-11238 — "filtering the PRF set with MonoT5 consistently lifts both AP and NDCG over RM3, with the largest gains on ROBUST04"
[^c6]: arxiv-2601-11238 — "(vi) the oracle shows substantial"
[^c7]: arxiv-2601-11238 — "can make relevance ambiguous."
[^c8]: arxiv-2601-11238 — "resulted in a"
[^c9]: arxiv-2601-11238 — "We would also like to explore"
[^c10]: arxiv-2601-11238 — "may incur a moderate computational"
