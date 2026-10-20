---
description: "A research controller spawns child branches from the knowledge gaps a report still shows, expanding or pruning each under depth and branch budgets; gaps, not a fixed plan, set breadth."
aliases: ["deep tree of research", "DToR", "hierarchical deep research", "gap-driven branch expansion", "knowledge-gap explorer"]
sources: ["arxiv-2511-18303"]
---
# Gap-spawned research branches

A deep-research agent can be organised so that its next moves are children of a tree rather than steps of a fixed plan. Each node is one research pass: a query, retrieval, a running summary, and a reflection that proposes a follow-up query, "reflects to propose follow-up query".[^c1] After a node, an analyst chooses between EXPAND and PRUNE, "a decision EXPAND, PRUNE", based on the remaining depth and budget and on the quality of the node's report.[^c2] If the decision is to expand, a knowledge-gap explorer creates new child nodes aimed at the gaps the report still shows, one level deeper: it "materializes new RNs from this RN targeted to those gaps (depth+1)".[^c3] Branches that stop producing anything new are pruned, "Branches that stagnate are pruned", and a branch that reaches its depth limit or converges is written into a perspective report.[^c4]

The breadth at the root is a separate choice. A diversifier proposes several orthogonal perspectives on the user's question, and each perspective "seeds one branch with a budget: maximum depth, nodes per branch, and total branches".[^c5] So there are two sources of breadth. The perspectives are fixed before any evidence arrives. The gap-spawned children are set by what the evidence has not yet covered. The paper describes the whole controller as "a tree-of-search over (query, evidence, summary) states rather than over purely symbolic" thoughts.[^c6]

The queries that drive each node are built in a particular order. A node runs local retrieval before any web search, "local-first retrieval (before web) to reduce drift, hallucination, and surface domain priors".[^c7] Its second query is derived from the local summary, "local summary derived complementary query", so that the next search is steered by what the first one already returned rather than repeating it.[^c8] That the second query is meant to avoid repetition is my reading of the design; the paper gives it the aim of "comprehensiveness" and does not test it on its own.

## What was measured

Across 27 topics and 41 agents, the tree beats the single instance once a local corpus is present. The paper says that DToR "outperforms single-instance DR once a non-trivial local corpus is present (local100/local500), whereas", and that "at local0 the gap narrows and a strong backbone (gpt-oss120B) can close it."[^c9] In component ablations on the best configuration, over three topics, cutting tree depth, reflection loops and retrieval count each reduces performance, "with reflection proving most critical".[^c10] Removing web search also degrades quality, "confirming gap-triggered web complement adds value".[^c11]

So within this configuration the reflection that writes the next query carries more of the gain than the branching does. That is the paper's own ranking among the components it removed. The gap-triggered expansion itself is not removed alone in the text I read, so its separate contribution is not isolated.

## Limits

- The judges see only the report. The paper states that "LLM judges see only the final report text", and that "so the evaluation targets synthesis/reasoning quality rather than retrieval exposure".[^c12] A higher score shows a better report as read by five LLM judges. It does not show that the gaps were the right ones to chase.
- The gap is named by an LLM. Nothing in the text checks that the explorer's gaps are real gaps in the evidence. My inference: a wrongly named gap spawns a branch that costs budget and returns nothing, and the stagnation rule may catch that only when the branch fails to add material.
- The evaluation covers one domain. The topics are "27 expert-crafted topics spanning materials and devices", written by the authors, and the dry-lab check covers five tasks.[^c13]
- Better reports did not mean feasible proposals. The dry-lab section reports candidates that stack incompatible phases, and says "the agents ignored likely colloidal incompatibilities".[^c14] A deeper tree improved the report, not the chemistry.
- Cost is real. The single-machine run with gpt-oss120B "averages 19.6 h" for DToR, against about 30 minutes for a single instance.[^c15]

## Related

- [[evidence-gap-state]] — the single-loop version: evidence and gap are carried as state and the loop stops when the gap empties. Here the gap spawns separate child nodes, each with its own report, and the stop is a budget and a prune rule.
- [[tree-search-methods]] — the wider search families. This controller searches over research states with budgeted expansion and pruning, not over reasoning thoughts.
- [[reasoning-gap-driven-retrieval]] — also turns unmet evidence into follow-up retrieval, but from a per-type checklist rather than from a report's gaps.
- [[search-saturation-under-fixed-queries]] — the repeat failure that a query stream not steered by what was retrieved produces; the complementary query is one design aimed at it.
- [[llm-judge-validation-gap]] — the judge set here is not validated against experts in the text read, which is the general gap that note records.

[^c1]: arxiv-2511-18303 — "reflects to propose follow-up query"
[^c2]: arxiv-2511-18303 — "a decision EXPAND, PRUNE"
[^c3]: arxiv-2511-18303 — "explorer to materializes new RNs from this RN targeted to those gaps (depth+1) and updates remaining"
[^c4]: arxiv-2511-18303 — "Branches that stagnate are pruned"
[^c5]: arxiv-2511-18303 — "each seeds one branch with a budget: maximum depth, nodes per branch, and total branches"
[^c6]: arxiv-2511-18303 — "Conceptually, this is a tree-of-search over (query, evidence, summary) states rather than over purely symbolic"
[^c7]: arxiv-2511-18303 — "local-first retrieval (before web) to reduce drift, hallucination, and surface domain priors"
[^c8]: arxiv-2511-18303 — "local summary derived complementary query"
[^c9]: arxiv-2511-18303 — "outperforms single-instance DR once a non-trivial local corpus is present (local100/local500), whereas"
[^c10]: arxiv-2511-18303 — "with reflection proving most critical"
[^c11]: arxiv-2511-18303 — "confirming gap-triggered web complement adds value"
[^c12]: arxiv-2511-18303 — "so the evaluation targets synthesis/reasoning quality rather than retrieval exposure"
[^c13]: arxiv-2511-18303 — "27 expert-crafted topics spanning materials and devices"
[^c14]: arxiv-2511-18303 — "the agents ignored likely colloidal incompatibilities"
[^c15]: arxiv-2511-18303 — "averages 19.6 h"
