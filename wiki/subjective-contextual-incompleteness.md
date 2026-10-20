---
description: "Two distinct gaps in a stated preference — not yet having formed one (subjective) versus omitting context that later matters (contextual) — closed by different elicitation mechanisms."
aliases: ["subjective incompleteness", "contextual incompleteness"]
sources: ["monteiro-2026"]
---
# Subjective vs. contextual incompleteness

> An incomplete preference is not one thing: the user may not yet have decided, or may have decided but left out a condition that only matters in a context they did not think of. The two call for different asking mechanisms, not the same clarifying question.

## Definition / Mechanism

Monteiro & Das distinguish two failure modes in stated access-control preferences. **Subjective incompleteness** is "not yet having fully formed preferences" — the user has not decided what they want. **Contextual incompleteness** is "gaps, ambiguities, and risks in under-specified policies" — the user has a preference but has not stated the conditions that would make it enforceable.[^c1]

In their study, freeform sketching addressed subjective incompleteness: "11 of 14 [participants] added relationships and conditions that were absent from their initial free-text preferences" while drawing, without any system prompt.[^c2]

Contextual incompleteness was instead addressed by the system's own gap-detection pass: participants "addressed contextual incompleteness … through the system-driven analysis and testing stages, which helped them identify and resolve issues they had not noticed on their own."[^c3]

The wiki's inference: the two types name different axis-selection problems. Subjective incompleteness has no axis yet to select — the mechanism that helps is one that lets the user generate candidate axes (open-ended sketching), not one that scores and asks about an axis already named. Contextual incompleteness does have a named axis, silently under-constrained; the mechanism that helps is the system flagging the specific under-constrained cell and asking about that cell alone.[^c4]

## Why it matters

A single elicitation-question policy is mismatched to at least one of the two: asking a structured question when the user has not yet formed an opinion produces a forced, low-information answer; waiting for the user to volunteer a well-formed preference before ever asking misses gaps the user does not know to mention.

## Limits

The distinction rests on one study of 14 participants in one domain (household access control), and the classification of which participant behavior counts as "subjective" versus "contextual" is the authors' own post-hoc coding of think-aloud and interview data, not an independently validated instrument.

## Related

[[specify-analyze-test-workflow]] · [[possible-worlds]] · [[constraint-as-information]]

[^c1]: monteiro-2026 — "Participants addressed subjective incompleteness—not yet having fully formed preferences—through sketching"
[^c2]: monteiro-2026 — "11 of 14 added relationships and conditions that were absent from their initial free-text preferences"
[^c3]: monteiro-2026 — "which helped them identify and resolve issues they had not noticed on their own"
[^c4]: monteiro-2026 — "Participants addressed contextual incompleteness—gaps, ambiguities, and risks in under-specified policies—through the system-driven analysis and testing stages, which helped them identify and resolve issues they had not noticed on their own."
