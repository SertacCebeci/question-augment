---
description: "Counting error in vision-language models rises with the number of objects in the picture: small below ten, non-linear past about thirty, and most variable for textured scenes."
aliases: ["count-range error", "enumeration error growth", "object-count degradation", "count magnitude effect"]
sources: ["arxiv-2511-17722"]
---
# Count magnitude and counting error

The number of objects a question asks about is a variable of its own. Before any other feature of the picture or the prompt is changed, a counting question can be easy or hard for a vision-language model, and the paper keeps this variable separate from the rest of its design. It bins the true counts into intervals (below 10, 10–19, and so on up to 40–50) and reports error inside each bin. The point where a model's counts begin to fail can then be read off the bins rather than inferred from one average.

The result is a monotone decline. The paper reports that "counting performance degrades monotonically with increasing object count."[^m1] Below ten the error is small: "In the low-count regime (<10), most models exhibit minimal error (<0.1)."[^m2] Above that the rise is not linear. Error grows non-linearly, "particularly beyond 30."[^m3] The authors summarise the pattern as a level-dependent robustness: performance "remains stable for small sets but declines as visual density and textural complexity increase."[^m4]

The decline is not the same for every model or every feature. Kimi-VL-A3B and Qwen2.5-32B "maintain the lowest relative errors" overall,[^m5] while Qwen2.5-7B and InternVL3-9B are the ones that "exhibit greater sensitivity under large-count conditions."[^m6] Across feature classes, "texture categories consistently exhibit the largest variance,"[^m7] which the authors read as complex surface patterns interfering with "spatial grouping mechanisms."[^m8] So the count and the cue interact: the same count is harder when the texture makes grouping harder. The bins are collapsed across all prompt formulations, so this is a statement about the count, not about the wording of the question.

The reasoning variants share the count sensitivity. For Qwen-Thinking, "images with > 10 objects resulted in interminable reasoning loops" in the reported table, so longer deliberation did not give a usable count at moderate sizes.[^m9] This is consistent with the paper's view that the failure sits in visual grounding and not in the amount of text-side reasoning. The relation to [[segmentation-cue-load]] is that one note says which added cue loads the count, and this one says how large the count is when it is asked.

For someone formulating a count question, this is my inference: the reliability of an answer is set partly by the size of the count and not only by the phrasing. A question about thirty-five objects is a different question from one about five, even when both name the same cue. The paper's data place the change near thirty, but the bins are coarse, so the location of the change is only bracketed to a ten-object interval.

## Limits

- The paper's count range is "object counts ranges (0–50 in increments" of ten.[^m10] Nothing beyond 50 is tested, and the claim about large counts is a claim about 30 to 50.
- "Beyond 30" is a reading of binned averages. No breakpoint is fitted and no confidence interval is given in the text. The 30–39 and 40–50 bins both lie above it, so the data bracket the change but do not locate it.
- The count is varied together with density. The images are "512×512 pixel images containing non-overlapping black circular objects,"[^m11] so more objects in the same frame are also denser and smaller. The paper names density as a factor in the decline, but the text does not separate the count from the density (my inference).
- The text reports only relative error, which divides the miss by the true count. A given miss weighs less at a high count under that normalization, so the text's trend is not checked against absolute error (my inference).
- The bins are from the synthetic benchmark, with a fixed object shape and a white background. Whether real scenes with occlusion show the same bins is not tested here; the paper names this as open.
- The benchmark uses three open-source families. The paper's own limitation is that its analysis "is limited to open-source VLMs," so the rank order of models is for these checkpoints only.

## Related

- [[segmentation-cue-load]] — the other axis of the same benchmark: which added cue loads the count, where this note covers how large the count is
- [[enumeration-cue-dependence]] — whether a serial count runs at all depends on the cue; here the question is how much count a running procedure can hold

[^m1]: arxiv-2511-17722 — "counting performance degrades monotonically with increasing object count"
[^m2]: arxiv-2511-17722 — "In the low-count regime (<10), most models exhibit minimal error (<0.1)"
[^m3]: arxiv-2511-17722 — "particularly beyond 30"
[^m4]: arxiv-2511-17722 — "performance remains stable for small sets but"
[^m5]: arxiv-2511-17722 — "maintain the lowest relative errors"
[^m6]: arxiv-2511-17722 — "exhibit greater sensitivity under large-count conditions"
[^m7]: arxiv-2511-17722 — "texture categories consistently exhibit the largest variance"
[^m8]: arxiv-2511-17722 — "spatial grouping mechanisms"
[^m9]: arxiv-2511-17722 — "in interminable reasoning loops"
[^m10]: arxiv-2511-17722 — "object counts ranges (0–50 in increments"
[^m11]: arxiv-2511-17722 — "512×512 pixel images containing non-overlapping black circular objects"
