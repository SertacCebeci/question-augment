---
description: "Structurally separating a concept bottleneck's uncertainty into epistemic and aleatoric by deriving each from different parameters, then routing on both."
aliases: ["CREDENCE", "Credal Ensemble Concept Estimation", "credal concept bottleneck model"]
sources: ["arxiv-2604-24170"]
---
# Credal concept bottleneck decomposition

> A concept is uncertain for one of two reasons — the model hasn't learned enough, or the input genuinely admits no single answer — and only a mechanism that cannot let the two collapse into one score can tell them apart.

## Definition / Mechanism

A Concept Bottleneck Model routes a prediction through human-interpretable
concepts (e.g. "expresses praise for service") before the final label.
CREDENCE replaces each concept's point probability with a **credal interval**
and derives its two halves from structurally separate parameters so that
they cannot merge back into one number. A frozen encoder feeds $H$ diverse
concept heads (LoRA adapters at different ranks); the interval is the
min–max spread across heads, and a dedicated head, trained to predict
annotator disagreement when it is available, is read off independently:

```text
epistemic  U_epi = Var_h[ p_h^(k) ]   — spread across the H heads (model confusion)
aleatoric  U_ale = sigma_theta(h)      — a separate head's own output (input ambiguity)
```

"CREDENCE represents each concept as a credal prediction (a probability
interval), derives epistemic uncertainty from disagreement across diverse
concept heads, and estimates aleatoric uncertainty via a dedicated ambiguity
output trained to match annotator disagreement when available." Because the
two signals come from different parameters — ensemble variance versus a
head supervised on human disagreement — they cannot collapse into a single
conflated score by construction, unlike a point-probability CBM's one
number.[^c1]

## Why it matters

The two signals cross into a **four-quadrant routing rule** rather than one
threshold on one number: "automate low-uncertainty cases, prioritize data
collection for high-epistemic cases, route high-aleatoric cases to human
review, and abstain when both are high." On CEBaB the quadrants carry
measured, and different, accuracy deltas:

| Quadrant | Epistemic / Aleatoric | ∆Acc | Action |
|---|---|---|---|
| TRUST | low / low | +78.8% | automate |
| DATA | high / low | +56.6% | collect training data |
| REVIEW | low / high | +85.7% | route to human — not because the model is wrong |
| ABSTAIN | high / high | +65.3% | decline or escalate |

The split is validated, not assumed: epistemic uncertainty is "positively
associated with prediction errors" across every dataset tested, while
aleatoric "closely tracks annotator disagreement" — $\rho_{ale} =
0.742$–$0.785$ for CREDENCE against a best baseline (a point-probability
ensemble) of $0.356$ — and the correlation rises with the concept's own
share of "unknown" annotator labels (Food 25%/$\rho{=}0.72$ → Noise
75%/$\rho{=}0.83$). On a dataset with no disagreement labels (SST-2),
aleatoric shows no association with error at all, which the authors read
as confirming the two signals measure different things rather than one
uncertainty under two names. Downstream, correcting the concepts with
highest aleatoric uncertainty recovers far more accuracy than correcting
the highest-epistemic ones (+18.9% vs. +4.3% mean, a 4.4× ratio), because
high-aleatoric concepts are the ones annotators disagree on precisely
because they are decision-relevant, while high-epistemic concepts are
often rare patterns weakly tied to the label.[^c5]

## Transfer

| | |
|---|---|
| **Home field** | classifier-ensemble aleatoric/epistemic decomposition (Shaker & Hüllermeier 2020) and set-valued, interval-valued (credal) prediction (Sale et al. 2023) |
| **Here** | pushed down from the label to the intermediate concept layer of a CBM, with the two terms forced apart by giving them different parameters rather than estimating both from one posterior |
| **What survives** | the reducible/irreducible distinction as an action rule, and the interval (not point) representation of a concept's probability |
| **What does not** | the aleatoric half is only as good as its supervision — where no annotator-disagreement label exists (SST-2), it has nothing to track and the correlation is null, not a measured ambiguity |

## Limits

- Requires concept-level annotations to train the heads, and aleatoric
  uncertainty specifically requires annotator-disagreement labels to
  supervise the dedicated head; without them the aleatoric signal is
  unverified as a general-purpose ambiguity measure, only demonstrated
  where CEBaB's "unknown" labels exist.
- "Correlations in epistemic error are moderate (ρ ≈ 0.3), indicating that
  boundary mistakes are influenced by both forms of uncertainty" — the
  four-quadrant rule does not cleanly separate all error cases.[^c6]
- Ensemble inference costs an extra $H\times$ forward passes (parallelizable).
- Evaluated only on text classification (sentiment, emotion, toxicity),
  not on generation or agentic settings; the authors name this as future
  work, not a result.
- The min–max credal interval is a conservative bound over $H$ heads, not
  a calibrated confidence region; its coverage properties are not measured.

## Related

[[uncertainty-decomposition]] · [[abstention]] · [[conformal-prediction]] · [[calibration]]

[^c1]: arxiv-2604-24170 — "CREDENCE represents each concept as a credal prediction (a probability interval), derives epistemic uncertainty from disagreement across diverse concept heads, and estimates aleatoric uncertainty via a dedicated ambiguity output trained to match annotator disagreement when available."
[^c5]: arxiv-2604-24170 — "prioritize correcting concepts with high aleatoric uncertainty. These are the concepts where human input provides maximum information gain."
[^c6]: arxiv-2604-24170 — "Correlations in epistemic error are moderate (ρ ≈ 0.3), indicating that boundary mistakes are influenced by both forms of uncertainty."
