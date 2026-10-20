---
description: "Making a system's committed interpretation of an ambiguous query visible raises measured inspectability but only sometimes raises the rate at which users correct a wrong interpretation."
aliases: ["visibility-repair gap", "visibility-action gap"]
sources: ["lee-2026-player"]
---
# Visibility-action gap

> Showing the answerer's assumed interpretation is not the same as making
> the asker fix it — transparency and correction are separate design axes,
> not one lever.

## Definition / Mechanism

In a within-subjects study (N = 16) comparing an XR sports-viewing system
that externalizes its interpretation of ambiguous spoken queries against a
voice-only baseline, externalization significantly raised three of four
Likert inspectability items — identifying which player was meant
(Mext = 5.94 vs Mbase = 4.69, p = .011), which moment (Mext = 6.25 vs
Mbase = 4.69, p = .003), and which alternatives were considered
(Mext = 4.75 vs Mbase = 3.62, p = .024) — and raised the rate of explicit
repair language overall (Mext = 5.6% vs Mbase = 3.3%, p = .039).[^c1]

Despite this, in trials where the system's interpretation was deliberately
misaligned with intent, participants corrected it in only 38% of trials,
leaving a 62% gap between externalized visibility and corrective action; no
single [[efe-planning-as-variational-inference|ambiguity]] type showed a significant repair increase on its own, and
the size of the gap varied by ambiguity type (large but non-significant
effects for temporal and metric queries; near-zero effect for referential
and spatial queries).[^c2]

The paper's own reading of this pattern is that the binding constraint is
**correction cost**, not the quality of the transparency: repair required a
verbally precise correction in a speech-only interface, and where a
cheaper acceptance (e.g. a "close enough" spatial zone) was available,
users took it instead of repairing.[^c3]

## Why it matters

For a clarification mechanism on the answerer's side, this is a
counter-example to the assumption that exposing uncertainty is sufficient
for it to be used: inspectability and correction are measured here as two
separable outcomes with different design levers, so a note or a system that
reports only "users could see the ambiguity" has not shown that ambiguity
gets fixed.[^c4]

## Limits

The baseline (voice-only) confounds externalization with added visual
richness, so the effect cannot be isolated to interpretation-exposure per
se; the paper argues the confound does not explain the 38% ceiling (no
increase in confirmation time, selective rather than uniform inspectability
gains) but does not rule it out. Misalignment was induced by prompt
manipulation, not naturally occurring, and correction was routed only
through speech, which the authors note imposes its own cost floor;
`replicated: false` because this is a single N = 16 study with the authors
themselves flagging several per-type effects as underpowered.[^c5]

## Related

[[interpretation-externalization]]

[^c1]: lee-2026-player — "Inspectability was significantly higher under externalization on three of four items (Figure 7a): identifying which player the system referred to (Mext = 5.94 vs. Mbase = 4.69; W = 3.0, p = .011, r = .62), which moment was shown (Mext = 6.25 vs. Mbase = 4.69; W = 4.0, p = .003, r = .73), and what alternatives were considered (Mext = 4.75 vs. Mbase = 3.62; W = 5.5, p = .024, r = .56)."
[^c2]: lee-2026-player
[^c3]: lee-2026-player — "The binding constraint was correction cost, not externalization quality, and this cost varied by ambiguity type."
[^c4]: lee-2026-player — "externalization supported higher inspectability and more repair language than the voice-only baseline, yet repair occurred in only 38% of misaligned trials, with the gap varying by ambiguity type in ways that indicate correction cost, not transparency quality, as the binding constraint."
[^c5]: lee-2026-player — "Because the baseline was voice-only, we cannot separate visual richness from interpretation externalization."
