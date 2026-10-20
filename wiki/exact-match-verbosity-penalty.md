---
description: "Exact-match scoring gives 0 to a correct answer wrapped in explanatory prose while a judge gives it full credit; across nine LLMs the two scorers agree only at r = 0.175."
aliases: ["verbosity paradox", "response-format misalignment", "exact-match format penalty", "wrapped-answer scoring failure"]
sources: ["arxiv-2511-18302"]
---
# Exact-match verbosity penalty

A string-matching scorer asks whether the response equals the expected answer. When the expected answer is a short token and the response is a sentence that contains it, the scorer answers no. The mechanism is a mismatch between what the scorer accepts (a bare answer) and what a generative model is shaped to produce (a full explanatory reply). The work names the resulting effect the "Verbosity Paradox", a failure in which "models providing conceptually perfect answers receive zero scores due to response format misalignment".[^c1]

The smallest case is the author's own example. For the query "What is the capital of France?" with the expected answer "Paris", the response "The capital of France is Paris, which has been the country's capital since..." gets a binary score of 0, marked "failed exact match", and a judge score of 1.0, marked "correctly identified concept".[^c2][^c3] The content is the same in both scores. Only the scoring rule differs.

The measured consequence is a disconnect between the two scorers. Over 1,800 evaluations, the correlation between judge and binary scores is r = 0.175, and the author reads this as "only 3.1% of the variance in one scoring method is explained by the other".[^c4] The disconnect is largest on crystallized knowledge, where "every functional model achieved exactly 100% binary accuracy while judge scores ranged from 25%" to 62%.[^c5] Under exact match, a binary score of 1 needs a response close to the reference, so a response that is right in content but phrased at length falls on the zero side. The gap is therefore a joint property of the rule and the response style, not of the knowledge alone.

The paper's response-pattern table is consistent with this. It separates a "Verbose_explanatory" pattern from a concise one and lists the verbose pattern with the larger average accuracy gap (0.54 against 0.21 for the concise pattern, as extracted).[^c6] The column alignment in the extracted table is not certain; I read it this way (my inference).

The same kind of failure appears in [[alias-tolerant-answer-matching]], where exact match marks a right entity as wrong because of its spelling. Here it marks a right answer as wrong because of its wording. [[exact-match-versus-weighted-agreement]] covers a different defect of the same rule, that it counts every error alike.

What transfers to asking and answering is a point about the scorer, not the model. An answer that is correct and complete can be invisible to a rule that accepts only the bare token. Any evaluation that asks for an answer and then checks it by string equality inherits this gap (my inference).

## Limits

- The judge is a single model, Claude Sonnet 4, used as "universal judge for all nonAnthropic models".[^c7] The sections read report no human rater and no agreement figure for the judge, so it is not shown that the judge's score is the right one.
- The paper calls the Gc pattern "a statistical impossibility under valid measurement conditions".[^c8] That does not follow from the data. Where the binary score is 1, the response matches the expected answer exactly. A judge that gives such a response 0.5 or 0 is at odds with the reference, so the pattern points at least as much to judge error as to the scoring rule (my inference). The paper's own reading, "not a measurement failure but a fundamental category error", is an interpretation the numbers do not force.[^c9]
- Judge scores are "Bimodal distribution clustering at 0 and 1",[^c10] from one run per item. Repeated-run stability is not reported, and judges that assign numbers to identical inputs can vary between runs (see [[llm-judge-score-instability]]).
- The verbosity explanation is offered, not isolated. No run holds the content fixed and varies only the length. The judge is also known to favour longer answers ([[llm-judge-biases]]), so a length-sensitive judge could widen the gap in the opposite direction from the one the paper reports.
- The gap is measured on one benchmark of CHC-style items and nine models. The IQ-like and "Paradox Severity Index" figures built on it inherit the same scorer disagreement and are not validated here.

## Related

- [[alias-tolerant-answer-matching]] — exact match also fails a right answer by spelling; the alias set is the fix that work proposes
- [[exact-match-versus-weighted-agreement]] — the same exact-match rule, judged on how it counts errors rather than on wording
- [[output-accuracy-format-gap]] — a format gap of another kind: replies that are correct but not parseable
- [[llm-judge-biases]] — verbosity and position biases in the judge that scores such answers
- [[llm-judge-score-instability]] — repeated judge runs disagree, which bounds how far a single judge score can be trusted

[^c1]: arxiv-2511-18302 — "zero scores due to response format misalignment"
[^c2]: arxiv-2511-18302 — "The capital of France is Paris"
[^c3]: arxiv-2511-18302 — "correctly identified concept"
[^c4]: arxiv-2511-18302 — "only 3.1% of the variance in one scoring"
[^c5]: arxiv-2511-18302 — "every functional model achieved exactly 100% binary accuracy while judge scores ranged from 25%"
[^c6]: arxiv-2511-18302 — "Verbose_explanatory"
[^c7]: arxiv-2511-18302 — "Using Claude Sonnet 4 as universal judge for all nonAnthropic models"
[^c8]: arxiv-2511-18302 — "a statistical impossibility under valid measurement conditions"
[^c9]: arxiv-2511-18302 — "not a measurement failure but a fundamental category error"
[^c10]: arxiv-2511-18302 — "Bimodal distribution clustering at 0 and 1"
