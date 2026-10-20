---
description: "Preferences a user never states but reveals in unrelated tasks are read from history by interpreting them, not by holding more context: frontier LLMs reach only 37–48% on such items."
aliases: ["implicit personalization", "implicit persona inference", "cross-scenario preference inference"]
sources: ["arxiv-2512-06688"]
---
# Implicit preference inference

A constraint on an answer is often never stated by the person asking. It sits in an earlier exchange about something else: an email polished for a job application reveals a field of study, a translation request reveals a cuisine. The asker never opened a slot for that constraint. The answerer can fill it only by reading the trace and deciding what it says about this person. PersonaMem-v2 builds this situation as a benchmark. Each preference is embedded in an ordinary task, and "Each user preference is converted into a multi-turn conversation"[^c1] before a query is put to the model with four options, of which "only one is personalized to the current user."[^c2]

The measured result is a gap. Frontier models "still struggle with implicit personalization, achieving only 37–48% accuracy."[^c3] The authors place the difficulty in interpretation rather than in search or storage. Removing conversations irrelevant to the persona, which shortens a history from 128k to 32k tokens, gave "no significant accuracy improvement."[^c4] The leading models on the benchmark were the ones with strong reasoning.[^c5] The paper's summary is that "reasoning remains the bottleneck for implicit personalization,"[^c6] and the heading of its section puts it as "Reasoning, not long-context capabilities, drives success in implicit personalization."[^c7] The distinction matters for the mechanism: the failure is not that the evidence is out of reach, but that the evidence is not correctly read. The authors say the main bottleneck is "correctly interpreting and integrating subtle preference signals."[^c8]

Training on the same kind of material moves the number. A 4B reasoning model trained with GRPO, using verifiable reward on the multiple-choice items and an LLM judge on open-ended ones, reaches "reaching 53.8% on MCQ and 56.0% on openended tasks," while GPT-5-Chat "which achieves 45.6% and 46.2% on the same benchmarks."[^c9][^c10] The work reads the gain as learning to use subtle signals, not as learning to remember more.

The errors are not uniform across kinds of preference. Models do best where the preference fits a population prior: "Frontier models perform best when user preferences align with common stereotypes."[^c11] Accuracy falls for neutral preferences and falls further for anti-stereotypical ones, and the authors read this as "suggesting reliance on population priors rather than individual behavior."[^c12] Preferences that change across sessions score lower than stable ones, "indicating instability and difficulty updating beliefs as preferences change."[^c13] A third axis, whose preference a piece of evidence states, is treated in [[preference-ownership-attribution]].

The mechanism, as I read it (my inference, not tested in the paper): answering from implicit evidence has two steps. The answerer first picks out the scattered turns that bear on the query, then integrates them into a preference that applies to this query and this person. The benchmark scores only the final choice, so the intermediate reading is never observed, and it is in that reading that the prior can take over from the evidence.

## Limits

- The histories are synthetic. Each preference is turned into a conversation by a generation pipeline, and "all data generation and validation are conducted with GPT-5."[^c14] Whether real user histories show the same gap is not tested here; the authors name real interactions as a direction for later work.[^c15]
- Open-ended scores come from LLM judges, with "three independent GPT-5Chat instances score each response."[^c16] The paper itself notes that judge-based open-ended samples "can make reward signals less stable."[^c17]
- The claim that reasoning rather than context length drives success is a comparison across leading models plus one removal of distractor conversations. It is not a controlled intervention on reasoning length or on reasoning style, and the "reasoning" label is applied to whole models.
- Training uses a single base model, Qwen3-4B-Instruct-2507,[^c18] so the gain is not shown for other sizes or families.
- The benchmark tests how an assistant personalizes its own answer. It does not test an asker generating the constraints, nor a question-and-answer exchange in which the answerer may ask back. Any transfer to asking well is my extension, not a measured result.
- Subgroup cells have wide spreads; the anti-stereotypical and other-party cells in particular are noisy, so their gaps are less firm than the headline accuracy.

## Related

- [[preference-ownership-attribution]] — the same history must also say whose preference a piece of evidence is before it can constrain an answer.
- [[latent-intent-before-answer]] — the answerer writes candidate intents before answering; this note concerns where such intents come from when no one stated them.
- [[history-conditioned-intent-reconstruction]] — uses the user's history to make a vague request explicit; the history supplies the constraint directly here.
- [[revealed-preference-action-generation]] — a related finding that a user's own past choices predict the next choice better than what they say they want.
- [[compressed-memory-versus-raw-retrieval]] — whether the history is kept raw or distilled into a memory; a trained memory on this benchmark is recorded there.
- [[paired-stereotype-bias-score]] — scores the same prior-driven error as a signed bias over paired items, where this note reports it as an accuracy gap by preference type.

[^c1]: arxiv-2512-06688 — "Each user preference is converted into a multi-turn conversation"
[^c2]: arxiv-2512-06688 — "only one is personalized to the current user"
[^c3]: arxiv-2512-06688 — "frontier LLMs still struggle with implicit personalization, achieving only 37–48% accuracy"
[^c4]: arxiv-2512-06688 — "we observe no significant accuracy improvement when the context is shortened from 128k to 32k tokens"
[^c5]: arxiv-2512-06688
[^c6]: arxiv-2512-06688 — "reasoning remains the bottleneck for implicit personalization"
[^c7]: arxiv-2512-06688 — "Reasoning, not long-context capabilities, drives success in implicit personalization"
[^c8]: arxiv-2512-06688 — "correctly interpreting and integrating subtle preference signals"
[^c9]: arxiv-2512-06688 — "reaching 53.8% on MCQ and 56.0% on openended tasks"
[^c10]: arxiv-2512-06688 — "which achieves 45.6% and 46.2% on the same benchmarks"
[^c11]: arxiv-2512-06688 — "Frontier models perform best when user preferences align with common stereotypes"
[^c12]: arxiv-2512-06688 — "suggesting reliance on population priors rather than individual behavior"
[^c13]: arxiv-2512-06688 — "indicating instability and difficulty updating beliefs as preferences change"
[^c14]: arxiv-2512-06688 — "all data generation and validation are conducted with GPT-5"
[^c15]: arxiv-2512-06688
[^c16]: arxiv-2512-06688 — "three independent GPT-5Chat instances score each response"
[^c17]: arxiv-2512-06688 — "can make reward signals less stable"
[^c18]: arxiv-2512-06688 — "We start from Qwen3-4B-Instruct-2507 model"
