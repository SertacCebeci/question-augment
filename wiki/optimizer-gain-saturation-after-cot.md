---
description: "After chain-of-thought, few-shot prompt optimizers added almost nothing to HELM accuracy, at about ten times the extra prompt tokens of zero-shot CoT."
aliases: ["diminishing returns of prompt optimization", "optimizer gain beyond CoT", "few-shot optimizer saturation", "DSPy optimizer plateau"]
sources: ["arxiv-2511-20836"]
---
# Optimizer gain saturation after chain-of-thought

Automatic prompt optimization searches for instructions and demonstrations that score well on a validation split, and its natural baseline is the structured prompt it starts from. The study places the optimizers at the end of a ladder: the HELM baseline, a zero-shot DSPy prompt, a zero-shot chain-of-thought prompt, and then two optimizers, BFRS and MIPROv2. The first step, from the baseline to plain zero-shot prediction, "yields minimal improvement" on average.[^o1] The step that adds a reasoning trace is the one that carries the gain: "moving from Zero-Shot Predict to Zero-Shot CoT results in" a statistically significant improvement.[^o2] Once that is in place, "sophisticated optimizers (BFRS and MIPROv2) does not lead to additional improvements," and the mean moves from 66.2% to 66.3%.[^o3]

The optimizers differ from zero-shot CoT in what they put into the prompt. BFRS bootstraps demonstrations from traces that score well and searches over random sets of them; MIPROv2 proposes instructions and runs "Bayesian search over instruction-demo pairs."[^o4] Both therefore prepend task demonstrations. The token cost is the visible difference: the structured template adds 164 tokens for zero-shot CoT, while "BFRS adds 1,741 tokens per query and MIPROv2 adds 1,816."[^o5][^o6] By my arithmetic that is about ten times the overhead. The authors summarise the trade as "Few-shot optimizers reach high performance but require the largest token budgets," and that "Zero-Shot CoT captures most of these gains while using" minimal extra tokens.[^o7][^o8]

The paper's appendix offers one reading of the plateau, tied to [[cot-prompt-invariance]]. Once a shared reasoning interface is present, the optimizers' instructions and demonstrations may mostly reweight reasoning paths that were already reachable: "These variations can be viewed as reweighting mechanisms" on the distribution over traces.[^o9] The evidence for this is the cluster of scores, "tight clustering of performance across structurally different prompts," which the authors say is consistent with the reading but does not verify it.[^o10] I take the reading as the paper's conjecture, not a finding.

## Limits

- The search budget is small and the runs are single. Demonstrations are capped at K ≤ 3 per module, "BFRS uses 16 optimization trials," and MIPROv2 is run for 13. The authors say that "Multiseed optimization, nested validation, and broader stability analyses" are "important future directions."[^o11]
- Two optimizers were tested, not the space. The authors say they did not search "rather than exhaustively searching the prompt space."[^o12] Population-based or Bayesian searches such as [[evolutionary-prompt-search]] and [[bayesian-prompt-optimization]] are outside the study. The one other optimizer it reports, GEPA, was run only on MMLU-Pro in the text I read, where its gains are shown without a saturation comparison. The authors' own reading is that "the choice of optimizer is less important than the conclusion that leaderboards can shift under alternative prompts."[^o13]
- The cost argument covers recurring inference only. The paper treats "prompt optimization as an amortized one-time setup cost."[^o14] A search that is expensive to run and reused across many queries is priced differently from one run per query. My inference: the saturation claim says nothing about whether an optimizer is worth its search cost.
- The plateau is an average. It is taken over six models and seven benchmarks, so a mean that is flat can hide per-benchmark differences in either direction. The paper's own per-benchmark tables show that the methods do not coincide on every row.
- The same ceiling caveat applies. Where baseline scores are saturated, as the paper says of HeadQA, adding structure cannot show a gain, so a plateau is not proof that optimizers add nothing where headroom exists.
- Scope is short-answer and multiple-choice tasks, as in [[cot-prompt-invariance]].

## Related

- [[cot-prompt-invariance]] — the conjectured reason the optimizers have little left to add once the reasoning interface is shared
- [[bayesian-prompt-optimization]] — a surrogate-guided prompt search in code generation; the same family of search that MIPROv2 uses, here asked what it adds after chain-of-thought
- [[evolutionary-prompt-search]] — a population-based prompt search that this study did not test
- [[task-conditional-prompt-gain]] — a structured prompt's gain varies by task, so a flat mean can hide movement on individual tasks

[^o1]: arxiv-2511-20836 — "yields minimal improvement"
[^o2]: arxiv-2511-20836 — "moving from Zero-Shot Predict to Zero-Shot CoT results in"
[^o3]: arxiv-2511-20836 — "sophisticated optimizers (BFRS and MIPROv2) does not lead to additional improvements"
[^o4]: arxiv-2511-20836 — "Bayesian search over instruction-demo pairs"
[^o5]: arxiv-2511-20836 — "164 tokens for Zero-Shot CoT"
[^o6]: arxiv-2511-20836 — "BFRS adds 1,741 tokens per query and MIPROv2 adds 1,816"
[^o7]: arxiv-2511-20836 — "require the largest token budgets"
[^o8]: arxiv-2511-20836 — "Zero-Shot CoT captures most of these gains while using"
[^o9]: arxiv-2511-20836 — "These variations can be viewed as reweighting mechanisms"
[^o10]: arxiv-2511-20836 — "tight clustering of performance across structurally different prompts"
[^o11]: arxiv-2511-20836 — "Multiseed optimization, nested validation, and broader stability analyses"
[^o12]: arxiv-2511-20836 — "rather than exhaustively searching the prompt space"
[^o13]: arxiv-2511-20836 — "the choice of optimizer is less"
[^o14]: arxiv-2511-20836 — "treat prompt optimization as an amortized one-time setup cost"
