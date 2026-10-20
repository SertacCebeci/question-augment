---
description: "Separate keyword, sentence-embedding and chunk-read tools let a retrieval agent pick granularity per step, and the paper reports better accuracy with fewer retrieved tokens than one embedding tool."
aliases: ["A-RAG", "multi-granularity retrieval tools", "hierarchical retrieval tools", "keyword, semantic and chunk-read interfaces"]
sources: ["doi-10-48550-arxiv-2602-03442"]
---
# Hierarchical retrieval interfaces

> The corpus is not stored at one grain. Exposing each grain as its own
> tool lets the model choose which grain to look at, and how much of it to
> read, instead of receiving a fixed set of top-k passages.

## Definition / Mechanism

The corpus is partitioned into chunks of roughly 1,000 tokens, with chunk
boundaries aligned to sentence boundaries.[^c1] Three granularities are then
kept, and each gets its own retrieval tool. The authors' premise is that
"information within a corpus is inherently organized at multiple
granularities."[^c2]

- **Keyword level, no pre-index.** The index is not built offline. The
  keyword tool does "exact text matching directly at query time."[^c3] A
  chunk's score is the sum over the agent's keywords of the keyword's
  frequency in the chunk times its character length, so longer, more specific
  keywords count for more.[^c4] The tool returns chunk IDs with short snippets
  made of the sentences that contain a keyword.
- **Sentence level, dense.** Each sentence gets its own embedding. The
  semantic tool scores sentences against a query, then ranks each chunk by its
  best sentence. The sentence-level embedding "enables fine-grained semantic
  matching" while keeping a link back to the parent chunk, "allowing the agent
  to first identify relevant sentences and then read the complete" chunk.[^c5]
- **Chunk level, full text.** The chunk-read tool returns the whole chunk and
  can read neighbouring chunks. A context tracker records chunks already read;
  a repeat read returns a notice "instead of returning the full text again."[^c6]

The loop is ReAct-like: one tool call per step, then observe, then decide. The
authors deliberately forbid parallel tool calls to keep the comparison clean.[^c7]
What the agent receives is therefore decided step by step. Snippets come
first, and full chunks are read only when a snippet looks promising. Context
is spent on demand rather than loaded in bulk.

What the paper measures:

- **Removing tools hurts.** In the ablation, removing either semantic search
  or keyword search degrades performance, which the authors read as
  "highlighting the importance of multi-granularity information for multi-hop
  retrieval tasks."[^c8] Replacing snippets with whole chunk texts and removing
  chunk read also lowers results, which the authors attribute to the agent
  being able to "selectively read only the most relevant chunks" and so avoid
  "the noise introduced by irrelevant content."[^c9]
- **Context efficiency.** On the GPT-5-mini backbone, the full hierarchy is
  reported to use fewer or comparable retrieved tokens than the baselines
  while scoring higher.[^c10] The naive variant, with only the embedding
  tool, retrieves far more. In the extracted table, the MuSiQue row reads
  56,360 tokens for the naive variant against 5,663 for the full one; I read
  that layout from garbled text, so treat the exact figures as provisional.[^c11]
- **Scaling with test-time compute.** On MuSiQue-300, accuracy rises with the
  step budget and with reasoning effort. Going from 5 to 20 steps adds about
  8 points for GPT-5-mini and about 4 for GPT-4o-mini. Raising reasoning effort
  from minimal to high adds roughly 25 points for both GPT-5-mini and GPT-5.[^c12]

The naive variant is itself a finding: a single embedding tool with agent
control already "establishes a new strong baseline for agentic RAG," ahead of
the fixed-workflow and graph methods the paper compares against.[^c13]

## Limits

- The tool suite is one design. The authors "do not exhaustively enumerate all
  possible tool designs" and do not compare other tool subsets, so the claim
  is that multi-granularity tools help, not that this granularity split is
  optimal.[^c14]
- Only one backbone family is tested. The authors state that they "have not
  validated the framework on larger and more powerful models," and they expect
  larger gains there without showing it.[^c15]
- The evidence is multi-hop QA on four benchmarks, with the corpus and
  questions taken from LinearRAG's setup. Generalisation to fact verification,
  dialogue, or long-form generation is untested.[^c16]
- The keyword tool does a runtime scan rather than an index, so its cost grows
  with the corpus. The paper says the design "significantly reduces both
  indexing time and computational cost" compared with graph methods, but it
  does not report query-time latency at scale.
- The ablation's numeric results are in a table whose text extraction is
  unreliable here; the claims above rest on the authors' prose.
- The efficiency comparison counts retrieved corpus tokens, not total tokens
  spent by the agent's reasoning and tool-call overhead.
- The failure analysis, on 100 MuSiQue errors, finds reasoning-chain errors
  dominate the full system.[^c17] So granular retrieval shifts the bottleneck
  to use rather than removing it; this matches the utilization-side failures
  described in [[retrieval-utilization-gap]].

## Related

- [[searchwiki-hierarchical-corpus]] — also gives the agent coarse-to-fine
  choices, but by compiling a three-layer wiki offline; A-RAG keeps a flat
  chunked corpus and gets its granularities from runtime matching and sentence
  embeddings.
- [[retrieval-utilization-gap]] — separates retrieval failures from use
  failures; A-RAG's failure analysis points at use after retrieval succeeds.
- [[agentic-rag-autonomy-principles]] — the three criteria the paper uses to
  call a retrieval method agentic, which this interface design is meant to
  satisfy.

[^c1]: doi-10-48550-arxiv-2602-03442 — "we partition the corpus into chunks of approximately 1,000 tokens each"
[^c2]: doi-10-48550-arxiv-2602-03442 — "information within a corpus is inherently organized at multiple granularities"
[^c3]: doi-10-48550-arxiv-2602-03442 — "we perform exact text matching directly at query time"
[^c4]: doi-10-48550-arxiv-2602-03442 — "longer keywords are weighted higher as they are typically more specific"
[^c5]: doi-10-48550-arxiv-2602-03442 — "allowing the agent to first identify relevant sentences and then read the complete"
[^c6]: doi-10-48550-arxiv-2602-03442 — "instead of returning the full text again"
[^c7]: doi-10-48550-arxiv-2602-03442 — "We intentionally avoid parallel tool calling"
[^c8]: doi-10-48550-arxiv-2602-03442 — "highlighting the importance of multi-granularity information for multi-hop retrieval tasks"
[^c9]: doi-10-48550-arxiv-2602-03442 — "avoiding the noise introduced by irrelevant content"
[^c10]: doi-10-48550-arxiv-2602-03442 — "A-RAG achieves superior accuracy with higher context efficiency"
[^c11]: doi-10-48550-arxiv-2602-03442 — "Retrieved tokens across methods (GPT-5-mini backbone). Lower values indicate higher efficiency."
[^c12]: doi-10-48550-arxiv-2602-03442 — "When scaling from 5 to 20 steps, GPT-5-mini improves by approximately 8%"
[^c13]: doi-10-48550-arxiv-2602-03442 — "Naive A-RAG establishes a new strong baseline for agentic RAG."
[^c14]: doi-10-48550-arxiv-2602-03442 — "we do not exhaustively enumerate all possible tool"
[^c15]: doi-10-48550-arxiv-2602-03442 — "Due to computational resource constraints, we have not validated the framework on larger and more powerful models"
[^c16]: doi-10-48550-arxiv-2602-03442 — "other knowledge-intensive tasks such as fact verification, dialogue systems, and long-form generation warrants further"
[^c17]: doi-10-48550-arxiv-2602-03442 — "dominant failure mode (82% on MuSiQue) is reasoning chain errors"
