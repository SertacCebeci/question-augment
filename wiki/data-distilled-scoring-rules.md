---
description: "A scoring rule is a set of aspect-and-rubric pairs that can be searched from labelled data, so a judge's criteria are fitted to the labels rather than written by hand or self-proposed."
aliases: ["learned scoring rules", "rule distillation", "learned evaluation principles", "data-derived rubrics"]
sources: ["arxiv-2512-01958"]
---
# Data-distilled scoring rules

A judge can be given a scoring rule instead of an open instruction to "evaluate this." The paper defines a rule as a set of sub-rules, and each sub-rule as a pair: an aspect of evaluation (clarity, coherence, relevance) and a rubric, the detailed scoring guideline for that aspect. A sub-rule is one evaluation criterion, and the aspects are meant to be independent of one another.[^c1] What makes the rule a learned object is where it comes from. The authors do not write it: their stated focus is "learning scoring rules from data."[^c2]

The search is a Monte Carlo tree search whose states are candidate rule sets. The root is the empty set.[^c3] An action either adds a sub-rule proposed by an LLM, or rewrites the rubric of a sub-rule already in the set, and rewrites are limited to two directions, stricter or more lenient.[^c4] The reward of a state is how well an LLM evaluator prompted with those rules reproduces the labels on a dataset, with the dataset and the LLM together serving as the environment.[^c5] Scoring every candidate over the whole dataset is costly, so the paper treats sub-rules as independent and gives them equal weight in the predicted score.[^c6][^c7] Selection uses the UCT formula down the tree. The search runs in two stages: an expansion stage that only adds sub-rules to explore aspects, and then, once a threshold of sub-rules is reached, a refinement stage that only rewrites rubrics to exploit what was found.[^c8]

The grain of the search state is part of the claim. The paper argues that searching over reasoning text is inefficient because "token-level states create an extremely large search space",[^c9] and that searching at the rule level gives a "rule-level, substantially reducing complexity" search.[^c10] The transferable point is that the size of a search space depends on what counts as one state. This is the authors' argument; the sections read do not run a token-level search for comparison.

What the search recovered is checked in part. On ASAP essays, the distilled aspects were compared with the expert-defined ones using precision, recall, Jaccard similarity and a hypergeometric test, and the paper reports: "Our method achieved high precision and recall", with the one miss being the conventions aspect.[^c11] The reward also matters to what is found. A pairwise reward variant produced sub-rules that are "more dispersed",[^c12] and the paper reads its own dataset-level reward as the one that gives "stable and unified rules".[^c13]

The motivation is an exploratory run. Qwen-7b, prompted to propose evaluation principles and score essays, produced principles that were "highly dispersed",[^c14] and the authors read the gap to human scores as "suggesting that the misalignment primarily stems from differing evaluation standards."[^c15] That is the authors' reading of one model on one dataset.

Learned rules can also be fed back as the evaluator's instruction. The Chain-of-Rule variant "prepend[s] the learned rules to the task instructions" without any training,[^c16] using the top five rules by average reward.[^c17] Against plain scoring and chain-of-thought prompting, the paper reports gains across model sizes, most for the 7B model on the essay task, "where it significantly outperforms CoT and Scoring for smaller".[^c18] The authors name the limit themselves: Chain-of-Rule "may not fully resolve misalignments, especially if the LLMs for" distillation and application differ.[^c19] In this setup the distiller is DeepSeek-v2.5,[^c20] and the trained evaluator is a different model.[^c21] A second step, reinforcement learning on the rule-prompted evaluator, is a separate mechanism and not part of this note.

One lesson from the ablations concerns which trajectories to learn from. Fine-tuning on high-reward search trajectories hurt most, and the authors explain it: "high-reward data often focuses on easily evaluable samples, introducing bias."[^c22]

## Limits

- The alignment check against expert aspects is reported for the essay task only. For the other tasks the paper argues that the learned aspects fit "aligning with common expectations",[^c23] which is argument, not a measured overlap.
- The gain is not uniform. On Amazon, Chain-of-Rule shows "limited improvement across other parameter sizes."[^c24]
- The ablations vary the reward and the training stage. In the sections read, no run replaces MCTS with a simpler search over rules, such as sampling rule sets and keeping the best. What the tree search buys is therefore not isolated (my reading).
- The rule-level complexity advantage is asserted, not measured against a token-level search (my reading).
- The rules are written by an LLM, so their wording inherits that model's biases. Whether a different distiller changes the rules was not tested here (my inference).
- Training ran one epoch on one model. I found no variance across seeds in the sections read (my reading).

## Related

- [[rubric-formation-gap]] — the same split between writing criteria and applying them; here the criteria are fitted to labels by search rather than proposed by a model or written by experts
- [[expert-report-derived-atomic-rubrics]] — criteria taken from expert text, another source of the same object
- [[weight-stratified-criterion-pass-rate]] — a reminder that an averaged criterion score can hide which criteria fail

[^c1]: arxiv-2512-01958 — "sub-rule encapsulates a specific evaluation criterion"
[^c2]: arxiv-2512-01958 — "learning scoring rules from data"
[^c3]: arxiv-2512-01958 — "The initial state is the empty set"
[^c4]: arxiv-2512-01958 — "modifications to two directions: stricter or more"
[^c5]: arxiv-2512-01958 — "LLM as the environment"
[^c6]: arxiv-2512-01958 — "Evaluating each new state across the dataset is computationally costly"
[^c7]: arxiv-2512-01958 — "dependent sub-rules have equal weight"
[^c8]: arxiv-2512-01958 — "the action space switches to Amod for refining existing sub-rules"
[^c9]: arxiv-2512-01958 — "token-level states create an extremely large search space"
[^c10]: arxiv-2512-01958 — "rule-level, substantially reducing complexity"
[^c11]: arxiv-2512-01958 — "Our method achieved high precision and recall"
[^c12]: arxiv-2512-01958 — "sub-rules from PAR are more dispersed"
[^c13]: arxiv-2512-01958 — "computation in identifying stable and unified rules"
[^c14]: arxiv-2512-01958 — "we observed highly dispersed principles"
[^c15]: arxiv-2512-01958 — "suggesting that the misalignment primarily stems from differing evaluation standards"
[^c16]: arxiv-2512-01958 — "We prepend the learned rules to the task instructions"
[^c17]: arxiv-2512-01958 — "the top 5 as scoring rules"
[^c18]: arxiv-2512-01958 — "where it significantly outperforms CoT and Scoring for smaller"
[^c19]: arxiv-2512-01958 — "it may not fully resolve misalignments, especially if the LLMs for"
[^c20]: arxiv-2512-01958 — "we utilize DeepSeek-v2.5 to assist in distillation"
[^c21]: arxiv-2512-01958 — "RuAE training is based on"
[^c22]: arxiv-2512-01958 — "high-reward data often focuses on easily evaluable samples, introducing bias"
[^c23]: arxiv-2512-01958 — "aligning with common expectations"
[^c24]: arxiv-2512-01958 — "limited improvement across other parameter sizes"
