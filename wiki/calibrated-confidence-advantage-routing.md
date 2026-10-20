---
description: "Calibrating two models on held-out data makes their confidences comparable; the per-bin gap (confidence advantage) then routes each query to the small or large model, training-free."
aliases: ["confidence advantage routing", "calibrated cascade", "calibrated advantage routing"]
sources: ["arxiv-2601-07965"]
---
# Calibrated confidence advantage routing

**Premise.** Raw model confidence is ordered correctly within one model but is not on a common scale across models. The paper states two observations: confidence from logit likelihoods is roughly monotone with accuracy even uncalibrated, and "Calibration trained on the validation set generalizes to the test set."[^c1] Calibration is a few parameters (temperature for vision, a Platt sigmoid on mean token logit for language) fitted by negative log-likelihood against a verifier's 0/1 judgment on a held-out split. Because it does not reorder samples, the monotone relation is what lets it work.[^c2] After calibration, confidences of different models "become comparable".[^c3]

**The routing signal.** Bin the small model's calibrated confidence by histogram equalization. In each bin i, the confidence advantage of the large model is the difference of mean calibrated confidences, a_i = mean c_large − mean c_small, estimated on validation data. Since calibration generalizes, a new input falling in bin i is expected to enjoy about a_i extra confidence under the large model.[^c4]

**The rule.** Sort bins by ascending advantage and keep the K bins where the large model helps least. At inference, run the small model; if its confidence falls in one of those K bins, keep its answer, else call the large model. K sets the accuracy–cost trade-off.[^c5] No router is trained, and the only fitted objects are the calibrators.

**What was measured.** On ImageNet-1K the small model was already well calibrated, so raw-confidence routing and calibrated routing performed alike, and both beat random picking at equal small-model share.[^c6] With LLaMA-8B and LLaMA-70B across MBPP, BigCodeBench, MMLU, GSM8K and ARC-Challenge, calibrated routing beat a matrix-factorization router (RouteLLM) and random picking, and beat uncalibrated confidence routing across the whole trade-off curve.[^c7] So calibration earns its keep where the raw confidences are poorly scaled.

**Same-size pairs.** The same signal lets two comparable models specialise. Two ~82% ImageNet models (DeiT-B, TinyViT) reached peak cascade accuracy up to 90%, and Qwen-32B with LLaMA-70B gained on MMLU.[^c8] The paper's reading is that the models complement each other on the data where each is better. A caution is mine: the 90% peak is at some operating point, and part of such gains may come from label noise in the benchmark, which the same paper shows is present.

**Why it matters for asking and answering.** Whether to answer yourself or defer is a question about relative competence on this input, and it is answerable only if self-reports are mapped to empirical accuracy first. The difference of calibrated confidences is that relative estimate.

## Limits

- Tested on classification-like or pass/fail tasks with a verifier available for calibration; open-ended answers without a verifier are not covered.
- Calibration is shown to carry over only in-distribution; the paper's claim is "reliable on in-distribution new data", and shift was not tested here.
- Advantage is a bin average, so it says nothing about a specific input where the large model is unusually better or worse (my inference).
- Costs are expressed as the small-model share, not measured latency or money.
- Comparisons against RouteLLM use one router configuration.

## Related

- [[temperature-scaled-deferral-gate]] — same temperature-fit step, but gating to a human on a single model's confidence
- [[sequence-likelihood-confidence]] — the token-likelihood confidence used for language models
- [[confidence-calibrated-cascade-judgment]] — another confidence-gated cascade
- [[differentiable-cascade-threshold-learning]] — learns cascade thresholds rather than deriving them from calibrated gaps

[^c1]: arxiv-2601-07965 — "Calibration trained on the validation set generalizes to the test set."
[^c2]: arxiv-2601-07965 — "The calibration methods described above do not alter the confidence ranking of"
[^c3]: arxiv-2601-07965 — "calibrated confidences across different models become comparable"
[^c4]: arxiv-2601-07965 — "its expected advantage under the large model will also be close to aci"
[^c5]: arxiv-2601-07965 — "where K is a hyperparameter balancing accuracy"
[^c6]: arxiv-2601-07965 — "Because the small model on"
[^c7]: arxiv-2601-07965 — "CC consistently outperforms UC across the entire accuracy–small-model-ratio trade-off"
[^c8]: arxiv-2601-07965 — "the combined system reaches an astonishing peak accuracy of up to 90%."
