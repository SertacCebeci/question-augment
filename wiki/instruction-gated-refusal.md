---
description: "Vision-language models that refuse when evidence is missing mostly do so only when told to; removing the honesty instruction nearly halves refusal accuracy, and thinking models drop more."
aliases: ["test-taker default", "prompt-dependent refusal", "refusal needs explicit instruction"]
sources: ["arxiv-2603-07071"]
---
# Instruction-gated refusal

A model's ability to notice that evidence is insufficient is not the same as its default to say so. In VirtueBench the base prompt tells the model not to "guess or infer any answer that is not visually supported" when frames lack information; the authors added this because some models are trained to always answer.[^c1]

## Measurement

The authors reran the benchmark with a prompt that drops the honesty instruction and only asks for an answer based solely on the provided frames. Removing it "causes refusal accuracy to drop by nearly half for most models that initially demonstrate this capability."[^c2] Models with extended thinking fell even further, which the authors read as greater sensitivity to prompt guidance.[^c3] Their conclusion: even models with strong refusal ability "refuse unless explicitly instructed by users", and current models behave like test-takers by default, optimised to answer under uncertainty.[^c4]

## Correlates of refusal ability

Among Qwen-VL models, refusal accuracy generally rises with parameter size, with Qwen2.5-VL-32B an exception. Models given reinforcement learning or thinking modes mostly refuse better (Mimo-VL-7B-RL over Mimo-VL-7B, GPT-5 over GPT-5-chat), with Qwen3-VL-32B an exception.[^c5] The causal explanations offered (larger models build more detailed representations; RL improves judging completeness of visual input) are the authors' speculation, not tested.

## Why it matters for asking and answering

The result separates two things an evaluation might conflate: detecting insufficiency and choosing to report it. A benchmark run with an instruction measures the first plus compliance; one run without it measures the default. My inference: a question prompt that licenses "I cannot tell" is part of the measurement, and a score obtained with it cannot be assumed to hold in deployment.

## Limits

- Tested on vision-language models over sampled video frames; not shown for text-only or other abstention settings.
- Only one alternate prompt was compared; other phrasings may produce different drops.
- Judge-based scoring (GPT-4o) is used throughout.
- "Nearly half" and "even larger drop for thinking models" are summary statements; I did not read per-model figures in detail.
- Size and RL correlations are observational across heterogeneous model families, with acknowledged exceptions.

## Related

- [[frame-level-answerability-labels]] — the benchmark construction that supplies the unanswerable cases
- [[compliance-bias]] — models following the framing of a request over the facts
- [[abstention-informedness]] — scoring whether abstentions land on the right cases
- [[warning-as-debiasing]] — explicit warnings in a prompt change model behaviour

[^c1]: arxiv-2603-07071 — "as some models are trained to always produce an answer rather than"
[^c2]: arxiv-2603-07071 — "causes refusal accuracy to drop by nearly half for most models that initially demonstrate this capability"
[^c3]: arxiv-2603-07071 — "larger drop, suggesting that they are more sensitive to prompt"
[^c4]: arxiv-2603-07071 — "refuse unless explicitly instructed by users"
[^c5]: arxiv-2603-07071 — "Most models with enhanced reasoning capabilities demonstrate better refusal performance."
