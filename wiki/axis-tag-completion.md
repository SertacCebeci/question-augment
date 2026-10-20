---
description: "MAIA declares Semantic Saturation once each of five pre-declared visual axes carries a resolved tag, confirmed or deliberately deferred, none left unaddressed or an unconfirmed guess."
aliases: ["Semantic Saturation"]
sources: ["wang-2026"]
---
# Axis-tag completion

> A checklist, not a novelty count: this stopping rule is satisfied the moment every cell of a small, fixed, pre-declared list carries a resolved tag, and it shares its name with a family that measures something else entirely.

## Definition / Mechanism

Wang, Lu, Chen & McGraw (2026) track eight requirement dimensions per commission, five visual (Subject Definition, Composition, Lighting, Color Palette, Artistic Style) and three logistical (Usage/Purpose, Dimensions/Format, Deliverable Specs), each carrying one of the four tags defined in [[verification-over-invention]].[^c1]

A commission reaches what the authors call Semantic Saturation once every one of the five visual axes is tagged EXPLICIT or DISCRETION, with none left UNADDRESSED or an unresolved INFERRED guess; the three logistical axes are not part of this criterion.[^c2]

The Brief Synthesizer then drafts the brief, which the validator re-audits once more under a stricter rule admitting zero remaining INFERRED items before delivery.[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Requirements engineering / multi-agent LLM systems (Wang et al. 2026) | Semantic Saturation | exact — this note |
| Qualitative research | data / thematic / code / meaning / theoretical saturation | not this concept — the family in [[saturation]] and operationalised in [[qualitative-saturation]] counts novelty across a growing sample of many respondents' interviews; this rule instead checks whether a fixed, pre-declared checklist of five axes has each been resolved, inside one session with one answerer |

## Why it matters

Stall 7 already holds two kinds of rule. One thresholds a quantity: [[sprt]] a [[likelihood-ratio|likelihood ratio]], [[value-of-information]] an expected gain, [[qualitative-saturation]] a novelty count over a growing sample. The other thresholds nothing: [[issue-tree]] stops when the frontier is empty, [[attribute-exploration]] when the enumeration is exhausted, and [[stopping-rules]] states the coverage form directly, at least one constraint on every dimension of the [[possible-worlds|hypothesis space]], with [[version-space]]'s S=G as its nearest formal relative. Axis-tag completion belongs to the second kind and is, as far as this wiki holds, the first published instance of that coverage condition applied inside a single elicitation session: a structural completeness test with no threshold, blind to an axis that is not on the list.

What it adds to the coverage row is specific to this instance: the list is a fixed, flat checklist, not a tree that grows as questions are asked; DISCRETION counts as resolved, so "deliberately left unconstrained" satisfies the condition; INFERRED does not count, so the asker's own guess cannot fill a cell; and a stricter second gate, zero INFERRED, runs at delivery after the first criterion has fired. This placement against the wiki's own coverage row and against qualitative saturation is this wiki's reading, not a classification Wang et al. make.

## Limits

- The criterion presupposes the axis list is complete and fixed in advance; an axis absent from the eight-dimension State Object cannot be tagged at all, the same precondition [[stopping-rules]] states for its coverage row.
- Nothing in the paper reports how many turns or questions a session needs to reach Semantic Saturation; only the finished brief's downstream ratings are measured, so the rule's own cost is unmeasured here.
- No result attributes any brief-quality gain to this stopping rule alone: the N=16 within-subjects evidence is for the whole MAIA configuration, and the authors leave isolating the sub-agent architecture from the inquiry strategy to follow-up work, on one model (MiniMax M2.5) in one domain.[^c4]
- The close relation to qualitative research's saturation family is this note's own reading; Wang et al. do not cite or compare against that literature.

## Related

[[stopping-rules]] · [[issue-tree]] · [[qualitative-saturation]] · [[saturation]] · [[verification-over-invention]] · [[discretion-tag]]

[^c1]: wang-2026 — "five visual (Subject Definition, Composition, Lighting, Color"
[^c2]: wang-2026 — "are tagged E XPLICIT or D ISCRETION, leaving no U NAD -"
[^c3]: wang-2026 — "a stricter regime (zero I NFERRED items) before delivery."
[^c4]: wang-2026 — "and leave isolating the sub-agent architecture from the in-"
