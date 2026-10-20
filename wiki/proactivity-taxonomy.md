---
description: "A three-level taxonomy — Reactive, Scheduled, Situation-Aware — sorting agents by whether a learned interruption policy, including staying silent, governs when they act."
aliases: ["three-level proactivity taxonomy", "Reactive/Scheduled/Situation-Aware", "insight policy"]
sources: ["bui-2026"]
---
# Proactivity taxonomy

> Autonomy is what an agent can do once running; proactivity is whether it
> decides, on its own, **when to run and whether to speak**.

## Definition / Mechanism

Bui & Evangelopoulos (2026) sort agentic coding systems into three
levels by which terms of a mixed-initiative decision an agent actually
computes:

- **Level 1, Reactive** — runs only when the developer starts an
  interaction; no persistent environmental presence between requests.
- **Level 2, Scheduled** — runs on a schedule or predefined trigger, and
  may filter, batch, rank or summarise within that trigger, but does not
  learn a cross-context, per-developer interruption policy; silence is not
  a learned choice over the full event stream.
- **Level 3, Situation-Aware** — monitors the event stream continuously,
  computes expected benefit against interruption cost over the full action
  space including staying silent, and updates its developer model from
  responses.[^c1]

The three levels are distinguished along three properties that are easy to
conflate: what initiates the agent, whether the developer may respond, and
whether that response changes future policy — a scheduled system can
produce artifacts a developer reviews and edits without that response ever
becoming a learned policy over when to interrupt.[^c2]

Underlying Level 3 is a mixed-initiative decision rule: the agent should
take the action $a\in A=\{\text{notify, question, draft, stay silent}\}$
whose expected payoff to the developer exceeds the cost of breaking their
flow, and choose *stay silent* — an explicit, deliberate option, not the
absence of one — whenever no action clears that bar. An **insight** is the
unit this policy emits: a context-grounded, time-sensitive hypothesis
about what matters next, paired with one of the four actions.[^c3]

## Why it matters

This gives the "which axis first" stall a third answer besides ranking
candidate questions by value: an agent can also rank *whether to surface
anything at all right now*, against a cost of interrupting that is a
property of the developer's current state, not of the candidate question.
Most deployed systems the paper surveys cluster at Level 2 — triggers and
batching without a learned per-developer cost of interruption — so the
taxonomy's main use here is diagnostic: a system that never treats silence
as a scored, learnable choice has not reached Level 3 regardless of how
much autonomous work it does.

## Transfer

| | |
|---|---|
| **In its home field** | Mixed-initiative interaction (Horvitz 1999, as the paper cites it): a human-computer interface reasons about interruption cost and [[expected-utility|expected utility]] to decide when to take initiative from the user. |
| **Here** | An agentic coding system deciding, at each moment, whether to notify, ask, draft, or stay silent about something it has noticed in the developer's environment. |
| **What survives** | The cost–benefit structure — act only when expected benefit beats interruption cost — and treating "stay silent" as an explicit, scoreable action rather than a default. |
| **What does not** | A validated cost or utility function; the paper names candidate proxies (IDE focus state, idle time, edit cadence, calendar status) but measures none of them. |

The paper reports no evaluation of the rule: "We present no measured
results."[^c4]

## Limits

- This is a proposed classification and decision formulation, not a tested
  one: the paper is explicit that it reports no measured results, so
  "Level 3" describes a target architecture, not a system shown to work.
- The taxonomy was built by auditing five deployed products against five
  documentation-based criteria, not by observing interruption decisions in
  use; a system scored "✓" on paper could still compute a poor cost
  estimate in practice.
- The interruption-cost formulation (Equation 1 in the source) assumes a
  developer-observable outcome and a utility over it are well-defined at
  each decision point; the paper does not supply either.

## Related

[[value-of-information]] · [[reversibility]] · [[bounded-rationality]] · [[clarification-benchmarks]]

[^c1]: bui-2026 — "Level 1, Reactive. The agent runs only when the developer starts an interaction. Between requests it has no persistent environmental presence, time model, or candidate action."
[^c2]: bui-2026 — "Figure 1 expresses the taxonomy as numbered interaction flows to separate three properties that are easy to conflate: what initiates the agent, whether the developer may respond, and whether that response changes future policy. This distinction matters most for Level 2: scheduled automation may still produce artifacts that developers review, accept, dismiss, or edit, but that response is not equivalent to a learned policy over when to interrupt, ask, draft, or remain silent."
[^c3]: bui-2026 — "The agent should pick the action whose expected payoff to the developer beats the cost of interrupting them right now, and pick stay silent when no action clears that bar."
[^c4]: bui-2026 — "We present no measured results."
