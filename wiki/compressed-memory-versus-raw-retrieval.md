---
description: "For personalizing from behavior logs, retrieving raw records beat an agentic memory that compresses them into atomic facts, and the gap narrows as models grow."
aliases: ["raw retrieval versus agentic memory", "fine-grained retrieval versus compressed memory", "RAG versus agentic memory"]
sources: ["doi-10-48550-arxiv-2608-05246", "arxiv-2601-00821", "doi-10-48550-arxiv-2608-23568", "arxiv-2512-06688", "arxiv-2511-21726"]
---
# Compressed memory versus raw retrieval

A model can be given a long behavior history in two lightweight ways. An agentic memory system such as Mem0 "first consolidates interaction histories into atomic memory facts before retrieval", so only short facts are kept and fetched.[^c1] Retrieval-augmented generation keeps the record itself: it "directly retrieves serialized behavioral logs, thereby preserving fine-grained event information."[^c2] Both avoid putting the full log in context. The question this note is about is whether the compression step costs answer quality when the models and logs are held fixed.

In LUNAR's comparison across 19 models, RAG beat agentic memory on both coverage and depth: "RAG consistently outperforms Agentic Memory on both Coverage and Depth, with an average Avg. score gap of 0.21 points."[^c3] The authors explain the gap as distortion: "direct retrieval of relevant document snippets introduces less information distortion than the compressed memory representations maintained by agentic systems."[^c4] The abstract states the same result in one line: "Direct retrieval of fine-grained behavioral records consistently outperforms compressed memory."[^c8]

The gap depends on scale. Small models lose the most under compression: Qwen3-0.6B and Qwen3-8B "suffer severe degradation under Agentic Memory, dropping 0.19–0.34 points relative to RAG."[^c5] Larger models narrow it. Kimi-K2.6 and Gemini Flash close the gap to 0.18 and 0.23 points and reach the highest absolute agentic-memory scores (2.97 and 2.90). The authors conclude that agentic memory "remains less effective than RAG in current implementations", but that "its relative viability improves with stronger base models."[^c6]

The mechanism, as I read it (my inference, not a measured result): a compressed fact fixes in advance which details survive, whereas a raw record keeps details that a later query may need and leaves the sorting to the model at answer time. A model that is weaker at rebuilding what a condensed fact left out loses more, which matches the scale pattern above. The paper does not isolate this step; it compares whole systems.

A later controlled ablation isolates it. Holding the retriever, reranker, answerer and judge fixed, and changing only the stored representation, verbatim 512-character chunks beat LLM-extracted typed artifacts: "Verbatim chunks win by 15.9 points on LoCoMo (43.9% vs. 28.0%)", and "22.0 points on LongMemEval-S" (67.4% vs. 45.4%).[^c9][^c10] The author reads the gap as loss of source text rather than the presence of structure: "accuracy tracks how much source text survives" in the store.[^c11] A dose check supports the reading. With the pipeline fixed, keeping a random fraction of each verbatim chunk's tokens lowers accuracy step by step, from 43.9% at full retention to 9.0% at 0.2, and the author reports this as "accuracy down monotonically".[^c12] The same work finds that a store which keeps the verbatim text alongside artifacts matches chunks alone, so the loss comes from replacing the text, not from adding structure to it.[^c15]

A trained compressed memory gives a different picture. In PersonaMem-v2 one 4B model writes a memory from successive history chunks and then answers from that memory alone, and the writer is rewarded when "memory turns out to be necessary and helpful in answering the final user query."[^c18] The memory is capped, "memory size Mi at 2,048 tokens to ensure compactness and efficiency,"[^c19] and the trained agentic model reaches 55.2% on multiple choice, "surpassing both the same Qwen3-4B model trained directly with long-context reasoning" and the GPT-5 series.[^c20][^c21] The task the memory must serve is the one described in [[implicit-preference-inference]]. The comparison is not raw retrieval against compression; it is a memory against a full-context model trained the same way, and the paper does not isolate which details the memory keeps. The mechanism I read into it (my inference): the writer is scored only on the later answer, so it learns in advance which details that answer will need, which is the step a fixed compressor cannot take. What this does not show is that a fixed, off-the-shelf store would do as well; the two results are about different memories.

A third arrangement moves the relevance decision wholly to query time. SUMER keeps the uncompressed conversation and trains a small agent, with reinforcement learning on a verifiable answer reward, to search it and answer: it "learns to use simple tools to search, inspect, and answer" from the raw history.[^c22] Its case against compression is the timing argument of [[write-time-relevance-commitment]]: goal-agnostic compression is applied "for a downstream query unknown at compression time", so a fixed compressor can discard what the later question needs.[^c23] On LoCoMo with Qwen2.5-7B-Instruct, the trained agent reaches judge accuracy 66.79 against 33.70 for MemMachine, and the authors describe this as "nearly doubling judge accuracy relative to the strongest compression-based baseline."[^c24][^c25] The untrained search agent over the same raw store, SUMER-Base, is the control that drops the RL step: "Even relative to our own pre-RL search baseline (SUMER-Base)," "GRPO training yields a substantial +18.24 gain in J."[^c26][^c27] By my arithmetic from these figures, the search over raw memory accounts for about 15 points over MemMachine before any RL, and RL adds the remaining 18.24. So on this benchmark a query-time search over the raw store beats compression even without training, and training widens the gap.

## Limits

- One compressed system is measured, Mem0 under the configuration in the appendix. The claim is about "current implementations", as the authors put it, not about agentic memory in general.[^c7]
- All behavior logs are synthetic, generated by the same pipeline for every model. Whether the ranking holds on real histories is not tested here.
- The headline gap is an average of 0.21 points on an LLM-judged 1–5 scale. The paper marks significance per model in its tables; it does not show that the average itself is separated from run-to-run variation on this benchmark.
- The two conditions may differ in more than compression: serialization format and the amount of text each one places in context are not varied separately in what this note has read. A raw-record advantage could partly reflect a different budget of tokens, which I cannot rule out from the text.
- The controlled ablation is a single fixed pipeline on LoCoMo and LongMemEval-S with a stateless, training-free memory. Its author states the scope: the result is "a negative result about lossy extraction, not a claim that verbatim chunks are universally optimal".[^c13] Chunks have their own weakness: they "abstain worse" on questions the store cannot answer.[^c14] The raw-versus-compressed comparison in this note therefore does not say raw storage is best at every question type. The budget question raised above has since been tested on LongMemEval in RENDER, which holds the answer contract fixed: at full length raw dialogue is the strongest baseline, but at a matched word budget a resolved packet beats recency-truncated raw dialogue, so the budget can decide the ordering in either direction.[^c16][^c17] RENDER's raw baseline is recency-truncated, so it shows that the budget matters, not that compression wins in general; see [[matched-budget-evidence-comparison]] and [[reader-facing-evidence-rendering]].
- The SUMER gain over compression mixes two changes: the raw store and a learned query-time policy. SUMER-Base keeps the raw store and drops RL, and it still beats the compression baseline; but no compressed store is run with the same trained policy, so the storage choice alone, under equal search, is not isolated (my inference from the design).
- The authors' own scope: "the LoCoMo dataset we study does not exceed the base" model's context window, so the regime where the history cannot be fed whole is not tested.[^c28] They name where compression may still help, for "distilling stable facts or schemas", and add that "while naive search alone may underperform."[^c29]
- The backbone differs from prior work: Qwen-based models stand in for GPT-4o-mini, and the authors say this "makes it difficult to directly compare our" absolute numbers with earlier reports.[^c30] The search policy is minimal by design: "the search policy we study is deliberately simple."[^c31] The result is that a simple search beats compression, not that a sophisticated search does.

## Related

- [[write-time-relevance-commitment]] — the timing argument behind the compression side of this note; SUMER gives the same reason for deferring relevance to query time.
- [[same-user-history-gating]] — the same memory-versus-raw question in coding sessions: a gate over the raw resolved history, where general memory managers (mem0, A-mem) did not reliably beat handing over the raw history.
- [[clarification-benchmarks]] — a table of benchmarks that run Full Context, Agentic Memory and RAG memory settings side by side; LUNAR's memory comparison uses that design.
- [[cross-domain-evidence-integration]] — what a retrieved record has to support once it reaches the model, when the evidence spans several domains.
- [[implicit-preference-inference]] — the task a trained memory is scored on in PersonaMem-v2; the trained-memory result is the counterpoint to the off-the-shelf comparisons above.

[^c1]: doi-10-48550-arxiv-2608-05246 — "first consolidates interaction histories into atomic memory facts before retrieval"
[^c2]: doi-10-48550-arxiv-2608-05246 — "directly retrieves serialized behavioral logs, thereby preserving fine-grained event information"
[^c3]: doi-10-48550-arxiv-2608-05246 — "RAG consistently outperforms Agentic Memory on both Coverage and Depth, with an average Avg. score gap of 0.21 points"
[^c4]: doi-10-48550-arxiv-2608-05246 — "direct retrieval of relevant document snippets introduces less information distortion than the compressed memory representations maintained by agentic systems"
[^c5]: doi-10-48550-arxiv-2608-05246 — "suffer severe degradation under Agentic Memory, dropping 0.19–0.34 points relative to RAG"
[^c6]: doi-10-48550-arxiv-2608-05246 — "its relative viability improves with stronger base models"
[^c7]: doi-10-48550-arxiv-2608-05246 — "although Agentic Memory remains less effective than RAG in current implementations"
[^c8]: doi-10-48550-arxiv-2608-05246 — "Direct retrieval of fine-grained behavioral records consistently outperforms compressed memory"
[^c9]: arxiv-2601-00821 — "Verbatim chunks win by 15.9 points on LoCoMo (43.9% vs."
[^c10]: arxiv-2601-00821 — "22.0 points on LongMemEval-S"
[^c11]: arxiv-2601-00821 — "accuracy tracks how much source text survives"
[^c12]: arxiv-2601-00821 — "accuracy down monotonically (retain 1.0→0.2:"
[^c13]: arxiv-2601-00821 — "claim that verbatim chunks are universally optimal"
[^c14]: arxiv-2601-00821 — "chunks abstain worse"
[^c15]: arxiv-2601-00821 — "should augment verbatim text rather than replace it"
[^c16]: doi-10-48550-arxiv-2608-23568 — "packets outperform recency-truncated raw"
[^c17]: doi-10-48550-arxiv-2608-23568 — "outperforms budgeted formal packets, but under"
[^c18]: arxiv-2512-06688 — "memory turns out to be necessary and helpful in answering the final user query"
[^c19]: arxiv-2512-06688 — "memory size Mi at 2,048 tokens to ensure compactness and efficiency"
[^c20]: arxiv-2512-06688 — "it reaches 55.2% accuracy on MCQ"
[^c21]: arxiv-2512-06688 — "surpassing both the same Qwen3-4B model trained directly with long-context reasoning"
[^c22]: arxiv-2511-21726 — "learns to use simple tools to search, inspect, and answer"
[^c23]: arxiv-2511-21726 — "for a downstream query unknown at compression time"
[^c24]: arxiv-2511-21726 — "nearly doubling judge accuracy relative to the strongest compression-based baseline"
[^c25]: arxiv-2511-21726 — "and J from 33.70 to 66.79"
[^c26]: arxiv-2511-21726 — "Even relative to our own pre-RL search baseline (SUMER-Base)"
[^c27]: arxiv-2511-21726 — "GRPO training yields a substantial +18.24 gain in J"
[^c28]: arxiv-2511-21726 — "the LoCoMo dataset we study does not exceed the base"
[^c29]: arxiv-2511-21726 — "while naive search alone may underperform"
[^c30]: arxiv-2511-21726 — "makes it difficult to directly compare our"
[^c31]: arxiv-2511-21726 — "the search policy we study is deliberately simple"
