---
description: "A planner chooses one named reasoning strategy (self-reflection, decomposition, validation) before each chain-of-thought step and injects it as a prompt the reasoner is trained to follow."
aliases: ["rSIM", "reinforced strategy injection", "planner-driven strategy injection", "leader-follower strategy injection"]
sources: ["arxiv-2512-08300"]
---
# Step-level strategy injection

A planner that sits beside a reasoning model chooses, before each step of a chain of thought (CoT), one strategy from a fixed menu and injects it into the context as a prompt. The reasoner then writes the next step under that instruction. The menu in the rSIM paper is nine human-designed moves: "commonly used strategies: self-reflection, decomposition, deliberative thinking, validation, summarization, prioritization, continuation, sub-planning," plus a termination option.[^c1] At each step the planner receives "the question and the current reasoning steps" and selects one of the nine.[^c2] The strategies are "expressed as prompts," so the reasoner receives them as ordinary context rather than as a change to its procedure.[^c3]

The planner is the leader and the reasoner the follower in a leader-follower multi-agent RL setup. The paper states that "the base LLM serves as the reasoner, responsible for generating the next reasoning step based on the planner" selected strategy.[^c4] Two rewards shape the pair. The planner is penalised by "ratio of the most frequently selected strategy," which pushes it away from repeating one move.[^c5] The reasoner earns a term that "is the ratio of reasoning steps that follow" the given plan.[^c6] So the training signal rewards both varied selection and actual compliance with the injected step.

The motivation is a correlation between the number of strategies in a chain and its accuracy. The paper counts strategies by keyword: "By detecting key words, we" tally them in each answer.[^c7] It reports "there exists a positive correlation between the number of strategies and the accuracy."[^c8] Small base models with no such strategies gain little from reinforcement learning alone: "and Qwen2.5-0.5B, which lack inherent reasoning strategies (i.e., strategy count is 0), cannot be" usefully trained this way.[^c9]

The reported gains come in two forms. Jointly trained, Qwen2.5-0.5B with a planner reaches "achieving accuracy on par with Qwen2.5-14B on" MATH.[^c10] As a plug-in with no further post-training, "Qwen2.5-1.5B+Planner consistently surpasses the" 7B models in the paper's comparison.[^c11] On AIME2024 the planner gets models to use "human-level strategies more than eight times per" problem.[^c12] A planner trained on the 0.5B reasoner also works "adaptively with different LLMs across various" datasets.[^c13]

What the mechanism claims, in short: the lever is the per-step choice of a named move, injected into the chain, rather than one instruction given up front. The paper's own baseline for this is a direct prompt asking an LLM to act as the planner, where "an LLM is directly prompted to act as the planner."[^c14] I did not read the slice that reports how the trained planner compares with that baseline, so I do not state the margin here.

## Limits

- The menu is fixed by hand. The paper says the planner's effectiveness, diversity and generalisation "depend heavily on expert priors and cannot be enhanced by the planner itself during reasoning."[^c15] A move absent from the menu cannot be learned by this method.
- Prompt wording matters and is not isolated. "Misleading, ambiguous, or overly narrow prompts can harm the reasoning process."[^c16] The paper does not separate the effect of the move from the effect of its wording.
- The planner shows an "imbalanced preference over strategies," which the paper lists as a limitation.[^c17] The repetition penalty targets this; the paper does not show that it removes it.
- The strategy count is a keyword proxy, and the correlation with accuracy is across models. A higher count with higher accuracy does not by itself show that injecting a move causes the gain. The plug-in results are the closer test, and they cover "seven datasets covering mathematics, multi-task reasoning, and code generation."[^c18] That is still one menu, one training recipe, and a few model families.
- The planner chooses moves, not questions. It never asks the user anything, and nothing here measures whether a human asker or answerer gains from being prompted with the same moves. Any such transfer is my inference, not a result of this work.

## Related

- [[per-problem-reasoning-pattern-selection]] — picks one reasoning pattern per problem and trains on it; here the choice is made again at every step, from a menu.
- [[strategy-template-intent-planner]] — a plug-in planner that conditions a generator on a template; it chooses the response strategy once, before generation, not inside the chain.
- [[decomposer-planner-centric-rl]] — an RL-trained planner that emits a whole research plan as a DAG; the plan is produced up front rather than injected step by step.
- [[step-boundary-steering]] — also intervenes at each reasoning step, but by editing activations at step boundaries rather than by prompting a named move.
- [[complexity-tiered-strategy-routing]] — routes each query to a reasoning mode by difficulty; the choice is per query, where this note's choice is per step.

[^c1]: arxiv-2512-08300 — "commonly used strategies: self-reflection, decomposition, deliberative thinking, validation, summarization, prioritization, continuation, sub-planning,"
[^c2]: arxiv-2512-08300 — "The planner receives the question and the current reasoning steps, and selects one of nine strategies to inject into"
[^c3]: arxiv-2512-08300 — "strategies, expressed as prompts, help bridge the"
[^c4]: arxiv-2512-08300 — "the base LLM serves as the reasoner, responsible for generating the next reasoning step based on the planner"
[^c5]: arxiv-2512-08300 — "ratio of the most frequently selected strategy"
[^c6]: arxiv-2512-08300 — "is the ratio of reasoning steps that follow"
[^c7]: arxiv-2512-08300 — "By detecting key words, we"
[^c8]: arxiv-2512-08300 — "there exists a positive correlation between the"
[^c9]: arxiv-2512-08300 — "and Qwen2.5-0.5B, which lack inherent reasoning strategies (i.e., strategy count is 0), cannot be"
[^c10]: arxiv-2512-08300 — "achieving accuracy on par with Qwen2.5-14B on"
[^c11]: arxiv-2512-08300 — "Qwen2.5-1.5B+Planner consistently surpasses the"
[^c12]: arxiv-2512-08300 — "human-level strategies more than eight times per"
[^c13]: arxiv-2512-08300 — "adaptively with different LLMs across various"
[^c14]: arxiv-2512-08300 — "where an LLM is directly prompted to act as the planner"
[^c15]: arxiv-2512-08300 — "depend heavily on expert priors and cannot be enhanced by the planner itself during reasoning."
[^c16]: arxiv-2512-08300 — "Misleading, ambiguous, or overly narrow prompts can harm the reasoning process."
[^c17]: arxiv-2512-08300 — "imbalanced preference over strategies."
[^c18]: arxiv-2512-08300 — "Our results across seven datasets covering mathematics, multi-task reasoning, and code generation"
