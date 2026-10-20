---
description: "A vision-language model can hedge in its prose while its structured output field still commits to a diagnosis, a dissociation invisible to a prose-only audit."
aliases: ["hedged mirage regime", "dual-channel commitment dissociation"]
sources: ["vohra-2026"]
---
# Hedged mirage

> Reading only what the answerer says about its own uncertainty
> undercounts how much it actually committed to.

## Definition / Mechanism

Vohra (2026) cross-classifies each fabricated VLM diagnosis
on two independent axes read from a dual-channel pipeline: whether the
free-text reasoning acknowledges the image is missing, and whether the
structured diagnosis field is populated — a classification not visible to
prose-only extraction. On Claude Opus 4.7's highest-divergence cell
(dermatology, 65-year-old white man), 62 of 94 fabrications are **hedged**:
the reasoning states the image is absent — sometimes with an explicit
qualifier such as "pending dermoscopy" — while the structured field still
names a disease. On GPT-5.4's highest cell (chest X-ray, 32-year-old Black
man) all 77 fabrications are **classic**: no hedging, the field is populated
outright. A structured `image_present` field is not an independent check
either: across 11,700 calls, no record has `image_present=false` alongside
a populated diagnosis.[^c1]

The measurement consequence is stated directly: an audit that reads only
the natural-language response would log 66% of Claude's fabricating
records on that cell as refusals, while a pipeline that reads the
structured diagnosis field receives a demographically structured diagnosis
from those same records.[^c2]

## Why it matters

The answerer's commitment is not one scalar; it can diverge by output
channel, and the channel a downstream pipeline reads determines whether
the failure is visible at all. [[abstention]]'s selection function $g$
assumes one committed output per instance; here $g$ effectively disagrees
with itself depending on which field of the same response is read. A
[[clarification-request]] made only in prose, with no corresponding hold
on the answer that gets consumed downstream, does not function as a
clarification request from the consuming pipeline's point of view — it
is dead language sitting next to a live answer.

## Limits

- Measured in one paper, on the top-fabrication cells of two of three
  tested models; Gemini's fabrication rate is near zero on most cells, so
  its hedged-versus-classic split is not reported at comparable volume.
- The paper does not test whether hedged text causes downstream
  channel-only audits to miss the fabrication, or only correlates with it
  in this dataset; the 66% figure describes this one cell, not a general
  rate.
- Enforcement is provider-native (OpenAI strict JSON schema, Anthropic
  forced tool call, Gemini JSON MIME), so the dissociation may be
  provider-specific plumbing rather than a shared property of the models'
  reasoning.[^c3]

## Related

[[demographic-conditioned-mirage]] · [[abstention]] · [[clarification-request]] · [[semantic-entropy]]

[^c1]: vohra-2026 — "acknowledges the missing image, and whether the structured diagnosis field is populated. This classification is not visible to proseonly extraction. On Claude’s derm_65wm, 62 of 94 fabrications are"
[^c2]: vohra-2026 — "with no such hedging. An audit that reads only the natural-language"
[^c3]: vohra-2026 — "Enforcement is provider-native (OpenAI strict JSON schema, Anthropic"
