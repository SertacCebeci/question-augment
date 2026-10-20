---
description: "Retrieved knowledge is filtered twice before an answerer reads it: a grounding filter drops elements the query never mentions, then a pruning step drops those the answer does not need."
aliases: ["GRASP", "query-grounded subgraph pruning", "answer-useful pruning", "grounded retrieval and selective pruning"]
sources: ["arxiv-2512-20136"]
---
# Grounded selective pruning

Retrieval hands an answerer more than it needs. A similarity search returns what sits near the query, and expanding the hits over graph edges adds facts that are related but unused. Park et al. name the first defect directly: similarity-only retrieval can "lack fine-grained alignment or include knowledge that may not be useful to answer the question".[^c4]

Grounded selective pruning is a filter placed between retrieval and generation, in two stages.

The first stage is grounding, and it asks whether an element is about the query at all. Each retrieved triplet is scored by an off-the-shelf multimodal grounding model against the query's own audio or visual content, and triplets whose presence score falls below a threshold are dropped. The paper's wording is that the grounding step drops triplets "not appearing in the query".[^c1] Where both audio and video are present, the two presence scores are added and compared against one threshold: "we simply sum their presence scores".[^c2]

The second stage asks whether an element bears on the answer. A lightweight language model produces a binary mask over the grounded triplets "under a conservative keep-or-drop policy".[^c3] Its stated target is to "prune triplets that do not contribute to answering the" question.[^c5] Only the surviving subgraph is serialised into the answering model's context.

The motivation is an example in which the question is "What instrument is being played?". Only the instruments present are useful, and "the remaining triplets mostly become noise for the MLLMs".[^c6] The general claim in the introduction is the same: facts that do not contribute to the answer "introduce noise in the MLLM context".[^c7]

What transfers, in my reading and not as a result of the paper: the relevance test on retrieved material has two different criteria, and only the second one needs the answer in view. Grounding can be checked against the question alone; usefulness can only be judged against what would answer it, so the paper hands that judgement to a separate model rather than to the answerer.

## What was measured

The one ablation on this stage is on VALOR, with Qwen2.5-Omni as the answering model. The text-only control, where the graph is retrieved in a shared space without modality-wise search, gets a modest gain from pruning alone: "Using GRASP improves faithfulness via fine-grained pruning, yet the initial graph retrieved" from a weakly aligned space gives "only modest improvements".[^c8][^c9] Pruning on top of a better candidate set does more: "Combining both offers the largest gain".[^c10] The reading I take from this is that pruning removes noise but does not rescue candidates that were never aligned to the query.

The appendix reports a threshold sweep. Moderate grounding-based pruning is beneficial, and overly aggressive thresholds "remove many triplets that still carry useful evidence".[^c11]

## Limits

- One ablation, on one benchmark and one answering model. The pruning-only row is the only isolation of this stage that I read.
- The only metric in the ablation is the Model-as-Judge score; "faithfulness" is the authors' word for what that score is taken to show. No separate faithfulness measure is reported in the parts read.
- The second stage is a language model's keep-or-drop mask. How often it removes an element the answer needed (a false drop) is not counted in the parts read; "conservative" is asserted, not measured.
- The thresholds are set per benchmark and held fixed within it. Transfer to other modalities, or to text-only settings where the grounding criterion would have to be replaced, is not tested.
- Whether pruning helps an answerer that already knows the answer is not tested here. The noise-damage result in [[parametric-knowledge-gates-retrieval-noise-damage]] suggests the benefit may depend on how much the answerer leans on the context; that is another paper's setting, and applying it here is my inference.

## Related

- [[modality-wise-retrieval]] — the step upstream, which supplies the candidates this filter prunes; the paper's ablation finds the two together give the largest gain
- [[parametric-knowledge-gates-retrieval-noise-damage]] — irrelevant documents hurt most where the answerer is weak; a relevance filter is one remedy aimed at the same noise
- [[distractor-similarity-reasoning-inflation]] — distractors that resemble the question do the most harm, and the grounding stage targets exactly resemblance to the query
- [[evidence-admission-gate]] — decides whether a whole retrieved memory enters the context; pruning decides which parts of an admitted subgraph do
- [[evidence-forgetting-rate]] — separates using retrieved evidence from retrieving it; pruning changes what is presented to the answerer, not what was found

[^c1]: arxiv-2512-20136 — "not appearing in the query"
[^c2]: arxiv-2512-20136 — "we simply sum their presence scores"
[^c3]: arxiv-2512-20136 — "under a conservative keep-or-drop policy"
[^c4]: arxiv-2512-20136 — "fine-grained alignment or include knowledge that may not be"
[^c5]: arxiv-2512-20136 — "to prune triplets that do not contribute to answering the"
[^c6]: arxiv-2512-20136 — "triplets mostly become noise for the MLLMs"
[^c7]: arxiv-2512-20136 — "introduce noise in the MLLM context"
[^c8]: arxiv-2512-20136 — "Using GRASP improves faithfulness via fine-grained pruning, yet the initial graph retrieved"
[^c9]: arxiv-2512-20136 — "yielding only modest improvements"
[^c10]: arxiv-2512-20136 — "Combining both offers the largest gain"
[^c11]: arxiv-2512-20136 — "overly aggressive thresholds remove many triplets that still carry useful evidence"
