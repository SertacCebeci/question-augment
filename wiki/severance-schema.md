---
description: "A prompt-level inventory of six person-context dimensions inserted into an LLM assistant's context so unmodelled facts about the user become named gaps it can ask about."
aliases: ["Severance Schema", "structured ignorance", "structured awareness"]
sources: ["litvak-2026"]
---
# Severance Schema

> Naming the categories of a person's life the model has no data on turns
> silent gaps into slots it can ask to fill.

## Definition / Mechanism

Litvak & Leqi (2026) give a personalized AI assistant a
fixed inventory of six dimensions of person-context — physicality,
temporality, consequences, continuity, multiplicity, interiority — each
either filled with what the assistant knows or marked `[unknown]`. The
schema carries no facts about the specific user; it is the *shape* of what
a person is, injected as text at the prompt level, independent of any
memory system. "The schema organizes person-context along six dimensions
designed to make the model aware that the person exists in the real
world: has a body, exists in time, faces real consequences, has a
history, occupies multiple roles, and has an inner life."[^c1]

The mechanism is explicitly framed as a conversion: an axis absent from
the model's context is an [[unknown-unknowns|unknown-unknown]] (nothing marks its absence);
naming the axis and leaving its value `[unknown]` turns it into a
known-unknown the model can act on. "Making these dimensions explicit
gives the model Structured Awareness: it converts unknown-unknowns into
known-unknowns, motivating the model to seek information on what it
lacks."[^c2]

Measured across five model families, assistants given the schema ask
clarifying questions about a missing dimension instead of extrapolating a
plausible answer from what little context they have. "Notably, models
with the schema ask clarifying questions when information about the user
is missing, rather than confidently extrapolating from incomplete user
information."[^c3]

## Why it matters

The schema is a generator for stall 2 (which axis first): it does not
rank candidate questions by a value function, it enumerates a fixed set
of axes that must each be checked filled-or-unknown before the assistant
answers, and any axis left `[unknown]` becomes a candidate question.

## Transfer

| | |
|---|---|
| **Home field** | Epistemology of ignorance — the known/unknown × aware/unaware grid (Rumsfeld's known-unknowns/unknown-unknowns, and the first-order/second-order distinction the paper attributes to Smithson's taxonomy of ignorance). |
| **Here** | Personalized LLM assistants: the axis is a category of a user's life (health, finances, roles, feelings), not a scientific or engineering parameter. |
| **What survives** | The core move — naming a category converts an unknown-unknown into an askable known-unknown — transfers intact; the paper's own framing cites this explicitly. |
| **What does not** | No formal measure of ignorance travels with it: the six dimensions are a fixed, hand-authored taxonomy for this domain, not derived from a probability model, and the paper does not claim they are exhaustive or that a missing seventh dimension is detectable by the same mechanism. |

## Limits

- The six dimensions are asserted as "a general-purpose starting set" by
  the paper's authors, not derived or validated as complete; an axis
  outside all six remains an unknown-unknown the schema cannot surface.
- Evaluated only on personal-advice-style single- and two-turn
  interactions across five model families, scored by an LLM judge
  (GPT-5.2, with a Sonnet 4 validation pass); no human-rated ground truth
  is reported here.
- The schema costs "a small usefulness tax" (~0.2 points) relative to
  answering immediately, because it asks rather than answers — a
  trade this note does not resolve for tasks where a fast answer is the
  point.

## Related

[[unknown-unknowns]] · [[clarification-benchmarks]] · [[expected-information-gain]]

[^c1]: litvak-2026 — "The schema organizes person-context along six dimensions designed to make the model aware that the person exists in the real world: has a body, exists in time, faces real consequences, has a history, occupies multiple roles, and has an inner life."
[^c2]: litvak-2026 — "Making these dimensions explicit gives the model Structured Awareness: it converts unknown-unknowns into known-unknowns, motivating the model to seek information on what it lacks."
[^c3]: litvak-2026 — "Notably, models with the schema ask clarifying questions when information about the user is missing, rather than confidently extrapolating from incomplete user information."
