---
description: "ESR ranks a candidate diagnostic question by its expected reduction in severity-weighted terminal risk, not by entropy reduction alone, then distills the ranking into a language policy."
aliases: ["expected-severity-risk", "ESR"]
sources: ["li-2026-beyond"]
---
# Expected-severity-risk

> A proactive medical-dialogue agent ranks the next question not by how
> much it shrinks diagnostic uncertainty, but by how much it is expected to
> lower a severity-weighted measure of diagnostic error — because the most
> informative question and the one that matters most for the patient can
> differ.

## Definition / Mechanism

Li, Chen & Zhang (2026) observe that existing
information-seeking approaches commonly prioritize questions that most
reduce diagnostic uncertainty, but this criterion overlooks an important
property of medical diagnosis: different diagnostic errors can carry
substantially different consequences.[^c1]

They propose Expected-Severity-Risk (ESR), a consequence-aware
question-supervision objective that values each candidate by its expected
reduction in severity-aware terminal risk. Since a question must be
selected before its answer is known, the expected risk is marginalized
over possible answers using population statistics computed only from the
training set, not from a teacher model queried at decision time.[^c2]

The resulting per-question ranking is not used directly at inference: its
rankings are distilled into a prefix-only language policy, requiring no
teacher-side risk computation at deployment — so the trained dialogue
model reproduces the severity-aware ordering without recomputing risk
itself.[^c3]

## Why it matters

This is a direct answer to stall 2 — which axis first — for a domain where
[[value-of-information]] is normally blocked by the lack of a written
utility ([[expected-utility]]): here the utility is supplied by a clinical
severity label already in the training data, playing the role
[[sensitivity-weighted-question-score]] gives the solver's own objective in
operations research.

Across three matched Qwen3-4B training seeds on the DDxPlus dataset, ESR
reduces mean high-severity diagnostic miss from 0.0645 to 0.0455 (29.5%
relative reduction) and improves mean diagnostic accuracy from 0.9123 to
0.9320 while requiring only 0.14 additional questions per dialogue — the
severity-weighted objective does not trade accuracy for safety, and costs
almost no extra questions.[^c4]

## Transfer

| | |
|---|---|
| **In its home field** | statistical decision theory: expected (Bayes) risk weights each possible error by its cost, not just its probability |
| **Here** | rank the next diagnostic question, before its answer is known, by the expected drop in a severity-weighted terminal risk rather than by [[entropy]] reduction |
| **What survives** | the core move — that the value of a question should be priced by the downstream cost of the errors it prevents, not only by how much it narrows the hypothesis set |
| **What does not** | the abstract reports no regret bound or optimality guarantee for the distilled prefix-only policy relative to the full ESR ranking it approximates; whether the distillation step preserves any such guarantee is not stated |

## Limits

Read from the paper's abstract only — no archived full-text extract was
available for this cell, so the mechanism above is stated as ESR's authors
summarize it, not verified against the method section's formulas or the
DDxPlus severity labels' construction. Reported results are on a single
dataset (DDxPlus) and a single base model family (Qwen3-4B); no
cross-model or cross-dataset transfer is claimed in the abstract. Risk is
marginalized with train-only population statistics — an approximation
whose sensitivity to distribution shift between training and deployment
populations is not addressed here.

## Related

[[value-of-information]] · [[sensitivity-weighted-question-score]] · [[expected-information-gain]] · [[expected-utility]]

[^c1]: li-2026-beyond — "Existing information-seeking approaches commonly prioritize questions that most reduce diagnostic uncertainty, but this criterion overlooks an important property of medical diagnosis: different diagnostic errors can carry substantially different consequences."
[^c2]: li-2026-beyond — "We propose Expected-Severity-Risk (ESR), a consequence-aware question-supervision objective that values each candidate by its expected reduction in severity-aware terminal risk."
[^c3]: li-2026-beyond — "Its rankings are then distilled into a prefix-only language policy, requiring no teacher-side risk computation at deployment."
[^c4]: li-2026-beyond — "Across three matched Qwen3-4B training seeds on DDxPlus, ESR reduces mean high-severity diagnostic miss from 0.0645 to 0.0455 (29.5% relative reduction) and improves mean diagnostic accuracy from 0.9123 to 0.9320 while requiring only 0.14 additional questions per dialogue."
