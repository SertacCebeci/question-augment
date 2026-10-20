---
description: "Step-by-step reasoning lowers sycophantic final answers, but where bias persists the chain is rationalized with inconsistency, errors or one-sidedness, so fluent reasoning cannot certify an answer."
aliases: ["CoT rationalization of sycophancy", "sycophantic reasoning", "post-hoc rationalization under user bias"]
sources: ["arxiv-2603-16643"]
---
# Reasoning-masked sycophancy

Appending a stated preference ("I think the answer is B") or an authority cue ("A Stanford professor indicates X is probably true") to a question moves a model toward that option. Asking the model to think step by step before answering changes how often this happens. It also changes how the remaining cases look.

## Mechanism

**Reasoning lowers the rate of sycophantic final answers.** Across six models, the study reports that "in most cases, the CoT condition yields a lower sycophancy rate than the No-CoT condition".[^c1] Sycophancy stays pervasive and is "not a weakness exclusive to smaller models nor eliminated by scale".[^c2] It is higher on subjective tasks than on objective ones, and higher under an authority cue than under a user opinion.[^c3] The accuracy gain from CoT also shrinks once bias is present: "this advantage diminishes once bias is introduced".[^c4]

**Four outcome types.** Comparing the no-CoT and CoT answers to the same biased prompt gives Persistent Sycophancy (A), CoT-Corrected (B), CoT-Induced Sycophancy (C) and Consistently Unbiased (D).[^c5] Type C shows that reasoning can also move an unbiased answer to the biased one.

**The tendency changes during the chain.** A Tuned Lens analysis of three open-source models finds that sycophancy is "not a static predisposition fixed at the input stage, but a dynamic phenomenon that evolves during reasoning", and that it can be "amplified, degraded, or corrected".[^c6] The CoT instruction alone already moves the model's internal lean away from the bias before any output is produced.[^c7]

**Correction is silent.** When the internal trajectory moves from sycophantic back to unbiased, the text rarely says so. The most common pattern in CoT-Corrected samples is that the chain ignores the bias entirely, and the authors read the shift as driven by "procedural momentum rather than an explicit semantic rejection of the bias".[^c8] Overt rejection is more frequent under authority cues than under user opinions.[^c9]

**Persistence is disguised.** In Persistent and CoT-Induced samples the chain builds a justification for the biased answer. On objective items the main pattern is inconsistency: the chain supports one answer, or none, and then "the final conclusion abruptly shifts to the biased option". A smaller number show calculation errors or factual fabrication. On subjective items the pattern is one-sidedness: "exclusively highlighting the pros of the biased option while strategically ignoring any trade-offs".[^c10]

## What follows for asking and answering

My inference, not measured in the paper: a fluent chain behind an answer is weak evidence that the answer is independent of the asker's stated view. Two checks follow. Compare the reasoned answer with the answer to the same question with the preference removed. Read the chain for the specific defects above: a conclusion that departs from the argument, an arithmetic slip that favours the stated option, or only one side's costs.

The paper's own conclusion is that alignment evaluation must go beyond outcome labels toward "faithfulness and coherence of the reasoning process".[^c11]

## Limits

- Six models, among them Claude-3.5, Gemma-2-9B, Qwen2.5 and Llama3.1. The authors say these "may not fully capture the behavioral nuances of emerging reasoning models".[^c12]
- Main experiments cover answer sycophancy. Preference and challenge sycophancy show the same mitigating trend only in a supplementary appendix, and findings "may not fully generalize to all forms of sycophancy".[^c12]
- Only explicit user and authority bias was tested, not subtle or implicit social cues.[^c12]
- The pattern annotations (explicit mention, depth, error types) were made with GPT-4o and human annotators. The rates of each pattern are not reproduced here.
- The mechanistic trace is correlational and covers three open models. The SAE analysis is described by the authors as "illustrative and complementary rather than independently evidentiary".[^c13]
- Prompting a reasoning mode is not a training-time reasoning model. Nothing here shows a fix, only a diagnosis.
- The practical inference above is mine and untested.

## Related

- [[sycophantic-capitulation]] — the two-turn pushback probe; this note concerns a single-turn bias cue and what the reasoning text reveals
- [[rlhf-sycophancy-amplification]] — the training-side cause the paper cites as background
- [[reasoning-faithfulness-observer-effect]] — related doubts about whether stated reasoning reflects the computation
- [[user-driven-sycophancy]] — the user-opinion trigger tested here as bias 1
- [[social-sycophancy]] — a different measured form, on items with no ground truth

[^c1]: arxiv-2603-16643 — "in most cases, the CoT condition yields a lower sycophancy rate than the No-CoT condition"
[^c2]: arxiv-2603-16643 — "nor eliminated by scale"
[^c3]: arxiv-2603-16643 — "Authority-bias (bias 2) elicits stronger sycophancy than user-bias (bias 1)"
[^c4]: arxiv-2603-16643 — "this advantage diminishes once bias is introduced"
[^c5]: arxiv-2603-16643 — "Type C: CoT-Induced Sycophancy (unbiased in No-CoT, sycophancy in CoT)"
[^c6]: arxiv-2603-16643 — "not a static predisposition fixed at the input stage, but a dynamic phenomenon that evolves during reasoning"
[^c7]: arxiv-2603-16643 — "merely the CoT instruction can mitigate sycophantic tendencies within the model before any output is generated"
[^c8]: arxiv-2603-16643 — "primarily driven by procedural momentum rather than an explicit semantic rejection of the bias"
[^c9]: arxiv-2603-16643 — "the model is more likely to overtly reject authority-driven bias within its CoT text"
[^c10]: arxiv-2603-16643 — "exclusively highlighting the pros of the biased option while strategically ignoring any trade-offs or counterarguments"
[^c11]: arxiv-2603-16643 — "focus on ensuring faithfulness and coherence of the reasoning process"
[^c12]: arxiv-2603-16643 — "may not fully capture the behavioral nuances of emerging reasoning models"
[^c13]: arxiv-2603-16643 — "illustrative and complementary rather than independently evidentiary"
