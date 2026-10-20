---
description: "Scores an agent's non-execution as correct only when it is paired with a positive requirement — a clarification trace, recovery path or semantic explanation — so silence never earns credit by itself."
aliases: ["conjunctive negative-evidence gating", "safe non-execution with positive clarification", "negative-evidence pairing"]
sources: ["qin-2026"]
---
# Conjunctive negative-evidence gating

> An agent that stays silent or refuses to act is not scored as "safe" for
> that reason alone — the benchmark also requires the trace to show *why*:
> a [[clarification-request|clarification request]], a [[recovery-postulate|recovery]] attempt, or a semantic explanation
> tied to the same scenario.

## Definition / Mechanism

Qin, Gu, Jiang et al. (2026) define StructureClaw-Bench's
terminal decisions from both positive and negative evidence together:
"Clarification means that material information remains missing or
ambiguous. Safe non-execution means that analysis should not proceed
because an input is invalid or inconsistent... In particular, the mere
absence of an analysis artifact is not a successful safety response: a
negative case must also satisfy its scenario-specific clarification or
semantic requirement and show that neither an analysis result nor an
analysis-tool invocation was recorded."[^c1]

The construction rule generalizes this: "Absence of a model or analysis may
reflect safe [[abstention]], but it may also reflect an execution failure. The
benchmark therefore pairs negative evidence with a positive scenario
requirement, such as a clarification trace, recovery path, or semantic
explanation. This conjunction prevents non-action from receiving credit
merely because no computation was [performed]."[^c2]

Applied to StructureClaw-Bench's 50 interactive-robustness scenarios: each
clarification or safe-abstention diagnostic exceeds 95% locally across
nine tested models, yet pooled single-attempt end-to-end (E2E) success is
82.6%, and the model with "perfect clarification and abstention
diagnostics" (Claude Opus 4.8) does not have the highest E2E success — "the
gap between these local safety checks and E2E Success shows that
clarification or abstention alone does not guarantee complete workflow
consistency."[^c3]

## Why it matters

On stall 2, this closes a specific scoring hole: a criterion that only
checks whether an agent *acted* or *refused* cannot distinguish a
justified refusal from a stalled or broken agent that produced nothing for
the wrong reason. Gating the negative case on a scenario-specific positive
artifact (the clarification text, the recovery step, the semantic
explanation) is what makes "the agent correctly chose not to act" a
checkable claim rather than an assumption read off an empty output slot.

## Limits

- The conjunction is checked by fixture-defined, scenario-specific
  assertions built for one domain (structural engineering artifacts); the
  paper does not claim the rule generalizes to domains without an
  artifact-comparable ground truth to check the positive half against.
- The gap it exposes (95%+ local diagnostics vs. 82.6% pooled E2E) is
  measured only on StructureClaw-Bench's 50 interactive scenarios across
  nine text-agent configurations; whether the same decoupling appears
  outside structural-engineering workflows is not tested here.
- The rule catches *silent* non-action [[proactive-expertise-clarification|passing]] as safety; it does not by
  itself certify that a clarification request or recovery path is the
  *correct* one for the scenario — that is checked by separate
  scenario-specific assertions, not by the conjunction itself.

## Related

Selection · [[agentabstain-paired-benchmark]] · [[abstention]] · [[defect-localization]]

[^c1]: qin-2026
[^c2]: qin-2026 — "Absence of a model or analysis may reflect safe abstention, but it may also reflect an execution failure. The benchmark therefore pairs negative evidence with a positive scenario requirement, such as a clarification trace, recovery path, or semantic explanation. This conjunction prevents non-action from receiving credit merely because no computation was"
[^c3]: qin-2026
