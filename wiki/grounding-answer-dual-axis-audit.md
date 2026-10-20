---
description: "Crossing evidence-localization success (crop overlap with gold box) with answer correctness separates lucky-correct answers from evidence-based ones that accuracy alone hides."
aliases: ["dual-axis capability matrix", "ungrounded correct answer", "grounded visual evidence audit", "answering-grounding gap", "judge-based faithful tool-use rate"]
sources: ["arxiv-2601-11633", "arxiv-2512-05091", "arxiv-2512-03479", "arxiv-2511-20162", "arxiv-2511-19661"]
---
# Grounding-answer dual-axis audit

Outcome accuracy cannot tell whether an answer rested on the evidence the question required. The audit scores each item on two orthogonal axes: whether the final answer is correct, and whether the evidence the model actually looked at overlaps expert-annotated gold evidence. Crossing them gives four quadrants. The setting is ViEBench, 200 high-resolution images where the evidence averages under 0.7% of the image area, so that it is invisible in a global view and the model must zoom in.[^c1]

## Mechanism

Grounding is scored by intersection-over-area between the model's crop and the gold box, taken in both directions. The final score is the maximum of the two, so tight crops and conservative expansive crops both count.[^c2] Grounding succeeds when the score exceeds 0.5. The quadrants are:

- Valid Grounded Reasoning (G+·A+): evidence found and answer right. This is the primary metric for verifiable reasoning.
- Ground-Success Answer-Failure (G+·A−): evidence found but the answer is wrong.
- Ungrounded Correct Answer (G−·A+): the answer is right although grounding failed.
- Dual failure (G−·A−): both wrong.[^c3]

The quadrants point to different repairs. A high G+·A− rate says the bottleneck is integrating the localized cue into reasoning. A high G−·A+ rate says correct answers come from textual priors or redundant cropping, not from the visual evidence.[^c4]

## What was observed

- Mini-o3 had the highest grounding score on reasoning tasks (78%) and also the peak G+·A− rate (28%). The authors read this as a failure to synthesize localized cues, not blind search.[^c5]
- Thyme's G−·A+ rate reached 57% on reasoning tasks despite competitive accuracy and a 16% tool-use ratio, so its tool calls were often redundant crops.[^c6]
- Qwen3-VL-32B-Instruct had high G+·A+ (71% on perception) with G−·A+ of only 9%, which the authors take as success derived from faithful evidence.[^c7]
- Pixel Reasoner's grounding stayed near 65% across task types, but G+·A+ fell from 54% (perception) to 40% (reasoning). Localization is necessary but not sufficient for correct reasoning.[^c8]
- A second instance comes from a segmentation benchmark, where the trace is scored by matching its named objects to ground-truth masks rather than by crop overlap. There, baseline models keep some answer accuracy while scoring zero on trace grounding.[^c10] Reinforcement learning on one model raised answer mIoU from 59.5 to 62.1 without improving trace visual quality, so an answer gain can occur with no gain in grounding.[^c11] See [[object-grounded-trace-scoring]] for the matching procedure.
- A temporal instance comes from ProcObject-10K, a video benchmark of object-state questions on instructional clips. The abstract reports that "models produce plausible answers while failing to localize the supporting evidence".[^c12] The authors name the result an answering-grounding gap, a "discrepancy between answering plausibility and grounding precision".[^c13] Grounding here is a time span scored by mIoU, not a crop, and the text read reports the answer and grounding scores side by side. It does not cross them per item into the four quadrants, so the per-item split above is not available for this benchmark (my reading).
- A second temporal instance is a hand-object video task: the model must say the frame where an object becomes attached to or detached from a hand. Naming the action and the objects scores high, while the frame is missed. The paper's summary is that "where semantic success masks a failure in physical grounding", and exact-frame accuracy stays "about chance level (10%)" for ten-frame clips.[^c14][^c15] Only the answer and the frame scores are reported side by side, not crossed per item. The event itself is described in [[contact-release-event]].
- A judge-based variant comes from CodeV, on V* visual search. Here a crop is not scored against a box. A judge model is shown the question and the crop and asked whether the crop includes the queried object or region. The rate is taken over tool calls "conditioned on the final answer being correct", and a run counts as faithful "if any crop is judged to contain the target".[^c16] On this measure "only about half of the intermediate tool" calls were faithful: 57% for DeepEyes and 43% for Pixel-Reasoner.[^c17] The authors read this as the same gap: "models can often guess the correct answer from text" cues.[^c18] This is a judge's verdict on the crop, not a box overlap, so the four-quadrant split is not available for it.

The authors conclude that accuracy-only benchmarks overestimate model reliability.[^c9] That is their reading of a prevalent ungrounded-correct pattern, not an independently tested claim about overestimation size.

## Limits

- Grounding is operationalized as crop overlap with one annotated box. A model might use evidence it never cropped, such as from the global view, or crop correctly yet answer from priors. The quadrants are therefore proxies for evidence use, not proofs of it. This is my inference, not tested in the paper.
- The 0.5 threshold and the max-of-two-directions rule are design choices. No sensitivity analysis was read.
- The benchmark has 200 images across four scenarios and a small set of models, so per-model percentages are noisy.
- It applies to settings where evidence has a spatial location and the model emits inspectable operations. Transfer to text-only question answering is not established. For retrieval, the analogue would be gold-passage overlap crossed with answer correctness, which is only my analogy.

## Related

- [[dependence-versus-utility-dissociation]] — detecting that evidence was used differs from showing it was needed; same gap between use and correctness
- [[calibrated-accuracy]] — another correction to accuracy as the sole outcome measure
- [[evidence-ablation-four-scenario-deflection-protocol]] — a four-cell design that likewise separates answers by evidence condition
- [[object-grounded-trace-scoring]] — mask-matched trace scores (LQ, VQ) kept apart from answer mIoU in a segmentation setting

[^c1]: arxiv-2601-11633 — "we enforce extreme"
[^c2]: arxiv-2601-11633 — "IoA = max(IoA(Bpred , Bgt ), IoA(Bgt , Bpred "
[^c3]: arxiv-2601-11633 — "This is the primary metric"
[^c4]: arxiv-2601-11633 — "indicating a reliance on"
[^c5]: arxiv-2601-11633 — "proves failure stems not from blind search, but from"
[^c6]: arxiv-2601-11633 — "its G− · A+ rate"
[^c7]: arxiv-2601-11633 — "proving its success derives from"
[^c8]: arxiv-2601-11633 — "Localization is a necessary but"
[^c9]: arxiv-2601-11633 — "suggesting that current benchmarks significantly"
[^c10]: arxiv-2512-05091 — "they completely fail to generate valid reasoning outputs (scoring zero on R-LQ and R-VQ)"
[^c11]: arxiv-2512-05091 — "despite the lack of improvement in intermediate visual grounding, the final Answer performance (A) increases significantly"
[^c12]: arxiv-2512-03479 — "models produce plausible answers while failing to localize the supporting evidence"
[^c13]: arxiv-2512-03479 — "discrepancy between answering plausibility and grounding precision"
[^c14]: arxiv-2511-20162 — "where semantic success masks a failure in physical grounding"
[^c15]: arxiv-2511-20162 — "the models’ accuracy is about chance level (10%) for detecting the exact frame where the event occurs"
[^c16]: arxiv-2511-19661 — "conditioned on the final answer being correct"
[^c17]: arxiv-2511-19661 — "for DeepEyes and 43% for Pixel-Reasoner"
[^c18]: arxiv-2511-19661 — "models can often guess the correct answer from text"
