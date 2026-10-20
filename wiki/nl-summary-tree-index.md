---
description: "Summarizing a code corpus into LLM-written natural-language notes at file, directory and repository level lets a bug report match by NL-to-NL search, not cross-modal retrieval."
aliases: ["NL knowledge base", "hierarchical NL summaries", "summary tree index", "NL-to-NL retrieval over summaries"]
sources: ["arxiv-2512-05908", "arxiv-2511-18177"]
---
# NL summary tree index

The corpus is rewritten before any question arrives. For each repository, an LLM first writes a summary from its tree, documents and code, and that summary becomes the "seed context" for everything below it.[^n1] Each source file is then summarized by an LLM from its raw code, primed with that seed context.[^n2] File summaries are aggregated at the directory level, and directory summaries sit under the repository summary. The paper calls the result a hierarchical NL knowledge base. It is built once, offline. The paper reports the cost as a "non-negligible computational cost", about $80 for its industrial system, and argues that the summaries "capture the high-level purpose and architectural role" of files, so that implementation churn rarely makes them wrong.[^n3][^n4]

The mechanism is a change in what gets compared. A bug report is written in ordinary language and the code is written in a programming language, and the usual retrieval setup has to match the two across that boundary with embeddings. The paper lifts the code to the level of the report instead. Matching then becomes "a unified NL-to-NL reasoning task", in which an LLM compares a report with summaries rather than with code vectors.[^n5] The tree is used top-down. To route a report, it is compared "against the high-level, repository-level summaries of all microservices", which yields a ranked list of candidate repositories. Inside a candidate repository, the report is compared "against all directory-level summaries" to keep the top-k directories, and only the files inside those directories are ranked.[^n6]

What was measured. The system is evaluated on DNext, "an industrial system with 46 repositories and 1.1M lines of code". The paper reports that its method "achieves Pass@10 of" 0.82 and MRR of 0.50, "significantly outperforming retrieval" baselines and agentic RAG systems.[^n7] The routing step "outperforms the Agentic RAG baselines on coverage metrics", meaning Pass@3 and Recall@3.[^n8] The paper's own summary of that table is that the NL approach "is more effective at identifying the correct set of" candidate repositories.[^n9] The ablation isolates the directory step. Removing it, so the ranker is given the summaries of every file in the repository, is, in the authors' words, a case that "forces the LLM to solve a" needle-in-a-haystack problem.[^n16] The result: "with MRR plummeting by 54% and Recall@10 falling by 37%", and the ablated version "requires a 44%" rise in prompt tokens.[^n10][^n11]

My reading, not the paper's prose: the extracted Table 2 is garbled, but as I read its numbers, the tree router's MRR (0.67) is below both GitHub Copilot (0.77) and Cursor (0.72). The coverage gain seems to come with lower rank-one precision.

## Limits

- One system. The evaluation "was conducted on a single large-scale industrial Java project", so other languages and monolithic architectures are untested.[^n12]
- One model. "we use the gpt-4.1 model to ensure a fair comparison" for every LLM method, the paper's own included. How the tree behaves with other models, or with weaker summaries, is not measured here.[^n13]
- Unclear baselines. GitHub Copilot and Cursor are described as "two leading commercial systems". The text I read does not give their configuration, so the comparison with them cannot be checked for fairness.[^n14]
- Staleness is assumed, not tested. The tree is rebuilt after major releases rather than every commit, and the authors' justification is that "implementation changes rarely invalidate them". The update schedule is left "to improve efficiency and sustainability" in future work, and no staleness rate is reported.
- Summary quality is not measured on its own. The paper does not report how often a summary misstates a file's role. Its evidence is end-to-end, so a poor summary and a poor ranker cannot be told apart.
- Bug localization only. The claim that the tree "can power a new class of" developer tools is the authors' speculation in the Discussion. No such task was tested.[^n15]
- Top-down routing over a document tree did worse on financial filings. This is a different setting, and it is a different tree: a table-of-contents tree of SEC filings, traversed by an LLM with no embeddings. There the paper reports that "Vector-based agentic RAG achieves a 68% win rate over hierarchical" node-based systems, and it places the failure at section selection, where the LLM's choice "proved less effective than vector-based semantic matching."[^n17][^n18] The authors offer one explanation: their question set "emphasized specific factual retrieval," and a tree might do better on broad questions.[^n19] Whether it does is not tested in the text read; the paper's suggested direction is to "combine vector search with hierarchical reasoning," using embeddings to narrow the candidate nodes before the LLM traverses.[^n20]

## Related

- [[abstraction-gap-costed-bridging]] — the same mismatch between a query and its evidence at different levels of abstraction, handled on the query side with typed bridges; here the corpus is lifted to the query's level instead.
- [[coarse-to-fine-evidence-zoom]] — the coarse-then-fine order; the directory-filter ablation is recorded on that note.

[^n1]: arxiv-2512-05908 — "generating a high-quality, repository-level summary for each"
[^n2]: arxiv-2512-05908 — "For each source file, an LLM is prompted with"
[^n3]: arxiv-2512-05908 — "non-negligible computational cost"
[^n4]: arxiv-2512-05908 — "since they capture the high-level purpose and architectural role"
[^n5]: arxiv-2512-05908 — "a unified NL-to-NL reasoning task"
[^n6]: arxiv-2512-05908 — "against all directory-level summaries"
[^n7]: arxiv-2512-05908 — "our method achieves Pass@10 of"
[^n8]: arxiv-2512-05908 — "outperforms the Agentic RAG baselines on coverage metrics"
[^n9]: arxiv-2512-05908 — "approach is more effective at identifying the correct set of"
[^n10]: arxiv-2512-05908 — "with MRR plummeting by 54% and Recall@10 falling by 37%"
[^n11]: arxiv-2512-05908 — "the ablated version requires a 44%"
[^n12]: arxiv-2512-05908 — "was conducted on a single large-scale industrial Java project"
[^n13]: arxiv-2512-05908 — "we use the gpt-4.1 model to ensure a fair comparison"
[^n14]: arxiv-2512-05908 — "We use two leading commercial systems"
[^n15]: arxiv-2512-05908 — "Beyond bug localization, it can power a new class of"
[^n16]: arxiv-2512-05908 — "Removing the directory-level filtering step forces the LLM to solve a"
[^n17]: arxiv-2511-18177 — "Vector-based agentic RAG achieves a 68% win rate over hierarchical"
[^n18]: arxiv-2511-18177 — "effective than vector-based semantic matching"
[^n19]: arxiv-2511-18177 — "rather than broad document summarization where hierarchical traversal might excel"
[^n20]: arxiv-2511-18177 — "combine vector search with hierarchical reasoning"
