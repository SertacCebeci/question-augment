---
description: "A critic agent restricted to asking clarification, constraint, causal and counterexample questions — never proposing answers — forces a hypothesis agent to revise its own physical model."
aliases: ["Socratic midwifery", "Socratic physics critic", "physics-critic agent"]
sources: ["zeng-2026"]
---
# Socratic physics critic

> A role-separated agent whose only output channel is a question — never a
> proposed correction — interrogating another agent's scientific hypothesis
> until it revises itself.

## Definition / Mechanism

In AHOIS, a five-agent system tested on a real multimode-fibre optical
platform, one agent (Boxue) proposes physical hypotheses and experimental
plans; a second agent (Duzhi) is architecturally restricted to interrogating
Boxue's reasoning rather than supplying a correction of its own. The
interrogation runs at four fixed levels: clarification (define terms,
separate measured from inferred quantities), constraint-checking (does the
claim respect the platform's optical and hardware limits), causal probing
(trace the full chain from modulation to measurement) and counterexample
generation (does the claim survive a changed object, modality or sampling
condition) Zeng et al. (2026). Duzhi "was constrained to
question rather than propose candidate mechanisms, research directions or
preferred conclusions. Its role was to expose ambiguous definitions,
unsupported assumptions, unresolved contradictions and incomplete causal
links in Boxue's current account of the optical system."[^c1]

A direct-correction variant of the same role (a "non-[[staged-socratic-hint-policy|Socratic]]" critic that
tells Boxue what is wrong) produced weaker downstream outcomes than the
question-only version: it substituted its own corrective statements for
Boxue's reasoning rather than forcing Boxue to resolve the inconsistency
itself. "Non-Socratic Duzhi identified weaknesses more directly, but often
replaced Boxue's reasoning with corrective statements. In contrast, Socratic
Duzhi forced Boxue to resolve inconsistencies itself, preserving the
distinction between guided inquiry and answer provision."[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Multi-agent scientific discovery (Zeng et al. 2026) | Socratic midwifery | `exact` — the paper's own name for the computational principle |
| Multi-agent scientific discovery (Zeng et al. 2026) | Socratic physics critic / "Duzhi" | `exact` — the agent role implementing it |
| Ancient philosophy | Socratic elenchus | **not this concept** — see [[socratic-method]]: the elenchus is purely refutative and ends in aporia (a withdrawn certainty, no replacement supplied); this mechanism is constructive — its loop ends in a revised, more internally consistent hypothesis Boxue itself constructs. |

## Why it matters

This is a source-of-constraint design: instead of an oracle answering a
question directly, a second agent whose only permitted move is to ask is
placed between the hypothesis-generator and acceptance. The constraint comes
from the *structure* of the interrogation (which classes of question are
asked, what they force the other agent to state) rather than from any
assertion the critic makes.

## Transfer

| | |
|---|---|
| In its home field | Socratic maieutics/elenchus (ancient philosophy): a human questioner elicits or refutes a human interlocutor's stated thesis through dialogue, typically ending in aporia rather than a constructed replacement account ([[socratic-method]]). |
| Here | An LLM agent is given a question-only output role and set against another LLM agent's stated hypothesis about a real optical experiment, under human supervision. |
| What survives | The role separation: the critic may expose gaps (ambiguous terms, unmet physical constraints, missing causal links, claims that do not generalise) but is held to withholding the corrected content itself. |
| What does not | No aporia or terminal state — the loop is scored to convergence (rising physics-consistency, completeness and [[calibration]] scores) rather than ending in acknowledged ignorance; no interlocutor "committing to theses" in the classical sense — Boxue's compliance is a role constraint on an LLM, not a human's assent to premises. |

## Limits

- The comparison against a generic reviewer and a non-Socratic critic is one
  ablation, on the paper's own rubric (physics consistency, hypothesis
  completeness, uncertainty calibration), on one experimental platform (a
  multimode-fibre optical testbed) — `zeng-2026` `[?]` until the verifier
  confirms; no independent replication is cited.
- "Constrained to question rather than propose" is a role/prompting design
  choice the paper describes and evaluates by outcome; it does not report an
  architectural check that Duzhi's outputs never contain a proposed
  correction, so the constraint's enforcement is behavioural, not provable.

## Related

[[socratic-method]] · [[dialectic-red-team]]

[^c1]: zeng-2026
[^c2]: zeng-2026
