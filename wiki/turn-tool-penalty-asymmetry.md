---
description: "On a ridehailing tool-agent benchmark, human pairwise preferences fit an excess user-facing turn to about twice the log-penalty of an excess backend tool call."
aliases: ["turn-tool penalty ratio"]
sources: ["han-2026"]
---
# Turn/tool penalty asymmetry

> The number behind "asking costs more than acting" for one tool-using
> agent benchmark: humans' revealed preference discounts an excess
> question about twice as hard as an excess tool call.

## Definition / Mechanism

Fitting [[efficiency-utility|Efficiency Utility]]'s two log-penalties
$a$ (tool excess) and $b$ (turn excess) from held-out human pairwise
preferences on Han, Fang, Hou & Liu's (2026) RideWay
benchmark gives $a = 0.1235$, $b = 0.2448$
($\lambda_{tool}=0.8838$, $\lambda_{turn}=0.7829$): "one excess
user-facing turn receives 2.01 times the log-penalty of one excess tool
call (90% bootstrap interval on b/a: [1.40, 2.96], B = 2500)."[^c1]

The metric's discrimination is asymmetric between the two axes it prices:
"Efficiency Utility achieves 78.7% accuracy overall: 90.6% when
trajectories differ in turns, but chance-level accuracy when they differ
solely in tool calls — the axis on which human annotators agree least."[^c2]

The fitted ratio is stable to the reference-floor annotation: "perturbing
every task's floor by ±1-2 units and refitting moves held-out accuracy
only within [0.787, 0.813]."[^c3]

## Why it matters

This is a measured, not assumed, price for asking versus acting inside
one benchmarked class of tool-using agent: on this task population,
raising the interaction burden by one avoidable question is judged
roughly twice as costly as raising it by one avoidable tool call. For a
stall-2 (which axis first) decision that trades a clarifying question
against a backend check, this is the first calibrated exchange rate this
wiki carries between the two.

## Limits

- One domain, one language, 58 tasks, 24 models (Chinese ridehailing
  dialogue) — the 2.01× ratio is this population's revealed trade-off,
  not shown to generalize to other agentic domains or task types.
- The tool-call side of the ratio is fit from a signal on which human
  annotators show only chance-level held-out agreement; the numerator
  (turn penalty) is better supported than the denominator.
- No independent replication of this specific ratio exists yet
  (`replicated: false`).
- `han-2026` is `status: queued` in `wiki/meta/sources.json`. `[?]`

## Related

[[efficiency-utility]] · [[clarification-benchmarks]] · [[value-of-information]] · [[bounded-rationality]]

[^c1]: han-2026 — "one excess user-facing turn receives 2.01 times the log-penalty of one excess tool call (90% bootstrap interval on b/a: [1.40, 2.96], B = 2500)"
[^c2]: han-2026 — "Efficiency Utility achieves 78.7% accuracy overall: 90.6% when trajectories differ in turns, but chance-level accuracy when they differ solely in tool calls — the axis on which human annotators agree least."
[^c3]: han-2026 — "perturbing every task’s floor by ±1–2 units and refitting moves held-out accuracy only within [0.787, 0.813]"
