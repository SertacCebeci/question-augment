---
description: "Giving a personal AI assistant retrieved facts about a user, with no structural marker for what remains unfilled, measurably lowers how often it flags missing person-context and raises hallucination."
aliases: ["memory's blind spot", "memory blind spot"]
sources: ["litvak-2026"]
---
# Memory-induced unawareness

> Handing the model retrieved facts about the user, without a structural
> marker for what is still missing, makes it act more finished than it is.

## Definition / Mechanism

Litvak & Leqi (2026) compare four prompting conditions
across five model families: no person-context, an unfilled schema of
person-context categories only, retrieved memory facts only, and memory
plus the schema. Adding memory alone — facts about the user, with no
explicit inventory of what categories of person-context exist — lowers
the fraction of missing-context categories the assistant flags below the
no-context baseline, and raises the rate at which it fabricates
information: "memory alone elevates hallucination from 0–1% to 3.7–11.7%
and suppresses unknown-awareness below the no-context baseline on every
model."[^c1]

The same identical memory, with the missing-category inventory added
(memory + schema), does not show this degradation: "Adding the schema
recovers both, reducing harm and sycophancy across all models at a small
usefulness cost (∼0.2 points)."[^c2]

Because the two compared conditions receive exactly the same retrieved
facts, the paper attributes the difference to the presence or absence of
the structural marker, not to the amount of information available.

## Why it matters

This is a documented failure mode for any answering system that adds
retrieved or remembered facts to make a response more personal: partial
information can make a model **less** likely to ask about what it still
lacks, not more, because filled slots read as completeness. On stall 2
(which axis first), naive memory is not merely inert — it actively biases the
model away from surfacing the axes memory did not happen to cover.

## Limits

- Measured on personal-advice dialogue tasks only, scored by an LLM judge
  (GPT-5.2, with a Sonnet 4 validation subset); the mechanism by which
  memory suppresses awareness (e.g. a completeness heuristic) is not
  independently tested, only the input–output effect.
- The reported range (0–1% to 3.7–11.7% hallucination) spans five model
  families with no single number reported for "memory" in general; the
  claim is the direction and the presence of the effect on every tested
  model, not a fixed magnitude.
- Both compared conditions are prompt-level; the finding does not speak
  to memory systems that themselves track and expose their own coverage
  gaps, which the paper does not test.

## Related

[[severance-schema]] · [[unknown-unknowns]] · [[clarification-benchmarks]]

[^c1]: litvak-2026 — "memory alone elevates hallucination from 0–1% to 3.7–11.7% and suppresses unknown-awareness below the no-context baseline on every model."
[^c2]: litvak-2026
