---
description: "Detecting a wrong reasoning trajectory does not predict that a triggered question recovers it; intervention harms correct trajectories about as often as it fixes wrong ones."
aliases: ["detection-recovery gap", "diagnosis-correction gap"]
sources: ["luo-2026-what"]
---
# Detection–recovery gap

> The [[belief-state-gating-policy|gate]] can tell a wrong trajectory from a
> right one. That is not the same as the question it triggers fixing the
> wrong one — or leaving the right one alone.

## Definition / Mechanism

Luo, Dahan & Zhu measure the gate's two jobs separately: catching wrong
trajectories, and helping once triggered. On catching: "In our adaptive
setting, the gating policy uses the internal hidden state probe and an
external PRM; of the trajectories caught by this policy, 51.4% were wrong in
their measured baseline. This demonstrates the policy itself is efficient at
catching samples that are likely wrong" — against a 23.3% base rate of wrong
samples when intervening on everything.[^c1]

On helping: "However, the effectiveness of our intervention is double-edged.
... We observe [[recovery-postulate|recovery]] of wrong samples, but our intervention can also harm
confidently correct samples; for the fixed trigger scheduling, |Δacc| is
greater in magnitude on confidently correct samples than on confidently
incorrect ones."[^c2]

The paper states the general result directly: "even after gating,
interventions are equally likely to harm correct trajectories as they are to
recover incorrect ones... These results demonstrate a gap between hidden
state detection and recovery in the reasoning trace. LLMs still struggle to
identify flaws in their own logic, even though the signal exists in the
hidden state."[^c3]

The authors' reading of the mechanism is an interpretation, not a second
measurement: they attribute the asymmetry to a general susceptibility-to-doubt
effect — "This asymmetry reflects the same mechanism identified by Kumaran et
al. [13], where a model is more susceptible to changing its opinion when it
is underconfident. Our question-asking intervention implicitly signals doubt
in the current trajectory and the model treats this as necessary feedback,
updating its distribution even when the original answer was correct."[^c4]

## Why it matters

This is a limit on any selection criterion that scores *whether to ask*, on
this stall: a criterion that correctly identifies which trajectories need
help does not thereby guarantee that intervening helps them and spares the
rest. The gap is between diagnosis and correction, not between two rival
detectors — no criterion on map-2 (EIG, VoI, [[semantic-entropy|semantic entropy]], or this
paper's own probe) is validated against the second half of that pair.

## Limits

Measured on math reasoning (GSM8k, Math500, AIME24) in a self-play or
matched-teacher setting with Qwen3 and Olmo-3-7B-Think, where "correct" is
majority-vote agreement with a verifiable ground-truth answer; the magnitude
comparison (|Δacc| on correct vs. incorrect trajectories) is reported for the
fixed-scheduling gate specifically, and the paper itself flags the
confidence intervals on the adaptive-setting comparison as not significant.
Whether the same asymmetry holds for open-domain questions with no
verifiable correctness label is untested by this source.

## Related

[[belief-state-gating-policy]] · [[value-of-information]] · [[semantic-entropy]]

[^c1]: luo-2026-what — "In our adaptive setting, the gating policy uses the internal hidden state probe and an external PRM; of the trajectories caught by this policy, 51.4% were wrong in their measured baseline. This demonstrates the policy itself is efficient at catching samples that are likely wrong."
[^c2]: luo-2026-what — "However, the effectiveness of our intervention is double-edged."
[^c3]: luo-2026-what — "even after gating, interventions are equally likely to harm correct trajectories as they are to recover incorrect ones"
[^c4]: luo-2026-what — "This asymmetry reflects the same mechanism identified by Kumaran et al. [13], where a model is more susceptible to changing its opinion when it is underconfident. Our question-asking intervention implicitly signals doubt in the current trajectory and the model treats this as necessary feedback, updating its distribution even when the original answer was correct."
