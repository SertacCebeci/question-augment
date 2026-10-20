---
description: "Conformal sets keep coverage for any model, but an overconfident net gets small sets while a better-calibrated one gets larger sets and a weaker entropy-to-set-size link (Fashion-MNIST CNNs)."
aliases: ["entropy versus conformal set size", "MC Dropout and conformal complementarity"]
sources: ["arxiv-2603-10731"]
---
# Conformal set size and calibration trade-off

Split conformal prediction sets are sized from the softmax probability the model gives the true class on a held-out calibration set, not from entropy.[^c1] Ruijs, Kosiakova and Javed (2026) compare it with MC Dropout (50 stochastic passes, entropy split into expected entropy and mutual information) on two CNNs trained on Fashion-MNIST. The two methods read different signals, so what they report can diverge.

## What was observed

- The more accurate model, H-CNN VGG16 (92.99% best), was overconfident. It reached near-perfect confidence within the first 1,000 sorted samples, and its mutual information was low, which the authors read as little epistemic uncertainty.[^c2]
- GoogLeNet (89.72% best) rose in confidence more gradually. It had higher predictive and expected entropy and substantially larger mutual information, and the authors judge it better calibrated.[^c3]
- Conformal sets followed the same split. VGG16 mostly produced sets of size one, with the Shirt class the main exception. GoogLeNet produced fewer singletons and many sets of size two or three.[^c4]
- Entropy and set size tracked each other closely for VGG16 and loosely for GoogLeNet. The authors explain that GoogLeNet spreads probability over several plausible classes even when correct. The true class then gets a modest probability, and conformal prediction enlarges the set.[^c5]
- The authors' summary is that conformal prediction "guarantees empirical coverage regardless of calibration quality". Where entropy and true-label confidence disagree, it acts as a corrective, and the reliability costs set size.[^c6]

Reading: small sets can mean efficiency or overconfidence, and the same coverage guarantee holds in both cases. Set size alone therefore does not show whether the model's uncertainty is honest. (This is my inference from the comparison, not a tested claim.)

## Limits

- Two architectures, one 10-class image dataset, and a single run per setting. The calibration ranking comes from plots of confidence and entropy. I saw no significance tests.
- The architectures differ in size (about 180M against 12M parameters), overfitting and accuracy. Calibration is confounded with these, so the "GoogLeNet is better calibrated" claim is the authors' reading.
- Coverage is the marginal guarantee. It does not promise equal coverage per class, and the authors report class-level differences, with Shirt having the widest sets.
- Whether the pattern holds for language models or open-ended answers is not tested.
- The mutual information read as epistemic uncertainty depends on MC Dropout being a good posterior approximation. That is not verified here.

## Related

- [[calibration]] — the property VGG16 lacks and GoogLeNet is said to approach
- [[uncertainty-decomposition]] — the expected-entropy and mutual-information split used here
- [[mondrian-conformal-prediction]] — class-conditional coverage, which the class-wise Shirt spread motivates
- [[pseudo-ensemble]] — another cheap multi-pass route to the same decomposition
- [[confidently-wrong-low-entropy-regime]] — low entropy does not mean correct

[^c1]: arxiv-2603-10731 — "Conformal Prediction does not rely on entropy; instead, it ensures statistically valid"
[^c2]: arxiv-2603-10731 — "The confidence curve for H-CNN VGG16 rises sharply, reaching near-perfect confidence"
[^c3]: arxiv-2603-10731 — "Both predictive and expected entropy values are higher, and mutual information is substantially larger."
[^c4]: arxiv-2603-10731 — "GoogLeNet (Figure 6 (right)) produces fewer prediction sets of size one and significantly"
[^c5]: arxiv-2603-10731 — "This behavior stems from the model’s cautious"
[^c6]: arxiv-2603-10731 — "CP guarantees empirical coverage regardless of calibration quality"
