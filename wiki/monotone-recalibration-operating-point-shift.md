---
description: "A monotone recalibration keeps the ranking of confidence scores but moves where a fixed numerical threshold falls, so the same cutoff commits to a different set of answers."
aliases: []
sources: ["doi-10-48550-arxiv-2608-26846"]
---
# Monotone recalibration shifts the operating point of a fixed threshold

A confidence score does two jobs in a controller. Its order ranks the candidate
answers, and its numerical value is compared with a cutoff. A monotone map
changes only the second job. Isotonic regression is monotone, so it cannot
reorder the states: "Because isotonic regression preserves score order (apart
from possible ties), it does not improve ranking quality."[^c1] It does move
the numbers, and the cutoff is applied to the moved numbers: "However, it can
rescale scores, so a fixed threshold such as 0.7 selects a different set of
states[^c2] and thus results in a different operating point."

## The mechanism

A controller that commits when confidence is at least $\tau$ splits the states
into a commit set and a remainder. That split depends on where $\tau$ falls on
the score axis. Two maps that both preserve order can place the same $\tau$ at
different points in the ranking, so the commit set changes while the ranking
does not. (This is my inference from monotonicity, not a measured result.)
A ranking metric such as AUROC is blind to this change; a fixed-threshold
metric is not.

The measurement isolates it. The paper collects every state along a fixed
evidence path, freezes an isotonic map fitted on a separate split, and replays
the same stored states under raw and calibrated scores. "Because the answers,
evidence, thresholds, budgets, and costs are identical, any difference in
actions comes only from the score shown to the controller."[^c11] At the same
threshold of 0.7, calibration "changes which questions agents ultimately
commit to answering."[^c3] Among committed answers, accuracy rises "by up to
41 percentage points" across six model–dataset pairs.[^c4]

The overall effect has no single sign. Overall accuracy improves by up to 15
points on HotpotQA and falls by up to 17 points on MuSiQue, as coverage drops
and retrieval use rises.[^c12] The paper reads the pattern as "a shift to a more selective, lower-risk
operating point"[^c5] and does not read it as better answers or better
confidence ranking. The same nominal cutoff is compared on purpose: "This is
not a matched-risk or matched-coverage comparison."[^c6] For a raw score the
number is a heuristic; for a calibrated score it is meant to carry a
probability: "for raw confidence, the identical number is only a heuristic."[^c7]

## Limits

- Selectivity is not utility. The paper says "greater selectivity does not
  mean greater utility" without explicit costs for errors, retrieval and
  deferral.[^c8] The reported cost curves are not end-to-end utility: the
  paper's accounting "price[s] only retrieval actions."[^c13]
- The 0.7 threshold was fixed a priori and not tuned, so the test shows what
  one nominal number does, not which number is right. The paper's advice for
  deployment: "A deployment threshold should instead be selected on a held-out
  validation set."[^c9]
- Only one monotone family (isotonic) is tested, on two multi-hop QA datasets
  and three models, so the generality of the shift across maps is not shown.
  "The empirical scope is limited to two multi-hop QA datasets, three models"
  is the paper's own statement of scope.[^c10]
- The claim that any monotone map shifts the operating point is a consequence
  of the mechanism, not a finding of the paper. The sign of the shift depends
  on the dataset, so a calibrated threshold cannot be assumed to help.

## Related

- [[calibration]] — the property that makes a numerical threshold a probability; the map used here is a calibration map, and its validity can decay with evidence depth.
- [[roc-curve]] — the same threshold sweep for a detector score; there the score's values are fixed and only the cutoff moves.
- [[accuracy-masks-selective-reliability]] — a risk-coverage evaluation; a single threshold is one point on such a curve.
- [[value-of-information]] — the decision a commitment threshold does not make: whether another retrieval is worth its cost.

[^c1]: doi-10-48550-arxiv-2608-26846 — "Because isotonic regression preserves score order (apart from possible ties), it does not improve ranking quality."
[^c2]: doi-10-48550-arxiv-2608-26846 — "However, it can rescale scores, so a fixed threshold such as 0.7 selects a different set of states"
[^c3]: doi-10-48550-arxiv-2608-26846 — "changes which questions agents ultimately commit to answering."
[^c4]: doi-10-48550-arxiv-2608-26846 — "accuracy among committed answers by up to 41 percentage points"
[^c5]: doi-10-48550-arxiv-2608-26846 — "These effects reflect a shift to a more selective, lower-risk operating"
[^c6]: doi-10-48550-arxiv-2608-26846 — "This is not a matched-risk or matched-coverage comparison"
[^c7]: doi-10-48550-arxiv-2608-26846 — "for raw confidence, the identical number is only a heuristic"
[^c8]: doi-10-48550-arxiv-2608-26846 — "greater selectivity does not mean greater utility"
[^c9]: doi-10-48550-arxiv-2608-26846 — "A deployment threshold should instead be selected on a held-out validation set"
[^c10]: doi-10-48550-arxiv-2608-26846 — "The empirical scope is limited to two multi-hop QA datasets, three models"
[^c11]: doi-10-48550-arxiv-2608-26846 — "any difference in actions comes only from the score shown to the"
[^c12]: doi-10-48550-arxiv-2608-26846 — "Overall accuracy improves by up to 15 percentage points on HotpotQA but falls by up"
[^c13]: doi-10-48550-arxiv-2608-26846 — "price only retrieval actions"
