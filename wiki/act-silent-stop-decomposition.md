---
description: "A mobile-agent benchmark scores proactive intervention as three disjoint rates — act, stay silent, stop after rejection — no model balances all three."
aliases: ["Act/Silent/Stop rates", "proactive safety decomposition", "KnowU-Bench proactive metrics"]
sources: ["arxiv-2604-08455"]
---
# Act/Silent/Stop decomposition

> A single "safety score" hides the tradeoff; three separate rates, computed over three disjoint sets of trials, do not.

## Definition / Mechanism

Chen et al. (2026)'s KnowU-Bench gives its proactive[^s1]
tasks no explicit instruction: the agent sees only ambient state (time,
location, on-device GUI state) and "must autonomously select one of three
strategies—direct execution, proposing an action for confirmation, or
remaining silent." If it proposes, a user simulator returns an accept
or reject grounded in a hidden profile, and a rule-based judge flags
"trajectory level violations such as unsafe actions after user rejection"
 — the agent is expected to condition on the reply, not merely emit it.

Rather than folding this into one aggregate score, the benchmark reports
three policy-aware rates over complementary trial subsets: "the Act rate
measures whether the agent intervenes when intervention is warranted, the
Silent rate measures whether the agent appropriately refrains from acting
when intervention is unnecessary, and the Stop rate measures whether the
agent ceases further attempts after an explicit user rejection." The
three rates are not redundant summaries of one underlying skill; each is
computed on a different subset of trials (warranted-intervention trials,
unnecessary-intervention trials, post-rejection trials), so a model can
score well on one while failing another.

## Why it matters

Across 11 models this decomposition exposes a real tradeoff rather than a
ranking: "Claude Sonnet 4.6 is the most balanced model, with the best Act
score... Qwen3.5-397B-A17B shows the opposite profile, leading on Silent
... and reaching 75.0% on Stop, but dropping to 31.8% on Act... an
effective agent must know when to intervene, when to stay silent, and
when to back off after rejection." A manual failure-mode breakdown on
one model's trajectories confirms which side of the tradeoff current
agents fall on: "Intervention errors account for the majority of failures
(60.0%)... the much higher rate of Intervention than Passive suggests
that current agents are more prone to over-act than to miss opportunities
for action." The benchmark isolates initiative calibration as its own
axis, separate from clarification quality or GUI execution — a model can
ask fluent clarifying questions and still fail by acting when it should
not, or by continuing after an explicit rejection.

## Limits

- Single-source, one 2026 preprint; the rates are reported as this paper
  computes them and are not independently replicated.
- The reported per-model numbers depend on the benchmark's fixed task
  templates (four user roles, a specific app set) and on an LLM-driven
  user simulator standing in for a real rejecting user — how the rates
  would shift with real users is not measured here.
- The failure-mode breakdown (Intervention 60% / Passive 20% / GUI 15% /
  Rejection 5%) is manually coded for one model (Claude Sonnet 4.6) only;
  it is offered as illustrative, not as a claim that over-acting dominates
  for every model — the Act/Silent/Stop numbers themselves show at least
  one model (Qwen3.5-397B-A17B) with the opposite profile.
- The decomposition names *that* models trade off act/silent/stop against
  each other; it does not itself explain why, or supply a mechanism that
  would let an agent hit all three.

## Related

[[intervention-advantage]] · [[watchdog-outcome-escalation]] · [[decision-centric-design]] · [[clarification-request]] · [[abstention]]

[^s1]: arxiv-2604-08455
