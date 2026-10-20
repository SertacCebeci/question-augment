---
description: "Splits one scalar satisfaction score into per-axis rewards (data, design, intent) and credits each ancestor node only on the axis its action type governs, instead of the full score to every ancestor."
aliases: ["Dimension-Aware Reward Decomposition"]
sources: ["xu-2026"]
---
# Dimension-aware reward decomposition

> When one scalar answer — a satisfaction score — actually judges several different things an agent did, crediting it uniformly to every decision misattributes blame; splitting it by which decision it actually judges fixes the search's value estimates.

## Definition / Mechanism

A rollout that interleaves a data query, a chart-design choice, and a clarifying question ends in one number, the user's satisfaction score, that a standard tree search would backpropagate unchanged to every ancestor action. In Vis-MCTS, Xu et al. (2026) instead have an LLM re-read the chart, the trajectory, and the user's textual critique to produce three relative sub-scores: "An LLM instantiates R to produce per-dimension scores (sd , se , si ) = R(img, τ, s, m) reflecting data fidelity, visualization design, and intent alignment respectively." These are then rescaled so their weighted sum reproduces exactly the original score — "We scale the LLM-assigned scores so that their weighted combination exactly equals the original user score, preserving the total reward injected into the tree" — so no reward is invented or discarded, only redistributed.[^c1]

A fixed map sends each action type to the one axis it governs: "we define a dimension mapping ϕ : A → {d, e, i, ∅} that sends execute_sql, execute_altair, ask_user_text to d, e, i respectively, and finish/root to ∅." Backpropagation then still reaches every ancestor, but credits each only on its own axis: "each node accumulates a Q-value drawn solely from the dimension it governs, namely rd at execute_sql, re at execute_altair, and ri at ask_user_text."[^c2]

## Why it matters

This is Xu et al.'s own fix for a credit-assignment failure they name directly: "when the user reports 'data is correct but the chart type is wrong' with a low overall score, a SQL node that issued a correct query is unfairly penalized for an unrelated visual deficiency."[^c3]

This wiki's reading: because these decomposed values feed the Q-values that [[vis-mcts]] uses to pick the next action, misattributed credit does not just report wrong — it steers the search away from the right question next time. The source does not say this; it is the inference that places the note on the selection map.[^c5]

Removing the decomposition measurably costs task success in Xu et al.'s ablation. The ablated variant is defined as "w/o Reward Decomposition. Replace Eq. 5 with uniform backpropagation, propagating s/10 to all ancestors regardless of action type." In Table 3 (Qwen3.5-flash [[backbone-of-a-formula|backbone]]) the full method's Merge Task Score is 51.46 and the "w/o Reward Decomposition" row's is 43.26 — a gap of 8.20 points, which the paper states as uniform backpropagation "degrades Merge Task Score by 8.20%."[^c4]

## Limits

The three-way split (data / design / intent) is fixed by this task's own action taxonomy and by an LLM's own relative judgment of which axis a critique concerns; neither the taxonomy nor the LLM-scored decomposition is checked against a held-out human judgment of which axis is really at fault, so the fix is shown to raise this benchmark's score, not shown to recover the true credit assignment. The score being redistributed is a simulated VLM user's satisfaction score (the [[leakage-controlled-user-agent]]), not a human's, and the 8.20-point ablation is reported on a single backbone (Qwen3.5-flash, Table 3), not on both backbones the paper otherwise evaluates. The 8.20-point figure itself (^c4) is [?] unverified as of this revision: the verifier could not locate the earlier quoted sentence, which the extract breaks across a page boundary; the claim is now quoted from the Table 3 rows and the ablation's definition and stays [?] until the verifier locates it. The steering claim (^c5) is this wiki's inference and rests on the assumption that the per-axis Q-values change which child UCT prefers, which the paper does not isolate.

## Related

[[vis-mcts]] · [[visinteract-bench]] · [[leakage-controlled-user-agent]] · [[value-of-information]] · [[expected-utility]]

[^c1]: xu-2026 — "An LLM instantiates R to produce per-dimension scores (sd , se , si ) = R(img, τ, s, m) reflecting data fidelity, visualization design, and intent alignment respectively."
[^c2]: xu-2026 — "we define a dimension mapping ϕ : A → {d, e, i, ∅} that sends execute_sql, execute_altair, ask_user_text to d, e, i respectively, and finish/root to ∅."
[^c3]: xu-2026 — "when the user reports “data is correct but the chart type is wrong” with a low overall score, a SQL node that issued a correct query is unfairly penalized for an unrelated visual deficiency."
[^c4]: xu-2026 — "Table 3: Ablation study on Vis-MCTS components with Qwen3.5-flash as the backbone."
[^c5]: xu-2026 — "each node accumulates a Q-value drawn solely from the dimension it governs, namely rd at execute_sql, re at execute_altair, and ri at ask_user_text."
