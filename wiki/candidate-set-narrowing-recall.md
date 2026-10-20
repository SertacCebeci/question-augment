---
description: "Narrowing a candidate set helps a choice only while the right option survives the cut: accuracy rises as distractors fall, but the gain is capped by the recall of the narrowing step."
aliases: ["recall-first retrieval", "shortlist recall trade-off", "candidate narrowing under distractor interference"]
sources: ["arxiv-2602-17046", "arxiv-2511-17208"]
---
# Candidate-set narrowing and recall

When a choice is made from a long list, every wrong item on the list is another chance for a wrong pick. The Instruction-Tool Retrieval paper states this as a hazard model: "Suppose the chance of a wrong tool call grows roughly with the number of irrelevant tools."[^c1] With N tools, one of them gold-valid, the chance of a correct pick is written as α/(α + β(N−1)), with α "capturing clarity of schema/exemplars and β the interference of distractors."[^c2]

Narrowing the list to m ≪ N items changes this in two ways at once. The distractor count falls, which raises accuracy. But the right item is kept only with some probability r, the recall of the narrowing step. The paper gives the combined value as r · α/(α + β(m−1)).[^c3] Two consequences follow from that expression. The first is that the gain depends on r: the paper concludes that "As m drops, accuracy rises unless recall r is too low".[^c4] The second is that the narrowing step should favour recall over precision. The paper's stated design is to "Prefer slightly higher recall for tools", leaving precision to a later stage: "precision is handled by the model and cross-encoder."[^c5]

The paper also adds a way back for an item that the cut has removed. The model self-rates whether the exposed tools suffice, and below a threshold a discovery sub-step widens the set.[^c6] Its ablation reports that the discovery fallback reduces cases where "correct tools are hidden from the agent."[^c7] A plain shortlist has no such step: an item dropped at the cut is never seen by the chooser, so the recall of the cut is the ceiling on what the chooser can do.

What the paper reports on its own benchmark is in the same direction. Tool accuracy for the monolithic baseline falls as the catalog grows, from 74% to 45%, while the narrowed system goes from 84% to 76%.[^c8] The gap widens with catalog size, which the paper reads as "consistent with interference model."[^c9]

A recall-first narrowing step also appears in conversational memory. The EMem-G system puts an LLM relevance filter over the retrieved memory units and deliberately keeps borderline items: it "keep[s] borderline candidates by biasing the LLM toward recall", and leaves the down-weighting to graph propagation and the QA step.[^c13] The filter is the largest single component on LoCoMo: "removing it reduces the overall LLM score from 0.780 to" 0.733 for EMem-G, and the authors call the filter "the most critical piece".[^c14][^c15] This is the same division of labour as the shortlist above, with the cut placed on the recall side. The text does not report the filter's recall at the cut, so the r in the formula stays unmeasured here as well. (my inference)

## Limits

- The hazard model is assumed, not fitted. The text gives no estimate of α, β or r, and calls the formula "a simple hazard model". What survives the transfer to other choice settings is the shape: a shortlist helps when distractor interference is large compared with the loss from dropping the right item. The paper's headline numbers cannot be recovered from the formula alone. (my inference)
- The benchmark is described as "controlled" and "internally consistent numbers".[^c10] It has 30 to 40 tasks per family, with validators, but the text gives no variance, seeds or significance test. The headline 95% token reduction rests on one production deployment described in a single paragraph ("In one production deployment with enterprise-grade").[^c11] The paper's "Internal Consistency Validation" checks its ratios against each other, not against an independent measurement.
- The trade-off is shown for tools with schemas. Whether it holds for answer options in a closed-choice question, whose distractors are built rather than retrieved, is not tested in the text.
- The retriever's recall at the cut is the critical unknown in the formula, and the text does not report it. Hidden-tool misses are reported as a miss-rate, but that does not give r directly.
- The paper's own limit applies: "Benchmarks may not capture adversarial or open-world settings."[^c12]

## Related

- [[max-distractor-similarity-difficulty]] — difficulty from how close the closest distractor is to the key, not from how many distractors there are; the two can combine.
- [[context-pollution-naive-tool-addition]] — a wider toolset is not free: adding search tools with no way to undo a bad retrieval lowered performance. The same worry runs the other way for the narrowed set.
- [[event-centric-memory-units]] — the memory units that the recall-biased EDU filter narrows; the filter's gain is measured on those units, not on triples.

[^c1]: arxiv-2602-17046 — "Suppose the chance of a wrong tool call grows roughly with the number of irrelevant tools"
[^c2]: arxiv-2602-17046 — "with α capturing clarity of schema/exemplars and β the interference of distractors"
[^c3]: arxiv-2602-17046
[^c4]: arxiv-2602-17046 — "As m drops, accuracy rises unless recall r is too low"
[^c5]: arxiv-2602-17046 — "Prefer slightly higher recall for tools"
[^c6]: arxiv-2602-17046 — "The model self-rates whether exposed tools suffice"
[^c7]: arxiv-2602-17046 — "correct tools are hidden from the agent"
[^c8]: arxiv-2602-17046
[^c9]: arxiv-2602-17046 — "consistent with interference model"
[^c10]: arxiv-2602-17046 — "Using a controlled benchmark with internally consistent numbers"
[^c11]: arxiv-2602-17046 — "In one production deployment with enterprise-grade"
[^c12]: arxiv-2602-17046 — "Benchmarks may not capture adversarial or open-world settings"
[^c13]: arxiv-2511-17208 — "keep borderline candidates by biasing the LLM toward recall"
[^c14]: arxiv-2511-17208 — "the LLM-based EDU filter is the most critical piece"
[^c15]: arxiv-2511-17208 — "removing it reduces the overall LLM score from 0.780 to"
