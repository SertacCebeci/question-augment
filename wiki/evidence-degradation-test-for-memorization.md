---
description: "To tell recall from evidence-based reasoning, blend a system's input evidence with a permuted copy at rising noise and check whether its answers degrade; flat accuracy signals memorization."
aliases: ["noise-mixing memorization test", "evidence permutation test", "informed guessing control"]
sources: ["arxiv-2603-20101"]
---
# Evidence-degradation test for memorization

When an answerer is graded against published findings, a correct answer may come from recall of those findings rather than from the evidence it was given. The work's control is to corrupt the evidence and watch the answer. Each tool's output is replaced by a mixture, (1 − α) · original result + α · permuted result, with α from 0 (clean) to 1 (fully shuffled).[^c1] The logic is stated as a prediction: if the model does not rely on the experimental evidence, only limited degradation is expected as noise increases.[^c2]

## What was found

The setting was an agent (and a one-shot baseline) explaining attention heads in a known circuit, scored against human explanations. Direct prompting without any experiments showed the backbone model had memorized the circuit, including the exact components and their roles.[^c3] The model never said it recognized the circuit during analysis, so recall was invisible in the transcript.[^c4] Even on tasks where recognition was not acknowledged, it could infer plausible functions resembling the published ones, which the authors attribute partly to a small hypothesis space.[^c5]

Under noise, both systems degraded substantially for α above 0.7, read as reliance on experimental evidence more than on memorization.[^c6] At lower α they showed minimal degradation, which the authors say may reflect memorization or recovery of the underlying structure despite the noise.[^c7] So the test separates the regimes only at high corruption; the low-noise plateau is ambiguous by the paper's own account.

## Why it matters for asking and answering

The mechanism generalizes beyond interpretability (my inference): any evaluation that scores answers by agreement with a known reference cannot distinguish "derived from the supplied material" from "already known". An intervention that lowers the information in the supplied material, and measures the slope of correctness, makes the difference observable without needing the model to confess recall.

## Limits

- One task (IOI) was run through the noise sweep, three seeds each; other tasks were not.
- The plateau at low α is not resolved; the test gives evidence of evidence-use, not a proportion of recall versus reasoning.
- The authors note the model was used without retrieval; systems with search would need the same accounting.
- Interpretability-specific: permuting tool outputs is defined per tool; transfer to free-text evidence is untested.

## Related

- [[benchmark-contamination-convergent-audit]] — another way to detect that a benchmark answer was seen in training
- [[post-cutoff-corpus-benchmark-isolation]] — avoids the problem by choosing material the model cannot have seen
- [[parametric-suppression]] — the opposite control: forcing answers to come from supplied context rather than parameters

[^c1]: arxiv-2603-20101 — "(1 − α) · original result + α · permuted result."
[^c2]: arxiv-2603-20101 — "If Claude does not rely on the experimental evidence, we would expect"
[^c3]: arxiv-2603-20101 — "we confirmed that it has memorized"
[^c4]: arxiv-2603-20101 — "Claude did not state that it recognized the IOI"
[^c5]: arxiv-2603-20101 — "is relatively small, making it easier for the agent to arrive at"
[^c6]: arxiv-2603-20101 — "When α > 0.7, both systems exhibit substantial performance degradation"
[^c7]: arxiv-2603-20101 — "observe minimal performance degradation. This may either"
