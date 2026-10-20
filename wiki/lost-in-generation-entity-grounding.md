---
description: "Splitting evidence into sentences strips the entity that grounds pronouns; the answerer degrades even with gold evidence in context, and a subject-entity prefix recovers most of the loss"
aliases: ["lost-in-generation", "subject entity prefix", "pronoun grounding loss after sentence splitting"]
sources: ["doi-10-48550-arxiv-2609-06065"]
---
# Lost-in-generation entity grounding

In retrieval-augmented multi-hop QA, Lee and Lim (2026) argue that entity information is lost at two separate points: in retrieval, where a later sub-question refers to the entity resolved at the previous hop only by a pronoun, and in generation, where an isolated sentence no longer says whom its pronouns mean.[^c1] The second is the one that is easy to miss, because retrieval still appears to succeed and retrieval-side metrics cannot see it.[^c2]

## Mechanism

A passage is split into sentences to make retrieval finer. A sentence such as "He won the Academy Award for Best Actor..." then reaches the answering model without its antecedent. The model holds the correct evidence but cannot tell which entity it is about.[^c3] The remedy tested is small: an LLM extracts one subject entity per passage offline, and that entity is prepended to each retrieved sentence at generation time. The index is not changed.[^c4]

## What was measured

The retriever is bypassed. Each question's context is every annotated passage (gold plus distractors), presented in three forms: full passage, split sentences, and split sentences with the subject prefix. Because the passages are identical, differences come from presentation alone.[^c5] Splitting lowered F1 on all three datasets by 2.2 to 2.9 points. The prefix improved over the plain sentence by 1.6 to 3.2 F1 and returned to roughly the full-passage level.[^c6]

This reconciles an apparent contradiction: under ordinary retrieval, sentences beat passages. The paper's reading is that a finer unit helps retrieval but hurts generation, so the plain sentence's retrieval gain is partly cancelled. The prefixed sentence keeps the retrieval gain and repairs the generation side.[^c7]

Exact-match results in the same table are mixed (for example MuSiQue EM is 36.0 for plain sentences and 35.5 for prefixed ones), so the F1 recovery is the firmer finding.[^c8]

## Limits

- One subject entity per passage is reused for every sentence and every query. It cannot resolve coreference chains where a sentence is about some other entity, and the most useful entity varies in granularity with the query.[^c9]
- Only Wikipedia-derived benchmarks (MuSiQue, 2WikiMultiHopQA, HotpotQA) were tested; domain corpora are untested.[^c10]
- The controlled-context sample is small (the table's EM values move in steps of 0.5, consistent with about 200 questions; my inference), and the effect sizes are a few points.
- The headline gains quoted in the introduction (+9.24, +9.08, +5.18 EM) come from a different, retrieved-sentence setting than the controlled Table 2 numbers, which are smaller. Treat the smaller figures as the controlled estimate.[^c11]
- The work does not separate how much of the benefit is pronoun resolution and how much is just extra topical context in the prefix.

## Related

- [[evidence-chain-question-generation]] — also concerns carrying resolved evidence across hops
- [[plan-before-search-anchoring]] — anchoring later search steps on earlier-resolved content
- [[hop-depth-difficulty-with-entropy-check]] — decomposition depth in multi-hop questions
- [[claim-decoupled-reinterrogation]] — also relies on decontextualizing a statement before it is judged

[^c1]: doi-10-48550-arxiv-2609-06065 — "this loss breaks the pipeline at two separate points"
[^c2]: doi-10-48550-arxiv-2609-06065 — "invisible to retrieval-side metrics"
[^c3]: doi-10-48550-arxiv-2609-06065 — "the LLM can no longer tell who “He” refers to"
[^c4]: doi-10-48550-arxiv-2609-06065 — "an LLM extracts the subject entity of each passage offline"
[^c5]: doi-10-48550-arxiv-2609-06065 — "any difference in answer quality reflects how the evidence is presented rather than what was retrieved"
[^c6]: doi-10-48550-arxiv-2609-06065 — "Splitting a passage into sentences lowers F1 on all three datasets, by 2.2 to 2.9 points."
[^c7]: doi-10-48550-arxiv-2609-06065 — "a finer unit helps retrieval (Chen et al., 2024b) but hurts generation"
[^c8]: doi-10-48550-arxiv-2609-06065 — "Prefixed sentence 47.85 35.5 64.55 53.5 65.24 50.5"
[^c9]: doi-10-48550-arxiv-2609-06065 — "A passage-level entity also cannot resolve every"
[^c10]: doi-10-48550-arxiv-2609-06065 — "our evaluation is conducted"
[^c11]: doi-10-48550-arxiv-2609-06065 — "Prepending the"
