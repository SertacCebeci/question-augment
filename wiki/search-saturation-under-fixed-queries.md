---
description: "An in-loop web search whose queries do not follow the solution keeps returning pages already seen: 88.1% of returned URLs were repeats in one run, and progress stopped after iteration 50."
aliases: ["in-loop search stall", "repeated-URL saturation", "joint-level search stall"]
sources: ["doi-10-48550-arxiv-2609-40340", "doi-10-48550-arxiv-2408-10490"]
---
# Search saturation under fixed queries

A solution search that can call a web tool looks like a free source of new knowledge. The paper's measurements show that the tool can saturate: it keeps returning the pages the run has already seen. The name "saturation" is mine; the paper describes the same thing as the search stalling. The abstract puts the mechanism plainly: "simply adding web search tool can keep returning the same pages as solutions change."[^c1] The paper's claim is that this is a property of when and how queries are formed, not of the number of queries.

The measurement is on Denoising with GPT-5.6-Luna over 100 iterations. The in-loop baseline, which lets the model write its own queries during optimization, "produces 185 queries, compared with 201" for the bi-level method.[^c2] The query counts are close, but the baseline "retrieves only 85 distinct" URLs, against 248 for the bi-level method.[^c3] The repeat rate is the sharper number: "88.1% of its returned URLs have appeared before", against "62.4% for E VO D UET".[^c4][^c5] The stall shows in progress as well. "joint-level search stops improving after iteration 50", and its best program reaches "held-out NDG of 27.7%, compared with 84.5% for E VO D UET."[^c6][^c7]

The paper's reading is that the query has no memory of what came back. In the in-loop baseline, the model "repeatedly retrieves the same pages and stalls" because it writes each query from the current prompt, which changes little from one iteration to the next.[^c8] The bi-level method instead has the query constructor produce "J queries targeting the remaining knowledge gaps", using the knowledge state and the scored documents from earlier rounds.[^c9] The bi-level search "retrieves about 2.9× as many distinct pages" under comparable query counts.[^c10] The mechanism I take from this is that a query aimed at a stated gap, rather than at the surface of the prompt, moves when the gap moves (my inference from the design, not a measured result).

A similar pattern appears in a different setting: long-form biography writing with web search, scored by attribution rather than repeated URLs. Godbole et al. test whether more of the same search helps. Doubling the snippets from the initial entity query is "inconsistent and it only improves attribution in 3 out of 8 settings".[^c12] A second search, with queries written per paragraph outline item, adds "improvements of about 5 points of Macro and Micro AIS and two points of strict AIS".[^c13] Their summary is that "appending more search results based on the initial query is not enough to improve attribution."[^c14] This fits the reading above: the extra results from one query do not move the evidence, while a query aimed at a new part of the outline does. The fit is my reading; the attribution scores do not measure repeats.

## Limits

- One task and one model carry the comparison. The figure is labelled "Effects of parallel generation and query evolution with GPT-5.6-Luna", and the saturation case is Denoising.[^c11] Whether the pattern holds on other tasks, or with a smaller model, is not in the text I read.
- The baseline is a specific setup: a Tavily search tool inside OpenEvolve. A different search engine, a different query budget, or a longer run could change the repeat rate. None of these was varied.
- The comparison does not isolate query evolution. The bi-level method also has the gate and the document scoring, so the gain cannot be assigned to query construction alone from this comparison (my inference).
- A distinct URL is not a unit of new knowledge. The paper counts repeats, but does not measure whether new pages carried information that changed a candidate (my inference).
- The stall is reported as stopped improvement after iteration 50 in one run. Whether the in-loop search would have recovered with more iterations is not tested.
- The second-search result is not isolated from the outline that writes its queries; the paper ablates the outline separately, so the two effects are not split here (my inference).

## Related

- [[knowledge-gap-reuse-gate]] — the gate that can reuse stored documents instead of issuing a new search whose results would repeat
- [[predicted-outcome-document-ranking]] — how the documents from new queries are ranked before they reach the solution prompt

[^c1]: doi-10-48550-arxiv-2609-40340 — "the same pages as solutions change"
[^c2]: doi-10-48550-arxiv-2609-40340 — "iterations and produces 185 queries, compared with 201 for E VO D UET"
[^c3]: doi-10-48550-arxiv-2609-40340 — "However, it retrieves only 85 distinct"
[^c4]: doi-10-48550-arxiv-2609-40340 — "88.1% of its returned URLs have appeared before"
[^c5]: doi-10-48550-arxiv-2609-40340 — "62.4% for E VO D UET"
[^c6]: doi-10-48550-arxiv-2609-40340 — "joint-level search stops improving after iteration 50"
[^c7]: doi-10-48550-arxiv-2609-40340 — "held-out NDG of 27.7%, compared with 84.5% for E VO D UET"
[^c8]: doi-10-48550-arxiv-2609-40340 — "Without query evolution, in-loop web search repeatedly retrieves the same pages and stalls."
[^c9]: doi-10-48550-arxiv-2609-40340 — "constructs J queries targeting the remaining knowledge gaps"
[^c10]: doi-10-48550-arxiv-2609-40340 — "retrieves about 2.9×"
[^c11]: doi-10-48550-arxiv-2609-40340 — "Effects of parallel generation and query evolution with GPT-5.6-Luna"
[^c12]: doi-10-48550-arxiv-2408-10490 — "the gain from this approach is inconsistent and it only improves attribution in 3 out of"
[^c13]: doi-10-48550-arxiv-2408-10490 — "produces improvements of about 5 points of Macro and Micro AIS and two points of strict AIS"
[^c14]: doi-10-48550-arxiv-2408-10490 — "appending more search results based on the initial query is not enough to improve attribution"
