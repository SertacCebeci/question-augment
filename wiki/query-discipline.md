---
description: "In search agents, how a query relates to the previous one — repeat, pivot, or refine — predicts accuracy far better than how many queries are issued."
aliases: ["query discipline", "query cleanliness"]
sources: ["liu-2026-diagnosing"]
---
# Query discipline

> Among search agents at similar cost, the ones that do better are not the
> ones that search less — they are the ones whose queries rarely repeat
> the last one and whose new angles land on evidence.

## Definition / Mechanism

Every search step is classified against the previous query by token
overlap: `repeat` at Jaccard overlap ≥ 0.85, `pivot` below 0.25, and
`add/drop_constraint` in between. "The weakest agent, gpt-oss-120b at
38.0%, issues the most searches, 31.8 search-turns, and volume runs the
wrong way for an effort story, anti-correlated with accuracy at 𝜌 =
−0.77; what tracks accuracy is query cleanliness and yield."[^c1]

## Why it matters

Redundant re-querying, not query volume, is what separates strong agents
from weak ones: "redundant re-querying is the cleanest behavioral
predictor of failure... repeat rate is the strongest non-mechanical
behavioral correlate of accuracy, with 𝜌 = −0.83."[^c2]

Exploring new angles is not itself the waste: "pivot rate is not
negatively correlated with accuracy, with 𝜌 = +0.31, and the most
pivot-heavy agent, Kimi K2.6 at 70%, is among the strongest... What
separates strong from weak is whether new angles land on evidence."[^c3]

Batching several queries into one reasoning turn also correlates
positively with accuracy (𝜌 = +0.75), but the paper is explicit this is a
style rather than a requirement: "Kimi K2.6 reaches 69.2% over 27 serial
turns, brute-forcing breadth where GLM 5.1 triangulates."[^c4]

## Limits

The correlations (𝜌 = −0.83 repeat, +0.31 pivot, +0.75 batching) are
Spearman statistics over six agents — a descriptive cross-agent pattern,
not a controlled experiment that manipulates query style and measures the
effect. The repeat-rate metric can itself be contaminated by tooling
rather than strategy: "Tongyi-DR's raw repeat rate of 4.8% looks like a
second offender, but it is an artifact of malformed calls: its scaffold
passes query as a JSON array, which the harness's single-string schema
rejects... excluding rejected calls drops genuine repeat to 1.5%."[^c5]

## Related

[[retrieval-utilization-gap]] · [[search-effort-accuracy-decoupling]]

[^c1]: liu-2026-diagnosing — "The weakest agent, gpt-oss-120b at 38.0%, issues the most searches, 31.8 search-turns, and volume runs the wrong way for an effort story, anti-correlated with accuracy at 𝜌 = −0.77; what tracks accuracy is query cleanliness and yield."
[^c2]: liu-2026-diagnosing
[^c3]: liu-2026-diagnosing
[^c4]: liu-2026-diagnosing — "Kimi K2.6 reaches 69.2% over 27 serial turns, brute-forcing breadth where GLM 5.1 triangulates."
[^c5]: liu-2026-diagnosing
