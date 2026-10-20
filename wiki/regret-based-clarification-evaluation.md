---
description: "Scores an LLM's clarification policy by regret — the whole-dialogue reward it loses against a semantic reference planner — separating asking-and-stopping efficiency from final-intent accuracy."
aliases: ["RegretBench regret", "benchmark-relative regret", "whole-dialogue regret", "dialogue-policy regret"]
sources: ["ta-2026"]
---
# Regret-based clarification policy evaluation

> Score a clarification policy by how much whole-dialogue value it loses
> against a competent reference [[planner-dynamic-stopping|planner]], not by whether it eventually
> reaches the right answer.

## Definition / Mechanism

Ta, Nguyen, Nguyen & al. (2026) represent an ambiguous request
as a clarification interaction graph (CIG): a set of hidden candidate
intents, the latent variables that distinguish them, a closed set of
supported semantic ask actions (one per variable), and a semantic
observation space that free-form questions and replies are mapped into. A
rollout's reward is $R(\tau,z) = U(\hat z,z) - C(\tau) - P(\tau)$: an
exact-match terminal utility on the recovered intent, minus an
assistant-token interaction cost, minus an accumulated penalty for
unsupported actions, off-topic or contradicted replies, redundant
clarification once the intent is resolved, and forced terminal answers at
the horizon. A normalized-regret form divides raw regret by the reference
planner's margin over an immediate-answer baseline, so a value near zero
reads as reference-level behavior and a value near one as no better than
answering without asking. Regret itself is this reward's gap to a
benchmark-supplied semantic reference planner operating over the same
intent space, action space, cost function and horizon: "Regret measures
the amount of whole-dialogue value a policy loses relative to the
reference strategy."[^c1]

## Why it matters

On stall 2 (which axis first, and when to stop), final-intent accuracy
alone cannot separate a well-ordered, well-stopped policy from a costly
one: two policies can reach similar success rates while one pays for it in
turns, cost and penalized clarification, since regret is the one quantity
in the reward decomposition that prices *when* and *how much* to ask
against a reference rather than just whether the final answer was right.
Across 16 models on open-domain QA, "models with similar accuracy can
differ substantially in efficiency, robustness to user behaviors, and
stopping decisions" — K2Think V2's success rate is "relatively high" but
its "reward is strongly negative due to excessive turns, high costs, and
substantial penalties," while GPT-4.1, a non-reasoning model, "achieved a
nearly optimal whole-dialogue reward and the lowest normalized regret of
any model, only surpassed by Gemini 3.1 Pro."[^c2]

## Transfer

| Home field | Here | What survives | What does not |
|---|---|---|---|
| Online decision theory / bandit regret (a policy's return measured against a best-in-hindsight or oracle comparator) | Whole-dialogue clarification-policy benchmarking (RegretBench) | The core operationalization: score = the gap between a candidate policy's return and a competent reference's return under identical information state, cost structure and horizon, decomposed into terminal utility, interaction cost and a behavior penalty | Any worst-case or minimax guarantee — the reference is one benchmark-authored semantic planner over the benchmark's own closed action/observation space, not a provable optimum over raw-language dialogue |

"Regret is benchmark-relative rather than an oracle measure of all possible
dialogue."[^c3]

## Limits

This note's claim that regret isolates the asking-and-stopping mechanism
rests on the reference planner being a competent, representative baseline
over the benchmark's own closed semantic space — the same abstraction the
Transfer claim above rests on. Scores also depend on a semantic parser and
a persona-conditioned LLM simulator (GPT-5 Nano) standing in for the user,
not a human interlocutor; the benchmark's own precision-oriented filtering
"may exclude cases of subtle [[efe-planning-as-variational-inference|ambiguity]]," and results are reported under one
fixed cost weight and a five-turn horizon.[^c4]

## Related

[[clarification-benchmarks]]

[^c1]: ta-2026 — "Regret measures the amount of whole-dialogue value a policy loses relative to the reference strategy."
[^c2]: ta-2026 — "models with similar accuracy can differ substantially in efficiency, robustness to user behaviors, and stopping decisions"
[^c3]: ta-2026 — "regret is benchmark-relative rather than an oracle measure of all possible dialogue"
[^c4]: ta-2026 — "This filter also favors quality over coverage and may exclude cases of subtle ambiguity."
