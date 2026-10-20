---
description: "Information foraging theory models a seeker following scent cues to information patches and reading inside a narrowed one; BookRAG imports this as narrow-then-reason, tested only in its own system."
aliases: ["information foraging theory", "IFT", "information scent", "information patches", "narrow-then-reason retrieval"]
sources: ["arxiv-2512-03413"]
---
# Information scent and patch navigation

Information foraging theory treats the search for information as animal foraging. The text describes it this way: users "follow cues, known as information scent (e.g., keywords or icons), to navigate between clusters of content, known as information patches (e.g., sections in handbooks)."[^c1] The seeker's aim is "to maximize the rate of valuable information gain while" keeping effort low, so each step is a decision either to stay in the current patch or to seek a new one.[^c2]

Two parts of this carry over to question answering. The first is the scent. The theory's example is an expert who first picks out key terms for the problem, and these terms "act as information scent" that point toward the likely sections.[^c3] The second is the order of the work: the seeker first picks promising patches and then reads inside them. The same division appears in the document-question-answering paper that imports the theory, where the retrieval "mimics foraging by using Selector to narrow down the search space via information scents and Reasoner to locate highly relevant evidence."[^c4]

In that system the scent is computed, not felt. An LLM step identifies the key entities in the question and links them to the knowledge graph; a Selector then keeps the subtrees of the document sections those entities point to, and only the retained content goes to the reasoning step.[^c5][^c6] What survives the transfer is the structure: narrow first, then reason inside the narrowed set. What does not survive, from the text read, is any claim about how people judge when to leave a patch. The theory's cost-benefit account of human search is not tested here.

The measured side is one ablation. A variant without the Selector keeps accuracy competitive but "incurs a prohibitive computational cost", reported as more than twice the tokens on Qasper.[^c7] So the narrowing is priced in tokens, and the paper reads its absence as a cost, not an accuracy loss.

## Limits

- The theory is an inspiration in this paper, not a tested model. The paper's experiments measure its own pipeline against baselines; no prediction of the theory about patch-leaving or scent strength is checked.
- The Selector result comes from one variant, one comparison on one dataset, and a single token ratio. The text I read does not show the accuracy of the narrowed set against a full search on the same questions.
- Narrowing can discard evidence. The slices I read do not report a case where the selected subtrees missed an answer that a wider search found. That is a gap in the reading, not a finding that it does not happen.
- The scent is an LLM extraction of entities, so its quality depends on that model. The paper does not report extraction errors in the text I read; I infer that they feed straight into what the Selector keeps.
- "Scent" here names a retrieval signal. Whether the human sense of a keyword's pull is the same thing is not shown and is not claimed.

## Related

- [[spreading-activation-retrieval]] — the same move in graph form: activation spreads from query entities to bridge documents; the Selector instead narrows to document subtrees.
- [[demand-typed-query-classification]] — decides which operators run; the Single-hop and Global Aggregation classes are the ones that rely on scent-based selection and filters.
- [[hierarchical-retrieval-interfaces]] — a retrieval agent that picks the granularity of each step, the choice of patch size seen from the tool side.

[^c1]: arxiv-2512-03413 — "scent (e.g., keywords or icons), to navigate between clusters of content, known as information patches"
[^c2]: arxiv-2512-03413 — "to maximize the rate of valuable information gain while"
[^c3]: arxiv-2512-03413 — "which act as information scent"
[^c4]: arxiv-2512-03413 — "mimics foraging by using Selector to narrow down"
[^c5]: arxiv-2512-03413 — "Extract, which employs an LLM to identify"
[^c6]: arxiv-2512-03413 — "It then retrieves all descendants of these targets to"
[^c7]: arxiv-2512-03413 — "incurs a prohibitive computational cost"
