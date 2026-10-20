---
description: "To build a training item that must use several linked things, a search over graph paths can score each path by the model's summed unfamiliarity with its links, then sample the item from the top paths."
aliases: ["UE-guided multi-API seed selection", "unfamiliarity-weighted path search", "uncertainty-weighted MCTS seed composition"]
sources: ["arxiv-2512-00380"]
---
# Uncertainty path seed composition

A single seed can be picked one at a time, but a question that has to use several linked things together needs a rule for choosing the combination. APIKG4Syn builds that combination from an API knowledge graph, in three steps. First the model is asked how unfamiliar each non-leaf node is: "UE for each non-leaf node, thereby quantifying the model" its own lack of knowledge of the node's members. The uncertainty of a child v under a parent u with relation ρ is "The negative logarithm of this probability", that is the negative log of the model's conditional probability of v given u and ρ.[^u1][^u2]

Second, Monte Carlo Tree Search runs over the graph with that uncertainty as the reward of each node. Selection uses UCB1, and the search is not anchored to one root: "each node is treated as a root once, aiming to explore a broader range of" API combination paths.[^u3] The reward enters the simulation and backup as a sum along a path, so a path accumulates value by passing through many nodes the model knows poorly.[^u4] The paper keeps "the top-5 highest-scoring paths".[^u5]

Third, the seed is not the whole path. From each path, "2–3 nodes are randomly sampled and" combined into one multi-API seed.[^u6] An LLM then writes the question and the code answer from that seed, and the graph supplies finer API detail to the code step.[^u7]

What the rule changes is the target of the question. The items are aimed at the stretches of an ecosystem where the answerer's own probabilities are thin, and the aim is computed from those probabilities rather than from a list of topics chosen by hand. That is my reading of the design; the paper does not argue the general point.

The measured result belongs to the whole pipeline, not to this step alone. Fine-tuning Qwen2.5-Coder-7B on the synthesized data gives a pass@1 of 25.00%, "outperforming untuned GPT-4o (17.59%)" on a HarmonyOS benchmark the paper builds.[^u8] The abstract states that "Ablation studies also confirm the necessity and effectiveness of each component in" the framework.[^u9]

## Limits

- The ablations are cited in the abstract but were not read in detail here. How much of the gain comes from the MCTS composition, as against the graph itself or the single-API seeds, is not established by what I read. No comparison with randomly sampled node combinations was found in the sections read.
- The uncertainty is the same model's own conditional probability, and the paper treats it as a measure of unfamiliarity. A model can be confidently wrong about an API relation, in which case the path is never chosen. Whether that happens here is not tested (my inference, the same caveat as in [[loss-based-seed-selection]]).
- The sum favours long paths. How path length is bounded was not checked in the sections read.
- One framework is the case study: "For evaluation, we select HarmonyOS".[^u10] The graph is built from one SDK's documentation. Transfer to graphs whose links are noisier or less documented is untested.
- The seed does not fix the item. An LLM writes the question from it, and deduplication and validation run afterwards, so the composition is only as faithful as that generation step (see [[seed-property-inheritance]]).
- The paper reports one composition ratio of single-API to multi-API items as best in its setting. That is a finding of this setting and is not carried into this note.

## Related

- [[loss-based-seed-selection]] — the single-seed version of the same score: a model's own uncertainty chooses the seed; here it is summed along a graph path
- [[student-in-the-loop-synthetic-generation]] — the loop in which the student's state, not the graph, picks the seeds a teacher expands
- [[tree-search-methods]] — the search family that Monte Carlo Tree Search belongs to
- [[reflection-shaped-tree-backup]] — another way a node reward enters the MCTS backup, here from a critic rather than an uncertainty
- [[off-graph-path-selection]] — choosing graph paths by a predictor's gain rather than by the model's own uncertainty
- [[seed-property-inheritance]] — why a seed's properties reach the generated item at all

[^u1]: arxiv-2512-00380 — "The negative logarithm of this probability"
[^u2]: arxiv-2512-00380 — "UE for each non-leaf node, thereby quantifying the model"
[^u3]: arxiv-2512-00380 — "each node is treated as a root once, aiming to explore a broader range of"
[^u4]: arxiv-2512-00380 — "In our implementation, the reward for each node is the uncertainty estimation from Section 2.1"
[^u5]: arxiv-2512-00380 — "to identify the top-5 highest-scoring paths"
[^u6]: arxiv-2512-00380 — "2–3 nodes are randomly sampled and"
[^u7]: arxiv-2512-00380 — "LLMs generate appropriately tailored API-Oriented problem"
[^u8]: arxiv-2512-00380 — "outperforming untuned GPT-4o (17.59%)"
[^u9]: arxiv-2512-00380 — "Ablation studies also confirm the necessity and effectiveness of each component in"
[^u10]: arxiv-2512-00380 — "For evaluation, we select HarmonyOS"
