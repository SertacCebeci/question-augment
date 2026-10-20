---
description: "Unanswerable questions written adversarially to resemble answerable ones expose unreliable guessing in extractive QA; a model at 86% F1 on SQuAD falls to 66% once abstention is required."
aliases: ["SQuADRUn", "SQuAD 2.0", "unanswerable questions for SQuAD"]
sources: ["rajpurkar-2018"]
---
# Adversarial unanswerable questions

Extractive reading-comprehension systems can often locate the correct answer in a context document, but they tend to make unreliable guesses when the answer is not stated there.[^c1] Datasets that contain only answerable questions never test this, and datasets whose unanswerable questions are generated automatically are easy to spot, so they test little.[^c2]

The remedy (Rajpurkar, Jia and Liang, 2018) is a test set built so that unanswerability cannot be read off the surface of the question. Crowdworkers wrote more than 50,000 unanswerable questions adversarially, to look similar to answerable ones, and these were combined with the existing SQuAD questions (the resulting dataset is called SQuADRUn).[^c3] A system now has two jobs: answer when it can, and decide when no answer is supported by the paragraph and abstain.[^c4]

The measured effect is large. A strong neural system that scores 86% F1 on SQuAD scores only 66% F1 on SQuADRUn.[^c5] The twenty-point drop is the cost of having no mechanism that distinguishes "the context supports an answer" from "a plausible span exists". For anyone asking or answering, the point is that a question can be well-formed, topical and near-identical to answerable ones while having no answer in the given material. Whether it is answerable is a relation between question and evidence, not a property of the question's wording.

## Limits

The text available here is the abstract and bibliographic metadata only; the construction protocol, annotator instructions, baselines other than the one quoted, and error analysis were not read. The result is for extractive QA over single Wikipedia paragraphs, with one strong system; it does not show how generative models or retrieval settings behave. The paper does not say what kinds of adversarial edits crowdworkers used. The 66% F1 mixes answering and abstention errors, so it does not separate them.

## Related

- [[false-premise-question]] — a different source of unanswerability, where the question presupposes something untrue
- [[two-stage-abstention-paradigm]] — abstention as a separate decision from answering
- [[gated-answerability-rule]] — gating an answer on whether the evidence supports one
- [[clarification-benchmarks]] — benchmarks that test the decision not to answer directly

[^c1]: rajpurkar-2018 — "they also tend to make unreliable guesses on questions for which the correct answer is not stated in the context"
[^c2]: rajpurkar-2018 — "Existing datasets either focus exclusively on answerable questions, or use automatically generated unanswerable questions that are easy to identify."
[^c3]: rajpurkar-2018 — "over 50,000 unanswerable questions written adversarially by crowdworkers to look similar to answerable ones"
[^c4]: rajpurkar-2018 — "systems must not only answer questions when possible, but also determine when no answer is supported by the paragraph and abstain from answering"
[^c5]: rajpurkar-2018 — "a strong neural system that gets 86% F1 on SQuAD achieves only 66% F1 on SQuADRUn"
