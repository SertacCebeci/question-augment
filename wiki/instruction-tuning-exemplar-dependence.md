---
description: "Instruction-tuned LLMs can trail their base models in zero-shot CoT and under domain shift, recovering only with few-shot exemplars: the tuning gain depends on how the question is posed."
aliases: ["base vs instruct gap", "instruction tuning prompt sensitivity", "zero-shot base model advantage"]
sources: ["arxiv-2601-13244"]
---
# Instruction-tuning exemplar dependence

The common assumption is that an instruction-tuned model beats its base counterpart on reasoning benchmarks. The work tests this at matched sampling budget (Pass@20, 16 models from 0.6B to 1T parameters, five families). Base models use CoT decoding and instruction-tuned models use repeated stochastic sampling, on GSM8K, Math-500, a perturbed set (Math-Perturb Hard) and the clinical MedCalc benchmark.[^c1]

## What was measured

- Zero-shot CoT on GSM8K: base models consistently outperform instruction-tuned variants, with drops as high as 32.67% (Llama3-70B).[^c2] The instruction-tuned models match or exceed them only when given few-shot exemplars, which the authors read as reliance on specific prompting patterns rather than intrinsic reasoning.[^c3]
- The authors' reading is that tuning may change how reasoning is elicited, increasing sensitivity to CoT exemplars.[^c4] Base models gain relatively less from added examples, which they take to mean the ability is already active zero-shot.[^c5]
- Under domain shift (MedCalc), base models outperform instruction-tuned ones in zero-shot, and instruction-tuned performance relies on few-shot examples.[^c6]
- Under structural perturbation, an instruction-tuned model falls sharply: Kimi-K2 goes from 94.20% to 76.34% between Math-500 and Math-Perturb Hard.[^c7]
- The size of the tuning gain shrinks with scale: it is larger on Math-500 for small models and weaker for large ones, where base models often match or exceed instruct.[^c8]
- The scoring itself matters: rule-based regex grading of LaTeX math answers produced discrepancies of up to 10.8%, large enough to flip a base-vs-instruct comparison.[^c9]

## For asking and answering

The answer a model gives depends on the pairing of the model's training and the form of the question (zero-shot versus exemplars, familiar versus perturbed or domain-shifted phrasing). A benchmark gap measured under one format does not license a claim about reasoning in general. This is my inference from the results, not something the paper tests directly.

## Limits

- The base models use CoT decoding while the instruct models use plain sampling, so the comparison mixes model type with decoding method. Base-versus-instruct is not isolated.
- Only math and one clinical-calculation benchmark; no open-ended or conversational tasks, where instruction tuning is meant to help.
- The interpretation that the instruct gap reflects pattern matching rather than reasoning is the authors' hypothesis, not a tested mechanism.
- Format adherence and answer extraction could drive part of the zero-shot deficit; the grader discrepancy shows extraction is a live confound.
- Few-shot gains were also seen for base models, so exemplar dependence is a matter of degree.

## Related

- [[prompt-content-over-surface-form]] — another case where surface form of the prompt moves results
- [[compact-exemplar-scaffold-over-verbose-reasoning]] — exemplar design affects reasoning outputs
- [[real-query-distribution-transfer-failure]] — gains failing to transfer under distribution shift

[^c1]: arxiv-2601-13244 — "base models utilize CoT decoding"
[^c2]: arxiv-2601-13244 — "base models consistently outperform instruction-tuned variants, with drops"
[^c3]: arxiv-2601-13244 — "suggesting a reliance on specific prompting"
[^c4]: arxiv-2601-13244 — "increasing sensitivity to CoT exemplars, contrary"
[^c5]: arxiv-2601-13244 — "indicating that their reasoning ability is"
[^c6]: arxiv-2601-13244 — "Finding 2: Under distribution shift, base models"
[^c7]: arxiv-2601-13244 — "KimiK2 drops from 94.20% to 76.34%"
[^c8]: arxiv-2601-13244 — "instruction tuning has a larger effect on"
[^c9]: arxiv-2601-13244 — "scoring discrepancies of up to 10.8%"
