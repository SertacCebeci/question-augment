---
description: "A small probe on a vision-language model's hidden states after it answers predicts when the answer is wrong, beating output-probability and self-report abstention baselines on scene-text VQA."
aliases: ["latent representation probing (LRP)", "hidden-state abstention probe", "post-answer internal confidence probe", "OCR abstention probe"]
sources: ["arxiv-2511-19806"]
---
# Latent representation abstention probe

A vision-language model (VLM) answers a question, and its internal states may already carry a judgement of whether that answer is right. A latent representation abstention probe reads that judgement. It is a small classifier trained on the hidden states of the answer's output tokens, or on attention patterns, to predict whether the answer is correct. The model abstains when the predicted confidence is low.[^c1] The setting is scene-text VQA, where one misread number is the failure that matters: "OCR errors like misreading “50 mph” as “60 mph” could cause severe traffic accidents."[^c2]

The argument for reading inside the model rests on a claim about its outputs: "output logits in VLMs are often severely miscalibrated."[^c3] The authors hypothesise that the failure of those output signals does not show absence of knowledge; "uncertainty signals could be hidden in VLMs’ internal representations."[^c4] The probe is the test of that hypothesis.

## Mechanism

For a given answer, the hidden states are read at each layer. "we average the hidden states of all output tokens at each layer."[^c5] A probe per layer, or one probe over all layers concatenated, gives a score from one forward pass, which the paper contrasts with the repeated generations that response-level methods need.[^c6]

The training target is graded, not yes-or-no. The probes are "trained using binary cross-entropy loss with soft labels," because OCR correctness is continuous.[^c7] The paper compares three designs. One is an MLP over all layers concatenated. The second averages attention over visual tokens. The third is an ensemble: one MLP per layer, the layers with the highest validation abstention accuracy are kept, and their thresholded verdicts are majority-voted, with "we set K = 5."[^c8] The ensemble over hidden states is the strongest of the designs: "ensemble hidden state probing achieves the best performance."[^c9]

The paper's reading of the difference between the two representations is that "hidden states encode richer semantic uncertainty signals than attention patterns."[^c10] Averaged over four benchmarks, the reported result is that "LRP improves abstention accuracy by 7.6% over best baselines."[^c11] The baselines are token probability, a VLM judge, R-tuning, a visual-attention ratio, Contextual Lens and a prompt-to-abstain instruction. The last one fails in a different direction from the others: "prompt-to-abstain exhibits severe underabstention with extremely high abstention precision."[^c12]

The paper scores a decision, not a confidence. Abstention accuracy counts "abstaining on incorrect answers and answering on correct answers."[^c13] This is a per-item agreement between the abstain decision and correctness, so it penalises both kinds of error, unlike a risk at a fixed coverage.

## Generalisation

On synthetic low-confidence sets built by the authors, probes trained on the main data reach "an average abstention accuracy of 0.825," which the paper reads as learning "general uncertainty representations."[^c14] Across datasets the ranking changes. The paper reports that "attention pattern probes achieve substantially stronger out-of-distribution performance" than the training-based baselines.[^c15] So the readout that is best in-distribution is not the one that transfers best.

## Depth

The signal is strongest in the middle of the network: "optimal confidence signals emerge in intermediate layers rather than final layers."[^c16] This matches the account in [[abstention]] of a score that must be estimated separately from the predictor, and it sits next to the depth-combination rule in [[cross-layer-probe-ensemble]].

The probe adds no generation. The paper's claim is "requiring only a single forward pass."[^c17] That makes it cheap in a deployed system, but only for a model whose hidden states can be read.

## Limits

- Labelled correctness is needed for every training question. The probe is supervised, so its score is only as good as the correctness judgement behind its soft labels. The parts of the paper read do not say in detail how the continuous OCR label is produced (my reading).
- Abstention accuracy is one number over two kinds of error. The paper itself notes that a high figure on either component "usually indicates over-abstention or under-abstention," which is why it reports the components beside the average.[^c18]
- The depth profile is task-dependent. Abstention accuracy "exhibits a clear rise-then-fall trend" on three datasets, but on OCRBench v2 "accuracy remains consistently high across most layers after initial rise."[^c19][^c20] The paper attributes the flat profile to training-data diversity. The middle-layer peak is therefore a property of the task and model, not a fixed depth (my inference from the figure text).
- The best readout in-distribution and the best readout across datasets differ. A deployer must guess which shift to expect, and the paper gives no rule for choosing.
- The video result is partly a comparison with baselines that break. The paper says they "fail due to their inability to handle long sequences effectively."[^c21] The gap on video is real in the paper's table, but it is not a measure of the probe's quality on video alone.
- Not tested in the parts read: whether the abstentions improve final accuracy when the system can retry or call a tool; whether the probe transfers to answers that come from a long reasoning trace rather than a short OCR answer; and whether the depth result holds beyond the two VLMs its layer analysis uses (my reading of that section).

## Related

- [[abstention]] — the reject option; this probe is one estimate of its uncertainty score, learned from labelled correctness
- [[cross-layer-probe-ensemble]] — the depth-combination rule; this paper's top-K majority vote is a second rule over the same layers
- [[pre-generation-success-probe]] — the same kind of readout taken before the answer is written; here it is taken from the answer's own tokens
- [[in-trajectory-answer-probing]] — probes answer quality by forcing an answer mid-trajectory; this probe needs no forced answer, only the answer already produced
- [[calibration]] — the output-probability route that the paper argues is miscalibrated in VLMs

[^c1]: arxiv-2511-19806 — "training lightweight probes on hidden states or attention patterns"
[^c2]: arxiv-2511-19806 — "OCR errors like misreading “50 mph” as “60 mph” could cause severe traffic accidents"
[^c3]: arxiv-2511-19806 — "output logits in VLMs are often severely miscalibrated"
[^c4]: arxiv-2511-19806 — "uncertainty signals could be hidden in VLMs’ internal representations"
[^c5]: arxiv-2511-19806 — "we average the hidden states of all output tokens at each layer"
[^c6]: arxiv-2511-19806 — "requiring only a single forward pass"
[^c7]: arxiv-2511-19806 — "The probes are trained using binary cross-entropy loss with soft labels"
[^c8]: arxiv-2511-19806 — "In our experiments, we set K = 5"
[^c9]: arxiv-2511-19806 — "ensemble hidden state probing achieves the best performance"
[^c10]: arxiv-2511-19806 — "hidden states encode richer semantic uncertainty signals than attention patterns"
[^c11]: arxiv-2511-19806 — "LRP improves abstention accuracy by 7.6% over best baselines"
[^c12]: arxiv-2511-19806 — "prompt-to-abstain exhibits severe underabstention with extremely high abstention precision"
[^c13]: arxiv-2511-19806 — "abstaining on incorrect answers and answering on correct answers"
[^c14]: arxiv-2511-19806 — "The average abstention accuracy of 0.825 suggests they learn general uncertainty representations"
[^c15]: arxiv-2511-19806 — "attention pattern probes achieve substantially stronger out-ofdistribution performance"
[^c16]: arxiv-2511-19806 — "optimal confidence signals emerge in intermediate layers rather than final layers"
[^c17]: arxiv-2511-19806 — "while requiring only a single forward pass"
[^c18]: arxiv-2511-19806 — "usually indicates over-abstention or under-abstention"
[^c19]: arxiv-2511-19806 — "exhibits a clear rise-then-fall trend"
[^c20]: arxiv-2511-19806 — "accuracy remains consistently high across most layers after initial rise"
[^c21]: arxiv-2511-19806 — "fail due to their inability to handle long sequences effectively"
