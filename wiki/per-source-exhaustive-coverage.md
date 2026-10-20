---
description: "Giving each document its own retrieval loop, rather than one top-K pass over a pooled index, raised the LOONG average score from 33.0 to 58.1 in one measured setup."
aliases: ["sub-agent per document", "document-axis decomposition", "per-document retrieval coverage", "exhaustive per-document retrieval"]
sources: ["doi-10-48550-arxiv-2603-08329"]
---
# Per-source exhaustive coverage

A single top-K pass over a pooled index has a fixed reach. Standard RAG pulls a fixed set of results into one context, and "evidence beyond the top-K results is typically discarded in a single retrieval pass."[^c1]

The alternative makes coverage a property of the plan rather than of the ranking. In SPD-RAG a coordinator decomposes the query "into a Shared Instruction Set for Documents and Synthesis Directives."[^c2] Each document then gets its own sub-agent, and "the assigned sub-agent is strictly constrained to search tool calls within" that document, so chunks from other documents cannot crowd out its results.[^c3] Each sub-agent runs an iterative retrieve-and-reason loop and returns a findings report; a synthesis layer merges the reports. The partition is by source, and the loop is per source.

The measured gain is large. On LOONG, "SPD-RAG achieves an Avg Score of 58.1, substantially outperforming both Normal RAG (33.0)" and Agentic RAG (32.8).[^c4] The authors read the perfect-rate figure the same way: exhaustive per-document processing "more frequently captures the complete set of required facts."[^c5]

The contrast that carries the claim is between two iterative loops, not between iterative and one-shot retrieval. The single-agent Agentic RAG baseline spends more tokens than Normal RAG and "does not yield score improvements."[^c6] The authors' reading is that "uninstructed iterative retrieval without per-document specialization does not effectively address the coverage challenge in exhaustive multi-document settings."[^c7] More steps over one pool did not buy coverage; the paper attributes the gain to giving each source its own loop.

The effect is sharpest where evidence is spread. On academic-paper instances both RAG baselines score 0% on the perfect rate, and the authors note that "Academic papers in Loong often require synthesizing facts spread across abstracts, methods, results,"[^c8] and that the recovery "demonstrates the practical value of per-document specialization."[^c9] On financial reports, which are shorter and more structured, the gap to full context is smaller: "the gap between SPD-RAG (56.9) and" the full-context baseline (61.0).[^c10] Where one salient fact is enough, the advantage is absent: for Spotlight Locating "all RAGbased systems perform reasonably well."[^c16]

Cost is the other side of the trade. SPD-RAG "reaches 85.4% of this performance while consuming only 37.9% of the API cost" of the full-context baseline.[^c11]

What transfers, in my reading and not as a result of the paper: a fixed-K ranking sets a coverage floor. When an answer needs one fact from each of many sources, a rule that reads per source can reach facts a pooled rule ranks below K, whatever the reader does afterwards. This is the same family as [[late-fusion-evidence-partitions]], with the cut made by document rather than by run. What does not transfer with the number: the coordinator, the particular models, and the 37.9% cost ratio, which belongs to one price set.

## Limits

- No arm isolates the partition. SPD-RAG differs from its baselines in retrieval scope, loop structure, coordinator and merge at once, so the gain belongs to the whole arrangement. It cannot be assigned to per-document coverage alone.
- The coordinator bounds what each sub-agent extracts. The paper reports that "under-specified tasks lead to incomplete document-level extractions," seen on the technical academic-paper instances.[^c12] A per-document loop inherits any gap in the decomposition.
- The recursive map-reduce merge never ran: "this recursive path was never activated," since a 1M-token model took all sub-agent summaries in one step.[^c13] For hundreds or thousands of documents the authors say the scalability properties "remain empirically unvalidated."[^c14] Claims about large corpora are design claims here.
- One benchmark and two domains. The paper says legal, medical or enterprise corpora "may have different structural characteristics that alter relative performance."[^c15]

## Related

- [[late-fusion-evidence-partitions]] — the same late merge of partitioned evidence, with the cut made by run rather than by document.
- [[domain-partitioned-retrieval]] — partitions the corpus by domain and routes with a classifier; this note partitions by document, with one loop per document and no router.
- [[retrieval-utilization-gap]] — separates evidence that never surfaced from evidence that surfaced and was misused; a per-source loop addresses the first.
- [[evidence-dense-context-distillation]] — the other route past a fixed top-K, distilling retrieved pages into a fixed-length context, which still depends on what the retriever returns.

[^c1]: doi-10-48550-arxiv-2603-08329 — "evidence beyond the top-K results is typically discarded in a single retrieval pass"
[^c2]: doi-10-48550-arxiv-2603-08329 — "into a Shared Instruction Set for Documents and Synthesis Directives"
[^c3]: doi-10-48550-arxiv-2603-08329 — "the assigned sub-agent is strictly constrained to search tool calls within"
[^c4]: doi-10-48550-arxiv-2603-08329 — "SPD-RAG achieves an Avg Score of 58.1, substantially outperforming both Normal RAG (33.0)"
[^c5]: doi-10-48550-arxiv-2603-08329 — "more frequently captures the complete set of required facts"
[^c6]: doi-10-48550-arxiv-2603-08329 — "does not yield score improvements"
[^c7]: doi-10-48550-arxiv-2603-08329 — "uninstructed iterative retrieval without per-document specialization does not effectively address the coverage challenge in exhaustive"
[^c8]: doi-10-48550-arxiv-2603-08329 — "Academic papers in Loong often require synthesizing facts spread across abstracts, methods, results,"
[^c9]: doi-10-48550-arxiv-2603-08329 — "demonstrates the practical value of per-document specialization"
[^c10]: doi-10-48550-arxiv-2603-08329 — "the gap between SPD-RAG (56.9) and"
[^c11]: doi-10-48550-arxiv-2603-08329 — "SPD-RAG reaches 85.4% of this performance while consuming only 37.9% of the"
[^c12]: doi-10-48550-arxiv-2603-08329 — "under-specified tasks lead to incomplete document-level extractions"
[^c13]: doi-10-48550-arxiv-2603-08329 — "this recursive path was never activated"
[^c14]: doi-10-48550-arxiv-2603-08329 — "remain empirically unvalidated"
[^c15]: doi-10-48550-arxiv-2603-08329 — "may have different structural characteristics that alter relative performance"
[^c16]: doi-10-48550-arxiv-2603-08329 — "all RAGbased systems perform reasonably well"
