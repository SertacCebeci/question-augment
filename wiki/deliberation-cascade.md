---
description: "Enabling self-questioning and self-critique tools at every node of a multi-agent hierarchy degrades task return for all tested models versus the same hierarchy without them."
aliases: ["deliberation cascade"]
sources: ["bogdanov-2026"]
---
# Deliberation cascade

> Giving every delegated sub-agent its own self-questioning/self-critique loop
> does not add up: in a controlled multi-agent study it made every one of six
> tested models worse, at roughly double the token cost.

## Definition / Mechanism

Bogdanov et al. (2026) run a controlled ablation of a compound LLM agent
([[planner-dynamic-stopping|Planner]] delegating to Analyst and ActionChooser sub-agents) defending a
network in the CybORG CAGE-2 adversarial POMDP, across six models from five
families (3,475 episodes). Turning on the same deliberation tools — a
self-questioning step, then self-critique, then a self-revision pass — on
every agent in the hierarchy (`hier-delib`) lowers mean episode return
relative to the identical hierarchy with the tools off (`hier-base`) for all
six models, while roughly doubling token cost (1.8–2.7×), reaching up to
3.4× worse return. The paper names this destructive interaction a
**deliberation cascade**: "independent deliberation loops in the Analyst,
ActionChooser, and Planner amplify uncertainty without an arbitration
protocol."[^c1]

The loss is not explained by the extra tokens alone: a hierarchy without
deliberation tools consumes token counts comparable to a monolithic agent
with chain-of-thought added, yet returns substantially better outcomes (e.g.
Grok: 141.9K vs. 144.5K tokens, −24.0 vs. −42.9 return) — "confirming the
loss is structural."[^c2]

A traced episode shows the mechanism: under low-severity, decoy-heavy
context, the deliberative ActionChooser's self-questioning converges on
"avoid redundant interventions" and defers action until evidence is
unambiguous; by the time the Analyst flags high severity, the Planner's
override arrives a critical step late — in a penalty-only, failure-mitigation
environment even a single-step deferral prolongs a high-penalty state. The
paper calls this **passivity amplification**: distributed deliberation
overestimates momentary stability signals under partial observability.[^c3]

## Why it matters

This bears directly on where a self-questioning or self-critique step is
placed in an agent pipeline (stall 2, selection): the finding is not that
self-questioning is bad, but that distributing it, uncoordinated, across
every delegated node compounds disagreement rather than resolving it, and
does so consistently across model families. Hierarchical decomposition
without any deliberation tool matched or beat the best monolithic
deliberation configuration at comparable or lower token cost for four of six
models — task decomposition substituted for deeper per-agent reasoning.[^c4]

## Limits

- Measured in one environment — CybORG CAGE-2, a 30-step, non-positive-reward
  (penalty-only) adversarial POMDP — with three fixed roles (Planner,
  Analyst, ActionChooser); whether the pattern holds outside failure-mitigation
  settings or different hierarchy shapes is not established.
- No arbitration or aggregation protocol across the independently-deliberating
  agents was tested; the paper attributes the failure to its absence but does
  not show that adding one removes the cascade — that is this wiki's
  reading of the gap, not the paper's tested claim.
- Effect size is model-dependent (1.55×–3.37× worse return across the six
  models): the qualitative direction replicates, the magnitude does not.

## Related

[[bounded-rationality]] · [[chain-of-self-questioning]] · [[value-of-information]] · [[returns-per-token-spent]]

[^c1]: bogdanov-2026 — "Enabling deliberation tools on all hierarchical agents (hier-delib) decreases mean return relative to hier-base for all six models (Table 3, Figure 3). Devstral worsens by 3.37× (−37.8 → −127.4), Grok by 1.68×, and Llama by 1.55×, while token costs typically double (1.8-2.7×). This compositional failure arises from deliberation cascade: independent deliberation loops in the Analyst, ActionChooser, and Planner amplify uncertainty without an arbitration protocol."
[^c2]: bogdanov-2026 — "The degradation under hier-delib is not attributable to token overhead per se: hier-base consumes comparable tokens to monolithic +COT (e.g., Grok: 141.9K vs. 144.5K) yet achieves substantially better returns (−24.0 vs. −42.9), confirming the loss is structural."
[^c3]: bogdanov-2026
[^c4]: bogdanov-2026 — "for four of six models (Grok, Devstral, Qwen, G3FP), hier-base matches or outperforms the best monolithic deliberation at comparable or lower token cost, achieving through task decomposition what deliberation attempts through deeper reasoning."
