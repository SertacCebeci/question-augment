---
description: "Checking every extracted statement of a report against fresh web evidence, with Right/Wrong/Unknown labels, covers uncited claims and separates unverifiable from false."
aliases: ["active fact-checking", "statement-level uncited claim verification"]
sources: ["arxiv-2601-09688"]
---
# Active fact-checking with an Unknown label

Citation-based checks ask whether a cited source supports a claim, not whether the claim is true, and they skip uncited text. DeepResearchEval names three failures: reports lack citations, claims appear in uncited segments, and citation checks test support rather than correctness.[^c1]

The alternative is an agent that segments the report, extracts verifiable statements (numbers, events, dates, locations, people), searches the web for each, and labels it Right, Wrong or Unknown.[^c2] The agent sees the whole segment and the original task, so judgments are context-aware. Unknown "marks insufficient evidence, explicitly distinguishing unverifiable claims from errors."[^c3] The score is the Ratio of Right statements to all statements.[^c4]

The same paper pairs this with adaptive scoring: four general dimensions (Coverage, Insight, Instruction-following, Clarity) plus task-specific dimensions with normalized weights, and the authors report task-specific scores systematically lower than general ones across all systems.[^c5] Factual correctness is kept as a separate module because its verification needs external retrieval.[^c6]

## Limits

- The checker is itself an LLM agent with web search; its own errors and the web's coverage bound the labels, and no accuracy of the checker is established in the slices I read.
- Ratio counts Unknown in the denominator, so it conflates falsehood with thin evidence only partly; how Unknown should be priced is not argued.
- The task-specific gap is a reported result, not shown to reflect true quality rather than stricter rubrics (my inference).

## Related

- [[search-necessity-filter]] — the task-side filter of the same framework
- [[rubric-formation-gap]] — what to check is the bottleneck in rubric judging
- [[process-report-alignment-evaluation]] — another way of checking reports beyond surface quality

[^c1]: arxiv-2601-09688 — "citation-based verification checks whether a cited"
[^c2]: arxiv-2601-09688 — "Right denotes"
[^c3]: arxiv-2601-09688 — "marks insufficient evidence, explicitly distinguishing"
[^c4]: arxiv-2601-09688 — "the proportion of right statements over all statements"
[^c5]: arxiv-2601-09688 — "task-specific scores"
[^c6]: arxiv-2601-09688 — "we treat it"
