---
description: "Monte Carlo tree search over reasoning steps, rewarded when the gold answer appears, yields many correct traces per question as training data, not as a test-time answering method."
aliases: ["MCTS trace generation", "search-generated CoT training traces", "tree-search data synthesis"]
sources: ["arxiv-2512-05336"]
---
# MCTS training-trace generation

Tree search is usually a way to spend inference compute (see [[tree-search-methods]]). PATHFINDER uses it offline. A search over reasoning steps generates candidate chains, and a smaller model is then fine-tuned on the chains that survive filtering. The stated reason is coverage: the search's ability "to diversify the search space, provide multiple" correct paths is what the authors want from it.[^c1]

The search runs over two alternating actions. Following ReAct, the authors "adopt a simplified action space consisting of subquestion generation and thought generation."[^c2] One action is a one-step thought (OST); the other is a sub-question that is sent to retrieval and answered (SGA). Branching comes from sampling at a non-zero temperature: "we set the number of sampling nodes to 2 for A1, and 3 for A2."[^c3] Nodes are selected by an upper-confidence rule, and a terminal OST node carries the reward, which is 1 when "answer is present in the prediction, and 0 otherwise."[^c4]

The reward is an outcome reward, so the search is steered toward reaching the answer, not toward sound steps. Every path that the reward marks correct is a candidate: "All the tree paths that lead to the correct answer are potential CoT train traces."[^c5] Those candidates are then cut down by the filters described in [[multi-hop-trace-error-score]]. The search budget is small: the authors "rollout the tree 12 times with max depth set to 12."[^c6] The generator is Qwen-2.5-72B-Instruct, and the targets are 7B and 9B models.

The contrast the paper draws is with inference-time search. Methods such as MCTS-RAG and Air-RAG explore several paths at answer time, and the authors note that "it comes at the cost of increased latency and computational complexity."[^c7] Their own approach "relies on fine-tuned models and hence these systems are orthogonal to ours,"[^c8] and they argue, in my paraphrase, that tree search is more useful as a source of training data than as a source of answers at test time. The same search, then, is placed on the training side and not on the answering side.

## Limits

- The reward checks containment: the gold answer must be present in the prediction. A prediction that contains the gold string along with other content scores 1, and so does a lucky route. The search cannot by itself separate sound traces from lucky ones; the filtering stage does that.
- No comparison is made with plain sampling at a matched budget. The baselines are DeepRAG's data generation and PATHFINDER's own filter ablations. Whether the tree produces more usable traces than twelve independent samples per question is not tested.
- The yield is reported only after filtering: 6852 traces from 8000 questions. The share of questions that yield any correct trace before filtering, and how that share changes with the rollout count, are not reported.
- The teacher is a 72B model and the students are 7B and 9B. The text does not isolate how much of the gain comes from the search, from the teacher, or from the filters.
- The action space (thought and sub-question) is designed for this retrieval format. Its transfer to other tasks, such as the open-ended questions this wiki is about, is not tested.
- Evaluation is on two in-distribution Wikipedia multi-hop sets and two out-of-distribution sets, all factoid. Nothing here shows the search generates useful traces for questions with no reference answer.

## Related

- [[tree-search-methods]] — the inference-time family (self-consistency, Tree of Thoughts); this note is the same kind of search spent on training data instead.
- [[minimal-edit-prompt-attack]] — MCTS used to search for input edits, rewarded by a margin; a different object and reward.
- [[multi-hop-trace-error-score]] — the filter applied to the traces this search produces.
- [[knowledge-distillation]] — training a smaller student on a larger model's outputs; the generator here is a larger teacher, and the paper does not test a distillation effect separately.

[^c1]: arxiv-2512-05336 — "diversify the search space, provide multiple"
[^c2]: arxiv-2512-05336 — "a simplified action space consisting of subquestion generation and"
[^c3]: arxiv-2512-05336 — "we set the number of sampling nodes to 2 for A1, and 3 for A2"
[^c4]: arxiv-2512-05336 — "answer is present in the prediction, and 0 otherwise"
[^c5]: arxiv-2512-05336 — "All the tree paths that lead to the correct answer are potential CoT train traces"
[^c6]: arxiv-2512-05336 — "rollout the tree 12 times with max depth set to 12"
[^c7]: arxiv-2512-05336 — "it comes at the cost of increased latency and"
[^c8]: arxiv-2512-05336 — "relies on fine-tuned models and hence these systems are orthogonal"
