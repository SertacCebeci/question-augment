---
description: "A refinement agent chooses per turn between asking a clarifying question and directly executing an edit, switching to asking only when it judges the user's feedback underspecified."
aliases: ["think-speak-act refinement", "Think+Speak/Think+Act"]
sources: ["ozden-2026"]
---
# Speak-act refinement

> Within one turn, decide whether the last constraint is usable before
> acting on it — and ask only when it is not.

## Definition / Mechanism

ConvDeck's per-stage refiners (Outline Refiner in Stage 3, Slide Refiner in
Stage 5) run a mechanism in which "the agent can communicate and clarify
before executing modifications. The agent operates in one of two modes:
Think+Speak, where it reasons about the request and asks a clarification
question when information is missing, and Think+Act, where it reasons about
the feedback and applies the appropriate edits."[^c1]

The paper attributes the design to ReSpAct (Dongre et al., 2025) as the
inspiration for interleaving reasoning, speech and action in one agent
loop, but the extract read here reports only ConvDeck's own use of the
pattern, not ReSpAct's own results.[^c2]

The mode switch is triggered by the refiner's own judgement that the
feedback is "underspecified" or "involves ambiguous presentation goals" —
the same turn that would otherwise silently apply an edit on a guessed
interpretation instead branches to a question.[^c3]

## Why it matters

This is a per-turn, per-edit decision rule for *whether to ask at all*,
operating inside a single conversational turn rather than across an entire
task — narrower in scope than [[clarifying-interaction-decomposition]]'s
task-level "when to ask" subtask, but sharing its structure: a gate that
must fire before the "what to ask" and "how to use the answer" questions
apply. It is evidence that a production multi-agent system finds it
necessary to let *every* tool-using refinement step, not just a dedicated
front-end classifier, decide whether it can act on what it has.

## Limits

- The trigger condition ("information is missing", "ambiguous") is not
  quantified in the extract read here — no threshold, uncertainty score, or
  held-out evaluation of the mode-switch decision itself is reported;
  Table 2/3's gains are attributed to the two-stage architecture as a
  whole ([[stage-specific-elicitation]]), not isolated to this switch.
- Reported only for two roles (Outline Refiner, Slide Refiner) inside one
  pipeline; whether the same decision rule holds for agents without a
  structured edit-operation vocabulary to fall back on (add/delete/merge
  slides, etc.) is not addressed.
- The attribution to ReSpAct is the source paper's own framing, not a claim
  this note verifies independently — Dongre et al. (2025) is not read here.

## Related

[[clarifying-interaction-decomposition]] · [[stage-specific-elicitation]] · [[elicitation-protocols]]

[^c1]: ozden-2026
[^c2]: ozden-2026 — "we adopt a speak–act refinement inspired by ReSpAct (Dongre et al., 2025), in which the agent can communicate and clarify before executing modifications"
[^c3]: ozden-2026 — "respond conversationally to request clarification, explain refinement choices, and discuss alternative revisions when user feedback is underspecified or involves ambiguous presentation goals"
