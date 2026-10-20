---
description: "A grounding answerer can fail to say that no object fits a description with a subtle error; most MLLMs score 0% on that rejection, and negative training data lifts it only partly."
aliases: ["ungroundable-query rejection", "reject misleading description", "no-referent rejection", "grounding rejection"]
sources: ["arxiv-2512-17495"]
---
# Referent rejection — saying that no object fits

A grounding answerer is given an image and a description and must return the box of the object the description names. A referent-rejection item is a description that fits no object in the image, because it carries a subtle error: a wrong attribute, a wrong part, or a relation that does not hold. The correct output is no box. GroundingME builds these items by editing correct descriptions. Its Rejection category has "no object for Rejection samples" as the ground truth, and annotators "intentionally introduce factual errors for Rejection" into the description.[^c1][^c2] The category is 201 of 1,005 items.[^c3]

The reason to measure it apart from ordinary grounding is that ordinary grounding accuracy says nothing about it. The authors argue that prior benchmarks "overlook the model ability to reject a description when its fine-grained details do" not match the image.[^c4] In their evaluation the gap is large. Most models score 0% on this category, and "on the Rejection category, with most models scoring 0%."[^c5] Without thinking, "most models exhibits 0% accuracy on the Rejection task."[^c6] Enabling thinking "generally improves performance and enables basic rejection" behaviour,[^c7] but rejection "still remains low under the thinking mode."[^c8]

The mechanism the authors propose is a training gap. They hypothesise that "the models' inability to reject stems from a lack of negative samples in training data."[^c9] To test it they took 30,000 RefCOCOg training descriptions and built a matching negative for each "by modifying the description," then fine-tuned Qwen3-VL-8B-Instruct on mixtures of the two.[^c10] In-domain, "simple incorporation of negative data effectively enables the model to learn" the rejection behaviour.[^c11] On the out-of-domain benchmark, rejection accuracy rose "from 0% to 27.9%" in the headline run.[^c12]

The same intervention costs something elsewhere. Positive grounding "demonstrates a clear degradation compared to the pre-fine-tuned baseline," from 38.8% to a maximum of 33.0% on the non-rejection categories.[^c13] The authors' reading is that the rejection gain "does not generalize for free to higher-difficulty, out-of-domain scenarios."[^c14] So a model that learns to say "no box" from negatives in one distribution does not keep its positive accuracy in another without further work.

## What the notion is, and is not

Referent rejection is a third answer, like [[abstention]], but it is triggered differently. Selective prediction gates the answer on a confidence score against a threshold. Here the trigger is the content of the description: whether any object in the image satisfies it. The paper does not measure the model's confidence on rejection items, so nothing here says whether the two signals coincide. This distinction is my inference from the design.

It also differs from the empty-box fallback in [[misleading-grounding-propagation]]. That fallback also yields "no box," but it is set off by a detector's low confidence, not by the description being false.

## Limits

- The rejection items are the authors' edits. What counts as a "misleading" description is their choice of error types, and the paper's measure of label reliability is "pairwise Cohen’s kappa scores of 0.64–0.73 (avg. 0.69), indicating substantial consistency," computed on 50 random samples.[^c15] Whether real users' false descriptions look like these edits is not tested.
- The in-domain evaluation uses "the macro average accuracy across both negative and positive classes," so a model that rejects too often is penalised there.[^c16] The out-of-domain table reports the categories separately; the excerpts read do not show a single balanced score for it.
- The training result rests on one base model (Qwen3-VL-8B-Instruct), one source dataset (RefCOCOg), and three epochs. Other models and other source datasets were not read.
- The 0% figures describe "most" models, not all. The paper does not report what prompt was used for the no-thinking condition beyond the appendix, which was not read here.

## Related

- [[abstention]] — selective prediction gates on a confidence threshold; referent rejection answers "no box" because the description has no referent, so the two need separate measures.
- [[misleading-grounding-propagation]] — an empty-box fallback also outputs "no box," triggered by low detector confidence rather than by a false description.

[^c1]: arxiv-2512-17495 — "refers to one and only one object, or no object for Rejection samples"
[^c2]: arxiv-2512-17495 — "intentionally introduce factual errors for Rejection"
[^c3]: arxiv-2512-17495 — "Rejection (201, 20.0%)"
[^c4]: arxiv-2512-17495 — "these works overlook the model ability to reject a description when its fine-grained details do"
[^c5]: arxiv-2512-17495 — "on the Rejection category, with most models scoring 0%."
[^c6]: arxiv-2512-17495 — "most models exhibits 0% accuracy on the Rejection"
[^c7]: arxiv-2512-17495 — "generally improves performance and enables basic rejection"
[^c8]: arxiv-2512-17495 — "still remains low under the thinking mode"
[^c9]: arxiv-2512-17495 — "inability to reject stems from a lack of negative"
[^c10]: arxiv-2512-17495 — "construct 30,000 corresponding negative samples by modifying the description"
[^c11]: arxiv-2512-17495 — "Simple incorporation of negative data effectively enables the model to learn"
[^c12]: arxiv-2512-17495 — "from 0% to 27.9%"
[^c13]: arxiv-2512-17495 — "a clear degradation compared to the pre-fine-tuned baseline"
[^c14]: arxiv-2512-17495 — "generalize for free to higher-difficulty, out-of-domain scenarios"
[^c15]: arxiv-2512-17495 — "of 0.64–0.73 (avg. 0.69), indicating substantial consistency."
[^c16]: arxiv-2512-17495 — "The macro average accuracy across both negative and positive classes"
