---
description: "A linear probe on a judge's middle-layer hidden state, fit with a Brier loss to whether its verdict is right, gives calibrated confidence with no extra training or sampling."
aliases: ["Brier-trained linear probe", "probe-based judge calibration", "interpretability-based uncertainty estimate", "hidden-state calibration probe"]
sources: ["arxiv-2512-22245"]
---
# Brier-trained calibration probe

An LLM judge that writes reasoning and then a verdict leaves a state at the last token that carries some information about whether the verdict will be right. The calibration probe reads that state. It is a linear regression on the judge's residual-stream activation, with verdict accuracy as the label, and its fit is scored by the Brier score rather than by a ranking or a likelihood.[^c1] The authors "optimize the Brier score" and choose the layer on validation performance; the output is then read as the predicted probability that the verdict is correct.[^c2][^c3]

Before the verdict, the judge is prompted to "verbally express its uncertainty before its verdict", so the probe reads a state that already holds linguistic hedging as well as whatever the hidden layers encode.[^c4] The probe is not trained into the judge: the judge's weights are untouched, and nothing is sampled at inference. That is the whole mechanism. What it buys is a number per verdict, computed from one forward pass.

## What was measured

On the Preference Proxy Evaluation datasets, the probe is compared with three baselines: verbalized confidence, self-consistency over N samples, and majority vote. The authors report that "our probes consistently achieve the best calibration, with the lowest Kuiper/ECE scores on both PPE Correctness" tasks, with the same pattern on preference tasks in most cells.[^c5] The layer and loss matter. An ablation over binary cross-entropy, focal loss and the Brier loss finds that "loss at the middle layer of models yields the most" calibrated probes.[^c6] The compute claim is an order of magnitude: the probe is said to need "an order of magnitude less compute" than the multi-generation baselines.[^c7] Those baselines were tuned at "N = 10, temperature = 0.7", so the saving is against that setting.[^c8]

Memory is the other half of the cost argument. Some single-pass selective-classification methods store hidden states for every token, while "our probes only require" a vector per layer.[^c9] Multi-generation methods are described as incurring "substantial computational costs".[^c10]

My inference, not the paper's finding: a regression fit to the 0/1 outcome with the Brier loss targets the conditional probability of correctness given the state, which is why it can be calibrated where a verbal number is not. The paper argues the same from its results ("probes are designed to temper overconfidence"), not from a derivation.[^c11]

## Where it sits

The readout family is the one in [[pre-generation-success-probe]], which predicts a model's own success from activations before it generates. The calibration probe differs in two ways: it reads the state after reasoning and after a stated uncertainty, and its target is the correctness of a judgment the model has already made. The property it aims at is the one in [[calibration]]. The paper's main score for that property is the [[kuiper-statistic]].

## Limits

- **Needs ground truth per judge.** The method requires "a labeled dataset with ground truth verdicts", and the authors say it does not work where such verdicts are unavailable.[^c12]
- **Needs white-box access to middle layers.** An API-only judge cannot be probed this way.
- **One probe per judge.** "we train one probe for each judge model, but" the probe must be refit "if the judge is retrained or finetuned, the probe may" be stale.[^c13][^c14]
- **Conservative on easy data.** The authors say "probes produce conservative estimates that underperform on easier datasets".[^c15] On RewardBench, "on RewardBench, probe performance lags behind" verbalized confidence for several models. The explanation given is that "higher overall accuracy across models, leading verbalized confidence" to look good, because verbalized confidence overestimates certainty and easy sets reward that.[^c16][^c17]
- **Out-of-distribution gains are mixed.** The probe wins on JudgeBench across model families, but the RewardBench lag shows that a win on one shifted set does not transfer to every shift.
- **Verdict correctness only.** The labels are whether the winning response is ranked higher, so the paper measures calibration of verdicts, not of open-ended answers; "correctness is verified by checking if the winning response is ranked higher".[^c18]
- **Mechanism unexamined.** The authors note "more investigation into interpreting which features are learned by the probes" is future work, so what the probe reads is not established.[^c19]

## Related

- [[calibration]] — the property this probe is fit to; the Brier score there mixes calibration with resolution.
- [[pre-generation-success-probe]] — the same kind of linear readout, applied before generation to predict success.
- [[kuiper-statistic]] — the calibration metric the paper treats as primary.
- [[free-form-brier-score]] — the Brier rule used as a scoring rule for free-form answers, not as a probe loss.
- [[savor-calibration-abstention-reward]] — a Brier term used as a training reward, where this note's probe is fit after the fact and leaves the model unchanged.
- [[reasoning-contamination-of-verbalized-confidence]] — a neighbouring finding that reasoning degrades verbalized confidence; the probe here is applied to reasoning judges, and that interaction is not tested in this paper.

[^c1]: arxiv-2512-22245 — "with a Brier score-based loss to provide calibrated uncertainty estimates from reasoning"
[^c2]: arxiv-2512-22245 — "from the last token, with verdict accuracy as the"
[^c3]: arxiv-2512-22245 — "we optimize the Brier score"
[^c4]: arxiv-2512-22245 — "verbally express its uncertainty before its verdict"
[^c5]: arxiv-2512-22245 — "Our probes consistently achieve the best calibration, with the lowest Kuiper/ECE scores on both PPE Correctness"
[^c6]: arxiv-2512-22245 — "loss at the middle layer of models yields the most"
[^c7]: arxiv-2512-22245 — "an order of magnitude less compute"
[^c8]: arxiv-2512-22245 — "with optimal results at N = 10, temperature = 0.7"
[^c9]: arxiv-2512-22245 — "our probes only require"
[^c10]: arxiv-2512-22245 — "they incur substantial computational costs"
[^c11]: arxiv-2512-22245 — "probes are designed to temper overconfidence"
[^c12]: arxiv-2512-22245 — "and a labeled dataset with ground truth verdicts"
[^c13]: arxiv-2512-22245 — "we train one probe for each judge model, but"
[^c14]: arxiv-2512-22245 — "if the judge is retrained or finetuned, the probe may"
[^c15]: arxiv-2512-22245 — "probes produce conservative estimates that underperform on easier datasets"
[^c16]: arxiv-2512-22245 — "on RewardBench, probe performance lags behind"
[^c17]: arxiv-2512-22245 — "higher overall accuracy across models, leading verbalized confidence"
[^c18]: arxiv-2512-22245 — "correctness is verified by checking if the winning response is ranked higher"
[^c19]: arxiv-2512-22245 — "interpreting which features are learned by the probes"
