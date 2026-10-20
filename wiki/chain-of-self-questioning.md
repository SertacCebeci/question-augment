---
description: "A prompt-only three-stage LLM method that decomposes a question into required information units, scores support for each, and gates commitment on a tunable threshold."
aliases: ["Chain-of-Self-Questioning", "CoSQ", "Grounded-CoSQ", "Critical-CoSQ", "Adaptive-CoSQ"]
sources: ["senol-2026"]
---
# Chain-of-Self-Questioning

> Before an LLM commits to an answer, make it name what it would need to know,
> score whether it has that support, and only then decide to answer or abstain
> — three prompts instead of one, with the gate explicit at every step.

## Definition / Mechanism

Şenol (2026) defines **Chain-of-Self-Questioning (CoSQ)** as a model-agnostic,
prompt-only three-stage framework: (1) given question $q$, the model
constructs the required information units $I(q) = \{i_1, \dots, i_m\}$; (2) it
assigns each unit a confidence score $s_j \in [0,1]$; (3) a decision rule
gates commitment on those scores, and only accepted units are passed to the
final answer-generation prompt.[^c1]

Three variants apply different gates to the same two-stage decomposition.
**Grounded-CoSQ** commits when the mean item score $\bar s(q) =
\frac{1}{m}\sum_j s_j \geq \tau$. **Critical-CoSQ** first labels each unit
critical or supporting and gates only on the mean of critical-unit scores.
**Adaptive-CoSQ** applies three simultaneous checks — overall mean $\geq
\tau$, critical-claim mean $\geq 0.65$, minimum critical-claim confidence
$\geq 0.40$ — and additionally re-checks the generated answer for
contradiction, abstaining if one is found. $\tau$ is swept over $\{0.50,
0.60, 0.70, 0.80, 0.90\}$ in all three variants.[^c2]

On the 817-item TruthfulQA multiple-choice set, across eleven open-weight and
hosted model families, Grounded-CoSQ at $\tau=0.90$ reduces the mean
unconditional wrong-commitment rate (questions answered incorrectly, as a
fraction of all questions) from 13.1% under chain-of-thought prompting to
8.9% — a 32.1% relative reduction — while raising answered accuracy from
86.9% to 89.7% and still answering 87.6% of questions; both the
wrong-commitment reduction and the accuracy increase hold for all eleven
models at every evaluated threshold.[^c3]

## Why it matters

CoSQ operationalizes "does the answerer have enough to commit" as a
per-question, per-information-unit score computed *before* the answer is
generated, rather than as a post-hoc confidence attached to an already-produced
answer (the usual order for [[calibration]] and self-consistency methods). The
threshold $\tau$ is an explicit, swept operating parameter on a
risk–coverage frontier, not a calibrated probability — the paper is explicit
that the elicited signal is a behavioral, selective one, not a claim of
introspective access.[^c4]

## Transfer

| | |
|---|---|
| In its home field | LLM question answering, black-box or hosted models, prompt-only intervention, evaluated on multiple-choice and short-answer benchmarks with a gold label |
| Here | any answerer deciding whether to commit to a value for a constraint before returning it |
| What survives | the decomposition of a question into the information units its answer depends on, scoring support per-unit rather than for the answer as a whole, and gating commitment on an explicit, swept threshold |
| What does not | the specific thresholds (0.65, 0.40, $\tau=0.90$) and the measured reduction — both are fit to TruthfulQA-MC and this model panel; nothing in the paper establishes the per-unit scores as calibrated probabilities transferable to another task |

[^c5]

## Limits

- The reported wrong-commitment reduction rests on the 817-item
  TruthfulQA-MC balanced-option protocol and this eleven-model panel; a
  secondary Natural Questions Short-Answer evaluation is reported as
  convergent but exploratory, so the claim above generalizes only as far as
  those two benchmarks establish.[^c6]
- The per-unit confidence scores $s_j$ are elicited from the same model that
  will answer, with no external verification of whether an accepted unit is
  actually correct — the paper treats the score as an empirical operating
  parameter, not a calibrated probability, so a threshold tuned on one task
  is not a guaranteed threshold on another (the same limit [[abstention]]
  names for any black-box uncertainty score).[^c7]

## Related

[[abstention]] · Commitment · Selection

[^c1]: senol-2026 — "Given a question q, the model first constructs information units I(q) = {i1 , . . . , im }. It then assigns a confidence score sj ∈ [0, 1] to each unit. A decision rule determines whether the model is allowed to commit."
[^c2]: senol-2026 — "The system commits when s̄(q) ≥ τ and abstains otherwise."
[^c3]: senol-2026 — "Grounded-CoSQ at τ = 0.90 reduces the mean unconditional wrong-commitment rate from 13.1% under chain-of-thought prompting to 8.9%, a 32.1% relative reduction, while increasing answered accuracy from 86.9% to 89.7% and answering 87.6% of questions. Both improvements hold for all eleven models and at every evaluated threshold."
[^c4]: senol-2026 — "The confidence threshold is not treated as a calibrated probability; it is an empirical operating parameter that determines a point on a risk–coverage frontier."
[^c6]: senol-2026 — "The study also includes a 300-question exploratory Natural Questions Short-Answer (NQShort) evaluation based on the Natural Questions benchmark [15]. NQ-Short is reported in the main Results section as a secondary generalization test."
[^c7]: senol-2026 — "The confidence threshold is not treated as a calibrated probability; it is an empirical operating parameter that determines a point on a risk–coverage frontier."
[^c5]: senol-2026
