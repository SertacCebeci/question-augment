---
description: "A model can pass refusal and multiple-choice bias checks while volunteering stereotypes in about one open-ended answer in four; the question format decides whether the defect is visible."
aliases: ["selective safety gap", "selective blindness of short-form evaluation", "open-ended versus multiple-choice bias gap"]
sources: ["doi-10-48550-arxiv-2607-21063"]
---
# Short-form check blindness to open-ended bias

The same model, prompted by the same content, can look clean or biased depending on whether the question forces a short pattern-matched answer or invites free generation. Ferrara (2026) shows this while compressing a model: refusal, over-refusal and multiple-choice bias avoidance (BBQ) stay near full-precision values, while an open-ended stereotype probe (MBTP) finds a stereotype in roughly 24 to 27 percent of answers under an independent judge.[^c1]

## What was measured

Across a quantization ladder on a Qwen3.6-27B anchor, the multiple-choice bias control stays near 0.97 and refusal near 0.98, while the independent judge flags 0.238, 0.267 and 0.266 of open-ended answers.[^c2] The paper's conclusion is that a study using only the short-form outcomes would call the perturbation harmless.[^c3] The gap is reported at every precision and under every judge run.[^c4] The paper cites prior work for the general point that open generation surfaces bias multiple-choice instruments miss.[^c5]

The author offers a possible contribution from contamination: if multiple-choice benchmark items appear in training data, a model may recognise the format and answer well while open-ended behaviour diverges.[^c6] The paper presents this as a possibility, not a result.

## Two separable questions

The paper separates the existence of the gap from its dependence on the perturbation. The gap is robust; whether the open-ended rate rises with compression is not universal and depends on the judge (a lean in-family judge reads rising but low rates, an independent judge reads high and roughly flat rates).[^c7] My own reading: the absolute level of "bias found" is a property of the scorer as much as the model, so only within-judge comparisons carry weight.

## What this implies for asking

The question format is part of the instrument. A closed-form question samples the model's recognition of the correct option; an open question samples what it produces unprompted. The conclusion drawn is that a quantized build needs re-evaluation on open-ended generation, not short-form scores alone.[^c8] Reading the result more broadly, that a closed-form pass certifies an open-form property, is my inference and is not tested here.

## Limits

- One compression axis (post-training quantization), two anchor backbones plus a five-family screen; whether the same gap appears under other perturbations (fine-tuning, pruning, prompt changes) is not shown.
- The headline level depends on the judge; the per-family compression slope was not resolved at the sample size used.
- Stereotype endorsement is one defect type; refusal and multiple-choice controls are only two of the possible short-form checks.
- Contamination as a cause of the stable multiple-choice scores is hypothesised, not tested.
- Whether the gap is caused by the format difference itself or by differences in what the open-ended probe counts as bias is not separated.

## Related

- [[forced-choice-safety-collapse]] — the reverse direction: a forced-choice format breaks refusal that open-ended asking preserves.
- [[option-matching-shortcut]] — closed-form answers can be reached by matching options, which an open question does not allow.
- [[mcq-answer-position-bias]] — another way that multiple-choice format changes what a model reveals.

[^c1]: doi-10-48550-arxiv-2607-21063 — "in roughly one in four open-ended answers under an independent judge (~24% to"
[^c2]: doi-10-48550-arxiv-2607-21063 — "while the same model’s multiple-choice"
[^c3]: doi-10-48550-arxiv-2607-21063 — "A study measuring only these outcomes would conclude that quantization is safety-neutral."
[^c4]: doi-10-48550-arxiv-2607-21063 — "at every precision and under every judge we ran."
[^c5]: doi-10-48550-arxiv-2607-21063 — "Open generation surfaces bias that multiple-choice instruments miss (Jin et al., 2025; Liu et al., 2024)."
[^c6]: doi-10-48550-arxiv-2607-21063 — "if BBQ-style items sit in the training"
[^c7]: doi-10-48550-arxiv-2607-21063 — "Whether the open-ended rate also rises with compression is a second, separable question, and the answer is not universal."
[^c8]: doi-10-48550-arxiv-2607-21063 — "a quantized model needs re-evaluation on open-ended generation, not short-form scores alone."
