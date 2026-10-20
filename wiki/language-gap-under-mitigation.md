---
description: "The English–Urdu gap in a composite bias-and-utility score fell from 0.166 at baseline to 0.017 under best-of-N selection and reopened to 0.060 under sequential refinement."
aliases: ["English–Urdu disparity", "cross-lingual fairness gap", "language gap under debiasing"]
sources: ["arxiv-2512-09854"]
---
# Language gap under mitigation

A stereotype score measured in two languages gives a gap between them. That gap is not a fixed property of the languages. It depends on the mitigation applied, and a method can close it on one axis while it reopens on another. The work measures this on 200 English prompts and their 200 Urdu translations, completed as single words by GPT-3.5 and scored by GPT-4o-mini "in zero-shot mode, allowing cross-lingual evaluation without supervised training."[^g1]

The headline gap is in the composite score, not in bias alone. At baseline, "Composite scores follow the same pattern: English = 0.96875 vs. Urdu = 0.8025."[^g2] The difference is 0.16625, which the paper reports as the baseline gap. The composite is the only quantity whose numbers match this figure, so the gap is a composite gap.

Best-of-N selection nearly closed it: "PRM-Select gap: 0.017 (almost eliminated)."[^g3] The authors summarise: "PRM-Select nearly eliminates the cross-lingual gap, reflected in Table 2."[^g4] The closing came mostly from the lower language. English bias moved little, from 0.9525 to 0.9765, while "Urdu bias rises dramatically: 0.755 → 0.96."[^g5] Utility converged the same way, with Urdu rising to 0.9825 against English's 1.0.

Sequential refinement gave the smallest bias gap but a larger composite gap. Its bias scores were "English bias = 0.99 Urdu bias = 0.975,"[^g6] a difference of 0.015. The composite gap nonetheless came back to "PRM-Sequential: 0.060 (gap reappears due to Urdu utility drop)."[^g7] So the residual gap under refinement is a utility gap, not a bias gap. The method that is fairest in the bias score leaves the language gap open through the utility score. The utility loss itself is treated in [[debiasing-utility-overcorrection]].

What transfers is a measurement rule. A cross-language comparison of a mitigated system has to be reported for each method and each axis. Reporting only the bias score under one method can show a closed gap that is open on the other axis. The paper gives a cause for the baseline gap that it does not test here: "English dominates global pretraining corpora."[^g8] The gap at baseline is consistent with that explanation, but the text read does not separate pretraining exposure from translation or from the judge.

## Limits

- The gap is defined through the composite with α fixed at 0.5. A different weight could change the size of the gap and its sign under refinement. The text reports no sweep.
- Each method appears once, with one set of numbers per language. The text read gives no interval or test for the 0.060 and 0.017 gaps, so a difference of a few hundredths is not shown to exceed run-to-run variation.
- The Urdu prompts are translations written by the authors, and "Urdu translations cannot fully capture culturally nuanced stereotypes."[^g9] Part of the baseline gap may be an artefact of translation. The same risk is treated for language gaps in [[translation-confounded-language-gap]].
- Two languages, one generator, one judge. The gap is not shown for other low-resource languages, and the judge's own behaviour in Urdu is not separately checked. The paper notes that "No human annotator study was conducted."[^g10]
- The sequential gap is read from the authors' statement that it "reappears due to Urdu utility drop." I checked the bias numbers against the composite numbers and they agree with the baseline gap, but the English sequential utility is not in the text, so the decomposition of the 0.060 is not shown.

## Related

- [[multilingual-safety-divide]] — the same point that language is a variable an evaluation must hold fixed, here applied to a stereotype score rather than to refusals
- [[translation-confounded-language-gap]] — a gap that can come from the translation step, which this paper's Urdu prompts do not rule out
- [[debiasing-utility-overcorrection]] — the utility cost under refinement that re-opens the composite gap

[^g1]: arxiv-2512-09854 — "in zero-shot mode, allowing cross-lingual evaluation without supervised training"
[^g2]: arxiv-2512-09854 — "Composite scores follow the same pattern: English = 0.96875 vs. Urdu = 0.8025."
[^g3]: arxiv-2512-09854 — "PRM-Select gap: 0.017 (almost eliminated)"
[^g4]: arxiv-2512-09854 — "PRM-Select nearly eliminates the cross-lingual gap, reflected in Table 2."
[^g5]: arxiv-2512-09854 — "Urdu bias rises dramatically: 0.755 → 0.96."
[^g6]: arxiv-2512-09854 — "English bias = 0.99 Urdu bias = 0.975"
[^g7]: arxiv-2512-09854 — "PRM-Sequential: 0.060 (gap reappears due to Urdu utility drop)"
[^g8]: arxiv-2512-09854 — "English dominates global pretraining corpora."
[^g9]: arxiv-2512-09854 — "Urdu translations cannot fully capture culturally nuanced stereotypes."
[^g10]: arxiv-2512-09854 — "No human annotator study was conducted."
