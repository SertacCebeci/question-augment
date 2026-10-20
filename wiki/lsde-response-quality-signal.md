---
description: "LSDE is an automated composite score of a chat response's quality — weighted normalized Length, Self-disclosure, Emotion intensity and Specificity — used live as an RL reward."
aliases: ["LSDE", "LSDE quality signal", "composite response quality score"]
sources: ["tang-2026-driven"]
---
# LSDE: a composite chat-response quality score

> Four separately-motivated survey-methodology indicators of "did this
> respondent give me something," folded into one linear score so a
> question-selecting policy can read it after every exchange.

## Definition / Mechanism

Tang (2026) defines LSDE as a weighted sum of four
normalized dimensions computed automatically after each chatbot
exchange: Length ($L_{norm}$, word count capped at the corpus's 75th
percentile), Self-disclosure ($D_{norm}$, first-person pronoun count,
capped), Emotion ($E_{norm}$, the absolute value of a VADER sentiment
compound score), and Specificity ($S_{norm}$, a 0–3 count of whether the
response names an entity, a time and a place, via GPT-4o classification).
"We developed a four-dimensional quality metric (Length, Specificity,
Self-disclosure, and Emotion; LSDE) that captures distinct aspects of
engagement," combined as $Q_{composite} = 0.20L_{norm} + 0.20D_{norm} +
0.35E_{norm} + 0.25S_{norm}$, with weights chosen to offset the strong
correlation between Length, Disclosure and Emotion (r = 0.52–0.86) rather
than fit to any downstream outcome.[^c1]

On the validating corpus (N = 467 exchanges), "scores spanned the full
[0, 1] range (mean = 0.328, SD = 0.276), indicating broad variability and
confirming that the metric captures meaningful differences in engagement
levels."[^c2]

Specificity is the sparsest component: "Specificity is extremely sparse
in our data (88.7% of responses have $S_{total} = 0$, Q75 = 0)."[^c3]

## Why it matters

LSDE is used as the reward and state signal for [[aura-adaptive-followup-rl|AURA]]'s
online follow-up-type selection: a real-time, automatable stand-in for
"was that answer any good" that needs no human coder and no explicit
information-theoretic objective — an alternative route to the same
question that [[expected-information-gain|EIG]] and [[semantic-entropy]]
answer with a distributional or [[entropy]] computation instead of a linear
composite of surface features.

## Transfer

| | |
|---|---|
| **In its home field** | Survey methodology and social psychology: response length as investment, first-person pronoun counts as self-disclosure, sentiment magnitude (Russell's circumplex) as emotional intensity, and episodic-memory entity/temporal/spatial markers as specificity — separate, individually validated constructs, usually scored post hoc by human coders. |
| **Here** | The four are computed automatically after every exchange and combined into one linear score, live, to drive an online reward. |
| **What survives** | Each dimension's individual motivation from its home literature, and — on this one corpus — the composite's full-range spread and internal correlation structure. |
| **What does not** | Any claim that the composite tracks an answer's downstream *usefulness*. The weights were fit to offset in-corpus correlation and preserve empirical spread, not to any outcome the answer was meant to serve, and the paper's own limitations note flags this directly. |

## Limits

- Weights (0.20/0.20/0.35/0.25) and category thresholds (e.g. the
  low/medium/high quality bounds, the $|\Delta Q| > 0.05$ "improving"
  threshold) were calibrated on this one N = 467 campus-climate corpus
  and not shown to transfer to another domain or language.
- Specificity's near-total sparsity (88.7% zero) on the validating data
  means most of the composite's observed spread is carried by Length,
  Disclosure and Emotion, which the paper itself reports as highly
  correlated (r = 0.52–0.86) — the fourth term may add little beyond a
  single elaboration measure on this corpus.
- Validated by distributional spread and correlation structure only, not
  against an external ground truth of informativeness: "AURA's
  exploration can be locally suboptimal in early exchanges and LSDE is a
  proxy that may reflect dataset biases."[^c4]

## Related

[[aura-adaptive-followup-rl]] · [[expected-information-gain]] · [[semantic-entropy]] · [[value-of-information]]

[^c1]: tang-2026-driven — "We developed a four-dimensional quality metric (Length, Specificity, Self-disclosure, and Emotion; LSDE) that captures distinct aspects of engagement"
[^c2]: tang-2026-driven
[^c3]: tang-2026-driven — "Specificity is extremely sparse in our data (88.7% of responses have Stotal = 0, Q75 = 0)."
[^c4]: tang-2026-driven — "AURA’s exploration can be locally suboptimal in early exchanges and LSDE is a proxy that may reflect dataset biases."
