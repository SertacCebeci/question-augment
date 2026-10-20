---
description: "Models state usable verbal confidence yet do not move their answer-or-abstain decision when the stated error penalty rises, so the confidence is not what drives the action; utility collapses."
aliases: ["RiskEval", "risk-insensitive abstention", "confidence-policy decoupling", "policy consistency under penalty"]
sources: ["arxiv-2601-07767"]
---
# Penalty-invariant abstention (confidence-action dissociation)

A model that verbalizes a confidence c for its answer has, in expected-utility terms, a decision rule: with a reward of +1 for a correct answer, -λ for a wrong one and 0 for abstaining, answering is optimal only when c ≥ τ(λ) = λ/(1+λ).[^c1] RiskEval varies λ in the prompt (0.1 to 100) and asks whether the model's actual answer/abstain choice follows that threshold. Ten models (GPT-5-mini/nano, GPT-4.1-mini, DeepSeek-V3.2 with and without thinking, Qwen3-Next, Gemini-2.5/3-Flash, Gemma-3n, Llama4-Maverick) were run on HLE, GPQA Diamond and GSM8K.

**Measures.** Policy Consistency is the fraction of items where the model's decision equals the optimal decision given its own stated c. Regret under the model's stated belief is (1+λ)·|c − τ(λ)| when the decision is wrong, and a normalized form drops the (1+λ) factor. AUARC (area under the accuracy-rejection curve) scores whether confidence ranks correct above incorrect answers independent of λ.[^c2]

**Finding.** Increasing the penalty has negligible effect on behavior: neither the stated confidence nor the answer/abstain decision changes significantly across the range.[^c3] Policy consistency is high at low penalties (λ ≤ 5) and then degrades abruptly for λ ≥ 10, rather than adjusting smoothly, so models do not implement penalty-dependent thresholds.[^c4] Because abstention stays low while errors persist, normalized utility turns strongly negative on the hard benchmarks.[^c5]

**Not a signal failure.** Calibration-type metrics (AUARC, ECE, Brier) stay stable as λ grows, and accuracy and confidence are flat, so the failure sits at the decision step, not in the uncertainty estimate.[^c6]

**Not an instruction failure.** Appending an instruction to use the confidence to decide whether to answer or abstain left abstention rates and regret essentially unchanged; the authors read this as a behavioral prior toward always answering.[^c7]

**Scaffold.** Enforcing π* after the fact, using the stated confidence and the known λ, improves utility over the model's own policy; I read this as showing the confidence carries decision value that the model itself does not use (the paper's text I read supports the improvement, not the size).[^c8]

Relation to calibration: calibration asks whether c is accurate; this asks whether c is causally used. A calibrated but unused confidence is useful to an outside decision rule and useless as evidence of the model's own risk-awareness.

## Limits

Penalties are stated in the prompt, so the test measures responsiveness to a verbally described cost, not to cost learned or implied otherwise. Regret is computed under the model's stated belief, not true correctness probability, so it measures consistency, not objective loss. Only single-turn QA and three datasets; abstention is a prompted option, and answering-heavy behavior may partly reflect training or leaderboard incentives that this work does not isolate. A judge model (GPT-4o-mini) grades answers. The scaffold's gain was not examined here against better elicitation.

## Related

- [[belief-action-consistency-test]] — a sibling test of whether stated probability governs action; this one varies the cost, that one tests sufficiency and monotonicity
- [[abstention-option-uncertainty-inflation]] — how offering abstention shifts confidence behavior
- [[noise-invariant-verbal-confidence-rules]] — verbal confidence reliability under perturbation
- [[decision-token-extraction-overconfidence]] — another gap between stated certainty and decisions

[^c1]: arxiv-2601-07767 — "yields the optimal decision threshold"
[^c2]: arxiv-2601-07767 — "Policy Consistency (PC) measures the frequency"
[^c3]: arxiv-2601-07767 — "Neither the selfevaluated confidence nor the decision to answer or abstain changes significantly across incorrect answer penalties ranging in [0.1, 100]."
[^c4]: arxiv-2601-07767 — "This indicates that models do not implement penalty-dependent decision thresholds;"
[^c5]: arxiv-2601-07767 — "Low Abstention Rate Causes Utility Collapse."
[^c6]: arxiv-2601-07767 — "While calibrationrelated metrics remain stable across models (Fig. 5),"
[^c7]: arxiv-2601-07767 — "This suggests that the observed rigidity is not due to underspecified"
[^c8]: arxiv-2601-07767 — "Scaffold with π ∗ Improves Utility."
