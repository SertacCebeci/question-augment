---
description: "Cross-document evidence can be combined at decode time: one expert per cached document votes each token and the best-supported token wins, so documents never share attention during prefill."
aliases: ["parallel context-of-experts decoding", "PCED", "token-level expert switching", "decode-time evidence aggregation"]
sources: ["openalex-org-w7124227879"]
---
# Decode-time expert aggregation

Parallel KV-cache methods encode each retrieved document on its own, so the cache for a document can be computed ahead of time and reused at query time. The cost of prefilling one long prompt goes away.[^c1] The price is that the documents no longer attend to each other, and the paper reports that removing cross-document attention "can substantially degrade performance on multi-hop and reasoning-intensive queries".[^c2]

The method keeps the separate caches and moves the cross-document step into decoding. Each retrieved document becomes an expert with its own cache. One more expert, with an empty cache, serves as the model's prior, and all of them process the query in a single batched forward pass.[^c3] At each step every expert proposes a next-token distribution from its own cache. The next token is the best candidate across all experts, a maximum rather than an average. The chosen token is then appended to the history of every expert, so the next step is conditioned on the same generated text in every stream.[^c4]

Because the choice is made per token, the expert that carries the evidence can change from one step to the next. In a HotpotQA trace the model settles on an expert that holds the bridging entity and then switches to a second expert for the final answer.[^c5] No joint attention over the documents is built at any point. The paper's summary is that "much of the benefit of cross-document interaction" can be recovered at decode time.[^c8]

The reported results are on LOFT retrieval-augmented and in-context tasks, with the same pool of retrieved documents for every method. On the multi-document QA tasks, which "require aggregating evidence across multiple documents",[^c6] the parallel variant beats KV-cache merging. Its dense scoring variant beats full-context concatenation in 11 of 16 settings, "in 11/16 settings despite encoding each" document separately.[^c7] Latency is the other claim. The paper reports time to first token of "TTFT (0.14s vs. 25.50s)" at the largest retrieval depth, a gain of over 180 times.[^c9]

## Limits

- The method needs the token-level logits of every expert at every step. The paper says this restricts it to open or self-hosted models, so it does not reach "closed-source or API-only language models".[^c10]
- Evaluation covers two instruct models of 8B and 13B parameters on LOFT, and Qwen3-8B on LongBench, with greedy decoding only. "Decoding is greedy for all methods."[^c11] Sampling, longer generations and other model families are not tested in the text.
- It is not uniformly better. MapReduce stays ahead on some settings, which the paper attributes to "cases where global synthesis across many documents is beneficial".[^c12] The paper's contrast is cost: MapReduce "relies on multiple LLM calls (per-document summarization and an aggregation pass)",[^c13] while this method aggregates within one decoding procedure.
- The result depends on retrieval. An expert whose evidence is weakly retrieved "may be underweighted or never selected during" decoding.[^c14] The method "cannot recover evidence that is entirely" absent from the candidate set.[^c15]
- The aggregation rule was tuned to a case. The paper's own ablation finds that "aggregation best supports token-level expert switching in multi-hop QA", and that soft mixtures can help single-document settings.[^c17]
- The latency figures hold for "a high-throughput setup with continuous batching and PagedAttention".[^c16] Speed in a different serving setup is not measured here. Each document adds a stream to the batch, so the decode cost should grow with the number of retrieved documents (my inference; the text does not report decode throughput against N).
- Figure 2 is one trace. The text gives no rate at which expert switching helps or hurts across items (my inference).

## Related

- [[retrieval-prior-contrastive-decoding]] — the scoring rule that weights each expert's logits against the amateur and by relevance; this note is the expert layout around it
- [[null-image-logit-subtraction]] — the same subtraction against a null-input pass, in vision-language decoding; here the null is an empty document cache
- [[aggregation-extraction-gap]] — the cross-document aggregation deficit that single-pass concatenation shows; this method is one proposed route around it (my inference: that note does not test this method)
- [[context-fidelity-boosting]] — another decoding-time method that raises tokens the context supports; the mechanism is a bias, not a per-document expert

[^c1]: openalex-org-w7124227879 — "encoding retrieved documents independently and reusing their cached states at inference"
[^c2]: openalex-org-w7124227879 — "can substantially degrade performance on multi-hop and"
[^c3]: openalex-org-w7124227879 — "one amateur expert with an empty cache"
[^c4]: openalex-org-w7124227879 — "The chosen token is appended to the shared generation history for all experts at each step."
[^c5]: openalex-org-w7124227879 — "expert containing the bridging entity, then pivots to"
[^c6]: openalex-org-w7124227879 — "require aggregating evidence across multiple documents"
[^c7]: openalex-org-w7124227879 — "in 11/16 settings despite encoding each"
[^c8]: openalex-org-w7124227879 — "much of the benefit of cross-document interaction"
[^c9]: openalex-org-w7124227879 — "TTFT (0.14s vs. 25.50s)"
[^c10]: openalex-org-w7124227879 — "closed-source or API-only language models"
[^c11]: openalex-org-w7124227879 — "Decoding is greedy for all methods."
[^c12]: openalex-org-w7124227879 — "cases where global synthesis across many documents is beneficial"
[^c13]: openalex-org-w7124227879 — "on multiple LLM calls (per-document summarization and an aggregation pass)"
[^c14]: openalex-org-w7124227879 — "may be underweighted or never selected during"
[^c15]: openalex-org-w7124227879 — "it cannot recover evidence that is entirely"
[^c16]: openalex-org-w7124227879 — "All results use a high-throughput setup with continuous batching and PagedAttention"
[^c17]: openalex-org-w7124227879 — "aggregation best supports token-level expert switching in multi-hop QA"
