---
description: "Faithfulness Divergence scores a confidence distribution by the concentration-weighted KL surprise when truth is revealed, so confident misalignment costs more than diffuse misalignment."
aliases: ["FD", "distributional linguistic confidence", "confidence as Beta distribution over reader interpretations"]
sources: ["doi-10-48550-arxiv-2605-19344"]
---
# Faithfulness Divergence

A hedged statement ("probably", "I believe") is read differently by different readers. Yeh et al. model its confidence not as one number but as a Beta distribution over the probability readers perceive that the statement is correct. The mean is the central tendency across readers. The concentration (alpha + beta) is the strength of agreement: the same mean with low concentration means readers interpret the cue inconsistently.[^c1]

## The metric

Calibration (ECE) is population-level. The authors argue it is necessary but not sufficient: two predictors can have similar average calibration yet convey very different instance-level confidence. Faithfulness is the instance-level complement: a confidence distribution is faithful when observing the ground truth induces little surprise relative to prior beliefs.[^c2]

Concretely, the prior Beta(a, b) is updated with one Bernoulli observation of the correctness label y, giving the posterior Beta(a+y, b+1-y). Then FD = (a+b) · KL(posterior || prior). The KL term is Bayesian surprise. The concentration weights it as the effective sample size of the prior.[^c3] Lower FD means more faithful communication.

## What it measured

On four controlled subsets built from Llama-3.1-8B-Instruct on SQuAD 2.0, which vary mean confidence, concentration and accuracy, FD was the only metric that recovered the expected ordering. Concentrated, misaligned distributions got the highest penalty. The same misalignment expressed with low concentration got less. Plain KL inverted the ranking because it penalises diffuse distributions more. Expected Brier and expected NLL also failed, since neither treats variance as an amplifier of surprise.[^c4]

The metric sits inside a pipeline, RALC. It Platt-scales the distribution mean and keeps the concentration. It then retrieves hedging expressions whose Beta distributions are nearest, by Wasserstein-1 distance, to the calibrated target, and rewrites the answer with them. The paper reports in-domain gains of up to 66% in faithfulness and 58% in calibration across three QA benchmarks and five model families.[^c5] The concentration is kept unchanged because the authors found no natural target for calibrating it.[^c6]

My inference, not the paper's: for asking and answering, the metric says an answer's hedge is judged by how strongly readers would have believed it, not only by where its mean sits. An unambiguous wrong assertion is the worst case.

## Limits

- "Readers" are human or model-based evaluators, abstracted as the estimator g. How well model-evaluator distributions match real human ones is not established by the text I read.
- FD is a relative instance-level score with no absolute scale. It was validated on one constructed four-subset comparison, not against human judgments of trust.
- Concentration is preserved rather than calibrated, so the pipeline cannot fix over- or under-agreement among readers.
- The Beta form is a modelling choice, justified by analogy to evidential deep learning and conjugacy. That analogy gives the form and nothing about whether real reader distributions are Beta.
- Gains are reported as in-domain, up to 66% and 58%. I read only the abstract and the setup for these, not the per-model tables.

## Related

- [[hedged-mirage]] — hedging in prose that diverges from what the answerer actually commits to
- [[decoupled-claim-calibration-training]] — another route to making expressed confidence track correctness
- [[belief-augmented-generation]] — conditioning generation on explicit belief state

[^c1]: doi-10-48550-arxiv-2605-19344 — "the concentration (α + β) encodes agreement strength: a high mean with"
[^c2]: doi-10-48550-arxiv-2605-19344 — "A confidence distribution is faithful when observing the ground truth induces little surprise relative"
[^c3]: doi-10-48550-arxiv-2605-19344 — "FDi := (αi + βi ) · KL(Si∗ ∥ Si )"
[^c4]: doi-10-48550-arxiv-2605-19344 — "FD is the only metric that recovers the expected surprise ordering"
[^c5]: doi-10-48550-arxiv-2605-19344 — "improves in-domain faithfulness"
[^c6]: doi-10-48550-arxiv-2605-19344 — "due to the nonexistence of a natural target for concentration calibration"
