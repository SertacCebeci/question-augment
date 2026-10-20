---
description: "Appending a scene's OCR-read text to a question raised F1 on signboard VQA, and the share of gold answer tokens the OCR recovers bounds what a span-selecting answerer can return."
aliases: ["OCR token match ratio", "OCR-context augmentation", "OCR suffix", "answer-token OCR coverage"]
sources: ["arxiv-2512-22218"]
---
# OCR answer-token coverage

When the answer to a question is printed in the image, a scene-text recogniser can read that text and the text can be given to the answering model as part of the question's context. In the signboard VQA paper, models that receive the OCR text "as part of the question input" outperform those that do not, on both F1 and exact match.[^o1] For PreSTU the F1 went "increasing from 24.05% (without OCR) to 50.37% (with OCR)".[^o2]

The mechanism the authors propose is that many answers are spans already present in the OCR output, so the task becomes "recognizing and selecting the correct span from OCR outputs".[^o3] The paper makes this measurable as a coverage variable: for each test question it takes the fraction of gold answer tokens that the OCR engine (SwinTextSpotter) actually returned, and groups questions into bins from under 25% to 100%.[^o4] Across models, F1 "generally improves as the proportion of answer tokens" found in the OCR output increases, and when coverage is under 25% "model performance is significantly lower".[^o5]

So the concept is a property of the pair (image, OCR output, gold answer), not of the question alone. Low coverage caps what a model that selects spans from the OCR text can get right; high coverage is necessary for the gain but does not secure it. The paper does not state the cap as a formula. It reports the shape of the curve, and the cap reading is mine.

## Limits

- Coverage is computed from the gold answer, so it is available after the fact. An asker or answerer does not know the bin of a question before answering, and the paper does not offer a predictor of coverage from the question or image. The variable diagnoses failure; it does not forecast it.
- Full coverage is not sufficiency. "Even when 100% of the answer tokens are found in the OCR text" the scores stayed low: "the F1 and EM scores remain below 0.6 and 0.2 respectively".[^o6] The paper says "OCR text alone is not a guarantee" of correct answers.[^o7]
- The curve is not monotone. F1 "peaks at the 75–100% range" for two models and then "slightly declines at 100%, possibly due to overfitting to OCR signals", a reading the authors offer without testing it.[^o8] Exact match zig-zags across the middle bins, and the authors say partial overlap "may even mislead the model".[^o9]
- The architectures do not share one reliance pattern. One model "predominantly exploits textual signals from OCR", while another loses little when OCR is removed: "excluding OCR features results in only a slight decrease in performance".[^o10] The coverage effect is reported for all four, but the size of the OCR dependence is not a single number.
- The headline "improvement of nearly 209%" is a ratio: 50.37 / 24.05 is about 2.09, so the relative gain is about 109%.[^o11] I read the figure as a 2.09-fold ratio, not as a 209% gain. The paper's own numbers are the safer quote.
- One dataset, one language, one OCR engine. The paper does not vary the OCR system, so the coverage-to-F1 curve is specific to SwinTextSpotter's recall on Vietnamese signboards.
- The multi-agent GPT-4 result (75.98% accuracy by majority vote) is outside this note. Table 3 compares different backbones, so its gain over single models is not separated from the choice of model here (my inference).

## Related

- [[perception-context-tradeoff]] — OCR is a compression of an image into text; that note measures the detail lost when a visual source is reduced to text, which is the cost this coverage variable tracks.
- [[text-modality-dominance]] — models lean on text when it is present; the OCR gain is consistent with that reliance, though this paper does not measure reliance directly.

[^o1]: arxiv-2512-22218 — "text as part of the question input significantly outperform those that do not"
[^o2]: arxiv-2512-22218 — "increasing from 24.05% (without OCR) to 50.37% (with OCR)"
[^o3]: arxiv-2512-22218 — "recognizing and selecting the correct span from OCR outputs"
[^o4]: arxiv-2512-22218 — "fraction of answer tokens successfully retrieved by SwinTextSpotter"
[^o5]: arxiv-2512-22218 — "When OCR text contains less than 25% of the answer tokens"
[^o6]: arxiv-2512-22218 — "the F1 and EM scores remain below 0.6 and 0.2 respectively"
[^o7]: arxiv-2512-22218 — "OCR text alone is not a guarantee"
[^o8]: arxiv-2512-22218 — "then slightly declines at 100%, possibly due to overfitting to OCR signals"
[^o9]: arxiv-2512-22218 — "insufficient for exact generation, and may even mislead the model"
[^o10]: arxiv-2512-22218 — "excluding OCR features results in only a slight decrease in performance"
[^o11]: arxiv-2512-22218 — "improvement of nearly 209%"
