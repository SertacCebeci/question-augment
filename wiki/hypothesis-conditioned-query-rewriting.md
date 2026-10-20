---
description: "Forming a working answer hypothesis first, then rewriting retrieval into support, distinction and clue-verification queries, retrieves decision-useful evidence rather than topical background."
aliases: ["HCQR", "hypothesis-conditioned query rewriting", "decision-useful retrieval", "three-role query rewriting"]
sources: ["arxiv-2603-19008"]
---
# Hypothesis-conditioned query rewriting

> Ask the corpus what would decide between the options, not what the topic is.

## Mechanism

When a task is a choice among competing options, a single query built from the question tends to return topically related background that does not discriminate between the options. Under a bounded context, such passages occupy scarce evidence slots and displace stronger evidence.[^c1] The difficulty is then mismatched evidence, not only missing knowledge.

Hypothesis-Conditioned Query Rewriting (HCQR) is a training-free, two-stage, pre-retrieval step. A hypothesis formulator reads the question and the candidate options and proposes a working hypothesis. It also names the key discriminating feature and the evidence expected if the hypothesis is true. A query rewriter then turns that state into exactly three queries. One seeks evidence supporting the hypothesis, one seeks evidence distinguishing it from competing alternatives, and one verifies salient clues in the question.[^c2] By default the hypothesis only steers retrieval and is not shown to the final generator, which keeps the method retrieval-side and reduces direct answer anchoring.[^c3]

The generator can then confirm or overturn the hypothesis from what comes back. The paper defines a context-utility labelling (entailed, useful-but-not-entailed, not useful) and a Decision-Useful Rate, the share of retrieved sets that are entailed or useful. It reports that HCQR raises that rate and sharply cuts not-useful contexts.[^c4]

## What was measured

On medical multiple-choice QA, simple single-query RAG underperformed no-retrieval chain-of-thought in every reported configuration.[^c5] HCQR was the strongest method in every dataset-model cell, with average gains over simple RAG of 5.9 points on MedQA and 3.6 on MMLU-Med.[^c6]

Reranking and filtering baselines did worse. The rerank baseline inspects a larger candidate pool yet stays weaker under the same final-context budget.[^c7] The authors read this as evidence that post-hoc selection is bounded by the quality of the first-pass pool, so retrieval should be steered toward decision-relevant evidence from the start.[^c8]

Two controls separate the parts. Giving a generic multi-query rewriter the answer options gave only a modest gain, so exposure to the options does not explain the benefit.[^c9] In the query ablation (MedQA, MMLU-Med), dropping the support query cost the most, from 75.0 to 72.4 and from 81.1 to 79.0. Dropping the distinction query (73.2, 80.1) or the key-feature query (73.0, 80.5) also lowered accuracy.[^c10] The authors take the three roles as complementary, and the roles are not interchangeable.[^c11]

## Limits

The evidence is medical multiple-choice QA only. The paper says medicine is a sharp testbed, not a unique one. Whether the three roles transfer to open-ended questions, where no option list seeds the hypothesis, is untested here. The hypothesis is formed with the options visible, so the method presupposes a closed candidate set. The gains are a few accuracy points and come from one author group's pipeline. The "decision-useful" labels are model-judged, and I have not checked how reliable that judge is. The mechanism story (hypothesis-first queries shift evidence composition) is the authors' reading of the label shift and the ablations. It is not an isolated causal test.

## Related

- [[contrastive-hypothesis-retrieval]] — also builds retrieval from a target hypothesis plus a named rival; it subtracts the rival in score space, while HCQR spends a separate query on the distinction.
- [[differential-questioning]] — asking what separates the leading candidates is the same move as the distinction query.
- [[hypothesis-testing]] — the working hypothesis is confirmed or overturned by evidence fetched to test it.
- [[verification-over-invention]] — retrieval aimed at checking a stated claim rather than generating new content.

[^c1]: arxiv-2603-19008 — "displace stronger evidence, and encourage weakly"
[^c2]: arxiv-2603-19008 — "(1) support the hypothesis, (2) distinguish it from competing alternatives, and (3)"
[^c3]: arxiv-2603-19008 — "the final generator. This keeps the method retrievalside by construction and reduces direct answer anchoring."
[^c4]: arxiv-2603-19008 — "HCQR achieves the"
[^c5]: arxiv-2603-19008 — "simple single-query RAG underperforms no-retrieval CoT in every reported model"
[^c6]: arxiv-2603-19008 — "5.9 points on MedQA and 3.6 points on MMLUMed"
[^c7]: arxiv-2603-19008 — "yet remains weaker under the same final-context budget."
[^c8]: arxiv-2603-19008 — "it is crucial to steer retrieval toward decisionrelevant evidence from the start rather than rely on"
[^c9]: arxiv-2603-19008 — "the benefit of HCQR is not explained by answeroption exposure alone."
[^c10]: arxiv-2603-19008 — "HCQR − q1 (Support)"
[^c11]: arxiv-2603-19008 — "removing q2 or q3 also degrades performance."
