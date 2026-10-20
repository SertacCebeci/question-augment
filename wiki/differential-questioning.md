---
description: "Feeding an agent's current candidate diagnoses back into its question generator so it asks what discriminates between them, an effect that swings 18 points in accuracy depending on when it starts."
aliases: ["differential questioning", "hypothesis-conditioned questioning"]
sources: ["sanghvi-2026"]
---
# Differential questioning

> Conditioning the next question on the agent's own leading hypotheses, instead
> of on the dialogue alone, is not uniformly good: it helps only once enough
> general evidence has already accumulated.

## Definition / Mechanism

In a baseline interactive-diagnosis agent, the next question is generated from
the conversation history alone, independent of the diagnosis predictions the
agent has already made. Differential questioning changes this: "the Question
agent additionally receives the candidate diagnoses, confidence scores, and
supporting reasoning, and is instructed to ask questions that differentiate
competing hypotheses."[^c1]

## Why it matters

The mechanism is only half the finding — *when* it is switched on is the
axis-selection variable that matters. Tested as an intervention activated
after a fixed turn threshold in a 20-turn consultation: "Activating it at
turn 2 reduces accuracy to 34.7%, 12.4 points below the baseline. Delaying
activation to turn 5 recovers most of the loss (50.4%) and turn 10 achieves
52.8%, yielding an 18.1-point swing from changing only the switch point."[^c2]
Early activation risks committing the question order to a weak hypothesis:
"This strategy has a known failure mode: conditioning too early on weak
hypotheses can lead to anchoring."[^c3]

## Limits

- Single benchmark (MeDxBench: 4,421 text-only diagnostic vignettes across
  20 specialties) and a single task domain (medicine); the specific switch
  points tested (turns 2, 5, 10) are calibrated to a 20-turn budget and a
  95%-confidence early-stopping rule, and may not transfer to a different
  turn budget or stopping rule.
- The switch-point sensitivity was measured with GPT-4o as the underlying
  model; cross-model transfer (Grok-4.1, DeepSeek-V3.2) was checked only for
  the full combined system, not for this timing curve specifically.
- The anchoring failure mode is the paper's own attribution to prior work
  (Graber et al. 2005; Chiu et al. 2026), not an independent measurement in
  this source. [?]

## Related

[[diagnostic-anchoring-in-agentic-llms]] · [[expected-information-gain]] · [[generalized-binary-search]] · [[bounded-rationality]]

[^c1]: sanghvi-2026 — "the Question agent additionally receives the candidate diagnoses, confidence scores, and supporting reasoning, and is instructed to ask questions that differentiate competing hypotheses."
[^c2]: sanghvi-2026 — "Activating it at turn 2 reduces accuracy to 34.7%, 12.4 points below the baseline. Delaying activation to turn 5 recovers most of the loss (50.4%) and turn 10 achieves 52.8%, yielding an 18.1-point swing from changing only the switch point."
[^c3]: sanghvi-2026 — "This strategy has a known failure mode: conditioning too early on weak hypotheses can lead to anchoring (Graber et al., 2005; Chiu et al., 2026)."
