---
description: "A two-stage clarification policy that separates tracking which facts could still change an optimization model's structure from deciding whether to ask or stop."
aliases: ["InterOPT", "Interactive Optimization", "gap-guided clarification", "Dynamic Gap Search", "Gap-Guided Action Search"]
sources: ["ge-2026"]
---
# InterOPT (gap-guided clarification)

> Before choosing what to ask, keep a running ledger of which unresolved
> facts would actually change the resulting formulation — and let the
> stopping decision consult that ledger without being bound by it.

## Definition / Mechanism

InterOPT is a two-stage policy for pre-formulation clarification in LLM
agents that build optimization models from natural-language requests. Stage
1, *Dynamic Gap Search*, is a structured LLM call that scans the public
brief and transcript each turn for unresolved **formulation-critical**
conditions — facts whose value would change the objective, constraints,
decision variables, or feasible region — across six fixed categories
(objectives/trade-offs, decision scope, operational constraints, time
boundaries, entity relationships, hard-vs-soft policy), and adds up to
three new entries to a persistent, cross-turn ledger with status Open or
Asked. Stage 2, *Gap-Guided Action Search*, reads the currently Open
entries and either emits READY_TO_MODEL or generates three candidate
questions, each anchored to a specific open ledger entry when the open set
is non-empty; a separate selector then picks one question to pose, ordering
candidates by risk to objectives, then constraints, then decision scope,
then silent-assumption risk.[^c1]

The two stages are deliberately decoupled: an empty open set does not force
readiness (Stage 1 may simply have missed a gap), and unresolved open
entries do not block Stage 2 from stopping — the ask-or-stop decision stays
with the acting model, informed by but not determined by the ledger.[^c2]

In a controlled comparison on the paper's own benchmark
([[clarification-benchmarks]], the OR-Clarify entry), InterOPT is
decomposed by two system-level ablations: removing Stage 1 (gap search)
while keeping three-candidate generation and the selector, and removing
Stage 2 (collapsing gap-finding and questioning into one direct policy).
Under the option-based (Choice) protocol, removing Stage 1 costs 11.1
percentage points of Core Exact [[recovery-postulate|recovery]] versus 6.0 for removing Stage 2,
and full InterOPT reaches 0.675 Core Exact against 0.506 (MC-D baseline, no
gap tracking) — the largest gain of any tested training-free method, at the
cost of roughly three times the atomic questions (10.0 vs. 2.4 per run).
Under the open/free-form protocol, removing Stage 2 keeps recovery similar
(0.506 vs. 0.538 Core Exact) but nearly doubles question count (9.5 vs. 4.8
atomic questions per run), so in that setting Stage 1 does most of the
recovery work and Stage 2 mainly cuts interaction length.[^c3]

## Why it matters

InterOPT operationalises "which axis first" as "which axis is still open
in a maintained ledger, ranked by what it could change" rather than by a
per-turn [[entropy]] or utility recomputation, and separates that selection
question from "have I asked enough" by giving the stopping decision access
to, but not control by, the same ledger. The open-setting diagnostics show
the two decisions fail differently: packaging (bundling several questions
in one turn) explains almost none of the shortfall (6.4% of turns), but the
agent declares readiness in 98.8% of runs while a stopping audit flags
40.6% of those as premature — the dominant failure is not not-asking, but
not-knowing-when-it-has-asked-enough.[^c4]

## Transfer

| | |
|---|---|
| Home field | Cognitive psychology — Nelson's (1990) monitoring/control distinction in metamemory: a reasoner tracks what is known and uncertain (monitoring) and separately allocates further search or stops (control). |
| Here | The distinction is used as an architectural design lens: Stage 1 (gap search) is monitoring, Stage 2 (ask-or-stop) is control, implemented as two separable LLM-driven modules with a shared ledger as the only channel between them. |
| What survives | The functional separation — a system can track what is unresolved without that tracking dictating when to stop, and the two can be measured and ablated independently. |
| What does not | Nelson's theory describes human metacognitive accuracy and its [[calibration]]; nothing here claims the LLM's "monitoring" state tracks the agent's own uncertainty the way a person's feeling-of-knowing does, and the paper reports the stopping decision is frequently premature even when the ledger is non-empty (40.6% of open-setting runs). |

[^c5]

## Limits

This note rests on one paper's own ablations on its own benchmark
(100 cases, one domain — operations-research model formulation) with one
LLM family as the acting model in the main comparison (DeepSeek V4 Pro);
the Choice-setting gain is large but the method also uses far more
interaction (10.7 turns vs. 3.3–4.0 for baselines), and in the open/free-
form setting InterOPT does not dominate the strongest baseline (ORPilot,
0.583 vs. 0.538 Core Exact) — the gap-ledger design is not shown to
transfer its Choice-setting advantage to free-form questioning.[^c6]

## Related

[[clarification-benchmarks]] · [[value-of-information]] · [[sprt]] · [[bounded-rationality]]

[^c1]: ge-2026 — "The first stage, Dynamic Gap Search, identifies formulation-critical gaps and maintains a cross-turn record of those that remain unresolved by the public transcript. The second stage, Gap-Guided Action Search, uses the currently unresolved gaps to decide whether to ask a targeted question or stop."
[^c2]: ge-2026 — "First, the runner never blocks READY_TO_MODEL merely because open entries remain: it terminates the interaction and records the event for diagnosis. Second, an empty open set does not force readiness, since Stage 1 may have missed a gap."
[^c3]: ge-2026
[^c4]: ge-2026
[^c5]: ge-2026 — "The decomposition is motivated by a monitoring-control view of problem solving. In this view, a reasoner not only performs task actions but also monitors what is known, what is still uncertain, and whether the current state is sufficient for the next step [16]. Control processes then use this monitored state to allocate further search or to stop."
[^c6]: ge-2026 — "In the open/free-form setting, no method is uniformly dominant: ORPilot attains the strongest recovery, GATE remains competitive, and InterOPT is close but not best"
