---
description: "Runs Monte Carlo Tree Search jointly over asking another question and committing to a diagnosis, scoring both by one risk-aware value function."
aliases: ["Severity-Aware Conformal Clinical Planning", "joint Ask-Commit planning"]
sources: ["zhou-2026"]
---
# Risk-aware ask-commit planning

> Whether to ask one more diagnostic question or commit to a diagnosis now is
> decided inside the same search, by the same value function — committing is
> scored as a competing action, not triggered once confidence crosses a
> fixed threshold.

## Definition / Mechanism

Zhou, Zhou, Zhang et al. (2026) run Monte Carlo Tree Search
over both action types at once: each node is scored by an objective that
combines remaining diagnostic [[efe-planning-as-variational-inference|ambiguity]] with the calibrated
[[severity-weighted-omission-risk]], $\Psi(N_t) = w_D(1-\max_y b_t(y)) +
w_S \cdot \mathcal{R}_t$, and Ask and Commit branches are evaluated under
that one objective. "Commit is therefore not a heuristic stopping rule based
solely on confidence, but an explicit decision option competing with further
information acquisition."[^c1]

The reported search is bounded — up to 50 simulations at 2-step depth — with
standard UCB-style selection allocating simulations between the two action
types.[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Zhou et al. (2026) | Severity-Aware Conformal Clinical Planning | exact — the paper's name for the whole framework, of which this planning step is the search component |
| Zhou et al. (2026) | joint Ask/Commit trajectories | exact |

[^c3]

## Why it matters

Stall 7 (is $|W|$ small enough) is usually answered by a threshold on a
scalar summary of belief. Here stopping is not a threshold rule at all:
committing is one branch of the same search that scores asking, so the
stopping decision and the next-question decision share one value function
instead of being computed by two separate mechanisms.

## Transfer

| | |
|---|---|
| **In its home field** | Monte Carlo Tree Search evaluates action sequences in a game or planning domain by rolling out simulations and backing up a value estimate |
| **Here** | the two action types scored inside one tree are "ask another question" and "commit to a diagnosis," both priced by the same risk-aware value function |
| **What survives** | the core MCTS machinery — simulation, backup, UCB-style action selection — unmodified |
| **What does not** | any regret or sample-complexity guarantee for the search itself; the source reports empirical accuracy/question-count tradeoffs, not a bound on how close a bounded-depth, bounded-simulation search comes to the unbounded optimum |

## Limits

Read from a web-rendered version of the arXiv HTML, not an archived, locally
stored text extract (none exists yet for this source), so exact wording
could not be cross-checked against a fixed local copy. The search depth (2
steps) and simulation budget (50) are the reported experimental
configuration; whether results are sensitive to these bounds is not
established in what was read. Results are reported for DDXPlus and MediQ
only — benchmark diagnostic dialogues, not deployed clinical use.

## Related

[[severity-weighted-omission-risk]] · [[expected-severity-risk]] · [[sprt]] · [[optimal-decision-tree]]

[^c1]: zhou-2026 — "Commit is therefore not a heuristic stopping rule based solely on confidence, but an explicit decision option competing with further information acquisition."
[^c2]: zhou-2026
[^c3]: zhou-2026 — "introduces the calibrated clinical risk into Monte Carlo Tree Search to jointly evaluate long-horizon Ask and Commit trajectories"
