---
description: "Before any answer, a gate decides whether an utterance is a query at all, judging its form, speaker and dialogue history rather than the answerer's confidence."
aliases: ["utterance rejection", "invalid-query rejection", "front-gate rejection", "should-reject decision", "voice-assistant rejection"]
sources: ["arxiv-2512-10257"]
---
# Query rejection — deciding whether an input is a query at all

Before an assistant answers, it has to decide whether an utterance is a query to be processed at all. The authors state the ordering directly: "Hence rejection should serve as a front-gate of the task pipeline, not a post-hoc" patch.[^c1] The gate runs first, and its output is a binary label per input, accept or reject. The label is set against a taxonomy of input types, not against how sure the system is of an answer. That is the difference from [[abstention]], which declines an answer after the question has been taken as one.

**What triggers a rejection.** The triggers are of three kinds. Some are about the form of the sound or words: non-human sounds, and "ASR-error garbled" or meaningless short phrases. The paper labels "Even highly human-like synthetic speech" as rejection.[^c2] Some are about who is being addressed: a user who "chats with others or talks to him/herself after the wake-word has been triggered" produces speech that the authors call "irrelevant to voice interaction."[^c3] Some are about feasibility: a command with clear intent that is unreasonable is rejected, in the paper's words "Commands that show clear intent but are unreasonable."[^c4]

**The same surface form can flip with dialogue state.** An ambiguous small-talk utterance with no prior valid command is rejected. The same kind of ambiguous utterance, when the history already contains a valid command, is accepted, because "the current utterance may supplement it or introduce a new one."[^c5] The gate therefore reads the input against its context, not the sentence alone. This is the point where query rejection and ordinary intent recognition come apart: an utterance can be a clear intent in isolation and still be rejected for its place in the conversation, and the reverse.

**The method stacks three parts on a small model.** A Qwen-2.5-3B adapter is fine-tuned on accept and reject samples "balanced 1:1."[^c6] Second, the household's recent dialogue is put into the prompt, to capture family-specific habits. Third, the household keeps a store of past errors, described as "utterances that should have been accepted but were wrongly rejected," and the top three similar cases are retrieved by RAG and appended to the prompt for each new input.[^c7] The second and third parts are the paper's proposal for personalization. They are a mechanism for correcting over-rejection per household, and they are the part of the design that changes over time.

**What was measured.** The authors report the highest weighted accuracy for their full method: "Best Model: The Improved Method has the highest accuracy rate at 96.75%."[^c8] The runner-up is a fine-tuned 3B model with the optimized prompt, at "a accuracy rate of 96.44%."[^c9] That gap is 0.31 points by my arithmetic. Zero-shot large models vary widely and fail on the harder subsets. One model "falls to 0.000 on subset 2" under the generic prompt, which the authors read as "indicating extreme sensitivity to noisy home-scene inputs."[^c10] On speech, a multimodal model is "consistently achieving accuracies above 0.85" on subsets 1 to 6[^c19] but "its performance sharply declines on subsets 8–11 (as low as 0.0322)."[^c11]

## Limits

- The text read does not isolate the history module or the bad-case retrieval. The comparisons are between models and between prompts, and the full method is set against a fine-tuned baseline that differs by 0.31 points. The abstract's "significantly outperforms" is not backed by a significance test in the text (my inference). Whether each added layer helps is not tested here.
- The taxonomy is counted inconsistently. The abstract speaks of "twelve typical dialogue types"[^c12], the body says the dataset "covers 13 categories of invalid queries"[^c13], and Table 1 lists IDs 0 to 11. The class boundaries are the authors' design, and the benchmark measures agreement with that design, not what users want. The authors themselves say that "evaluation must" "go beyond accuracy and incorporate subjective user experience (e.g., sense of disturbance, trust) and behavioral" measures.[^c14]
- The command categories are defined relative to one manufacturer's supported functions: "Mainstream command type supported by the brand."[^c15] A label of "supported" moves with the vendor's device list, so the boundary is not a property of language alone.
- The speech set is synthetic: "The speech data are synthesized from the text corpus via text-to-speech (TTS)."[^c16] It tests TTS-voiced inputs, not recordings from a household. The text is from one vendor's online logs, and the benchmark is described as "Chinese-oriented."[^c17] Transfer to other languages or device ecosystems is not tested.
- A store of past errors can drift. The authors name it as open: "how to prevent model drift caused by accumulated false feedback."[^c18]

## Related

- [[abstention]] — a confidence-gated reject option declines an answer to a question; query rejection gates the input before any answer, on its form and history, so the two triggers can disagree.
- [[referent-rejection]] — the same "no" move, here triggered by a description that has no referent in the scene.
- [[act-silent-stop-decomposition]] — proactive intervention scored as act, stay silent, or stop; the silent outcome there is the non-response this gate produces.
- [[context-gated-query-rewriting]] — a history-conditioned reject outcome on query rewriting, the same use of dialogue history to decide whether to act.

[^c1]: arxiv-2512-10257 — "Hence rejection should serve as a front-gate of the task pipeline, not a post-hoc"
[^c2]: arxiv-2512-10257 — "Even highly human-like synthetic speech is treated as rejection."
[^c3]: arxiv-2512-10257 — "the recorded speech is irrelevant to voice interaction."
[^c4]: arxiv-2512-10257 — "Commands that show clear intent but are unreasonable."
[^c5]: arxiv-2512-10257 — "valid command; the current utterance may supplement it or introduce a new one."
[^c6]: arxiv-2512-10257 — "Acceptance and rejection samples are balanced 1:1."
[^c7]: arxiv-2512-10257 — "utterances that should have been accepted but were wrongly rejected"
[^c8]: arxiv-2512-10257 — "Best Model: The Improved Method has the highest accuracy rate at 96.75%."
[^c9]: arxiv-2512-10257 — "Second Best Model: Qwen-2.5-3B (Instruct, Opt. Prompt SFT) has a accuracy rate of 96.44%, closely following"
[^c10]: arxiv-2512-10257 — "indicating extreme sensitivity to noisy home-scene inputs"
[^c11]: arxiv-2512-10257 — "its performance sharply declines on subsets 8–11 (as low as 0.0322)"
[^c12]: arxiv-2512-10257 — "systematically cover twelve typical dialogue types"
[^c13]: arxiv-2512-10257 — "covers 13 categories of invalid queries"
[^c14]: arxiv-2512-10257 — "go beyond accuracy and incorporate subjective user experience (e.g., sense of disturbance, trust) and behavioral"
[^c15]: arxiv-2512-10257 — "Mainstream command type supported by the brand."
[^c16]: arxiv-2512-10257 — "The speech data are synthesized from the text corpus via text-to-speech (TTS)"
[^c17]: arxiv-2512-10257 — "Chinese-oriented open-source benchmark"
[^c18]: arxiv-2512-10257 — "how to prevent model drift caused by accumulated false feedback"
[^c19]: arxiv-2512-10257 — "consistently achieving accuracies above 0.85"
