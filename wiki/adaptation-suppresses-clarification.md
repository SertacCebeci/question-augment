---
description: "Domain-adaptation fine-tuning that raises task accuracy drives clarification-seeking toward zero across languages, and oversampling clarifying examples alone does not restore it."
aliases: ["clarification recall collapse"]
sources: ["albattra-2026"]
---
# Adaptation suppresses clarification

> Fine-tuning a model to be better at the task it was adapted for can, in the
> same run, make it stop asking — even when the training data included
> clarification examples.

## Definition / Mechanism

Albattra et al. (2026) adapt a multilingual instruction
model (Qwen3.5-9B-Instruct) with QLoRA on a women's-health communication
task and measure clarification recall — whether the model requests missing
information on a deliberately under-specified case — before and after
adaptation. The zero-shot baseline reaches 0.856 recall on English; after
structured English QLoRA it falls to 0.044, and adding 4× oversampling of
the clarification-positive class does not recover it: "clarification recall
falls from 0.856 (Model 1) to 0.044 (Model 2) and 0.000 (Models 3 and 4)."
Oversampling changes triage accuracy but not this rate.[^c1]

The collapse is not an English artifact: joint English–French–Arabic QLoRA
(Model 4) drives recall "to 0.000 in English and French and to 0.011 in
Arabic," while a separate, English-source risk-label collapse (see
[[under-triage]]) is concentrated in French and Arabic only — the two
failures move independently.[^c2]

Correcting the risk-label pipeline (Model 5, risk-corrected re-adaptation)
repairs the triage collapse but not this one: "clarification recall remains
0.000 in every language, so risk correction does not repair clarification
failure."[^c3]

## Why it matters

Every adapted configuration the paper tests — plain QLoRA, oversampled
QLoRA, joint multilingual QLoRA, and risk-corrected QLoRA — reaches
near-zero clarification recall while the zero-shot baseline reaches 0.856.
The authors read the null effect of oversampling as showing that mere
exposure to clarification-positive examples is not the fix: "clarification
may require an explicit training objective."[^c4]

For a practitioner adapting a model for a task, the standard move —
fine-tune on task-labelled data, even with the clarification class
oversampled — is evidenced here to actively remove the behaviour this
wiki's subject depends on, unless the training objective targets it
directly.

## Limits

- Measured on one model family (Qwen3.5-9B-Instruct) and one set of QLoRA
  configurations, in one domain (women's-health communication) and three
  languages; whether the effect generalises to other architectures, tasks,
  or adaptation methods (full fine-tuning, RLHF) is untested by this paper.
- The clarification target is mechanical — the deliberately under-specified
  form is positive and every other form negative — so the measured quantity
  is recognition of an injected information gap, not a clinician-adjudicated
  judgement of when clarification is clinically needed.
- No mechanism is isolated: the paper does not run an ablation separating
  "more task data" from "more task optimisation" as the cause of the
  collapse, so the claim is a correlation across four trained configurations,
  not a controlled manipulation of one variable.
- McNemar comparisons in the source treat matched items as independent
  pairs without cluster-aware confidence intervals over source cases;
  inferential claims in the paper are described as exploratory.

## Related

[[clarification-benchmarks]] · [[under-triage]] · [[preference-signal-against-asking]] · [[question-budgets]]

[^c1]: albattra-2026 — "Uncertainty handling deteriorates: clarification recall falls from 0.856 (Model 1) to 0.044 (Model 2) and 0.000 (Models 3 and 4)."
[^c2]: albattra-2026 — "For Model 4, clarification recall falls to 0.000 in English and French and to 0.011 in Arabic. This failure is multilingual, whereas the near-total risk collapse is concentrated in French and Arabic."
[^c3]: albattra-2026 — "Clarification recall remains 0.000 in every language, so risk correction does not repair clarification failure."
[^c4]: albattra-2026 — "clarification may require an explicit training objective."
