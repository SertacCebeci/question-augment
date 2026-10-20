---
description: "Eight frontier LLM agents solve 15-24% of future tasks needing an unasked preference versus 83-97% with the preference given; asking, not applying it, is the bottleneck."
aliases: ["ATRBench"]
sources: ["wu-2026-later"]
---
# ATRBench

> A benchmark that hides each simulated user's standing preferences from
> the agent during ordinary tasks, then scores a later, user-offline task
> that only a preference obtained earlier makes solvable — isolating
> whether an agent asked in time from whether it can act once told.

## Definition / Mechanism

Wu, Zou, Wang, Zhao & Shi (2026) built ATRBench around a
decoupled construction: "standing rules, rule-bound test sessions, and
learning sessions are generated from the same persona and environment, but
target rules are not directly inserted into the learning trajectory."[^c1]

Each episode runs a learning phase (user online, agent may ask) and a
frozen test phase (user offline, agent must act from context already
gathered). The primary metric, TSAcc, is the pass rate on rule-bound test
sessions; diagnostic metrics separate whether the agent asked (RuleAsk),
whether its questions hit a real hidden rule (AcqPrec), how much of the
rule pool it covered (RuleCov), and whether an acquired rule was correctly
applied later (AppliedRate).[^c2]

Across eight frontier LLM agents: "rule-naive default agents solve only
15.0–23.7% of rule-bound future tasks, whereas oracle agents reach
82.5–96.7% when the rule answer is injected. This 62.1–76.6 point Gap
shows the test sessions are usually executable once the missing rule is
known; the hard part is acquiring it beforehand." Prompting-based
intervention barely helps: "the best non-oracle TSAcc beats default by
only +0.9 to +11.9 points, recovering 1.3–15.5% of the oracle gap."[^c3]

Forcing the agent to ask (the `always_ask` variant) does not fix targeting:
"among the seven active always_ask models, AcqPrec sits at 6.0–10.4%
... below the 10.1–22.4% the four atr-engaged models reach spontaneously
... What to ask remains the bottleneck once asking time is fixed."[^c4]

## Why it matters

This is a direct measurement, not an inference, that the failure on stall
2 for reusable-preference axes is not primarily a stopping or application
problem: once the axis is filled (oracle), agents apply it correctly
82.5–96.7% of the time, but they select and ask the right question at a
rate that recovers at most 15.5% of that gap on their own. Forcing the ask
event does not raise precision — the bottleneck named is *which* axis to
ask about, matching this map's own finding that an unmodelled axis is
invisible to a selection criterion.

## Limits

- All eight evaluated systems are frontier API agents tested by this one
  team, under one Router–Classifier scaffold and one persona pool
  (Nemotron-Personas-USA) with an LLM-simulated user; the numeric gaps are
  this benchmark's construction, not a cross-benchmark consensus.
- `replicated: false` — a single 2026 arXiv preprint (`wu-2026-later`,
  status `queued` in `wiki/meta/sources.json`); no independent replication
  is cited.
- The `always_ask` finding rests on a single trial per model/persona cell
  ("each cell runs a single trial"), so the AppliedRate drop under forced
  asking is reported by the source itself as an observation, not a
  measured effect.

## Related

[[ask-to-remember]] · [[clarification-benchmarks]] · [[expected-information-gain]] · [[proactivity-taxonomy]]

[^c1]: wu-2026-later — "standing rules, rule-bound test sessions, and learning sessions are generated from the same persona and environment, but target rules are not directly inserted into the learning trajectory."
[^c2]: wu-2026-later — "ATRBench also reports learning-side diagnostics. RuleAsk is the number of strict standing-rule questions per learning session."
[^c3]: wu-2026-later — "rule-naive default agents solve only 15.0–23.7 % of rulebound future tasks, whereas oracle agents reach 82.5–96.7 % when the rule answer is injected. This 62.1–76.6 point Gap shows the test sessions are usually executable once the missing rule is known; the hard part is acquiring it beforehand."
[^c4]: wu-2026-later — "among the seven active always_ask models, AcqPrec sits at 6.0–10.4 % (MiniMax M2.7 remains at 4.2% with low ask volume), below the 10.1–22.4 % the four atr-engaged models reach spontaneously."
