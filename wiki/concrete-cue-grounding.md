---
description: "A judgment is recognized reliably when visible objects carry it and splits by polarity when only colour and mood do; a forced binary over such an image yields contradictory answers."
aliases: ["concrete versus abstract recognition gradient", "visual grounding of affective judgments"]
sources: ["arxiv-2511-22929"]
---
# Concrete-cue grounding

A vision-language model answers a question about an image by reading cues the image shows. Where the answer rests on cues that can be named (a face, a posture, a skull, a storm), the answer tends to hold. Where it rests on diffuse qualities such as colour fields or mood, the answer is less stable. The case study of three VLMs on 38 artworks reports this as a continuum rather than a switch: "Properties of images that can characterized concretely at the visual level are captured more reliably by the VLMs than properties requiring more interpretation."[^c1]

The gradient shows inside a single image too. Facial expressions and postures are identified more precisely than abstract forms, and the abstract forms become more accurate "the more elements point in the same direction."[^c2] A mood carried by several concrete elements that agree is read correctly. A mood carried by colour and shape alone is not.

The sharpest case in the sample is the abstract group. The authors describe these paintings as ones that "primarily convey moods through colors and shapes", with few concrete objects.[^c3] The models do recognise the mood, but the authors say that "due to semantic underdetermination, they tend to detect both positive and" negative emotions for the same picture, "offering an inconsistent interpretation."[^c4] The answer splits by polarity because the image does not fix one. A question that asks for one polarity has no answer the picture settles.

The mechanism I draw from this is mine, not the paper's: a binary question over a stimulus with few anchoring cues asks for a verdict the stimulus does not contain, so each reading the model can construct gets surfaced. The paper observes the split; it does not test whether giving the model more concrete anchors, or asking for a graded answer, removes it.

## Limits

- The sample is 38 images, three models, one case study.[^c5] The authors' judgment is the evaluation: the outputs were checked "by hand to understand" how differentiated the models are, not scored against a labelled gold standard.[^c6] The continuum is therefore an ordering the authors read from their evaluation, not a measured accuracy curve, at least in the sections read.
- The abstract group is three images: "There are three highly abstract images in our sample".[^c7] The polarity split is shown on those, not across a population.
- Abstraction is confounded with other categories. The models also "struggle with three other categories of artworks: abstract images, allegories, and highly contextualized artworks".[^c8] The text does not separate which of these causes the failure.
- All models were used as published, without fine-tuning, and prompts were English. Whether the gradient moves with training is not tested here.

## Related

- [[correctness-non-bias-utility-trilemma]] — a conjecture that semantic underdetermination forces a trade-off between correctness, non-bias and decisiveness; the abstract images here are an observed instance of underdetermination, not a test of that conjecture.
- [[semantic-distance-graded-confidence-target]] — grades near-miss emotion labels; the split reported here falls on polarity, which a graded label of that kind would also need to handle.
- [[cross-question-answer-consistency]] — the same paper's measure of whether answers to linked questions agree; the inconsistency it reports is concentrated where the cues are weakest.
- [[conventional-symbol-versus-expressive-feature]] — the symbol questions that the models answer worst, where the cue is a convention rather than a visible object.

[^c1]: arxiv-2511-22929 — "images that can characterized concretely at the visual level are captured more reliably by the VLMs"
[^c2]: arxiv-2511-22929 — "the more elements point in the same direction"
[^c3]: arxiv-2511-22929 — "primarily convey moods through colors and shapes"
[^c4]: arxiv-2511-22929 — "due to semantic underdetermination, they tend to detect both positive and"
[^c5]: arxiv-2511-22929 — "We select 38 images of artworks"
[^c6]: arxiv-2511-22929 — "by hand to understand"
[^c7]: arxiv-2511-22929 — "There are three highly abstract images in our"
[^c8]: arxiv-2511-22929 — "the models struggle with three other categories of artworks: abstract images, allegories, and"
