---
description: "Training a multimodal answerer with RLVR under outcome-only grounding rewards raises answerable recall but lowers calibrated abstention, a measured recall-abstention trade-off."
aliases: ["reward-induced answering bias", "recall-calibration trade-off", "RLVR abstention collapse"]
sources: ["oh-2026"]
---
# RLVR answering bias

> Reinforcement learning with verifiable rewards teaches a multimodal
> answerer to ground better and decline less — in the same run, from the
> same reward.

## Definition / Mechanism

Across four backbones on the Omni-Persona benchmark, [[oh-2026|Oh et al.
(2026)]] report: "RLVR improves recall but not calibrated [[abstention]] under
our reward design, leaving Cal at or below the base model."[^c1]

The recall gain is real and substantial — "RLVR directly and substantially
improves answerable recall" — but it does not carry over to the
abstention side: "these gains do not translate into [[calibration]]: RLVR
fails to induce abstention, and Cal falls below base for every [[backbone-of-a-formula|backbone]]
(−0.8 to −4.0)."[^c2]

This is the source's own reading of the mechanism, not a further
measurement: "We interpret this as a reward-induced answering bias: since
our outcome rewards directly target grounding and reasoning, attempting a
grounded answer becomes the dominant signal even when the target persona
is absent, so abstention is rarely reinforced."[^c3]

## Why it matters

On stall 10, this is a measured cost of a specific training choice: an
outcome-only, verifiable reward that scores whether the answer is grounded
gives no separate credit for declining, so optimisation pressure moves the
policy toward asserting even on queries the reward signal never actually
resolves. A post-training design for an answerer that must sometimes say
"absent" cannot assume grounding-accuracy reward alone will preserve that
behaviour — the two must be rewarded, and reward-shaped, separately.

## Limits

- Measured for one reward design (rule-based perceptual verification plus
  LLM-as-judge retrieval verification, no SFT warm-up) on one benchmark
  (Omni-Persona) and four backbones (Qwen2.5-Omni-3B/7B, Gemma4-E2B/E4B);
  the authors flag that "more sophisticated reward shaping or cold-start
  SFT (Guo et al., 2025) may restore calibrated abstention," so the bias is
  a property of this reward design, not shown inherent to RLVR as a class.
- Abstention on the unanswerable side is scored by keyword matching, a
  coarse proxy that may undercount abstentions phrased unconventionally,
  so the size of the Cal drop is bounded by that instrument's precision.

## Related

[[calibrated-accuracy]] · [[detection-to-abstention-gap]] · [[abstention]] · Commitment

[^c1]: oh-2026 — "RLVR improves recall but not calibrated abstention under our reward design, leaving Cal at or below the base model."
[^c2]: oh-2026 — "RLVR directly and substantially improves answerable recall"
[^c3]: oh-2026 — "We interpret this as a reward-induced answering bias: since our outcome rewards directly target grounding and reasoning, attempting a grounded answer becomes the dominant signal even when the target persona is absent, so abstention is rarely reinforced."
