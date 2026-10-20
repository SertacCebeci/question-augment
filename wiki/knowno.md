---
description: "KnowNo forms a conformal-prediction candidate set from an LLM planner's confidences and asks a human for help exactly when that set is not a singleton."
aliases: ["KnowNo", "KNOWNO", "Know When You Don't Know"]
sources: ["ren-2023"]
---
# KnowNo

> A robot that asks "plastic or metal?" instead of guessing: conformal
> prediction turns an LLM's raw confidence into a candidate set, and the
> set's size — not a hand-tuned threshold — is the trigger to ask.

## Definition / Mechanism

Given a language instruction and the robot's observations, KnowNo prompts
the LLM to generate a small labelled set of candidate next steps
(multiple-choice Q&A), then scores each candidate with the LLM's own
next-token confidence. Ren et al. (2023) apply conformal
prediction (CP) to these confidences: a [[calibration]] set of labelled
scenarios sets a quantile threshold so the resulting prediction set
contains the true candidate with probability at least $1-\epsilon$. If the
prediction set is a singleton the robot acts; otherwise it asks a human to
choose among the candidates in the set. If the prediction set is a
non-singleton, the robot leverages help from a human (or any[^c1]

Proposition 1 (single-step): with probability $1-\delta$ over the sampling
of the calibration set, the task completion rate over new test scenarios
is at least $1-\epsilon$; if the confidence scores model true conditional
probabilities, the average prediction-set size is the smallest among all
schemes achieving that completion rate.[^c2]

A multi-step extension — lifting calibration to whole action sequences and
causally reconstructing the set at each timestep — carries the same
guarantee across a full plan; it is a distinct technical contribution,
covered in [[sequence-level-conformal-prediction]].

## Known as

| Field | Name there | Relation |
|---|---|---|
| Robotics / LLM planning (Ren et al. 2023) | KnowNo / KNOWNO | exact |
| Robotics / LLM planning (Ren et al. 2023) | Know When You Don't Know (the acronym's expansion) | exact |

## Why it matters

KnowNo makes "ask iff the candidate set is not a singleton" a calibrated
decision rather than a tuned confidence cutoff: the trigger threshold is
set once, from held-out data, to hit a user-declared completion rate, and
the coverage guarantee is distribution-free — it needs no assumption about
how well-calibrated the LLM's raw confidence is (only the set-size
*minimality* result needs that assumption). This gives map-2's "ask only
if it matters" criteria a distribution-free trigger that ships with a
numeric guarantee instead of a rule of thumb.

## Transfer

| | |
|---|---|
| **In its home field** | Conformal prediction: a calibration set of i.i.d. labelled examples sets a quantile on nonconformity scores, giving a distribution-free, finite-sample coverage guarantee for a prediction set (statistics/ML) |
| **Here** | The calibration set is labelled robot scenarios; the prediction set is a set of candidate next-step plans; a non-singleton set is read as "ask a human" |
| **What survives** | The finite-sample coverage guarantee itself, and its independence from whether the LLM's raw confidence is well-calibrated |
| **What does not** | Minimality of the prediction set (needs $\hat f$ to model true conditional probabilities); and validity requires the human's answer to be correct whenever it is possible — Ren et al. (2023) assume accurate human help, and an inaccurate human breaks the completion-rate guarantee silently |

## Limits

- The guarantee is conditional on the calibration set being i.i.d. from the
  same distribution as deployment; distribution shift between calibration
  and test scenarios is not covered.
- Requires the correct option to be among the LLM-generated candidates
  (realizability): if the true next step is never in the label set, no
  prediction set can cover it.
- Assumes accurate human help: a human who answers incorrectly when asked
  breaks the task-completion guarantee (Proposition 1's proof).
- The minimal-set-size result is conditional on the LLM confidence
  modelling true conditional probabilities — an assumption the paper
  itself flags as an approximation for LLMs, not a verified property.

## Related

[[value-of-information]] · [[clarification-benchmarks]] · [[conformal-test-martingale]] · [[sequence-level-conformal-prediction]]

[^c1]: ren-2023 — "If the prediction set is a non-singleton, the robot leverages help from a human (or any"
[^c2]: ren-2023 — "probability 1−δ over the sampling of the calibration set, the task completion rate over new test scenarios"
