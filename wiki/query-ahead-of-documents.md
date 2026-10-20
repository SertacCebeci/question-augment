---
description: "With causal attention a document cannot see a query placed after it, so relevance is judged only in the short query pass; putting the query first moves the judgment into the longer document pass."
aliases: ["query-first ordering", "query ahead of documents", "reverse query placement", "query placement in RAG prompts"]
sources: ["arxiv-2601-01896"]
---
# Query ahead of documents

Most LLMs are trained auto-regressively, so a token cannot draw on anything that comes after it: "a token cannot aggregate information from any tokens that appear later in the sequence."[^c1] The paper's point is what this does to the usual RAG prompt, where the query follows the retrieved documents. "Typically, the query is positioned after the document tokens, preventing these document tokens from assessing their relevance effectively because they have no access to the query."[^c2] The relevance judgment then has to be made while the query tokens are encoded, and the paper notes that the query is "usually much shorter than the document," so the judgment is packed into the fewest tokens.[^c6]

Reversing the order changes where the judgment is made. With the query first, each document token can attend to the query while its own embedding is computed. Because the documents are the longer segment, the paper argues that "so placing the query ahead could help."[^c3] The relevance of document tokens is then computed during the document pass, which has more tokens to spread the judgment over, rather than during the query pass.

The paper reports the effect in its fine-tuning setting. Its main experiments put the query before the documents by default, and in its comparison of query placements, "after fine-tuning, placing the query ahead of documents still helps."[^c4] The claim is therefore that the ordering effect survives the paper's noise-filtering fine-tuning, not that it is a property of untuned models.

## Limits

- The paper states the ordering as a hypothesis first: "we can hypothesize that when there is noise in the document, placing the query at the beginning would help the judgment."[^c5] The main text supports it through comparisons between placements on five QA datasets; the appendix experiments on placement were not checked for this note.
- The benefit was measured with LoRA-fine-tuned 7–8B models (Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.2). Nothing here says the effect holds for larger or proprietary models, or for prompts built from many short documents.
- The argument relies on documents being much longer than the query. (My inference:) if the query were long, or the documents short, the token-count reasoning would weaken, and the paper gives no case for that regime.
- The main results also add gold documents to the context, so the comparison is between placements under a mix of relevant and noisy text, not under retrieval noise alone.
- Query-first ordering changes the prefix that every document token sees, so it is not a free change to the prompt: the document representations now depend on the query. The paper does not measure what that costs in caching or in cross-query reuse.

## Related

- [[triple-wise-relevance-judgment]] — the same pairwise limit of attention, which makes the place where relevance is computed matter.
- [[llm-judge-biases]] — position effects in judging, where the wiki notes that a causal-attention origin is suspected but not studied; here the causal-attention constraint is the mechanism the paper uses for the RAG prompt.

[^c1]: arxiv-2601-01896 — "a token cannot aggregate information from any tokens that appear later in the sequence"
[^c2]: arxiv-2601-01896 — "Typically, the query is positioned after the document tokens, preventing these document tokens from assessing their relevance effectively"
[^c3]: arxiv-2601-01896 — "so placing the query ahead could help"
[^c4]: arxiv-2601-01896 — "after fine-tuning, placing the query ahead of documents still helps"
[^c5]: arxiv-2601-01896 — "we can hypothesize that when there is noise in the document, placing the query at the beginning would help the judgment"
[^c6]: arxiv-2601-01896 — "which is usually much shorter than the document"
