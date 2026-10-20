---
description: "Wide information seeking (collect every atomic item meeting criteria) fails on completeness at scale, not on finding single facts: item F1 nears 80 while exact-table success stays under 20."
aliases: ["wide information seeking", "WideSearch", "wide-context collection", "broad info-seeking"]
sources: ["doi-10-48550-arxiv-2508-07999"]
---
# Breadth-oriented information seeking

A class of questions asks not for one hard-to-find fact (deep search) or a synthesised narrative (deep research) but for *all* items meeting a set of criteria, arranged in a table. Wong et al. (2025) call it WideSearch and place it apart from both: DeepSearch targets "the 'I can't find it' problem", DeepResearch "the 'I can't write it well' problem", while this class is "the 'I could do it, but the sheer volume is overwhelming' problem".[^c1] Examples: every open Department of Justice attorney posting in a date range, or every company in a sector meeting revenue and growth thresholds.

## Mechanism: the unit of success is the whole set

Success is all-or-nothing: a task counts as completed only if the produced table "is a perfect match to the ground-truth table".[^c2] With thousands of atomic facts, one extra, missing or wrong item fails the task; the authors give the case of 5,000 pieces where 4,999 correct still fails.[^c3] The paper reports three granularities (table success, row F1, item F1) and Avg@N / Pass@N over repeated runs, so the gap between partial and complete correctness is itself measurable.

## What was measured

- Over 10 systems (single-agent, multi-agent, commercial) on 200 questions: most near 0% success, best 5%.[^c4]
- A single human working alone, with ample time and any tools, reached only 20%; cross-validation by several annotators approaches 100%.[^c5]
- Test-time scaling with one model: item-level F1 reaches close to 80 at 128 attempts, but table-level success stays below 20. The authors read this as: finding one fact is easy, exhaustive and exact retrieval is not.[^c6]
- Recall is "significantly lower than Precision across all test subsets", so omission, not wrong answers, dominates.[^c7]

## Named failure modes

1. Incomplete query decomposition: the intent is not split into a "comprehensive and complementary set of sub-queries", so constraints or scopes are missed.[^c8]
2. No reflection after an empty or thin result: agents abandon the search and answer from incomplete information or internal knowledge.[^c9]
3. Failure in evidence utilization: relevant content misread, or true but contextually inappropriate facts used.[^c10]
4. Hallucination when search returns nothing, plus basic tool-call and format errors (specialised research systems wrote long reports instead of the single required table).

The authors propose, but do not test, multi-agent parallel search with mutual cross-validation, modelled on how the ground truth itself was annotated.[^c11]

## Limits

- The benchmark is a table-of-facts format with objectively checkable cells; subjective or open-ended breadth is outside it (see [[subjective-contextual-incompleteness]]).
- The strict exact-match success criterion is a design choice; it inflates the headline gap, and the paper's own row and item F1 show much more partial success.
- The failure-mode taxonomy comes from manual case review; no ablation shows which mode accounts for how much loss.
- The multi-agent remedy is a suggestion, my reading of their conclusion, not a measured result. The 20% human figure is for single individuals, with no breakdown by effort.

## Related

- [[calibrated-completeness-stopping]] — a stopping rule for knowing when a collection is complete, the missing piece when recall lags precision
- [[unbudgetable-completeness]] — completeness as a demand that cannot be capped in advance
- [[relevance-completeness-divergence]] — relevant answers that are not complete answers
- [[dual-judge-completeness-recall]] — judging completeness as recall against a reference
- [[subjective-contextual-incompleteness]] — the open-ended counterpart where no exhaustive ground truth exists

[^c1]: doi-10-48550-arxiv-2508-07999 — "the "I could do it, but the sheer volume is overwhelming" problem"
[^c2]: doi-10-48550-arxiv-2508-07999 — "A task is considered completed if and only if the agent-generated Markdown table is a perfect match to the ground-truth table"
[^c3]: doi-10-48550-arxiv-2508-07999 — "even if you find 4,999 correct"
[^c4]: doi-10-48550-arxiv-2508-07999 — "Most systems achieve overall success rates near 0%, with the best performer reaching just 5%."
[^c5]: doi-10-48550-arxiv-2508-07999 — "the success rate for a single individual completing the task independently is merely 20%"
[^c6]: doi-10-48550-arxiv-2508-07999 — "even with 128 attempts, the table-level score only reaches a level below 20 points"
[^c7]: doi-10-48550-arxiv-2508-07999 — "Recall is significantly lower than Precision"
[^c8]: doi-10-48550-arxiv-2508-07999 — "comprehensive and complementary set of sub-queries"
[^c9]: doi-10-48550-arxiv-2508-07999 — "They tend to abandon the search after an initial failed attempt"
[^c10]: doi-10-48550-arxiv-2508-07999 — "Failure in Evidence Utilization."
[^c11]: doi-10-48550-arxiv-2508-07999 — "Multiple agents can conduct parallel searches and perform mutual cross-validation"
