---
description: "A benchmark-agnostic framework that converts any failure-free tool-use benchmark into a controlled robustness test by assigning each episode an explicit solvability class."
aliases: ["Bench2Robust", "BENCH2ROBUST"]
sources: ["chen-2026-retry"]
---
# Bench2Robust

> A benchmark-agnostic layer that turns any failure-free tool-use benchmark into a controlled test of [[recovery-postulate|recovery]] behaviour, by assigning each episode an explicit solvability class instead of injecting undifferentiated noise.

## Definition / Mechanism

Bench2Robust interposes between an agent and tool execution: any benchmark exposing a `tool_call(name, args) → response` interface can be adapted via a thin adapter, and only the observed tool response is corrupted — the benchmark's latent task state and evaluator are unchanged.[^c1]

Each episode is additionally assigned a solvability class before injection: in S1 (retry_works) no path is permanently blocked, so retrying the same tool recovers; in S2 (switch_needed) the primary path is blocked for the whole episode and only a fallback-equivalent tool completes the task; in S3 (impossible) every task-relevant path is blocked, making escalation the appropriate behaviour.[^c2]

## Why it matters

Because the scenario class is fixed independently of the stochastic per-call noise, a policy's behaviour on realized S1 versus S2 episodes can be scored separately — separating recovery-policy quality from environmental luck, which undifferentiated noise injection cannot do.

## Transfer

| | |
|---|---|
| home field | POMDP planning — a latent-state process observed through a noisy channel |
| here | the clean benchmark's transition and reward are kept exactly; only the observation kernel is corrupted, formalized as a POMDP with a corrupted observation kernel layered over the clean one |
| what survives | the separation of a stochastic per-call noise budget from a deterministic, episode-persistent scenario block (S1/S2/S3) |
| what does not | the framework does not solve the POMDP — no belief-state [[planner-dynamic-stopping|planner]] is built from it; the formal object states the corruption, it is not given to the agent under test |

[^c3]

## Limits

S3 (the abstain-requiring scenario) is used only during training, not in the held-out S1/S2 evaluation, because the underlying benchmark evaluators award no positive completion credit for an unsolvable task — the authors state their held-out evidence covers retry and switch selection and does not claim fully learned [[abstention]].[^c4]

## Related

[[bayesian-tool-memory]] · [[tool-use-robustness-gap]] · [[scenario-curriculum-rl]] · [[bounded-rationality]]

[^c1]: chen-2026-retry — "B ENCH 2ROBUST is a benchmark-agnostic injection framework that interposes between agent and tool execution. Any benchmark following the tool_call(name, args) → response pattern can be integrated via a thin adapter"
[^c2]: chen-2026-retry — "in S1, no path is permanently blocked and retrying can recover; in S2, the primary path is blocked episode-wide and completion requires a fallback-equivalent tool; in S3, all available paths are blocked, defining the environment state in which escalation is appropriate."
[^c3]: chen-2026-retry — "We formalize the injected environment as a POMDP Minj = (S, A, O, T, Zinj , R, γ) with the same latent state transition T (st+1 | st , at ) and reward R as the clean benchmark, but a corrupted observation kernel"
[^c4]: chen-2026-retry — "S3 is used as a training scenario in the current study, but because our task evaluators do not assign positive task-completion credit to impossible episodes, our held-out behavioral evidence focuses on retry and switch selection; we do not claim fully learned abstention."
