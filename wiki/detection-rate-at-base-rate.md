---
description: "A detector's alarm is worth what its false-alarm rate at the deployed base rate makes it, so a recall reported alone leaves the operator's question open."
aliases: ["Bayesian detection rate", "base-rate fallacy in intrusion detection", "base-rate neglect", "positive predictive value at the base rate"]
sources: ["doi-10-48550-arxiv-2608-24850"]
---
# Detection rate at the base rate

When the event being detected is rare, what an alarm is worth depends less on how often the detector catches true events than on how often it fires on ordinary ones. The review names the quantity an analyst actually experiences the Bayesian detection rate, P(I|A): the probability of an intrusion given an alert. It is built from the true-positive rate P(A|I), the prior probability of an intrusion P(I), and the false-alarm rate P(A|¬I).[^c1] Because the prior is so small, P(I|A) "remains low even for a detector with an excellent" true-positive rate, unless the false-alarm rate is driven very low.[^c2] The formula is Axelsson's, and the review cites it for the base-rate fallacy in intrusion detection.[^c1]

The mechanism transfers as a point about what gets reported. A recall figure is a statement about P(A|I). The number an operator needs is P(I|A), and that needs the false-alarm rate at the rate of intrusions the deployment will actually see. The review puts the consequence bluntly: "A paper reporting 99% recall without reporting the false-alarm rate" has "not addressed the question an operator has."[^c3] Its checklist asks for the same thing, "Report the false-alarm rate at a realistic base rate" rather than on a balanced test set.[^c4] Where the deployment cares about ranking under heavy imbalance, the review prefers precision-recall curves, because the ROC curve's "false-positive-rate axis is dominated by the large negative class", which compresses the region of interest.[^c5]

The point is old enough to have a name in the review's list of pitfalls. Arp et al. include "base-rate neglect" among the recurring problems in machine learning for computer security, next to sampling bias and inappropriate performance measures.[^c6] A later study of graph-based lateral-movement detection is cited for the same dependence: the choice of "base rate determines the reported result."[^c7] So the same detector can be reported as strong or weak by the mix of events in its test set, which is the reason the operating base rate has to be named before a number is read.

The structure also appears outside intrusion detection. A reported score can depend on the share of items of one kind in the evaluation, as in [[abstention-base-rate-sensitivity-in-rl]], where an always-abstain policy follows from the training mix. Here the dependence runs through the test mix rather than the training mix. Which split the test mix comes from is a separate question, treated in [[question-matched-split]].

## Limits

- The formula and its argument are the review's citation of Axelsson's analysis. The review gives no worked numbers beyond the "99% recall" example, so the size of the effect at any real deployment is not shown in this text.
- The note requires a deployed base rate, and the text does not say how to estimate one. The checklist says "realistic" without a method (my inference: when the base rate is unknown, P(I|A) cannot be stated, and the text does not address that case).
- The false-alarm rate is treated as stable across the deployment. The review does not analyse how it varies across sites, times or attack types (my inference).
- The review argues the point; it does not test it on a detector. The lateral-movement result [114] is reported only in summary, and the text gives no table.
- The transfer from intrusion detection to other rare-event classifiers is my inference. The review's scope is enterprise security.

## Related

- [[abstention-base-rate-sensitivity-in-rl]] — a reported behaviour that depends on the share of one item kind in the data; there the mix is in training, here it is in the test set
- [[question-matched-split]] — which test mix a number comes from decides which question it answers
- [[benchmark-drift]] — a reported agreement that holds at release and decays later; the operating condition has to be named for the number to mean anything

[^c1]: doi-10-48550-arxiv-2608-24850 — "the quantity an analyst actually experiences"
[^c2]: doi-10-48550-arxiv-2608-24850 — "which remains low even for a detector with an excellent"
[^c3]: doi-10-48550-arxiv-2608-24850 — "A paper reporting 99% recall without reporting the false-alarm rate"
[^c4]: doi-10-48550-arxiv-2608-24850 — "Report the false-alarm rate at a realistic base rate"
[^c5]: doi-10-48550-arxiv-2608-24850 — "false-positive-rate axis is dominated by the large negative class"
[^c6]: doi-10-48550-arxiv-2608-24850 — "base-rate neglect, lab-only evaluation"
[^c7]: doi-10-48550-arxiv-2608-24850 — "base rate determines the reported result"
