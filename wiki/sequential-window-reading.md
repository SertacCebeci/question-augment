---
description: "Reading ranked retrieval window by window, stopping at the first sufficient one, trades recall against distractor noise; order and window size set how many irrelevant windows must be rejected."
aliases: ["adaptive prompting", "iterative prompting", "sliding-window prompting over retrieved pages", "divide-and-conquer prompting in RAG"]
sources: ["arxiv-2512-23836"]
---
# Sequential window reading

Standard retrieval-augmented answering puts every retrieved passage into the context at once. Sequential window reading cuts the ranked list into windows of w pages and prompts the model once per window, in descending retrieval score. The mechanism is a loop with a stop: "if a window yields sufficient information, the LLM generates the answer and terminates the process; otherwise, it signals the insufficiency and iterates to the next window."[^c1] Each window is a set of Wikipedia pages, each given as page ID, title and main content, and the window is "window of w Wikipedia pages (where w < K)" of the top-K retrieved.[^c2] When a window contains the answer, the model locates the page, quotes the passage and answers. When it does not, the model "provides a rationale for not providing an answer and proceeds to the subsequent window."[^c3]

The loop trades two quantities against each other through window size. A larger window is more likely to hold a relevant page but also brings more distractors: it is "to be positive but also introduce more distractors."[^c4] On the paper's fixed-window baseline this shows as an inverted U: "a tension between improved recall and increased" noise accumulation, with performance rising from windows of 50 to 100 pages and falling at 200.[^c5] The sequential reader takes the same trade in small steps. "Smaller windows reduce noise per step but require" the model to reject more windows, and the risk is that each rejection is one more chance for error: "sequence of negative windows, increasing the risk" of cumulative error.[^c6] In the ablation on Natural Questions, "a window size of 60 offers the best" balance between per-window difficulty and the total number of predictions.[^c7]

Order is the second dial. Reading the ranked list forward, the reader meets fewer than 0.5 irrelevant windows before the first relevant one at size 60; reading it backward, by ascending score, it meets 3.8 — "0.5 negative windows before seeing a positive window (at size 60), the backward approach encounters" 3.8 — and exact match falls.[^c8] The paper's conclusion from this is that "high-probability context windows first is critical to" avoiding hallucinated answers.[^c9]

The reported benefit is economy as well as accuracy. "By contrast, our iterative approach consistently" beats the top-K baseline on the datasets, and "reduces token usage" by more than half on average, because the model never sees the whole list at once.[^c10][^c11]

## Limits

- The stop is the model's own answer. A window that yields a wrong answer ends the loop, so the reader's false positives are terminal, while its false negatives are repaid only by later windows. The paper's analysis of false answers on irrelevant windows is what makes this matter (see [[search-induced-abstention-degradation]] for the abstention side). That the wrong answer terminates the loop is my inference from the stated procedure, not a measured quantity.
- Everything runs on one model: "Gemini 1.5 Pro for our experiments as it achieves" the best results among those it compared.[^c12] Retrieval is an in-house BM25 over Wikipedia pages, so the window count depends on the retriever's recall curve (Table 1 of the paper).
- Window sizes were 40 to 200 pages, not a continuous sweep. The best size of 60 is specific to these three open-domain QA datasets and this retriever; it is not a general rule for chunk length.
- The order effect is measured by sliding the window backward once. Other orders, and orders that interleave scores with evidence signals, were not tested.
- The sequential method was compared against fixed windows and top-K, not against chunk-level retrieval with reranking; whether the gain survives a stronger retriever is open.

## Related

- [[abstention]] — the reject option that a negative window asks the reader to exercise
- [[search-induced-abstention-degradation]] — the same failure to abstain on irrelevant retrieved text, measured with search in the loop
- [[stop-continue-criteria-in-retrieval-loops]] — how multi-hop loops decide when to stop; a window loop stops on the answer alone
- [[decoupled-search-context-chunk-size]] — the same recall-versus-context trade-off, solved there by indexing small chunks and passing larger ones
- [[rank-zero-misinformation-collapse]] — the position effect of retrieval order, here seen as a cost of reading the wrong window first

[^c1]: arxiv-2512-23836 — "Specifically, if a window yields sufficient information, the LLM generates the answer and terminates"
[^c2]: arxiv-2512-23836 — "window of w Wikipedia pages (where w < K) and"
[^c3]: arxiv-2512-23836 — "Otherwise, the LLM provides a rationale for not providing an answer and proceeds to the subsequent"
[^c4]: arxiv-2512-23836 — "to be positive but also introduce more distractors."
[^c5]: arxiv-2512-23836 — "a tension between improved recall and increased"
[^c6]: arxiv-2512-23836 — "sequence of negative windows, increasing the risk"
[^c7]: arxiv-2512-23836 — "a window size of 60 offers the best"
[^c8]: arxiv-2512-23836 — "0.5 negative windows before seeing a positive window (at size 60), the backward approach encounters"
[^c9]: arxiv-2512-23836 — "high-probability context windows first is critical to"
[^c10]: arxiv-2512-23836 — "By contrast, our iterative approach consistently"
[^c11]: arxiv-2512-23836 — "context at once, our strategy reduces token usage"
[^c12]: arxiv-2512-23836 — "Gemini 1.5 Pro for our experiments as it achieves"
