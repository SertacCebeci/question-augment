---
description: "A machine-translated benchmark's language gap mixes model weakness with translation error; paired expert-reviewed items measure the translation share."
aliases: ["translation-induced benchmark gap", "machine-translation measurement bias", "translation artefact in multilingual benchmarks"]
sources: ["doi-10-48550-arxiv-2608-19981"]
---
# Translation-confounded language gap

A multilingual benchmark built by translating an English test set reports a lower score in the target language. That score can come from two sources: the model is weaker in that language, or the translated item tests the content less faithfully than the English original. A score on the translated version alone cannot say which. The authors put it directly: "lower score in a target language may therefore reflect weaker model capability, translation error or both."[^c1] "Without expert review, these sources of error cannot be separated."[^c2]

The separation the work proposes keeps two versions of every item: the machine translation (MT) and an expert-reviewed revision. The same models are then scored on both. Because the model is held fixed, a difference between the two scores is attributed to the text the model was given. In HealMed, the review was two-stage. "In the first stage, Reviewer 1 scored the original" machine translation and wrote a corrected version where needed. "Reviewer 2 independently scored the original translation using the same criteria" and then checked the first revision.[^c3]

The English control is what turns a raw difference into a translation-attributable one. English is the source language and has no translation step, so a shift measured on English reflects everything else that changed between the two versions. The authors subtract it: each language-by-dataset shift is adjusted "by the corresponding English shift".[^c4] On 14 models and six MCQA and NLI datasets, the adjusted shifts were largest in the lower-resource languages. "The mean absolute shifts were 4.9 percentage points in Thai," with Swahili and Zulu also above the higher-resource languages.[^c5] The authors' reading is that "benchmarks relying solely on machine translation may conflate model limitations with translation artefacts."[^c6]

The same paired design applied to open-ended QA, with an LLM judge on a five-point scale, gives much smaller shifts. "Mean absolute English-adjusted shifts ranged from 0.06 to 0.12 points" across the eight translated languages, and "Expert-reviewed scores were lower in" 18 of 24 language-by-dataset cells.[^c7] The sign and size of the effect therefore depend on the task format and the scorer, not only on the language.

What the design buys, in my reading, is that the translation term is measured rather than assumed. Without the second version, a benchmark author cannot tell a weak model from a bad translation; with it, a score change that survives the English adjustment is at least evidence that the translated text is doing work.

## Limits

- The expert review is not ground truth. Revisions toward local clinical usage are not necessarily corrections: revisions "should not automatically be interpreted as corrections of translation errors."[^c8] The reviewed version is one defensible target, not the target.
- Expert judgements were made by separate groups for each language. The authors say that "cross-language differences should be interpreted descriptively rather" than as calibrated rankings of translation quality.[^c9]
- The open-ended QA result may be an artefact of the scorer. The authors note "the possibility that the LLM evaluator was more" aligned with the literal phrasing of the machine translation, so the judge may favour the MT wording.[^c10]
- The design shows that the translated version changes scores. It does not show which translation errors cause the change; that attribution is the authors' interpretation, not something the paired comparison isolates.
- The paper does not test whether the expert-reviewed version matches scores on questions written natively in each language. The claim that MT "may not fully represent" naturally phrased questions is a hedged inference from the paired gap.
- One benchmark, nine languages, two reviewers per item. The generalisation to other translation pipelines, other language pairs, or other reviewer pools is not tested in the slices read.

## Related

- [[structural-priors-in-language-preference]] — the same reading error from the data side: a language gap read as a model's preference when the evidence sits in one language.
- [[multilingual-safety-divide]] — language is a variable an evaluation must hold fixed; here the paired design holds the content and the model fixed and lets only the translation vary.
- [[reference-answer-defect-audit]] — defects in a benchmark's items also move its scores; expert review of translated items is a language-specific version of that audit (my reading).

[^c1]: doi-10-48550-arxiv-2608-19981 — "lower score in a target language may therefore reflect weaker model capability, translation error or"
[^c2]: doi-10-48550-arxiv-2608-19981 — "Without expert review, these sources of error"
[^c3]: doi-10-48550-arxiv-2608-19981 — "Reviewer 2 independently scored the original translation using the same criteria"
[^c4]: doi-10-48550-arxiv-2608-19981 — "by the corresponding English shift"
[^c5]: doi-10-48550-arxiv-2608-19981 — "absolute shifts were 4.9 percentage points in Thai,"
[^c6]: doi-10-48550-arxiv-2608-19981 — "benchmarks relying solely on machine translation may conflate model limitations with translation artefacts"
[^c7]: doi-10-48550-arxiv-2608-19981 — "ranged from 0.06 to 0.12 points"
[^c8]: doi-10-48550-arxiv-2608-19981 — "should not automatically be interpreted as corrections of translation errors"
[^c9]: doi-10-48550-arxiv-2608-19981 — "cross-language differences should be interpreted descriptively rather"
[^c10]: doi-10-48550-arxiv-2608-19981 — "the possibility that the LLM evaluator was more"
