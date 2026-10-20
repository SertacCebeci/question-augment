---
description: "Extending an LLM assistant's clarification turns from 2 to 8 raises social-reasoning accuracy only until turn 4, after which it plateaus or degrades."
aliases: []
sources: ["taubenfeld-2026"]
---
# Multi-turn clarification plateau

> More turns to ask clarifying questions do not monotonically raise an
> answerer's accuracy — even when the extra turns carry real new evidence,
> not a contentless challenge.

## Definition / Mechanism

Taubenfeld et al. (2026) extend the debrief phase of
their Fuse social-reasoning simulation from 2 turns to 8, starting from a
low-detail first message, and let 12 LLM assistants ask follow-up questions
of a simulated user across the extra turns while their motive-prediction
accuracy (MSR) is tracked turn by turn.

The steepest increase occurs between turns 2 and 4; beyond turn 4,
performance mostly plateaus and even degrades.[^c1]

Even with the expanded turn budget, no model matches human performance at
turn 2, and most models stay significantly below their own performance in
the high-detail single-message setting.[^c2]

Tracking individual predictions from turn 2 to turn 8: by turn 8 only 18% of
initial abstentions remain, while the majority of predictions turn into
correct ones (58%) and the rest become incorrect (24%).[^c3]

Models also show high position persistence — when a model commits to a
prediction at turn 2, 81% of these positions remain unchanged by turn 8,
with 8% moving toward an incorrect prediction and 11% shifting to a correct
one.[^c4]

The paper's own framing of the result: longer conversations do not always
improve performance despite providing opportunities for clarifying
questions.[^c5]

## Why it matters

Extra clarification turns are not a free substitute for asking the right
question early: the steepest gain is concentrated between turns 2 and 4, and
turns beyond that mix genuine correction (bias-contradicting evidence
arriving late) with harm (the assistant adopting the user's framing rather
than probing it). A turn budget that assumes "more asking is better" is
falsified by this measurement — the stopping question (Stopping)
cannot be answered by simply allocating more turns.

## Limits

- Single benchmark (Fuse), single task family (motive prediction from a
  user's subjective retelling); the plateau's turn count (4) and the split
  percentages are specific to this simulation's dialogue design and are not
  shown to generalize to other clarification tasks.
- The user in this study is itself simulated (an LLM playing the user role
  with access to the full underlying scenario); the paper's own §5.3 flags
  that some portion of any assistant-side effect may be a simulator
  artifact, not a property of real users.
- The analysis is aggregated across 12 models and all scenarios; it does not
  isolate which models plateau versus degrade, or separate turns spent on
  clarifying questions from turns spent adopting the user's framing.
- The mechanism proposed for the correct-to-incorrect direction
  (accumulation of user bias across turns) is illustrated by one case study,
  not quantified at the same resolution as the turn-4 plateau itself.

## Related

[[clarification-benchmarks]] · [[sycophantic-capitulation]] · Stopping · [[value-of-information]]

[^c1]: taubenfeld-2026 — "The steepest increase occurs between turns 2 and 4, as the user introduces additional evidence clarifying the social situation. Beyond turn 4, performance mostly plateaus and even degrades."
[^c2]: taubenfeld-2026 — "even with an expanded turn budget, no model matches human performance at turn 2, and most models are significantly below their performance at the high detail setting."
[^c3]: taubenfeld-2026 — "by turn 8 only 18% of initial abstentions remain, while the majority of prediction turn into correct ones (58%) and the rest become incorrect (24%)."
[^c4]: taubenfeld-2026 — "when a model commits to a prediction at turn 2, 81% of these positions remain unchanged by turn 8, with 8% moving toward an incorrect prediction and 11% shifting to a correct one."
[^c5]: taubenfeld-2026 — "longer conversations do not always improve performance despite providing opportunities for clarifying questions"
