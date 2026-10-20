---
description: "A cached answer is reusable only while fresh retrieval still supports it: query similarity, evidence overlap, source versions and lexical support must all hold, or the router regenerates."
aliases: ["GroundedCache", "evidence-validated cache router", "validated semantic answer cache"]
sources: ["doi-10-48550-arxiv-2605-27494"]
---
# Evidence-validated answer reuse

A semantic answer cache stores a generated answer under the query that produced it, and returns that stored answer when a new query's embedding lands close enough. The stored answer, though, is a claim about evidence. Shah (2026) puts the design question this way: "the right framing for cached answer reuse is not how to reuse faster but when reuse is safe."[^c1] The failure is concrete. A cosine-similar prior query can return a cached answer "whose underlying evidence is no longer valid, no longer the same evidence, or never supported the question in the first place."[^c2]

The proposed router, GroundedCache, serves a cached answer only when four gates hold together. (G1) Query similarity: the cosine between the new and the cached query embedding clears a threshold. (G2) Evidence overlap: the Jaccard overlap of the fresh chunk-hash signature with the cached one clears a threshold. (G3) Version match: chunks shared by the two signatures carry the same source version. (G4) Evidence support: the cached answer is scored against the freshly retrieved chunks, by default as "the fraction of content tokens in a that also appear in C", and rejected below a threshold (0.6 by default).[^c3] When any gate fails, the router compresses the fresh chunks and regenerates, so a rejected reuse costs one cache miss. The router also keeps a retrieval cache beneath the gates, which reuses the top-k set rather than the answer. That path is outside the safety count, since a retrieval-cache hit still regenerates.[^c4]

The gates do not contribute equally. In the ablation, the paper's text says "Removing G3 raises mean USR by +0.125 on HotpotQA and +0.118 on mtRAG, whereas removing G1 or G2 leaves USR within ≤ 0.001 of the full system."[^c5] This paragraph labels the lexical check G3, while the definitions and Figure 1 call it G4 and reserve G3 for version match. The paper does not reconcile the two labels; I read the ablation as the support check, since the claim is about lexical support. The authors' summary is that "that single cheap check carries essentially the entire safety gain."[^c6]

The reported numbers show what the gates cost in reuse. On HotpotQA, naive semantic caching emits unsafe answers at 15–35% across regimes, and GroundedCache drives USR "to zero on every regime that has any USR to begin with."[^c7] On the mtRAG document-drift regime, naive caching "answers from cache for 56.5% of queries with USR=51.5%", and the validator keeps the wrong-answer rate at 1.5%.[^c8] On HotpotQA document drift, GroundedCache answers from cache for 0.5% of queries, against 62.0% for naive caching. The safety is bought with hits. The latency side is modest: GroundedCache "stays within 1.04–1.07× of a no-cache RAG baseline", while the no-support variant "trades USR for 1.4–1.5× speedup."[^c9] My reading is that on this measure the gates give back most of the speed the cache could offer, and what they buy is the avoided wrong answers.

The paper treats prefix and KV reuse as a different layer: "Our framing is complementary to, rather than competitive with, prefix-level work."[^c10] The answer-level policy sits above those primitives and decides only whether an answer may be returned.

## Limits

- The workloads are synthetic. The document-drift regime "mutates numeric tokens in the gold documents so that a cached answer becomes verifiably wrong unless rejected."[^c11] The gates are therefore scored against the failure they were designed to catch. Production traffic is not sampled here.
- The generator is Qwen2.5-7B-Instruct "served by vLLM with Automatic Prefix Caching enabled" in the main runs.[^c12] The deterministic extractive backend, used for reproducible runs, "returns the sentence in the retrieved context with the highest query-token overlap."[^c13] An extractive answer is copied from evidence, so the support score is non-trivial by design. That exercises the gate but says little about answers that paraphrase the evidence.
- Lexical support cannot see referent. On mtRAG the paper notes that "lexically compatible answers can match fresh evidence tokens while pragmatically referring to a" different turn, and the residual false-hit rate there stays high "conditional on the rare answer-cache hits it serves."[^c14]
- The authors call G1 and G2 redundant on this workload, and keep them as defense-in-depth "because they fail closed at near-zero cost."[^c15] The judge-based variant of the support check is described in the method, but the defense-in-depth argument for it is argued, not measured in the parts I read.
- The authors attribute the loss of hits on HotpotQA to the version gate, because freeform answers vary lexically, and propose answer normalization before hashing. They state "We expect aHR to recover toward the naive baseline after that fix", which is an expectation the paper does not test.[^c16]
- The paper's policy reading for multi-turn traffic is that "the answer cache should largely be disabled."[^c17] This is the paper's interpretation, and the gates implement it only by suppressing hits, not by modelling the referent.

## Related

- [[unsafe-served-rate]] — the metric these results are scored in; it counts wrong reuse over all queries, not over hits.
- [[retrieval-state-drift]] — a similar failure seen on the agent side: an answer that is plausible but tied to a state that has moved.
- [[groundedness-gated-tool-routing]] — also gates an action on whether the answer is grounded, but chooses a retrieval source rather than deciding whether to reuse.

[^c1]: doi-10-48550-arxiv-2605-27494 — "the right framing for cached answer reuse is not how to reuse faster but when reuse is safe"
[^c2]: doi-10-48550-arxiv-2605-27494 — "whose underlying evidence is no longer valid, no longer the same evidence, or never supported the question in the first place"
[^c3]: doi-10-48550-arxiv-2605-27494 — "the fraction of content tokens in a that also appear in C"
[^c4]: doi-10-48550-arxiv-2605-27494 — "so by construction it cannot return a stale answer"
[^c5]: doi-10-48550-arxiv-2605-27494 — "Removing G3 raises mean USR by +0.125 on HotpotQA and +0.118 on mtRAG"
[^c6]: doi-10-48550-arxiv-2605-27494 — "that single cheap check carries essentially the entire safety"
[^c7]: doi-10-48550-arxiv-2605-27494 — "to zero on every regime that has any USR to begin with"
[^c8]: doi-10-48550-arxiv-2605-27494 — "cache for 56.5% of queries with USR=51.5%"
[^c9]: doi-10-48550-arxiv-2605-27494 — "GroundedCache stays within 1.04–1.07× of a no-cache RAG baseline"
[^c10]: doi-10-48550-arxiv-2605-27494 — "Our framing is complementary to, rather than competitive with, prefix-level work"
[^c11]: doi-10-48550-arxiv-2605-27494 — "mutates numeric tokens in the gold documents so that a cached answer becomes"
[^c12]: doi-10-48550-arxiv-2605-27494 — "served by vLLM with Automatic Prefix Caching enabled"
[^c13]: doi-10-48550-arxiv-2605-27494 — "returns the sentence in the retrieved context with the highest query-token overlap"
[^c14]: doi-10-48550-arxiv-2605-27494 — "conditional on the rare answer-cache hits it serves"
[^c15]: doi-10-48550-arxiv-2605-27494 — "because they fail closed at near-zero cost"
[^c16]: doi-10-48550-arxiv-2605-27494 — "We expect aHR to recover toward the naive baseline after that fix"
[^c17]: doi-10-48550-arxiv-2605-27494 — "the answer cache should largely be disabled"
