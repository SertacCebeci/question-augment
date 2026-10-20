---
description: "A vision-language model's attention to its input images falls as its reasoning chain lengthens; a tool call that re-presents an image restores it, measured by attention ratio."
aliases: ["visual forgetting", "image attention decay", "visual neglect in long reasoning", "text inertia", "reasoning drift"]
sources: ["arxiv-2512-08980", "arxiv-2512-05546", "arxiv-2512-02699"]
---
# Visual forgetting during reasoning

A vision-language model reasons partly in text, and as that text grows its attention to the input images shrinks. The paper measures this on Qwen2.5-VL: its attention to image tokens "gradually decreases and approaches zero under multi-image input"[^c1], and without tool use "token-level focus on image content drops to near zero in later inference stages."[^c2] The authors read the cause as a training habit: the model leans on its first look at the image and keeps "continuing reasoning based on already generated linguistic content rather than revisiting visual evidence."[^c3] The effect is worst with several images, where the model "gradually stops attending to images in later reasoning steps."[^c4]

The remedy the paper builds is an explicit way to look again. IMAgent is trained with reinforcement learning to call two tools inside its chain: a zoom-in that crops a region, and "visual reflection (lookback reuse to restore global context)."[^c5] The tool output is appended to the context and the model continues from it. The authors say that "through timely tool calls, refocuses image attention."[^c6] The mechanism is therefore not a better encoding of the image at the start, but a second presentation of the image at the point where the text has already drifted away from it.

The attention effect is quantified with a ratio: the mean attention inside a region divided by the mean attention outside it. On 100 samples from the V* dataset, the ratio for answer-relevant regions is the quantity reported.[^c7] The untrained baseline gets 10. "Equipping the same model with tools raises this to" 19.0, and the trained agent reaches a higher value: "IMAgent further improves it to 26.9."[^c8][^c9] So tools alone raise the ratio, and training raises it further. The authors also claim that "explicit visual reflection enables the model to reexamine images," which they link to accuracy gains on multi-image benchmarks.[^c10]

## Relation to text-only decay

The same shape appears in text-only search agents. There, the longer the reasoning written before a search, the less the model uses the retrieved document, because earlier reasoning dominates attention while the document is encoded; see [[knowledge-integration-decay]]. My inference, not the paper's claim: both are a source losing weight against the model's own preceding output. The fixes differ. The text-search paper repeats the document after the reasoning; this paper re-supplies the image through a tool the model chooses to call. Whether repetition of the image at a fixed point would help as well was not tested here.

## The same decay as a precursor to error

A separate paper on InstructBLIP calls a closely related drop "text inertia": attention drifts from the image toward the model's own generated text. Its analysis of captions is the basis for its claim that this is "a primary failure mode".[^c13] The paper reports that "67% of hallucinations occur after" the image attention has fallen low, and that the drop begins "visual attention drops below 20%, indicating a mid-generation" loss of focus.[^c14][^c15] It also reports irreversibility: "Once attention shifts to text priors, the probability of recovering visual grounding drops by 84%."[^c16] So the decay is read here as a precursor of error, not only a property of long reasoning. The statistics are observational, drawn from the paper's own captions, and they do not show that the drop causes the error. Whether the two papers measure the same object is my inference. The remedy differs: that paper re-weights attention internally at the trigger, see [[interaction-variance-gate]], rather than re-presenting the image through a tool.

## The same drift in emotion reasoning

The MIGR paper on multimodal emotion reasoning describes the same shift for audio and vision: "the model’s attention gradually shifts from multimodal inputs" to its own generated text as reasoning proceeds, and the shift makes the model "anchor its subsequent reasoning on whatever emotional cues appear in" its first generated segment.[^c17][^c18] The paper's Figure 1(a) caption opens with the claim that "The model’s attention gradually drifts from external" inputs toward generated text, and the figure is a schematic.[^c19] The remedy it builds is not a second look at the input but a change of order: the first segment is the one carrying the dominant modality, so the early anchor sits on the informative channel (see [[modality-importance]]). Whether re-presenting the input would help in that setting is not tested in the work.

## Limits

- The emotion-setting drift is a schematic plus one baseline, and the sections read report no attention share across the length of the reasoning. It is an observation in that work, not a measurement (my reading).
- The attention ratio is a proxy. The paper's own wording is hedged: "This suggests that the performance gains of IMAgent stem from more precise visual localization" of relevant regions.[^c11] A high ratio shows where attention goes, not that the answer depends on it.
- The analysis rests on one baseline (Qwen2.5-VL-7B) against one trained agent, and on 100 V* samples for the quantitative part. Nothing I read shows the decay across other model families or reasoning lengths.
- Forgetting is measured as attention share, not as errors. The link to accuracy is asserted in the text: "When facing complex visual scenarios, this often leads to performance degradation."[^c12] The accuracy ablations, including the run without the reflection tool, were not read in this pass, so how much of the gain the reflection tool alone accounts for is not stated here.
- The tool-call trace in the paper is one worked example. Whether models decide to look again at the right moment, rather than looping or looking at the wrong region, is outside the attention analysis.

## Related

- [[knowledge-integration-decay]] — the text-only analogue: earlier reasoning dominates attention to retrieved evidence, and duplicating the document partly restores its use
- [[confidence-triggered-visual-reattention]] — a single crop-and-requery gated on the model's own confidence, where this paper's tool is called at the model's discretion
- [[coarse-to-fine-evidence-zoom]] — a second, finer look at evidence in video, with the zoom fixed rather than chosen
- [[tool-integrated-reasoning]] — the general frame in which a reasoner calls tools inside its chain

[^c1]: arxiv-2512-08980 — "gradually decreases and approaches zero under multi-image input"
[^c2]: arxiv-2512-08980 — "content drops to near zero in later inference stages"
[^c3]: arxiv-2512-08980 — "toward continuing reasoning based on already generated linguistic content rather"
[^c4]: arxiv-2512-08980 — "gradually stops attending to images in later"
[^c5]: arxiv-2512-08980 — "visual reflection (lookback reuse to restore global context)"
[^c6]: arxiv-2512-08980 — "through timely tool calls, refocuses image attention"
[^c7]: arxiv-2512-08980 — "we evaluate on 100 samples from the V* dataset"
[^c8]: arxiv-2512-08980 — "Equipping the same model with tools raises this to"
[^c9]: arxiv-2512-08980 — "IMAgent further improves it to 26.9"
[^c10]: arxiv-2512-08980 — "Explicit visual reflection enables the model to reexamine images"
[^c11]: arxiv-2512-08980 — "This suggests that the performance gains of IMAgent stem from more precise visual localization"
[^c12]: arxiv-2512-08980 — "this often leads to performance degradation"
[^c13]: arxiv-2512-05546 — "Our analysis of 2,000 MSCOCO captions"
[^c14]: arxiv-2512-05546 — "67% of hallucinations occur after"
[^c15]: arxiv-2512-05546 — "visual attention drops below 20%, indicating a mid-generation"
[^c16]: arxiv-2512-05546 — "Once attention shifts to text priors, the probability of recovering visual grounding drops by 84%."
[^c17]: arxiv-2512-02699 — "the model’s attention gradually shifts from multimodal inputs"
[^c18]: arxiv-2512-02699 — "anchor its subsequent reasoning on whatever emotional cues appear in"
[^c19]: arxiv-2512-02699 — "The model’s attention gradually drifts from external"
