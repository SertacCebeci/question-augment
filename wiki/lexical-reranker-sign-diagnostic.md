---
description: "A lexical reranker hurts where a benchmark's paraphrases suppress overlap (adversarial) and helps where variation is incidental; its sign diagnoses the benchmark, not the retriever."
aliases: ["lexical control sign flip", "adversarial versus incidental surface variation"]
sources: ["doi-10-48550-arxiv-2609-01556"]
---
# Lexical reranker sign diagnostic

Applying the same cheap lexical reranker to the top candidates of an embedding retriever gave opposite effects in two benchmarks. In competition mathematics it hurt; in ALFWorld trajectories it helped, closing +25.9% [11.3, 41.2], +36.4% [23.4, 50.0] and +32.1% [18.5, 47.1] of the strict gap for three embedders, all intervals excluding zero.[^c1]

## Mechanism

The sign depends on how the benchmark's surface variation was built. In the math benchmark, equivalents are adversarially paraphrased to suppress lexical overlap while decoys preserve it, so lexical signal points the wrong way. In ALFWorld surface variation is incidental, so verb and receptacle overlap really correlates with task type.[^c2] A token-class ablation locates the effect: a verb-only variant reproduces most of the gain on the original-40 subset, a noun-only variant adds little (0 to 12.5% of gap closed).[^c3]

The authors' conclusion is that the control "costs nothing to compute" and its sign "indicates which regime a benchmark occupies before any expensive evaluation runs"; it diagnoses the benchmark rather than the retriever.[^c4] A single-benchmark claim about "semantic" retrieval that omits this axis conflates the two regimes.[^c5]

## Limits

- Only two benchmarks show the flip; treating the sign as a general diagnostic is the authors' suggestion, not a validated instrument.
- Magnitudes do not transfer: LLM-reranker effect sizes, tier profiles and even the best judge change across domains.
- The reranker is one lexical scorer; other lexical controls were not compared.
- Part of the LLM-reranking recovery in mathematics reflects memorization of well-known competitions, so reranker gains there are not pure reasoning.

## Related

- [[embedding-retrieval-literal-token-anchoring]] — the failure the control is applied to
- [[information-utility-retrieval-control]] — another control for what retrieval contributes
- [[real-query-distribution-transfer-failure]] — benchmark construction limits what a result means

[^c1]: doi-10-48550-arxiv-2609-01556 — "share of strict gap closed is +25.9% [11.3, 41.2] (Qwenemb), +36.4% [23.4, 50.0] (Gemini-emb), and"
[^c2]: doi-10-48550-arxiv-2609-01556 — "MathNet’s equivalents are adversarially paraphrased to suppress lexical overlap while its decoys"
[^c3]: doi-10-48550-arxiv-2609-01556 — "A verb-only variant, run on the original-40"
[^c4]: doi-10-48550-arxiv-2609-01556 — "and its sign indicates which regime a benchmark occupies before any expensive evaluation runs."
[^c5]: doi-10-48550-arxiv-2609-01556 — "2. The lexical control’s sign diagnoses the benchmark rather than the retriever."
