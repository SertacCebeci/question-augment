---
description: "Ranking tool nodes first and rolling each hit up to its owning agent through ownership edges retrieved the right agent more often than matching agent descriptions alone."
aliases: ["Agent-as-a-Graph retrieval", "agent-as-a-graph", "tool-to-agent graph traversal", "parent-agent roll-up"]
sources: ["arxiv-2511-18194"]
---
# Parent roll-up retrieval

A multi-agent system can index its capabilities at two grains. The coarse grain is the agent: one description per agent, matched against the query. The fine grain is the tool: each agent bundles many tools, each with its own name and description. The coarse method hides the fine grain. Existing methods match queries against "a single agent description, obscuring fine-grained tool capabilities of each agent"[^c1], so a query that one tool could answer can score low against the agent's summary.

Parent roll-up retrieval searches at the fine grain and returns at the coarse one. Agents and tools are nodes in one vector index, and each tool carries an edge to its parent agent. At query time the system takes the top N nodes of either type by similarity, follows each hit's edge to its owner, and keeps the top K distinct owners; in the authors' wording, "the top-K unique agents are selected".[^c2] The edge is the mechanism. The returned unit is an agent that owns the matched tool, so the request can be acted on: the authors say every query or sub-query "ultimately resolves to an executable agent".[^c3]

The argument for keeping both grains is about context. Retrieval by agent description alone "can miss" a tool's capability.[^c4] Retrieving tools without their owner "discards important execution context such as authentication, parameter inference, or access policies maintained at the" agent level.[^c5] The roll-up is meant to keep the tool's specificity while the parent supplies the bundle's context. Agent nodes are not dropped in favour of tools. They "aggregate the capabilities of their associated tools"[^c21], so they remain coarser retrieval targets in the same index.

The two node types are scored together by a weighted reciprocal rank fusion: "weighted reciprocal rank fusion (wRRF) for reranking tools and agents".[^c6] The design choice is to "decouple tools and agents at scoring time"[^c7]. A merged list gives every entity one global rank, and a weight per node type scales the reciprocal of that rank. The two weights are the only knobs that set how much agent coverage counts against tool specificity. Ties are broken by the global rank.

What the paper measured. On LiveMCPBench, with one encoder (ada-002), the unweighted graph reached Recall@5 of 0.83 against 0.79 for standard RRF: "Our approach achieves Recall@5 of 0.83 compared to RRF".[^c8] The type weighting at a 1.5:1 agent-to-tool ratio reached 0.85, "outperforming the unweighted baseline".[^c9] Across eight embedding models the average Recall@5 was 0.85 against 0.70 for MCPZero: "Agent-as-a-Graph achieves Recall@5 of 0.85 compared to 0.70 for MCPZero".[^c10] MCPZero is the comparison point, described by the authors as "state-of-the-art agent retrievers MCPZero".[^c11] The authors also report that "over 39% of retrieved items come from agent" nodes,[^c12] which they read as agent-side evidence staying important during selection.

## Limits

- **Small benchmark.** The evaluation uses a set "which contains 70 MCP servers and 527 tools, with 95 realworld questions".[^c13] A gap of 0.83 against 0.79 in Recall@5 is a difference of a few questions out of 95 (my inference). The text read gives no interval and no significance test.
- **Weights chosen on the evaluated set.** The weight grid was "swept over a ratio grid including the unweighted point"[^c14], and the reported optimum comes from that same sweep on one encoder: "We use OpenAI text-embedding-ada-002".[^c15] No held-out choice of weights is described, so the wRRF gain in the abstract, "2.4% improvements in wRRF optimizations",[^c16] is probably an optimistic estimate (my inference).
- **The roll-up's own contribution is asserted, not isolated.** The authors write that "the performance lift is not attributable to tool-level retrieval alone",[^c17] but the parts read contain no run with graph traversal switched off, and no run of a flat tool-only index on the same embeddings with the same fusion. Whether owner roll-up beats that baseline is therefore not shown here (my inference).
- **One setting of querying.** Each step of a decomposed task is sent to the retriever on its own, and that is "the primary setting used in our evaluations".[^c18] Querying with the user's whole request is described but its results were not in the text read.
- **The metric scores identity, not execution.** "Retrieval accuracy compares retrieved" agents against labelled agents.[^c19] A correct agent that then fails to run the tool is not a miss under this metric, and nothing here tests execution.
- **One owner per tool.** Each tool links to its parent through "edges explicitly linking it to its parent MCP server".[^c20] Tools shared by several agents, and agents nested inside agents, are outside what the text tests (my inference).

## Related

- [[groundedness-gated-tool-routing]] — picks a tool for a sub-query by whether its target is grounded; here the tool is found by similarity and its owning agent is the unit returned.
- [[typed-source-abstraction]] — routes a sub-query among source types; the roll-up routes among agents that bundle tools, a finer instance of the same choice.
- [[explanatory-abstention-protocol]] — a misrouted sub-agent reports the misroute back to its coordinator; roll-up is one way the query reaches the right agent before any such report is needed.

[^c1]: arxiv-2511-18194 — "a single agent description, obscuring fine-grained tool capabilities of each agent"
[^c2]: arxiv-2511-18194 — "the top-K unique agents are selected"
[^c3]: arxiv-2511-18194 — "ultimately resolves to an executable agent"
[^c4]: arxiv-2511-18194 — "Retrieving solely by agent descriptions can miss"
[^c5]: arxiv-2511-18194 — "discards important execution context such as authentication, parameter inference, or access policies maintained at the"
[^c6]: arxiv-2511-18194 — "weighted reciprocal rank fusion (wRRF) for reranking tools and agents"
[^c7]: arxiv-2511-18194 — "decouple tools and agents at scoring time"
[^c8]: arxiv-2511-18194 — "Our approach achieves Recall@5 of 0.83 compared to RRF"
[^c9]: arxiv-2511-18194 — "Recall@5 of 0.85 and nDCG@5 of 0.47, outperforming the unweighted baseline"
[^c10]: arxiv-2511-18194 — "Agent-as-a-Graph achieves Recall@5 of 0.85 compared to 0.70 for MCPZero"
[^c11]: arxiv-2511-18194 — "state-of-the-art agent retrievers MCPZero"
[^c12]: arxiv-2511-18194 — "over 39% of retrieved items come from agent"
[^c13]: arxiv-2511-18194 — "which contains 70 MCP servers and 527 tools, with 95 realworld questions"
[^c14]: arxiv-2511-18194 — "swept over a ratio grid including the unweighted point"
[^c15]: arxiv-2511-18194 — "We use OpenAI text-embedding-ada-002"
[^c16]: arxiv-2511-18194 — "2.4% improvements in wRRF optimizations"
[^c17]: arxiv-2511-18194 — "the performance lift is not attributable to tool-level retrieval alone"
[^c18]: arxiv-2511-18194 — "the primary setting used in our evaluations"
[^c19]: arxiv-2511-18194 — "Retrieval accuracy compares retrieved"
[^c20]: arxiv-2511-18194 — "edges explicitly linking it to its parent MCP server"
[^c21]: arxiv-2511-18194 — "Agent nodes aggregate the capabilities of their associated tools"
