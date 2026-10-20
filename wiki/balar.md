---
description: "A training-free outer loop scoring each clarifying question by mutual information over a factorized belief, updated by a soft Bayesian rule on free-text answers."
aliases: ["BALAR", "Bayesian Agentic Loop for Active Reasoning"]
sources: ["echarghaoui-2026"]
---
# BALAR

> A task-agnostic outer loop wrapped around an LLM: maintain a factorized
> belief over "disambiguating dimensions" of user intent, ask the
> unasked (question, answer-set) pair with the highest mutual information,
> update on the free-text reply, repeat until the posterior concentrates.

## Definition / Mechanism

At sleep time BALAR proposes a set of dimensions $\theta_1,\dots,\theta_p$
(e.g. "vascular involvement", "trigger pattern"), elicits a prior on each via
parallel LLM calls, and builds a likelihood table per candidate question.
The belief state is a log-probability tensor. Echarghaoui, Wu & Fox (2026):
"The belief state $\pi_t$ is stored as a log-probability tensor of shape
$n_1\times\cdots\times n_p$, initialized from marginals and updated in
log-space for numerical stability."[^c1]

Each round it scores every unasked (question, user) pair by expected
[[mutual-information]] between the belief and the answer and asks the
argmax pair — "The agent selects the unasked pair with highest MI" — then
maps the user's free-form reply to a soft distribution over the question's
discrete answer options (an LLM-estimated confidence vector, not a hard
label) before the Bayesian update, so an ambiguous answer shifts mass
rather than eliminating a hypothesis outright. Under the assumption that
answers are conditionally independent given $\theta$, the paper states a
guarantee for this greedy rule over the fixed pair space: "BALAR's greedy
MI-maximizing selection within the Ask sub-loop with a fixed pair space
$Q\times U$ satisfies" the $(1-1/e)$ ratio to the optimal $k$-round policy —
the same bound [[adaptive-submodularity]] gives for greedy coverage under a
submodular objective, applied here to MI over a fixed candidate set.[^c2]

## Why it matters

Across three active-reasoning benchmarks (detective cases, logic puzzles,
clinical diagnosis), the paper reports: "BALAR significantly outperforms
all baselines across all three benchmarks, with 14.6% higher accuracy on
AR-Bench-DC, 38.5% on AR-Bench-SP, and 30.5% on iCraft-MD."[^c3]

## Transfer

| | |
|---|---|
| **Home field** | [[bayesian-experimental-design]] / adaptive submodularity: rank a candidate design by [[expected-information-gain|expected information gain]] against a modelled likelihood; greedy has a $(1-1/e)$ guarantee under submodularity and conditional independence. |
| **Here** | Multi-turn LLM dialogue: the "design" is a (question, user) pair with an LLM-elicited likelihood table per dimension, not a written model; the answer is free text, soft-mapped to a discrete distribution before updating. |
| **What survives** | One-step-ahead MI ranking, and the $(1-1/e)$ greedy bound — but only conditional on the paper's stated assumption that answers are conditionally independent given $\theta$, which does not hold once dimensions are added mid-dialogue by [[entropy-gap-expansion]]. |
| **What does not** | Any guarantee on the *elicited* likelihood tables themselves: they are LLM output, not a fitted or known model, so the ranking the bound is proved for is computed on an approximation of unknown fidelity. |

## Limits

- The $(1-1/e)$ guarantee is proved for a **fixed** pair space $Q\times U$;
  it says nothing once [[entropy-gap-expansion]] adds a dimension mid-run,
  which the same paper's own outer loop does routinely.
- Single arXiv preprint (2026-05), no peer review found; self-reported
  benchmarks with the same model family plausibly used as both agent and
  simulated user in at least part of the evaluation — not independently
  checked here.
- The soft answer-mapping step depends on an LLM's [[calibration]] of its own
  confidence estimate $\hat\omega$; no calibration check is reported.

## Related

[[ca-bed]] · [[bayesian-experimental-design]] · [[mutual-information]] · [[adaptive-submodularity]] · [[entropy-gap-expansion]]

[^c1]: echarghaoui-2026 — "The belief state πt is stored as a log-probability tensor of shape n1 ˆ ¨ ¨ ¨ ˆ np , initialized from marginals and updated in log-space for numerical stability."
[^c2]: echarghaoui-2026 — "The agent selects the unasked pair with highest MI"
[^c3]: echarghaoui-2026 — "BALAR significantly outperforms all baselines across all three benchmarks, with 14.6% higher accuracy on AR-Bench-DC, 38.5% on AR-Bench-SP, and 30.5% on iCraft-MD."
