---
description: "Forcing an LLM to reason in English rather than a low-resource question's own language closes most of the uncertainty-estimation quality gap, isolating a generation-not-comprehension bottleneck."
aliases: ["generation-language bottleneck", "English-reasoning transfer"]
sources: ["alfarano-2026"]
---
# Reasoning-language bottleneck in uncertainty estimation

> A model's uncertainty signal degrades in low-resource languages not
> because it fails to understand the question, but because it struggles to
> *generate* reasoning in that language — switching only the reasoning
> language to English recovers most of the loss.

## Definition / Mechanism

Alfarano, Bacciu & Mansour (2026) evaluate nine
uncertainty-estimation (UE) methods on two human-curated MCQA datasets
across 22 languages, comparing two prompting conditions that hold the
question fixed and vary only where the model reasons: reasoning in the
target language, versus reasoning forced into English.[^c1]

"On average, English reasoning improves UE quality (0.72 vs. 0.68 AUROC).
Crucially, this improvement is driven by low-resource languages: English
reasoning effectively brings their UE performance to the level of
high-resource languages." For Yoruba AUROC rises from 0.58 to 0.68, for
Swahili from 0.58 to 0.64, for Nepali from 0.66 to 0.71 — non-overlapping
confidence intervals — closing the gap to Germanic and Romance languages
(0.71–0.73), which show no significant change between conditions.[^c2]

Two controls rule out confounds: restricted to the Self-Verbalized method
alone, which "relies directly on the model's reported confidence and
involves no similarity scoring", "the improvement under English reasoning
remains significant (AUROC 0.665 → 0.679, paired bootstrap p < 0.001)"; and
on the 88.4% of questions answered identically under both conditions, where
accuracy is held constant by construction, "the effect persists... (AUROC
0.670 → 0.684, p < 0.001)".[^c3]

The paper's reading: because the question stays in the target language in
both conditions, "if comprehension were the bottleneck, changing the
reasoning language would not help... The fact that English reasoning closes
the gap suggests that models comprehend low-resource questions adequately
but struggle to generate coherent reasoning in those languages."[^c4]

## Why it matters

On stall 2, a confidence or axis-selection signal read off a model's stated
uncertainty is only as good as the language it reasons in: a low-resource
deployment produces a systematically weaker signal for reasons unrelated to
what the model actually knows, and the fix tested here does not touch the
question language at all — only where the model is told to reason. See also
[[ue-method-scale-dependence]] for a second condition — model size — under
which the same UE methods' [[calibration|reliability]] shifts.

## Limits

- Measured on MCQA with three large models (Qwen3-235B, Gemma3-27B, Claude
  Sonnet 4.5); whether the effect holds for open-ended free-text answers or
  smaller models is not tested here.[^c5]
- The claim is about AUROC for error detection specifically, not about
  calibration or any other UE metric.
- 22 languages sampled across resource levels and language families, not
  exhaustive of low-resource settings; effect sizes vary by WALS language
  genus and are largest for South Asian and African languages.

## Related

[[ue-method-scale-dependence]] · [[abstention]] · [[semantic-entropy]]

[^c1]: alfarano-2026 — "we compare two configurations: Multilingual, where the model reasons in the target language (i.e., language of the question and answers), and English Reasoning, where reasoning is conducted in English regardless of the target language."
[^c2]: alfarano-2026 — "On average, English reasoning improves UE quality (0.72 vs. 0.68 AUROC). Crucially, this improvement is driven by low-resource languages: English reasoning effectively brings their UE performance to the level of high-resource languages."
[^c3]: alfarano-2026 — "the improvement under English reasoning remains significant (AUROC 0.665 → 0.679, paired bootstrap p < 0.001)."
[^c4]: alfarano-2026
[^c5]: alfarano-2026
