---
description: "Scoring search actions by value per unit budget works mainly because a penalty tied to the remaining budget is subtracted; removing it costs the most F1 of any component in a multi-hop QA agent."
aliases: ["budget-dependent penalty", "task-level VOI score", "dual-budget action allocation"]
sources: ["doi-10-48550-arxiv-2605-05701"]
---
# Remaining-budget penalty in action scoring

> Under hard limits on tool calls and tokens, the next action should be ranked by estimated task value per unit budget, and the part of that score that reacts to how much budget is left carries most of the gain.

## Mechanism

Fang et al. (doi-10-48550-arxiv-2605-05701) treat a multi-hop QA search agent as choosing, at each step, among retrieval, decomposition and answer commitment. Each feasible action gets a task-level score the authors call an operational estimate of "marginal task value per unit budget under the current state and remaining dual budget", explicitly not Shannon information gain or a Bayesian posterior value.[^c1] It is built from a critic-derived progress signal, structural signals (bridge structure, loop pressure, readiness, early-answer risk), and a signed budget-dependent penalty that is positive for search and decompose under tight budgets. The utility is then clipped at zero and divided by an action-specific budget scale, so cheap and expensive actions compete on value per unit cost.[^c2] This is a close relative of [[value-of-information]] and of [[voi-per-cost-modality-selection]], with the benefit supplied by a critic rather than computed from a belief.

## What was measured

In an ablation on Qwen3-32B at the upper-mid budget, the full controller had the best F1 on all four benchmarks, every component removal lowered the macro average, and the largest drop came from removing the budget-dependent penalty.[^c3] The authors read this as the remaining-budget term being "a central part of the action-allocation rule" rather than a cosmetic one. In a timing probe the controller cut mean inference time against the BAVT baseline from 20.91s to 15.23s, which they attribute to avoiding low-value operations.[^c4] The gain is largest at low and middle budgets; BATS stays competitive at upper budgets, and the stronger Qwen3.5-122B backbone gives a more mixed picture.[^c5]

## Limits

- The coefficients are fixed by hand (for example a cost-penalty scale of 0.7); the penalty is a proxy for an oracle shadow cost, and the approximation error is assumed bounded, not measured.
- The ablation is on one backbone and one budget level; the dataset that gains differs per component.
- Only multi-hop QA with question-only queries and one retrieval backend was tested; whether it carries to open-ended browsing is stated by the authors as future work.
- That the same penalty helps a human asker deciding what to ask next is my inference, not shown.

## Related

- [[value-of-information]] — the general quantity this score approximates operationally.
- [[voi-per-cost-modality-selection]] — same gain-over-cost ranking, different action set.
- [[cost-priced-joint-selection-and-stopping]] — subtracts cost rather than dividing, and also halts when no action is worth it.
- [[selective-answer-finalization]] — the answer-time half of the same controller.

[^c1]: doi-10-48550-arxiv-2605-05701 — "an operational estimate of marginal task value per unit budget under the current state and remaining dual"
[^c2]: doi-10-48550-arxiv-2605-05701 — "it is positive for S E A R C H and D E C O M P O S E under tight budgets."
[^c3]: doi-10-48550-arxiv-2605-05701 — "The largest drop comes from removing budgetdependent penalty"
[^c4]: doi-10-48550-arxiv-2605-05701 — "from 20.91s to 15.23s on average, a 27.2% reduction"
[^c5]: doi-10-48550-arxiv-2605-05701 — "BATS remains competitive in several upper-budget"
