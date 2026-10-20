---
description: "A recursive framework audits a fixed narrative, turns missing premises into typed self-queries resolved by internal hypothesis generation, gated on measured conflict density."
aliases: ["SABA", "Self-Awareness before Action", "Query-driven Structured Reasoning", "QSR", "Information Fusion", "IF", "proactive cognitive awareness"]
sources: ["arxiv-2604-20413"]
---
# Obstacle-driven state audit

> Before answering, name every gap that blocks the answer, turn each one into
> a private query the model answers from what it already has, and only run
> that loop at all when a cheap upfront check says the state actually needs it.

## Definition / Mechanism

Fan et al.'s (2026) SABA framework targets a
non-interactive setting — a fixed narrative with no further information
obtainable — where an LLM must reconstruct a hidden truth instead of
answering directly. It has two modules run in a recursive loop. **Information
Fusion (IF)** first turns the raw text into a structured, verified baseline
state: events are extracted as a backbone, descriptive attributes are bound
back onto the events they qualify, and each resulting unit is annotated with
a consistency check that flags but does not discard conflicting or uncertain
material.[^c1]

**Query-driven Structured Reasoning (QSR)** then audits that state against
the target task, diagnosing the set of missing or underspecified premises as
explicit, typed **obstacles** — a `(type, blocked_dimension, requirement)`
triple, e.g. `MissingLink`, `Ambiguity`, `MotiveGap` — rather than a single
undifferentiated "I don't know".[^c2]

Each obstacle is decomposed into sub-queries, each sub-query is answered by
generating a hypothesis grounded in the existing state (never by asking
anyone or fetching new text), and the state is updated with both the query
and the hypothesis before the next round. The loop terminates when no
obstacles remain ("logical closure") or a depth cap is hit.[^c4]

An **adaptive gate** sits between the two modules and measures the density
of unresolved conflicts and doubts in the freshly fused state; below
threshold, the recursive obstacle loop is skipped entirely and the model
synthesizes directly, so the cost of self-questioning is paid only on
narratives that actually need it.[^c3]

## Why it matters

The paper is explicit that its problem is not deciding whether, when or
whom to ask — there is no one to ask — but locating and connecting
information the model already possesses.[^c7] Still, its solution generalizes
the *form* of asking to a source-less setting: an obstacle is worded and
typed exactly like a clarification question would be, but answered by
retrieval-and-hypothesis over material already in hand.

A controlled ablation isolates the payoff of this obstacle-awareness step
specifically — removing it (while keeping fused state and the reasoning
loop) drops DP-Complex suspect accuracy by 22.2% relative, the single
largest drop of any ablated component — which supports treating explicit
self-questioning, not merely more inference compute, as the load-bearing
mechanism against early-hypothesis lock-in.[^c5]

The adaptive gate additionally buys most of that gain back cheaply:
normalized inference cost is 23.3–74.2% lower than other iterative/graph-based
baselines at comparable or better accuracy.[^c6]

## Limits

- Every hypothesis is generated and scored by the same model reasoning over
  the same fixed narrative; nothing here checks a hypothesis against an
  independent source, so a fluent but wrong hypothesis can pass consistency
  annotation and be folded into the state that later obstacles build on.
- Evaluated on one 31-case detective-puzzle benchmark plus HotpotQA,
  StrategyQA and BBH, all with a single backbone-model pair (DeepSeek-V3,
  Gemini-1.5-Flash); the gating thresholds are tuned parameters, not shown
  to transfer across domains.
- Explicitly out of scope for genuine information-gathering: the mechanism
  has nothing to say about who to ask, what question form elicits more, or
  when asking beats self-hypothesizing, because its setting removes the
  option to ask at all.[^c7]

## Related

[[self-hypothesized-clarification]] · [[premature-closure]] · [[chain-of-self-questioning]] · [[abstention]]

[^c1]: arxiv-2604-20413 — "SABA consists of two modules. The first module is Information Fusion (IF), which transforms the raw narrative into a structured and verified baseline by aligning events with attributes and by annotating logical consistency."
[^c2]: arxiv-2604-20413
[^c3]: arxiv-2604-20413 — "an adaptive gating mechanism is employed between phases: the system evaluates the density of logical Conflicts (alignment contradictions) and Doubts (missing causal links) within Dbase . If both indicators fall below predefined thresholds, the iterative loop is bypassed in favor of immediate synthesis, preventing redundant computation on straightforward tasks."
[^c4]: arxiv-2604-20413 — "The recursion terminates when either Ωt = ∅ (logical closure) or a maximum depth tmax is reached."
[^c5]: arxiv-2604-20413
[^c6]: arxiv-2604-20413 — "SABA achieves a normalized inference cost of T = 9.2, compared with T = 12.0 for SC and T = 35.7 for GoT. This means that SABA reduces inference cost by 23.3% relative to SC and by 74.2% relative to GoT, while still delivering consistently stronger reasoning performance."
[^c7]: arxiv-2604-20413
