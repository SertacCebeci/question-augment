---
description: "Qwen3-4B's overconfidence rate on identical logical-inference items depends heavily on how uncertainty must be expressed — worst for a numeric 1-5 confidence score, best for a free verbal hedge."
aliases: []
sources: ["mazzaccara-2026"]
---
# Expression-format overconfidence gap

> The same model, on the same 300 items it should hedge on, is not equally
> overconfident in every format it can hedge in — asking it to pick a number
> is the worst way to find out what it knows.

## Definition / Mechanism

Mazzaccara, Bertolazzi & Bernardi (2026) test Qwen3-4B
on 450 controlled logical-inference stories (300 where the evidence
licenses only "might", 150 where it licenses assertion), in three separate
formats for expressing the answer: a free verbal epistemic marker, a binary
[[abstention]] option ("I don't know"), and a 1–5 numeric confidence score. On
the uncertainty-licensing items, the model wrongly "expresses certainty in
14%, 27%, and 80% of cases in the verbal, abstention, and numeric settings,
respectively. This tendency towards overconfidence is particularly
pronounced in the numeric confidence setting, i.e., the model tends to
state '5' (certain) in all scenarios."[^c1]

Token-probability mass confirms the ranking is not an artifact of the
certain/uncertain labeling rule used to score each format: "in uncertainty
scenarios it concentrates near one for the verbal setting, splits between
the two extremes for abstention" — i.e. the numeric format is worst by both
the label-matching accuracy metric and by the underlying probability
distribution over tokens.[^c2]

## Limits

- One model (Qwen3-4B) and one controlled-story dataset (from Li et al.
  2025, reframed as open-ended QA); the paper does not test whether the
  ranking of formats holds for other models or more naturalistic questions.
- The verbal-marker judgments depend on an LLM-as-judge (Claude Haiku)
  labeling free text as certain/uncertain, an extra measurement step the
  binary-abstention and numeric-score formats do not need — some of the
  verbal format's apparent advantage could be judge leniency rather than
  better-calibrated generation.
- The three formats differ in more than surface form (a numeric scale
  forces a forced-choice among five discrete points, with no "3" reachable
  mid-scale as a genuine hedge if the model's default is 5); the paper does
  not isolate which structural feature of the numeric format drives the
  gap.

## Related

[[calibration]] · [[abstention]] · [[certainty-default-sparse-override]]

[^c1]: mazzaccara-2026
[^c2]: mazzaccara-2026 — "in uncertainty scenarios it concentrates near one for the verbal setting, splits between the two extremes for abstention"
