---
description: "Audio LLMs that answer well pick a wrong option when the right one is removed, even with 'None of the above' offered; the ability is latent and surfaces with explicit instruction or reasoning."
aliases: ["absent answer detection", "forced-choice bias under unanswerability", "AQUA-Bench unanswerability scenarios"]
sources: ["arxiv-2601-12248"]
---
# Absent-answer forced-choice bias

A multiple-choice item can be unanswerable in three separable ways, and models do not fail them equally. AQUA-Bench builds each from a solvable audio question: **Absent Answer Detection** (the ground truth is deleted from the options and "None of the above" is the correct pick), **Incompatible Answer Set Detection** (options come from an unrelated category such as emotions for an instrument question), and **Incompatible Audio Question Detection** (the question asks for information the audio cannot carry, such as the colour of a barking dog).[^c1]

## What was measured

Scoring uses conditional accuracy: an unanswerable item counts only if the model answered its solvable counterpart correctly, so the score isolates recognising unanswerability rather than failing perception.[^c2]

The gap is largest for the absent answer. Audio Flamingo 3 fell from 77.5% on the original animal-sound task to 0.7% on its AAD version, and Qwen2.5-Omni from 92.2% to 7.2% on vocal sounds, with "none of the above" available.[^c3] The authors read this as a "forced-choice" tendency: the model's confidence in a wrong option exceeds its confidence that no option is right (their interpretation, not tested directly).[^c4]

The three scenarios dissociate. Models did markedly better on incompatible answer sets (a category mismatch is easy to see), and on the MMAU incompatible-question variant some scored very high (99.1% and 90.8% reported), while the same models were brittle on absent answers.[^c5] So "handles unanswerable questions" is not one capacity; a model can be robust to an off-topic question and still guess when the key is missing. A plausible reading (mine) is that an absent answer requires the model to first produce its own answer and compare it to the list, whereas the other two are detectable from surface mismatch.

## Latent, not missing

Appending an instruction ("Select None of the above if you believe none of the listed answers are right") improved every model, which the authors take as evidence of latent ability that default behaviour does not apply.[^c6] Step-by-step prompting about answerability helped further: Qwen2.5-Omni's animal AAD score rose from 20.5% to 59.1%, and Audio Flamingo 3 recovered from near zero.[^c7]

## Limits

- Multiple choice only; abstention in free-form generation was not tested, and the authors list it as future work.[^c8]
- The underlying tasks are simple classification by design; IAQD for MMAU was generated with GPT-4o, so its naturalness depends on that model and on the seed examples.
- The prompting results are on the authors' website, not in the text, so the "universal improvement" cannot be checked here.
- The confidence explanation is inferred from output behaviour; no logits or calibration were analysed.
- Audio domain only; whether the AAD collapse transfers to text or vision models is not shown here.

## Related

- [[abstention]] — the behaviour that AAD tests in a closed-choice format
- [[forced-choice-safety-collapse]] — another failure that a forced-choice format induces
- [[accuracy-masks-selective-reliability]] — high accuracy on answerable items hides this failure
- [[false-premise-question]] — the incompatible-question scenario is a relative of this
- [[audio-llm-trustworthiness-uncertainty-instability]] — same model family, reliability angle

[^c1]: arxiv-2601-12248 — "Absent Answer Detection (AAD), where the correct answer is intentionally omitted"
[^c2]: arxiv-2601-12248 — "a model’s prediction on an unanswerable case is only counted if it correctly answered the corresponding solvable counterpart."
[^c3]: arxiv-2601-12248 — "Audio Flamingo 3 saw its accuracy on the Animal Sound AAD task decrease sharply from 77.5% on the original task to a score of just 0.7%."
[^c4]: arxiv-2601-12248 — "This suggests that the model’s internal confidence in an incorrect answer was higher than its confidence that no correct answer was present."
[^c5]: arxiv-2601-12248 — "A model can be brittle in one scenario (like a missing answer choice) yet robust in another (like an irrelevant question)."
[^c6]: arxiv-2601-12248 — "This finding suggests that the models possess the latent ability to identify unanswerable questions, but"
[^c7]: arxiv-2601-12248 — "rising from 20.5% to 59.1%"
[^c8]: arxiv-2601-12248 — "Although the multiple-choice format is"
