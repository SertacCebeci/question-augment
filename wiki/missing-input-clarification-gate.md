---
description: "A deterministic gate in a tool-using agent that halts before any tool call when a task-defining parameter is missing, instead of assuming a value, and measurably raises end-to-end task success."
aliases: []
sources: ["cao-2026-urbanagent"]
---
# Missing-input clarification gate

> Before acting, split a request's parameters into what is mandatory and
> what is a preference, and refuse to touch a tool until every mandatory
> one is filled — rather than scoring how much a question would help.

## Definition / Mechanism

Cao et al. (2026) give UrbanAgent's cognition
component a structured task representation that separates hard,
task-defining conditions from soft ranking preferences: "Chard encodes
mandatory conditions and Csoft ranking preferences."[^c1]

Any entity the task needs that cannot be inferred without changing the
task — a missing location, date, or destination — goes into a third set,
M. The gate is a single rule on that set: "If M ̸= ∅, UrbanAgent requests
these inputs and terminates before any tool call, rather than inferring a
location, destination, or other task-defining value."[^c2]

This is not a [[value-of-information]] comparison among candidate questions;
it is a completeness check that blocks the reasoning–execution loop
entirely until it passes. Selection, when it happens, is downstream of the
gate, over an already-reduced axis set.

## Why it matters

For stall 2 (which axis first), this is a different answer from
[[entropy]]-threshold or EIG-based triggers: instead of ranking candidate
axes by expected value, it draws a hard line between axes the task cannot
proceed without (must ask) and axes that only refine the ranking of
outcomes (never force a halt).

On UrbanEval's 250 cross-system urban requests, UrbanAgent reaches a 71%
overall task-success rate against 61% for the strongest tool-augmented
baselines (Native tool-calling and AutoGen), holding across four base
LLMs.[^c3]

The gap traces partly to the gate itself: across the 50
ambiguous-or-incomplete-intent queries, UrbanAgent "departs only in never
acting on an assumed value, returning no assumption... against 5–8 for
the baselines."[^c4]

Baselines that skip the gate silently assume the missing value and
produce a fluent but wrong-location answer.

## Limits

The paper evaluates the gate only as part of an integrated four-component
architecture and states it does not attribute gains to any single
component, so the 10-point margin cannot be assigned to the gate alone
versus the other three (reasoning-execution ordering, tool-observation
grounding, and constraint-checked synthesis). The gate's own recall (MIR)
is already near-saturated for every tested tool-augmented system
(0.90–0.98), so the measured task-success gap is not evidence that this
gate detects missing inputs better than alternatives — only that acting
on the detection, rather than assuming, does. Evaluation is on one
self-authored benchmark (UrbanEval) with an LLM judge and time-varying
live services; generalization to unseen cities, domains, or task types is
not established.

## Related

[[entropy-threshold-clarification-trigger]] · [[activation-gate]] · [[value-of-information]]

[^c1]: cao-2026-urbanagent — "Chard encodes mandatory conditions and Csoft ranking preferences."
[^c2]: cao-2026-urbanagent
[^c3]: cao-2026-urbanagent — "Over all 250 queries UrbanAgent attains an overall TSR of 71%, against 61% for the strongest baselines, Native tool-calling and AutoGen (Table 2)."
[^c4]: cao-2026-urbanagent — "UrbanAgent departs only in never acting on an assumed value, returning no assumption across the 50 ambiguous or incomplete intent queries against 5–8 for the baselines."
