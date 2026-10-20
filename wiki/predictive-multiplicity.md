---
description: "Predictive multiplicity measures disagreement among equally accurate models on one instance; on vision benchmarks it tracks human vote entropy only modestly beyond single-model entropy."
aliases: ["model multiplicity", "inter-model disagreement", "Rashomon-set disagreement"]
sources: ["doi-10-48550-arxiv-2609-34506"]
---
# Predictive multiplicity

Predictive multiplicity is the disagreement among models that are about
equally good on the same data. The paper defines it as "predictive
multiplicity, which measures the disagreement among equivalent models that
are able to achieve nearly equivalent accuracy on a given dataset".[^c1] It
is a property of the set of models, not of any one of them. A single model's
[[entropy]] or softmax confidence asks how sure that model is; multiplicity
asks whether the equally good models agree.

Two measures are used. The first is inter-model label disagreement. Each
model's predicted class is one vote, and the entropy of the vote shares is
normalised by log K; it is computed over "the proportion of models predicting
each category as the vote probability".[^c2] It is zero when every model
agrees, and it cannot say anything else on those images: "being discrete, it
is exactly zero on the 83.5% of images where all eight models agree, and
carries information only through the remaining 16.5%."[^c3] The second is
inter-model distribution divergence, the Jensen-Shannon divergence between the
models' full predictive distributions, which "measures the divergence between
model prediction distributions".[^c4]

The motivation is an intuition the paper states directly: "one can intuitively
expect images where equivalent models disagree to also be where multiple
humans disagree".[^c5] The test uses eight fine-tuned networks from three
families (ResNet, EfficientNet, MobileNetV3), treated as a subset of the
[[rashomon-committee-querying|Rashomon set]], correlated against normalised
human vote entropy on FER+ and CIFAR-10H.

What it found is a modest gain, not a better proxy. On CIFAR-10H, "inter-model
vote entropy aligns at ρ = 0.315, slightly below the continuous measures
(0.363)", the average single-model entropy.[^c6] On FER+ the best-aligned
measure is again a single-model one: "Even in the best-aligned setting (FER+,
average predictive entropy)".[^c7] The paper's summary is that "predictive
multiplicity provides only modest improvement" over single-model uncertainty.[^c8]

## Limits

The eight models were all fine-tuned on one training split with one recipe,
so their disagreement is among models trained alike. Whether a set of
independently trained models would show more spread is not tested; that is my
inference from the setup, not a finding. The paper asserts that the eight
models are a subset of the Rashomon set without checking a near-optimality
bound on them.

Only two image datasets were used, and the training target is one label per
image (a majority vote for FER+). The paper "do[es] not adopt the method of
training with soft labels", so a model trained on the full vote distribution
was not compared.[^c9] Results are Spearman correlations and agreement counts;
no decision rule built on multiplicity is evaluated, so whether it changes a
deployment outcome is open. Nothing here covers language models or dialogue
agents.

## Related

- [[human-model-uncertainty-dissociation]] — the single-model version of this
  gap, measured on clarification timing in a dialogue agent; the vision
  replication there cites this measure.
- [[rashomon-committee-querying]] — uses vote entropy over a Rashomon set, but
  to choose queries in active learning, not to check the set against human
  labels.
- [[calibration]] — the property of single-model confidence that multiplicity
  is compared against; the paper does not calibrate its scores.

[^c1]: doi-10-48550-arxiv-2609-34506 — "predictive multiplicity, which measures the disagreement among equivalent models that are able to achieve nearly equivalent accuracy on a given dataset"
[^c2]: doi-10-48550-arxiv-2609-34506 — "the proportion of models predicting each category as the vote probability"
[^c3]: doi-10-48550-arxiv-2609-34506 — "being discrete, it is exactly zero on the 83.5% of images where all eight models agree, and carries information only through the remaining 16.5%."
[^c4]: doi-10-48550-arxiv-2609-34506 — "We measure the divergence between model prediction distributions using the Jensen-Shannon divergence"
[^c5]: doi-10-48550-arxiv-2609-34506 — "one can intuitively expect images where equivalent models disagree to also be where multiple humans disagree"
[^c6]: doi-10-48550-arxiv-2609-34506 — "inter-model vote entropy aligns at ρ = 0.315, slightly below the continuous measures (0.363)"
[^c7]: doi-10-48550-arxiv-2609-34506 — "Even in the best-aligned setting (FER+, average predictive entropy)"
[^c8]: doi-10-48550-arxiv-2609-34506 — "predictive multiplicity provides only modest improvement"
[^c9]: doi-10-48550-arxiv-2609-34506 — "we do not adopt the method of training with soft labels"
