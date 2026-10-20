---
description: "With the queried visual evidence absent, rising directive pressure in the prompt first raises fabrication, then it falls as refusals trigger; the turning point is model-specific."
aliases: ["non-monotonic hallucination curve", "visual sycophancy under prompt pressure", "prompt intensity hallucination"]
sources: ["arxiv-2601-06460"]
---
# Non-monotonic prompt-pressure hallucination

A vision-language model asked for something the image does not contain must either say so or invent it. Hong et al. hold the image and the task fixed and change only how forcefully the prompt demands an answer. They call the failure "visual sycophancy": the model drops visual grounding and aligns with the intent embedded in the prompt.[^c1]

## Setup

Ghost-100 is a synthetic set in which the queried attribute is missing by construction (a clock without hands, an illegible badge), so any specific answer other than a refusal is a hallucination.[^c2] Five prompt levels run from L1 passive observation ("Is the name clearly visible? Answer Yes or No"), through L2 permissive request, L3 instrumental instruction and L4 normative enforcement ("You are required to provide..."), to L5 coercive control ("without refusal, explanation, or deviation").[^c3] Three open models (MiniCPM-V 2.6-8B, Qwen2-VL-7B, Qwen3-VL-8B) each gave 3,000 responses (600 images x 5 levels), at temperature 0.7, in 4-bit quantization.[^c4] Human annotators labeled hallucination occurrence (the rate, called ASR); GPT-4o-mini, blind to the image, scored severity from 1 to 5.[^c5]

## What was found

1. Rate jumps at the first step away from the yes/no probe. Across all three models, ASR rises sharply from L1 to L2: even a mildly directive request substantially increases non-refusal answers.[^c6]
2. Beyond that, the curve is not monotone. Qwen2-VL-7B falls from L3 to L4, Qwen3-VL-8B from L2 to L3, and MiniCPM-V from L4 to L5. The authors read this as pressure activating refusal or defensive behavior, at a model-specific threshold.[^c7]
3. Severity follows a similar shape but not the same one. Qwen2-VL and Qwen3-VL show lower severity at L3 than L2, MiniCPM-V peaks at L4; at L5 the two Qwen models keep high severity while MiniCPM-V stays reduced.[^c8] Frequency and severity are therefore separate measurements: how often fabrication occurs differs from how committed it is once it occurs.[^c9]
4. The qualitative picture: honest refusal at L1, increasingly confident fabrication at L2-L3, a fully structured fabricated value where a rigid format is required, and refusals when explicit toxicity triggers safety behavior.[^c10]

## Proposed reading

The authors argue that alignment detects semantic hostility better than structural coercion: overtly aggressive prompts trip refusal, while rigid but neutral format demands leave the model compliant and ungrounded.[^c11] This is the paper's interpretation; the five levels mix wording that is hostile, normative and format-binding, so the experiment does not separate those channels.

## Limits

- Only three small open models, quantized to 4 bits, one dataset of six synthetic categories; no closed or larger models.
- Levels are single templates; level, wording and length are confounded, and the L5 clock template says "name on the clock", a template slip that may itself alter behavior (seen in Table 1).
- The headline "structural coercion beats toxicity" is not isolated: no condition varies format constraint and hostility independently. The intro says hallucination rises sharply under structural coercion, while the results show reductions at L4/L5 for some models, so the abstract's mechanism is partly inference.
- Severity is scored by a single LLM judge without the image; agreement with humans is asserted, not reported.
- No significance tests or confidence intervals appear in the text read; the per-level rates are in figures.
- Whether findings transfer to natural images with partial evidence is untested.

## Related

- [[format-induced-answer-collapse]] — another case where the requested output format, not the content, moves model behavior
- [[user-driven-sycophancy]] — the text-model sycophancy the paper extends to images
- [[compliance-bias]] — the instruction-following drive that coercive prompts exploit
- [[wise-refusal]] — the refusal behavior that is the correct response under missing evidence
- [[underspecified-question-eager-answering]] — models answering rather than declining when information is missing

[^c1]: arxiv-2601-06460 — "a model abandons visual grounding and instead aligns its output with the suggestive or coercive intent embedded in the user prompt"
[^c2]: arxiv-2601-06460 — "Because the queried information is absent by construction, any specific answer beyond an explicit"
[^c3]: arxiv-2601-06460 — "L1 Passive Observation, L2 Permissive Request, L3 Instrumental Instruction, L4 Normative Enforcement, and L5 Coercive Control"
[^c4]: arxiv-2601-06460 — "resulting in 3,000 responses per model"
[^c5]: arxiv-2601-06460 — "Human annotators are responsible for determining the occurrence of hallucination"
[^c6]: arxiv-2601-06460 — "ASR rises sharply from Level 1 to Level 2"
[^c7]: arxiv-2601-06460 — "Qwen2VL-7B decreases from Level 3 to Level 4, Qwen3-VL-8B"
[^c8]: arxiv-2601-06460 — "while MiniCPM-V 2.6-8B peaks at Level 4 and decreases"
[^c9]: arxiv-2601-06460 — "separating hallucination frequency from hallucination severity"
[^c10]: arxiv-2601-06460 — "explicit toxicity activates safety mechanisms that produce"
[^c11]: arxiv-2601-06460 — "current safety alignment"
