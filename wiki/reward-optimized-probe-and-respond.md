---
description: "A turn-level dialogue policy for health-misinformation correction that probes only when a learned forward-looking reward gain exceeds a per-question cost, conditioned on the user's latent state."
aliases: ["RO-PnR", "Reward-Optimized Probe-and-Respond", "ask-or-answer decision framework"]
sources: ["song-2026"]
---
# Reward-Optimized Probe-and-Respond

> In multi-turn health-misinformation correction, ask a clarifying question
> only when the forward-looking gain from asking clears a per-question cost
> — priced against a reward the policy has learned, not a written utility.

## Definition / Mechanism

Song, Anik & Liu (2026) frame each dialogue turn as a choice
between **Probe** (ask a clarifying question) and **Respond** (commit to a
correction), because existing systems "either respond immediately or probe
indiscriminately, treating clarification as either unnecessary or always
beneficial."[^c1]

RO-PnR subtracts an interaction cost from the value of probing: $r_t(\text{Probe}) = R_{future} - c\cdot n_t$, "where $c>0$ is the
per-question cost and $n_t$ is the number of clarification questions asked
up to turn $t$," and probes exactly when $R_{future}(h_t) - R(h_t) > c\cdot n_t$ —
the expected end-of-dialogue reward gain from probing must exceed the
accumulated cost of the questions already asked.[^c2]

To make probing value depend on who is being asked, "we model each
simulated user with a latent state along health literacy and belief
commitment," so the same dialogue history can cross the probe threshold for
one user type and not another.[^c3]

## Why it matters

Against baselines that always respond immediately, always probe a fixed
number of times, or probe reactively without user modelling, RO-PnR
"achieves the highest cost-adjusted utility across three health-misinformation
datasets and three base models, using 30% fewer turns than always-probe
baselines," reaching "0.71–0.73 in utility versus 0.68-0.72 for the
strongest baseline (SFT)."[^c4]

An ablation isolates the forward-looking term: removing it and reverting to
a one-step reward "degrades utility from 0.71 to 0.60, showing that a
probe's value often materializes several turns later" — the gain from
asking is not visible to a myopic, single-turn reward.[^c5]

## Transfer

| | |
|---|---|
| In its home field | Net [[value-of-information|value of information]]: expected decision-quality gain from a signal minus its cost (Howard 1966); in reinforcement learning, a shaped per-turn reward trained by policy optimization |
| Here | A per-turn probe-or-respond choice in misinformation-correction dialogue, where the "expected gain" is a learned reward estimate rather than a computed expectation over a written utility |
| What survives | The subtraction structure — price probing against a cost that grows with questions already asked, and act only when the net is positive — and the finding that a myopic (one-step) version of this reward under-values probing |
| What does not | No enumerated action set or declared utility as in Howard's VoI: $R_{future}$ is whatever the trained reward model outputs, so the probe/respond boundary is only as trustworthy as that estimator, not a derived quantity |

## Limits

- Single arXiv paper (2026); `song-2026` is queued, not yet independently
  verified — treat the numbers as reported, not confirmed.
- The per-question cost $c$ is an exogenous constant the experimenters set,
  not measured from a real user's burden; the paper's own ablation shows
  the rule is sensitive to it (c=0 produces far more turns and a utility
  collapse in their reported ablation table), so the threshold's
  practical value depends on a choice this note cannot verify was
  validated against real interaction cost.
- "User" here is a simulated latent state (health literacy × belief
  commitment), not an observed one; the probe decision is only as good as
  that simulation's fidelity to how real users actually respond.
- Evaluated with an LLM judge for quality/utility, cross-checked against
  human raters at a reported but moderate agreement level — the utility
  numbers this note cites inherit that judge's noise.

## Related

[[value-of-information]] · [[cold-start-value-of-information]] · [[bounded-rationality]] · [[question-budgets]]

[^c1]: song-2026 — "Yet existing methods either respond immediately or probe indiscriminately, treating clarification as either unnecessary or always beneficial."
[^c2]: song-2026
[^c3]: song-2026 — "To capture how user heterogeneity affects probing value, we model each simulated user with a latent state along health literacy and belief commitment."
[^c4]: song-2026
[^c5]: song-2026
