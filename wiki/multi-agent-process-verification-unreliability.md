---
description: "Verifying intermediate steps of multi-agent trajectories does not reliably raise accuracy: gains are noisy, generative judges beat scalar reward models, and unsolvable queries are rarely recovered."
aliases: ["MAS process verification", "MAS-ProVe", "partial trajectory verification"]
sources: ["arxiv-2602-03053"]
---
# Multi-agent process verification is unreliable

In a multi-agent system (MAS) each sub-agent output is a "step" toward the final answer. MAS-ProVe wraps six MAS frameworks with a verifier that picks the most promising of several parallel candidate trajectories, at two granularities (each agent call, or each whole iteration). It tests three verifier families: reward models (a score on a terminal output), process reward models (scores on intermediate states) and generative LLM judges.[^c1] The question was whether this steering helps. The answer is mostly "not consistently".

## What was found

- **Noisy, non-monotonic gains.** Verification "does not consistently improve performance and frequently exhibits high variance"; the authors name evaluating partial multi-agent trajectories as the intrinsic difficulty.[^c2]
- **Generative judges beat scalar scorers.** Judges won in 24 of 36 configurations against a reward model (Skywork-Reward-V2) and a process reward model (Qwen2.5-Math-PRM).[^c3] The authors' explanation, which they present as a hypothesis, is that scalar models are trained on narrow math-step or outcome data, while natural-language judgment copes better with heterogeneous MAS trajectories.
- **Trained judges beat general ones.** The finetuned evaluator FARE-20B "generally outperforms both general-purpose models", suggesting evaluation-specific finetuning adds gain.[^c4]
- **Verifying is easier than solving.** The gap between a small generalist judge (GPT-4o-mini) and a reasoning judge (GPT-5-mini) is much smaller than the gap between the same models as solvers, so the reasoning needed to verify a trajectory is lower than the reasoning needed to generate it.[^c5]
- **No best granularity.** Neither agent-level nor iteration-level verification wins across architectures; the choice is "architecture-dependent rather than a global heuristic", although each MAS often has its own clear preference.[^c6]
- **Solvability ceiling.** Verification can make queries already within reach more stable (fewer 1-2 of 3 outcomes) but rarely resurrects queries where the baseline succeeds 0 times in 3. The authors say utility is "strictly bounded by the agent's intrinsic generation horizon".[^c7]
- **Context handling.** Summarizing prior context helps in long-context math MAS but hurts on information-extraction tasks, where summaries lose evidence (my reading of the appendix figure captions; not quoted here).

## Limits

- Models are small or mid-sized (GPT-5-mini, GPT-4o-mini, a 20B finetuned judge); stronger verifiers were not tested.
- Only five verifiers, math, coding, science and agentic-search benchmarks; results per cell have wide error bars, so rankings rest on counts like 24 of 36.
- The same model (GPT-5-mini) serves as generator and judge in places; the authors concede a risk of self-preference bias.
- Why scalar models lose is hypothesised, not isolated by ablation.
- Nothing here concerns asking or clarifying questions; it concerns choosing among answer trajectories.

## Related

- [[process-reward-model-hackability]] — another account of why step scorers fail
- [[process-outcome-consistency-verification]] — a whole-derivation verifier that did help, in single-model RL
- [[verification-weighted-voting]] — using verifier scores to aggregate candidates
- [[judge-master-key-false-positives]] — generative judges can themselves be fooled

[^c1]: arxiv-2602-03053 — "reward model (RMs), which produce a continuous score"
[^c2]: arxiv-2602-03053 — "find that process-level verification does not consistently improve performance and frequently exhibits high variance"
[^c3]: arxiv-2602-03053 — "judges achieved higher accuracy in 24 out of 36 experimental configurations across Agent-Call and Iteration levels"
[^c4]: arxiv-2602-03053 — "the task-specific evaluator FARE-20B generally outperforms both general-purpose models"
[^c5]: arxiv-2602-03053 — "these models act as solvers. This indicates that the reasoning threshold required to verify a multi-agent trajectory is"
[^c6]: arxiv-2602-03053 — "indicating that granularity choice is highly"
[^c7]: arxiv-2602-03053 — "by the agent’s intrinsic generation horizon"
