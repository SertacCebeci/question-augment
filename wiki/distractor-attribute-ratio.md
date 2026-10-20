---
description: "Under visual distractors, the share of a reasoning trace's visual attributes tied to distractors, not the trace's length, tracks the final answer's accuracy."
aliases: ["distractor attribute ratio", "distractor attribute fraction", "distractor-related attribute share"]
sources: ["arxiv-2511-21397"]
---
# Distractor attribute ratio

A reasoning vision-language model writes out visual attributes as it thinks: the colour of an object, its shape, its surroundings. Each attribute can be linked to the target object or to a distractor inserted into the image. The distractor attribute ratio is the fraction of a trace's attributes that are linked to distractors. In the Idis study, measured on Qwen3 traces with conflicting distractors, the ratio tracked the final answer closely: "Final predictions are strongly influenced by the raw fraction of distractor attributes".[^d1] The accuracy "drops to near zero whenever the distractor attribute ratio exceeds 50%,"[^d2] and "remains above 97% whenever the ratio is below 20%."[^d3]

The ratio is not the same as how long the trace is. Adding distractors leaves the total number of attributes about the same and changes their mix: "the fraction of distractor attributes, on the other hand, steadily grows as we increase the number of distractors."[^d4] The ratio also rises with the area the distractors cover: "Distractor attributes increase with distractor area".[^d5] This is the mechanism the paper offers for the modality split. Visual distractors lower accuracy by changing which attributes the model writes down, so the length-accuracy curve shifts downward without stretching along the length axis, which is the opposite of the textual case in [[distractor-similarity-reasoning-inflation]]. The paper states the claim as "distractor attribute ratio—not reasoning length—drives accuracy for visual distractors".[^d6]

The paper also tests whether the attributes act on the answer or only accompany it. Blocking the final answer tokens' attention to distractor-related attributes "improves accuracy", while blocking target-related attributes degrades it.[^d7] The authors read this as the trace guiding the answer: "the latter is more plausible than the former."[^d8] Here "the latter" is the reasoning trace guiding the final prediction, against the reverse. The blocking results are the reason for that reading, not a direct trace-to-error test.

What follows, in my inference and not the paper's wording: the lever under visual distraction is what the trace attends to, not how long it runs. The paper says as much when it writes that the robust reasoning "may require mechanisms that suppress distractor attributes during trace generation."[^d9] The paper also reports a prompt that lowers the ratio and raises accuracy a little, and says that the measure, not the prompt, is the finding it stands behind. The prompt's content is not carried here.

The same measure is applied to Waterbirds, where the distractor is the background rather than an inserted object: "distractors arise from background context rather than localized inserted objects."[^d10] A background-share measure computed on saliency maps is a different object; see [[background-attribution-share]].

## Limits

- The link is correlational across traces. The attention-blocking test is the only causal-leaning evidence, and it intervenes on the answer tokens' access to trace attributes, not on the trace text itself. It does not show that a particular attribute produced a particular wrong answer.
- Attributes are extracted by another language model. The paper uses "DeepSeek-V3.2-Exp (DeepSeek-AI, 2025) with structured instructions" and validates that extraction in an appendix, which this note has not read.[^d11] The ratio is only as stable as that parser.
- The curves are for one model. "The plots are for Qwen 3, when we add conflicting distractors."[^d12] The 50% and 20% thresholds are from that model. The Idis-math result is reported as "a similar pattern" with a threshold of 0.4 on the ratio, so the numbers do not transfer across tasks.
- The distractors are generated or composited and then checked by people. "Our analyses focus on a VQA domain"[^d13], on ImageNet-9 and MathVerse. Natural clutter, agentic tasks and other model families are not tested here.
- The prompt-based gain is small. The paper says its prompting strategy "is somewhat limited in its ability to improve" accuracy.[^d14]

## Related

- [[distractor-similarity-reasoning-inflation]] — the textual-context side: there inflation tracks similarity, while visual distractors leave trace length flat.
- [[test-time-scaling]] — the wider frame; this note measures what the extra tokens contain rather than how many there are.
- [[background-attribution-share]] — another measure of background reliance, computed on saliency rather than on trace text.
- [[clutter-induced-recognition-error]] — a visual misreading caused by crowding in a diagram, the same kind of visual distraction.
- [[step-level-region-attribution]] — a region-masking method that attributes trace steps to image regions, the nearest causal tool to the attention-blocking test here.

[^d1]: arxiv-2511-21397 — "Final predictions are strongly influenced by the raw fraction of distractor attributes"
[^d2]: arxiv-2511-21397 — "The accuracy drops to near zero whenever the distractor attribute ratio exceeds 50%,"
[^d3]: arxiv-2511-21397 — "yet remains above 97% whenever the ratio is below 20%."
[^d4]: arxiv-2511-21397 — "the fraction of distractor attributes, on the other hand, steadily grows as we increase the number of distractors."
[^d5]: arxiv-2511-21397 — "Distractor attributes increase with distractor area"
[^d6]: arxiv-2511-21397 — "distractor attribute ratio—not reasoning length—"
[^d7]: arxiv-2511-21397 — "blocking the attention of the final answer tokens to distractor-related attributes improves accuracy"
[^d8]: arxiv-2511-21397 — "the latter is more plausible than the former"
[^d9]: arxiv-2511-21397 — "mechanisms that suppress distractor attributes during trace generation"
[^d10]: arxiv-2511-21397 — "distractors arise from background context rather"
[^d11]: arxiv-2511-21397 — "We use DeepSeek-V3.2-Exp (DeepSeek-AI, 2025) with"
[^d12]: arxiv-2511-21397 — "The plots are for Qwen 3, when we add conflicting distractors."
[^d13]: arxiv-2511-21397 — "Our analyses focus on a VQA domain"
[^d14]: arxiv-2511-21397 — "is somewhat limited in its ability to improve"
