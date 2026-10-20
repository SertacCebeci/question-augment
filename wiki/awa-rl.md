---
description: "A GRPO reward that replaces a fixed abstention bonus with a per-query refusal reward set from the model's own estimated prior success rate, adjusted live by a batch-level penalty during training."
aliases: ["Abstention-Aware Reinforcement Learning", "Abstention-aWAre Reinforcement Learning", "AWA-RL", "query-aware refusal reward"]
sources: ["zhang-2026-answer"]
---
# AWA-RL

> A search agent's [[savor-calibration-abstention-reward|abstention reward]], set per query from the agent's own
> prior success probability rather than a constant, so that whether to
> answer or refuse is calibrated to that specific question's difficulty.

## Definition / Mechanism

Standard outcome-reward RL for search agents gives a sparse binary reward
for the final answer and "fundamentally fails to supervise the [[abstention]]
action ⊥." AWA-RL reformulates the reward so that abstaining pays a
query-specific $r_{ref}(q_i)$ instead of zero: "$R(y,y^*,q_i) = 1$ if
$y=y^*$ (Correct), $0$ if $y\neq y^*$ and $y\neq\bot$ (Incorrect),
$r_{ref}(q_i)$ if $y=\bot$ (Abstention)."[^c1]

$r_{ref}(q_i)$ decomposes into a query-aware base term and a batch-level
dynamic penalty, $r_{ref}(q_i) = R_{base}(q_i) - P(E_t)$. The base term is
set before training: evaluate an abstain-free checkpoint's estimated
correctness probability $p_i$ for the query, clip it away from zero, and
pass it through a "non-linear optimistic mapping controlled by a single,
explainable 'courage' factor" $\gamma \in (0,1]$: $p_i^* = (p_{clip})^\gamma$,
$R_{base}(q_i) = 1 - p_i^*$. Lower $\gamma$ pushes $p_i^*$ down for every
query, raising the refusal reward and countering the agent's "natural bias
toward 'lazy refusal'" since a full multi-step search is harder to execute
than emitting a refusal token.[^c2]

During RL, a batch-level penalty $P(E_t)$ is subtracted from $R_{base}$,
computed from the gap $E_t$ between the batch's empirical refusal rate and
its theoretical expectation; it is a piecewise function bounded so that
"severe over-refusal ... pushes $r_{ref}\to -1$, while severe
under-refusal ... pushes $r_{ref}\to 1$," self-correcting the policy back
toward the query-specific target during on-policy training.[^c3]

## Why it matters

On three multi-hop QA benchmarks (HotpotQA, 2WikiMultiHopQA, MuSiQue)
with Qwen2.5-7B-Instruct, two static alternatives fail outright: injecting
unanswerable queries into RL data produces unstable refusal rates, and a
fixed refusal reward causes "catastrophic reward hacking (99.9% refusal)"
at even $r_{ref}=0.05$ in from-scratch RL, or a rigid precision/accuracy
trade-off in cold-start RL. AWA-RL avoids both: at its reported optimum
($\gamma=0.2$, cold-started) it reaches "[[ra-f1|RA-F1]] of 0.585, boosting
Precision from 0.559 to 0.662 with only a marginal drop in Accuracy
(0.552 to 0.529)," with batch refusal rates converging to a stable
plateau within 20-30 steps rather than collapsing or oscillating.[^c4]

## Limits

- The base term $R_{base}(q_i)$ is only as good as the abstain-free
  checkpoint's own estimated $p_i$; a checkpoint whose confidence is
  itself miscalibrated sets a target the dynamic penalty then chases, not
  corrects.
- Results are on one base model (Qwen2.5-7B-Instruct) and three
  Wikipedia-search multi-hop QA benchmarks with an LLM judge (GPT-oss-120b)
  scoring correctness; no cross-model or cross-domain replication is
  reported here.
- The "courage" factor $\gamma$ is tuned by grid search over a handful of
  values (Table 3); the paper reports no rule for choosing it a priori for
  a new task.

## Related

[[abstention]] · [[savor-calibration-abstention-reward]] · [[ra-f1]] · [[post-hoc-abstention]]

[^c1]: zhang-2026-answer
[^c2]: zhang-2026-answer — "we apply a non-linear transformation p∗i = (pclip )γ . γ ∈ (0, 1] is the “courage” factor, which scales the model’s confidence. The query-specific base refusal reward is then defined as Rbase (qi ) = 1 − p∗i ."
[^c3]: zhang-2026-answer — "severe over-refusal (Et → Emax ) pushes rref → −1, while severe under-refusal (Et → −1) pushes rref → 1"
[^c4]: zhang-2026-answer — "AWA-RL hits a state-of-the-art RA-F1 of 0.585, boosting Precision from 0.559 to 0.662 with only a marginal drop in Accuracy (0.552 to 0.529)"
