---
description: "Cold-start SFT sets how deeply a research agent searches before RL begins; RL refines that prior rather than escaping it, so shallow initial tool use persists after training."
aliases: ["initialization bottleneck", "shallow tool-use prior", "exploration prior from cold-start SFT", "initialization-bounded exploration"]
sources: ["doi-10-48550-arxiv-2603-07853"]
---
# Initialization-bounded exploration

In reinforcement learning with verifiable rewards (RLVR), the policy is improved from its own rollouts. The work gives the mechanism in one sentence: "a weak initialization restricts exploration and traps the policy in suboptimal tooluse behaviors."[^i1] For a research agent that must interleave reasoning with web search and page reading, the starting policy's tool-use habits decide which trajectories are ever sampled, and so which ones the reward can reinforce. If the start is shallow, the reward has little deep behaviour to amplify.

The authors name two symptoms in their research agents. The first is premature stopping: "the agent tends to terminate reasoning prematurely", producing an answer "before executing enough tool calls to adequately explore the search space."[^i2] The second is an imbalance across tools: "web search is invoked far more frequently than crawl webpage."[^i3] Both shrink the variety of trajectories that RL has to work with, and the paper attributes the premature pattern to the initial policy, describing the aim as avoiding "the shallow and premature termination patterns common under naive initialization."[^i4]

The claim that gives the concept its name is about persistence. Comparing initializations with RL held fixed, the authors conclude that "RL alone can refine an existing exploration policy but is insufficient to overcome a shallow tool-use prior induced by initialization."[^i5] On this reading, the depth of search is largely set before the outcome reward is applied, and RL adjusts within that depth.

## How the prior is measured

The depth is measured by tool-call counts in the trajectories used to train the agent, not by counting calls of a finished agent. A vanilla ReAct prompt yields short traces: "the model issues only 1.35 tool calls on average."[^i6] An explicit plan raised the count from 1.400 to 2.050, "but the generated trajectories follow the prescribed plan only 28.32%" of the time.[^i7] Step-wise cues in the thoughts pushed plan adherence to "adheres to the target plan in 76.96% of trajectories."[^i8] The cue ablation is the sharpest test. Removing cues from the synthetic data led to "substantial performance drops on three of four benchmarks", and the authors write that "without cues, the model tends to deviate from the prescribed diverse tool plan, resulting in shallower exploration patterns."[^i9]

Early training shows the same thing as entropy. The depth-prior variant "maintains higher policy entropy during early training," which the authors give as part of why it performs better.[^i10] This connects to [[rlvr-entropy-collapse]], where entropy falls under group-relative RLVR and narrows exploration. The work places the start of that narrowing in the cold-start stage. That placement is my reading of the entropy curves; the paper does not state it in those terms.

## Limits

- The depth-accuracy link is shown in two ways: a training-time cap of the tool budget from 8 to 6 steps, and the cue ablation. The paper reports that the cap "consistently degrades performance," and reads this as "indicating a positive correlation between performance and the depth of tool-based exploration."[^i11] A correlation between a training budget and accuracy is not a test of how many calls a fixed agent should make.
- Tool-call counts are a proxy for exploration, and the paper's own figures are counts from a large reasoning model generating training data, not from the trained agent. Whether a deeper trace is better evidence gathering is not measured here.
- The scope is two tools (web search, crawl webpage), text-only research agents, and Qwen3-8B and Qwen3-4B backbones across seven benchmarks.[^i12] The claimed gains are "up to 6.0%" and "5.8%" over baselines. I did not check the appendix for seed variance, so the size of the effect is not established by this note.
- The "cannot overcome" claim compares against control baselines, "vanilla RL from cold-start SFT and RL-from-scratch."[^i13] Whether a longer, differently tuned RL run would close the gap is not tested in the part of the text I read.
- The prior is set by a particular data generator, a large reasoning model prompted with plans and cues. Whether a different generator, or human trajectories, would give the same persistence is not shown.

## Related

- [[rlvr-entropy-collapse]] — entropy narrowing under group-relative RLVR; this work locates a shallow starting point for it in the cold-start stage (my reading)
- [[search-effort-accuracy-decoupling]] — the test-time counterpart: across six finished agents, search volume predicts little accuracy, which is in tension with the training-time depth-accuracy link here
- [[extra-search-penalty]] — a reward that charges each search after the first, the opposite pressure to a prior that asks for more depth
- [[stop-continue-criteria-in-retrieval-loops]] — stopping as a budget decision; the paper treats premature stopping as a product of the initial policy, not of any stop rule

[^i1]: doi-10-48550-arxiv-2603-07853 — "a weak initialization restricts exploration and traps the policy in suboptimal tooluse behaviors"
[^i2]: doi-10-48550-arxiv-2603-07853 — "producing the final answer before executing enough tool calls to adequately explore the search space"
[^i3]: doi-10-48550-arxiv-2603-07853 — "web search is invoked far more frequently than crawl webpage"
[^i4]: doi-10-48550-arxiv-2603-07853 — "avoiding the shallow and premature termination patterns common under naive initialization"
[^i5]: doi-10-48550-arxiv-2603-07853 — "RL alone can refine an existing exploration policy but is insufficient to overcome a shallow tool-use prior induced by initialization"
[^i6]: doi-10-48550-arxiv-2603-07853 — "the model issues only 1.35 tool calls on average"
[^i7]: doi-10-48550-arxiv-2603-07853 — "but the generated trajectories follow the prescribed plan only 28.32%"
[^i8]: doi-10-48550-arxiv-2603-07853 — "adheres to the target plan in 76.96% of trajectories"
[^i9]: doi-10-48550-arxiv-2603-07853 — "Without cues, the model tends to deviate from the prescribed diverse tool plan, resulting in shallower exploration patterns"
[^i10]: doi-10-48550-arxiv-2603-07853 — "maintains higher policy entropy during early training"
[^i11]: doi-10-48550-arxiv-2603-07853 — "indicating a positive correlation between performance and the depth of tool-based exploration"
[^i12]: doi-10-48550-arxiv-2603-07853 — "Across seven multi-hop and open-web benchmarks"
[^i13]: doi-10-48550-arxiv-2603-07853 — "vanilla RL from cold-start SFT and RL-from-scratch"
