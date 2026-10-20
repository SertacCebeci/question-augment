---
description: "A paired benchmark on AgentDojo that isolates clarification-seeking as a distinct agent state, holding task, attacker goal and environment fixed and varying only interaction state and channel."
aliases: ["ASPI", "Ambiguous-State Prompt Injection"]
sources: ["sehwag-2026"]
---
# ASPI benchmark

> To attribute a security effect to the act of asking rather than to some other difference between scenarios, Sehwag et al. (2026) build a paired benchmark where the only thing that changes between the two conditions being compared is whether the agent had to request clarification first.

## Definition / Mechanism
ASPI (Ambiguous-State Prompt Injection) starts from AgentDojo's fully specified tasks and attacker goals and derives an underspecified twin of each: "the pipeline produces a base prompt by removing exactly one piece of user-provided information required for correct execution. The resulting prompt is intentionally underspecified, necessitating the agent to request clarification before proceeding." The execution twin and the clarification twin share task, attacker goal, environment and scoring function, so a difference in attack success between them is attributable to interaction state and delivery channel rather than to task difficulty: "ASPI builds on AgentDojo (Debenedetti et al., 2024) and constructs controlled comparisons in which the task, attacker goal, environment, and scoring functions are held fixed while varying the agent's interaction state and the channel through which adversarial content is delivered."[^c1]

The design is deliberately conservative about what it can claim: single-slot removal is "the minimal clarification setting, involving one question and one expected answer of a known type, where filtering extraneous content is easiest," against multi-slot, multi-turn real-world [[efe-planning-as-variational-inference|ambiguity]] that the authors expect to expose more attack surface — "real-world ambiguity often involves multi-slot omissions, multi-turn dialogue, or open-ended requests, producing longer and less constrained interactions with greater injection surface. As a result, the attack success rates we report are likely an underestimation."[^c2]

The benchmark also separates the source of an effect (interaction state vs. delivery channel) by running the same attack content through the tool channel and the user/`ask_user` channel under both execution and clarification, rather than a single condition per state — the design that supports [[clarification-injection-vulnerability]]'s decomposition claim.

## Why it matters
A protocol for measuring the security cost of asking, separable from other differences in the scenario, is a prerequisite for putting that cost into a selection rule such as [[value-of-information]]'s $\mathrm{Cost}(q)$ term rather than treating it as an unmeasured qualitative worry. Without a paired control, a raw comparison of attack rates in clarification-heavy vs. clarification-light deployments would confound interaction state with which tasks happen to be ambiguous.

## Limits
The benchmark is built on top of AgentDojo's four domains (workspace, messaging, travel, banking) and its deterministic scoring; scenarios and attacker goals outside that coverage are untested. Single-slot, one-round ambiguity is the only ambiguity structure constructed, and the paper states its own rates likely underestimate multi-slot or multi-turn settings. This is a 2026 arXiv preprint, not yet peer reviewed, and the benchmark's 728 instances are the authors' own construction, not an independently replicated dataset.

## Related
[[clarification-injection-vulnerability]] · [[value-of-information]] · [[self-answering-injection-compliance]]

[^c1]: sehwag-2026 — "the pipeline produces a base prompt by removing exactly one piece of user-provided information required for correct execution. The resulting prompt is intentionally underspecified, necessitating the agent to request clarification before proceeding."
[^c2]: sehwag-2026 — "real-world ambiguity often involves multi-slot omissions, multi-turn dialogue, or open-ended requests, producing longer and less constrained interactions with greater injection surface. As a result, the attack success rates we report are likely an underestimation."
