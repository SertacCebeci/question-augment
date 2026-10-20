---
description: "A control policy that chooses to retrieve, clarify, reformulate, or stop from element coverage, evidence-validity coverage, and marginal retrieval gain, cutting rounds versus fixed-budget retrieval."
aliases: ["MAP-Law", "coverage-driven retrieval control", "element coverage"]
sources: ["cheng-2026-coverage"]
---
# Coverage-driven retrieval control

> In a multi-turn consultation agent, whether to retrieve more, ask the user
> a clarifying question, reformulate the query, or stop is decided from an
> explicit state of what is still missing — not from a fixed turn budget.

## Definition / Mechanism

MAP-Law represents a consultation as a graph over user facts, a fixed set
of legal elements for the case type, retrieved evidence, and the links
between them. At each round it computes element coverage EC (the fraction
of required elements currently supported by facts or evidence) and
evidence-validity coverage EVC (the fraction of retrieved evidence that is
actually linked to an element), and tracks the marginal gain MG that recent
retrieval added to the still-unresolved elements. An action selector then
chooses the next action — retrieve a statute, retrieve a case, request
clarification, reformulate the query, or generate the conclusion — from the
subset of legal elements that remain unresolved, not from the dialogue as a
whole.[^c1]

The agent stops once (EC ≥ θe ∧ EVC ≥ θev) or two consecutive rounds have
marginal gain below δ (reported thresholds: θe = 0.85, θev = 0.70, δ =
0.05), or a round budget is exhausted.[^c2]

On a 50-case synthetic Chinese labor-law pilot, a model-backed
(DeepSeek V4-Pro) action-selection variant reached EC/EVC 1.000 using 3.4
retrieval rounds and 7.1 evidence snippets on average, against a
fixed-seven-round baseline that used 7.0 rounds and 18.0 evidence snippets
without reaching full coverage; a deterministic rule policy plateaued at EC
0.780. Removing the structured coverage graph (MAP-no-graph) made EC fail
outright even though retrieval continued, and removing the threshold-based
stop while keeping the same action policy left the hard-to-resolve cases
unsolved at any tested budget up to r = 7 — [[recovery-postulate|recovery]] on those cases came
from a small increase in retrieval budget under the model-backed action
selector, not from removing the stopping check.[^c3]

## Why it matters

This is a working instance of an ask-vs-retrieve router: the same control
loop that decides whether to fetch more evidence can, by the same coverage
signal, decide to ask the user instead (`request_clarification`) — coverage
of a structured element set stands in for a [[value-of-information]] signal
without any elicited utility, at the cost of assuming the element schema
is already fixed and given.

## Limits

The pilot is a 50-case *synthetic* Chinese labor-law benchmark with a
legal-element schema fixed and held identical across every compared
system; the paper itself states the coverage scores are "internal
retrieval-control metrics under synthetic fixed-schema conditions" and
"should not be interpreted as deployment-level legal correctness."[^c4]
Multi-seed and hard-case robustness checks are reported only for the
model-backed policy, not for the underlying element-extraction step that
the whole mechanism assumes is solved upstream.

## Related

[[value-of-information]] · [[expected-information-gain]] · [[sprt]]

[^c1]: cheng-2026-coverage — "MAP-Law maintains a structured map over user facts, legal elements, retrieval goals, and retrieved evidence, and uses element coverage, evidence validity coverage, and marginal retrieval gain to decide whether to retrieve, clarify, reformulate, or stop."
[^c2]: cheng-2026-coverage — "(ECt ≥ θe ∧EVCt ≥ θev ) ∨ (MGt−1 < δ ∧MGt < δ)"
[^c3]: cheng-2026-coverage
[^c4]: cheng-2026-coverage
