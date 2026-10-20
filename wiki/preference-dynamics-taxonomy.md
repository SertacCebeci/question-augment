---
description: "A four-way classification of how a user preference becomes knowable — withheld, flexible, infeasible, or not yet formed — assigning each a different agent move, not a single ask-or-not choice."
aliases: ["AcCoRD taxonomy"]
sources: ["srinivasan-2026"]
---
# Preference dynamics taxonomy

> A preference is not simply present or absent to an agent: whether it
> should ask, wait, negotiate, or watch depends on *which* of four ways
> that preference becomes knowable during an interaction.

## Definition / Mechanism

Srinivasan et al. (2026) sort every preference an
agent must satisfy into one of four dynamics by how it is discovered,
communicated, and how it evolves over a user-agent interaction: hard
underspecification (a fixed, achievable preference not stated up front,
requiring a targeted question), soft underspecification (a preference
held with partial flexibility, revealed only once the agent signals
difficulty satisfying the primary value), unachievable preference (a
stated preference the environment cannot satisfy, requiring the agent to
recognize infeasibility and negotiate a fallback), and triggered
preference (not yet formed at the start of the episode, coming into
existence only when the agent surfaces relevant information from the
environment — it "cannot be elicited through direct questioning").[^c1]

## Why it matters

Each dynamic prescribes a different move on the selection stall rather
than a uniform "ask vs. don't ask" rule: hard underspecification calls for
a direct question, soft calls for offering a trade-off only once
difficulty appears, unachievable calls for negotiation after a failed
search, and triggered calls for proactively exposing information instead
of asking anything at all. Evaluated across five frontier LLMs
(Llama-3.1-70B, DeepSeek-V3.2, GPT-4.1, GPT-5.1-high, Claude-Sonnet-4.5)
on two benchmarks, models satisfy hard and soft underspecified preferences
well (outcome score 0.7–0.9 and 0.8–0.95 respectively) but score
consistently lower on unachievable and triggered preferences, which the
authors report are "universally the hardest dynamics" and where agents
are "poorly equipped to recognize when a new preference becomes
relevant."[^c2]

## Limits

- The taxonomy is drawn from two scripted simulator domains (shopping,
  travel booking) under designer-written revelation rules and an LLM user
  simulator, not observed real-user dialogue; whether four categories
  exhaust real preference dynamics, or whether a real user's preferences
  mix categories mid-sentence, is untested.
- "Triggered" preferences are scored only against a scenario author's
  pre-planted set of niche attributes the simulator is instructed to
  reveal "only when the agent proactively surfaces the specific target
  attribute" — the benchmark cannot detect a triggered preference the
  authors did not anticipate, so the reported difficulty is a lower bound
  on how hard the dynamic is against an open-ended source of new
  information.
- The "why it matters" claim that each dynamic *should* receive a
  different agent move is this wiki's reading of the taxonomy's structure;
  the source measures outcome scores per dynamic, it does not itself
  prescribe or test a dynamic-conditioned selection policy against a
  dynamic-blind one.

## Related

[[clarification-benchmarks]] · [[value-of-information]] · [[question-budgets]] · [[constraint-seeking]]

[^c1]: srinivasan-2026 — "resolve user preferences across four preference dynamics that characterize how preferences are discovered, communicated, and evolve over the course of a user-agent interaction"
[^c2]: srinivasan-2026 — "Preferences from the two underspecification dynamics receive high satisfaction scores (hard: 0.7–0.9; soft: 0.8–0.95), while unachievable and triggered preferences are consistently lower."
