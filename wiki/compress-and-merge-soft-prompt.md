---
description: "Compress each user document into a fixed-size soft prompt, then merge the set by mean pooling for a frozen LLM: cheap and order-free, good for shared style, lossy for detailed facts."
aliases: ["ComMer", "compress-and-merge", "mean-pooled document compression", "multi-document soft prompt compression"]
sources: ["doi-10-48550-arxiv-2501-03276"]
---
# Compress-and-merge soft prompt

The usual way to give a frozen LLM a user's documents is to place them in the prompt. Existing methods "rely on exposing fresh data to the model through" the prompt, a route limited by context size and costly as the prompt grows.[^c1] The compress-and-merge design keeps the model frozen and changes what is passed in. First, each document is compressed separately: "Each document is independently compressed into a soft prompt." The compressor is the same frozen LLM with trainable compression embeddings appended to the document and a trainable LoRA adapter; its output is the last-layer representation of those embeddings.[^c2] Second, the per-document compressions are merged by mean pooling, since "We use mean pool as the merge operation".[^c3] The single merged soft prompt is fed to the frozen LLM to generate the answer. Training updates only "compression embeddings and LoRA weights, while keeping" the backbone fixed.[^c4] Because the trained compressor is shared across users, "ComMer is amortized across all users, eliminating the need" for per-user training.[^c5]

The merge has three properties the authors name. The shape of the representation does not depend on how many documents there are: "The shape of the resulting representation is independent of the number of documents, addressing".[^c6] The result does not depend on order: "The process is order-agnostic, eliminating the bias".[^c7] And it updates cheaply. "When a new document is added, only that document needs to be" compressed, and the older documents are not reprocessed.[^c8][^c9]

On personalized skill learning, the tweet-paraphrasing and headline tasks from LaMP, the merged prompt does well at small budgets: "In the small token budget regime, ComMer achieves higher quality results with fewer resources than prompt-tuning".[^c10] The authors' account of why averaging keeps the signal is that one document suggests only a range of possible styles, and intersecting across documents narrows to the user's style: "potential styles across multiple documents, we can narrow".[^c11] This is also why they prefer averaging to concatenating the compressions: "the interference introduced by mean pooling is not detrimental to capturing a user".[^c12] As documents are added, perplexity "follows a power-law relation in both the personalized tweet" and headline tasks.[^c17]

On knowledge-intensive QA (a PerLTQA-derived set) the picture reverses. "a single document is the optimal scenario, as additional" documents bring irrelevant content, and "inclusion of more documents leads to worse perplexity and" ROUGE-L for ComMer.[^c13][^c14] The authors' explanation is that "Averaging the compressions can negate these particularities through destructive" interference, and they "conjecture that this qualitative difference between the" two task types reflects a wider trend.[^c15][^c16] My reading, not a result of the paper: a mean keeps what the documents share and cancels what each holds alone. That suits a style, which is shared across documents, and is harmful for a fact, which lives in one of them.

The merge also transfers across document counts. A model trained on j documents and tested on i gets better when i is larger: "ComMer improves when exposed to more documents than it was trained".[^c19]

## Limits

- One backbone is measured: "We conduct experiments using Gemma-2b".[^c20] The same weights serve as compressor and generator. Other sizes and families are not tested, so the knowledge-intensive failure may partly reflect a small compressor. The paper does not separate that.
- The metrics are noisy: "metrics exhibit significant noise, which complicates drawing coherent conclusions."[^c21] The conclusions lean on perplexity, with ROUGE-L as a noisier second check.
- The power-law in document count is an extrapolation. The datasets have "at most eight documents for most users",[^c18] so the claim that more documents will help further is untested at realistic per-user counts.
- The knowledge-intensive test rests on few personas: "27 personas are allocated to the training set", with 5 for test.[^c22]
- Pretraining gains are reported on the tweet task only. "Table 1 shows that pretraining improves downstream performance, measured by perplexity."[^c23] Other tasks were not run.
- Privacy and bias are named and left open: "In this paper we do not aim to address these challenges."[^c24] Compressing real user data raises the concern the paper flags, and nothing here addresses it.
- Query-dependent use is argued, not run. The merge is said to be "better suited for retrieval-based" use, where only relevant documents are merged per query.[^c25] The paper defers that experiment, so the claim that the merge suits per-query selection is untested.

## Related

- [[query-relative-token-overflow]] — another soft compression, of retrieved passages into single dense tokens; there the loss depends on the question, while here the compression is fixed before any question arrives.
- [[compressed-memory-versus-raw-retrieval]] — the same cost question for behavior logs, compressed into facts against raw records; the merge here is latent rather than fact-level, and it is the detail-bearing tasks that lose.
- [[situational-relevance]] — personalization where the needed fact sits in a document unrelated to the query; a query-independent merge cannot single that document out.

[^c1]: doi-10-48550-arxiv-2501-03276 — "rely on exposing fresh data to the model through"
[^c2]: doi-10-48550-arxiv-2501-03276 — "Each document is independently compressed into a soft prompt."
[^c3]: doi-10-48550-arxiv-2501-03276 — "We use mean pool as the merge operation"
[^c4]: doi-10-48550-arxiv-2501-03276 — "compression embeddings and LoRA weights, while keeping"
[^c5]: doi-10-48550-arxiv-2501-03276 — "ComMer is amortized across all users, eliminating the need"
[^c6]: doi-10-48550-arxiv-2501-03276 — "The shape of the resulting representation is independent of the number of documents, addressing"
[^c7]: doi-10-48550-arxiv-2501-03276 — "The process is order-agnostic, eliminating the bias"
[^c8]: doi-10-48550-arxiv-2501-03276 — "When a new document is added, only that document needs to be"
[^c9]: doi-10-48550-arxiv-2501-03276 — "This eliminates the need to reprocess older documents, leading"
[^c10]: doi-10-48550-arxiv-2501-03276 — "In the small token budget regime, ComMer achieves higher quality results with fewer resources than prompt-tuning"
[^c11]: doi-10-48550-arxiv-2501-03276 — "potential styles across multiple documents, we can narrow"
[^c12]: doi-10-48550-arxiv-2501-03276 — "the interference introduced by mean pooling is not detrimental to capturing a user"
[^c13]: doi-10-48550-arxiv-2501-03276 — "a single document is the optimal scenario, as additional"
[^c14]: doi-10-48550-arxiv-2501-03276 — "inclusion of more documents leads to worse perplexity and"
[^c15]: doi-10-48550-arxiv-2501-03276 — "Averaging the compressions can negate these particularities through destructive"
[^c16]: doi-10-48550-arxiv-2501-03276 — "We conjecture that this qualitative difference between the"
[^c17]: doi-10-48550-arxiv-2501-03276 — "follows a power-law relation in both the personalized tweet"
[^c18]: doi-10-48550-arxiv-2501-03276 — "contain at most eight documents for most users."
[^c19]: doi-10-48550-arxiv-2501-03276 — "ComMer improves when exposed to more documents than it was trained"
[^c20]: doi-10-48550-arxiv-2501-03276 — "We conduct experiments using Gemma-2b"
[^c21]: doi-10-48550-arxiv-2501-03276 — "metrics exhibit significant noise, which complicates drawing coherent conclusions."
[^c22]: doi-10-48550-arxiv-2501-03276 — "27 personas are allocated to the training set"
[^c23]: doi-10-48550-arxiv-2501-03276 — "Table 1 shows that pretraining improves downstream performance, measured by perplexity."
[^c24]: doi-10-48550-arxiv-2501-03276 — "In this paper we do not aim to address these challenges."
[^c25]: doi-10-48550-arxiv-2501-03276 — "vanilla ComMer is better suited for retrieval-based"
