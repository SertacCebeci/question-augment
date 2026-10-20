---
description: "Adding random noise to numeric input before tokenization, then taking the median over draws, is reported to steady a frozen LLM's forecasts, with gains at a moderate noise level."
aliases: ["input noise injection at inference", "noise augmentation at inference", "test-time noise injection", "NLTS noise injection"]
sources: ["arxiv-2512-20140"]
---
# Inference-time input noise injection

A frozen language model that forecasts a numeric series by reading it as text is brittle: the forecast "is acutely sensitive to the textual representation of the input".[^c1] Noise injection is a way to act on that sensitivity without touching the model. Before the series is turned into tokens, each value is perturbed by a random term whose size is set by the series' own spread: x̃ = x + αε, with the noise variance written as α²σ_x², where σ_x² is the variance of the original series and α "is the scaling factor that governs the noise magnitude relative to the original".[^c2] The perturbed series is tokenized in the usual way and given to the frozen model. The procedure is repeated over several noisy instances, and the forecast is the median of the draws, with the spread across draws read as a measure of reliability.[^c3] No gradient is computed and no weight changes.

The authors' argument for why this should help is an augmentation argument carried into inference. Their Lemma 1 expands the model output to second order in the input. Averaging over Gaussian ε adds a term proportional to α²σ² times the trace of the input-space Hessian, and the lemma is that this term is non-positive for a model they call well-trained, so the noisy expected error does not exceed the clean one.[^c4] The non-positivity is derived from a condition on the parameter-space Hessian: the input-space Hessian "relates to the parameter-space Hessian via" a chain-rule product.[^c5]

The noise level matters, and the effect is not monotone. The authors report that "particularly those in the range of 0.005 to 0.02, consistently" give the more stable results, and call the band a sweet spot, where regularization helps before distortion dominates.[^c6] For some models the gain is large, "with relative improvements of 62.97%" for one model at the smallest noise level.[^c7] Others "present more variability, with fluctuations in performance depending on the noise".[^c8] The abstract summarizes the outcome as having "consistently observe[d] improved performance" across benchmarks.[^c9] The authors also build two datasets outside the pre-training scope of the models, "to fully eliminate potential biases from data contamination during LLM pre-training".[^c10]

Transfer. What survives outside time series is the design choice of aggregating over several perturbed views of one input with a median, and reading their spread as uncertainty; the same move appears in [[pseudo-ensemble]]. What does not obviously survive is the Hessian argument, which is a local, small-noise, training-likelihood statement, and the noise here changes values rather than surface form, so it is not a question-wording transformation. A question's answer is not held fixed by construction, which is the property that makes the pseudo-ensemble readable as an ensemble.

## Limits

- The lemma is local. The expansion is in α with an o(α²) remainder, so it speaks to small noise. The useful band reported (0.005 to 0.02) is not shown to lie inside the regime where that remainder is negligible; the authors do not check this (my inference).[^c11]
- The Hessian in the argument is the Hessian of the training log-likelihood, L̂(Θ), while the lemma needs the Hessian of the model's output. The bridge between them is stated in one line and not derived in the sections read. Negative definiteness is assumed over training data, not at the test inputs where forecasts are made (my inference).
- The lemma bounds an expectation over ε at a fixed x. It says nothing about the median over draws that the method actually reports; the benefit of the median is shown only by experiment.
- Results vary by model and noise level: the authors say the "extent and consistency of these gains vary by model".[^c12] The sweet-spot reading comes from five datasets in one figure, and the per-model tables cover nine LLMs on one dataset.[^c13]
- The variance across draws is offered as an uncertainty measure. Whether it tracks forecast error is not tested in the sections read (my inference).
- The result concerns numeric forecasting with off-the-shelf models. Nothing here establishes the transfer to question answering, where a perturbation that changes an answer would not be neutral.

## Related

- [[pseudo-ensemble]] — answer-preserving views of one input stand in for ensemble members; noise injection changes the numbers rather than the surface form, and does not keep the answer fixed by design.
- [[prompt-variant-augmentation]] — the training-time counterpart: varying wording during fine-tuning, where this note varies values at inference.
- [[medium-context-sweet-spot-for-numeric-prediction]] — another interior optimum in numeric prediction, here over the amount of context rather than the noise scale.

[^c1]: arxiv-2512-20140 — "is acutely sensitive to the textual representation of the input"
[^c2]: arxiv-2512-20140 — "is the variance of the original TS, and α is the scaling factor that governs the noise magnitude relative to the original"
[^c3]: arxiv-2512-20140 — "compute the median and variance across these samples"
[^c4]: arxiv-2512-20140 — "can be reduced by noise injection on the input for zeroshot forecasting"
[^c5]: arxiv-2512-20140 — "Hessian relates to the parameter-space Hessian via"
[^c6]: arxiv-2512-20140 — "particularly those in the range of 0.005 to 0.02, consistently"
[^c7]: arxiv-2512-20140 — "with relative improvements of 62.97%"
[^c8]: arxiv-2512-20140 — "present more variability, with fluctuations in performance depending on the noise"
[^c9]: arxiv-2512-20140 — "consistently observe improved performance"
[^c10]: arxiv-2512-20140 — "fully eliminate potential biases from data contamination during LLM pre-training"
[^c11]: arxiv-2512-20140 — "where α scales the noise magnitude"
[^c12]: arxiv-2512-20140 — "the extent and consistency of these gains vary"
[^c13]: arxiv-2512-20140 — "report the performance of nine different LLMs"
