---
description: "Scoring how much of what mattered actually came back, as a recall fraction Gupta et al. (2026) score a generated video caption with two checklist-recall metrics,"
aliases: []
sources: ["gupta-2026"]
---
# Dual-judge completeness recall

> Scoring how much of what mattered actually came back, as a recall fraction
> against a checklist — read by two independent judges instead of one.

## Mechanism

Gupta et al. (2026) score a generated video caption with two checklist-recall[^s1]
metrics, each in $[0,1]$:

```text
completeness      = (# important narrative events included) / (# important narrative events on the checklist)
visual enrichment = (# visual details included)             / (# visual details on the checklist)
```

These are two separately scored quantities on two different checklists —
narrative events versus visual detail — not two names for one score; the
paper reports them with different numbers for the same caption (e.g. 0.62
completeness against 0.61 visual enrichment for one configuration, 0.58
against 0.63 for another). Both checklists are scored by two independently
run LLM judges (Gemini and DeepSeek) rather than one, and the two judges'
scores are averaged. A third metric, factual accuracy — whether what is
included is actually grounded in the video — is scored by human raters
instead.

## Why it matters

Stall 5's empty-cells table names "LLM-as-judge: automatic
scoring of answers" as an open question — a way to score whether a returned
answer is a usable constraint without a human rating every item. This is a
working instance of that: a recall fraction against a named, enumerable
checklist, computed twice by two different judge models and averaged so
that no single model's blind spots set the whole score. It also gives an
asker a per-item accounting of what is still missing — the checklist entries
not yet included — rather than only a scalar quality judgement, which is
closer to a stopping signal than to a pass/fail check.

## Transfer

| | |
|---|---|
| **In its home field** | Recall, from information retrieval and detection theory: true positives over actual positives, ordinarily computed against a fixed, exactly-matchable ground-truth set. |
| **Here** | The "positive" is a checklist item worded in natural language, and "included" is not an exact match but an LLM judge's semantic decision that the caption covers it. |
| **What survives** | The recall framing — a fraction of a named, enumerable set of relevant items — and using more than one assessor to reduce dependence on any single rater's bias. |
| **What does not** | A checkable ground truth. Nothing in the reported method verifies that the checklist itself is complete, or that either judge's inclusion calls are correct rather than merely similar to each other; no inter-judge agreement figure is reported, so averaging two judges is shown to reduce dependence on one model, not shown to reduce error. |

## Limits

- No human annotation of completeness or visual enrichment is reported —
  only factual accuracy is human-scored. This metric is two LLMs checking
  the same kind of thing, not a human-verified count.
- The checklists' own construction — who or what decided a given event or
  visual detail was "important" enough to include — is not described in the
  material read for this note; a narrower or more generous checklist would
  move the score without any change in caption quality.
- Reported on one domain (359 BWC clips) with one specific judge pair
  (Gemini, DeepSeek); whether the averaging behaves the same with a
  different pair of judges is untested.

## Related

[[probe-question-video-captioning]] · [[semantic-entropy]] · [[calibration]] · [[format-restriction-effect]]

[^s1]: gupta-2026
