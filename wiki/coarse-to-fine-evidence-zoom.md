---
description: "Answer in two passes: locate the query-relevant span at coarse resolution, then re-inspect only that span at finer resolution, rewarding spans whose zoomed view supports the answer."
aliases: ["temporal zoom-in", "coarse-to-fine grounding", "localize-then-zoom answering", "zoom-in accuracy reward"]
sources: ["arxiv-2512-14273", "doi-10-48550-arxiv-2506-04585", "arxiv-2512-05908", "arxiv-2511-23477", "arxiv-2511-20460", "arxiv-2511-19652"]
---
# Coarse-to-fine evidence zoom

A model with a fixed input budget faces a trade-off. If it spreads the budget thinly over a long source, the fine detail that answers the question is lost. If it concentrates the budget, it must already know where to look. The Zoom-Zero paper resolves this with two passes. A coarse pass first "predicts query-conditioned intervals" and then a fine pass takes "only the localized segments at higher per-frame token resolution" as input.[^z1] The authors' motivating case is a coarse pass that "may overlook the small visual detail “29%” due to low-resolution tokens", so the right answer appears only when the model first finds the segment and then looks at it closely.[^z2]

The idea is a response to the budget problem. The paper states that "limited context budgets compel models to depend on coarse-grained representations, which overlook the" fine detail needed for accurate answers, and that this is worse on long videos.[^z3]

The training side adds a reward. Each rollout localizes a segment and answers, and a zoom-in accuracy reward checks the localized span. The paper gives it two roles: "verifying that grounded segments contain requisite evidence to answer the query", and dynamically reallocating context by zooming into key frames at higher resolution.[^z4] My reading is that the reward credits a localization only when the zoomed span actually supports the answer. A window that overlaps the reference timestamps but does not let the answer be recovered is penalised less than one that does; the paper does not separate those two cases in its experiments.

A measurement in another setting cuts against the premise that locating first helps. On scientific figures, a vision-language model asked to localize its evidence and then reason does worse than one that reasons over the whole figure: "Model performance deteriorates when localizing before reasoning."[^z11] A located panel does help, but as an input the model did not have to choose: a visual hint showing the relevant panel alone is better again than a textual hint naming it, "They improve even further."[^z12] My reading, not the paper's claim: the coarse-to-fine gain may depend on whether the located span can be read directly, as a segment of a timeline can. Where localization is a choice among panels, the extra step can cost accuracy. See [[evidence-localization-gap]].

The same order shows up on code, over a tree of text summaries rather than a video or a figure. In a multi-repository bug-localization study, the LLM first narrows the search to candidate directories and then ranks only the files inside them.[^z13] Removing that narrowing, so the ranker is given the summaries of every file in the repository, is reported to cost "with MRR plummeting by 54% and Recall@10 falling by 37%", and the ablated version "requires a 44%" increase in prompt tokens.[^z14][^z15] That ablation removes only the coarse step, so the drop is attributed to it. The study runs on one industrial system with one model, so this is one measured drop for one coarse filter, not a rate. See [[nl-summary-tree-index]].

## What was measured

- In the paper's ablation the zoom reward gives "larger gains in accuracy (+1.9) on ReXTime over GRPO", and with token-selective credit assignment (the span-restricted credit described in [[confidence-first-segmented-credit-rl]]) both components together report ReXTime accuracy and mIoU gains of "+3.7" and "+4.0" (the paper's table, relative to the baseline as I read it).[^z5][^z6]
- At inference, the coarse-to-fine pass without retraining gives "an average 6.4% improvement on long-video benchmarks" in the paper's summary.[^z7]
- The cost is modest: "representing a 1.15× increase in training time per step" over the same training without the zoom.[^z8]

## Limits

- The paper runs one round of zoom. "Our current approach performs only a single round of zoom-in during both training and inference."[^z9] Iterated or recursive zoom was not tested, so whether the gain compounds is unknown.
- The zoom is fixed rather than chosen. "Another limitation is that the zoom-in process is enforced rather than adaptive."[^z10] A model that could decide when a second look is worth its cost was not built.
- The 29% example is one illustrative case in Figure 1. The paper does not measure how often a coarse pass misses such a cue, so the mechanism is shown by example, not by rate.
- All results are on video grounded QA and long-video multiple choice. Whether the same two-pass gain holds for text passages or images is my inference, not tested here.
- The gains are measured against GRPO-trained baselines on specific benchmarks; the effect sizes are a few points and the paper reports single runs in the text I read.
- A later video paper runs the zoom iteratively. Its loop feeds each observation back into the reasoning: "Each manipulation produces new observations that are fed back into the model for continued reasoning."[^z16] The turn cap of five is set from the data, "corresponding to the longest reasoning trajectory in the dataset."[^z17] Its ablations vary which operations are enabled, not the number of turns, so the compounding question remains open in the text I read.
- A remote-sensing pilot tests a recursive zoom, on still images rather than video. Its hierarchical policy "selected region into a 3 × 3 grid and continues to zoom in" until evidence is found, and in a pilot on 2,000 question–image pairs with a 0.5B backbone, "the hierarchical policy consistently yields superior" end-to-end accuracy to a single coarse grid and to fixed fine tiles.[^z18][^z19][^z20] The pilot keeps only the top-1 patch and the depth is not varied, so it does not settle whether more rounds help for video.
- Correct localization does not guarantee the answer. In the same paper's failure analysis the search "correctly isolates the target region", and the answer can still be wrong: "yet the base VLM still produces an incorrect answer." The authors read this as "imposed by the backbone rather than the search policy."[^z21][^z22][^z23] Their counting gain is also smaller, which they attribute to the fact that "correct localization does not always lead to correct answers."[^z24]
- A gigapixel pathology paper runs the look-again step as a loop of up to twenty model-chosen crops, each informed by the earlier ones. Its step count was swept from 1 to 25, and "across all tasks is highest at 20 iterations."[^z25] That is a different object from this note's single fixed zoom, and it does not separate the coarse pass from the iterated one; see iterative-crop-navigation.


## Related

- [[evidence-forgetting-rate]] — counts answers wrong even though the golden evidence was retrieved; zoom targets a related case where the evidence is present but too coarse to read.
- [[groundedness-gated-tool-routing]] — also decides where to look before answering, by whether the target is grounded rather than by resolution.
- [[confidence-first-segmented-credit-rl]] — the span-restricted credit used in the same paper to train grounding and answer tokens separately.
- [[evidence-localization-gap]] — the figure-side result: localizing before reasoning lowered accuracy on claim verification, the reverse of this ordering's premise.
- [[nl-summary-tree-index]] — the code-side case: the same coarse-then-fine order over a tree of file and directory summaries, with the coarse pass ablated.
- [[annotated-step-grounding-reward]] — the multi-turn video version of this loop, where each zoom or localization call is scored against annotated segments and boxes rather than by the final answer.

[^z1]: arxiv-2512-14273 — "query-conditioned intervals, followed by a fine-grained zoom-in that takes as input only the localized segments"
[^z2]: arxiv-2512-14273 — "the coarse pass may overlook the small visual detail “29%” due to low-resolution tokens"
[^z3]: arxiv-2512-14273 — "limited context budgets compel models to depend on coarse-grained representations, which overlook the"
[^z4]: arxiv-2512-14273 — "verifying that grounded segments contain requisite evidence to answer the query"
[^z5]: arxiv-2512-14273 — "larger gains in accuracy (+1.9) on ReXTime over GRPO"
[^z6]: arxiv-2512-14273 — "ReXTime accuracy (+3.7) and mIoU (+4.0)"
[^z7]: arxiv-2512-14273 — "resulting in an average 6.4% improvement on long-video benchmarks"
[^z8]: arxiv-2512-14273 — "representing a 1.15× increase in training time per step"
[^z9]: arxiv-2512-14273 — "Our current approach performs only a single round of zoom-in during both training and inference."
[^z10]: arxiv-2512-14273 — "Another limitation is that the zoom-in process is enforced rather than adaptive."
[^z11]: doi-10-48550-arxiv-2506-04585 — "Model performance deteriorates when localizing before reasoning"
[^z12]: doi-10-48550-arxiv-2506-04585 — "They improve even further"
[^z13]: arxiv-2512-05908 — "against all directory-level summaries"
[^z14]: arxiv-2512-05908 — "with MRR plummeting by 54% and Recall@10 falling by 37%"
[^z15]: arxiv-2512-05908 — "the ablated version requires a 44%"
[^z16]: arxiv-2511-23477 — "Each manipulation produces new observations that are fed back into the model for continued reasoning"
[^z17]: arxiv-2511-23477 — "corresponding to the longest reasoning trajectory in the dataset"
[^z18]: arxiv-2511-20460 — "selected region into a 3 × 3 grid and continues to zoom in"
[^z19]: arxiv-2511-20460 — "the hierarchical policy consistently yields superior"
[^z20]: arxiv-2511-20460 — "backbone for all subsequent pilot studies on this subset"
[^z21]: arxiv-2511-20460 — "search correctly isolates the target region"
[^z22]: arxiv-2511-20460 — "yet the base VLM still produces an incorrect answer"
[^z23]: arxiv-2511-20460 — "imposed by the backbone rather than the search policy"
[^z24]: arxiv-2511-20460 — "correct localization does not always lead to correct answers"
[^z25]: arxiv-2511-19652 — "across all tasks is highest at 20 iterations"
