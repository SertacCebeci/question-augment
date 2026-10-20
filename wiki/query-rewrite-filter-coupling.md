---
description: "A verbose user question rewritten into search keywords can lose context and lower retrieval scores; the paper reports that drop only in a run without URL filtering."
aliases: ["query refinement", "search-query rephrasing", "rephrase-then-retrieve", "rewrite-filter interaction"]
sources: ["arxiv-2512-22442"]
---
# Query rewrite and downstream filter coupling

A user's question can be rewritten before it reaches a search engine. HiFi-RAG asks Gemini 2.5 Flash to turn the question into "an effective and concise Google search query".[^c1] The stated reason is that user queries are "often too verbose or conversational for effective retrieval".[^c2] The rewrite is meant to extract the core intent and the distinct search terms, which the authors expect to help recall "for complex constraints".[^c3]

What the rewrite keeps is a choice. The paper's examples show a request that opens with a persona and asks for an explanation "like I am five" reduced to keyword queries, one of which is "ELI5 how a camera works".[^c4] The persona, the framing and the stylistic asks are dropped, and the search engine never sees them.

The paper's one measured observation of a rewrite, on its own, is on the synthesized Test2025 set: "query rephrasing without URL filtering (RAG w/ Filters + Rephrase) resulted in lower scores, likely due to the removal of context from verbose queries which can introduce ambiguity."[^c5] The authors' reading is that words removed from a verbose question carried constraints, and without them the search is ambiguous. The word "likely" marks this as their explanation. The paper does not compare the dropped words with the pages that came back.

The same passage ties the effect to a second step: "Because URL filtering mitigates these errors, query refinement proves most effective when implemented in conjunction with filtering."[^c6] Read with the table, a rewrite is not a gain by itself. Its effect depends on what the downstream step does with the pages the new query returns. That dependence is my inference, not the paper's claim: a different query returns a different set of pages, and a gate decides which of them are read.

The numbers, as I read Table 3: ROUGE-L is 0.2898 for the row labelled "RAG w/ Filters + Rephrase"[^c7] and 0.3031 for the same filters without the rewrite. The final system in Table 2 bundles the rewrite with a second generation turn, labelled "Final (RAG w/ Filters + Rephrase + 2-Turn)",[^c8] so its best score cannot be attributed to the rewrite.

The paper's label and its text disagree. The row name says "Filters", while the sentence says "without URL filtering". I have kept the text's reading and have not resolved the conflict.

## Limits

- No run isolates the rewrite on the validation set. The final row also contains a second generation turn.
- The Test2025 comparison is one set of 100 questions written by a model (Gemini 3.0), and the paper reports no variance across runs.
- The context-removal cause is the authors' guess ("likely"). It was not measured.
- One rewriting model (Gemini 2.5 Flash) and one prompt were used. Whether a rewrite that keeps the user's constraints verbatim avoids the loss was not tested.
- The row-label conflict noted above is unresolved in the text.

## Related

- [[query-to-question-reformulation]] — the opposite direction: agent keyword queries rewritten into questions help a neural ranker and hurt BM25, so a rewrite's gain depends on the component it feeds.
- [[query-expansion-harm-asymmetry]] — expansion helps few queries and hurts more, and averages hide the split. A rewrite could show the same per-query pattern (my inference; not tested in either note).
- [[cost-ordered-perception-pyramid]] — the cheap text-side gate that HiFi-RAG pairs with its rewrite, judged from titles and snippets before any page is read.
- [[question-rewriting-schema-scaling]] — a question-clarifying rewrite step in Text-to-SQL, where ablating it costs accuracy.

[^c1]: arxiv-2512-22442 — "Create an effective and concise Google search query for this question:"
[^c2]: arxiv-2512-22442 — "User queries are often too verbose or conversational for effective retrieval"
[^c3]: arxiv-2512-22442 — "this step extracts core intent and distinct search terms, improving recall for complex constraints"
[^c4]: arxiv-2512-22442 — "ELI5 how a camera works"
[^c5]: arxiv-2512-22442 — "likely due to the removal of context from verbose queries which can introduce ambiguity"
[^c6]: arxiv-2512-22442 — "query refinement proves most effective when implemented in conjunction with filtering"
[^c7]: arxiv-2512-22442 — "RAG w/ Filters + Rephrase"
[^c8]: arxiv-2512-22442 — "Final (RAG w/ Filters + Rephrase + 2-Turn)"
