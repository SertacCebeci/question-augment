---
description: "MLLM confidence stays flat as the image degrades; a reward on the confidence gap between original and noised images plus an accuracy-signed confidence term retrains it to track perception."
aliases: ["confidence-driven RL from vision", "CDRL", "perception-confidence alignment"]
sources: ["arxiv-2603-12149"]
---
# Perception-sensitive confidence reward

**The failure.** In a probing experiment, noise is progressively added to the key visual evidence of an image. A model that relies on what it sees should lose both accuracy and confidence. Instead, mean confidence stays nearly constant while accuracy falls sharply, so self-reported certainty and performance disconnect.[^c1] The authors call this confidence miscalibration under perception degradation.[^c2]

**Confidence as a whole-response quantity.** Token-level uncertainty methods from text LLMs are said to mismatch visual perception, which shows up across the entire response. Confidence is therefore the mean negative log-probability over all output tokens.[^c3] Each token's score is averaged over the top-k log-probabilities, and a lower value means a sharper distribution and higher certainty.[^c4]

**The reward.** Training uses GRPO on pairs of an original image and a noised copy. CLIP attention maps place the noise on the informative regions. The total reward adds accuracy, format and a confidence term.[^c5] The confidence term has two parts. The perception part is alpha·tanh(beta·ΔC), where ΔC is the confidence difference between the original-image and noised-image outputs, so it rewards a large confidence change. The calibration part is (2·accuracy − 1)·normalized confidence. It adds confidence when the answer is correct and subtracts it when wrong.[^c6] The calibration term uses only the original-image output, so the perturbed trajectory does not contaminate the gradient.[^c7]

**What was measured.** On Math-Vision with Qwen2.5-VL-7B, the confidence drop under perturbation was small for the base model (some conditions even rose, for example +0.09 under a viewpoint change) and large after training (−0.86 to −1.39). ECE improved in every condition.[^c8] The authors say the model learns to reduce confidence when visual evidence is insufficient.[^c9] The calibrated confidence was then reused as a weight in majority voting and as a trigger for extra reasoning, which they call a free lunch of calibration.[^c10]

**Why it matters for asking and answering.** A system that asks for or reports confidence needs that confidence to move when the evidence is removed. A counterfactual-input check (same question, degraded evidence) is a way to test this. That use is my inference. The paper trains one model family and tests no other method of restoring sensitivity.

## Limits

- One base model (Qwen2.5-VL-7B), a small filtered training set of 1936 items, and perception-heavy math and VQA benchmarks. Transfer to other models or to text-only questions is not tested here.
- Noise on the attended region is one kind of degradation. Occlusion, viewpoint and mosaic were evaluated, but confidence on irrelevant-region noise was not examined.
- The reward bundles a perception term and a calibration term. I did not locate an ablation separating their effects, so which term drives the ECE gain is unestablished here.
- Table 4 values were read from a flattened extract, so the column pairing is my reading.

## Related

- [[calibration]] — the general property this reward trains in a visual setting
- [[visual-evidence-scoring]] — scoring how strongly visual evidence supports an answer
- [[text-modality-dominance]] — models under-use non-text evidence, a plausible cause of flat confidence (my inference)
- [[confidently-wrong-low-entropy-regime]] — another case of high confidence with wrong answers

[^c1]: arxiv-2603-12149 — "confidence remains surprisingly stable despite severe perception degradation"
[^c2]: arxiv-2603-12149 — "MLLMs suffer from severe confidence miscalibration, which maintaining high confidence"
[^c3]: arxiv-2603-12149 — "we calculate the confidence for entire response as the mean negative log-probability across all output tokens"
[^c4]: arxiv-2603-12149 — "A lower NMLP value indicates a sharper probability distribution, signifying higher certainty."
[^c5]: arxiv-2603-12149 — "rj = RConf,j + ROutput,j + RFormat,j"
[^c6]: arxiv-2603-12149 — "This combined"
[^c7]: arxiv-2603-12149 — "To avoid contaminating the training trajectory, the"
[^c8]: arxiv-2603-12149 — "CDRL improves calibration metrics"
[^c9]: arxiv-2603-12149 — "reduce confidence when visual"
[^c10]: arxiv-2603-12149 — "A free lunch for this confidence calibration is its direct applicability to test-time scaling"
