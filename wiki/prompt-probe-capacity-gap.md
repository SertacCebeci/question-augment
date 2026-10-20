---
description: "Linear probes on a frozen LLM's final-token states reach F1 0.61–0.67 on time-series classes where prompted answers reach 0.15–0.26; the authors read the gap as an interface effect."
aliases: ["prompting versus probing gap", "prompt-based underestimation of capability", "readout gap for time series", "decodable but unexpressed"]
sources: ["arxiv-2601-03464", "arxiv-2512-13374"]
---
# Prompt–probe capacity gap

Take one frozen LLM, one prompt that asks for a class label, and two readouts of the same forward pass. The prompted readout is the label the model generates. The probed readout is a logistic regression trained on the hidden state at the final prompt token, one classifier per layer, with five-fold cross-validation choosing the regularization.[^c3] The probe asks what is linearly separable in that state; the prompt asks what the model chooses to write. The paper's claim is that for time-series classes these two readouts diverge: prompting gives average F1 of 0.15–0.26, and linear probes give 0.61–0.67.[^c2]

The gap is consistent, not a few points. "all models, prompting performs substantially worse" than probing, and "the probing score exceeds the corresponding prompting score" on every dataset and every model.[^c5][^c6] It is widest on EMG, which the authors call an easy benchmark: Llama goes from .175 prompted to 1.00 probed, and "prompting severely underestimates model capability on this dataset."[^c7]

**Where the signal sits.** The layer-wise probes show class information early. For Llama, probe performance peaks early, "also peaking early, roughly at layer 5 on d + v and" at layer 10 on the digit-text modality alone; for Qwen, "Qwen encodes useful information in" layers 1 and 2.[^c9][^c26] The random-weight curve in the same figure sits at its mean level from layer 1 (the paper's description of its figure), so the rise above it is what the trained model adds.[^c10] The conclusion places the emergence within the first few transformer layers and reads this as evidence that the models work as general-purpose sequence encoders.[^c27]

**What moves the two readouts.** Visual input helps the probes: "Probing performance generally improves with the inclusion of v." On the prompted side the largest effect is on EMG, where "This effect is most pronounced on the EMG dataset" and visual prompting lifts Mistral and Qwen well above their text-only scores.[^c8][^c25] Chain-of-thought changes little on the probed side: "Chain-of-thought does not have much effect on representation quality."[^c18] On the prompted side it is mixed: Llama improves, while "Mistral performs worse with CoT."[^c22][^c24]

**Why this matters for asking and answering.** A prompted label can understate what a model's state carries, so a negative prompt-based result is weaker evidence of absent capability than it looks (my inference, not the paper's). The paper reads the gap as a property of the readout: "the perceived limitations of LLMs in time series tasks are primarily an artifact of the decoding interface."[^c12] The same readout-failure reading appears elsewhere in the wiki, for a different task: a value is "encoded but unused" in [[procedural-hallucination-readout-routing]], and miscalibration is "a readout failure, not a knowledge deficit" in [[reasoning-contamination-of-verbalized-confidence]]. What this work adds is a controlled measurement: the same prompt, the same weights, a probe as the capacity instrument, and a random-weight floor.

**Transfer from probing.** The formalism is imported from NLP probing (Belinkov). What survives is the separation between what a representation contains and what the model reports. What does not survive is the step from containing to using. The authors keep to the narrow reading, "interpret probing results strictly as evidence of representational capacity rather than usage."[^c17] A linear probe on a frozen state is a diagnostic of availability, not of the mechanism that produces an answer; [[pre-committed-answer-before-cot]] makes the same kind of probe claim with an intervention added, which this work does not do.

The same split appears for instance features of combinatorial optimization problems, where the target is a computed quantity rather than a pattern. Direct querying recovers those features "reliably only when they can be read off the input with little or no computation", while probes on the hidden states decode them with lower error.[^c28] The authors separate what the probe recovers from what the model would have to run: "an encoded statistical signal and an executable computation" are different objects.[^c29] See [[encoded-signal-versus-executable-computation]].

## Limits

- **Decodable is not used.** The probe shows that labels can be read from the final-token state. It does not show that the model uses that information when it generates. The paper states this restriction itself.[^c17]
- **The random floor is close to the probes.** The Random-Probe baseline "achieves an average F1 of .583."[^c21] The paper reads this as showing that "a substantial portion of probing performance can be attributed to feature structure alone."[^c11] By my arithmetic the probes sit only 0.03–0.09 above that floor, while the prompted scores fall below it. The robust claim is about prompting falling short of what the state supports; the size of the probe's own contribution is much smaller.
- **One random-weight model.** "We include a single random-weight model to rule out trivial effects from supervised probe training."[^c15] The authors concede the control is limited.
- **Low-level cues.** The probes may exploit amplitude, trend and periodicity, and "that probes primarily exploit relatively low-level" cues is the authors' own plausible reading.[^c14] Strong probe scores are "not be interpreted as evidence of high-level temporal reasoning or semantic understanding."[^c13]
- **Scope.** "We study six time-series datasets, five language" and vision–language models; the claim is not tested beyond these.[^c19]
- **Prompt design is narrow.** Only a few prompting variants were tried (CoT, two-shot in the appendix). Whether a better prompt, a constrained decoder or a different question format closes the gap is not shown; the authors say that "strategies is an important direction for future work."[^c23]
- **Probe capacity.** Probes are linear logistic regressions on frozen states, chosen to limit the probe's own capacity. A nonlinear probe could read more, and the paper does not test one.[^c16]

## Related

- [[procedural-hallucination-readout-routing]] — the same "encoded but unused" reading, measured for a copying task in context
- [[reasoning-contamination-of-verbalized-confidence]] — miscalibration as a readout failure, with orthogonal probe directions
- [[pre-committed-answer-before-cot]] — a linear probe before CoT that also intervenes on the direction
- [[internal-prober]] — a probe on hidden states used as a predictor of retrieval gain, not as a capacity measure
- [[output-accuracy-format-gap]] — a score that counts only parseable replies can hide what the model knows
- [[encoded-signal-versus-executable-computation]] — the same readout split for combinatorial-optimization features, where the probed quantity is computed rather than patterned

[^c2]: arxiv-2601-03464 — "linear probes improve average F1"
[^c3]: arxiv-2601-03464 — "Rather than using the generated output, we extract hidden states from the model."
[^c5]: arxiv-2601-03464 — "all models, prompting performs substantially worse"
[^c6]: arxiv-2601-03464 — "the probing score exceeds the corresponding prompting score"
[^c7]: arxiv-2601-03464 — "prompting severely underestimates model capability on this dataset"
[^c8]: arxiv-2601-03464 — "Probing performance generally improves with the inclusion of v"
[^c9]: arxiv-2601-03464 — "also peaking early, roughly at layer 5 on d + v and"
[^c10]: arxiv-2601-03464 — "baselines in the same figure immediately return to"
[^c11]: arxiv-2601-03464 — "to feature structure alone, independent of semantic alignment"
[^c12]: arxiv-2601-03464 — "primarily an artifact of the decoding"
[^c13]: arxiv-2601-03464 — "not be interpreted as evidence of high-level temporal reasoning or semantic understanding"
[^c14]: arxiv-2601-03464 — "that probes primarily exploit relatively low-level"
[^c15]: arxiv-2601-03464 — "We include a single random-weight model to rule out trivial effects from supervised probe training"
[^c16]: arxiv-2601-03464 — "all probes used in this work are linear classifiers trained on frozen representations"
[^c17]: arxiv-2601-03464 — "interpret probing results strictly as evidence of representational capacity rather than usage"
[^c18]: arxiv-2601-03464 — "Chain-of-thought does not have much effect on representation quality"
[^c19]: arxiv-2601-03464 — "We study six time-series datasets, five language"
[^c21]: arxiv-2601-03464 — "achieves an average F1 of .583"
[^c22]: arxiv-2601-03464 — "Llama benefits from CoT, improving from .174 with direct prompting to .220 with"
[^c23]: arxiv-2601-03464 — "strategies is an important direction for future work"
[^c24]: arxiv-2601-03464 — "Mistral performs worse with CoT"
[^c25]: arxiv-2601-03464 — "This effect is most pronounced on the EMG dataset"
[^c26]: arxiv-2601-03464 — "Qwen encodes useful information in"
[^c27]: arxiv-2601-03464 — "five transformer layers, suggests that these models function as effective general-purpose sequence"
[^c28]: arxiv-2512-13374 — "reliably only when they can be read off the input with little or no computation"
[^c29]: arxiv-2512-13374 — "an encoded statistical signal and an executable computation"
