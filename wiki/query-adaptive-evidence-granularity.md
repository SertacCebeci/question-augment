---
description: "The grain of evidence a question needs, from one fact to a long narrative span, belongs to the question; a planner choosing the chunk-size range per query beat fixed chunking in its runs."
aliases: ["query-adaptive chunking", "query-aware chunk granularity", "per-query chunk size selection", "adaptive retrieval granularity", "multi-level retrieval granularity"]
sources: ["arxiv-2602-22225", "doi-10-48550-arxiv-2512-02425", "doi-10-48550-arxiv-2607-10463"]
---
# Query-adaptive evidence granularity

A retrieval system that answers questions from a long document has to decide how big a piece of text to hand the answerer. The SmartChunk paper treats that size as something to choose per question rather than fix once for the corpus. Its planner takes the question and the document's metadata and outputs a range: "decides the smallest and largest chunk sizes required to answer a query."[^c1] Retrieval is then restricted to chunks whose level falls inside that range. The chunks come from a hierarchy built over the document, so one question can draw on fine spans while another draws on coarse ones.

The motivation is the same sensitivity that other notes on chunking describe. The paper states that retrieval quality is sensitive to chunk size and that "no single granularity works" across heterogeneous queries and document structures.[^c2] A fixed size therefore serves some questions and misses others. The per-question choice is the paper's answer to that.

The reported behaviour shows the question setting the grain. On NarrativeQA, with abstractive questions about long fiction, the planner picks large spans: "larger chunks (avg. size: 1725) to capture broader contextual arcs necessary for narrative understanding."[^c3] On QASPER, with factual multi-hop questions over dense papers, it "favors smaller chunks (avg. size: 230) to maintain precision."[^c4] The authors read the spread as the planner adjusting "chunk selection to dataset characteristics and query complexity."[^c5] The minimum and maximum levels also differ within a query, so the planner starts from fine spans for grounding and widens when broader evidence helps.

Two things carry the idea. The first is that granularity is a variable of the question, not only of the corpus: the same document can need a sentence for one question and a section for the next. The second is that the choice is made before retrieval and before the answerer reads anything. The planner is a learned model, not a search over the answers. How the planner is trained is a separate question: the paper trains it with reinforcement learning, using expert traces as hints and imitation for cases left unsolved. That training loop is method, and this note does not carry it. The concept is only the per-question range.

A video memory agent sets the grain inside its retrieval loop instead of before retrieval. WorldMM keeps episodic memories at several temporal scales, and its retrieval agent chooses among them per question: the agent "leverages multiple temporal granularities based on the query."[^c8] The stated motivation is the same variable-scope point: "retrieving a fixed number of clips limits the model's ability to handle queries that require varying temporal scopes."[^c9] The paper's scale table compares three sets of scales as a whole, not a per-query range against a fixed one; its caption reads "Performance with different episodic timescales," and the extracted accuracies sit in a narrow band.[^c10] So the per-question claim is motivated in the paper but not isolated by it.

A different placement of the choice appears in a multi-hop QA agent trained with reinforcement learning. There the grain is an action taken at each step, not a range set before retrieval. The search tools return sentences, and a separate read action returns the parent paragraph of a sentence the agent has found.[^c11] The paper's ablation removes the read action, which "denotes fixed paragraph-level granularity," and exact match falls from 0.510 to 0.388.[^c12] The authors read the gap as a query problem: when the agent sees whole paragraphs, "it tends to generate follow-up queries that remain" close to the original question, since "paragraph-level results expose many entities" at once and the next missing clue is harder to isolate.[^c13] So the same variable, the grain of evidence, can be fixed per question or chosen per step, and the paper measures the per-step version only.

## Limits

- The granularity claim is a measurement on the paper's own QA benchmarks, using one generator family and one planner design. The "no single granularity works" statement is introduced with a citation to another chunk-size study rather than shown here.[^c2]
- The planner's labels are pseudo-labels. The paper says "ground-truth labels are unavailable," so the target it learns is itself constructed by the method's own pipeline.[^c6] Whether the per-query range matches what a human reader would need is not checked.
- Generalization was tested on one out-of-domain set, NewsQA. The planner trained on other datasets "significantly outperforms the fixed-size chunking baseline," but that is one transfer target.[^c7]
- The planner is judged by answer accuracy and cost jointly. A gain in one can hide a loss in the other, and the sections read do not separate them for the granularity choice alone.
- The concept is retrieval for a machine answerer. What carries over to a human asker is my inference: that the grain a question needs can be read off its type. The paper does not test human askers or human answerers.
- The per-step granularity result rests on one 3B backbone and a single ablation, so it shows that the read action matters in that setting, not that a per-step grain beats a per-question range. "Our experiments are limited to a single 3B-parameter backbone," as the paper itself says.[^c14]
- The video agent's grain is chosen by a model inside an iterative loop over stored memories, with no fixed range fed to it before retrieval. The paper's scale sweep changes the set of scales as a whole, so whether a per-query range beats a fixed one is not measured there.[^c10]

## Related

- [[decoupled-search-context-chunk-size]] — the fixed alternative: one set of small search chunks and one larger context chunk per page, the same size for every question. Query-adaptive granularity instead varies the size per question.
- [[on-demand-resolution-zoom]] — the answerer requests a finer look mid-reasoning; here the grain is fixed before retrieval from the question and metadata. Both locate the decision about grain away from a single static choice.
- [[evidence-scope-gradient]] — the same idea of scope as a property of the question, on the evidence side.
- [[query-relative-token-overflow]] — sufficiency of a compressed context is relative to the question asked of it; the planner's per-question range is the retrieval-side version of that point.
- [[requested-span-granularity-gradient]] — granularity as a difficulty variable in code requests, on the output side.
- [[query-adaptive-memory-modality]] — the same per-question choice on the memory-type axis, in a video memory agent that also picks the scale inside its loop.

[^c1]: arxiv-2602-22225 — "decides the smallest and largest chunk sizes required to answer a query"
[^c2]: arxiv-2602-22225 — "no single granularity works"
[^c3]: arxiv-2602-22225 — "larger chunks (avg. size: 1725) to capture broader contextual arcs necessary for narrative understanding"
[^c4]: arxiv-2602-22225 — "favors smaller chunks (avg. size: 230) to maintain precision"
[^c5]: arxiv-2602-22225 — "tailor chunk selection to dataset characteristics and query complexity"
[^c6]: arxiv-2602-22225 — "ground-truth labels are unavailable"
[^c7]: arxiv-2602-22225 — "significantly outperforms the fixed-size chunking baseline"
[^c8]: doi-10-48550-arxiv-2512-02425 — "leverages multiple temporal granularities based on the query"
[^c9]: doi-10-48550-arxiv-2512-02425 — "queries that require varying temporal scopes"
[^c10]: doi-10-48550-arxiv-2512-02425 — "Performance with different episodic timescales"
[^c11]: doi-10-48550-arxiv-2607-10463 — "The first two retrieve sentence-level evidence from the corpus S"
[^c12]: doi-10-48550-arxiv-2607-10463 — "Without τr denotes fixed paragraph-level granularity."
[^c13]: doi-10-48550-arxiv-2607-10463 — "it tends to generate follow-up queries that remain"
[^c14]: doi-10-48550-arxiv-2607-10463 — "our experiments are limited to a single 3B-parameter backbone"
