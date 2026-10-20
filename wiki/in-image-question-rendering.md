---
description: "Putting a question's text inside its image, not beside it, lowered open-source multimodal models' accuracy on identical items; OCR ability explains only part of the drop."
aliases: ["composite question image", "text-in-image question", "image-embedded question", "integrated visual-textual question"]
sources: ["arxiv-2512-14620"]
---
# In-image question rendering

A visual question usually reaches a model as two inputs: a picture and a block of text. In-image rendering composes both into one picture, so the question text is drawn in the same frame as the figure. JMMMU-Pro does this to the 1,320 items of JMMMU: the question text and image are composed "into a single image", with the content "identical to those in the original JMMMU".[^r1] The same design had already been used for English in MMMU-Pro, where "both the question text and the question image are embedded within a single image".[^r2]

The motivation is about the input people actually send. "users commonly provide LMMs with screenshots that include both Japanese text and images".[^r3] A model that is tested only on text and picture as separate channels is never asked to read the text out of the picture and then reason with it.

## What it does to measured accuracy

Holding the question content fixed and changing only the presentation, most open-source models score lower: "Most open-source LMMs exhibit a significant performance drop compared to JMMMU."[^r4] The reported ceiling is "open-source LMMs exhibit a decrease ranging up to 23%."[^r5] Closed models do not show the same pattern: "while closed-source LMMs maintain strong performance".[^r6]

## What the drop is attributed to

The authors' first hypothesis was a reading failure: "the primary cause of performance degradation on JMMMU-Pro is the inability of current LMMs to perform Japanese Optical Character Recognition (OCR)."[^r7] The data support part of it. "The correlation coefficient between OCR accuracy and JMMMU-Pro accuracy is 0.593."[^r8] The paper then limits the reading: "high OCR ability does not necessarily translate directly into high JMMMU-Pro accuracy."[^r9] Its conclusion is that "JMMMU-Pro demands not only strong OCR capabilities, but also the ability to interpret and reason over language and vision in an integrated manner through visual perception."[^r10]

So, as measured, the composite item requires at least two steps that the separated item does not: extracting the glyphs, and reasoning over the extracted content together with the figure. A model can fail either step. My inference, not measured here: a benchmark with separated channels can be passed by a model that never reads the text in the picture, so its score says little about the joint step.

## Limits

- One language (Japanese), one benchmark, one set of models. The paper does not say why closed models were unaffected; the open-versus-closed split is also a capability split.
- The comparison is between the original JMMMU images and the regenerated composite images. The composite images were made by an image generator, so rendering artefacts are confounded with presentation. No run separated the two.
- The OCR correlation is across models, not within one. A correlation of 0.593 leaves most of the variance unexplained, and the paper itself says OCR is not sufficient.
- The paper's numbers do not fully agree at one point: the text gives 45.83 for the best open model, Qwen3-VL-8B, while the table extraction shows 47.27 for that model in the JMMMU-Pro column. I did not resolve this.
- Qwen2.5-VL-7B is an exception to the drop, which the paper notes and does not explain.
- Some question content cannot be rendered reliably (long text, small text, chemical formulas, musical notation); see [[generator-rendered-question-items]].

## Related

- [[text-modality-dominance]] — text cues outweigh vision in omni-modal models; in-image rendering moves the question text into the visual channel, so the reliance question changes shape
- [[presentation-modality-shapes-question-intention]] — another sense of presentation medium; there the medium changed why learners asked, here it changes whether the item is answered
- [[divergence-rewarded-probe-generation]] — image generators also struggle to render text and diagrams, which bounds what composite items can contain
- [[generator-rendered-question-items]] — how the composite items were produced and checked

[^r1]: arxiv-2512-14620 — "composing the question image and question text into a single image"
[^r2]: arxiv-2512-14620 — "both the question text and the question image are embedded within a single image"
[^r3]: arxiv-2512-14620 — "users commonly provide LMMs with screenshots that include both Japanese text and images"
[^r4]: arxiv-2512-14620 — "Most open-source LMMs exhibit a significant performance drop compared to JMMMU."
[^r5]: arxiv-2512-14620 — "open-source LMMs exhibit a decrease ranging up to 23%"
[^r6]: arxiv-2512-14620 — "while closed-source LMMs maintain strong performance"
[^r7]: arxiv-2512-14620 — "the primary cause of performance degradation on JMMMU-Pro is the inability of current LMMs to perform Japanese Optical Character Recognition (OCR)"
[^r8]: arxiv-2512-14620 — "The correlation coefficient between OCR accuracy and JMMMU-Pro accuracy is 0.593."
[^r9]: arxiv-2512-14620 — "high OCR ability does not necessarily translate directly into high JMMMU-Pro accuracy"
[^r10]: arxiv-2512-14620 — "JMMMU-Pro demands not only strong OCR capabilities, but also the ability to interpret and reason over language and vision in an integrated manner through visual perception"
