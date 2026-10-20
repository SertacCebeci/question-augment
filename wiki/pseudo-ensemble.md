---
description: "Answer-preserving input perturbations of one frozen model substitute for a trained ensemble, giving member distributions that rank abstention errors better than single-pass entropy."
aliases: ["pseudo-ensemble", "test-time augmentation", "virtual ensemble"]
sources: ["maheshwari-2026"]
---
# Pseudo-ensemble

> A cheap stand-in for a trained ensemble: perturb the input in ways that
> cannot change the correct answer, run the frozen model once per
> perturbation, and treat the resulting distributions as ensemble members.

## Definition / Mechanism

Maheshwari & Raina (2026) define answer-preserving
transformations $t_1,\dots,t_M$ of an input $x$: applying $t_m$ changes the
surface form of a multiple-choice question without changing which option is
correct. Running a single pretrained model once on each $t_m(x)$ gives $M$
categorical distributions $p^{(m)} = P(y \mid t_m(x), \theta)$, which are
then treated as ensemble members: averaged to a prediction $\bar p$, and fed
into the standard ensemble-[[uncertainty-decomposition|uncertainty decomposition]] — [[entropy]] of the
average ($H[\bar p]$, "entropy of expected"), the average of the member
entropies ("expected entropy"), and their difference ([[mutual-information|mutual information]],
read as "knowledge uncertainty" versus "data uncertainty"). Diversity that a
conventional ensemble gets from independently trained parameters is instead
obtained from different views of one input, at the cost of $M$ forward
passes and no retraining.[^c1]

The paper's main construction is **option shuffling**: each member sees the
same multiple-choice question with the $K$ candidate answers relabelled
under a different permutation $\pi_m$; the member's distribution over label
positions is mapped back through $\pi_m^{-1}$ before averaging, which both
cancels the position bias multiple-choice language models are known to carry
and supplies the ensemble's diversity. Two other constructions are tested
and found weaker: perturbing the audio (Gaussian noise, compression, a time
shift) and swapping the option symbols (A/B/C/D → 1/2/3/4, etc.).[^c2]

On TinyMU (229M parameters) over MuChoMusic, option shuffling with $M=4$
raised accuracy from 55.7% to 59.2% and reduced the area under the error
retention curve (questions sorted by an uncertainty score, most uncertain
discarded first, error rate plotted against the retained fraction) from
0.293 (single-pass entropy) to 0.261 for expected entropy — the best of the
five measures tested. Mutual information performed *worse* than the
single-pass baseline (0.306): members disagree on questions the averaged
prediction still answers correctly, because shuffling moves probability mass
between option labels without changing the ensemble's arg max, so the
"knowledge uncertainty" term picks up shuffling artifacts rather than
genuine model ignorance.[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| This paper (music audio-language models) | pseudo-ensemble | — |
| Computer vision | test-time augmentation | close — the paper names this as the precedent it follows for getting diversity from input views rather than parameters, but does not establish the two as measured identically |
| Deep-learning uncertainty estimation | virtual ensembles | close — same relation: cited as precedent, not shown equivalent |

Evidence for the "close" naming: "Diversity that a conventional ensemble
gets from different parameters is here obtained from different views of the
same input, following test-time augmentation [4] and virtual ensembles
[32]."[^c4]

## Why it matters

This is a concrete, cited answer to stall 10's cost problem: [[abstention]]
needs a scalar uncertainty score to build the selection function $g$, and a
trained ensemble is the richest known source of one but is often too
expensive to build. Pseudo-ensembles show that the same decomposition
(total / data / knowledge uncertainty) is available from a single frozen
model at the cost of a few extra forward passes — provided the perturbation
used to generate diversity does not itself corrupt the mutual-information
term, which this paper's own result shows is not automatic.[^c5]

## Transfer

| | |
|---|---|
| Home field | ensemble uncertainty quantification: $M$ independently trained models, member disagreement reflecting genuine epistemic uncertainty about parameters |
| Here | one frozen model, $M$ answer-preserving views of the same input, member disagreement reflecting sensitivity to surface form rather than parameters |
| What survives | the total/data/knowledge decomposition ($H[\bar p]$, expected entropy, mutual information) and its use to rank abstention errors; the empirical finding that this decomposition, computed from perturbation-only diversity, can beat single-pass entropy |
| What does not | the interpretation of mutual information as knowledge uncertainty — here it partly measures the perturbation's own artifacts (shuffling-induced label-mass movement), and on this benchmark it is worse than the single-pass baseline, the opposite of its role in a trained ensemble |

## Limits

- One model (TinyMU, 229M parameters) and one benchmark (MuChoMusic); the
  paper states it has not shown the ranking holds for larger models or other
  music QA sets.[^c6]
- Option shuffling exploits a known position bias in multiple-choice
  prompting; the paper notes it may lose its effect on models invariant to
  option order, and it applies only to multiple-choice formats.[^c7]
- Better error-ranking is not [[calibration]]: a low expected-entropy score
  means the prediction is more likely correct, not that $\bar p$ is a
  well-calibrated probability — the paper reports no calibration curve.[^c8]
- The claim that this transfers the ensemble decomposition rests on this one
  paper's single-model, single-benchmark result; no independent replication
  is cited here.

## Related

[[abstention]] · [[semantic-entropy]] · [[entropy]]

[^c1]: maheshwari-2026 — "Let t1 , . . . , tM be transformations of the input which are answer-preserving: applying tm to x changes the surface form of the query without changing which candidate answer is correct. Running the model once on each transformed input gives M distributions over the options"
[^c2]: maheshwari-2026
[^c3]: maheshwari-2026
[^c4]: maheshwari-2026 — "Diversity that a conventional ensemble gets from different parameters is here obtained from different views of the same input, following test-time augmentation [4] and virtual ensembles [32]."
[^c5]: maheshwari-2026
[^c6]: maheshwari-2026 — "The study uses one model and one benchmark. TinyMU is a good test case for a compact music model, but we have not shown that the same ranking holds for multi-billion-parameter systems or for other music QA sets."
[^c7]: maheshwari-2026 — "Option shuffling exploits a known position bias, so it may become less useful if future models become invariant to option order, and it applies only to multiple-choice prompts."
[^c8]: maheshwari-2026 — "Better uncertainty ranking is not the same as calibration: a low expected entropy means the prediction is more likely to be correct, not that p̄ is a well-calibrated probability."
