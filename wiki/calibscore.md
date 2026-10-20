---
description: "A single number combining an agent's clarification recall on ambiguous tasks with its restraint on fully specified ones, so over-asking and under-asking are scored together."
aliases: ["CalibScore"]
sources: ["stoisser-2026"]
---
# CalibScore

> Asking well is two failure directions at once — asking when nothing is
> missing, and not asking when something is — and this metric refuses to
> let a model trade one for the other and call it calibrated.

## Definition / Mechanism

Stoisser et al. (2026) define CalibScore for Ambig-DS
from two rates measured under a fixed ask-or-act policy: Ask on Ambig.,
the fraction of ambiguous, decision-relevant tasks on which the agent
asks its one permitted clarifying question (clarification recall, where
asking is preferred), and Ask on Full, the fraction of fully specified
tasks on which it asks anyway (unnecessary clarification, where acting
without asking is preferred). "CalibScore combines both into a single
[[calibration]] metric: CalibScore = 2·AskOnAmbig·(1 − AskOnFull)/(AskOnAmbig
+ (1 − AskOnFull)), where 1.00 denotes perfect calibration." Across the
five models and two tested prompt policies (permissive: ask exactly one
question or write NONE; conservative: the same, plus an instruction to
ask only when the task cannot be solved from the prompt and data), no
model–policy combination achieved consistent calibration on both of the
benchmark's two independently analyzed [[efe-planning-as-variational-inference|ambiguity]] axes — a policy that
scores well on one axis fails on the other.[^c1]

## Why it matters

CalibScore separates a system's ability to *use* a clarifying question,
once offered, from its ability to *know when to reach for one* — the
decision this wiki's stall 2 is about. Ambig-DS shows the two can come
apart sharply: under the conservative policy, Gemini 3.1 Pro asks on 94%
of ambiguous target-ambiguity tasks and 0% of fully specified ones (near
1.00), while on the objective-ambiguity axis the same class of policy
collapses recall to 5% (Claude Haiku 4.5) or 0% (GPT-5.4 Nano, GPT-5.4) —
the same instruction that calibrates one axis silences asking on the
other. The permissive policy trades this the other way: high recall on
ambiguous tasks bought with high false-positive asking on tasks that
needed none. Neither prompt policy substitutes for a model that can tell,
per instance, whether the observation before it is underdetermined.[^c2]

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | Binary classification: the F1 score is the harmonic mean of precision and recall, so a classifier cannot buy a high score by trading one to zero for the other | CalibScore is the harmonic mean of Ask-on-Ambig. (a recall: of the tasks that need asking, how many get asked) and $1-$Ask-on-Full (a specificity: of the tasks that need no question, how many are left alone) |
| What survives | The harmonic mean's refusal to average away a collapse in either component — a 0 in either term drives the score to 0 | Unchanged: a policy that never over-asks but also never asks on ambiguous tasks scores 0, exactly as recall-blind precision would in F1 |
| What does not | F1 is computed over a fixed, pre-labeled test set with one ground-truth positive/negative label per item and no policy choice by the scorer | The two rates come from two different task populations (ambiguous vs. fully specified) scored under a policy the agent itself was given as a prompt, so CalibScore mixes a within-condition recall with a between-condition specificity rather than one confusion matrix over one population |

## Limits

Rests on one benchmark, two discrete prompt policies (permissive,
conservative) bracketing but not sweeping the operating range, and five
models — the claim that no combination is well-calibrated is over
5 models × 2 policies × 2 suites = 20 cells, not a sweep over prompt
space or trained classifiers. The two axes (target, objective) are
confounded with their source benchmarks (DSBench, MLE-bench), so a
metric value is not yet shown to transfer to a third ambiguity axis or a
system trained (rather than prompted) to decide when to ask. Unverified
beyond Stoisser et al. (2026) [?].

## Related

[[clarification-benchmarks]] · [[clarification-need-predictor-parity]] · [[query-clarification-rate]] · [[value-of-information]]

[^c1]: stoisser-2026 — "CalibScore combines both into a single calibration metric: CalibScore = 2·AskOnAmbig·"
[^c2]: stoisser-2026 — "model–policy combinations approach good calibration (e.g., Gemini 3.1 Pro under the conservative"
