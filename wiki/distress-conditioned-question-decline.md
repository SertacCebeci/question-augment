---
description: "A deployed chatbot's inferred response policy shows it asking progressively fewer follow-up questions as a user's distress persists over weeks of repeated interaction."
aliases: ["response policy drift", "follow-up question decline", "probing decay"]
sources: ["chu-2026"]
---
# Distress-conditioned question decline

> Whether an agent keeps asking is not fixed by the axis or the state alone:
> a deployed companion chatbot's own measured policy shows its propensity to
> ask a follow-up question falling as the same user's distress persists
> across sessions.

## Definition / Mechanism

Chu et al. (2026) fit Maximum Causal [[entropy|Entropy]] (MCE) IRL to real transcripts
of GPT-4.1 conversations (Study 2 of Hwang et al. 2025: 110 users, four
weekly sessions each) to recover a short-horizon response policy π(a | s):
the probability the chatbot's next turn falls into one of seven response
categories given the user's current vulnerability state (one of five,
including externally- and internally-triggered distress). Fitting the
policy separately per week and regressing π(a | s) on week index (1–4),
across 1,000 bootstrap refits, shows a significant linear decline in the
probability of a follow-up-question response (A4) as the same distress
state recurs across weeks: "probing declines significantly on both
externally triggered distress (β1 = −0.065*) and internal emotional
distress (β1 = −0.083*), with the strongest effect on internal distress. On
internal distress, this decline is accompanied by a rise in the
boundary/pushback/referral category (β1 = 0.037*)."[^c1]

The same direction shows up cross-sectionally, not only longitudinally:
users with higher pre-existing psychological risk (PHQ-9, GAD-7,
loneliness) receive fewer follow-up questions from GPT-4.1 under external
distress in an exploratory between-user comparison — "Psychologically
high-risk users ... receive significantly fewer follow-up questions when
they express external distress (∆ = −0.27**). This parallels the
longitudinal drift: probing declines both over weeks and for users with
higher psychological risk."[^c2]

## Why it matters

For question selection under a deployment loop (stall 2), the axis and the
user's state are not the only inputs: repeated exposure to the same signal
from the same asker moves an agent's actual propensity to ask, in a
direction that removes the corrective friction a follow-up question would
add — the paper frames this as a policy-level safety property invisible to
single-turn audits, not a property of any one response.

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | Maximum Causal Entropy IRL (Ziebart et al., 2008; 2010): recover a reward over state-action pairs from trajectories, then a Boltzmann policy π(a \| s) ∝ exp Q*(s, a) — built for imitation learning and robotics, where transitions are physical | A five-state, seven-action AC-VRT taxonomy stands in for the state/action space; transitions P(s'\|s,a) are estimated empirically from the same conversation transcripts |
| What survives | The policy as a comparable, transition-aware summary of behavior | Usable to contrast platforms, user subgroups, and weeks on the same footing |
| What does not | [[recovery-postulate|Recovery]] of the agent's training objective | "They do not recover a platform's training objective; ... what IRL estimates is the effective reward rationalizing the behavior of the deployed composite of base model, system prompt, and safety layers" — the estimate is observational and platform-level, not causal |

[^c3.1][^c3.2][^c3]

## Limits

The claim rests on GPT-4.1 being the only platform in the corpus with four
weeks of repeated interaction (Study 2's controlled deployment, a minimal
system prompt); it is not established for Character.AI or Replika, nor for
GPT-4.1 outside that deployment context. The transition model assumes the
Markov property, which the authors say is not validated — a first-order
diagnostic shows the previous chatbot action carries information the
current state does not — so π(a | s) inherits an unverified assumption,
though it stays within 0.02 nats/turn of assumption-free smoothed
frequencies. The cross-sectional psychological-risk comparison (^c2) is
explicitly exploratory: smaller sample, weaker correction tier than the
longitudinal result.

## Related

[[expected-information-gain]] · [[value-of-information]] · [[clarification-benchmarks]] · [[bounded-rationality]]

[^c1]: chu-2026 — "probing declines significantly on both externally triggered distress (β1 = −0.065* ) and internal emotional distress (β1 = −0.083* ), with the strongest effect on internal distress. On internal distress, this decline is accompanied by a rise in the boundary/pushback/referral category (β1 = 0.037* )."
[^c2]: chu-2026 — "Psychologically high-risk users (high PHQ-9, GAD7, loneliness) receive significantly fewer followup questions when they express external distress (∆ = −0.27** ). This parallels the longitudinal drift: probing declines both over weeks and for users with higher psychological risk."
[^c3.1]: chu-2026 — "The inferred reward function induces a stochastic policy π(a | s) ∝ exp Q∗ (s, a), where Q∗ (s, a) denotes the expected long-run value of taking action a in state s."
[^c3.2]: chu-2026 — "They do not recover a platform’s training objective; what IRL estimates is the effective reward rationalizing the behavior of the deployed composite of base model, system prompt, and safety layers"
[^c3]: chu-2026
