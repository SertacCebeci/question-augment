---
description: "A three-stage workflow — Specify, Analyze, Test — where sketch interpretation surfaces unanticipated gaps and drives clarifying dialogue before scenario validation."
aliases: ["Specify-Analyze-Test workflow", "SBAC workflow", "articulation-contestation-ratification"]
sources: ["monteiro-2026"]
---
# Specify-Analyze-Test workflow

> A staged elicitation workflow where the system does not ask questions up front: it lets the user externalize loose preferences by sketching, compiles that sketch into structured policies, and only then surfaces the gaps it finds as targeted clarifying dialogue.

## Definition / Mechanism

Sketch-Based Access Control (SBAC) walks a user through three phases. In **Specify**, the user draws access-control preferences freeform on a canvas; guidance cards scaffold the four ABAC parameters (who, what, action, when) but no AI analysis runs yet. In **Analyze**, the system "compiles" the sketch into structured ABAC policies and evaluates them, surfacing each detected risk, [[efe-planning-as-variational-inference|ambiguity]] or conflict as an insight card the user can resolve conversationally, by editing a policy field, or by editing the sketch. In **Test**, the system generates boundary-probing scenario vignettes from the current policy set and asks the user to confirm, refine or acknowledge the expected outcome.[^c1]

The Analyze phase is the routing step: rather than asking a fixed elicitation sequence, the system only opens a clarifying question where its own compiled policy is ambiguous, risky, or conflicting.[^c2]

A change made in any one modality — sketch, conversation, or the policy panel — propagates to the other two, so a question and its answer stay attached to the same represented entity across turns.[^c3]

In a 14-participant user evaluation grounded in participants' own real-world access-control scenarios, the workflow "helped participants progressively refine initially underspecified preferences into more complete and precise policies — surfacing gaps they had not anticipated, resolving ambiguities through dialogue, and validating policy behavior through concrete scenarios."[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| human-computer-interaction | SBAC (Sketch-Based Access Control) workflow | exact |
| human-computer-interaction | articulation–contestation–ratification | exact |

The paper reframes its own three phases in the discussion as articulation (Specify), contestation (Analyze) and ratification (Test) — the same object under a second name, not a different mechanism.

## Why it matters

It separates *forming* a preference from *finding a gap in it*: freeform sketching is the mechanism for preferences the user has not yet fully formed, while system-driven analysis is the mechanism for gaps the user has formed a preference about but did not think to state. A fixed elicitation-question sequence conflates the two and asks before the user has anything to answer with.

## Limits

The claim rests on one system, one domain (household access control), and a single-session exploratory design: "a single-system exploratory design with scenarios limited to at most two devices and two groups, in ∼60-minute sessions without real deployment."[^c5]

The system gives no formal completeness guarantee — "the LLM provides soft validation without formal guarantees of completeness, consistency, or correctness" — and whether the staged structure transfers outside access control "remains a hypothesis for future study, not a claim established here."[^c6]

## Related

[[possible-worlds]] · [[constraint-as-information]] · [[subjective-contextual-incompleteness]]

[^c1]: monteiro-2026 — "The card carousel, which displayed guidance cards in the Specify phase, now displays insight cards, each surfacing a specific risk, ambiguity, or conflict identified in the policy set."
[^c2]: monteiro-2026 — "Users can respond to insight cards in three ways: conversationally, directly editing policy fields in the policy panel, or modifying the sketch."
[^c3]: monteiro-2026 — "Changes in one modality propagate to the others."
[^c4]: monteiro-2026 — "In a user evaluation with 14 participants grounded in their real-world access control scenarios, we found the system and the workflow helped participants progressively refine initially underspecified preferences into more complete and precise policies—surfacing gaps they had not anticipated, resolving ambiguities through dialogue, and validating policy behavior through concrete scenarios."
[^c5]: monteiro-2026 — "We used a single-system exploratory design with scenarios limited to at most two devices and two groups, in ∼60-minute sessions without real deployment."
[^c6]: monteiro-2026 — "the LLM provides soft validation without formal guarantees of completeness, consistency, or correctness"
