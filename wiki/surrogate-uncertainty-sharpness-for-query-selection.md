---
description: "Query selection is only as good as the surrogate's uncertainty ranking: coverage alone is not enough, since wide intervals or overconfident ones both mislead acquisition and cost extra evaluations."
aliases: ["uncertainty calibration for active learning", "coverage versus sharpness of surrogate uncertainty", "foundation-model surrogate for active learning"]
sources: ["arxiv-2603-12567"]
---
# Surrogate uncertainty sharpness for query selection

An active-learning loop asks the next question (which candidate to synthesise and measure) by scoring candidates with an acquisition function such as Expected Improvement or Upper Confidence Bound, built from a surrogate's predicted mean and uncertainty. Hu et al. (2026) argue and measure that the efficiency of that loop depends on what the uncertainty signal can distinguish, not on predictive accuracy alone. They name the dilemma: "GP models have reliable uncertainty but insufficient modeling capacity; RF and NN models have high capacity but unreliable uncertainty in small-data regimes."[^c1]

## Two ways uncertainty fails the query

Interval coverage hides both failures, so the paper reads coverage together with width and with a ranking metric.

- **Wide but covering (Gaussian process).** On the lattice-thermal-conductivity set the GP reached PICP 0.99 "through extremely wide prediction intervals (MPIW = 237.23, nearly 10× larger than TabPFN's 33.16)", so its uncertainty "provides no meaningful signal for distinguishing informative from uninformative candidates."[^c2] On the copper-alloy set it had coverage near 0.93 with intervals about three times wider than the foundation model's.[^c3]
- **Narrow and overconfident (random forest).** RF coverage was 0.86 against a 0.95 target; the paper says its ensemble variance underestimates uncertainty and so "the acquisition function over-exploit[s] overconfident predictions and miss[es] the global optimum."[^c4] This is the same undercoverage pattern as [[credible-interval-undercoverage]].

The ranking metric is AUSE (area under the sparsification error curve): low AUSE means the samples the surrogate flags as uncertain are the ones with the largest errors, so "the model is 'honestly' uncertain only when it is likely to be wrong."[^c5] NLL, a proper scoring rule, penalises both error and miscalibration.[^c6]

## What was measured

The surrogate tested is TabPFN, a transformer meta-trained on synthetic tabular tasks to approximate Bayesian inference in one forward pass, used inside the In-Context Active Learning (ICAL) loop. On ten materials datasets it needed fewer extra evaluations to find the optimum on 8, with mean savings of 52% against GP and 29.77% against RF over the datasets it won.[^c7] Its cross-validated NLL was 2.34 against 3.46 (GP) and 3.11 (RF) on the copper set, and AUSE 0.83 against 15.58 and 1.77.[^c8] The authors attribute the loop gains to this calibration. That attribution is correlational across datasets; no intervention swaps only the uncertainty and holds the mean fixed, except the hybrid variant below.

## A decoupled variant

Because kernel variance encodes spatial coverage of the labelled pool, the authors also pair TabPFN's mean with the GP's variance in a hybrid acquisition function, which they say "exploits the complementary strengths of both models."[^c9] The best acquisition function differed by dataset (UCB, EI, hybrid UCB), so the mean and the uncertainty come from different sources when it helps.

## A minimum-data threshold

The in-context surrogate was worse at very small starts. On the electrical-conductivity set with initial fraction at most 0.15, TabPFN needed about 80 extra evaluations against GP's 38-79 and RF's 22-42. The authors suggest "a minimum initial dataset size, approximately 15-20% of the candidate pool, should be collected" before relying on it.[^c10] A well-calibrated posterior still needs some task data to form.

## Limits

- Benchmarks are retrospective: candidates come from fixed datasets of tens to hundreds of materials, and "extra evaluations" counts steps to the known optimum. No prospective campaign is reported here.
- The causal claim that calibration explains the savings rests on metric agreement across datasets, not a controlled ablation. In the cases the paper reports, RF and TabPFN tie in mid-range settings and RF won 20% on one set.
- The 15-20% threshold comes from one dataset and is a rule of thumb, not a derived bound.
- Acquisition functions were normalised and tuned, which the authors admit "may disrupt the theoretical rigor" of the original Bayesian optimisation; part of the gain may come from that tuning.[^c11]
- The domain is materials property regression with a scalar objective; whether the same coverage-sharpness reading transfers to question selection by language models is my inference, not tested here.

## Related

- [[expected-information-gain]] — the ideal acquisition target that a surrogate's uncertainty only approximates.
- [[credible-interval-undercoverage]] — the RF failure here is undercoverage of nominal intervals.
- [[active-in-context-learning]] — in-context inference as a query-selection engine.
- [[active-testing]] — choosing which points to label when labels are costly.

[^c1]: arxiv-2603-12567 — "GP models have reliable uncertainty but insufficient modeling capacity; RF and NN models have high capacity but unreliable uncertainty in small-data regimes."
[^c2]: arxiv-2603-12567 — "provides no meaningful signal for distinguishing informative from uninformative"
[^c3]: arxiv-2603-12567 — "while the Gaussian Process achieved high coverage (PICP ≈ 0.93), it did so by producing excessively wide intervals (MPIW ≈ 32.50)"
[^c4]: arxiv-2603-12567 — "its heuristic ensemble variance systematically underestimates true predictive uncertainty, which in turn causes the acquisition function to over-exploit overconfident predictions"
[^c5]: arxiv-2603-12567 — "a low score implies that the model is “honestly” uncertain only when it is likely to be wrong"
[^c6]: arxiv-2603-12567 — "NLL is a proper scoring rule that penalizes both prediction error and poor uncertainty calibration"
[^c7]: arxiv-2603-12567 — "TabPFN achieves the lowest number of extra evaluations on 8 out of 10 datasets, with a mean saving of 52% relative to"
[^c8]: arxiv-2603-12567 — "TabPFN achieved the lowest NLL (2.34)"
[^c9]: arxiv-2603-12567 — "This decoupling exploits the complementary strengths of both models"
[^c10]: arxiv-2603-12567 — "it suggests that a minimum initial dataset size ,approximately 15–20% of the candidate pool ,should be collected"
[^c11]: arxiv-2603-12567 — "While this normalization may disrupt the theoretical rigor of original GP model based BO"
