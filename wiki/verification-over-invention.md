---
description: "MAIA tags any brief element the system itself proposes but the user did not say as an unratified hypothesis, blocking it from the brief until the user confirms it."
aliases: ["Verification over Invention", "validator gate"]
sources: ["wang-2026"]
---
# Verification over Invention

> A generated guess is not a constraint until it is said back and confirmed, and the check is routed through a second role that may only answer approved or not.

## Definition / Mechanism

Wang, Lu, Chen & McGraw (2026) name MAIA's governing rule for a multi-agent system that elicits a visual-art commission brief through [[staged-socratic-hint-policy|Socratic]] dialogue: any visual element the AI proposes that is not explicitly present in the user's input is treated as a tentative hypothesis and must be ratified by the user before inclusion.[^c1]

MAIA tracks this per requirement axis with a four-state tag: UNADDRESSED (no information yet), INFERRED (an AI hypothesis that must be ratified before use), EXPLICIT (stated or confirmed by the user), or DISCRETION (deferred to the artist — see [[discretion-tag]]).[^c2]

An INFERRED item is produced freely by the Intent Diagnostician, but the architecture routes it through a second, separately-instructed role, the Response Validator, before the coordinator may show it to the user; that role returns only approved or revision-needed and never authors user-facing content itself.[^c3]

Evidence the gate does something: across the 14 of 16 Maieutic sessions with retained logs, it returned revision-needed in 4 sessions (29%), catching unratified inferences, affective descriptors inflated into visual codes, over-specified DISCRETION dimensions, and missing lay-term definitions.[^c4]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Requirements engineering / multi-agent LLM systems (Wang et al. 2026) | Verification over Invention | exact — the governing principle: unratified AI-proposed content does not count |
| Requirements engineering / multi-agent LLM systems (Wang et al. 2026) | validator gate | close — the architectural role (the Response Validator) that enforces the principle; a rule and the component that applies it are not one object |

## Why it matters

The full MAIA configuration, this rule plus bounded either/or questioning, produced a large, significant gain in Cognitive Support over a minimal single-agent baseline in a within-subjects study (N=16; Wilcoxon r=0.96, p_FDR=0.015), corroborated by blind professional-artist ratings of higher completeness and executability on all eight sampled tasks (rank-biserial r=1.0; task-level Wilcoxon p=0.008, FDR q=0.010).[^c5]

This is the paper's own answer to stall 5 for a system whose own output can masquerade as an answer: an [[elicitation-protocols|answerer's constrained reply]] is checked against a schema, but here it is the *asker's* generated content that is checked before it may count as a constraint at all.

## Transfer

| | |
|---|---|
| In its home field | one bespoke-art-commission harness (MAIA on OpenCode Desktop v1.1.60, every agent MiniMax M2.5 at temperature 0.2), N=16 laypeople, a fixed 8-dimension checklist, one validator role sharing the generator's weights |
| Here | any asker system that lets a generative step propose content on the answerer's behalf before the answerer has said it |
| What survives | tagging AI-proposed content as tentative until the answerer ratifies it, and routing that check through a role built to say only approved or not |
| What does not | true model-independent verification — the paper's own validator shares the generator's weights, so this instance never tested a second, differently-trained judge |

[^c6]

## Limits

- The Cognitive Support gain is measured for the whole configuration (multi-agent architecture, bounded questions and the verification gate together) against a minimal baseline; the authors leave isolating this rule from the rest of the architecture to follow-up work, so the r=0.96 result cannot be attributed to Verification over Invention alone.
- "Structurally independent" means a separate role and prompt, not a separate model: the validator shares the generator's underlying weights, so a systematic failure mode common to both is not something this architecture can catch.
- One model (MiniMax M2.5, OpenCode Desktop v1.1.60, temperature 0.2), N=16, one domain (bespoke visual-art commissioning); there is no cross-model or cross-domain replication.
- The 29% figure is a session-level proportion, 4 of the 14 sessions with retained logs saw at least one revision-needed verdict, not a rate per question or per axis, and the two sessions without retained logs are excluded from it.

## Related

[[elicitation-protocols]] · [[socratic-method]] · [[axis-tag-completion]] · [[discretion-tag]] · [[abstention]]

[^c1]: wang-2026 — "any visual element the AI proposes that is not"
[^c2]: wang-2026 — "I NFERRED (an AI hypothesis"
[^c3]: wang-2026 — "returns only A PPROVED or R EVISION -N EEDED; it never"
[^c4]: wang-2026 — "control (the validator gate): across the 14 Maieutic sessions"
[^c5]: wang-2026 — "Support over a minimal baseline (𝑟=0.96, 𝑝 FDR =0.015; LMM"
[^c6]: wang-2026 — "MAIA on OpenCode (OpenCode Desktop v1.1.60; all agents"
