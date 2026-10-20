---
description: "Variation ratio scores an unlabelled item by the share of ensemble members that dissent from the majority class, a vote-based uncertainty that does not use how confident each member is."
aliases: ["VaR", "variation ratio uncertainty", "majority-dissent score"]
sources: ["arxiv-2512-05759"]
---
# Variation ratio

The variation ratio is an uncertainty score for active learning over an ensemble. "The variation ratio (VaR) is based on deep ensembles,"[^c1] where N networks share one training set and differ in their initial parameters. Their disagreement on an item is read as the model's uncertainty about it. For a point x, "the VaR measures the fraction of ensemble members diverging from the majority class",[^c2] computed as one minus the share of members that vote for the most frequent class. "If all members agree on a prediction, the VaR will be 0."[^c3] A region's score is the mean over its points, which is how the paper ranks regions.

The mechanism is a hard-vote measure. VaR reads only which class each member predicts, not how sure each member is. The paper's other ensemble score, ensemble entropy, works on the averaged probabilities: it "is then defined as the entropy of the average prediction".[^c4] My reading is that the two can diverge where members are confident and split, and where members are soft and agree; VaR sees a split vote in both cases, while the entropy of the mean reacts to the probability mass. The paper does not separate these cases with a test of its own.

The motivation for an ensemble at all is that a single network's softmax probabilities are "known to be overconfident".[^c5] Averaging over members "can significantly improve the calibration",[^c6] a claim the paper cites to prior work rather than measures in the parts it reports.

Results on the column partition are close for the two scores. On Toronto-3D with SPVCNN, "reaches the mIoU@90 threshold with 12 % and 14 % of annotated data, respectively" for entropy and VaR.[^c7] On S3DIS the entropy-based selection "is able to reach the mIoU@90 threshold with 11.3 % of labeled points".[^c8] The paper's summary is that both metrics "can lead to significantly improved uncertainty estimates for AL".[^c9]

## Limits

- The 12 % and 14 % gap on Toronto is within the seed noise the paper reports: "the mIoU@90 value differs by up to ±3 % of labeled points."[^c10] These runs do not separate VaR from entropy, and the paper does not claim they do.
- The ensemble is small: "an ensemble size of N = 4 (where applicable)".[^c11] No ensemble-size ablation appears in the parts read, and the cost of training N networks per cycle is not set against the annotation it saves.
- The mIoU@90 target is itself unstable where performance saturates: "The mIoU@90 is particularly sensitive" to seed effects in that regime.[^c12]
- Two architectures and three datasets were tested, and the advantage over single-network uncertainty is cited, not measured here.
- The reading of VaR as blind to member confidence is a consequence of its formula, not an experiment in the paper.

## Related

- [[rashomon-committee-querying]] — committee disagreement scored by weighted vote entropy; VaR belongs to the same vote-based family, as my reading.
- [[entropy]] — the Shannon entropy that the paper's second ensemble score applies to the averaged prediction.
- [[annotatable-region-partition]] — the regions over which the paper averages VaR and entropy.
- [[model-variant-spread-as-disagreement]] — ensemble spread read as disagreement, a related reading of the same signal.
- [[class-stratified-scheduled-noise-uncertainty-sampling]] — a modified uncertainty score for 3D segmentation selection; the plain top-k ranking it fixes has the picks pile onto the majority class.

[^c1]: arxiv-2512-05759 — "The variation ratio (VaR) is based on deep ensembles,"
[^c2]: arxiv-2512-05759 — "the VaR measures the fraction of ensemble members diverging from"
[^c3]: arxiv-2512-05759 — "If all members agree on a prediction, the VaR will be 0."
[^c4]: arxiv-2512-05759 — "is then defined as the entropy of the average prediction"
[^c5]: arxiv-2512-05759 — "softmax probabilities of the network which are known to be overconfident"
[^c6]: arxiv-2512-05759 — "can significantly improve the calibration"
[^c7]: arxiv-2512-05759 — "reaches the mIoU@90 threshold with 12 % and 14 % of annotated data, respectively"
[^c8]: arxiv-2512-05759 — "is able to reach the mIoU@90 threshold with 11.3 % of labeled points"
[^c9]: arxiv-2512-05759 — "can lead to significantly improved uncertainty estimates for AL"
[^c10]: arxiv-2512-05759 — "the mIoU@90 value differs by up to ±3 % of labeled points"
[^c11]: arxiv-2512-05759 — "an ensemble size of N = 4 (where applicable)"
[^c12]: arxiv-2512-05759 — "The mIoU@90 is particularly sensitive"
