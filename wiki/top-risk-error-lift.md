---
description: "Lift@k scores a risk ranking by the error rate among its top-k riskiest answers relative to the base error rate, so it shows whether errors cluster at the top where global AUROC can hide them."
aliases: ["Lift@20", "top-k error lift", "top-ranked error concentration", "risk-ranking lift"]
sources: ["arxiv-2512-24562", "arxiv-2511-20515"]
---
# Top-risk error lift

A hallucination risk score can be judged by how well it orders answers from safest to riskiest, and AUROC summarizes that ordering over every cut point at once. A different question is what happens at the top of the list: if someone reviews only the riskiest fraction of answers, how many of the errors do they catch? Lift@k answers that question. Take the fraction k of answers with the highest risk, measure the error rate inside that fraction, and divide by the error rate over all answers. The paper defines it as "the error rate among the top 20% highest-risk answers relative to the overall error rate", and borrows the frame from top-ranked retrieval.[^c1]

The headline use is the text-QA detector's human-labelled evaluation: "its top 20% highest-risk answers contain 96.5% errors, yielding a 2.06× lift over the base error rate."[^c2] The paper's reading is that gains in lift are a different claim from gains in separability. Larger gains in AUPRC and Lift@20 "indicate that HaluNet concentrates unsupported answers near the top of the risk ranking, beyond improvements in global separability alone."[^c3] So a detector can rank well on AUROC while spreading its errors thinly through the list, and lift is the check that catches the spread.

The arithmetic is simple and is my own, not the paper's. Let E be the error count and N the answer count, so the base rate is e = E/N. If the top fraction k holds a share s of all errors, its error rate is sE/(kN), and the lift is s/k. Lift is therefore capped at 1/k: when every error sits in the top k, lift is 1/k, which is 5 for k = 20%. The reported figures imply that the top 20% holds about 41% of all errors (2.06 × 0.20), and imply a base error rate near 47% (96.5% ÷ 2.06). Both numbers are back-calculated from the abstract and not stated in the text I read. The paper's own reading is consistent with this: "A value above one indicates that unsupported answers are concentrated among the top-risk examples."[^c4]

What survives the transfer from retrieval is the ratio to a base rate and the reading of the head of a ranking. What does not survive is the usual retrieval setting, where the relevant set is small and the top-k cut is far from the base rate. Here the base error rate is large, which caps what lift can show.

The same head-of-ranking reading applies when the ranking is used to choose data rather than to review answers. HalDec-Bench, a benchmark for detectors of hallucination in image captions, uses a detector to clean image-caption pairs: "we select the top 20% of sentences and measure their precision."[^c8] The noise rate "substantially decreases across all caption sources."[^c9] The case that bears most on the lift reading is the weakest one. For GPT-4o captions the detector's global ranking is poor, and the paper says so: "AUROC on GPT-4o is only 67.8, yet picking the confident examples can effectively reduce the noise rate."[^c10] The text gives the post-filter noise on that source as 5.0%, but not the unfiltered rate, which the text read does not carry.[^c11] My inference: a score can be too weak to order the whole pool and still be clean at its top, so a filter that keeps only the head is judged by precision at that cut, not by AUROC.

## Limits

- Lift is relative to the base rate, so it is not comparable across settings with different error rates. The paper's Table 1 reports hallucination rates "under different context ratios", so the same lift can mean different absolute precision in different rows.[^c5]
- The excerpt reports lift at one cut, k = 20%. I did not see a curve over k, so the shape of concentration elsewhere in the ranking is not shown.
- The human-labelled lift rests on 284 valid examples after 16 ambiguous ones were excluded.[^c6] The passages I read give no interval around the 2.06, so one lift value from a set this size is a noisy point estimate.
- Lift says nothing about whether the score is a probability. The paper says its score "is not intended to serve as a calibrated uncertainty estimate", so a lift of 2 is a statement about ranking, not about how often a top answer is wrong in an absolute sense.[^c7]
- The main-table lift is measured against judge labels, not human ones. The human check is the smaller sample on which the headline number was reported.

## Related

- [[single-pass-internal-signal-detector]] — the detector family whose headline number is reported as a lift alongside AUROC
- [[calibration]] — the other axis: a score can rank well without being a calibrated probability, which is why lift and calibration are separate checks
- [[log-score-verbalized-confidence-reward]] — the same keep-the-confident-head filter, where precision rose with the threshold at a cost in coverage

[^c1]: arxiv-2512-24562 — "it measures the error rate among the top 20% highest-risk answers relative to the overall error rate"
[^c2]: arxiv-2512-24562 — "its top 20% highest-risk answers contain 96.5% errors, yielding a 2.06× lift over the base error rate."
[^c3]: arxiv-2512-24562 — "indicate that HaluNet concentrates unsupported answers near the top of the risk ranking, beyond improvements in global separability alone"
[^c4]: arxiv-2512-24562 — "A value above one indicates that unsupported answers are concentrated among the top-risk examples."
[^c5]: arxiv-2512-24562 — "Dataset sizes and hallucination rates (%) under different context ratios"
[^c6]: arxiv-2512-24562 — "After excluding 16 examples marked ambiguous, 284 valid examples remain."
[^c7]: arxiv-2512-24562 — "it is not intended to serve as a calibrated uncertainty estimate"
[^c8]: arxiv-2511-20515 — "we select the top 20% of sentences and measure their precision"
[^c9]: arxiv-2511-20515 — "substantially decreases across all caption sources"
[^c10]: arxiv-2511-20515 — "AUROC on GPT-4o is only 67.8, yet picking the confident examples can"
[^c11]: arxiv-2511-20515 — "is also reduced to 5.0%"
