---
description: "A 2,208-prompt DevOps benchmark that varies action, target and environment clarity independently and scores coding agents by which action boundary they cross, not by task completion."
aliases: ["UnderSpecBench", "action-boundary violation benchmark", "Safe Success / Wrong Target / OverScope taxonomy"]
sources: ["ji-2026"]
---
# UnderSpecBench

> A benchmark that stops scoring coding agents by whether they finished the
> task and starts scoring them by which boundary they crossed to get there.

## Definition / Mechanism

UnderSpecBench holds 69 DevOps task families fixed (same environment, same
ground-truth safe action) and varies only the natural-language instruction
along three orthogonal axes: **S** (intent clarity, 4 levels — how
explicitly the requested action is named), **B** (target certainty, 4
levels — how uniquely the object is identified) and **R** (blast radius, 2
levels — contained vs. shared/irreversible surface), for 69 × 32 = 2,208
prompt variants. A deterministic, hand-written oracle per task compares a
before/after state diff against an intended-object set and an
over-scope set, emitting three booleans — `Intended`, `WrongTarget`,
`OverScope` — from which Safe Success, Wrong Target Rate, OverScope Rate
and Overstep Rate (Wrong Target ∨ OverScope) are computed; runs with none
of the three signals are Under Completion, further split by an LLM judge
(human-validated, Cohen's κ = 0.860) into Ask / Refuse / Defer.[^c1]

Across five agent×model configurations (OpenCode, Claude Code and Codex
harnesses over Haiku-4.5, Codex-5.1-mini and DeepSeek-v4), 55.8–67.8% of
runs violate at least one boundary, and acted-run Safe Success falls from
67.9% at B0 to 8.6% at B3 while Wrong Target rises from 9.6% to 75.1% —
target underspecification, not blast radius, is what degrades action
quality.[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper | UnderSpecBench | exact |
| This paper (internal) | the Safe Success / Wrong Target / OverScope taxonomy | exact — the scoring scheme the benchmark is built from |

## Why it matters

It gives the "should this axis be resolved before acting" question in
agent safety a scored answer per axis instead of an aggregate pass/fail:
which of several concurrent ambiguities (what to do / on what / how
dangerous) actually predicts a bad outcome, separately from whether the
agent merely finished the task.

## Transfer

| | |
|---|---|
| Home field | Access control — NIST's Attribute-Based Access Control (ABAC), where an authorization decision needs the subject, action, object and environment attributes |
| Here | The three non-subject ABAC attributes become the benchmark's three independent underspecification axes: action → S, object → B, environment → R |
| What survives | The attribute decomposition itself: that "can this be acted on safely" factors into three independently-perturbable facts an instruction can leave unstated |
| What does not | ABAC's actual decision procedure (policy evaluation against attributes to grant/deny) — UnderSpecBench uses the attributes only to construct test instructions, not to compute an authorization verdict |

[^c3]

## Limits

The oracle is deterministic and per-task, but the Ask/Refuse/Defer split
behind Under Completion rests on an LLM judge, validated only on a
100-case human-annotated subsample (85/100 exact agreement, κ = 0.860
excluding 7 unclear cases) — not on the full 2,208 × 5 run set. The domain
is DevOps/SRE shell-and-API actions in sandboxed containers with five
agent×model configurations; the axis-dominance finding is not shown to
transfer outside this action space.

## Related

[[clarification-benchmarks]] · [[reversibility]] · [[clarification-request]]

[^c1]: ji-2026 — "The resulting 2,208 prompt variants are evaluated with deterministic, side-effect-based oracles that separate Safe Success, Wrong Target, and OverScope outcomes; non-action runs are further classified as clarification, refusal, or deferment."
[^c2]: ji-2026 — "55.8–67.8% of runs violate at least one boundary. Target underspecification sharply degrades action quality, while blastradius cues barely reduce action propensity."
[^c3]: ji-2026
