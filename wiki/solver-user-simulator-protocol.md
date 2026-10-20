---
description: "An interactive-agent protocol that prices asking the user and inspecting the environment as separate, differently-costed actions under one explicit turn budget."
aliases: ["Solver-User Simulator protocol"]
sources: ["zhang-2026"]
---
# Solver-User Simulator protocol

> A controlled action space for an interactive code-generation agent: asking
> the user and probing the database are both available, but neither is free,
> and the two are priced differently.

## Definition / Mechanism

In [[direct-interactive-accuracy-gap|ProcArena]]'s Interactive mode, an LLM Solver working on a PL/SQL task can
take nine kinds of action: two user-facing (`ask_user`, a free-form
question; `ask_selector`, a forced choice among candidate readings),
six environment-facing (schema/table inspection, sample rows, compile,
execute, reset), and `submit`. A held-out LLM plays the User Simulator and
answers only from the information a routing "elicitation ledger" assigns it
— it never leaks hidden evaluation facts. `ask_user` and `ask_selector` each
cost two budget units; the environment actions cost between 0.5 and one
unit; `submit` is free. The Solver's total budget is `6 + 2|Λ| + 3` units,
where `Λ` is the task's own elicitation ledger, and both the budget and the
per-action price list are shown to the Solver throughout the episode.[^c1]

Resolving a requirement–environment contradiction requires both channels in
sequence: an environment action (e.g. `describe_table`) finds the objective
mismatch, but only `ask_user` or `ask_selector` can recover which reading
the user actually intends — the protocol keeps "what is true of the
database" and "what the user wants" as two separately-priced, separately
sourced queries rather than one undifferentiated "ask a question" action.[^c2]

## Why it matters

Most benchmarks and frameworks on this stall treat "ask a clarifying
question" as a single, typically free, action. This protocol is a
concrete counter-design: it forces an agent to weigh a user-facing question
against a same-turn alternative (probe the environment instead) inside one
shared budget, so the selection decision ("which axis first, and by which
channel") has a real, visible price.

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | Interactive PL/SQL code-generation benchmarking | Generic question-selection accounting (stall 2) |
| What survives | Treating "ask the user" and "inspect the environment" as distinct, differently-priced actions under one shared budget, not one interchangeable "ask" action | same |
| What does not | The specific unit prices (2 for a user-facing action, 0.5–1 for an environment probe, budget `6+2\|Λ\|+3`) are calibrated to this benchmark's own step-cost accounting; no claim in the source that this ratio is optimal or transfers to another domain's real cost of asking a human | — |

## Limits

- The "user" answering `ask_user`/`ask_selector` is itself a held-out LLM
  (DeepSeek V4 Flash), not a person: the protocol's realism rests on that
  simulator's fidelity, which a human audit found 85.6% acceptable — not
  on interaction with real users.[^c3]
- The price list is fixed by the benchmark designers, not derived from any
  independent cost model of a real developer's time or a real user's
  attention.

## Related

[[clarification-benchmarks]] · [[direct-interactive-accuracy-gap]] · [[defect-localization]]

[^c1]: zhang-2026 — "The Solver may take at most 60 recorded steps. Its tool budget is 6 + 2|Λ| + 3 units, where Λ is the task’s elicitation ledger. ask_user and ask_selector cost two units each, environment tools cost between 0.5 and one unit, and submit is free. Both the budget and the price list are shown to the Solver, and every tool result reports the units spent so far."
[^c2]: zhang-2026 — "Every environment action and every ask_user or ask_selector action consumes the interaction budget; submit is cost-free but terminates the episode immediately and returns no execution-accuracy feedback, preventing the Solver from iteratively refining its solution against the hidden oracle. The protocol provides two user-facing actions. ask_user routes"
[^c3]: zhang-2026
