---
description: "An RL reward for agentic RAG that finds the earliest search step whose self-generated intermediate answer would already be correct, then trains the agent to stop there."
aliases: ["AutoSearch", "capability-aware optimal search depth", "minimal sufficient search depth", "search efficiency reward"]
sources: ["arxiv-2604-17337"]
---
# Self-answer-driven search depth

> Sun, Chong, Tu, Zhang, Zhang & Chai (2026): "we
> first investigate how search depth affects accuracy and find a minimal
> sufficient search depth that defines an accuracy-efficiency trade-off,
> jointly determined by question complexity and the agent's capability."[^c1]

## Definition / Mechanism

Prior agentic-RAG stopping rules penalize search depth directly (a fixed
cap, or a reward shrinking with trajectory length), trading accuracy on
hard questions for less search on easy ones without telling the two
apart. AutoSearch instead measures, per trajectory, the step at which
the agent itself could already answer correctly, and rewards stopping
there: "By a self-answering mechanism, AutoSearch identifies the minimal
sufficient search depth and promotes efficient search by rewarding its
attainment while penalizing over-searching."[^c2]

At every retrieval step t the policy is prompted, on the trajectory so
far, to produce an intermediate answer. The **capability-aware optimal
depth** $t_c$ is the earliest step whose intermediate answer exactly
matches the ground truth (or $t_c=-1$ if none ever does): "This depth
represents the minimal retrieval steps required for the agent to answer
the question correctly, reflecting its capability for the given task."[^c3]

Every retrieval step is then labeled one of three ways and rewarded
accordingly: steps in a trajectory that never reaches a correct
intermediate answer are **under-search** (small positive reward, to keep
exploring); steps before $t_c$ are **effective search** (positive, larger
for a shorter $t_c$); steps after $t_c$ are **over-search** (penalized).
The cumulative reward is maximized exactly at $t_c$ and falls off on
either side: "Both insufficient searching and over-searching lead to
lower rewards, encouraging the agent to learn an optimal search depth
rather than simply minimizing retrieval steps."[^c4]

This efficiency reward is one of three RL signals trained jointly: a
*base reward* (format validity plus exact-match outcome), the
*search-efficiency reward* above, and a *search-quality reward* (F1 gain
of each intermediate answer over the best F1 so far). Because $t_c$ is
recomputed per trajectory from the policy's own current competence, the
target stopping depth shifts as the agent gets stronger — the stopping
rule is capability-relative, not a fixed threshold on the question.

## Why it matters

The self-answer probe turns "have I searched enough" into something the
agent checks locally, per step, instead of only at episode end or via a
fixed external budget. Against baselines that penalize depth or
trajectory length directly, it keeps over-searching near zero while
depth still grows with question complexity: baselines show "high
over-searching ratios, particularly on multi-hop tasks," while
AutoSearch "effectively suppresses over-searching while maintaining
strong performance, leveraging the agent's own capability to adaptively
control search depth" (0.0–0.9% over-searching across four datasets).[^c5]

An ablation isolates the efficiency reward's role as the stopping
mechanism specifically, not just a quality booster: "Removing the search
efficiency reward decreases accuracy and significantly increases search
depth, indicating its importance for the accuracy-efficiency trade-off."[^c6]

## Limits

$t_c$ is an exact-match proxy for "the agent could already answer
correctly" — a paraphrase-correct intermediate answer that fails exact
match is scored as if still short of sufficiency, which can push the
reward toward searching past the point the agent actually had the
answer. The method is trained and evaluated only over a low range of
maximum search steps: "this study focuses on relatively low maximum
search steps," leaving the balance at deeper budgets untested (the
paper's own stated limitation). The reward also assumes a single
ground-truth answer checkable by exact match or F1 — no stopping signal
for open-ended or multi-part questions.

## Related

- [[search-effort-accuracy-decoupling]] — the diagnostic counterpart: across other search agents, effort barely predicts accuracy at all, which is the failure mode this reward is built to correct for.
- [[planner-dynamic-stopping]] — a different domain's version of the same shape: an agent-internal check of sufficiency triggers stopping instead of a fixed step count.
- [[calibrated-retrieval-budget-allocation]] — also grades a RAG system's retrieval effort per query, but by a calibrated confidence threshold fit once, not a per-trajectory RL reward.
- [[question-budgets]] — the general framing this method instantiates: a stopping decision priced against the cost of one more step.
- [[bounded-rationality]] — "good enough" as the stopping criterion, here made operational and trainable rather than a modeling assumption.

[^c1]: arxiv-2604-17337 — "we first investigate how search depth affects accuracy and find a minimal sufficient search depth that defines an accuracy-efficiency trade-off, jointly determined by question complexity and the agent’s capability"
[^c2]: arxiv-2604-17337 — "By a self-answering mechanism, AutoSearch identifies the minimal sufficient search depth and promotes efficient search by rewarding its attainment while penalizing over-searching"
[^c3]: arxiv-2604-17337 — "This depth represents the minimal retrieval steps required for the agent to answer the question correctly, reflecting its capability for the given task"
[^c4]: arxiv-2604-17337 — "Both insufficient searching and over-searching lead to lower rewards, encouraging the agent to learn an optimal search depth rather than simply minimizing retrieval steps"
[^c5]: arxiv-2604-17337 — "AutoSearch effectively suppresses over-searching while maintaining strong performance, leveraging the agent’s own capability to adaptively control search depth"
[^c6]: arxiv-2604-17337 — "Removing the search efficiency reward decreases accuracy and significantly increases search depth, indicating its importance for the accuracy-efficiency trade-off"
