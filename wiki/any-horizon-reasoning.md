---
description: "A tool-using agent keeps a direct answer as a live option at every turn; RL shapes when it takes it by adding per-step rewards and penalizing wrong answers."
aliases: ["any-horizon agent", "any-horizon reasoning"]
sources: ["arxiv-2512-13874"]
---
# Any-horizon reasoning

Any-horizon reasoning is a policy that decides, per question, how many turns to spend. It answers in one step when the input is short or the question is direct, and it iterates over tool calls when the input is too long to take in at once. The SAGE paper states the design as a human habit: "we can decide whether to iteratively skim long videos or watch" short ones in full when the task needs it.[^c1] It sets this against video models that "are still trained to predict answers in a single turn" while reading a large number of frames.[^c2]

The mechanism is a per-turn exit rather than a mode chosen in advance. The orchestrator, SAGE-MM, emits one JSON action per step: a tool call (extract a video segment, search the web, transcribe speech, ground an event) or a final answer. The answer is available at every turn, so a direct answer is one action among the others, not a separate pipeline. The paper describes the orchestrator as "responsible for deciding between multi-turn and single-turn behavior for effective any-horizon reasoning."[^c3]

Training is what shapes the choice. Distilling from a stronger teacher gives the student the teacher's habits: the distilled model "tends to show signs of overcalling tools" while keeping its single-turn ability.[^c4] RL then works against overcalling through the reward. Each trajectory's total is assigned to every action in it, so whole trajectories are compared inside a GRPO group.[^c5] The total has two parts. The step terms give small positive scores for well-formed and sensible calls, such as "+0.10, if current tool call is reasonable," where a GPT-4o judge decides rationality, and negative scores for invalid or repeated arguments.[^c6] The step scores are set so that "the accumulated step-level reward for a trajectory with 10 steps would" be comparable to the accuracy reward.[^c7] The accuracy term is a judged verdict on the final answer.

Because the step scores are positive for sensible calls, a tool call is not charged on its own. The charge is taken from the end: the authors "penalize the model for predicting a wrong answer with tool" calls "to compensate for the positive step-level rewards," and the stated aim is "enforcing the any-horizon nature."[^c8][^c13] A correct answer that used visual tools earns more, "a slightly higher reward of +1.25 when the answer is correct and SAGE used visual tools," which the authors justify by "the higher difficulty and importance of getting these tool calls right."[^c9] The training set is balanced to teach both regimes: "half of the samples required tool calls and the other half had single-turn responses."[^c10]

What the paper reports is a shift in the policy. The SFT model overcalls, and "Incorporating RL further refines this behavior" while improving single-turn and multi-turn accuracy.[^c11] The evidence for this is the paper's Table 9, which the slices read here do not reproduce, so the size of the shift is not checked.

## Limits

- The printed accuracy term reads "−0.5, if wrong answer and N ≥ 1." Read literally, N ≥ 1 holds for a one-step trajectory too, so a wrong direct answer would be penalized as well. The prose says the penalty targets wrong answers "with tool" calls. My reading is that the single-turn and multi-turn paths are separated by the accumulated step scores, not by the penalty. The text read does not settle which was implemented.
- The reward depends on frontier-model judges. Tool rationality is judged by GPT-4o at each step, and correctness by GPT-4o at the end. Neither judge's agreement with a human, nor the sensitivity of the policy to the judge, is reported in the slices read.
- Training was not stable without a cap: "Nmax = 6 for the first 100 steps is necessary for stable" RL, then the cap rises to 11.[^c12] How the exit behaviour depends on that schedule is not tested here.
- The slices read do not include an ablation that removes the step scores or the wrong-answer penalty alone, so the claim that these terms cause the any-horizon behaviour is the authors' design argument, not a measured effect of each term.
- The paper does not report, in the text read, how often the policy's choice of single or multi turn matches what the question required. The evidence is accuracy by bucket and a tool-use distribution, which can improve with fewer calls without the exit being chosen well.
- The domain is long-video question answering on a benchmark the authors built. Whether the same per-turn exit works for retrieval loops or for asking questions is my conjecture, not a result here.

## Related

- [[agentic-abstention]] — the same per-turn choice to stop, but the terminal action there is abstention, and the evidence that stopping is warranted often arrives late.
- [[benefit-scaled-tool-reward]] — prices each call by a paired with-and-without gain; here the step scores are fixed and the charge against extra calls lands on the final answer.
- [[complexity-tiered-strategy-routing]] — a router picks the strategy once, before the loop; here the same choice is revisited at every turn.
- [[exam-cost-reward]] — charges unnecessary investigation directly in the reward; here the wrong-answer penalty does that work.
- [[tool-integrated-reasoning]] — the loop this exit sits inside.
- [[stop-continue-criteria-in-retrieval-loops]] — the same stop decision in multi-hop retrieval, where fixed budgets rather than learned exits usually decide.

[^c1]: arxiv-2512-13874 — "can decide whether to iteratively skim long videos or watch"
[^c2]: arxiv-2512-13874 — "models are still trained to predict answers in a single turn"
[^c3]: arxiv-2512-13874 — "responsible for deciding between multi-turn and single-turn behavior for effective any-horizon reasoning"
[^c4]: arxiv-2512-13874 — "tends to show signs of overcalling"
[^c5]: arxiv-2512-13874 — "a single scalar reward Ri to every action in the trajectory"
[^c6]: arxiv-2512-13874 — "+0.10, if current tool call is reasonable"
[^c7]: arxiv-2512-13874 — "the accumulated step-level reward for a trajectory with 10 steps would"
[^c8]: arxiv-2512-13874 — "we penalize the model for predicting a wrong answer with tool"
[^c9]: arxiv-2512-13874 — "a slightly higher reward of +1.25 when the answer is correct and SAGE used visual tools"
[^c10]: arxiv-2512-13874 — "half of the samples required tool calls and the other half had"
[^c11]: arxiv-2512-13874 — "Incorporating RL further refines this behavior"
[^c12]: arxiv-2512-13874 — "Nmax = 6 for the first 100 steps is necessary for stable"
[^c13]: arxiv-2512-13874 — "enforcing the any-horizon nature"
