---
description: "A model predicts, before generating its response, the score an external LLM-judge would give that response — a pre-hoc self-estimate meant to trigger routing to a larger model."
aliases: ["PA paradigm", "RPRA paradigm", "Predict-Answer/Act", "Reason-Predict-Reason-Answer/Act", "report card", "pre-hoc judge prediction"]
sources: ["arxiv-2604-12634"]
---
# Judge-score self-prediction

> Before a model answers, it first guesses the grade an outside judge would give the answer — and that guess, not the answer's own confidence, is what should decide whether to answer at all.

## Definition / Mechanism

Ashley, Le Lan, Zhao et al. (2026) name two paradigms for a model estimating, prior to responding, how an [[abstention|external]] LLM-or-agentic judge would score its output: "Predict-Answer/Act (PA), where a model predicts how a judge would score its response before generating it, and Reason-Predict-Reason-Answer/Act (RPRA), which extends PA by having the model reason before predicting and again before responding."[^c1]

The predicted score is the trigger for a routing decision, not an end in itself: "a PA/RPRA model could directly respond to queries it is confident it can answer well, and trigger routing to a larger model otherwise." The judge itself is a separate, costlier LLM/agentic evaluator scoring "great," "ok," or "bad," so the mechanism substitutes a cheap self-estimate of that judge's verdict for running the judge (or the larger model) on every query.[^c2]

Zero-shot self-prediction is unreliable in exactly the regime that matters most: "reasoning models exhibited an often better ability to estimate their own performance" while "smaller models typically performed at or worse than a random guess accuracy" — the models least able to answer well are also the ones least able to tell they can't.[^c3]

Two orthogonal fixes are evaluated, both aimed at the small-model failure. First, an in-context **report card**: "the mode of the scores for that model on that dataset" for every dataset the model has been judged on before, given to the model as context at prediction time. This closed most of the small-model gap: "the effect of the report card is particularly good on the smaller and non-reasoning models, enabling them to work in a PA paradigm." Second, fine-tuning without a report card, using a relabeling step borrowed from reinforcement learning: "we produced a dataset of zero-shot prompts and the respective zero-shot model evaluations... We then applied the hindsight trick... to relabel the zero-shot predictions as though they were accurate," then supervised-fine-tuned the model on the relabeled pairs.[^c4]

Across datasets, "report cards and fine-tuning [achieved] mean improvements of up to 55% and 52%... respectively" in self-prediction accuracy over zero-shot.[^c5]

## Why it matters

This is a distinct way of deciding whether an agent should act alone or defer: instead of thresholding the agent's own confidence or entropy on its answer (the usual abstention/escalation signal), the agent predicts a *third party's* verdict on an answer it has not yet committed to, and that forecast — sharpened by a report card or by fine-tuning — is what would gate the deferral. It decouples "does the model feel sure" from "would an external standard actually approve," which matters because the two can diverge (an overconfident small model is exactly the case a self-confidence threshold misses and a judge-forecast, once calibrated, can catch).

## Transfer

| | |
|---|---|
| **Home field** | Reinforcement learning: hindsight experience replay relabels a failed trajectory's target so it becomes a positive example of the goal it actually reached. |
| **Here** | A zero-shot self-prediction (whatever score the model happened to guess) is relabeled as the *correct* target for supervised fine-tuning, using the judge's real score, not the model's guess, as ground truth. |
| **What survives** | Turning a record of "what happened" into supervised training signal without new judge calls beyond the ones already collected. |
| **What does not** | HER's counterfactual-goal substitution (any reached state becomes a valid goal); here the relabeling target is a real evaluator's score, not a redefinition of the task. |

## Limits

The paper states plainly that it only establishes feasibility of the prediction step, not of the routing system it motivates: "this work focuses on establishing the feasibility of pre-hoc performance prediction rather than demonstrating the exact degree of improvement this would offer in deployment; evaluating complete routing systems that leverage these predictions to optimize cost-quality trade-offs in practice remains future work." So no claim here is about a measured downstream effect of asking/deferring on task accuracy or cost — only about how accurately a model can forecast a judge's score, before and after report-card or fine-tuning help. The report-card approach requires processing report-card tokens at every inference, offsetting some of the savings routing is meant to produce; the fine-tuned models tested are all non-reasoning, so they realize PA, not RPRA; and evaluation is single-turn, which the authors flag as possibly not generalizing to multi-turn deferral decisions.

## Related

[[confidence-calibrated-cascade-judgment]] · [[learned-deferral]] · [[calibration]] · [[abstention]] · [[bayesian-self-escalation]]

[^c1]: arxiv-2604-12634 — "We formalize this pre-hoc prediction of an LLM/agentic judge as two paradigms: Predict-Answer/Act (PA), where a model predicts how a judge would score its response before generating it, and Reason-Predict-Reason-Answer/Act (RPRA), which extends PA by having the model reason before predicting and again before responding."
[^c2]: arxiv-2604-12634 — "In practice, a PA/RPRA model could directly respond to queries it is confident it can answer well, and trigger routing to a larger model otherwise."
[^c3]: arxiv-2604-12634 — "reasoning models exhibited an often better ability to estimate their own performance, and (3) smaller models typically performed at or worse than a random guess accuracy."
[^c4]: arxiv-2604-12634 — "we produced a dataset of zero-shot prompts and the respective zero-shot model evaluations collected in Section 4. We then applied the hindsight trick (see, e.g., Andrychowicz et al. (2017)) to relabel the zero-shot predictions as though they were accurate."
[^c5]: arxiv-2604-12634 — "with report cards and fine-tuning achieving mean improvements of up to 55% and 52% across datasets, respectively."
