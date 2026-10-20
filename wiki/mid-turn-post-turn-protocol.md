---
description: "Three composable trigger conditions — agent-initiated ask, user-initiated interruption, post-completion follow-up — fixing when a scripted user turn reopens an agent's task."
aliases: ["DeskCraft interaction protocol"]
sources: ["wang-2026-deskcraft"]
---
# Mid-turn/post-turn interaction protocol

> A benchmark-construction device that decides, deterministically and
> reproducibly, exactly when a long-horizon agent's execution is
> interrupted by a user turn — separating *who* opens the turn (agent or
> user) from *when* it can open (during execution or after completion).

## Definition / Mechanism

DeskCraft represents an interactive task as a phase sequence
$\Phi=(\phi_1,\dots,\phi_K)$, where each phase pairs a user message with a
trigger condition. Three trigger types close the loop: for **mid-turn**
interaction, occurring while the agent is still executing, `agent_ask`
fires when the agent itself emits an ASK/`call_user` action to solicit
clarification, and `step_count` fires after a predetermined number of
steps, modelling a user-initiated interruption that the agent did not
request; for **post-turn** interaction, `agent_done` fires when the agent
signals completion, letting the (simulated) user verify the deliverable
and issue a follow-up or correction.[^c1]

The three triggers compose freely within one task to produce phase
sequences such as "clarify → interrupt → refine"; scenario families
([[efe-planning-as-variational-inference|ambiguity]] resolution, interruption, progressive refinement, feedback
correction) are analysis labels for which collaborative ability is being
tested, not additional trigger types.[^c2]

Operationally, when the agent emits its `call_user` action the runtime
converts it to a non-executable signal, skips environment execution for
that step, and lets an LLM user simulator — conditioned on the authored
scenario, persona and current phase — generate the next utterance before
the agent's rollout resumes from the same desktop state; persistent user
requirements are kept visible in a bounded history across later steps.[^c3]

## Why it matters

Across 18 agents on 538 long-horizon desktop-GUI tasks built on this
protocol, the best standard-split score (GPT-5.4, 31.6%) drops on the
interactive split (27.6%), and grouped by collaboration mode, tasks that
require the agent to use the `agent_ask` channel have the lowest success
rate of any mode for both tested frontier models — the authors read this
as agents over-committing to an initial guess rather than as a missing
capability, since the Ask channel is available and rarely used.[^c4]

## Transfer

| | Home field | Here | Survives | Does not |
|---|---|---|---|---|
| — | Desktop-agent benchmark engineering (event-driven simulation / scripted rollout control) | Timing and initiation-direction of a clarifying question during long-horizon task execution | The separation of *initiation direction* (agent-initiated vs. user-initiated) from *timing* (mid-execution vs. post-completion) as two independent axes for classifying an interaction turn | Any account of *why* the agent should choose ASK at a given step — the protocol only says which authored condition reopens the loop; the threshold for `agent_ask` is the evaluated policy's own decision, not part of the protocol, and `step_count` is a fixed, scripted stand-in for a real interruption, not a model of when a user actually intervenes |
[^c5.1][^c5.2][^c5]

## Limits

This note's claim rests on one benchmark's construction choices: the
triggers are authored and scripted for reproducibility, so `step_count`
models "user-initiated interruption" only as a fixed step budget, not as
a naturalistic signal of when a human would actually interrupt, and both
the post-turn feedback and the mid-turn responses to `agent_ask` are
produced by an LLM user simulator conditioned on the authored scenario,
not by a human interlocutor. The 27.6%/31.6% comparison is reported for
one model family (GPT-5.4) among 18 evaluated; the protocol itself does
not adjudicate whether a given step was the *right* moment to trigger a
turn, only that the authored condition fired.

## Related

[[clarification-benchmarks]] · [[frame-change-trigger]] · [[entropy-threshold-clarification-trigger]] · [[value-of-information]]

[^c1]: wang-2026-deskcraft — "For mid-turn interaction, occurring while the agent is still executing: agent_ask fires when the agent emits ASK to solicit clarification, and step_count fires after a predetermined number of steps to model user-initiated interruption. For post-turn interaction, occurring after the agent signals completion: agent_done fires when the agent emits DONE, allowing the user to verify deliverables and issue follow-up instructions or corrections"
[^c2]: wang-2026-deskcraft — "Triggers compose freely within a task, enabling phase sequences that interleave them to produce realistic patterns such as “clarify → interrupt → refine.” Scenario families (ambiguity resolution, interruption, progressive refinement, feedback correction) are analysis labels for the collaborative ability being tested, not additional trigger types."
[^c3]: wang-2026-deskcraft — "If Kimi emits call_user, the parser converts it to a non-executable CALL_USER signal, skips environment execution for that turn, and lets the simulator produce a response before rollout resumes from the same desktop state."
[^c4]: wang-2026-deskcraft — "We evaluate 18 proprietary and open source agents on 538 tasks and find that GPT-5.4 reaches 31.6% on standard tasks and 27.6% on interactive tasks."
[^c5.1]: wang-2026-deskcraft — "DeskCraft therefore represents interaction as an executable phase protocol that captures goal evolution while keeping it deterministic."
[^c5.2]: wang-2026-deskcraft — "DeskCraft closes the human-agent interaction loop with a minimal set of three composable trigger types, covering mid-turn and post-turn interaction."
[^c5]: wang-2026-deskcraft
