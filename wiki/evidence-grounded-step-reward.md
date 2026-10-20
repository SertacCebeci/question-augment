---
description: "A generative PRM scores each retrieval-augmented step for logic and evidential grounding; its verdicts pick step-level preference pairs that beat outcome-only rewards on five QA sets."
aliases: ["RAG process reward model", "step-level evidence grounding reward", "spurious-success filter", "grounded step verdict in tree search"]
sources: ["doi-10-48550-arxiv-2609-01658"]
---
# Evidence-grounded step reward

In retrieval-augmented reasoning a trajectory alternates reasoning with search calls, and an outcome reward scores only its final answer. The work's diagnosis is that such a reward cannot separate a sound path from a lucky one. Its wording: "spurious successes where flawed retrieval coincidentally produces the correct answer" are rewarded like sound ones.[^c1] The reward is also sparse: it is "derived solely from final-answer correctness", so feedback arrives only after the whole chain.[^c16] An early retrieval error then "propagates" through later steps, which an outcome reward has no way to detect.[^c14]

The remedy has two parts. The first is a verdict per step. The work trains a generative process reward model that outputs, for each step, a rationale and then a binary label, so its output is "with a correctness label and a rationale" rather than a bare scalar.[^c2] The label is meant to check two things at once, "both logical validity and evidential grounding".[^c3] A step can be valid reasoning from passages that do not support it, and the verdict is designed to mark that case. The generator is initialised from "DeepSeek-R1-Distill-8B".[^c15] The training labels come from a judge model that reads each step with the question and its preceding context.

The second part uses the verdict inside a value tree search over the policy's own sampled steps, not only as a score after the fact. A non-terminal node takes the binary verdict as its reward, "we directly use the binary prediction from" the PRM, and a terminal node takes the depth-discounted F1.[^c4] A node's value for ranking siblings combines the back-propagated descendant quality with the step's verdict. The paper's formula adds them with a weight; I read that weight from the formula, the text does not discuss it.[^c5] Where two siblings differ by more than a margin, "we assign the higher-valued node as the chosen" step and the other becomes the rejected one.[^c6] The resulting step-level pairs train the policy with direct preference optimisation. A step that is flagged as ungrounded loses value even when its descendants reach the right answer.

Two design choices are worth naming. The first is that a step labelled 0 does not discard the trajectory after it: because the policy "can recover" by reissuing a search, "a local failure (rt = 0) does not invalidate subsequent steps".[^c9] The second is that the PRM is queried on steps in a tree, so the same verdict serves both pair construction and the value of intermediate nodes.

The measured effect is modest. Removing the PRM term, so that pairs are built from depth-discounted F1 alone, lowers the average from 34.5 to 32.7 EM and from 44.1 to 41.9 F1, with the largest drops on multi-hop sets.[^c7] The authors read that pattern as evidence that "PRM supervision is particularly beneficial for multi-hop reasoning".[^c8] On recovered trajectories, where the first search missed the gold passage and a later one found it, the trained policy reaches higher final EM than Search-R1 on all five datasets.[^c13]

## Limits

- The labels come from QwQ-32B, chosen so the pipeline needs no paid API. The authors audit 500 samples against another frontier model and report "substantial agreement (κ = 0.6104) without systematic permissive bias".[^c10] A kappa of 0.61 leaves room for label error, and the policy is then optimised against those labels.
- The PRM is one 8B model, trained on 5,000 seed questions. On MuSiQue the method trails StepSearch by 1.3 EM, which the authors attribute to a "pool (5,000 seed questions, 15,877 pairs) than" a larger distilled corpus.[^c11]
- Bamboogle has only 125 test items, "yielding wide confidence intervals",[^c12] so its gap to the baselines says little. The paper's own significance test on that gap finds it indistinguishable from noise.
- All five benchmarks are short-answer QA (PopQA, HotpotQA, 2WikiMultiHopQA, Bamboogle, MuSiQue) by my reading. Whether a grounding verdict transfers to long-form answers is not tested.
- The grounding check is itself a model reading the retrieved passages. The text I read does not test whether a step labelled grounded is supported in the sense a human reader would accept (my inference).
- Step-level scorers can be gamed. The wiki's [[process-reward-model-hackability]] shows that step PRMs can be pushed up by style edits; this work does not test that failure.

## Related

- [[logic-only-reranking-drift]] — the same RAG setting, where a PRM that scores only logic degrades as candidates grow, and the grounded verdict does not.
- [[multi-hop-trace-error-score]] — the trace-level version of the spurious-success filter, which counts erroneous sub-steps after generation instead of penalising them inside the search.
- [[process-outcome-consistency-verification]] — the lucky-guess form of the same failure, checked by a product of outcome and consistency indicators.
- [[reflection-shaped-tree-backup]] — another dense per-node signal in tree search that replaces a sparse terminal outcome.
- [[process-reward-model-hackability]] — the gaming risk of step-level scorers.

[^c1]: doi-10-48550-arxiv-2609-01658 — "spurious successes where flawed retrieval coincidentally produces the correct answer"
[^c2]: doi-10-48550-arxiv-2609-01658 — "with a correctness label and a rationale"
[^c3]: doi-10-48550-arxiv-2609-01658 — "both logical validity and evidential grounding"
[^c4]: doi-10-48550-arxiv-2609-01658 — "we directly use the binary prediction from"
[^c5]: doi-10-48550-arxiv-2609-01658 — "aggregates the quality of descendant trajectories through back-propagation"
[^c6]: doi-10-48550-arxiv-2609-01658 — "we assign the higher-valued node as the chosen"
[^c7]: doi-10-48550-arxiv-2609-01658 — "performance from 34.5 to 32.7 EM and from 44.1"
[^c8]: doi-10-48550-arxiv-2609-01658 — "PRM supervision is particularly beneficial for multi-hop reasoning"
[^c9]: doi-10-48550-arxiv-2609-01658 — "a local failure (rt = 0) does not invalidate subsequent steps"
[^c10]: doi-10-48550-arxiv-2609-01658 — "substantial agreement (κ = 0.6104) without systematic permissive bias"
[^c11]: doi-10-48550-arxiv-2609-01658 — "pool (5,000 seed questions, 15,877 pairs) than"
[^c12]: doi-10-48550-arxiv-2609-01658 — "yielding wide confidence intervals"
[^c13]: doi-10-48550-arxiv-2609-01658 — "final EM than Search-R1 on all five datasets"
[^c14]: doi-10-48550-arxiv-2609-01658 — "allowing early errors to propagate through subsequent reasoning steps"
[^c15]: doi-10-48550-arxiv-2609-01658 — "DeepSeek-R1-Distill-8B"
[^c16]: doi-10-48550-arxiv-2609-01658 — "solely from final-answer correctness, it is sparse"
