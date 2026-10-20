---
description: "Vision-language models trained mostly on anatomical images can fail to read PET tracer intensity; zero-shot accuracy drops on functional tasks while structural benchmarks stay high."
aliases: ["PET perception gap", "anatomical-prior dependence in functional imaging"]
sources: ["arxiv-2601-02737"]
---
# Functional perception gap

A vision encoder can read anatomy and still fail to read function. In PET the diagnostic signal is the intensity of a radiotracer's biodistribution: voxel magnitude tracks metabolic or molecular activity, so pathology is defined by uptake relative to a physiological background.[^c1] Encoders trained on natural images and on structural medical data are tuned to a different signal. Their high-frequency features carry the semantics there, while "absolute intensity variations are often treated as illumination noise to be normalized."[^c2]

The authors define the gap as a feature-extraction failure rather than a domain shift: "not merely as a domain shift, but as a feature extraction failure."[^c3] Read as a formula, two regions with the same morphology and different uptake should map to nearly the same representation, so the decoder describes them identically from the anatomical prior. That reading is the paper's; the paper gives no direct measurement of the encoder's representations.

The measured symptom is a cross-task drop. Across 19 MLLMs evaluated zero-shot on a five-level PET hierarchy, medical models did worse than general ones on diagnosis: "While GPT-4o achieves a diagnostic accuracy of 54.78%, Lingshu-7B and MedGemma-27B reach only 21.23% and 28.03%, respectively."[^c4] Image quality assessment was uniformly poor, "with a mean accuracy of 15.44% across all models."[^c5] Tracer identification, which relies on global biodistribution, was easier, at "solvable (mean of 62.93%)."[^c6] Organ recognition could be good while diagnosis failed: "Lingshu-7B achieves competitive organ recognition (70.14%) but fails at diagnosis."[^c7] The authors read this as the model localizing uptake without a framework for its pathological meaning. Their explanation for the whole pattern is that "the features learned from structural imaging appear orthogonal to the requirements of functional interpretation."[^c8]

The benchmark design separates this from a confound. Fused PET/CT inputs let a model "extract morphological features from the high-resolution CT component while ignoring the lower-resolution, metabolic and molecular PET signal."[^c9] PET-Bench therefore uses SUV-normalized pure PET volumes "without PET/CT overlays."[^c10] With the confound removed, a model that scores well on CT or MRI benchmarks can still score poorly on the function, which is what the gap names.

What the gap does to asking and answering: an answer about a lesion can rest on the anatomical prior rather than on the uptake. The paper's account of the deficit is that anatomical conditioning makes models lose the capacity to represent tracer biodistribution and voxel intensity apart from morphology.[^c11] (My inference, not measured in the paper: the same failure applies to any signal whose meaning depends on an intensity scale the encoder was never tuned to. [[prerequisite-gated-decodability]] states the general form: a signal carries information only if the perception it needs has been acquired.)

## Limits

- The gap is inferred from comparisons across models trained on different data. The paper's own wording is a hypothesis: "This structural bias motivates our hypothesis of a functional perception gap."[^c12] No ablation in the read text isolates the encoder from the data mix, the model size or the prompt.
- The model input is not the volume: "we define the model input x not as a raw volume, but as a sequence" of 2D slices or projections.[^c13] A part of the drop may come from which views are chosen. That was not tested here.
- The probe is multiple-choice with a label-only answer in the zero-shot setting. Other output formats are not in the read text.
- One modality (PET), a few tracers (FDG, PSMA, FAPI), eight centers. The paper suggests the template applies to "PET, SPECT, and other functional modalities,"[^c14] but SPECT and other modalities are not tested.
- The gap is a zero-shot finding. Whether it persists after fine-tuning is a separate question; the paper reports fine-tuning results that I did not read in full, so this note makes no claim about them.

## Related

- [[cot-hallucination-trap]] — what standard chain-of-thought does when this gap is present
- [[text-modality-dominance]] — a different reliance result: a model weights text over equally informative vision, measured by corruption
- [[prerequisite-gated-decodability]] — a signal is usable only once its prerequisite perception is acquired
- [[perception-influence-gap]] — shares the word "gap", but there the gap is between what an AI perceives and what it influences

[^c1]: arxiv-2601-02737 — "PET semantics are intrinsically defined by the low-frequency biodistribution of tracer intensity"
[^c2]: arxiv-2601-02737 — "absolute intensity variations are often treated as illumination noise to be normalized"
[^c3]: arxiv-2601-02737 — "not merely as a domain shift, but as a feature extraction failure"
[^c4]: arxiv-2601-02737 — "While GPT-4o achieves a diagnostic accuracy of 54.78%, Lingshu-7B and MedGemma-27B reach only 21.23% and 28.03%, respectively"
[^c5]: arxiv-2601-02737 — "with a mean accuracy of 15.44% across all models"
[^c6]: arxiv-2601-02737 — "solvable (mean of 62.93%) due to distinct global biodistribution patterns"
[^c7]: arxiv-2601-02737 — "Lingshu-7B achieves competitive organ recognition (70.14%) but fails at diagnosis"
[^c8]: arxiv-2601-02737 — "The features learned from structural imaging appear orthogonal to the requirements of functional interpretation"
[^c9]: arxiv-2601-02737 — "extract morphological features from the high-resolution CT component while ignoring the lower-resolution, metabolic and molecular PET signal"
[^c10]: arxiv-2601-02737 — "without PET/CT overlays"
[^c11]: arxiv-2601-02737 — "a fundamental deficit where MLLMs, conditioned heavily on anatomical features, lose the capability to represent tracer biodistribution and voxel intensity independent of morphological priors"
[^c12]: arxiv-2601-02737 — "This structural bias motivates our hypothesis of a functional perception gap"
[^c13]: arxiv-2601-02737 — "we define the model input x not as a raw volume, but as a sequence"
[^c14]: arxiv-2601-02737 — "PET, SPECT, and other functional modalities"
