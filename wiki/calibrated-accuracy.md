---
description: "An item-weighted benchmark accuracy that equally scores correct grounding on answerable queries and correct abstention on absent-persona queries, separating calibration from recall."
aliases: ["Cal", "Calibrated Accuracy"]
sources: ["oh-2026"]
---
# Calibrated Accuracy (Cal)

> A recall score can be high while an answerer hallucinates on every query
> where the target is missing; Cal forces the two failure modes into one
> number so neither can hide behind the other.

## Definition / Mechanism

Oh et al. (2026) build Cal into the Omni-Persona benchmark
because "recall alone cannot capture hallucination and over-[[abstention]], we
employ Calibrated accuracy (Cal) as our primary metric, equally scoring
correct grounding for answerable items and correct abstention for
absent-persona items."[^c1]

Mechanically, "Our primary metric is the item-weighted accuracy over all
queries" — Cal is a weighted average of Answerable Recall (Ans) and
Unanswerable Recall (Unans) by their item counts; "Answerable Recall (Ans)
is evaluated for binary correctness using an LLM-as-a-judge GPT-5.4-mini,
while Unanswerable Recall (Unans) is measured via abstention-keyword
matching (Chen et al., 2024)."[^c2]

Applied across closed- and open-source models, the metric separates two
things recall alone conflates: "The Cal score exposes a sharp divide that
recall alone hides. No closed-source model achieves both strong grounding
and reliable abstention."[^c3]

## Why it matters

On stall 10 (how much to commit, and how to say the rest), Cal is a
single-number instrument for exactly the failure a recall-only benchmark
cannot show: an answerer that is good at grounding when the target is
present but never declines when it is absent looks strong on recall and
fails on Cal. It makes "willing to decline" a scored, comparable property
of an answerer rather than a qualitative footnote.

## Limits

- Ans is judged by an LLM-as-judge and Unans by keyword matching for
  abstention phrases — both are proxies, not ground truth, and the paper's
  own companion "Anti-Hallucination Accuracy" metrics (1−FA, TA) exist
  because item-weighting Cal alone can be inflated by blanket abstention
  without those metrics tracking the split separately.
- Cal is a single operating point (the model's own decision boundary for
  answering vs. abstaining), not a swept threshold — it reports one
  accuracy number, not a curve.
- Defined only for this benchmark's construction of "unanswerable" (a
  ground-truth persona removed from the retrieved context); it does not
  generalise to abstention triggered by other kinds of uncertainty.

## Related

[[abstention]] · [[detection-to-abstention-gap]] · [[calibration]] · Commitment

[^c1]: oh-2026 — "recall alone cannot capture hallucination and over-abstention, we employ Calibrated accuracy (Cal) as our primary metric, equally scoring correct grounding for answerable items and correct abstention for absent-persona items."
[^c2]: oh-2026 — "Our primary metric is the item-weighted accuracy over all queries"
[^c3]: oh-2026 — "The Cal score exposes a sharp divide that recall alone hides. No closedsource model achieves both strong grounding and reliable abstention."
