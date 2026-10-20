---
description: "Reusing an old version's judge error rates to correct a new one removes attenuation but divides differential error by the old Youden index, which can worsen close comparisons."
aliases: ["transported judge calibration", "Rogan-Gladen transport across versions", "shared judge calibration"]
sources: ["doi-10-48550-arxiv-2609-34198"]
---
# Transported judge calibration

A judge's error rates are estimated on labelled outputs and then applied to outputs that are only judged. Across agent versions this is the practice the paper tests: calibrate the judge on the previous version's labels, then correct the new version's judged rate with those rates. The correction is the Rogan–Gladen inversion of [[calibrated-judge-estimator-efficiency-ordering]] applied across versions, "by the Rogan–Gladen correction with the old version's error rates".[^c1] The new version's success rate is recovered from its judged rate by subtracting the old false-positive rate and dividing by the old Youden index J_o.

The paper's Proposition 2 gives the resulting comparison error. Transport removes the attenuation term but keeps the differential term, divided by J_o. "Transport removes attenuation but divides the differential component by J_o < 1."[^c2] Because J_o is below one, the differential error is inflated, and the inflation is largest for the pairs where the true difference is small. "calibrating on the previous version makes the comparison worse" when the true difference is small relative to the differential term.[^c3]

The contrast is with the naive comparison. For a judge with no differential error, the naive comparison is pure attenuation: the judged difference is shrunk toward zero but keeps its sign. Transport gives that up in exchange for removing the shrinkage, and the differential term that was small becomes large after the division. The mechanism is therefore a trade of one error for another, and which trade is worse depends on the pair.

**Measured.** On the primary SWE-bench analysis, the paper reports that transporting old-version calibration raises the comparison error from 3.8 to 19.5 points.[^c4] It also reports that 24.6% of the bootstrap ratios are undefined, because the old version's Youden index can become nonpositive in a bootstrap draw.[^c5] The naive error of 3.8 points is the mean absolute comparison error across the 60 judge-by-pair units, which the paper's discussion reports.

## Limits

- The 19.5-point figure comes from one cohort: 35 agents of one scaffold family, three judges, 250 issues. It is not a general transport constant.
- The paper's Propositions 1 and 2 are not new mathematics. "Our Propositions 1 and 2 restate these classical and shared-calibration results for version pairs" [^c6]; the contribution is the measurement on public versions.
- Transport is not the only way to lose efficiency. The paper also reports a finite-sample effect that does not depend on differential error: "transport amplifies sampling noise and the naive error of a non-differential judge is pure attenuation" [^c7]. So a test that only asks whether transport beats the naive estimate can be met, or failed, by a judge with no differential error at all.
- The shared-calibration amplification by 1/J is attributed by the paper to Fiedler (2026), who reports it on MMLU-Pro; this note has not read that source. "Fiedler (2026) shows that shared calibration amplifies bias by 1/J" [^c8] is the paper's citation.
- The paper's conclusion is a preference, not a result about every setting: "of current outputs over judge-only release decisions or transported calibration" [^c9]. Labels on the current outputs cost more, and this note does not measure that cost.

## Related

- [[version-dependent-judge-error]] — the differential term that transport divides by J_o
- [[calibrated-judge-estimator-efficiency-ordering]] — the same Rogan–Gladen estimator for a single rate, on a calibration sample from the population it is applied to
- [[youden-index-threshold-for-noisy-reward-learning]] — the Youden index J as the judge's discriminability, which is what the division runs through
- [[paired-difference-judge-efficiency]] — labels on the current outputs, which the paper prefers to transported labels

[^c1]: doi-10-48550-arxiv-2609-34198 — "by the Rogan–Gladen correction with the old version's error rates"
[^c2]: doi-10-48550-arxiv-2609-34198 — "Transport removes attenuation but divides the differential component by J_o < 1."
[^c3]: doi-10-48550-arxiv-2609-34198 — "calibrating on the previous version makes the comparison worse."
[^c4]: doi-10-48550-arxiv-2609-34198 — "Transporting old-version calibration raises SWE-bench comparison error from 3.8 to 19.5 points, with"
[^c5]: doi-10-48550-arxiv-2609-34198 — "24.6% undefined bootstrap ratios"
[^c6]: doi-10-48550-arxiv-2609-34198 — "Our Propositions 1 and 2 restate these classical and shared-calibration results for version pairs"
[^c7]: doi-10-48550-arxiv-2609-34198 — "transport amplifies sampling noise and the naive error of a non-differential judge is pure attenuation"
[^c8]: doi-10-48550-arxiv-2609-34198 — "Fiedler (2026) shows that shared calibration amplifies bias by 1/J"
[^c9]: doi-10-48550-arxiv-2609-34198 — "of current outputs over judge-only release decisions or transported calibration"
