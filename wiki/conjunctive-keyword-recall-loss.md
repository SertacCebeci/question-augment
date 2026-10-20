---
description: "In LLM-built keyword queries for RAG, joining terms with AND retrieved fewer relevant documents than OR-only queries did, though the AND queries collected more documents in total."
aliases: ["OR versus AND query breadth", "Boolean conjunction recall cost", "AND-joined keyword query recall loss"]
sources: ["arxiv-2512-00772"]
---
# Conjunctive keyword recall loss

A keyword query can join its terms with AND, which keeps a document only if it contains every term, or with OR, which keeps a document that contains any one of them. The older Boolean literature hoped the operators would give "high recall and precision simultaneously",[^c1] but it also noted that natural-language queries often did better than Boolean ones.[^c2] The SHRAG paper tests the operator choice inside a retrieval-augmented pipeline. An LLM extracts ranked keywords in English and Korean, and the search query joins them with OR. The test varies the number of ANDs from 0 (OR only) to 9 (AND only) over 50 queries, runs each condition ten times, and measures "the proportion of answer documents that are included in search documents".[^c3]

OR-only queries did better on that proportion. The paper reports that OR-only queries "showed superior document collection performance compared to cases that included the AND operator."[^c4] On the count of documents, the order reverses: "search queries using only OR (0 ANDs) collected fewer than" about 1,500 documents, "whereas search queries containing AND collected approximately 2,000" or more.[^c5][^c6] So a conjunction enlarged the pool and lowered the share of answers inside it. The paper reads this as a loss of relevance: "although a wider variety of documents may be collected, there is a tendency for document relevance to decrease."[^c7] Its explanation is interpretive: the AND operator "is interpreted as overemphasizing the specific connected keywords, thereby leading to search results that deviate from the core topic."[^c8]

The mechanism, stated without reference to the search engine, is a count of the ways a relevant document can be lost. A conjunction of k terms drops a document whenever it lacks any one of them, so a relevant page that uses a synonym, a translation or a different phrasing of one term falls out. A disjunction loses it only when it lacks all the terms. This is why the paper argues for breadth: it aims "to secure a broad range of potentially relevant documents",[^c9] on the reasoning that a query aimed at a few specific documents leaves a RAG system with nothing when one of them is missed.[^c10] The same reasoning suggests why mixing the two languages is cheap under OR. A document in either language can match, so the English and Korean keywords widen the set without requiring both (my inference, not tested separately).

## Limits

- One search platform (ScienceON, a Korean academic site), 50 queries and one generator (Gemini 2.5 Flash). The operator comparison is reported for that setting only.
- The measure is the share of gold answer documents that the search returns, which is a recall-type figure. The paper's phrase "document relevance" for the same result is its own gloss; precision was not measured. (my reading)
- The AND queries were built differently from the OR-only one: they "start from the lower priority keywords" and add higher ones, so the document counts compare different query shapes.[^c11] The text does not explain why such queries return more documents, and the explanation offered is an interpretation that was not tested. (my reading)
- The paper says the operator comparison was repeated on a Wikipedia setting with the MIRACL dataset.[^c12] The results it reports for that dataset are the final framework's query success rate only, so the operator effect outside ScienceON is not shown in the text. (my reading)
- NOT was not tested. The paper excluded NOT queries because "Queries incorporating the NOT operator were considered but excluded from this study," and writing them needs reasoning the keyword step lacks.[^c13]
- The result is a breadth trade inside one pipeline. The paper does not isolate how a wider pool changed final answer quality, and it says nothing about dense retrieval, where the AND/OR choice does not arise in the same form. (my inference)

## Related

- [[candidate-set-narrowing-recall]] — the same recall-first case for a shortlist before a chooser; there the cut sets the ceiling, here the conjunction is the cut.
- [[conjunctive-masked-criteria]] — the same intersection property used the other way: several criteria jointly pick out one page, whereas a conjunction of literal keywords here discards the relevant page.
- [[literal-match-dependence]] — retrieval that leans on literal word overlap; a conjunction raises the overlap a document must have with the query.
- [[multi-query-expansion-precision-penalty]] — broader retrieval by more queries lowered precision with no recall gain, a different outcome from the OR breadth found here.

[^c1]: arxiv-2512-00772 — "operators such as AND, OR, and NOT were proposed to achieve high recall and precision simultaneously."
[^c2]: arxiv-2512-00772 — "queries showed better performance than search queries using Boolean operators"
[^c3]: arxiv-2512-00772 — "measured the proportion of answer documents that are included in search documents"
[^c4]: arxiv-2512-00772 — "showed superior document collection performance compared to cases that included the AND operator"
[^c5]: arxiv-2512-00772 — "search queries using only OR (0 ANDs) collected fewer than"
[^c6]: arxiv-2512-00772 — "whereas search queries containing AND collected approximately 2,000"
[^c7]: arxiv-2512-00772 — "although a wider variety of documents may be collected, there is a tendency for document relevance to"
[^c8]: arxiv-2512-00772 — "the AND operator is interpreted as overemphasizing the specific connected"
[^c9]: arxiv-2512-00772 — "This aims to secure a broad range of potentially relevant documents"
[^c10]: arxiv-2512-00772
[^c11]: arxiv-2512-00772 — "starting from the lower priority keywords in the importance ranking"
[^c12]: arxiv-2512-00772 — "we performed an identical experiment in a Wikipedia based search environment"
[^c13]: arxiv-2512-00772 — "Queries incorporating the NOT operator were considered but excluded from this study"
