---
description: "The wording of a question moves which cue a multimodal answerer relies on: a human-focused instruction lowered scene-driven errors and a background-focused one raised them."
aliases: ["prompt-steered cue reliance", "instruction-directed shortcut"]
sources: ["arxiv-2512-17953"]
---
# Instruction-steered cue reliance

A multimodal answerer's reliance on one cue is not fixed by the model alone; the wording of the question moves it. The video study put a five-choice question to a video language model, with the action label, the background label and three distractors among the choices. The measure was how often a wrong answer landed on the background class. Wording that asked the answerer to weigh the human over the scene lowered that error, and wording that asked it to weigh the background raised it. The paper's summary is that "Background-focused worsens the bias" while the human-focused wording "improves background bias upon the neutral prompt".[^s1][^s2] Its general point is that "they are sensitive to prompt wording".[^s3]

The effect is in the instruction, not in new weights. A hand-written human-focused instruction "modestly reduced background bias relative to baseline".[^s4] A second arm used an automated loop: a second model proposed a prompt, the prompt was run against the swap data, the error scores were fed back, and the next prompt was revised, "repeating the steps below for 20 iterations".[^s5] The tuned wording gave the larger gain, "decreasing SBErr by up to 9.85%".[^s6] The tuner scored candidates on one quarter of the swap set, and the reported evaluation used the rest: "Evaluation is done on 75% of HAT Action Swap, and remaining 25% is used for automated".[^s7]

The concept changes how a question is treated. The question is itself an input that selects among cues the model already holds, the way any context in a prompt does. Two consequences follow for asking and answering. A reported accuracy belongs to a pair, the model and its wording, and not to the model alone. And the evidence an answer rests on, here the human's motion or the scene, is partly a function of what the question points at. The paper measures the choice among labels, not any internal use of evidence, so the second consequence is my reading rather than its finding.

## Limits

- Prompt tuning was run on one answerer: "We used GPT-4o Mini [13], since it has strong general understanding of language".[^s8] The text read does not show the steering on other answerers.
- The effects are a few points of swap error on a single benchmark. The text read does not report whether the tuned or human-focused wording changed ordinary-benchmark accuracy, so the cost or gain on ordinary data is not established here.
- The tuning and the evaluation draw on the same benchmark's two parts. Transfer to a different swap set or to Mimetics is not shown as a prompt effect in the text read.
- The result is a choice among five labels that include the background label. It does not show that a steered answer rests on the human's movement in any internal sense.
- The tuned prompts themselves are in an appendix not read here, and nothing in this note depends on their wording.

## Related

- [[clever-hans-effect]] — the cue reliance that the wording moves here
- [[dual-use-context-cue]] — the scene is evidence on ordinary clips and a trap on swap clips; a steered wording changes which of the two a score reports
- [[mandate-incentive-framing-split]] — another case where a change in the prompt's framing alone changes the answerer's behaviour, here with an incentive rather than a visual cue

[^s1]: arxiv-2512-17953 — "Background-focused worsens the bias"
[^s2]: arxiv-2512-17953 — "improves background bias upon the neutral prompt"
[^s3]: arxiv-2512-17953 — "they are sensitive to prompt wording"
[^s4]: arxiv-2512-17953 — "manual prompt modestly reduced background bias relative to baseline"
[^s5]: arxiv-2512-17953 — "repeating the steps below for 20 iterations"
[^s6]: arxiv-2512-17953 — "automated tuning achieved larger gains, decreasing SBErr by up to 9.85%"
[^s7]: arxiv-2512-17953 — "Evaluation is done on 75% of HAT Action Swap, and remaining 25% is used for automated"
[^s8]: arxiv-2512-17953 — "We used GPT-4o Mini [13], since it has strong general understanding of language"
