---
description: "Predicting disagreement as a set of present labels, one independent yes/no per label, recovers more of an item's possible interpretations than a fourth Complicated class or a single soft distribution."
aliases: ["multilabel NLI", "multi-label disagreement", "set-valued labels", "multilabel classification for disagreement"]
sources: ["doi-10-48550-arxiv-2209-03392"]
---
# Set-valued disagreement label

A classifier for a disagreement-prone item has three options. It can output a distribution over labels, it can add a fourth class for disagreement, or it can output a set of the labels that annotators actually chose. The third is the set-valued label. Jiang and de Marneffe take it for NLI, where an item can be labelled Entailment, Neutral, Contradiction, or any subset of these. The motivation is that a fourth "Complicated" class is not informative about which labels the annotators split between: "a 'Complicated' or 'Disagreement' class is not easily interpretable. We not only need to know whether there is disagreement, but also in what way."[^s1]

The mechanism is independent sigmoids on the three label logits. "We predict each E/N/C label independently, by applying the sigmoid function on top of the 3 logits," and a label is present "if its probability is greater than 0.5." The model is trained with cross-entropy on that output.[^s2] The gold set is built from annotator counts. On the ChaosNLI items a label is present if it has at least 20 of 100 votes, and on the original MNLI items if it has at least 2 of 5.[^s3][^s13] So the target itself is a subset of labels, not a soft distribution.

The measured effect is on recall of interpretations. The fourth-class model is weakest on the Complicated class, which the paper ties to the class's heterogeneity.[^s4] The multilabel model has a higher F1 than a soft-label baseline but a lower precision.[^s11] Its gain is in recall: "the macro recall increases compared to the 4-way classification (83.35 vs. 67.78)."[^s5] The paper's reading of the confusion table is that when the multilabel model predicts more than one label, the 4-way model "may miss one or more labels while the multilabel model can identify all of them."[^s6]

The authors also tie the choice to a use. The goal is not to maximise accuracy: "A model that can recall the possible interpretations is preferred to a model that misses them." The use they name is budget allocation: "The annotation budget could thus be prioritized by collecting annotations for items with potential for disagreement, as predicted by the model."[^s7]

## Limits

- Precision and exact-match accuracy are lower. The multilabel model has more output classes (seven, against four), and "The baseline model is more successful at items on which annotators agree," while the multilabel model is better "on items with disagreement (2/3 Labels Accuracy)."[^s8] A deployment that is mostly unanimous items would be worse off on the common case.
- The threshold is fixed by hand. The 0.5 probability cut and the 20-vote rule are the authors' choices, and the paper shows the effect: "the multilabel model often predicts labels when they are only slightly below the threshold of 20."[^s9] The reported recall depends on that cut, and no sensitivity curve is given in the sections read.
- The gold labels are defined with the same 20-vote rule, so recall is measured against labels built from a rule of the kind the model is trained on. This is a fair test of the rule's learnability, not of whether a set is the right representation of human interpretation.
- One model family (RoBERTa), one dataset (MNLI with ChaosNLI annotations), and three random initialisations. The paper did not test other architectures, other tasks, or generation.
- The paper proposes the multilabel output as intrinsic evaluation of how well a model captures the population's judgments, but does not test it as such: "the multilabel approach could potentially be used as intrinsic evaluation" is left as a suggestion.[^s10]
- The paper also reports that categorical training is the better choice when categorical output is needed. Its soft-label baseline is weaker on categorical scoring: "training with categorical labels performs better"[^s12] in predicting categorical labels. So part of the gain is the gain of training on categories rather than on distributions, which the paper does not separate from the change of output form (my inference).

## Related

- [[annotator-distribution-target]] — trains on the full annotator distribution and scores on two axes; the set-valued label drops the distribution and keeps the presence of each label.
- [[label-distribution-readings]] — what a spread of labels means, which bears on whether a set of labels or a single probability is the right output.
- [[annotation-disagreement-sources]] — the sources of disagreement that a set of labels is meant to expose.
- [[cross-rater-reliability]] — the agreement statistics that a set-valued label would need, which this note does not cover.

[^s1]: doi-10-48550-arxiv-2209-03392 — "We not only need to know whether there is disagreement, but also in what way"
[^s2]: doi-10-48550-arxiv-2209-03392 — "We predict each E/N/C label independently, by applying the sigmoid function on top of the 3 logits given by the MLP classifier on top of RoBERTa to obtain probabilities"
[^s3]: doi-10-48550-arxiv-2209-03392 — "For multilabel, a label is present if it has at least 20 votes (complement of 80 used for the single label items)."
[^s4]: doi-10-48550-arxiv-2209-03392 — "the Complicated class is hard to model, due to its heterogeneity, as we saw in Section 3.2."
[^s5]: doi-10-48550-arxiv-2209-03392 — "the macro recall increases compared to the 4-way classification (83.35 vs. 67.78)"
[^s6]: doi-10-48550-arxiv-2209-03392 — "the 4way model may miss one or more labels while the multilabel model can identify all of them."
[^s7]: doi-10-48550-arxiv-2209-03392 — "The annotation budget could thus be prioritized by collecting annotations for items with potential for disagreement, as predicted by the model."
[^s8]: doi-10-48550-arxiv-2209-03392 — "The baseline model is more successful at items on which annotators agree (higher 1 Label Accuracy), while our model performs better on items with disagreement (2/3 Labels Accuracy)."
[^s9]: doi-10-48550-arxiv-2209-03392 — "the multilabel model often predicts labels when they are only slightly below the threshold of 20"
[^s10]: doi-10-48550-arxiv-2209-03392 — "the multilabel approach could potentially be used as intrinsic evaluation for how well the model captures the judgments of the population"
[^s11]: doi-10-48550-arxiv-2209-03392 — "Our model has a higher F1 score than the baseline but a lower precision"
[^s12]: doi-10-48550-arxiv-2209-03392 — "training with categorical labels performs better"
[^s13]: doi-10-48550-arxiv-2209-03392 — "For multilabel, a label is present if it has at least 2 votes."
