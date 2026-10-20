---
description: "In a 24-participant VR study, pairing clarification questions with spatially-anchored graphical previews cut conversation rounds to resolve ambiguity, without changing final accuracy."
aliases: ["CQGP", "spatially-anchored graphical previews", "hybrid disambiguation (clarification questions + graphical previews)"]
sources: ["chen-2026-beyond"]
---
# Graphical-preview disambiguation (CQGP)

> Adding a graphical preview to a clarification question, not the question
> alone, is what cuts the number of rounds needed to resolve an ambiguous
> command.

## Definition / Mechanism

CQGP is the full-support condition of a within-subjects VR study of an
LLM-driven geometry editor (DisambVR): whenever the system judges a spoken
edit command ambiguous, it pairs its clarification question with graphical
previews of the candidate readings — a 2D preview image plus a short heading
and description for each option, and a live 3D preview of the edited
geometry, rendered in purple, shown when the user hovers over an option.
"If the user input is ambiguous, the system provides a clarification
question accompanied by a few graphical preview options underneath it. The
options consist of a 2D preview image in the left, and a heading and brief
description in the right. When the user hovers the cursor over the option,
a 3D preview of the edited geometry will be displayed in purple."[^c1]

## Why it matters

Twenty-four participants edited three parametric 3D shapes to match a
target under three conditions — NONE (no disambiguation), CQ (clarification
questions only), CQGP (questions plus previews) — counterbalanced across
condition and geometry. Conversation rounds differed significantly across
conditions (Friedman χ²=25.2, p<.001): NONE M=12.3 (SD=3.57), CQ M=14.3
(SD=3.23), CQGP M=8.23 (SD=2.48); CQGP was significantly lower than both
NONE (T=4.02, p<.001) and CQ (T=7.11, p<.001). "Friedman tests indicated a
significant difference (χ2 = 25.2, p < .001) in the rounds of conversations
of the NONE (M = 12.3, SD = 3.57), CQ (M = 14.3, SD = 3.23), and CQGP (M =
8.23, SD = 2.48) conditions. Post-hoc Conover comparisons revealed a
significant difference in the number of conversations between the NONE and
CQGP condition (T = 4.02, p < .001), as well as the CQ and CQGP conditions
(T = 7.11, p < .001)."[^c2]

No pairwise test reported a significant difference between NONE and CQ, and
CQ's mean round count (14.3) is numerically higher than NONE's (12.3): asking
a clarification question with no graphical support did not measurably lower
interaction cost in this task — only pairing it with the preview did.
Reading this contrast into the round counts above is this wiki's own
inference from the reported means, not a separate significance test the
paper ran.[^c3]

Final task accuracy (a normalized closeness-to-target score) was not
distinguished by any of the three conditions: "Conventional paired t-tests
revealed no statistically significant differences in the maximum closeness
scores between the NONE and CQ conditions (t (23) = 1.97, p = .061), the
NONE and CQGP conditions (t (23) = 0.15, p = .880), or the CQ and CQGP
conditions (t (23) = −1.55, p = .134). Friedman tests also did not reveal a
significant difference across the three conditions (χ2 = 4.75, p = .093)."
The measured benefit is in interaction efficiency (rounds) and progression
stability, not peak accuracy.[^c4]

## Limits

The claim rests on one testbed (DisambVR), one modality (VR geometry
editing with speech input), three parametric shape tasks and N=24; the
paper's own equivalence tests for peak accuracy were statistically
underpowered (8–24% observed power against a ±0.03 bound, versus the ~56–72
participants a conventional 80%-power design would need), so the accuracy
null above is not evidence that the three conditions perform identically —
only that this study could not detect a difference. Conversation-round
count is this system's own operational metric (one system turn / one user
turn), not a general definition of interaction cost, and no comparison
condition varied the preview modality alone (graphical preview without any
clarification question was not tested).

## Related

[[clarification-benchmarks]] · [[sprt]] · [[constraint-as-information]]

[^c1]: chen-2026-beyond — "If the user input is ambiguous, the system provides a clarification question accompanied by a few graphical preview options underneath it. The options consist of a 2D preview image in the left, and a heading and brief description in the right. When the user hovers the cursor over the option, a 3D preview of the edited geometry will be displayed in purple."
[^c2]: chen-2026-beyond
[^c3]: chen-2026-beyond — "the rounds of conversations of the NONE (M = 12.3, SD = 3.57), CQ (M = 14.3, SD = 3.23), and CQGP (M = 8.23, SD = 2.48) conditions"
[^c4]: chen-2026-beyond
