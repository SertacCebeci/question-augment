---
description: "A detector's class confidence and box variance can be calibrated to the spread of annotators' labels instead of a ground truth, so calibration needs no gold labels."
aliases: ["calibration to annotator disagreement", "annotator-uncertainty calibration", "ground-truth-free calibration"]
sources: ["doi-10-48550-arxiv-2605-24722"]
---
# Calibration to annotator disagreement

Calibration asks whether a stated confidence matches how often the event occurs, and the usual measurements need an outcome to score against ([[calibration]]). Object-detection calibrators inherit that need: existing methods are "they require ground truth annotations to" compute their precision and IoU targets.[^c1] Where annotators disagree on an ambiguous object, there is no single outcome to score. The mechanism here replaces the outcome with the annotators' own distribution. The detector's class confidence and box variance are pushed toward the spread of the annotations, so the ground truth is removed from both training and evaluation.[^c14]

**Targets.** Annotations on an image are grouped into clusters, one per object. For a cluster, the soft class target for each class is the share of annotators who chose it; an annotator who did not mark the object is counted as choosing background.[^c2] The class calibrator's target is the "percentage of annotators that annotated the j-th class", a share rather than a majority vote.[^c3] For boxes, the target variance per coordinate is built from the cluster's minimum and maximum box, scaled by the annotator certainty, the fraction of annotators "agreeing on the bounding box location in the" cluster, with the ratio capped at 0.999 for numerical stability.[^c4] The result is a variance "given the confidence interval and the specified" level of agreement.[^c5]

**Train-time.** The classification head is trained with cross-entropy against the soft target "instead of hard one-hot labels".[^c6] Localisation is trained so that the predicted mean and covariance place "all bounding boxes of the h-th cluster" inside the predicted interval.[^c7] The regression term is a modification of direct moment matching that matches the annotators' statistics, not the sample statistics "obtained using the ground truth values".[^c27]

**Post-hoc.** On a held-out validation set, predictions are paired with annotator shares, and isotonic regression is fitted from predicted confidence to share, one calibrator per class and one per box-variance component. The authors choose isotonic regression because it "models the calibration task as a monotonic regression problem".[^c8] Low-scoring predictions are down-weighted by their prediction certainty so that they do not dominate the fit.[^c28] At inference the other class probabilities are rescaled so that the vector still sums to one, since "the probability vector should sum to one" after any calibration.[^c9]

**Evaluation without ground truth.** Four metrics are computed against the annotation clusters: total variation distance on matched objects, on false positives, a localisation error, and a penalty for missed clusters. They are reported with their geometric mean of complements, so one poor component pulls the aggregate down.[^c10] The paper also reports D-ECE and LaECE, which do need a reference; for those it builds a proxy ground truth by majority voting over the clusters.[^c11] That is a substitute for the reference, not an absence of one.

**Result.** On a dental set (DX-20), a chest radiograph set (VBD-CXR) and a synthetic-annotator natural-image set (VOC-MIX), the calibrated Gaussian detectors "perform on par against the deep ensemble models", whose cost grows because "models increase linearly with the number of annotators".[^c12][^c13] In an ablation on one detector, supervising directly with the annotators' agreement "significantly improves our model confidence estimates for FP".[^c13b]

## Limits

- The share is a proxy, not the uncertainty itself. The method assumes the annotators' spread is the target a reader should be shown. The authors state that they "also assume that the annotators' uncertainty" in class and box is linearly coupled, and note that the two are "often orthogonal in practice".[^c16][^c17]
- Annotator counts are small and agreement is low. DX-20 used "five dentists" per image with a Krippendorff's alpha of 0.109; VBD-CXR and VOC-MIX reach only 0.305 and 0.339.[^c20][^c21] With three to five annotators, a share takes few values. This coarseness is my inference, not a measured effect, and it may limit what the isotonic fit can learn.
- The natural-image set is synthetic: "all 5,011 natural images were annotated by 25 simulated annotators".[^c26] Only the medical sets have real multi-annotator disagreement.
- The localisation metrics "cannot be directly compared across architectures".[^c15] Only within-architecture comparison against the uncalibrated model is supported.
- Generalisation is claimed, not tested broadly. The framework "is generalizable to many existing probabilistic object detectors", but the experiments use three Gaussian extensions: YOLOX, Faster R-CNN and RetinaNet.[^c18]
- The method is not the best on mean error. Deep ensembles obtain "the best mean calibration error in most of the experiment settings", and the calibrated detectors are on par, not ahead.[^c19]
- The ablation is on one model, "RetinaNet-G" with the proposed loss.[^c22]
- The usual calibration metrics are "not directly applicable to our" setting, so the comparison rests on the four new metrics the authors designed.[^c29]

## Related

- [[calibration]] — the ground-truth calibration whose target this note replaces with annotator shares; that note's limits already say its numbers need resolved outcomes.
- [[single-reference-grading-confound]] — one reference answer scores professional disagreement as error; this method takes the spread of annotators as the target instead.
- [[claim-level-agreement-labeling]] — agreement used as a tag rather than as a calibration target; neither treats agreement as truth.
- [[uncertainty-decomposition]] — the aleatoric and epistemic cut; annotator spread is plausibly the ambiguity part, though the paper does not make that split (my inference).
- [[reducible-context-gap-disagreement]] — rater disagreement studied as a measured quantity; there it is explained, here it is used as a training target.

[^c1]: doi-10-48550-arxiv-2605-24722 — "they require ground truth annotations to"
[^c2]: doi-10-48550-arxiv-2605-24722 — "When a cluster does not contain an annotation from a certain annotator"
[^c3]: doi-10-48550-arxiv-2605-24722 — "percentage of annotators that annotated the j-th class"
[^c4]: doi-10-48550-arxiv-2605-24722 — "annotators agreeing on the bounding box location in the"
[^c5]: doi-10-48550-arxiv-2605-24722 — "variance given the confidence interval and the specified"
[^c6]: doi-10-48550-arxiv-2605-24722 — "instead of hard one-hot labels"
[^c7]: doi-10-48550-arxiv-2605-24722 — "mean and covariance matrix such that all bounding boxes"
[^c8]: doi-10-48550-arxiv-2605-24722 — "a monotonic regression problem and is easy to implement"
[^c9]: doi-10-48550-arxiv-2605-24722 — "the probability vector should sum to one"
[^c10]: doi-10-48550-arxiv-2605-24722 — "as well as their geometric mean"
[^c11]: doi-10-48550-arxiv-2605-24722 — "by using majority voting to obtain reference ground truth"
[^c12]: doi-10-48550-arxiv-2605-24722 — "perform on par against the deep ensemble models"
[^c13]: doi-10-48550-arxiv-2605-24722 — "models increase linearly with the number of annotators"
[^c13b]: doi-10-48550-arxiv-2605-24722 — "significantly improves our model confidence estimates for FP"
[^c14]: doi-10-48550-arxiv-2605-24722 — "annotators’ annotation distribution offers a more intuitive approach"
[^c15]: doi-10-48550-arxiv-2605-24722 — "cannot be directly compared across architectures"
[^c16]: doi-10-48550-arxiv-2605-24722 — "we also assume that the annotators’ uncertainty"
[^c17]: doi-10-48550-arxiv-2605-24722 — "often orthogonal in practice"
[^c18]: doi-10-48550-arxiv-2605-24722 — "This framework is generalizable to many existing probabilistic object detectors"
[^c19]: doi-10-48550-arxiv-2605-24722 — "the best mean calibration error in most of the experiment"
[^c20]: doi-10-48550-arxiv-2605-24722 — "We randomly assigned five dentists"
[^c21]: doi-10-48550-arxiv-2605-24722 — "0.109, 0.305, and"
[^c22]: doi-10-48550-arxiv-2605-24722 — "in the proposed framework by analyzing RetinaNet-G"
[^c26]: doi-10-48550-arxiv-2605-24722 — "all 5,011 natural images were annotated by 25 simulated annotators"
[^c27]: doi-10-48550-arxiv-2605-24722 — "statistics obtained using the ground truth values"
[^c28]: doi-10-48550-arxiv-2605-24722 — "To prevent low-scoring predictions from dominating the training of"
[^c29]: doi-10-48550-arxiv-2605-24722 — "are not directly applicable to our"
