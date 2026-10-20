---
description: "Pairs a should-act and a should-abstain task differing by one trigger, scored by Paired Accuracy, so no constant act-or-refuse policy exceeds 50%."
aliases: ["AgentAbstain", "AGENTABSTAIN", "paired-task abstention benchmark", "Paired Accuracy", "Conditioned Abstention Rate", "CAR"]
sources: ["liu-2026-agentabstain"]
---
# AgentAbstain: paired should-act/should-abstain evaluation

> Score a tool-using agent on two tasks that differ by exactly one
> controlled trigger — one it should complete, one it should refuse — so
> that always acting and always refusing both score at chance.

## Definition / Mechanism

Liu et al. (2026) build every benchmark instance
as a pair $(T^+, T^-)$ sharing one sandbox: "Every instance is a pair
(T + , T − ) sharing the same sandbox but differing in a single controlled
perturbation δ." $T^+$ is fully specified and should be executed; $T^-$
carries exactly one trigger (in the query, the environment state, or the
tool set) making execution incorrect, harmful, or unjustified, and the
agent should refuse or ask for clarification. "By construction, no
always-act or always-refuse policy can exceed 50% Paired Accuracy."[^c1]

Four metrics follow: Act Accuracy (fraction of $T^+$ passed), Abstain
Accuracy (fraction of $T^-$ passed), Paired Accuracy — the primary metric,
the fraction of pairs where both sides pass — and Conditioned [[abstention|Abstention]]
Rate (abstain accuracy restricted to pairs whose act side the same model
already solved, isolating restraint from raw capability). Each task is
scored by combining a deterministic check of the tool-call trace with an
LLM judge on the terminal response.[^c2]

Across 17 frontier LLMs on 263 paired tasks in 42 executable MCP sandboxes,
"the best model (Gemini 3.1 Pro) achieves only 59.5% Paired Accuracy," and
13 of 17 models score below 50%.[^c3]

The paper's second finding is that this is not a capability-scaling
problem: "abstention capability is largely independent of general
task-solving capability, indicating that scaling task-solving alone will
not close this gap." Mean Act Accuracy exceeds mean Abstain Accuracy by 21
percentage points across the benchmark, and the gap between the two does
not shrink from the weakest to the strongest models tested.[^c4]

## Why it matters

On stall 2, this benchmark operationalises the same split
[[selection-abstention-asymmetry]] names for static retrieval — choosing
among candidates versus recognizing none should be acted on — but for a
*sequential*, environment-grounded agent: the trigger for $T^-$ can be
discoverable only mid-trajectory, through a tool call, not from the
instruction alone. Because the pairing removes the trivial
always-act/always-refuse strategies, Paired Accuracy is a harder,
better-defined target than a raw refusal rate for judging whether an
agent's "ask, don't act" decision is calibrated rather than a fixed
disposition.

## Limits

- The 42 sandboxes expose 3–29 deterministic tools each; the authors state
  the gap to production tool surfaces with "hundreds of endpoints,
  non-standard error handling, and partial failures" means results "may not
  fully transfer to more complex settings."[^c5]
- Each model runs each task once; stochastic LLM outputs mean the reported
  numbers carry unmeasured run-to-run variance.
- The taxonomy of 8 trigger scenarios covers single-agent, single-turn tool
  use only — no multi-agent delegation, long-horizon accumulating risk, or
  adversarial prompt injection.
- The LLM judge (GPT-5.4) scores the verbal response; the paper reports
  high but not perfect agreement with human annotators, leaving judge bias
  as an uncontrolled source of error on borderline cases.

## Related

[[abstention]] · [[selection-abstention-asymmetry]] · [[sage-abstention-evaluation]] · [[reversibility]]

[^c1]: liu-2026-agentabstain — "Every instance is a pair (T + , T − ) sharing the same sandbox but differing in a single controlled perturbation δ."
[^c2]: liu-2026-agentabstain — "Act Accuracy (fraction of T + passed), Abstain Accuracy (fraction of T − passed), Paired Accuracy (fraction of pairs where both pass), and Conditioned Abstention Rate (CAR: abstain accuracy conditioned on the paired act task being correct, isolating restraint from baseline capability)."
[^c3]: liu-2026-agentabstain — "the best model (Gemini 3.1 Pro) achieves only 59.5% Paired Accuracy2 , and 13 of 17 models stay below 50%."
[^c4]: liu-2026-agentabstain — "abstention capability is largely independent of general task-solving capability, indicating that scaling task-solving alone will not close this gap."
[^c5]: liu-2026-agentabstain — "Real-world deployments often connect agents to dozens of independent systems with hundreds of endpoints, non-standard error handling, and partial failures. The gap between our sandboxes and production tool surfaces means that results may not fully transfer to more complex settings."
