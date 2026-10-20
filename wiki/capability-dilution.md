---
description: "Adding an uncertainty-decomposition objective to an agent's prompt measurably degrades its primary task success rate, worst where the task is already demanding."
aliases: ["capability dilution"]
sources: ["matsnev-2026-uncertainty"]
---
# Capability dilution

> Deciding whether to ask costs the reasoning budget that would otherwise go
> to the task itself — and the cost is not uniform across tasks.

## The finding

Matsnev (2026) instruments an LLM agent to emit,
in a single forward pass, an action, an action-confidence score, and (in the
proposed variant) a request-uncertainty score with its own explanation. Task
success rate falls monotonically as more such objectives are added to the
same prompt: 28.6% (ReAct+UE, one score) → 27.8% (Uncertainty-Aware Memory,
adds a natural-language explanation) → 27.0% (the proposed method, adds the
request-uncertainty channel), averaged across five LLM backbones and five
benchmarks. Because UAM and the proposed method differ only in the added
request-uncertainty signal, the 0.8-point gap between them isolates that
one addition's cost: "We call this capability dilution: each additional
uncertainty objective added to the prompt degrades the primary task
objective."[^c1]

The degradation is not uniform: "concentrated on benchmarks where the task
itself is already demanding (REAL: 32.1% → 19.2%; WebShop: 31.9% → 26.1%)
and is absent on the more structured ALFWorld, where success rate is
essentially unchanged (57.5% → 58.9%)."[^c2]

## Mechanism

Trajectory inspection ties the effect to a shared, fixed reasoning budget:
"the proposed agent spends a disproportionate share of its reasoning budget
debating whether the goal is underspecified, producing a long $u_t$
explanation and only a perfunctory action rationale... consistent with a
bounded reasoning budget that must be split across task-solving, confidence
estimation, and request-uncertainty assessment."[^c3]

The paper holds this is not a prompt-engineering artifact: "This is a
limitation that cannot be resolved by better prompt engineering within the
prompt-only regime, because the root cause is a fixed shared reasoning
budget rather than a specific phrasing failure."[^c4]

## Limits

- One paper, single-author preprint, not peer reviewed (`matsnev-2026-uncertainty [?]`
  in sources); the effect is reported, not yet independently replicated.
- Measured only for prompt-based, single-forward-pass elicitation on five
  LLM backbones and three environments (WebShop, ALFWorld, REAL); whether a
  trained (non-prompted) uncertainty head shows the same cost is untested
  here — the paper's own proposed remedy (§7.5) is to move estimation off
  the prompt.
- The claim rests on an isolation argument (UAM vs. the proposed method
  differ by one added signal) rather than a controlled ablation that varies
  the number of objectives directly; a third or fourth added objective is
  not tested, so the "monotonic" pattern is observed over exactly two steps.
- Task-dependence (present on REAL/WebShop, absent on ALFWorld) is not
  explained beyond "task is already demanding" — no independent measure of
  task demand is given.

## Related

[[bounded-rationality]] · [[uncertainty-decomposition]] · [[value-of-information]]

[^c1]: matsnev-2026-uncertainty — "We call this capability dilution: each additional uncertainty objective added to the prompt degrades the primary task objective."
[^c2]: matsnev-2026-uncertainty — "concentrated on benchmarks where the task itself is already demanding (REAL: 32.1% → 19.2%; WebShop: 31.9% → 26.1%) and is absent on the more structured ALFWorld, where success rate is essentially unchanged (57.5% → 58.9%)."
[^c3]: matsnev-2026-uncertainty — "the proposed agent spends a disproportionate share of its reasoning budget debating whether the goal is underspecified, producing a long ut explanation and only a perfunctory action rationale. This is consistent with a bounded reasoning budget that must be split across task-solving, confidence estimation, and request-uncertainty assessment."
[^c4]: matsnev-2026-uncertainty — "This is a limitation that cannot be resolved by better prompt engineering within the prompt-only regime, because the root cause is a fixed shared reasoning budget rather than a specific phrasing failure."
