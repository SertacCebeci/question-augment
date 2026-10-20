---
description: "An answerer abstains when its output distribution sits far from the crowd's label distribution for the same item, so annotator disagreement itself becomes the reason to withhold an answer."
aliases: ["CROWD-CALIBRATOR", "crowd-calibrated abstention", "soft calibration", "crowd-disagreement gate"]
sources: ["doi-10-48550-arxiv-2408-14141"]
---
# Crowd-distance abstention

An [[abstention]] gate needs a score to decide whether the answer goes through. The usual score is the model's own confidence: the answer is given when the top probability clears a threshold, "If the confidence is higher than t, the model predicts".[^c1] The objection the paper raises is that such a score is read off the model alone, so it cannot show whether the people who would label the item agree. Crowd-distance abstention replaces the score with a comparison. The model's output distribution is set against the distribution of labels a crowd would give the same input, and the answer is withheld when the two are far apart. The paper's own summary: the method "models the distance between the distribution of crowd worker labels and the model’s own distribution over labels to inform whether the model should abstain from a decision."[^c2]

## Mechanism

There are three parts. First, a base model is trained on the majority-vote label as usual and produces an output distribution over the labels. Second, a crowd estimator predicts the human distribution for an input at test time, when no annotators are present. For hate speech the estimator is built from individual annotators who are not in the target data: the paper selects "individual annotators that have annotated more than 2000 samples" in other corpora and trains one small network per annotator on the base model's [CLS] hidden state. The per-annotator outputs are merged into one distribution in three ways (label distribution, averaged confidence, weighted scoring).[^c3] For NLI there are no separate annotators to reuse, so a small regressor is trained to output the soft label directly, on a set where "Each sample gets 100 annotations".[^c4] Third, a distance between the base model's distribution and the crowd distribution is compared with a threshold. The paper tries KL, JSD and TVD, and an optional variant that adds the entropy of the base model's output.[^c5] Above the threshold the model abstains; below it the base model's argmax goes through. The rule is stated as: "far off from the human probability distribution, the model will abstain".[^c6]

The reason to put the crowd in the gate rather than in the training target is an earlier null result. The paper first trained on soft labels from three to five annotators and found that disagreement items did not get lower confidence: the analysis "shows that this is generally not the case."[^c7] My reading is that the authors therefore keep the crowd out of the model's training and estimate it separately at gate time.

## What counts as correct

The metrics still score the gate against correctness, and the paper says this does not presuppose one ground truth: "view it as observing a single sample of the underlying crowd distribution."[^c8] On this reading a correct answer is one draw from the crowd, and the question the gate answers is whether it lets the correct draws through. That is the paper's defence of the unit, not a result that the unit is right.

## Results

The paper's claim is that the method is "competitive with these baselines for hate speech detection and outperforms them for NLI."[^c9] The in-domain hate-speech gain is small. The Kamath et al. (2020) baseline "performs" close to the plain confidence gate, and the best crowd variant (average of annotator confidences, JSD with entropy) wins by fractions of a point.[^c10][^c11] On unseen hate-speech sets the picture is stronger: "Here we see that our C ROWD -C ALIBRATOR can outperform both MaxProb and Kamath".[^c12] The same passage adds that "This reveals the sensitivity of our method to the individual annotators" it was trained on, and for the original test set "the Gab annotators were more useful instead."[^c13][^c14] On NLI, evaluated on a test of 312 samples, "we can beat the baseline with an increase of 4.65% in AUC and 8.37% in AUROC" with TVD and entropy.[^c15][^c16]

## Limits

- Two tasks only, hate speech and NLI. Open-ended answers, generation and questions where the asker's cost of silence matters were not tested. (my inference)
- The gain is conditioned on dense annotation. The paper frames its benefit as arising "when we have access to a small set of samples with many annotations per instance (∼ 100)".[^c17] The NLI estimator exists because each item has 100 labels; the hate-speech estimator exists only because other corpora contain annotators with more than 2000 items each.
- The disagreement signal on the main hate-speech data comes from three to five annotators, which "can be limited in learning the crowd distribution."[^c18]
- The gate's quality is the estimator's quality. Both distributions are model outputs, so estimator error enters the threshold directly. The paper does not measure this separately. (my inference)
- The threshold is set by the designer, as in every confidence gate. A threshold fitted on one annotator set or one distribution need not hold on another, the same caution [[abstention]] records for confidence gates. (my inference)
- The out-of-domain results depend on which annotators the estimator came from, as above. A reader cannot tell from this work which annotator set is the right one for a new task.

## Related

- [[abstention]] — the decision frame this is a score for; the score here is a distance between two distributions, not the model's confidence.
- [[calibration]] — "Most of the calibration research has focused on the alignment between a model’s confidence" and predictive performance; the crowd gate asks instead whether the model's distribution matches the crowd's.[^c19]
- [[annotator-disagreement-calibration]] — the same crowd spread used as the calibration target, but there it recalibrates a detector's confidence rather than gating an answer.
- [[annotator-distribution-target]] — training on the annotator distribution as a soft label; this note keeps the crowd out of training and moves it into the gate.
- [[cross-regime-disagreement-abstention]] — abstention from disagreement between model regimes, not between the model and human annotators.

[^c1]: doi-10-48550-arxiv-2408-14141 — "If the confidence is higher than t, the model predicts,"
[^c2]: doi-10-48550-arxiv-2408-14141 — "models the distance between the distribution of crowd worker labels and the model’s own distribution over labels"
[^c3]: doi-10-48550-arxiv-2408-14141 — "individual annotators that have annotated more than 2000 samples"
[^c4]: doi-10-48550-arxiv-2408-14141 — "Each sample gets 100 annotations"
[^c5]: doi-10-48550-arxiv-2408-14141 — "we experiment with different distance metrics (KL divergence (KL), JSD, and TVD"
[^c6]: doi-10-48550-arxiv-2408-14141 — "far off from the human probability distribution, the model will abstain"
[^c7]: doi-10-48550-arxiv-2408-14141 — "shows that this is generally not the case."
[^c8]: doi-10-48550-arxiv-2408-14141 — "view it as observing a single sample of the underlying crowd distribution."
[^c9]: doi-10-48550-arxiv-2408-14141 — "competitive with these baselines for hate speech detection and outperforms them for NLI."
[^c10]: doi-10-48550-arxiv-2408-14141 — "The Kamath et al. (2020) baseline performs"
[^c11]: doi-10-48550-arxiv-2408-14141 — "using JSD as a distance metric with entropy yields the best results."
[^c12]: doi-10-48550-arxiv-2408-14141 — "Here we see that our C ROWD -C ALIBRATOR can outperform both MaxProb and Kamath"
[^c13]: doi-10-48550-arxiv-2408-14141 — "This reveals the sensitivity of our method to the individual annotators"
[^c14]: doi-10-48550-arxiv-2408-14141 — "the Gab annotators were more useful instead"
[^c15]: doi-10-48550-arxiv-2408-14141 — "We show the results obtained on the test of ChaosNLI (312 samples)"
[^c16]: doi-10-48550-arxiv-2408-14141 — "we can beat the baseline with an increase of 4.65% in AUC and 8.37% in AUROC."
[^c17]: doi-10-48550-arxiv-2408-14141 — "small set of samples with many annotations per instance (∼ 100)"
[^c18]: doi-10-48550-arxiv-2408-14141 — "is based on 3 - 5 annotators, which can be limited in learning the crowd distribution."
[^c19]: doi-10-48550-arxiv-2408-14141 — "Most of the calibration research has focused on the alignment between a model’s confidence"
