---
description: "Frontier VLMs asked to diagnose a medical image that was never attached fabricate rather than abstain; whether and which diagnosis is fabricated tracks patient demographic, not evidence."
aliases: ["demographic mirage", "demographic-conditioned confabulation"]
sources: ["vohra-2026"]
---
# Demographic-conditioned mirage

> A vision-language model asked to describe an image that is not there should
> abstain — or ask for the image. Instead it names a disease, and which
> disease depends on who the patient is said to be.

## Definition / Mechanism

Prior work names the base phenomenon: a VLM queried about an image it was
never given produces a visual description and diagnosis instead of
abstaining, the *mirage effect* (Asadi et al. 2026, cited in
Vohra (2026)). Vohra tests whether the fabricated content is
structured, querying Claude Opus 4.7, GPT-5.4 and Gemini 3.1 Pro with only a
demographic descriptor and no image, over a 2×2×3 factorial (age, sex, race)
across chest X-ray, brain MRI and dermatology, with diagnoses read from an
enforced JSON schema rather than judged from prose.[^c1]

Demographic descriptor changes both **whether** a diagnosis is fabricated
and **which** one: per-cell Jensen-Shannon divergence against a
demographic-free baseline reaches 0.834 on Claude (dermatology, 65-year-old
white man: 94% "Melanoma"), GPT-5.4 fabricates on all 36 tested demographic
cells, and a chi-square test of refusal versus fabrication against the
demographic label rejects independence on six of nine (model, domain) pairs
after Bonferroni correction — refusal itself, not only the content once a
diagnosis is produced, is a function of the demographic descriptor.[^c2]

A paraphrase-noise control bounds the effect against wording noise alone:
the demographic signal exceeds surface-phrasing variation by a factor of
roughly 3 to 14 across the three models tested.[^c3]

## Why it matters

This is a measured failure of the decision the answerer must make before
committing to any output: whether the evidence in hand supports an answer
at all. Here the evidence is absent by construction (no image), yet the
model's decision to answer or abstain — and the content of the answer it
gives — tracks a variable (patient demographic) that has no evidentiary
bearing on the missing image. [[abstention]] treats the answer/abstain
choice as a selection function $g$ over a named cost or risk; this result
shows $g$ itself can be a function of a protected attribute rather than of
the actual uncertainty, which the abstention framework's marginal
coverage/risk accounting does not surface on its own.

## Limits

- Three frontier models, one snapshot in time; the paper makes no claim
  about other model versions or providers.
- The neutral baseline is itself not fabrication-free for GPT-5.4, so the
  demographic-vs-baseline divergences are reported as a lower bound on the
  true demographic effect.[^c4]
- The race label "brown" is noted as a heterogeneous, colloquial descriptor
  whose referent varies across pretraining corpora, so effects keyed to it
  are not attributable to a stable racial category.[^c5]
- The paper does not separate pretraining bias from a calibrated clinical
  prevalence prior as the source of the shift; it reports the shift is
  present, not which mechanism produces it.[^c6]

## Related

[[abstention]] · [[clarification-request]] · [[hedged-mirage]] · [[semantic-entropy]]

[^c1]: vohra-2026 — "Claude Opus 4.7, GPT-5.4, and Gemini 3.1 Pro are each queried with only a demographic descriptor"
[^c2]: vohra-2026 — "adding “I am a 65-year-old white man.” yields 94% Melanoma (bootstrapped JSD 0.834, 95% CI [0.741, 0.929])."
[^c3]: vohra-2026 — "demographic-to-paraphrase ratios are 10.5×, 13.9×, and 3.0× (Figure 2). The demographic signal exceeds surface-phrasing variation"
[^c4]: vohra-2026 — "GPT-5.4 D0 fabricates at 11% (xray) and 19% (derm), so demographicvs-D0 JSDs are a lower bound."
[^c5]: vohra-2026 — "The race label “brown” has a heterogeneous referent across pretraining corpora; GPT-5.4’s 25% Neurocysticercosis on mri_32rm cues a"
[^c6]: vohra-2026 — "Pretraining bias and a calibrated prevalence prior are observationally equivalent sources of the second (melanoma incidence really is higher in older non-Hispanic"
