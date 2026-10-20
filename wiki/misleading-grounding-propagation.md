---
description: "When a reasoner localizes evidence before judging, a wrong box carries into the rationale and raises hallucination; sending unsure cases to global context limits the damage."
aliases: ["grounding error propagation", "misleading visual evidence", "strict grounding fallback", "empty-box global fallback"]
sources: ["arxiv-2512-23169"]
---
# Misleading grounding propagation

A reasoner that first points at the evidence and then reasons over it inherits the pointing error. In REVEALER, a multimodal model is trained to emit a "special token <box>, followed by a predicted bounding box list that localizes a semantic element from the input prompt within the generated image," then a free-form rationale, then a score.[^c1] The boxes come from an external detector (Grounding DINO) run on each prompt element, and the rationale is conditioned on them. When the box is wrong, the rationale is built on the wrong region.

The authors split a 2,000-pair human-boxed set by whether the detector's box overlapped the gold box (MIoU of at least 0.5 versus below 0.5). With accurate boxes, the reasoning hallucination rate was 8.4%, and alignment accuracy was 89.6%. With misleading boxes it rose to 46.2%, and accuracy fell to 76.3%.[^c2] The authors read this as direct propagation: "confirms that incorrect visual cues actively mislead the reasoning process."[^c3] The mechanism is that a rationale has no independent check on whether its cited region is the right one; it narrates what it was given.

## The fallback

The same paper adds a gate on the detector instead of on the answer. It raises the detector's confidence threshold from 0.35 to 0.55, which "encourages the output of empty box lists ([]) when visual evidence is ambiguous, which prevents grounding error propagation."[^c4] An empty list switches the model to global reasoning over the whole image, for abstract elements the paper says "switch to global reasoning for abstract concepts."[^c5]

The effect is concentrated where localization is weakest. For abstract elements the empty-box share rose from 12.4% to 53.0%, and their accuracy rose by 4.2 points; for concrete elements the empty-box share changed by only 2.4 points and accuracy by 0.9.[^c6] On the 2,000-pair set, the strict-grounding condition brought hallucination down to 14.7% and accuracy to 81.2%, which the authors summarize as "relying on global context is far superior to reasoning based on erroneous visual evidence."[^c7]

The point for asking and answering is that "I could not locate it" is itself a usable state. An answerer that cannot tell a reliable pointer from a misleading one can decline to build on the pointer and reason from what it sees overall, rather than committing to a narrated region.

## Limits

- The grouping in Table 4 uses the gold box, which the answerer does not have at test time. The deployed gate uses detector confidence as a proxy for a misleading box, and the paper does not report how well that confidence separates the two groups beyond the single threshold change.[^c8]
- Only two thresholds (0.35 and 0.55) were compared, on one benchmark, with one base model (Qwen3-VL-8B for the error analysis). No threshold curve or other detector was read.
- The link between wrong boxes and wrong reasoning is measured as correlation: "a strong positive correlation (Pearson r = 0.8773) between grounding accuracy and alignment scores."[^c9] A hard image can make both the box and the judgment fail together, so the direction of propagation is the authors' reading, not something the design isolates. This is my inference.
- The gate trades evidence for context. For a case where the global view is also uninformative, going global does not recover the answer, and the paper does not measure that group separately.
- The authors state the box paradigm "is optimized for concrete semantic elements and may be less naturally suited for evaluating holistic qualities."[^c10] The mechanism therefore applies where evidence has a spatial location; it is not shown for style, mood, or temporal content.

## Related

- [[grounding-answer-dual-axis-audit]] — crosses localization with answer correctness to find ungrounded correct answers; this note is the mechanism by which a bad localization reaches the answer
- [[cot-hallucination-trap]] — when visual grounding is weak, rationales follow the question's language prior; the same failure seen from the rationale side
- [[ungrounded-reasoning-gap-ratio]] — how far a trace keeps fabricating after it first voices uncertainty; a measure of reasoning past a failed evidence step
- [[visual-robustness-score]] — separates answers that are visually grounded from ones that match a textual trap, another guard against credit for lucky reasoning

[^c1]: arxiv-2512-23169 — "followed by a predicted bounding box list that localizes a semantic element from the input prompt within the generated image"
[^c2]: arxiv-2512-23169 — "reasoning hallucination rate to 46.2%"
[^c3]: arxiv-2512-23169 — "confirms that incorrect visual cues actively mislead the reasoning process"
[^c4]: arxiv-2512-23169 — "which prevents grounding error propagation"
[^c5]: arxiv-2512-23169 — "switch to global reasoning for abstract concepts"
[^c6]: arxiv-2512-23169
[^c7]: arxiv-2512-23169 — "demonstrating that relying on global context is far superior to reasoning based on erroneous visual evidence"
[^c8]: arxiv-2512-23169
[^c9]: arxiv-2512-23169 — "correlation (Pearson r = 0.8773) between grounding accuracy and alignment scores"
[^c10]: arxiv-2512-23169 — "is optimized for concrete semantic elements and may be less naturally"
