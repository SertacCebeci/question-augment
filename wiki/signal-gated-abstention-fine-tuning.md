---
description: "Fine-tuning an LLM to abstain using only its own frozen token-probability confidence as the training target matches label-supervised abstention-tuning at matched coverage."
aliases: ["signal-gated abstention fine-tuning", "label-free abstention fine-tuning", "C3 (Asaria et al. 2026)"]
sources: ["asaria-2026"]
---
# Signal-gated abstention fine-tuning

> Teaching a model when not to answer is usually paid for with correctness
> labels; the model's own frozen confidence, computed once and never
> checked against a right answer, buys the same behavior.

## Definition / Mechanism

Asaria, Salomone & Gandhi (2026) define a training-question
confidence $s(q)$ as the mean log-probability the frozen base model assigns
to its own greedily-decoded answer tokens, computed once before any
fine-tuning. Training questions are ranked by $s(q)$; the lowest-$s$
fraction (a coverage knob) gets the fixed target "I'm not sure," the rest
keep the model's own answer as a self-distillation target. The model is
then fine-tuned with LoRA ($r=16$) on this signal-only target — no
correctness label enters the procedure at any point.[^c1]

Compared head-to-head at matched coverage against R-Tuning-style
label-supervised [[abstention]]-tuning (abstain where the base model was
actually wrong, by gold-answer match) across six open-weights models
(Llama-3.2-1B/3B, Llama-3.1-8B, Qwen3-1.7B/4B/8B) on short-form factual QA
(PopQA, TriviaQA), judge-adjudicated hallucination rate showed overlapping
95% bootstrap confidence intervals on every model — no detected difference
between the label-free and label-supervised recipes (point-estimate
reduction ratio 0.95–1.10).[^c2]

An up-weighting control that drills the same low-signal questions harder
without retargeting them to abstention stayed at base hallucination,
isolating the source of the gain as [[calibration]] (learning where to
abstain) rather than memorization (learning the fact better).[^c3]

## Why it matters

This is a training-time, not inference-time, use of a confidence signal:
the frozen score decides which examples in the training set get retargeted
to abstention, and the behavior is then baked into the weights rather than
applied as an external gate at deployment. It shows the signal-quality
question ([[sequence-likelihood-confidence]]) and the "can this substitute
for labels" question are separable — a signal too weak to rank live
outputs for routing can still be strong enough, thresholded once over a
training set, to supervise which examples should be retargeted.

## Limits

- The comparison reported is a failure to detect a difference (overlapping
  confidence intervals on a 700-item test set), not a proven equivalence;
  the source itself proposes a formal equivalence test (TOST) as the
  needed next step.
- The blind spot is structural, not incidental: 36% of all items are
  answered-but-wrong with confidence high enough that the signal never
  flags them, so the method's calibration claim is specific to low-signal
  items, not a claim that fine-tuning removes hallucination overall.[^c4]
- Tested only on English short-form factual QA at ≤8B parameters, one
  judge model, and one confidence signal (mean log-probability; an energy
  signal substitute gave no gain); long-form generation and larger models
  are untested.

## Related

[[sequence-likelihood-confidence]] · [[abstention]] · [[calibration-training]] · [[semantic-entropy]] · [[post-hoc-abstention]]

[^c1]: asaria-2026 — "We fine-tune each model (with LoRA) to answer when its frozen confidence is high and to say “I’m not sure” when it is low, using the signal alone and no correctness labels."
[^c2]: asaria-2026 — "On every model the C2-vs-C3 95% bootstrap confidence intervals overlap, i.e. we do not detect a hallucination difference between the label-free and label-supervised methods."
[^c3]: asaria-2026 — "The up-weighting control (C4) stays at base hallucination with near-full coverage, whereas C3 reduces hallucination: drilling low-signal questions harder does nothing, while retargeting them to abstention helps."
[^c4]: asaria-2026 — "Second, and dominant, are confidently wrong answers: 36% of all items are answered-but-wrong with confidence high enough that the signal does not flag them, the bulk of the 39% answered-but-wrong residual."
