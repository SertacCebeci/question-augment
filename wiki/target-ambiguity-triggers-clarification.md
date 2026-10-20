---
description: "Coding agents stay action-biased regardless of danger; when they stop to ask, the question tracks a missing target, not vague intent or a large blast radius."
aliases: ["Ask User Rate vs target underspecification", "target-seeking clarification"]
sources: ["ji-2026"]
---
# Target ambiguity triggers clarification, blast radius does not

> Across five coding-agent configurations, the trigger for stopping to ask
> is a missing referent, not the size of the mistake that acting would cause.

## Definition / Mechanism

Pooled over five agent×model configurations on [[underspecbench|UnderSpecBench]]'s
2,208 DevOps prompts, action rate falls only mildly and never to
[[abstention]] as intent clarity (S) or target certainty (B) drops — 72.3%→58.5%
over S, 70.9%→59.5% over B — while it is flat across blast radius (R:
65.5% vs. 64.0%): agents do not act less on operations flagged as
irreversible or production-scale.[^c1]

Conditioned on acted runs, Safe Success falls from 67.9% to 8.6% as target
certainty (B) drops across its four levels, versus a gentler 50.9%→29.4%
fall over the four levels of intent clarity (S), and no fall at all over
blast radius (42.4% vs. 43.0%, R0 vs. R1); Wrong Target and OverScope rise
symmetrically.[^c2]

Refusal is negligible everywhere (≤2.5% of runs); when an agent stops, the
stop is a clarifying question or a silent non-answer, and the question
rate itself is target-seeking: Ask User Rate rises monotonically as the
target axis (B) is underspecified but stays flat across both intent
clarity (S) and blast radius (R), "because a missing target is a
well-formed, answerable question... a vague intent gives it nothing
concrete to ask about... a larger blast radius signals danger but no
missing fact, so it prompts no question."[^c3]

Whether the resulting tendency to ask surfaces at all is set mostly by the
model (Haiku asks 38–45% of the time, DeepSeek-v4 1.7%) and modulated by
the harness: the same Codex-5.1-mini model asks 31.8% of the time under
the Codex-native harness but only 10.5% under OpenCode, where its stops
become silent dry-run Defers instead — "we conjecture that this
modulation is driven by whether the harness exposes an explicit
clarification affordance (a first-class 'ask the user' tool)."[^c4]

## Why it matters

For the stall of which axis to resolve first, this is a negative result
about the mechanism doing the choosing inside deployed coding agents: none
of the three axes is weighted by its cost of being wrong. Danger (blast
radius) does not raise the chance of asking or even of pausing — only
"can I name a concrete missing fact" does, which selects for whichever
[[efe-planning-as-variational-inference|ambiguity]] is easiest to phrase as a question, not whichever is most
consequential to get wrong.

## Limits

The disposition split (Ask/Refuse/Defer) rests on an LLM judge, and the
harness-affordance explanation for why the tendency to ask surfaces is the
paper's own conjecture (kind: interpretation), not a manipulated,
controlled comparison — the paper varies harness and model together across
only five configurations, so model effect and harness effect are not
cleanly separated for every pair. The domain is DevOps/SRE action-taking;
whether "askability" rather than "stakes" governs clarification elsewhere
is untested here.

## Related

[[underspecbench]] · [[reversibility]] · [[clarification-request]] · [[value-of-information]]

[^c1]: ji-2026
[^c2]: ji-2026 — "acted-run Safe Success Rate falls from 67.9% at B0 to 8.6% at B3"
[^c3]: ji-2026 — "Explicit refusal is negligible, at most 2.5% of scored runs for every configuration."
[^c4]: ji-2026 — "The tendency to seek confirmation is primarily a model property: Haiku asks heavily under both scaffolds (38.3% under OpenCode, 44.5% under Claude Code), whereas DeepSeek-v4 almost never asks (1.7%)"
