---
description: "A lightweight PPO policy chooses which prerequisite-graph node an LLM tutor teaches next and how many dialogue turns to spend, decoupling axis selection from question phrasing."
aliases: ["decomposed curriculum sequencing", "PPO tutoring policy", "sequencing-dialogue decomposition"]
sources: ["tio-2026"]
---
# Curriculum sequencing policy

> Splits "which axis to teach next" from "how to ask about it": a small
> reinforcement-learned policy answers the first, an LLM the second — and
> the split, not a bigger LLM, is what closes the gap on long, unstructured
> tutoring sessions.

## Definition / Mechanism

Given a student query, the system builds a prerequisite knowledge graph $G$
whose nodes are subtopics and whose edges are dependency relations; the
query sits at the root. Tutoring is cast as a POMDP: the true state is each
node's mastery, hidden behind a per-node difficulty threshold $k_v$ that the
policy never observes; the action is which node $a_t \in V$ to teach next;
the observation is the student's response together with summary statistics
of the per-node response history and the graph structure; the reward is
+10 for mastering the root and a small per-step penalty otherwise. A policy
$\pi_\theta$ trained with PPO on this POMDP — in simulation, against a
binary student model, with domain randomisation over topic, per-node
difficulty and prior knowledge — decides only the sequencing/pacing
question; a separate LLM conducts the [[staged-socratic-hint-policy|Socratic]] exchange at the chosen node
and returns a mastery judgement the policy consumes as its next
observation.[^c1]

Across 10 held-out STEM and non-STEM topics, pairing this policy with a
7B-parameter LLM (PPO+Qwen2.5: 78.0% success; PPO+TutorRL: 82.0%) beats
every monolithic LLM-only tutor evaluated the same way, including
frontier general-purpose models (GPT-5-mini: 3.3%; Gemini-Flash: 23.3%)
and a Socratic-specialised model, on both the fraction of sessions that
reach full mastery and the number of turns needed; the same frontier
models reach near-optimal performance once handed the ground-truth mastery
signal directly, so the failure is not a lack of domain understanding but
an inability to do three things — sequence, dialogue, and infer state —
at once.[^c2]

## Why it matters

For stall 2 this is a working instance of "decide the axis first, with a
mechanism separate from the one that phrases the question": the sequencing
decision (which prerequisite to teach) is answered by a policy trained
purely on graph/mastery structure, never on dialogue text, and this
separation — not a larger dialogue model — is what the paper credits for
the gain.[^c3]

## Transfer

| | Home field (control/RL) | Here (question sequencing) | Survives | Does not |
|---|---|---|---|
| PPO | continuous-control policy optimisation over a fully simulated MDP | curriculum-node selection over a POMDP with a hidden per-node threshold | the actor trained in cheap simulation, deployed by composing its action with a separate executor | the reward signal itself — real student responses are natural language, so training uses a hand-specified binary proxy student, not the LLM-judged signal used at inference[^c4]

## Limits

The reported gains rest on an LLM-simulated, prompt-defined student
(Qwen2.5-14B-Instruct as respondent and the tutor LLM as judge of its own
correctness), and on a hand-specified reward/threshold model of mastery
($k_v$ Poisson-distributed, mastery a hard step function); the paper does
not evaluate against real human students, so whether the sequencing gain
survives noisier real natural-language responses and genuine (not
simulated) prior knowledge is untested here.[^c5]

## Related

[[optimal-decision-tree]] · [[adaptive-submodularity]] · [[semantic-entropy]] · [[bounded-rationality]]

[^c1]: tio-2026 — "A lightweight PPO policy handles this sequencing decision, while an LLM conducts the Socratic exchange at the chosen node and returns a signal of student progress."
[^c2]: tio-2026 — "decomposing the task into a learned sequencing policy paired with a small LLM instructor outperforms every monolithic LLM-only method evaluated under the same conditions. Both PPO + TutorRL and PPO + Qwen2.5 substantially exceed the LLM-only and heuristic baselines, despite the LLM in each case being a 7B-parameter model."
[^c3]: tio-2026
[^c4]: tio-2026 — "Training is performed entirely in simulation, with student responses yt generated from the binary stochastic model in Equation 1 and no language model in the loop."
[^c5]: tio-2026 — "For scalability, we use an LLM as a student simulator; our focus is on LLM tutoring behaviour in unstructured settings and its ability to exploit structure when provided."
