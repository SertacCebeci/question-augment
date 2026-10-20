---
description: "Chain-of-thought steps that each emit a bounding box, re-rendered onto the chart, help chart reading only when the model already localizes well; weaker localizers gain nothing."
aliases: ["PointCoT", "bounding-box reflection chain-of-thought", "reflective interaction in CoT", "grounding reflection", "point-based CoT"]
sources: ["arxiv-2512-00305"]
---
# Bounding-box reflection in chain of thought

A chart-reading model is trained to write its reasoning as numbered steps and to attach to each grounding step a bounding box marking where on the chart that value is read. The chart is then re-rendered with those boxes drawn on it, so the text is checked against the visual region it names. Xu et al. call this PointCoT, and the link they aim at is "we establish connections between textual reasoning steps and visual grounding regions."[^c1]

The motivating observation is weak grounding. The authors find that multimodal models show "weak grounding in chart elements and proportional relationships, as evidenced by their inability to localize key positions to match their reasoning."[^c2] Asked to point at the region behind each step, the models "either overlook this request or generate entirely" irrelevant positions.[^c3] The reflection is therefore not a prompt that the model can follow on its own; it has to be trained in.

The training data is built automatically. An LLM writes a numerical question with step-by-step reasoning and labels each step as grounding or reasoning. The code that drew the chart is edited to insert marker characters at grounding positions, the chart is re-rendered, and "on each rendered chart to extract embedded character positions" gives the boxes by OCR.[^c4] The result is 19.2K chart samples, each with a CoT and position annotations, which the authors use for supervised fine-tuning of two Qwen-based models.

Two effects are reported. First, the grounding is what carries the gain. The authors' ablation finds that textual CoT alone did not raise the accuracy of reading basic numbers from the chart, and they attribute this partly to the fact that "the reasoning process does not leverage chart information."[^c5] Adding grounding supervision to the steps raised results "particularly on sparse-annotated ChartBench."[^c6] The headline figure is "+5.04% on ChartBench."[^c7] Second, the format of the box matters. The authors compare three numeric encodings of the same boxes and write that "representation format significantly impacts the tuning process."[^c8]

The limit that matters most for transfer is the dependence on the base model. The authors write that "PointCoT is highly dependent on the underlying localization capabilities."[^c11] For two backbones with weaker localization, "BBox fails to enhance their performance further."[^c9] So the mechanism is a check on a reasoning step against a region, and it only adds information when the model can place the region at all.

For question answering in general, what plausibly transfers is the link between each reasoning step and a located piece of evidence, so that a wrong step can be seen against the place it claims to read from. That transfer is my inference; the paper tests only chart QA.

## Limits

- The evidence is chart QA only: ChartQA and ChartBench, under supervised fine-tuning of two models. Open-ended chart questions, other visual domains and text-only questions were not tested.
- The gains depend on a synthetic pipeline (chart code, LLM-written reasoning, OCR-derived boxes). Whether the reflection helps without that supervision is not shown. The stage-one alignment step alone gave "marginal performance improvements," which the authors attribute to the baseline having been optimized for ChartQA.[^c10]
- The boxes are checked against the chart, not against the answer's truth. The paper measures accuracy on benchmarks; it does not show that the boxes causally carry the answer, nor that a faithful box implies a correct number.
- Weaker localizers were tested on only two backbones, and the reflection did not help them. Whether a stronger localizer gives a larger effect was not measured here.

## Related

- [[staged-perception-decomposition]] — also orders a visual answer into stages with boxes, but for detection, where the boxes are the output rather than a check on earlier reasoning
- [[grounding-precision-hardness]] — the weakness this method targets: exact coordinates and object-location binding are where multimodal models fail
- [[post-hoc-visual-augmentation]] — also feeds a re-encoded image back into the reasoning, with image transforms instead of drawn boxes
- [[step-level-region-attribution]] — links reasoning steps to image regions by masking, a causal version of the same step-to-region link
- [[object-grounded-trace-scoring]] — scores a finished trace's object mentions against masks, checking the same link after the fact

[^c1]: arxiv-2512-00305 — "we establish connections between textual reasoning steps and visual grounding regions"
[^c2]: arxiv-2512-00305 — "weak grounding in chart elements and proportional relationships, as evidenced by their inability to localize key positions to match their reasoning"
[^c3]: arxiv-2512-00305 — "MLLMs either overlook this request or generate entirely"
[^c4]: arxiv-2512-00305 — "on each rendered chart to extract embedded character positions"
[^c5]: arxiv-2512-00305 — "the reasoning process does not leverage chart information"
[^c6]: arxiv-2512-00305 — "particularly on sparse-annotated ChartBench"
[^c7]: arxiv-2512-00305 — "+5.04% on ChartBench"
[^c8]: arxiv-2512-00305 — "representation format significantly impacts the tuning process"
[^c9]: arxiv-2512-00305 — "BBox fails to enhance their performance further"
[^c10]: arxiv-2512-00305 — "yields marginal performance improvements"
[^c11]: arxiv-2512-00305 — "PointCoT is highly dependent on the underlying localization capabilities"
