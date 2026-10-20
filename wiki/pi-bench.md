---
description: "A 100-task long-horizon benchmark that scores an LLM personal-assistant agent's proactive discovery of unstated user intents separately from its completion of the visible task."
aliases: ["π-Bench", "pi-bench"]
sources: ["zhang-2026-bench"]
---
# π-Bench

> Underspecified requests hide requirements that only surface as a session unfolds; Zhang et al. (2026) ask whether an agent surfaces them itself before the user has to, and score that separately from whether the task ends up done.

## Definition / Mechanism
π-Bench places an evaluated agent in a persistent project workspace across 5 user personas, each an episode of 20 multi-turn sessions with cross-session dependencies. Each session is annotated with a set of hidden intents $I=\{i_1,\dots,i_m\}$ — "a latent requirement that should shape how the task is handled, e.g., constraints, preferences, and downstream dependencies" — that are absent from the initial request but recoverable from prior sessions, workspace artifacts, or a targeted question. As the interaction proceeds, a simulated user agent assigns each intent exactly one terminal status: "completed: the agent resolves i without the user explicitly stating it... inferred: the agent asks a focused question that directly targets i, and the user reveals the missing requirement in the next turn... provided: the agent neither resolves i nor asks a relevant question, and the user must proactively supply i to move the task forward." A session terminates only once every intent has a terminal status.[^c1]

The benchmark reports two scores over the same trajectory $H$ rather than one blended score: proactivity, $\mathrm{PROC}(H) = (|I_{com}|+|I_{inf}|)/|I|$, "the fraction of intents that the agent resolves proactively, either by direct completion or by targeted elicitation," giving completion and elicitation equal credit as agent-driven discovery; and completeness, $\mathrm{COMP}(H)$, the mean rubric- or rule-based grader score over the task's checklist items. Because the simulated user eventually discloses any intent the agent fails to elicit, a purely reactive agent can still finish the visible task — "the final trajectory can contain the full set of intents even when the agent passively waits for user-provided information" — so $\mathrm{COMP}$ alone cannot detect passivity; $\mathrm{PROC}$ is the score built to isolate it.[^c2]

Across nine frontier models, the two scores rank models differently: "Kimi K2.5 attains a relatively high COMP score but a much lower PROC score, suggesting that it can execute tasks once constraints are stated, yet often waits for the user to reveal those constraints step by step... Seed2.0 Pro shows the reverse pattern, with higher PROC than COMP, indicating that early discovery of hidden intents is not sufficient when final execution remains weak." The paper reads this as "a practical decoupling between proactivity and completeness, where reactive [[recovery-postulate|recovery]] can preserve final task quality while shifting requirement discovery back to the user."[^c3]

## Why it matters
For stall 2 (which axis first), π-Bench is a mechanism-isolating instrument rather than a selection rule: it does not tell an agent which hidden intent to chase, but it gives a way to tell, after the fact, whether an agent chased any of them at all versus waited for the environment to supply them anyway. A selection policy tuned only against a task-completion metric — the common target in agent benchmarks the paper surveys — can look competent while never initiating a question, because the simulated (or real) user's eventual disclosure repairs the visible outcome.

## Limits
The decoupling claim rests on nine specific frontier models under one agentic scaffold (adapted from Nanobot) and one grader configuration (GPT-5.4 as both user agent and rubric judge), so the direction and size of the PROC/COMP gap may reflect that scaffold and grader as much as the models. All 100 tasks and their hidden-intent annotations are the authors' own construction across five personas, not an independently replicated dataset, and this is a 2026 arXiv preprint, not yet peer reviewed. The `inferred` category folds asking into "credit equal to completed," so π-Bench does not itself distinguish a well-timed question from a late one, only whether one was asked before disclosure.

## Related
[[mutual-information]] · [[value-of-information]] · [[clarification-benchmarks]] · [[aspi-benchmark]]

[^c1]: zhang-2026-bench
[^c2]: zhang-2026-bench
[^c3]: zhang-2026-bench
