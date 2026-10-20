---
description: "Which prompt makes the best LLM pseudo-document depends on query length: one-to-two-word queries do best with zero-shot, longer natural questions with few-shot; elaborate prompts add drift."
aliases: ["prompt choice by query length", "zero-shot vs few-shot query expansion", "generative query expansion prompting"]
sources: ["doi-10-48550-arxiv-2511-19325"]
---
# Query-length-dependent expansion prompting

Generative query expansion asks an LLM to write a pseudo-document from the query and retrieves with it. The paper compares zero-shot, few-shot, chain-of-thought (CoT) and rephrase-and-respond (RaR) prompts on two cross-lingual datasets that differ mainly in query length. It finds that the best prompt flips with the query.[^c1]

## Mechanism

In CLIRMatrix the queries are Wikipedia titles, "typically one or two words", and the documents are long. In mMARCO the queries are longer, human-written questions and the passages are short.[^c2] On the short queries, zero-shot prompting beat the other methods in most configurations. The authors' explanation: with so little input, any term that is not directly relevant can "substantially degrade retrieval". CoT and RaR often emit meta text such as "To answer this query, I will provide information about...", which hurts BM25. Few-shot prompting lets the model blend the examples' content into the target, which the authors call concept drift.[^c3]

On the longer mMARCO queries the order reversed: few-shot was most effective.[^c4] The authors conclude that "optimal prompt design must be tailored to the length and structure of the input query."[^c5]

The second effect is how the pseudo-document is used. On mMARCO, the largest gains came from concatenating the original query with the pseudo-document, rather than retrieving with the pseudo-document alone. On CLIRMatrix this added little, because a one- or two-word query is almost always already contained in the pseudo-document.[^c6] Expanding before translation and then concatenating was generally better than the original query on both sets. Gains were up to about 15% on CLIRMatrix and 10% on mMARCO, and the differences between techniques were smaller than that.[^c7] The abstract states the summary claim: more elaborate prompts "often do not yield further gains".[^c8]

## Limits

- Detailed prompt-by-query-length results are from one model (Aya Expanse 8B) in the body; the Gemma 3 results are in appendices I did not read.
- Query length is confounded with dataset: format, source, document length and relevance judgements all differ. The authors call length only a "plausible explanation". The causal story about drift and meta text rests on qualitative inspection, not an ablation.
- The mechanism is argued for sparse (BM25) retrieval; I did not read the dense-retrieval comparison closely.
- Cross-lingual setting only; whether the same flip holds monolingually is not tested here.
- I did not read the fine-tuning or script-disparity sections, so those claims are not carried here.

## Related

- [[query-anchored-expansion-integration]] — also finds that how the expansion is combined with the query matters; here concatenation, there vector interpolation.
- [[cross-retriever-reformulation-gain]] — expansion gain depends on the retriever, as it does here on query length.
- [[corpus-grounded-one-shot-query]] — another way of controlling what generated text enters the query.

[^c1]: doi-10-48550-arxiv-2511-19325 — "Results show that query length"
[^c2]: doi-10-48550-arxiv-2511-19325 — "typically one or two words, while the associated documents are comparatively long"
[^c3]: doi-10-48550-arxiv-2511-19325 — "To answer this query, I will provide information about"
[^c4]: doi-10-48550-arxiv-2511-19325 — "whereas few-shot prompting is most"
[^c5]: doi-10-48550-arxiv-2511-19325 — "optimal prompt design must be"
[^c6]: doi-10-48550-arxiv-2511-19325 — "so explicitly appending the query contributes"
[^c7]: doi-10-48550-arxiv-2511-19325 — "Cross-lingual query expansion yields gains of up to approximately 15% on CLIRMatrix and 10% on mMARCO"
[^c8]: doi-10-48550-arxiv-2511-19325 — "not yield further gains"
