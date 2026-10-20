---
description: "Some LLM hallucinations get near-zero entropy, so entropy scores cannot rank them; a supervised correctness probe separates them and lowers the risk floor of selective prediction."
aliases: ["confidently wrong regime", "low-entropy hallucination", "entropy risk floor"]
sources: ["arxiv-2603-21172", "arxiv-2512-04748"]
---
# Confidently wrong low-entropy regime

An entropy-based uncertainty score (sequence NLL, [[semantic-entropy]], or a semantic entropy probe) ranks questions by how dispersed the model's outputs are. It fails where a model gives the same wrong answer every time: the output distribution lacks diversity, so the hallucination receives the same near-zero score as a correct answer. The paper names this the "confidently wrong regime" and finds it model-dependent.[^c1]

## What was observed

For Qwen on TriviaQA, a substantial fraction of questions get near-zero semantic entropy, which collapses them onto a vertical line in the score plane. That cluster holds both correct answers and hallucinations.[^c2] A probability-of-correctness (PC) probe is a logistic regression on prompt representations trained with external correctness labels. It does not collapse in this way: questions with identical zero SE are spread across a range of probe logits, and hallucinations often receive elevated risk.[^c3]

Which signal wins depends on the model. On TriviaQA, SE is the stronger detector for Llama and Ministral and the PC probe dominates for Qwen. The two risk scores correlate only moderately (Spearman about 0.34 to 0.54), so they carry different information.[^c4]

## Consequence for selective prediction

A selective predictor answers only when a risk score is below a threshold tuned on held-out data to meet a target hallucination rate. When the confident errors cannot be ranked, the risk-coverage curve has a floor. For Ministral 8B on BioASQ, entropy methods fail to enter the high-trust regime (risk at most 0.15) at non-trivial coverage.[^c5] The realized hallucination rate then stays well above a strict target after the threshold is tuned. Methods that include the PC probe lower this floor and track the calibration diagonal more closely.[^c6]

The fix is a two-feature logistic regression over the entropy risk and the probe risk. It adds no inference beyond one forward pass of the LLM. Across three QA benchmarks and four model families the combination generally improves E-AURC and Target Calibration Error (TCE) over the entropy baselines. The paper reports it usually beats the standalone probe too.[^c7]

## Why the metric matters

TCE averages |realized risk − target risk| over target risks from 0.05 to 0.30 and is used instead of ECE because the goal is risk control at specific operating points. The authors argue that strong AUROC does not imply reliable operation at strict safety thresholds, so global detection metrics can hide this failure.[^c8]

## Limits

- Only short-form QA judged against reference strings; whether the failure mode or the complementarity carries over to long-form, reasoning or open-ended tasks is unclear.[^c9]
- Only 3B to 8B models. Larger models may fail differently.[^c9]
- The probe needs labelled correctness data. The combiner is trained on the same split used to fit the probe, which the authors say adds a mild optimistic bias.[^c10]
- On MedicalQA with SE, neither the probe nor the combination reliably improves TCE. The authors attribute this to low base accuracy making the probe hard to calibrate; that explanation is theirs and was not tested.[^c11]
- TCE falls back to the base hallucination rate when coverage is zero, so complete abstention is penalized lightly.[^c12]
- Optimising a model toward low output entropy, rather than only reading entropy off it, is the same bet with a different lever. A test-time prefix tuned to minimise entropy is reported to raise accuracy, and its authors name the risk: the objective "can push the model into a state of over-confidence, leading to" overly deterministic reasoning.[^c13] They argue freezing the weights guards against it; no confidence-versus-correctness measure is reported in the sections read. See [[test-time-prefix-steering]].
- My inference, untested here: the same blind spot should affect any abstention or clarification gate that thresholds a dispersion score, since a consistent wrong reading looks settled to it.

## Related

- [[semantic-entropy]] — its Limits already note that consistent error scores low; this note measures the cost of that for abstention
- [[abstention]] — the decision this score feeds
- [[conformal-abstention]] — another route to holding a stated error rate
- [[internal-prober]] — the probe family the PC probe belongs to
- [[post-hoc-abstention]] — thresholding a score after generation
- [[within-question-entropy-inversion]] — the same blind spot inside one question's candidates, where a misleading passage rather than the model's own repetition yields the confident error

[^c1]: arxiv-2603-21172 — "We show that the effectiveness of entropybased UQ methods is highly model-dependent and identify a characteristic failure mode, the confidently wrong regime, in which models produce low-entropy hallucinations."
[^c2]: arxiv-2603-21172 — "This cluster includes both correct answers and hallucinations, the latter being confidently wrong instances in which the output distribution lacks diversity despite being incorrect"
[^c3]: arxiv-2603-21172 — "questions assigned identical zero SE scores are spread across a range of PC probe logits, with hallucinations often receiving elevated risk scores."
[^c4]: arxiv-2603-21172 — "SE is the stronger detector for Llama and Ministral on TriviaQA, while the PC probe dominates for Qwen."
[^c5]: arxiv-2603-21172 — "Entropy based methods fail to enter this regime at non-trivial coverage."
[^c6]: arxiv-2603-21172 — "Methods incorporating the PC probe lower the risk floor, and consequently track the calibration diagonal more closely throughout the high-trust regime."
[^c7]: arxiv-2603-21172 — "These gains are achieved without additional inference overhead beyond a single forward pass of the LLM."
[^c8]: arxiv-2603-21172 — "strong AUROC does not imply reliable selective prediction at strict safety thresholds"
[^c9]: arxiv-2603-21172 — "Our experiments are limited to short-form QA tasks, where answers can be judged as hallucination relative to reference strings."
[^c10]: arxiv-2603-21172 — "this introduces a mild optimistic bias, mitigated but not eliminated by strong regularization."
[^c11]: arxiv-2603-21172 — "when base model accuracy is low, the correctness probe itself becomes harder to calibrate, limiting the benefit of combination."
[^c12]: arxiv-2603-21172 — "This penalizes complete abstention less harshly than some alternative designs"
[^c13]: arxiv-2512-04748 — "push the model into a state of over-confidence, leading to"
