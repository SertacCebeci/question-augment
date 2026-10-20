---
description: "An RL reward for LLM exploration on knowledge graphs adds the fraction of ground-truth reasoning triplets whose subject, relation and object all appear in the generated reasoning text."
aliases: ["path-refined reward", "path reward R_path", "triplet-coverage reward", "reference-path recall reward"]
sources: ["doi-10-48550-arxiv-2602-21728"]
---
# Reference-path coverage reward

An outcome reward scores only where a reasoning chain ends. On a knowledge graph the chain is a sequence of relational triples, and a right answer can be reached through a path nobody would endorse. The Explore-on-Graph work keeps the outcome term and adds a second term that scores the path. Its outcome reward is computed "as reward signals, which can be computed programmatically" from the gold label.[^c1] The added term is "the path-based reward" of the form "the proportion of ground-truth reasoning steps successfully articulated in the generated thought process."[^c2]

The mechanism is a set-membership count. Each ground-truth triple (s, r, o) is checked for whether its three components all occur as substrings in the generated reasoning text, and the reward is "the ratio of fully matched triplets to" the number of triplets in the reference path.[^c3] The combined objective is an outcome term plus a weighted path term, with the weight a free ratio.[^c4]

The reference path is not given by the datasets in every case. The authors build it with a search-and-verify step: a breadth-first search over the graph between topic entities and answer entities within a hop limit, which "ensures high recall of potential reasoning chains," followed by an LLM check of each path, since "BFS may yield spurious paths that are" connected but unrelated.[^c5] The check asks "whether a path logically corresponds to the question's intent," so the reference is itself a model's judgment.[^c6]

What the authors measure is that the term matters. Removing it from the RL objective lowers the scores on both CWQ and WebQSP, which the authors summarise as "the path reward is critical to performance."[^c7] Reading Table 2, CWQ Hit@1 falls from 82.6 to 81.5 and CWQ F1 from 73.9 to 70.8 when the path term is removed.[^c8] The ratio itself is sensitive: their sweep of the weight shows that a small path weight hurts, and so does a large one.[^c9] They read the large-weight result as a reduced concern for answer correctness.[^c10]

The design is a dense, non-learned process signal. It differs from [[evidence-grounded-step-reward]], where a generative model judges each step, and it sits beside the terminal reward in the same family as [[two-tiered-reward-architecture]].

## Limits

- The score is a string containment test. A reasoning text that names a triple's subject, relation and object without using them in an inference counts as covered. The text does not test whether covered triples are used correctly (my inference from the matching rule).
- The reference paths carry the errors of their construction. The verifier is one LLM; I did not find in the sections I read a measure of how often it accepts a spurious path (my reading, not checked against the full text). Coverage of a wrong reference rewards the wrong route.
- The ablation is run on two of the five KGQA sets (CWQ and WebQSP) with two base models in the main table. The text I read does not show the gain transfers to open-domain questions, where no reference path exists.
- The ablation removes the path term from the combined objective; it does not isolate the path term as the only reward, so "critical" describes the combination, not the term alone (my inference).
- Gaming is untested. A policy optimised for triple mention could learn to list triples without reasoning, the step-scorer failure described in [[process-reward-model-hackability]]. The work does not test that.

## Related

- [[evidence-grounded-step-reward]] — the learned, per-step verdict version of the same aim: reward the grounded steps, not only the final answer.
- [[two-tiered-reward-architecture]] — a dense process term beside a terminal outcome reward, the same split as outcome plus path here.
- [[process-reward-model-hackability]] — why a step-level score that is easy to satisfy can be pushed up without better reasoning.

[^c1]: doi-10-48550-arxiv-2602-21728 — "as reward signals, which can be computed programmatically"
[^c2]: doi-10-48550-arxiv-2602-21728 — "is formulated to quantify the proportion of ground-truth reasoning"
[^c3]: doi-10-48550-arxiv-2602-21728 — "The reward is then calculated as the ratio of fully matched triplets to"
[^c4]: doi-10-48550-arxiv-2602-21728 — "Then we integrate a path-refined reward that provides additional"
[^c5]: doi-10-48550-arxiv-2602-21728 — "since BFS may yield spurious paths that are"
[^c6]: doi-10-48550-arxiv-2602-21728 — "The LLM is prompted to determine if a path logically corresponds"
[^c7]: doi-10-48550-arxiv-2602-21728 — "the path reward is critical to performance"
[^c8]: doi-10-48550-arxiv-2602-21728
[^c9]: doi-10-48550-arxiv-2602-21728 — "We hypothesize that reducing path signals"
[^c10]: doi-10-48550-arxiv-2602-21728 — "When the ratio is excessively increased, EoG may pay less attention to the correctness of the answers given the"
