---
description: "LLMs generating multiple-choice questions place the correct answer in a model-specific, non-uniform position, a bias encoded in the question stem's hidden states before the options are written."
aliases: ["position bias in MCQ generation", "answer-position planning", "implicit positional planning"]
sources: ["tang-2026-large"]
---
# MCQ answer-position bias

> When an LLM authors a multiple-choice item rather than answering one, the
> position it assigns the correct option is not incidental: it is a
> generation choice the model has already made by the end of the question
> stem, before the options exist on the page.

## Definition / Mechanism

Tang, Duan & Cai (2026) test 10 LLMs and 5 VLMs on three
MCQ-generation tasks (knowledge items, reading-comprehension items,
vision-language items) and find the correct-answer position is far from the
25% uniform baseline, with the skew tied to model family — LLaMA models favor
option "A", Qwen3 and DeepSeek variants favor "B", Gemini models favor "B"
and "C", and option "D" is underrepresented almost everywhere.[^c1]

The bias survives removing explicit option identifiers (A/B/C/D) — models
still skew, and more strongly toward the first position, when asked to
generate four unordered candidate answers instead — so it is not just an
artifact of the identifier tokens.[^c2]

Probing the question stem's hidden states (before the options are decoded)
with a classifier trained to predict the eventual answer-position label
beats majority and random baselines across all tested models, and the
signal is distributed across many layers rather than confined to the top —
evidence that the position is implicitly decided during stem generation,
not chosen afterward.[^c3]

Activation steering confirms the encoding is causal, not merely
correlational: adding a mean-difference direction (computed from the hidden
states of items whose answer was "A" vs items whose answer was "B") to the
stem's penultimate-token representation at intermediate layers shifts
Llama-3.2-3B-Instruct's A→B answer rate by up to 22% at the best layer,
substantially more than a magnitude-matched random direction (which
plateaus around 8-10%).[^c4]

## Why it matters

A benchmark built by prompting an LLM to author its own MCQs (a common
recipe for scaling question-generation datasets) inherits this bias for
free: the correct answer is not where the model says it is by chance, it is
where the model's stem-generation dynamics already committed to putting it.
Any downstream use of such a benchmark to measure answer-selection bias, or
any pipeline that uses one LLM to generate quiz items another is graded on,
carries this artifact silently unless option order is explicit and checked.[^c5]

## Transfer

| | Home field (mechanistic interpretability) | Here (MCQ generation) | What survives | What does not |
|---|---|---|---|---|
| Formalism | probing classifiers + activation steering (mean-difference / classifier-based direction) on hidden states, established for next-token and future-content planning | applied to the answer-position label of a not-yet-written multiple-choice item | the causal test (probe finds a signal, steering moves the outcome) is unchanged | the paper's own steering only partially controls the outcome and degrades question semantics at higher strength, so the technique is diagnostic here, not yet a reliable formulation control |

[^c6]

## Limits

The causal (steering) result is reported for a single model
(Llama-3.2-3B-Instruct) and a single target shift (A→B); the probing result
is broader (10 LLMs, 5 VLMs) but is correlational only, and both tasks are
capped at four options with an explicit "generate exactly one correct
answer" instruction, so the finding does not by itself establish how the
bias behaves for open-ended item generation or larger option sets.

## Related

[[item-writing-guidelines]]

[^c1]: tang-2026-large — "We observe consistent and structured positional biases across model families. LLaMA models consistently favor option “A” in K-MCQ and VL-MCQ settings. In contrast, Qwen3 and DeepSeek variants tend to prefer option “B”, while Gemini models more frequently assign correct answers to options “B” and “C”. Across nearly all models and tasks, option “D” is systematically underrepresented."
[^c2]: tang-2026-large — "We observe a consistent shift toward the first position across models in the identifier-free setting."
[^c3]: tang-2026-large — "Across all models, both metrics consistently exceed random and majority baselines, indicating that hidden representations in the question stem encode predictive signals of the correct answer position."
[^c4]: tang-2026-large — "the mean-difference method exhibits a stable, monotonic increase in the A→B shift, reaching 22.2% at α = 400. In contrast, random vectors show high variance at small α due to directional instability, and plateau at around 8–10% for larger α"
[^c5]: tang-2026-large — "To investigate the underlying mechanisms, we conduct probing experiments and find that hidden representations in the question stem encode predictive signals of the correct answer position, suggesting that answer position may be implicitly planned during generation."
[^c6]: tang-2026-large
