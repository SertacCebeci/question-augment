---
description: "The Brier skill score reports a probability forecast's Brier score as a fractional improvement over always predicting the base rate, so it stays comparable across unbalanced datasets."
aliases: ["BSS", "Brier skill", "Brier skill score"]
sources: ["arxiv-2512-08810"]
---
# Brier skill score

The Brier score is the mean squared gap between a stated probability and the 0/1 outcome. A Brier score of 0 implies perfect calibration, with confidences exactly 1 on correct outputs and exactly 0 on incorrect ones.[^b1] Its raw value is hard to read across datasets: a fixed number means different things at different base rates. The Brier skill score (BSS) fixes the reference point. The reference is the unskilled predictor, which "assigns every sample the base-rate confidence," that is, the fraction of correct outputs in the set. Its Brier score has a closed form, B_ref = p_r(1 − p_r), and BSS = (B_ref − B) / B_ref.[^b2]

The reading follows from that construction. Positive BSS values show improvement over the unskilled baseline, and negative values show deterioration.[^b3] The scale is anchored by the balanced case: random binary confidences are expected to give B = 0.25 on a set that is 50% correct and 50% incorrect.[^b4] The study reports BSS "particularly in unbalanced scenarios," where a raw Brier value would look small simply because the outcome is rarely the minority class.[^b5]

The score has a degenerate case. When the base rate is 0 or 1, the denominator is zero, and the convention is BSS = 1 if B = 0 (perfect prediction) and BSS = −∞ otherwise.[^b6]

The study pairs BSS with expected calibration error because the two fail differently. ECE "is intuitive but can be misleading": a predictor that always outputs the base rate falls into one bin and can show a deceptively low ECE.[^b7] A skill score against that same base-rate predictor catches the case, because a predictor that carries no information scores zero.

## Limits

- BSS is a skill measure, not a calibration measure on its own. Its reference is the base-rate predictor, which is perfectly calibrated and carries no information, so BSS mixes how well the confidences are calibrated with how much they discriminate. The study does not split the two. (The split is the point of the Brier decomposition in [[calibration-grouping-information-loss-decomposition]]; that link is my inference, not a result of this work.)
- The reference changes with the base rate of each set. Two datasets with different correctness rates give BSS values measured against different baselines, so BSS across datasets is comparable only in the sense of improvement over the local base rate.
- The degenerate case is a convention. A set with all outputs correct or all incorrect has no defined skill in the usual sense, and the convention decides what is reported.
- The study's BSS numbers come from one initial confidence measure (average token likelihood) on three code benchmarks. The values in its table were not checked here beyond their existence, and nothing above extends them to other domains.

## Related

- [[calibration]] — the Brier score is one of three measures there; BSS is a skill transform of it, and ECE is a different measure of the same property.
- [[multicalibration]] — the study that reports BSS beside ECE for group-conditional calibration of code LLMs.
- [[calibration-grouping-information-loss-decomposition]] — decomposes the Brier-type loss into calibration, grouping and irreducible terms, which a single skill number does not separate.

[^b1]: arxiv-2512-08810 — "A Brier score of 0 implies perfect calibration"
[^b2]: arxiv-2512-08810 — "assigns every sample the base-rate confidence"
[^b3]: arxiv-2512-08810 — "where positive BSS values show improvement over the unskilled"
[^b4]: arxiv-2512-08810 — "Random binary confidences are expected to yield B = 0.25 for a balanced dataset"
[^b5]: arxiv-2512-08810 — "particularly in unbalanced scenarios, we also report the Brier Skill"
[^b6]: arxiv-2512-08810 — "by convention, we set BSS = 1 if"
[^b7]: arxiv-2512-08810 — "ECE is intuitive but can be misleading: a naive"
