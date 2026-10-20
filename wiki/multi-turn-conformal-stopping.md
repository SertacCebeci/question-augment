---
description: "Splits one global conformal error budget across a multi-turn LLM pipeline's turns, calibrating a per-turn stopping threshold so early stopping preserves one end-to-end coverage guarantee."
aliases: ["MiCP", "Multi-Turn Language Models with Conformal Prediction", "multi-level conformal prediction for multi-turn LLMs"]
sources: ["arxiv-2604-01413"]
---
# Multi-turn conformal stopping

> A fixed miscoverage budget $\alpha$ is not one threshold, it is something
> to spend — divide it across the turns a multi-turn LLM pipeline might
> take, calibrate each turn's own stopping threshold from its own share,
> and the pipeline can stop as soon as any turn's threshold is cleared
> without losing the end-to-end coverage guarantee.

## Definition / Mechanism

A multi-turn LLM pipeline (adaptive RAG, a ReAct agent) answers after a
variable number of turns $t=0,\dots,T$, sampling $M$ candidate answers at
each. Standard [[conformal-prediction|conformal prediction]] calibrates
one threshold for one fixed-shape output and does not say which turn's
output to trust when the stopping time itself is a random, data-dependent
choice. MiCP resolves this by decomposing the single target error rate
$\alpha$ into **per-turn budgets** $\alpha_0,\dots,\alpha_T$ under a
constraint that discounts turns already exhausted by unanswerable
questions: "To address this, we decompose the total error budget α across
turns, allowing each turn to operate with its own calibrated NE
threshold."[^c1]

Each turn's threshold $\hat q_t$ is the empirical quantile of the
normalized entropy (NE) of that turn's sampled-answer distribution,
computed only over questions still active — not yet stopped and not yet
resolved — at turn $t$. At test time the pipeline stops at the first turn
whose NE clears $\hat q_t$; the final prediction set is built from every
turn's samples up to the stopping turn, plus an optional "Can't Answer"
label when the budget runs out with no cluster confident enough: "MiCP
guarantees the prediction set either contains the correct answer when it
appears among the sampled answers, or abstains via 'Can't Answer' when no
sampled answer is correct."[^c2]

A second, separate conformal threshold filters retrieved passages at
every turn by relevance, so noise does not accumulate in context across
turns while the same $1-\alpha_{\text{ret}}$ retention guarantee holds.
Empirically the coverage target holds across both stages under early
stopping: "These results confirm that MiCP
maintains the desired $1-\alpha$ coverage guarantee across both the
retrieval and prediction stages, even with early stopping enabled, which
comes from our multi-hop retrieval calibration and error budget
allocation."[^c3]

The allocation itself is chosen, not fixed: a grid search over
$\alpha_0,\dots,\alpha_{T-1}$ (the last is implied by the budget
constraint) minimizes a composite objective trading average turn count
against per-turn correct/incorrect answer rates, so the split reflects
which turns tend to already hold enough evidence. Optimizing for turn
count alone pushes the allocation toward the earliest turns: "optimizing
for fewer turns encourages the system to allocate more error budget to
early turns, causing the LLM to stop earlier and thereby avoiding the
accumulation of noisy, low-confidence answers from unnecessary later
turns."[^c4]

## Why it matters

This is a **sufficiency test with a coverage guarantee**, not a
confidence-threshold heuristic: the stopping decision at each turn is
tied by construction to a finite-sample bound on the final answer's
correctness, so "stop now" and "the answer is still in the prediction
set" are the same calibrated event rather than two independently tuned
knobs.

## Limits

The guarantee is marginal over the calibration distribution, not
conditional on any one question, and assumes calibration and test
questions are exchangeable — an assumption a genuinely adaptive
retrieval policy can strain (see [[turn-valid-coverage]]). The per-turn
allocation is fit by grid search on a held-out set, so it is a property
of the model/dataset pair calibrated on, not a closed-form spending
schedule; the paper's own experiments show it destabilizing on a model
(Gemma-2-9B-IT) that cannot separate answerable from unanswerable
questions well. The framework needs $M$ answers sampled per turn, so its
sampling cost still grows with $T$, only combinatorially less than a
naive per-turn CP.

## Related

- [[conformal-prediction]]
- [[alpha-spending-function]]
- [[sequence-level-conformal-prediction]]
- [[round-wise-regret-conformal-acceptance]]
- [[turn-valid-coverage]]

[^c1]: arxiv-2604-01413 — "To address this, we decompose the total error budget α across turns, allowing each turn to operate with its own calibrated NE threshold."
[^c2]: arxiv-2604-01413 — "That is, MiCP guarantees the prediction set either contains the correct answer when it appears among the sampled answers, or abstains via “Can’t Answer” when no sampled answer is correct."
[^c3]: arxiv-2604-01413 — "These results confirm that MiCP maintains the desired 1 − α coverage guarantee across both the retrieval and prediction stages, even with early stopping enabled, which comes from our multi-hop retrieval calibration and error budget allocation."
[^c4]: arxiv-2604-01413 — "This is because optimizing for fewer turns encourages the system to allocate more error budget to early turns, causing the LLM to stop earlier and thereby avoiding the accumulation of noisy, low-confidence answers from unnecessary later turns."
