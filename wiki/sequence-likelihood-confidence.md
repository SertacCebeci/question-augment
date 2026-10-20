---
description: "A domain-adapted LLM's own token-probability confidence weakly discriminates correct answers (AUROC 0.65–0.81) — too poor to gate abstention or mode-routing."
aliases: ["pFT", "parametric confidence", "intrinsic sequence-likelihood confidence", "mean log-probability answer confidence"]
sources: ["asaria-2026", "lee-2026"]
---
# Sequence-likelihood confidence

> The one control signal a fine-tuned model hands you for free — its own
> token probability — turns out not to separate right answers from wrong
> ones well enough to act on.

## Definition / Mechanism

$p_{FT}(q)$ is the geometric mean of the generated tokens' probabilities:
exp of the mean token log-probability over the generated sequence, prompt
tokens excluded, the end-of-sequence token included in the likelihood
though not in the returned text — length-normalized by construction.[^c1]

Lee et al. (2026) pre-register criteria for using $p_{FT}$ as (a) a
routing-and-abstention trigger choosing between a retrieval mode and a
domain-adapted parametric mode, and (b) a distillation trigger selecting
which queries need further adaptation, across four 7–9B model families
(LLaMA-3.1, Qwen2.5, Gemma-2, Mistral) on retrieval-dominated extractive
document QA. The sequence-likelihood signal is insufficient relative to
retrieval — area under the [[roc-curve|receiver operating characteristic]] curve
0.65–0.81 under the registered criterion, before adaptation as well as
after, unchanged by scalar recalibration and not consistently improved by
token-level temperature rescaling.[^c2]

Three alternative intrinsic signals — minimum token probability, mean
[[entropy]], top-1/top-2 margin — fall in the same weak band, so the failure is
not an artifact of this particular scalarization.[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Lee et al. (2026) | $p_{FT}$ / parametric confidence | exact |
| Selective-prediction literature generally | sequence-likelihood confidence | exact |
| Asaria, Salomone & Gandhi (2026) | mean log-probability answer confidence $s(q)$ (unexponentiated; same ranking) | exact |

[^c4]

## Why it matters

Any framework that builds a selection function on a "proper uncertainty
score" ([[abstention]]) assumes that score already ranks correct above
incorrect. Here it barely does: correlation with correctness is +0.12 to
+0.32 and expected [[calibration]] error 0.48–0.72, on the exact model class
(small, domain-fine-tuned, no external ground truth at deployment) where an
enterprise would be most tempted to trust it for free.

Asaria, Salomone & Gandhi (2026) measure the identical
statistic — mean answer-token log-probability, frozen before fine-tuning —
on six open-weights models (1B–8B) on short-form factual QA and report
AUROC 0.73–0.86, a narrower and higher band than Lee et al.'s 0.65–0.81.
Used there not as a live inference-time routing trigger but as a one-time
training-set threshold that decides which examples get retargeted to an
abstention label during LoRA fine-tuning, the same signal produces a
model competitive with label-supervised abstention-tuning at matched
coverage (no detected difference across six models). The two results do
not contradict each other's numbers, but they disagree on what the signal
is fit for: Lee et al. call it too weak to gate a live routing decision;
Asaria et al. show a weaker-than-ideal signal can still be strong enough
to supervise a training-time abstain/answer split, because a coarse
threshold over a whole training set tolerates more noise than a per-query
inference gate does.[^c6]

## Limits

- One setting: extractive, source-grounded QA where retrieval is
  structurally favored; the paper states the value of confidence-based
  routing where retrieval is weak or unavailable remains an open question
  it does not answer, and this note's claim rests on that same boundary.[^c5]
- Rank-based metrics (AUROC/AURC) carry the comparative claim; the ECE
  numbers describe the signal's scale, not a ranking.
- Model scale is fixed at 7–9B in Lee et al.; Asaria et al. extend the
  measurement down to 1B but on a different task (short-form factual QA,
  not extraction), so the two AUROC bands are not a controlled comparison
  of scale or task alone.
- The routing verdict this signal feeds is separately explained by a
  near-zero headroom ceiling ([[routing-ceiling]]) — the two findings are
  not evidence for each other.

## Related

[[abstention]] · [[calibration]] · [[semantic-entropy]] · [[routing-ceiling]] · [[signal-gated-abstention-fine-tuning]]

[^c6]: asaria-2026 — "the mean log-probability over an answer span separates correct from incorrect answers with AUROC 0.73–0.86, holding even for a 1B model"
[^c1]: lee-2026 — "Parametric confidence pFT (q ) is the geometric mean of the generated tokens’ probabilities — exp of the mean token log-probability over the generated sequence, prompt tokens excluded, the end-of-sequence token included in the likelihood though not in the returned text. It is length-normalized by construction."
[^c2]: lee-2026
[^c3]: lee-2026 — "three alternative intrinsic signals (minimum token probability, mean entropy, top-1/top-2 margin) fall in the same band."
[^c4]: lee-2026 — "Parametric confidence pFT (q ) is the geometric mean of the generated tokens’ probabilities"
[^c5]: lee-2026
