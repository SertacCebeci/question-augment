---
description: "A search trajectory is scored by how many essential steps of a reference plan it accomplishes, in any order, so partial structure earns credit where a final-answer reward gives none."
aliases: ["path-centric reward", "reference-alignment score", "order-agnostic step coverage", "reference-plan coverage"]
sources: ["openalex-org-w7131909710"]
---
# Order-agnostic step coverage

In agentic retrieval-augmented generation the model interleaves reasoning with search actions, and a reward that reads only the final answer gives the same value to every trajectory that ends wrong. The Search-P1 work scores the structure of the trajectory as well. Offline, it generates candidate trajectories for each training question with a strong model, keeps the ones that reach a correct answer, and has an LLM vote out a reference path: "The voting identifies the minimal set of essential steps across successful trajectories, yielding a reference reasoning path."[^c1]

At training time the coverage term counts how many of those reference steps a rollout accomplishes, and "ncovered counts accomplished reference steps regardless of execution order."[^c2] The order is discarded on purpose. A rollout that reaches the same sub-goals in a different sequence earns the same coverage as one that follows the reference sequence, so the score measures what was established rather than the route taken.

Coverage is one of two tracks. The other, self-consistency, asks whether the model carries out the plan it declared before searching. The final path score takes the maximum of the two tracks rather than a weighted sum, and the stated reason is that a weak reference should not dilute a good self-declared plan, or the reverse: "the self-consistency track can dominate" when the reference is suboptimal.[^c3] Both tracks carry an efficiency ratio, included "to prevent reward hacking through excessive redundant steps".[^c4] As the extracted formula reads (my reading; the extraction garbles the fractions), the reference track multiplies the covered share of the reference by a second ratio over the total actions. The exact form of the efficiency term is not certain from the text.

The path term is one part of a total reward that also carries an outcome term and a format term: "where Rpath is the path-centric reward computed".[^c15] The reported best setting, λp = 0.3 and λa = 0.6, is described as one that "balances accuracy as the primary objective with" reasoning quality as a regularizer.[^c5]

What it was measured to do: on seven QA benchmarks the method reports "an average accuracy gain of 7.7" over Search-R1 and other baselines.[^c6] In the ablation on Qwen2.5-7B, removing reference alignment "causes a 5.3% accuracy drop",[^c7] and "Removing self-consistency results in a 3.1% decrease."[^c13] The authors also report that the trained policy reaches Search-R1's final accuracy "within 60 steps versus over 150".[^c8]

## Limits

- The reference is distilled by LLM voting over correct trajectories from a strong model. Coverage can only be as good as that reference: a consistent but wrong path, if the voters agree on it, becomes the thing that gets covered (my inference; the paper does not test a wrong-reference condition).
- Order-agnostic matching cannot tell a correct sequence of sub-goals from an incorrect one that touches the same steps. The paper's design accepts this; the text does not measure how often it matters.
- The step matching is judged by an LLM evaluator during training, and "Our dual-track scoring and soft outcome scoring rely on an external LLM evaluator during" training.[^c9] Swapping in Qwen3-8B "degrades by 3.2 points with lower outcome scoring", while the step-coverage agreement "remains robust even with the 8B evaluator".[^c14] So the step judgement is less sensitive than the outcome judgement, but the accuracy still moved.
- The path weight has a sweet spot. Too much weight induces "reward overfitting where path metrics improve but" accuracy drops.[^c11]
- The experiments use Qwen2.5 models at 3B and 7B, a fixed E5 retriever and a 2018 Wikipedia index: "we use the 2018 Wikipedia dump as the" knowledge source.[^c12] Nothing here tests the coverage idea on web search, on learned retrievers, or on tool use outside question answering.
- The gains are benchmark accuracy under one RL setup (GRPO with identical training across the RL baselines). They do not show that a coverage-shaped trajectory asks better questions in any human sense.
- Transfer, in the terms of this wiki: what survives outside RL training is the idea of scoring a line of inquiry against a set of essential sub-goals regardless of their order. What does not survive is the training loop and the LLM matching that makes the score computable. Whether a human asker or answerer benefits from being checked against such a set is not tested in this work.

## Related

- [[zero-variance-group-waste]] — the all-equal rollout groups that a final-answer reward leaves with no signal; a structure score is one way to rank rollouts inside such a group
- [[step-level-consensus-labels]] — step labels from the majority verdict of verifier runs, without a reference path to compare against
- [[reference-anchored-residual-credit]] — credit measured against a reference set, here a set of claims rather than a plan
- [[stagewise-judged-credit]] — denser credit over the stages of a long run, another answer to sparse terminal reward
- [[decomposer-planner-centric-rl]] — rewards a planner's sub-question structure apart from the answer; there the plan is a typed DAG, here a reference path scored by coverage
- [[signed-process-reward-stabilization]] — how a step-level signal is shaped before it enters the advantage

[^c1]: openalex-org-w7131909710 — "The voting identifies the minimal set of essential"
[^c2]: openalex-org-w7131909710 — "regardless of execution order"
[^c3]: openalex-org-w7131909710 — "the self-consistency track can dominate"
[^c4]: openalex-org-w7131909710 — "through excessive redundant steps"
[^c5]: openalex-org-w7131909710 — "balances accuracy as the primary objective with"
[^c6]: openalex-org-w7131909710 — "an average accuracy gain of 7.7"
[^c7]: openalex-org-w7131909710 — "causes a 5.3% accuracy drop"
[^c8]: openalex-org-w7131909710 — "within 60 steps versus over 150"
[^c9]: openalex-org-w7131909710 — "rely on an external LLM evaluator during"
[^c10]: openalex-org-w7131909710 — "degrades by 3.2 points with lower outcome scoring"
[^c11]: openalex-org-w7131909710 — "reward overfitting where path metrics improve but"
[^c12]: openalex-org-w7131909710 — "we use the 2018 Wikipedia dump as the"
[^c13]: openalex-org-w7131909710 — "Removing self-consistency results in a 3.1% decrease"
[^c14]: openalex-org-w7131909710 — "remains robust even with the 8B evaluator"
[^c15]: openalex-org-w7131909710 — "where Rpath is the path-centric reward computed"
