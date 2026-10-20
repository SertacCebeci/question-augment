---
description: "A held-out split answers one question only: a random split asks whether a model can separate, a temporal split asks whether it will work later, so the split must match the decision."
aliases: ["random versus temporal split", "split-to-question match", "temporal split for deployment", "random k-fold split"]
sources: ["doi-10-48550-arxiv-2608-24850"]
---
# Question-matched split

A score computed on held-out data is an answer to a question, and the way the held-out data are chosen decides which question it answers. A random k-fold split draws test items from the same pool, in the same period, as the training items (my reading of the contrast the review draws). Its number therefore says whether the model can separate the classes it was shown. A temporal split puts the test items after the training items. Its number says something about what happens when the model is used later. The review puts the contrast in a compact form: random k-fold asks "can it separate?", and a temporal split asks "will it work next month?"[^c1]

The review turns this into a rule rather than a preference. The step that chooses the split is a gate, not a step: "random and temporal splits answer different questions," and "only one of them is the question a deployment asks."[^c2] For a claim about future performance, the requirement is explicit: "Any study whose claim concerns future performance owes the reader a temporally consistent split."[^c3] The earlier defect is the temporal bias, which occurs when "training data contains samples that post-date test samples."[^c4] A random split can contain that defect without anyone choosing it, and a reported number then answers the separation question while being read as the deployment question.

The mechanism depends on the data carrying a time axis. The review says that studying drift "requires a dataset with a usable time axis, which most security benchmarks do not have," and that "a single snapshot cannot exhibit drift no matter how it is split."[^c5] So the choice of split is limited by the dataset before the protocol starts. The review's advice follows from that: choose the dataset for its time coverage first, because no evaluation protocol can recover a time axis the data does not carry.[^c6] Its longitudinal example, LAMDA, was built with samples "spanning multiple years" so that temporally consistent splitting is possible.[^c7]

This is a different failure from one in which the split is correct but the pipeline is leaky. A temporal split can still be contaminated if the preprocessing is fitted before it, which is the order-of-operations problem in [[split-order-leakage]]. The two are checked separately. The question a split answers is also one part of the reported number: the operating base rate, treated in [[detection-rate-at-base-rate]], decides how the same test set reads.

## Limits

- The review states the rule and gives no measurement of how much a random split overstates deployment performance. The size of the gap between the two splits on any dataset is not shown in this text.
- A temporal split answers "will it work next month" only for the gap the split implies. The review does not say how large a gap is needed, or whether a short gap between train and test is enough to represent deployment (my inference: the gap is a second design choice the text leaves open).
- The rule needs a dataset with a time axis. Where the data are a single snapshot, no split can show drift, and the text gives no method for that case beyond choosing other data.
- The claim that only one split matches a deployment assumes the deployment's question is about future performance. Where the question is about separating known classes, the random split answers it, and the text does not say so explicitly (my inference).
- Drift is measured against human judgment in the cited judge work, and the review's split rule is not tested on any detector in the text read here.

## Related

- [[split-order-leakage]] — the other way a held-out number is inflated: by the order of operations, not by which question the split answers
- [[benchmark-drift]] — what a time-ordered check can show and a snapshot cannot: agreement that decays as the producing models change
- [[detection-rate-at-base-rate]] — the test set's mix of events decides the reported detection rate, as the split decides the question

[^c1]: doi-10-48550-arxiv-2608-24850 — "will it work next month?"
[^c2]: doi-10-48550-arxiv-2608-24850 — "random and temporal splits answer different questions"
[^c3]: doi-10-48550-arxiv-2608-24850 — "Any study whose claim concerns future performance owes the reader a temporally consistent split"
[^c4]: doi-10-48550-arxiv-2608-24850 — "training data contains"
[^c5]: doi-10-48550-arxiv-2608-24850 — "a single snapshot cannot exhibit drift no matter how it is split"
[^c6]: doi-10-48550-arxiv-2608-24850 — "choose the dataset for its time coverage first"
[^c7]: doi-10-48550-arxiv-2608-24850 — "spanning multiple years"
