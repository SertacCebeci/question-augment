---
description: "The share of positive saliency mass that falls on background pixels tracks training-data correlation and task shape demands, so it is not a clean sign of a healthy classifier."
aliases: ["background attention", "background feature importance", "pixel ratio", "background attribution ratio"]
sources: ["arxiv-2512-05937"]
---
# Background attribution share

A saliency map of a classifier can be reduced to one number: how much of its positive attribution lands on the object, and how much on what surrounds it. In the traffic-sign study the number is a pixel ratio, defined as "the ratio of positive attributing features within the traffic sign" image area "relative to the absolute value of attributing features in the whole image."[^c1] A low background share has been read as the sign of a healthy classifier, and a high one as a sign that it "overfitted on spurious background correlations."[^c2] The authors' starting point is that this reading "has thus far not been evaluated systematically."[^c3]

The mechanism they test is that the share is a function of the training data as well as of the learner. Six synthetic training sets were generated from one pipeline, differing in their background correlation and in the stage of camera variation; three networks (two ConvNeXt sizes and a ResNet50) were trained on them and attributed with Kernel SHAP and with GradCAM.[^c4] Three properties of the data were expected to move the share. The result for each:

- **Background correlation.** Training on uncorrelated data gave higher pixel ratios, "meaning they are less focused on the background" than the correlated counterparts, with the authors reading this as a "significant trend" toward "a higher importance to background features" under correlation.[^c5] Correlation gives the network a reason to use the background, because the background then carries class information.
- **Shape variety.** A wider set of sign shapes raised background importance, which the authors attribute to recognising the shape against the background as a discriminative feature.[^c6] Here the background share rises because the task requires the contrast, not because the model overfit.
- **Camera variation.** The support is weak; the authors report only "weak support for the hypothesis that higher camera variation" raises background attention, particularly for uncorrelated backgrounds on two of the networks.[^c7]

The share therefore separates less than its reading assumes. The ConvNeXt networks, when tested on data from the same domain, gained from the correlated background and "showed especially the modern ConvNeXt architectures being able to benefit" from it.[^c8] The same correlated training gave the worst accuracy when the test set was uncorrelated, "in almost all cases (16 out of 18)."[^c9] A high background share, then, can accompany good performance on the domain the model was trained on, and a low one can accompany poor transfer. The authors' conclusion is that "Background attention should not inherently be interpreted as detrimental to performance."[^c10]

The concept that transfers is this: a saliency quantity measures what the network uses, and what the network uses is shaped by what the training set made informative. The share is evidence about the data-plus-model pair. Read alone it cannot say whether the background use was a cue that will break under shift or a legitimate contextual signal. That is the gap between this measure and the spurious-cue account in [[clever-hans-effect]]: the share is the quantity an attribution check would read, and the study shows it moving with a design choice.

## Limits

- One use case, traffic signs, and one synthetic pipeline. The authors say that "The presented study has only shed light on the problem with" regard to this use case.[^c11] Whether the same dependence holds for natural images or real collections is not tested.
- Two saliency methods only. The metric "could also be replaced by another suitable saliency method,"[^c12] but the paper evaluates only Kernel SHAP and GradCAM, and asks for "a larger selection of saliency methods."[^c13] A different method could give different shares.
- The expensive method was run on a subset: "we apply both methods only to the first 200 images of" each class, and on one test set, the correlated frontal one.[^c14] The findings are on that subset.
- The paper does not establish a better health measure. It shows that the share is not a clean indicator; it does not show which attribution quantity, if any, separates spurious from legitimate background use. The shape explanation is the authors' presumption, not something they test.
- The realism of the synthetic data is taken from an earlier cross-dataset evaluation, not re-established in this paper.
- Each configuration was trained with three random seeds, which is a small number for the variance of attribution-based measures.

## Related

- [[clever-hans-effect]] — the spurious-cue account that an attribution share is meant to detect; this share does not separate spurious from legitimate background use
- [[dual-use-context-cue]] — a background cue that is signal on ordinary data and a trap under a swap; the same two-sided reading applies to the share
- [[occlusion-logprob-saliency]] — another saliency map read as a statement about where an answer leans, in a different modality and method

[^c1]: arxiv-2512-05937 — "ratio of positive attributing features within the traffic sign"
[^c2]: arxiv-2512-05937 — "overfitted on spurious background correlations"
[^c3]: arxiv-2512-05937 — "has thus far not been evaluated systematically."
[^c4]: arxiv-2512-05937 — "which differ with respect to their background correlation"
[^c5]: arxiv-2512-05937 — "network giving a higher importance to background features."
[^c6]: arxiv-2512-05937 — "importance of background features, presumably as recognizing"
[^c7]: arxiv-2512-05937 — "weak support for the hypothesis that higher camera variation"
[^c8]: arxiv-2512-05937 — "showed especially the modern ConvNeXt architectures being able to benefit"
[^c9]: arxiv-2512-05937 — "in almost all cases (16 out of 18) the worst result"
[^c10]: arxiv-2512-05937 — "Background attention should not inherently be interpreted as detrimental to performance."
[^c11]: arxiv-2512-05937 — "The presented study has only shed light on the problem with"
[^c12]: arxiv-2512-05937 — "could also be replaced by another suitable saliency method."
[^c13]: arxiv-2512-05937 — "a larger selection of saliency methods"
[^c14]: arxiv-2512-05937 — "we apply both methods only to the first 200 images of"
