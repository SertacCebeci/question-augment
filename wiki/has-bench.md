---
description: "HAS-Bench evaluates LLM-based human-agent systems by configuring the level, channel and timing of human participation and scoring both task outcomes and process-level collaboration behavior."
aliases: ["HAS-Bench", "HAS-Framework"]
sources: ["wu-2026"]
---
# HAS-Bench

> A benchmark that treats the choice of *how much a human participates* as
> an experimental variable, not a fixed setting, and scores the resulting
> collaboration process, not only whether the task finished.

## Definition / Mechanism

HAS-Framework models humans and LLM agents as nodes of one interaction
graph with explicit roles, permissions, communication paths and action
authority. HAS-Bench, built on it, evaluates systems under configurable
human participation across two axes: five **agency levels** — A1 full
automation (agent alone) through A3 equal partnership (default) to A5
human-driven — and three **interaction channels** — clarification (resolve
missing or ambiguous input before the agent commits), feedback (correct
the agent's intermediate output) and control (authorize or veto risky
actions before execution), each usable at the agent's request or the
human's own initiative.[^c1]

Across six task domains (service-oriented, retail, open-ended expert
coding, negotiation/bargaining, telecom, airline, research), the same task
is run at different agency levels and scored on both task outcomes
(Pass@1, Task Score, HAS Rescue Rate) and process-level metrics —
[[clarification-quality-score|Clarification Quality Score]], Feedback [[information-utilization-rate|Utilization Rate]], Control Request
Justification, Action Safety Rate, Initiative [[entropy|Entropy]] and Human
Intervention Rate — computed from the execution trace.[^c2]

## Why it matters

Raising the agency level does not move clarification quality the same way
in every domain: from A1/A3 to A4, Coding's Clarification Quality Score
stays near ceiling (0.99 → 0.97) while its Feedback Utilization Rate falls
(0.20 → 0.16); in Research both improve (0.71 → 0.90 and 0.54 → 0.60). The
paper reads this as agency level changing not just how much a human
intervenes but how that intervention is incorporated — a domain-dependent
effect, not a monotone one.[^c3]

Giving the agent more human input is not uniformly a gain even within one
run: A4 rescues 27 tasks that failed under A3 but breaks 13 that A3 had
solved, traced to premature interventions or redundant, distracting input.
This is evidence, at the level of a whole benchmark rather than one
theorem, that *when* a channel opens matters as much as *whether* it does.[^c4]

## Limits

The process metrics (Clarification Quality Score etc.) are LLM-judge
scores against a rubric, not a ground-truth measure of information gained;
the agency-level results above are reported for two of six domains
(Coding, Research) with specific [[backbone-of-a-formula|backbone]] models, and the paper itself
flags Human Intervention Rate as a cost/intensity statistic that does not
track task performance — a higher rate is not claimed to be better.

## Related

[[clarification-benchmarks]] · [[value-of-information]] · [[bounded-rationality]]

[^c1]: wu-2026 — "A1 Full automation — Agent alone, no human. A2 Minimal input — Agent runs; human confirms key steps. A3 Equal partnership (default) — Equal partners, back-and-forth. A4 Agent-assisted — Human leads; agent assists. A5 Human-driven — Human-driven; agent on call."
[^c2]: wu-2026 — "Process-level metrics, computed from execution traces, characterize how collaboration unfolds: Clarification Quality Score (CQS), Feedback Utilization Rate (FUR), Control Request Justification (CRJ), Action Safety Rate (ASR), Initiative Entropy (Hinit ), and Human Intervention Rate (HIR)."
[^c3]: wu-2026
[^c4]: wu-2026
