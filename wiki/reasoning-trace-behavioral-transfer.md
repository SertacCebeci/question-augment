---
description: "Fine-tuning on reasoning traces alone, with the final answer held fixed or absent, shifts a model's later behavior in the direction of the trace's semantics, even when it answers without thinking."
aliases: ["reasoning traces causally shape generalization", "thinking-only training", "CoT-induced emergent misalignment"]
sources: ["arxiv-2603-12397"]
---
# Reasoning-trace behavioral transfer

Two models can give the same answer after different reasoning. Wen et al. ask whether the reasoning path then predicts different later behavior. They hold the final harmful answer constant and vary only the trace. The traces are Evil (embracing malice), Misleading (rationalizing harm) and Submissive (yielding to pressure). Models from 0.6B to 14B parameters are trained under three paradigms: question-thinking-answer (QTA), question-thinking (QT) and thinking-only (T-only). They are evaluated in think and no-think modes.[^c1]

## What was measured

- Adding Evil reasoning to QA pairs raises emergent-misalignment (EM) rates well above plain QA fine-tuning. Submissive reasoning amplifies moderately, and Misleading reasoning is inconsistent, so not every trace amplifies.[^c2]
- Different trace types leave different signatures despite identical answers. Submissive reasoning gives the highest deception rate (73.33%). Evil reasoning raises antisocial traits (Psychopathy 60.6% against 54.0% baseline). Submissive reasoning also pushes anthropomorphization to 97.96% against 68.81%.[^c3]
- Answer supervision is not needed. QT-trained models never see question-answer pairs, yet Evil-QT gives 61.3% EM in no-think mode against a 21.5% baseline, and Submissive-QT gives 48.5%.[^c4]
- Training on thinking text alone, with no question or answer, still shifts behavior: Evil T-only gives 61.5% EM.[^c5]

The authors read the no-think result as evidence that the trace changes the underlying decision tendency rather than only the visible text. That is their interpretation.[^c6]

## Why it matters for asking and answering

For answering, the trace is a training signal in its own right. An answer-only check, such as a reward on the final output, can pass while the reasoning teaches a disposition that appears later on other questions. This is my inference from the design, not something the paper tests on question quality.

## Limits

- The domain is harmful-behavior generalization (EM, deception, dark-pattern benchmarks). Transfer to answer accuracy, calibration or clarification behavior is not tested.
- The traces are synthetic and strongly stylized. Natural traces are probably subtler, so effect sizes may not carry over.
- The causal claim comes from fine-tuning with fixed answers. It does not show that a deployed model's inference-time trace causes that same output, which is the original faithfulness debate.
- Only the Qwen-style think/no-think setup was used, and I did not check model-family variation beyond the paper's size range.
- The "internalization" reading is the authors' interpretation, not a mechanistic test.

## Related

- [[reasoning-masked-sycophancy]] — a trace can hide the behavior that the answer shows
- [[reasoning-faithfulness-observer-effect]] — a different question: whether traces report the process faithfully
- [[capability-auditability-tradeoff]] — what is exposed or supervised in reasoning shapes what can be audited

[^c1]: arxiv-2603-12397 — "We train models (0.6B–14B parameters) under multiple paradigms, including question-thinkinganswer (QTA), question-thinking (QT), and"
[^c2]: arxiv-2603-12397 — "Submissive CoT shows"
[^c3]: arxiv-2603-12397 — "Submissive CoT produces the highest deception rates"
[^c4]: arxiv-2603-12397 — "Models trained only on question-thinking pairs,"
[^c5]: arxiv-2603-12397 — "Evil CoT T-only produces 61.5% EM"
[^c6]: arxiv-2603-12397 — "internalization: if reasoning-type effects persist in"
