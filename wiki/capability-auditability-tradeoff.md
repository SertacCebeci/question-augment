---
description: "An abstaining speak-or-stay-silent policy trained with an inspectable reasoning trace loses decision quality (chiefly recall of true intervention opportunities) relative to the best trace-free policy."
aliases: ["capability-auditability tradeoff"]
sources: ["mendi-2026"]
---
# Capability–auditability tradeoff

> The best policy for deciding whether to speak is the one you cannot
> inspect; giving it a reasoning trace to audit costs it the recall of the
> moments it should have spoken at all.

## Definition / Mechanism

Mendi & Bent (2026) study **intervention timing**: at each
turn of a multi-party conversation an assistant must decide whether to
speak (act) or remain silent (abstain).[^c1]

Using Qwen3-8B they compare a **direct decision policy** (the action with
no exposed reasoning), a **reasoning policy** (chain-of-thought before the
action), and both under supervised fine-tuning and reinforcement learning.
They report: "the strongest direct policy achieves higher quality but
exposes no reasoning to inspect, while the reasoning policy provides a
trace at the cost of lower performance, particularly recall of true
intervention opportunities."[^c2]

Reinforcement learning does not close the gap. The paper names one
mechanism for the failure: "group relative objectives provide no learning
signal on confidently wrong prompts when sampled rollouts all select the
same action" — when every sampled rollout on a hard prompt agrees on the
same (wrong) action, a group-relative reward has no variance to learn from,
so the reasoning policy is never pushed off that prompt.[^c3]

## Why it matters

On stall 2 this is a point cost on "ask/intervene now or not": the setting
that gives the highest-quality speak-or-silent decisions is exactly the one
that cannot be inspected for why it decided that way, so an asker or
overseer who wants both the best decision and a legible reason for it is
choosing a point on a curve, not a single design.[^c4]

## Limits

- One model family (Qwen3-8B) and one task (multi-party intervention
  timing); whether the tradeoff holds for other act/abstain decisions (tool
  calls, escalation) is untested.[^c5]
- `mendi-2026` is an unreviewed 2026 arXiv preprint — `[?]` pending
  verifier confirmation; only the abstract was accessible for this note (no
  archived full-text extract), so the size of the quality gap and the
  recall figures are not independently quoted here.[^c6]

## Related

[[abstention]] · [[reasoning-faithfulness-observer-effect]] · [[value-of-information]] · [[investigative-question-grpo-training]]

[^c1]: mendi-2026
[^c2]: mendi-2026
[^c3]: mendi-2026
[^c4]: mendi-2026
[^c5]: mendi-2026
[^c6]: mendi-2026
