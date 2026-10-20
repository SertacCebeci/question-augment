---
description: "Privatizing a threshold-indexed histogram by Gaussian noise, with sensitivity fixed at 2 for any number of thresholds and zCDP charged per stream occurrence along the adaptive transcript."
aliases: ["event-level zCDP", "pathwise zCDP accountant", "occurrence-level differential privacy histogram"]
sources: ["doi-10-48550-arxiv-2608-07913"]
---
# Event-level zCDP histogram release

A calibration set is summarized by counts of how many examples fall in each score bin and how much loss they carry. Releasing those counts with Gaussian noise is a standard differential-privacy mechanism. What the work adds is the accounting for a release that is repeated, adaptive, and threshold-indexed.

The release is a fixed vector of bin counts and loss-weighted bin counts, one pair per client release. Adjacency is the zero-out relation on one stream occurrence: "one event occurrence contributes its histogram vector or zero while message shape remains fixed."[^c1] Under that relation the two histograms have a bounded L2 sensitivity that does not grow with the threshold grid: "Two binned histograms, one for all examples and one weighted by loss, have add or remove L2 sensitivity at most 2 regardless of the number of thresholds."[^c2] The reason this matters is that thresholds are chosen after seeing releases. (My inference, not the paper's wording: if each threshold had its own released count, the sensitivity of the joint release would grow with the grid.) A single finite histogram from which every threshold's cumulative counts are read off avoids that. The paper's phrasing: "Finite histograms of scores and errors provide sensitivity independent of threshold count, while pathwise zCDP accounts for the adaptive transcript."[^c3]

## The accountant

Gaussian noise of coordinate variance σ² on a sensitivity-Δ release costs a fixed amount in zCDP, and zCDP composes additively. The paper states the basic cost as "A release with coordinate noise variance σ² is 1/σ²-zCDP," after scaling to the sensitivity bound.[^c4] The charge is not a flat per-round sum. It is pathwise: "We prove pathwise event level zCDP that charges each occurrence only for releases containing it."[^c5] An occurrence that is dropped from a release is not charged for that release, and an occurrence present in many releases pays for each. Because the server chooses the next client and batch size from the transcript, the accountant has to be a bound along each realized path, not a single worst-case number; that is the "fully adaptive composition/filter argument" the paper cites for zCDP.[^c6]

Two consequences are the paper's own. First, reuse is the cost: the same occurrence enters every monitored prefix, so repeated calibration over rounds consumes privacy on the same records. Second, the certificate's privacy is per occurrence, not per person or per source document. A stream of repeated items is charged once per occurrence.

## What was measured

The experiments show that the accountant is binding in practice rather than a formality. Every positive private cell "consumes roughly 20× to 78× event reuse," and certification "draws 30 to 78 events per unique calibration item."[^c7] An item-level or person-level guarantee has to compose over all of them; the paper says this directly: "If one support response, source document, or person contributes repeatedly, all occurrences must be charged together."[^c8]

## Limits

- **Event-level only.** The main statement is "event-level DP for one stream occurrence." The guarantee "is not privacy for the 839 public support responses, nor for their contributors."[^c9] Source- or person-level protection needs bounded contribution and a recalibrated accountant, which the paper does not supply.
- **Metadata leaks.** Client identity, release status and padded batch capacity are public. "The mechanism also does not hide public padded" participation metadata.[^c11]
- **Discretization.** The paper notes that "empirical CDFs require explicit" discretization and sensitivity, so the bin grid is part of the privacy claim, not a free choice.[^c12]
- **Schedule leaks.** "Privacy additionally requires the visible schedule to depend only on public information and earlier DP messages; otherwise the schedule itself can leak data."[^c10]
- **Utility cost.** Positive private certificates were rare. At the secondary target 0.20, "HaluEval fires in 11 of 200 trials at ε = 4" and never at ε ≤ 2; the strong ε = 2 results used the exploratory target 0.30.[^c14] The paper names repeated event use as one of its main limitations, not a solved one.
- **Not a comparison to the alternative.** The paper notes that "Validity-preserving DP e-value mechanisms" exist and that adapting them to private federated selective risk is nontrivial. Whether they would give a tighter private accountant here is untested.[^c13]

## Related

- [[private-federated-selective-risk-certificate]] — the certificate whose histograms this accountant covers
- [[gated-target-risk-contrast]] — the statistic read off the cumulative counts
- [[dp-stability-full-data-conformal-coverage]] — a different differential-privacy object: a coverage floor for full-data conformal sets, not a released histogram
- [[atom-stratified-federated-conformal-calibration]] — mergeable score digests for federated calibration, without a stated privacy accountant

[^c1]: doi-10-48550-arxiv-2608-07913 — "its histogram vector or zero while message shape remains fixed"
[^c2]: doi-10-48550-arxiv-2608-07913 — "have add or remove L2 sensitivity at most 2 regardless of the number of"
[^c3]: doi-10-48550-arxiv-2608-07913 — "Finite histograms of scores and errors provide sensitivity independent of threshold count"
[^c4]: doi-10-48550-arxiv-2608-07913 — "A release with coordinate noise variance"
[^c5]: doi-10-48550-arxiv-2608-07913 — "that charges each occurrence only for releases containing it"
[^c6]: doi-10-48550-arxiv-2608-07913 — "the fully adaptive composition/filter argument specialized to zCDP"
[^c7]: doi-10-48550-arxiv-2608-07913 — "roughly 20× to 78× event reuse"
[^c8]: doi-10-48550-arxiv-2608-07913 — "If one support response, source document, or person contributes repeatedly, all occurrences must be charged together."
[^c9]: doi-10-48550-arxiv-2608-07913 — "the guarantee is not privacy for the 839 public support responses, nor for their contributors"
[^c10]: doi-10-48550-arxiv-2608-07913 — "Privacy additionally requires the visible schedule to depend"
[^c11]: doi-10-48550-arxiv-2608-07913 — "The mechanism also does not hide public padded"
[^c12]: doi-10-48550-arxiv-2608-07913 — "empirical CDFs require explicit"
[^c13]: doi-10-48550-arxiv-2608-07913 — "Validity-preserving DP e-value mechanisms"
[^c14]: doi-10-48550-arxiv-2608-07913 — "HaluEval fires in 11 of 200 trials at ε = 4"
