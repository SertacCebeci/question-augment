---
description: "A six-class taxonomy (ANSWER, REPORT DONE, REFUSE, CONFIRM, CLARIFY, ACT) derived from real assistive-robot dialogue, reliably annotated (kappa 0.72-0.95) and learnable by a fine-tuned VLM."
aliases: ["taxonomy of robot response decisions", "robot response mode taxonomy", "hierarchical taxonomy of robot response modes"]
sources: ["liu-2026"]
---
# Robot response mode taxonomy

> Before a robot acts on an instruction, its move is one of six mutually
> exclusive classes, not a binary clarify-or-act split — and which one is
> chosen is annotatable with substantial human-human and human-AI agreement.

## Definition / Mechanism

Liu, Hawkins, Sultan, Esposito & Dian (2026) retrospectively
annotated 40 Wizard-of-Oz human-robot dialogue episodes (an assistive mobile
manipulator, five indoor tasks) at each robot decision point: "Each decision
point was then assigned one mutually exclusive response mode: ANSWER for
responding to a user question or providing reassurance, REPORT DONE for
announcing task completion, REFUSE for impossible or safety-limited
requests, CONFIRM for verifying a single task inferred by the robot, CLARIFY
when essential task information remained unresolved, and ACT when the
action, object, and required destination were sufficiently specified,"
with CLARIFY turns further split by what is missing — "intent for an
unspecified goal or action, referential for multiple visible candidate
objects, spatial for an unknown location or out-of-view target, and
intelligibility for speech that could not be reliably interpreted."[^c1]

Two human annotators and an AI annotator independently applied the scheme.
Coverage was high and reproducible: "The clean rates for both human
annotators were approximately 90%" and, across decision-point, mode and
[[efe-planning-as-variational-inference|ambiguity]]-type levels, "the results show substantial agreement across all
annotation levels for both the human-human and human-AI comparisons" —
reported Cohen's kappa ranges from 0.72 to 0.95 depending on the level.[^c2]

Applied to the pilot's 184 decision points, the classes were unevenly
populated: "ACT was the dominant response mode, while the other modes
occurred less frequently. Among the 36 CLARIFY decisions, referential and
intent-related ambiguities were most common, whereas spatial and
intelligibility ambiguities were rarely observed."[^c3]

A feasibility check fine-tuned a VLM (LLaVA-1.6-7B) on the taxonomy-derived
labels for ACT and CLARIFY (with its three better-populated ambiguity
subtypes) from images, dialogue history and the current instruction: "the
fine-tuned model demonstrated the ability to classify the two trained
response modes, ACT and CLARIFY, as well as the associated ambiguity
types."[^c4]

## Known as

| Name | Field | Relation |
|---|---|---|
| taxonomy of robot response decisions | the paper's title | exact — the paper's own name |
| robot response mode taxonomy | this wiki | exact — the generalized name used here |
| hierarchical taxonomy of robot response modes | the paper's abstract | exact — same object, abstract's phrasing |

## Why it matters

This is a second, independently derived instance of the finding
[[pre-action-authorization-decision]] reports for vehicle voice commands:
an answerer facing an instruction does not choose between acting and
asking, but among several distinct moves (here: answer, report, refuse,
confirm, clarify, act), and CLARIFY itself is not one move but four,
triggered by different kinds of missing information (intent, referential,
spatial, intelligibility). Unlike the vehicle benchmark's hand-built
reference decisions, this taxonomy is grounded in unscripted, real dialogue
and its class boundaries are shown to be reliably annotatable by independent
humans and by an AI annotator, not merely internally consistent.

## Limits

- One pilot: 40 episodes, 5 participants, one teleoperator with no prior
  [[communication-policy|communication policy]] — the class frequencies (ACT dominant, spatial and
  intelligibility CLARIFY rare) reflect this protocol and task set, not a
  general distribution of robot decisions.
- The taxonomy was built by the same team that then evaluates its own
  coverage and [[calibration|reliability]]; "uncovered" and "forced-fit" cases (up to ~10%)
  are the categories the scheme itself could not cleanly place.
- The learnability result covers only ACT and CLARIFY (three of its four
  ambiguity subtypes); ANSWER, REPORT DONE, REFUSE and CONFIRM were not
  tested for learnability at all.
- Authors describe this as a pilot with a "version 2 taxonomy" still to
  come to fix boundary disputes (decision-point identification, REPORT DONE
  scope); the six-class split is not yet a settled instrument.

## Related

[[pre-action-authorization-decision]] · [[clarification-request]] · [[ambiguity-taxonomy]] · [[value-of-information]]

[^c1]: liu-2026 — "Each decision point was then assigned one mutually exclusive response mode: ANSWER for responding to a user question or providing reassurance, REPORT DONE for announcing task completion, REFUSE for impossible or safety-limited requests, CONFIRM for verifying a single task inferred by the robot, CLARIFY when essential task information remained unresolved, and ACT when the action, object, and required destination were sufficiently specified."
[^c2]: liu-2026 — "The clean rates for both human annotators were approximately 90%"
[^c3]: liu-2026 — "ACT was the dominant response mode, while the other modes occurred less frequently. Among the 36 CLARIFY decisions, referential and intent-related ambiguities were most common, whereas spatial and intelligibility ambiguities were rarely observed."
[^c4]: liu-2026 — "the fine-tuned model demonstrated the ability to classify the two trained response modes, ACT and CLARIFY, as well as the associated ambiguity types."
