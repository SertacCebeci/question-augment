---
description: "Distills full agent-environment rollouts into a reusable stopping-rule playbook appended to context, raising timely abstention without updating model weights."
aliases: ["CONVOLVE", "Context Evolution", "convolve"]
sources: ["luo-2026"]
---
# CONVOLVE (Context Evolution)

> Learn when to stop from whole trajectories, not from final answers: a
> reflection pass over each rollout writes a lesson into a playbook, and the
> playbook — not a weight update — is what the next episode carries forward.

## Definition / Mechanism

Luo, Wen & Wang (2026) propose CONVOLVE as "a framework for
learning agentic abstention from multi-step interaction trajectories,"
distilling full environment rollouts, not just final answers, "into reusable
[[stopping-rules|stopping rules]] that are added to the agent's context for future episodes."
Formally, after episode $k$ produces trajectory $\tau^{(k)}$, a reflection
agent derives feedback $y^{(k)}=\phi(\tau^{(k)})$ from it, and the evolving
context updates as $c^{(k+1)} = U(c^{(k)}, \tau^{(k)}, y^{(k)})$: the reflection
identifies "whether the agent continued acting after the task had become
infeasible" and "which actions delayed [[abstention]]," and a curator model
converts that into structured playbook additions.[^c1]

Instantiated on a 500-example abstention-only subset of WebShop (20
trajectories for training, 101 held out), CONVOLVE is reported as "highly
data-efficient": with Llama-3.3-70B learning from its own 20 trajectories,
timely abstention recall (AbsRec@1) rises from 26.7 to 57.4 and overall
recall (AbsRec@10) from 83.2 to 100.0. Playbooks learned by the smaller
Llama-3.3-8B transfer to the 70B model — timely recall 26.7 → 55.3, overall
83.2 → 99.0 — nearly matching the model's own-lesson gains, "showing that
the useful part of CONVOLVE is not tied to the size of the model that
produces the lessons."[^c2]

## Why it matters

On stall 2, this is a concrete answer to "how would an asking agent learn a
stopping rule without a labeled stopping dataset or a reward signal": distill
the *evidence pattern* that preceded a correct stop from past trajectories
into declarative context, rather than fine-tuning a policy. It targets
exactly the failure [[agentic-abstention]] isolates — late abstention, not
absent abstention — and reports the same intervention closing most of the
overall-recall gap (WebShop, Llama-3.3-70B: 83.2 → 100.0) while more than
doubling the timely-recall gap closed (26.7 → 57.4).

## Limits

- The reported gains are from one environment (WebShop) with a 500-example
  abstention-only subset and only 20 training trajectories; the paper states
  additional AbstentionBench/TerminalBench results are in an appendix this
  note's source slices did not cover, so the WebShop numbers above should not
  be read as the method's performance in general.
- Training and held-out splits are stratified by scenario and grouped by the
  underlying WebShop goal, but both draw from the same benchmark distribution
  the method is evaluated on — no test of transfer to a differently
  constructed abstention task.
- The playbook is capped (80,000-token budget, 6,000-token curator input);
  the paper does not report what is lost when curation must discard material
  under that cap, or how performance degrades as the interaction history it
  must summarize grows.
- Gains are reported for one base-model family (Llama-3.3) at two sizes; the
  claim that lesson quality does not depend on the producing model's size
  rests on a single size pair (8B, 70B).

## Related

[[agentic-abstention]] · [[abstention]] · [[reversibility]]

[^c1]: luo-2026 — "a framework for learning agentic abstention from multi-step interaction trajectories"
[^c2]: luo-2026
