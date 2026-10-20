---
description: "An LLM states what it still lacks, then chooses among no search, reusing stored documents, or retrieving new ones; the paper reports this gate beats a stalled-progress trigger."
aliases: ["knowledge-gap-based retrieval gating", "retrieval gate with reuse", "LOOK-UP gate", "knowledge-gap gate"]
sources: ["doi-10-48550-arxiv-2609-40340"]
---
# Knowledge-gap reuse gate

In an evolutionary search that can call a web tool, a gate decides at each iteration whether a search is needed at all. The gate is one LLM call. It outputs a knowledge state, a written account of what the model already holds, what earlier searches and experiments established, and "unresolved questions about xt that define the current knowledge gap."[^c1] From that state it returns one of three actions. It selects NO-OP "when the model’s knowledge suffices", LOOK-UP "when stored documents provide the missing knowledge", and RETRIEVE "when neither source is sufficient."[^c2]

The third action is what separates this from a plain retrieve-or-not switch. The gate can reuse documents already in the store, so a gap that an earlier search covered does not cause a new search. "Under LOOK - UP, the selected documents are included in the solution prompt without a new web" search.[^c3] The paper's example is an iteration where "the gate reuses stored documents without a new web search."[^c4] The reused documents go into the solution prompt as they are; no query is issued.

The decision is conditioned on a different signal from the triggers already in this wiki. [[uncertainty-guided-retrieval-triggering]] makes one retrieve-or-not call before drafting, from the likelihood of the whole query. [[step-level-retrieval-trigger]] scores each reasoning step for uncertainty and fires where the score is high. Here the signal is the model's own written statement of what the current solution still lacks, and the outcomes are three, not two. The paper's comparison is with a heuristic: EvoX changes its search strategy on "stalled progress", and the paper reports that "knowledge-gap-based gating is more effective than the heuristic gating" in its Table 1b.[^c5][^c6] I did not read the table's numbers; the claim is the paper's.

When the gate chooses RETRIEVE, it hands control to an inner loop of query construction, search, and scoring, and the knowledge state is carried through those rounds. So the gate is the link between the solution loop and the query loop. What the inner loop does with the new documents is the subject of [[predicted-outcome-document-ranking]].

## Limits

- The gate trusts the model's account of its own gap. Nothing in the text checks the written knowledge state against what the model actually lacks. Whether a model can say what it does not know is an assumption the method rests on, not something the paper tests (my inference).
- The method's headline result is not uniform across models. The abstract says that "whereas Qwen3.5-9B does not benefit".[^c7] Whether the gate's self-report is weaker in the smaller model is not separated from the other parts of the method in the text I read (my inference).
- The only gating comparison I read is against one heuristic, the stall trigger of EvoX. The text does not compare the gate with a fixed schedule, a learned policy, or always-retrieve, so the reported advantage is relative to that one alternative.
- The gate is a model call on every iteration, which the baselines do not make. The text I read does not separate its share of the total cost.

## Related

- [[uncertainty-guided-retrieval-triggering]] — the same retrieve-or-not question, asked once before drafting and from likelihood rather than a written knowledge state
- [[step-level-retrieval-trigger]] — a per-step uncertainty trigger inside a reasoning chain; it has no reuse branch for documents already fetched
- [[hypothetical-query-context-ranking]] — another LLM pass over documents before retrieval, but it writes questions a context answers, not a predicted solution score
- [[predicted-outcome-document-ranking]] — what the RETRIEVE branch does with the documents it returns
- [[search-saturation-under-fixed-queries]] — why a gate that can reuse stored evidence matters when a search keeps returning the same pages

[^c1]: doi-10-48550-arxiv-2609-40340 — "unresolved questions about xt that define the current knowledge gap"
[^c2]: doi-10-48550-arxiv-2609-40340 — "The gate selects NO - OP when the model’s knowledge suffices"
[^c3]: doi-10-48550-arxiv-2609-40340 — "Under LOOK - UP, the selected documents are included in the solution prompt without a new web"
[^c4]: doi-10-48550-arxiv-2609-40340 — "At iteration 64, the gate reuses stored documents without a new web search."
[^c5]: doi-10-48550-arxiv-2609-40340 — "based on stalled progress used in EvoX"
[^c6]: doi-10-48550-arxiv-2609-40340 — "knowledge-gap-based gating is more effective than the heuristic gating"
[^c7]: doi-10-48550-arxiv-2609-40340 — "whereas Qwen3.5-9B does not benefit"
