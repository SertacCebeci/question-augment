---
description: "Attachment and detachment of a hand and an object mark where an interaction starts and ends; video models name the action around that frame but cannot locate it."
aliases: ["contact-release event", "core interaction event", "attachment-detachment event", "physical contact and release"]
sources: ["arxiv-2511-20162"]
---
# Contact-release event

An interaction between an agent and an object has a boundary in time: the frame where the object becomes attached to the agent (contact) or detached from it (release). Harari et al. annotate exactly this pair of things, asking for "the frame number and image coordinates where the physical event occurs".[^c1] The boundary is a discrete change in coupling, not a stretch of motion, so it can be pinned to a frame. A question about when an interaction starts or ends can therefore have an answer that is a frame, not a verb.

The concept is taken from developmental psychology, where "physical contact and release are considered" primitives of causal reasoning, the "foundational building blocks that allow" people to move beyond surface correlations to agency and physical law.[^c2] The paper uses this to motivate why the boundary matters for video models. It does not test the developmental claim.

On the annotations, the frame of the boundary is well defined for humans. Three random annotators agreed on the frame with an intraclass correlation of 0.95, but only at a "medium agreement level on the spatial location where the events occur" (ICC 0.73 and 0.39 for the two coordinates).[^c3][^c4] The paper's figure shows that a hand can sit near an object without contact: "Humans are sensitive to the gap between the hand and the target object even one frame before a contact or after a release."[^c5] Two naive human subjects reached 43.00% exact-frame accuracy, and the text reports their one-frame-off score as "for 1-frame off - high above the best performing model".[^c6][^c7]

The models show the mirror image. Asked to name the action and the objects, they do well: "the models demonstrate robust global understanding", with most reaching over 85% top-5 action accuracy.[^c8] Asked for the frame where contact or release occurs, their exact-frame accuracy is "about chance level (10%)" for the ten-frame clips, and the best one-frame-off accuracy is 42.9%.[^c9][^c10] The failures tend to fall on frames with no visible contact.[^c11] The predicted image region is also poor: the best mean intersection-over-union with the labelled point is 0.147.[^c12]

Tolerance is part of the measurement. The same model answers score very differently at exact-frame and at one-frame-off tolerance, and the human scores move the same way. A reported frame accuracy means little without the tolerance it used. The paper reports both, which is why the gap is visible at all.[^c9][^c7]

Asking for the grounding did not close the gap. Prompts that asked for step-by-step reasoning, or for the target object to be named first, did not necessarily raise accuracy, and "these instructions, may sometimes yield a decrease in the models’ performance."[^c13] This is the paper's observation on its own prompting conditions; it does not show that no verbal scaffold could help.

## Limits

- The test is small: 33 videos, 99 events, ten frames each, with each event isolated by hand from a busier clip. Per-model figures rest on that set.
- Only the 10K-video dataset was annotated by one worker per video. Inter-rater agreement was measured on a subset, and the spatial agreement is only medium.
- The human ceiling is two naive subjects, not experts.
- The events are hand-object contacts in Something-Something-V2, a set of staged actions. Whether the same boundary definition holds for tool use, occlusion or continuous contact is not tested here.
- The paper's account of why models fail (a "loose integration" between visual and language representations, and a missing "System 2") is stated as a hypothesis: "We hypothesize that the main limitation is rooted in a loose integration between the visual".[^c14] The data show the localization failure, not its cause.
- Using the boundary to shape a question is my inference from this paper, not something it tests.

## Related

- [[grounding-answer-dual-axis-audit]] — the same split between a correct answer and failed grounding, here in time rather than in space
- [[evidence-localization-gap]] — localizing before judging does not reliably help in a different setting, figure panels
- [[clever-hans-effect]] — a model that keys on a cue correlated with the answer, here a hand near an object
- [[counterfactual-image-grounding-audit]] — a test that the answer depends on the evidence, of the kind this boundary task supplies

[^c1]: arxiv-2511-20162 — "the frame number and image coordinates where the physical event occurs"
[^c2]: arxiv-2511-20162 — "physical contact and release are considered"
[^c3]: arxiv-2511-20162 — "The results indicate a high agreement level on the frame annotation (ICC of 0.95)"
[^c4]: arxiv-2511-20162 — "medium agreement level on the spatial location where the events occur"
[^c5]: arxiv-2511-20162 — "Humans are sensitive to the gap between the hand and the target object even one frame before a contact or after a release"
[^c6]: arxiv-2511-20162 — "the mean accuracy on the event frame detection task was"
[^c7]: arxiv-2511-20162 — "for 1-frame off - high above the best performing model"
[^c8]: arxiv-2511-20162 — "the models demonstrate robust global understanding"
[^c9]: arxiv-2511-20162 — "the models’ accuracy is about chance level (10%) for detecting the exact frame where the event occurs"
[^c10]: arxiv-2511-20162 — "The accuracy for an error tolerance of one-frame off peaks at 42.9% with"
[^c11]: arxiv-2511-20162 — "the models’ failure often tends to frames with no visual grounding of a physical contact"
[^c12]: arxiv-2511-20162 — "mean IoU of only 0.147 for Gemini-3-Pro"
[^c13]: arxiv-2511-20162 — "these instructions, may sometimes yield a decrease in the models’ performance"
[^c14]: arxiv-2511-20162 — "We hypothesize that the main limitation is rooted in a loose integration between the visual"
