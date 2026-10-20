---
description: "Putting the retrieved evidence in the target language hurts VLMs far more than putting the instructions there, so non-English evidence is integrated worse than non-English prompts are followed."
aliases: ["cross-lingual evidence integration", "context-language penalty", "non-English retrieved context degradation", "oracle-context language gap"]
sources: ["arxiv-2512-05959"]
---
# Evidence-language integration gap

A multilingual answerer can be handed two things in a language other than the question's: the instructions it is told to follow, and the evidence it is asked to reason from. They are not the same burden. The M4-RAG paper separates them in cross-lingual visual question answering: the whole instruction template was translated into each target language, and the oracle context was translated separately. Both were produced with Gemini-2.5-Flash and "all translations were subsequently reviewed and validated by annotators."[^c1]

Against the English baseline, the two conditions come apart. Switching the prompt to a target language "consistently degrades performance across all resource levels", mildly for high-resource languages (mostly within -1% to -2%) and more for low-resource ones.[^c2] Switching the evidence costs much more: "performance deteriorates dramatically, with drops as large as -32.4% for Qwen2.5-VL" 32B on CVQA.[^c3] The paper's summary of the contrast is that "The multilingual gap is far more pronounced even when the oracle context is provided in the target language rather than English."[^c4]

The authors draw the distinction directly. Models "can tolerate non-English instructions to some extent, but fail much more severely when the retrieved evidence itself is in a non-English language", and so "cross-lingual evidence integration is a deeper bottleneck than instruction following."[^c5] The result runs against a plausible expectation, which the paper names: "Contrary to the intuition that culturally aligned context should help, performance deteriorates dramatically."[^c6]

## What it says about answering

The measure is that an answerer can follow a question in one language and still fail to use an evidence passage in another, even when the passage is correct and about the same culture. Whatever the model does with the evidence, the language of the evidence is part of the cost, not only the language of the question. For someone building a multilingual retrieval pipeline, translating the retrieved text into the query language is then not a free step: my inference, not tested here, is that it can cost more accuracy than the translation of the instructions.

Training on more multilingual data does not remove it. Pangea, which the authors describe as trained on multilingual and multicultural Wikipedia data, is "still among the most severely affected", and the paper concludes that "exposure to multilingual training data does not straightforwardly confer robustness to non-English retrieved context at inference time."[^c7]

The gap is also uneven across families and sizes. The Qwen family "exhibits a sharper collapse in low-resource settings compared to Gemma", which the authors read as showing that "model scale alone does not resolve this bias."[^c8]

This note is the generator-side complement to [[structural-priors-in-language-preference]], which explains a language preference by what the retriever surfaces. Here the evidence is held fixed in content and only its language changes, so retrieval exposure cannot be the whole story.

## Limits

- The oracle context on CVQA is a caption generated "conditioned on the image, question, and human-annotated ground-truth answer".[^c9] So the English reference already contains the answer, and the translated version is an answer-bearing text, which is not a typical retrieved passage.
- Translation is a confound the paper does not separate from the language effect. Machine translation with annotator review measures the translated text's quality together with the model's use of it; [[translation-confounded-language-gap]] treats this confound in general (my inference that it applies here).
- Answer language is confounded with scoring. The authors observe that "smaller models show a lesser performance drop overall because they tend to code-switch to English even when prompted in a target language, whereas larger models attempt to respond fully in the target language and fail more dramatically as a result."[^c10] Part of a drop may be the answer's language, not the integration of evidence.
- The measure is macro-averaged accuracy over multiple-choice answers, so this is not a claim about free-form generation.
- The mechanism is not isolated. The paper does not say whether the failure is in reading the non-English evidence, in linking it to the image, or in matching it to the answer options.

## Related

- [[structural-priors-in-language-preference]] — retriever-side language preference; this note is the generator-side residue with the evidence's content fixed
- [[translation-confounded-language-gap]] — translation as a measurement artefact in cross-language gaps, which bears on the translated oracle here
- [[retention-correction-asymmetry]] — the same retrieval evidence can preserve or fix an answer, and its integration is where the scale effect appears
- [[respondent-language-conditioning]] — the prompt language matters in a different direction there, for simulated respondents

[^c1]: arxiv-2512-05959 — "all translations were subsequently reviewed and validated by annotators"
[^c2]: arxiv-2512-05959 — "consistently degrades performance across all resource levels"
[^c3]: arxiv-2512-05959 — "performance deteriorates dramatically, with drops as large as -32.4% for Qwen2.5-VL"
[^c4]: arxiv-2512-05959 — "The multilingual gap is far more pronounced even when the oracle context is provided in the target language rather than English."
[^c5]: arxiv-2512-05959 — "fail much more severely when the retrieved evidence itself is in a non-English language"
[^c6]: arxiv-2512-05959 — "Contrary to the intuition that culturally aligned context should help, performance deteriorates dramatically"
[^c7]: arxiv-2512-05959 — "exposure to multilingual training data does not straightforwardly confer robustness to non-English retrieved context at inference time"
[^c8]: arxiv-2512-05959 — "The Qwen family exhibits a sharper collapse in low-resource settings compared to Gemma, showing that model scale alone does not resolve this bias"
[^c9]: arxiv-2512-05959 — "conditioned on the image, question, and human-annotated ground-truth answer"
[^c10]: arxiv-2512-05959 — "smaller models show a lesser performance drop overall because they tend to code-switch to English even when prompted in a target language"
