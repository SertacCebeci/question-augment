---
description: "A caption stands in for its image only as far as a text-only reader can still answer from it; for MLLMs the drop is roughly 9 to 32 percent, and image-QA rankings miss it."
aliases: ["QA-on-caption gap", "caption utility gap", "image-to-caption utility loss", "caption as surrogate"]
sources: ["arxiv-2511-21025"]
---
# Caption-utility gap

A caption replaces an image for whatever comes after it, so its adequacy can be measured by what a reader can still do with it, not by how well it reads. CaptionQA sets this up as one question: can a caption "replace the image for downstream reasoning"?[^c1] A captioning model writes a caption; a text-only LLM then answers a multiple-choice question from that caption alone, "without access to the original image".[^c2] The same questions answered from the image give the reference. The difference between the two accuracies is the gap.

The image side is close to saturated. The paper reports that GPT-5 "reaches close to 98% accuracy on QA-on-image".[^c3] With its own captions the same model loses about nine points. Across strong proprietary models the gap is "consistently around 9.2-16.4%";[^c4] for open-source models it is "substantially larger, ranging from" about 11% to 32.4%.[^c5] The loss is therefore not a fixed cost of captioning: it is the share of the image's answerable content that the caption fails to carry into text.

## What image-QA rankings miss

The gap is not a monotone function of image-QA ability. The paper's example: Claude Sonnet 4.5 and LLaVA-OneVision-7B are close on image questions, "but their caption-based scores differ by 17.2%".[^c6] The authors draw the consequence that "standard QA-on-image benchmarks like MMBench or MME would consider these models" close.[^c7] Two models with the same image-answering score can carry very different amounts of usable information in their captions. That is the concept's main use: a description is evaluated by a second, text-only reader, and the image benchmark does not measure this.

The gap also depends on the domain. E-commerce, where product attributes are written on the page, has the smallest gaps, since its information "is relatively easy to preserve in text".[^c8] "Embodied AI exhibits the largest gaps".[^c9]

## Two kinds of loss

The paper separates the shortfall by a length test. Where a caption has the information but leaves it unstated, the loss is a verbalization bottleneck: "information is present but under-described".[^c10] Document structure and e-commerce text gain "+41-56%" when the caption moves from Short to Simple.[^c11] Where the caption lacks the detail, the loss is an information bottleneck: for Embodied AI, the gains are smaller, because "required details (activity and task context) are still" missing from longer captions.[^c12] The two loss types call for different fixes, and the length test is what tells them apart.

Longer captions do not close the gap by themselves. "Additional verbosity does not translate to improved utility".[^c13] Moving from Short to Simple "captures 99% of the benefit from going all the way to Long".[^c14] Complex prompts can make things worse: "More complex prompts can backfire."[^c15] The paper reads the Taxonomy-Hinted failure as "from content grounding to format imitation",[^c16] the model filling a template instead of describing the picture.

## The scoring rule

A caption-QA score that rewards only correct answers would reward a caption for guessing. CaptionQA adds an option: "we append an additional option" "Cannot answer from the caption" to every non-yes/no question.[^c17] A correct selection scores 1, an incorrect one 0, and the cannot-answer option scores "1/nchoices + 0.05" (the chance rate for the semantic options, plus a small margin).[^c18] The design, in the paper's words, "favors precision over hallucinated detail": "less, but avoids misleading content, is preferable to one that" confidently misleads.[^c19] So the gap is partly a measure of how often a caption says nothing about an answer, which the rule does not punish as a wrong answer. See [[abstention]] for the reject option in general.

The questions themselves are the reference set. Each one is screened by a text-only filter, which the same paper uses as a construction step, described in [[text-answerability]]. Questions that a text-only model answers above the threshold are dropped.[^c20] The items that survive are described by the authors as ensuring "that all retained questions are visually answerable".[^c21]

## Limits

- The gap is measured on questions that the benchmark's taxonomy generated and that passed visual screening. A caption's loss on information nobody asked about is not measured. "Utility" here is answerability of these questions, not usefulness for any task.
- One text-only reader is used. The paper chooses "Qwen2.5 72B as the QA model"[^c22] among four candidates, for speed and run-to-run stability as well as accuracy. The gap includes the reader's own reading errors, and a different reader could move the numbers. The text read does not test that.
- The two accuracies come from different input channels, and the paper does not separate caption loss from reader loss in each item. The reference is the image-QA score, which is also an accuracy, so a model that answers image questions less reliably has a smaller gap by construction. The paper's point that the gap "is not simply a reflection of baseline multimodal ability" rests on a few example pairs (my reading; the text gives no regression).
- The "1/nchoices + 0.05" credit is the authors' choice. No sensitivity analysis for it appears in the parts read, so how much the reject credit moves the ranking is not established.
- The domain differences rest on four domains with images curated by the authors, and the Embodied AI frames come from existing datasets selected by hand. The gap per domain is a measurement of this benchmark, not of the domain.

## Related

- [[text-answerability]] — the item-side probe: a text-only model answers the question without the picture; the same filter is applied at construction here
- [[abstention]] — the cannot-answer option as a scored third output; here it is credited above chance
- [[cross-modal-aggregation-gap]] — the caption channel next to a figure: combining the two does not beat either alone, a different test of the same channel
- [[text-modality-dominance]] — reliance on text over another modality, measured by corruption; this gap runs the other way, text standing in for the image

[^c1]: arxiv-2511-21025 — "they can replace the image for downstream reasoning"
[^c2]: arxiv-2511-21025 — "without access to the original image"
[^c3]: arxiv-2511-21025 — "reaches close to 98% accuracy on QA-on-image"
[^c4]: arxiv-2511-21025 — "consistently around 9.2-16.4%"
[^c5]: arxiv-2511-21025 — "substantially larger, ranging from"
[^c6]: arxiv-2511-21025 — "but their caption-based scores differ by 17.2%"
[^c7]: arxiv-2511-21025 — "standard QA-on-image benchmarks like MMBench or MME would consider these models"
[^c8]: arxiv-2511-21025 — "is relatively easy to preserve in text"
[^c9]: arxiv-2511-21025 — "Embodied AI exhibits the largest gaps"
[^c10]: arxiv-2511-21025 — "information is present but under-described"
[^c11]: arxiv-2511-21025 — "Document structural elements and E-commerce textual content gain +41-56%"
[^c12]: arxiv-2511-21025 — "required details (activity and task context) are still"
[^c13]: arxiv-2511-21025 — "Additional verbosity does not translate to improved utility."
[^c14]: arxiv-2511-21025 — "captures 99% of the benefit from going all the way to Long"
[^c15]: arxiv-2511-21025 — "More complex prompts can backfire."
[^c16]: arxiv-2511-21025 — "from content grounding to format imitation"
[^c17]: arxiv-2511-21025 — "we append an additional option"
[^c18]: arxiv-2511-21025 — "1/nchoices + 0.05"
[^c19]: arxiv-2511-21025 — "less, but avoids misleading content, is preferable to one that"
[^c20]: arxiv-2511-21025 — "we treat the question as text-answerable and discard it"
[^c21]: arxiv-2511-21025 — "ensuring that all retained questions are visually answerable"
[^c22]: arxiv-2511-21025 — "we adopt Qwen2.5 72B as the QA model"
