---
description: "Instructions are kept as a population inside the RL loop, credited by the reward of the rollouts they condition, pruned, and refilled from reflection on failures."
aliases: ["INSPO", "online instruction optimization", "dynamic instruction population", "instruction-policy co-evolution"]
sources: ["arxiv-2512-01945"]
---
# Instruction-policy co-evolution

Reinforcement learning with verifiable rewards usually trains an agent under one fixed instruction, the protocol that says what role the agent plays and which tools it has. The paper's premise is that the best instruction for a base model is not known in advance, and may change as the policy improves.[^c1] Co-evolution keeps the instruction inside the training loop instead of fixing it before training. The method maintains "a dynamic population of instruction candidates"[^c2], and each rollout is conditioned on one candidate sampled from that population.

Reward is credited back to the candidate that produced it. The paper's formulation is that "The reward signals not only provide the policy gradients" but also attribute reward "to each instruction candidate based on the assignment."[^c3] Each candidate carries an importance weight, kept as a running average over recent steps. The population is pruned periodically by successive halving: "candidates via successive halving and evolve new instructions from high-performing ones."[^c4] Concretely, the bottom half by weight is removed.[^c5]

New candidates come from reflection on failure. A replay buffer prioritizes trajectories where the agent gave "incorrect or low-reward predictions," and an LLM-based proposer reads them and writes revised instructions. A proposed instruction is "verified via a low-cost proxy before merging into the" active population, and weak candidates are rejected.[^c6] The proxy in the appendix is a set of 200 samples.[^c7]

The reported gains come from the whole loop. With a constant population and no pruning, the average score was "which shows an average score of 33.0%". Adding periodic pruning and expansion raised it to 36.3%, and the full generate-and-verify loop was best.[^c8] The authors also state that "the online co-evolution of instruction and policy outperforms optimizing the instruction either before or" after training.[^c9] Two offline-style optimizers, one paraphrasing the instruction and one conditioning on instruction-reward history, gave the authors' verdict that "both optimizers are inadequate to yield meaningful gains."[^c10]

The case analysis gives a picture of what a fixed framing does. The static-instruction baseline issued one broad query that "mirrors the input question. It fails to retrieve the necessary" evidence, and then answered from its own knowledge.[^c11] The evolved instructions named failure modes such as "poor adherence to structure" and then required a step-by-step plan before tool use.[^c12]

Reading for question-asking (my inference, not the paper's claim): the mechanism is a feedback loop in which the framing of a search or an answer is revised from observed failures during the work, rather than chosen once beforehand. A fixed framing is then a bet on the average question. The paper does not test human asking, so this carries over only as a hypothesis.

## Limits

- The gains depend on the optimizer. The authors say the method "relies on a capable LLM-based optimizer for self-reflection"[^c13], and the main experiments used one model: "primarily studied using Gemini 2.5 Pro as the optimizer."[^c14]
- The tasks are narrow. The authors say their experiments "have primarily focused on search-based question answering tasks."[^c15] The component ablation was run on a single base model, "Ablation studies on the components of I NSPO on Qwen-2.5-3B."[^c16]
- The setting assumes a verifiable reward. The paper frames the reward as one where "the reward is typically defined via a" rule-based verifier with exact match.[^c17] Without such a reward the credit assignment that drives pruning has no clear signal, and the paper does not test one.
- The overhead is small but not zero: "marginal but non-zero computation overhead."[^c18]
- The text read does not show how sensitive the result is to the 200-sample proxy size, the importance-weight window, or the pruning fraction. Those are open here.

## Related

- [[evolutionary-prompt-search]] — also evolves a population of prompts with an LLM, but offline and scored on a dev set; co-evolution runs inside the RL loop and credits reward by the rollouts each instruction conditioned.
- [[reinforcement-prompt-selection]] — RL chooses among a fixed pool of prompt strategies; co-evolution evolves the pool itself.
- [[output-grounded-instruction-refinement]] — rewrites an instruction after scoring its output; co-evolution revises instructions from failure trajectories across many rollouts, inside training.

[^c1]: arxiv-2512-01945 — "those instructions may be suboptimal for the base model"
[^c2]: arxiv-2512-01945 — "a dynamic population of instruction candidates"
[^c3]: arxiv-2512-01945 — "The reward signals not only provide the policy gradients"
[^c4]: arxiv-2512-01945 — "candidates via successive halving and evolve new instructions from high-performing ones"
[^c5]: arxiv-2512-01945 — "the bottom half of instruction candidates, ranked by their importance weights"
[^c6]: arxiv-2512-01945 — "are verified via a low-cost proxy before merging into the"
[^c7]: arxiv-2512-01945 — "For verification, we set |DB | of 200 samples as a low-cost proxy"
[^c8]: arxiv-2512-01945 — "which shows an average score of 33.0%"
[^c9]: arxiv-2512-01945 — "the online co-evolution of instruction and policy outperforms optimizing the instruction either before or"
[^c10]: arxiv-2512-01945 — "both optimizers are inadequate to yield meaningful gains"
[^c11]: arxiv-2512-01945 — "mirrors the input question. It fails to retrieve the necessary"
[^c12]: arxiv-2512-01945 — "poor adherence to structure"
[^c13]: arxiv-2512-01945 — "relies on a capable LLM-based optimizer for self-reflection"
[^c14]: arxiv-2512-01945 — "primarily studied using Gemini 2.5 Pro as the optimizer"
[^c15]: arxiv-2512-01945 — "on search-based question answering tasks"
[^c16]: arxiv-2512-01945 — "Ablation studies on the components of I NSPO on Qwen-2.5-3B"
[^c17]: arxiv-2512-01945 — "the reward is typically defined via a"
[^c18]: arxiv-2512-01945 — "marginal but non-zero computation overhead"
