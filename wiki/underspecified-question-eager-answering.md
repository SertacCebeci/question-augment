---
description: "Most LLMs answer underspecified multi-turn questions from a plausible assumed reading instead of asking back; clarification turns also score below follow-ups in MTRAG-UN."
aliases: ["underspecified question handling", "answer-eagerness under ambiguity", "unclear response clarification", "under-clarification bias"]
sources: ["arxiv-2602-23184", "arxiv-2512-21120", "arxiv-2512-21345"]
---
# Underspecified question eager answering

An underspecified question is "ill-formed or ambiguous, lacking the information to determine a clear intent". The desired behavior is to detect this and go back to the user, "either by pointing out missing details, presenting several plausible interpretations, or listing options based on the underlying passages", rather than guess or say "I don't know".[^c1]

## What was measured

MTRAG-UN built underspecified items two ways: annotators wrote conversations ending on an underspecified question, or a human-written underspecified question was stitched as the last turn onto an existing conversation, with passages for several interpretations added by query expansion.[^c2] A clarification judge (GPT-OSS-120B) was built for these items; its accuracy on 80 sampled responses was 96.2%.[^c3]

Across 14 models, performance on underspecified questions was "consistently low, as models are generally eager to answer based on a plausible but assumed interpretation of the question."[^c4] This held even though the generation prompt was extended with a sentence telling the model to say that clarification is needed for underspecified questions.[^c5] By contrast, DeepSeek-V3 and GPT-OSS models handled unanswerable questions comparatively well by saying "I don't know", so declining and asking back are separable skills.[^c6]

A second finding concerns the user's side: when a user disagrees with or misunderstands an answer (an unclear response, e.g. contesting where a show was filmed), models did worse than on ordinary follow-ups. The authors read this as models being "better at conversational continuation than for intent refinement and self-correction."[^c7]

The same answer-eagerness appears in multi-turn dialogues with simulated users. ClarifyMT-Bench evaluates representative LLMs on ask-or-answer decisions and names the pattern under-clarification bias. Accuracy falls on later turns, and the authors state that multi-turn clarification "compounds reasoning difficulty."[^c9] Their summary is that "Most LLMs exhibit a strong tendency to underclarify as dialogue depth increases, particularly for smaller models."[^c10] The measure there is the ask-or-answer decision, not the quality of a question, so a turn answered early where a question was needed counts as an under-clarification error ([[ask-answer-error-direction]]).

A structured-query setting shows a related pattern (my reading; the authors do not frame it this way). In a text-to-SQL pipeline over a biomedical database, the generator "often generated SQL referencing one fitting column without recognizing ambiguity," so a question with several plausible columns was answered from one of them, and column-ambiguous questions reached at most 0.3 accuracy.[^c11]

## Limits

- The paper reports the pattern in a figure and in prose; per-model underspecified scores are not tabulated in the text, so the size of the gap is not quoted here.
- One added prompt sentence was tried; no other elicitation or training was compared, so how far prompting can close the gap is unknown.
- English, six closed domains, a small annotator pool; stitched last-turn questions may be artificial.[^c8]
- The "eagerness" explanation is the authors' interpretation, not an isolated mechanism.

## Related

- [[ambiguity-graded-response-strategy]] — grading response by degree of ambiguity
- [[result-divergence-clarification-trigger]] — a rule for when to ask back
- [[adversarial-unanswerable-questions]] — the unanswerable case, which this benchmark finds some models now handle
- [[non-standalone-question-retrieval-gap]] — the retrieval-side challenge in the same benchmark

[^c1]: arxiv-2602-23184 — "either by pointing out missing details, presenting several plausible interpretations, or listing options based on the underlying passages"
[^c2]: arxiv-2602-23184 — "an underspecified question (also written by a human) was stitched as a last turn on an existing human annotated multi-turn conversation"
[^c3]: arxiv-2602-23184 — "Its accuracy on 80 random llama-4 and gpt-oss-120b model responses from underspecified instances is 96.2%."
[^c4]: arxiv-2602-23184 — "Performance on underspecified question is consistently low, as models are generally eager to answer based on a plausible but assumed interpretation of the question."
[^c5]: arxiv-2602-23184 — "include that further clarification/information is needed from the user in your response."
[^c6]: arxiv-2602-23184 — "DeepSeek-V3 and GPT-OSS models exhibit comparatively robust behavior by frequently responding with IDK."
[^c7]: arxiv-2602-23184 — "This suggests that current models are better at conversational continuation than for intent refinement and self-correction."
[^c8]: arxiv-2602-23184 — "Our conversations are limited to English and 6 closed domains."
[^c9]: arxiv-2512-21120 — "showing that multiturn clarification compounds reasoning difficulty"
[^c10]: arxiv-2512-21120 — "Most LLMs exhibit a strong tendency to underclarify as dialogue depth increases, particularly for smaller models."
[^c11]: arxiv-2512-21345 — "text-to-SQL often generated SQL referencing one fitting column without recognizing ambiguity"
