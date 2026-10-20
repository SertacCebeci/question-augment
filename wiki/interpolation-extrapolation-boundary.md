---
description: "Nearly every tested LLM agent performs worse on scientific papers published after its training-data cutoff than before it, evidence that in-loop competence leans on memorized material."
aliases: ["interpolation-extrapolation gap"]
sources: ["cui-2026"]
---
# Interpolation–extrapolation boundary

> An agent's apparent scientific competence is partly a lookup: ask about a
> paper it could not have memorized and the same agent performs worse.

## Definition / Mechanism

Using each model's documented (or best-estimate) training-data cutoff
date, [[inquitree]] splits its paper pool into pre-cutoff and post-cutoff
items: "we use publication date relative to a model's documented knowledge
cutoff as an approximate criterion for seen vs. unseen papers."[^c1]

With one exception, every evaluated agent shows a drop on post-cutoff
material: "With the notable exception of DeepSeek-R1, all evaluated models
exhibit a distinct performance degradation on papers published post-cutoff
compared to pre-cutoff."[^c2]

The paper reads this as evidence of reliance on memorized knowledge: "The
systematic drop on post-cutoff papers ... provides strong evidence that
current agents rely heavily on interpolation over familiar knowledge, and
are less robust when asked to reason about genuinely novel science."[^c3]

## Why it matters

For stall 4 (where does the constraint come from — who answers?), the
agent's own prior knowledge is itself a candidate source of a constraint,
and this result puts a boundary condition on that source's [[calibration|reliability]]: it
degrades exactly where the training-data record runs out. For stall 10
(answerer commitment), it argues that the confidence an agent expresses
inside a long inquiry loop is not a stable signal to hedge against — it is
higher than warranted whenever the material sits inside familiar training
territory and lower once it does not, so calibration would need to track
novelty, not just the loop's internal consistency.

## Limits

The training-cutoff split is a proxy, not a verified measurement of what a
proprietary model actually saw in training — cutoff dates are partly
self-reported and partly the paper's own estimate ("est."); the drop on
post-cutoff papers is not isolated from a possible confound of post-cutoff
papers being harder or less well documented on average.

## Related

[[inquitree]] · [[erosion-of-marginal-capabilities]] · [[sycophantic-capitulation]]

[^c1]: cui-2026
[^c2]: cui-2026 — "With the notable exception of DeepSeek-R1, all evaluated models exhibit a distinct performance degradation on papers published post-cutoff compared to pre-cutoff."
[^c3]: cui-2026
