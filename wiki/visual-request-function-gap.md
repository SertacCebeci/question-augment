---
description: "A sketched or annotated request carries layout but not behaviour: vision-language models copied the drawn layout and missed the implied function, the most common of three error types."
aliases: ["visual interpretation gap", "sketch-to-function gap", "layout-without-function errors"]
sources: ["arxiv-2601-04203"]
---
# Visual request function gap

A request can arrive as text or as a drawing on a screenshot: a sketch of a new layout, or an annotation pointing at an element. The FronTalk paper gives the same intent in both channels and finds the drawn channel harder. "Visual feedback proves consistently more difficult than textual feedback, resulting in significantly lower pass rate."[^c1] The paper's name for this is the visual interpretation gap.

The mechanism it reports is about what the drawing carries. The authors analysed 608 cases where a model failed the visual version of an instruction but passed its textual equivalent.[^c2] The most frequent error is "Failure to implement implicit functionalities, the most common": the model "replicate[s] the UI layout but fail[s] to implement the underlying functionalities."[^c3] [^c4] Its example is the page-update behaviour of navigation arrows, which the model leaves unimplemented while the layout is reproduced.[^c12] The paper calls this "the literal replication of layout sketches without implementing the underlying functionality."[^c5] The second error type is missing text annotations, "especially in densely annotated images."[^c6] The third, misreading of visual clues, is the least common.

A sketch specifies where something goes and how it looks. It does not specify what the element must do when used. A text request usually states the behaviour; a drawn one leaves it to be inferred, and the answerer that copies the surface produces the layout without the function. My inference, not the paper's: the failure is one of what the channel can express, not only of the model's perception. The paper's wording is that the gap is about a visual instruction's "implicit functionalities," which is a claim about content, so the same reasoning applies to any drawn or pointed request whose effect is not visible in the image.

The paper also reports that the gap is wider for open-source models: the degradation "is particularly pronounced for open-source VLMs."[^c7]

## Limits

- Error analysis was done on two representative models, GPT-4o and Qwen2.5-VL-72B, from 608 failing cases. The percentages behind "most common" and "least common" are in the paper's figure, which this note did not read; the ordering is what is claimed.
- The visual instructions were produced by a simulator, and the paper reports that visual simulation is less reliable than textual simulation: "Visual simulation shows slightly lower reliability."[^c8] Part of the gap may be simulator error. The paper then uses a stronger simulator and reports fidelity comparable to the textual one, which narrows this worry but was not checked independently.[^c10]
- The paper says "most of these issues stem from fundamental model capabilities."[^c9] So the channel explains part of the gap, and the rest is model capacity. The note's claim about the channel is therefore weaker than the paper's title might suggest, and the split was not measured.
- Only front-end code generation was tested. Whether drawn requests in other domains, such as diagrams or chart edits, show the same behaviour-omission pattern is not established here.
- The one proposed remedy in the paper, a critique of prior instructions, addresses forgetting and not the visual gap as its primary target; the gain there is smaller for visual instructions, since "the gains are more modest" there,[^c11] and this note does not claim a fix.

## Related

- [[textual-annotation-dependence]] — a related reliance on printed text in visual answers; here the printed annotations themselves are missed in dense images.
- [[functional-perception-gap]] — the same shape in another field: a model that learned the anatomy reads the layout and misses the function, in PET imaging. The transfer is only of the failure shape.
- unsolicited-disclosure-dependence — a drawing leaves its behaviour unsaid, as a silent user leaves the intent unsaid.
- [[cross-turn-requirement-overwrite]] — the other error family in the same paper, in which the visual channel is not the issue.

[^c1]: arxiv-2601-04203 — "Visual feedback proves consistently more difficult than textual"
[^c2]: arxiv-2601-04203 — "analyze 608 test cases where VLMs fail the visual"
[^c3]: arxiv-2601-04203 — "Failure to implement implicit functionalities, the most common"
[^c4]: arxiv-2601-04203 — "where VLMs replicate the UI layout but fail to implement the underlying functionalities"
[^c5]: arxiv-2601-04203 — "literal replication of layout sketches without implementing the underlying functionality"
[^c6]: arxiv-2601-04203 — "especially in densely annotated images"
[^c7]: arxiv-2601-04203 — "pronounced for open-source VLMs"
[^c8]: arxiv-2601-04203 — "Visual simulation shows slightly lower reliability"
[^c9]: arxiv-2601-04203 — "While most of these issues stem from fundamental model capabilities"
[^c10]: arxiv-2601-04203 — "to that of the textual instruction simulator"
[^c11]: arxiv-2601-04203 — "the gains are more modest"
[^c12]: arxiv-2601-04203 — "failing to implement the page-update behavior for navigation arrows"
