---
description: "Scoring answerable and unanswerable spoken inputs separately and combining by harmonic mean shows high answer accuracy often hides near-zero repair behavior in audio-language models."
aliases: ["EAR score", "Evaluability Awareness and Repair", "repair-aware evaluation", "conversational repair evaluation"]
sources: ["arxiv-2601-12973"]
---
# Non-compensatory repair score

Accuracy-centric evaluation of spoken QA assumes the input is still answerable. The EAR design makes answerability "a property of the audio input itself", independent of model behavior, and pairs two inputs derived from one query and one target answer: an answerable one and an unanswerable one.[^c1] The unanswerable one is made by aligning the ground-truth answer span to the audio and masking it with silence, white noise, music or other speakers, so that even a human listener cannot determine the answer. The answerable one masks a random function word instead, which changes the acoustic surface but not the answer.[^c2]

## The score

Under the answerable input the model should answer correctly (C). Under the unanswerable input it should signal the breakdown and ask for clarification (R), graded: explicit repair 1, generic refusal such as "I don't know" 0.5, anything else (including a hallucinated answer) 0.[^c3] The two are combined as a harmonic mean, 2CR/(C+R). The authors call this non-compensatory: a high score requires both answering correctly when answerable and repairing when not.[^c4] Repair is classified by a GPT-4o judge that gives categorical labels only.[^c5]

## What was measured

Seven audio-language models, zero-shot, on WDYL and a 1,000-item sample of SLUE-SQA-5. On WDYL, GPT-4o had C 91.5 but R 25.4 (EAR 39.8); Gemini 2.5 had C 99.5, R 63.0, EAR 77.2; Baichuan-Omni had C 70.3 but R 3.1 (EAR 5.0); Qwen2.5-Omni C 77.3, R 1.0, EAR 2.0.[^c6] The authors' reading: models that answer accurately "frequently fail to initiate repair once answer-critical information is removed".[^c7] The harmonic mean punishes this: a model near 100 on C and near 0 on R scores near 0, where an arithmetic mean would give about 50 (my arithmetic, not a reported result).

## Limits

- Answer-critical content is operationalized only through the known answer span; the paper concedes that finding minimal answer-critical units in arbitrary speech is hard.[^c8]
- The 0.5 credit for generic refusal and the harmonic mean are design choices; no sensitivity analysis to them was read.
- Repair is judged by one LLM (GPT-4o), which is also an evaluated model; judge agreement with humans was not examined in the slices read.
- Zero-shot, default prompts; how far prompting or training raises R was not tested in what I read. Masking type effects (silence, noise, music, speakers) appear in a figure whose values I did not fully parse.
- Spoken English QA only; whether the design transfers to text underspecification is not shown.

## Related

- [[underspecified-question-eager-answering]] — the same eager-answering failure in text multi-turn QA
- [[adversarial-unanswerable-questions]] — unanswerable inputs as a test, here with repair rather than refusal as the target
- [[wise-refusal]] — refusal versus constructive alternatives
- [[frame-level-answerability-labels]] — another answerability-as-input-property construction

[^c1]: arxiv-2601-12973 — "Answerability is thus defined as a property of the audio input itself, independent of model behavior."
[^c2]: arxiv-2601-12973 — "making the input intrinsically unanswerable even for a human listener (A(x) = 0)"
[^c3]: arxiv-2601-12973 — "Generic refusals (e.g., “I don’t know”) receive partial credit, while hallucinated or incorrect answers"
[^c4]: arxiv-2601-12973 — "This non-compensatory formulation ensures that high scores are achieved only when a model both"
[^c5]: arxiv-2601-12973 — "The judge produces categorical decisions only, reducing"
[^c6]: arxiv-2601-12973 — "Table 1: Repair-aware evaluation results across two spoken QA datasets."
[^c7]: arxiv-2601-12973 — "frequently fail to initiate repair once answer-critical"
[^c8]: arxiv-2601-12973 — "In practice, identifying minimal answer-critical"
