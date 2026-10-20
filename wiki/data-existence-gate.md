---
description: "Placing the reject option at retrieval: a question with no dataset behind it stops the pipeline before any analysis, and the benchmark scores that refusal as answerability accuracy."
aliases: ["k=0 termination", "no-relevant-dataset stop", "retrieval-stage refusal", "data-availability check"]
sources: ["arxiv-2602-00012"]
---
# Data-existence gate

A question put to a store of documents or datasets can be refused before any answer is written, by asking whether the store holds what the question needs. OGD4All, a system that answers citizens' questions about geospatial open government data, puts this check first. An LLM searches a metadata database for the datasets a question could use. If none of the retrieved datasets is relevant, the case is k = 0, and the authors use that case as the stop: "the case k = 0 is used as a termination criterion."[^g1] The reason they give is trust: "This is an important trust mechanism usually missing in typical LLM interfaces."[^g2] When no dataset is found, "this is communicated to the user, and the interaction ends, reducing the risk of hallucinations."[^g3]

## Mechanism

The gate is a yes-or-no test on the output of retrieval, not a score. It has no threshold to tune and no coverage to sweep, so the selective-risk quantities of [[abstention]] do not describe it. What it decides is whether the answerer may commit at all. The analysis step runs only on datasets that retrieval returned. If retrieval returned none, nothing is computed and the user is told so. My reading: the stop is placed upstream of generation, so the answerer never reaches the point where it would have to produce a number from data it does not have.

The gate also separates two errors that one correctness score would mix. A relevant dataset that retrieval missed and a question that has no dataset behind it can both end in a wrong or empty answer, but they call for different fixes. The first is a retrieval problem; the second is a correct stop. The paper does not show what the same system does without the gate, so whether an answerer would fabricate from unrelated data at the analysis step is not tested in the text.

## What is measured

The benchmark includes refusal cases: "The benchmark also includes 30 negative examples,"[^g4] "specifically questions where no answer exists based on the available data."[^g5] The gate is scored by one metric, "Accuracy of classifying whether a question can be answered with the available data or not."[^g6] It sits beside recall, the share of relevant datasets retrieved. Across the models tested, GPT-4.1 "achieves both the highest recall and answerability accuracy scores, reaching near-perfect rejection of unanswerable questions."[^g7] The authors give the reason for weighting these two numbers most: they "determine whether the system correctly grounds its responses in existing data rather than hallucinating unsupported content."[^g8]

The paper also states that training against human feedback can weaken this ability: "learning based on human feedback has been shown to even worsen it."[^g9] No source is cited at that sentence in the passage read, so it is the authors' claim, and this note does not test it.

## Limits

- The refusal is measured on 30 negative questions, inside a benchmark whose retrieval pool is "benchmark runs operate in a larger pool of 430 available datasets."[^g10] The passages read give no interval for these rates, only point values, and the pool is one city's open data.
- A missed dataset looks like an absent one at the gate. A false k = 0 refuses a question the store could answer. The paper reports recall and answerability as separate numbers, and the joint error at the gate is not shown. This is my inference from the metric definitions.
- Ambiguity is untested: "ambiguous or open questions and prompts was also not evaluated."[^g11] The gate is measured on questions with one unique answer, so it is unknown whether a vague question with partial data would be refused, answered, or sent back for clarification.
- No coverage curve is given. The gate does not state the price of refusing an answerable question, which is the price [[abstention]] asks the asker to name. This work does not name it.
- The gate depends on metadata as much as on the model: "all the metadata used in the prototype framework is in German."[^g12] A store described in another language, or with thin descriptions, may give a different gate, and this is not tested.

## Related

- [[abstention]] — the general reject option, of which this is one placement: before analysis, decided by whether the store holds the data
- [[stopping-rules]] — the gate is a stop that ends the interaction at one fixed case, k = 0
- [[referent-rejection]] — the same refusal to answer an ungroundable query, named there for a referent rather than a dataset store; I have not compared the two in detail
- [[text-answerability]] — whether a question can be answered without its source at all; the gate asks the related question of the store

[^g1]: arxiv-2602-00012 — "the case k = 0 is used as a termination criterion"
[^g2]: arxiv-2602-00012 — "This is an important trust mechanism usually missing in typical LLM interfaces"
[^g3]: arxiv-2602-00012 — "If no appropriate datasets are found, this is communicated to the user, and the interaction ends, reducing the risk of hallucinations"
[^g4]: arxiv-2602-00012 — "The benchmark also includes 30 negative examples"
[^g5]: arxiv-2602-00012 — "specifically questions where no answer exists based on the available data"
[^g6]: arxiv-2602-00012 — "Accuracy of classifying whether a question can be answered with the available data or not"
[^g7]: arxiv-2602-00012 — "achieves both the highest recall and answerability accuracy scores, reaching near-perfect rejection of unanswerable questions"
[^g8]: arxiv-2602-00012 — "they determine whether the system correctly grounds its responses in existing data rather than hallucinating unsupported content"
[^g9]: arxiv-2602-00012 — "learning based on human feedback has been shown to even worsen it"
[^g10]: arxiv-2602-00012 — "benchmark runs operate in a larger pool of 430 available datasets"
[^g11]: arxiv-2602-00012 — "ambiguous or open questions and prompts was also not evaluated"
[^g12]: arxiv-2602-00012 — "all the metadata used in the prototype framework is in German"
