---
description: "In a specialist-domain benchmark, tasks demanding exact verbatim knowledge fail and fabricate more than harder open-ended reasoning tasks, where models project competence by generalizing."
aliases: ["non-monotonic difficulty", "verbatim-knowledge hallucination gap"]
sources: ["arxiv-2602-21226"]
---
# Exactness-demand difficulty inversion

Difficulty as a human expert rates it does not predict where a model fails. In IslamicLegalBench (718 instances, 13 tasks, 9 LLMs, 38 texts across seven schools), moderate-complexity tasks that need exact, verbatim knowledge show consistently high error. Examples are enumerating contract conditions and synthesizing statutory articles. Their hallucination rates reach up to 73%. High-complexity tasks do better, because models rely on semantic generalization and verbose reasoning, "projecting competence while lacking precise textual understanding".[^c1]

Source Attribution reaches only 23-47% correctness even among leading models. Condition Enumeration and Comparative Distinction similarly constrain every system.[^c2] A high-complexity task such as Maxim Mapping draws minimal hallucination, while the exactness-demanding moderate tasks draw substantially more fabrication. The authors summarize this as models that "reason extensively about abstract legal principles without hallucinating, but systematically invent precise conditions when lacking training exposure".[^c3]

For asking and answering, the consequence is that the form of a question matters more than its apparent depth. A question with a closed, checkable answer (a list, a citation, a distinction) exposes missing knowledge. An open question about principles hides it behind fluent reasoning. A fluent, long answer is therefore weak evidence of knowledge. This reading is mine, drawn from the paper's pattern.

The same work reports that few-shot prompting gives minimal benefit: only 2 of 9 models improve by more than 1%. The authors conclude that prompting cannot compensate for absent foundational knowledge.[^c4] They also report confident incorrectness (correctness below 50%, hallucination above 25%, abstention below 1%).[^c5] Models fail on exact items and almost never decline.

## Limits

- One domain (Islamic jurisprudence), one benchmark, with complexity tiers assigned by a human expert. The authors' explanation, reliance on semantic generalization, is an interpretation and was not tested by intervention.
- Hallucination is scored by an LLM judge plus expert review. The inversion could partly reflect how strict the scoring is on exact items versus open ones.
- The result is silent on whether retrieval removes the gap.

## Related

- [[calibration]] — near-zero abstention on exact items is a calibration failure
- [[skepticism-trap]] — another way fluent responses mislead about competence
- [[over-reliance-discrimination-failure]] — fluent wrong answers are hard for users to discriminate
- [[wise-refusal]] — what declining would look like on the failing items

[^c1]: arxiv-2602-21226 — "projecting competence while lacking precise textual understanding"
[^c2]: arxiv-2602-21226 — "Source Attribution (T5) achieves only 23-47%"
[^c3]: arxiv-2602-21226 — "Models can reason extensively about abstract legal principles without hallucinating, but systematically invent precise"
[^c4]: arxiv-2602-21226 — "prompting cannot compensate for absent foundational"
[^c5]: arxiv-2602-21226 — "confident incorrectness (correctness <50%, hallucination >25%, abstention <1%)"
