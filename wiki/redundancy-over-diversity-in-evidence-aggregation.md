---
description: "Given grouped retrieved evidence against its prior, an LLM flips more often on paraphrases of one document than on distinct documents; balanced conflict attenuates this."
aliases: ["illusory truth effect in RAG", "repetition-as-consensus bias", "paraphrase persuasion", "context stuffing vulnerability"]
sources: ["arxiv-2601-06189"]
---
# Redundancy over diversity in evidence aggregation

A reader that weighed evidence rationally would value independent sources over one source repeated. Naphade (2026) tests this on GroupQA, 1,635 controversial yes/no questions with 15,058 web paragraphs labelled for stance (about 9.2 per question).[^c1] Each question's evidence is set against the model's own prior answer, and the number of documents is increased one at a time.

## What was measured

**Two conditions.** "Distinct" accumulates unique supporting documents. "Paraphrased" accumulates GPT-4o rephrasings of a single supporting document. Both oppose the prior. The outcomes are the flip rate (discrete answer inversion under greedy decoding) and the flip threshold X_min, the mean minimum number of documents needed to invert the answer.[^c2]

**Repetition wins.** DeepSeek-R1-8B flips in 67.6% of cases with distinct evidence and 76.5% with paraphrases; Gemini-2.5-Flash goes from 63.7% to 75.6%. The paper reports the trend across all four models tested.[^c3] The authors read this as an illusory-truth effect, borrowed from human psychology, in which repetition is conflated with consensus.[^c4]

**A crossover with quantity.** For Llama-3.1-70B, with 1 to 2 documents only distinct evidence initiates revision; as context grows, the redundant condition scales more steeply.[^c5] So the effect is a property of accumulation, not of the first document.

**Conflict attenuates it.** Starting from a balanced context (one supporting, one opposing document), models need more evidence to flip and flip rates fall substantially. Paraphrases show faster diminishing returns and distinct documents keep more causal impact, but this holds cleanly only for Llama-3.1-70B; smaller models sometimes still favor paraphrases.[^c6]

**Reasoning does not repair it.** Chain-of-thought changed the Yes probability by under 0.5 percentage points at all scales; the authors call such traces post-hoc rationalization.[^c7] Verbalized attribution is also unreliable: Llama-3.1-70B named the leave-one-out most decisive document on only 26% of questions.[^c8]

**Related findings in the same study.** Belief plasticity (mean absolute shift in P(Yes) after evidence) falls with parameter count, fitted as y = 0.180 x^-0.097 over 10 checkpoints (R2 = 0.472).[^c9] When prior-confirming evidence is placed first in a balanced pair, Llama-3.1-70B retains its prior 3.5% more often than with the reverse order, which the authors call primacy.[^c10]

## Limits

- Binary yes/no questions only; English web text with no source or date metadata; richer answer spaces and high-consensus domains (maths, logic) may differ.[^c11]
- Stance labels come from LLM judges (99% agreement on a 100-document manual check), so they proxy model-perceived stance, not truth.
- Only four models in the main table (8B to 70B plus Gemini); the scale trend rests on a noisy fit, and the mechanism (attention, circuits) is not analysed by the authors.
- The paraphrase set is generated from one document, so it confounds repetition with the quality of that one document; this confound is my observation, not tested.
- The remedies named (de-duplication, deliberately retrieving dissenting views, order randomization) are the author's suggestions, not evaluated here.

## Related

- [[reader-slot-zero-primacy]] — a separate measurement of position effects in retrieved-passage reading, with a slot-anchored rather than order-of-belief framing
- [[retrieval-permutation-hallucination]] — order of retrieved documents also changes outputs
- [[cot-mediation-index]] — how much a reasoning trace actually mediates the answer
- [[value-of-information]] — what independent evidence ought to be worth, which the heuristic ignores

[^c1]: arxiv-2601-06189 — "a curated dataset of 1,635 controversial questions paired with 15,058 diverselysourced evidence documents, annotated for stance and qualitative strength"
[^c2]: arxiv-2601-06189 — "we define the Flip Threshold,"
[^c3]: arxiv-2601-06189 — "DeepSeek-R1-8B flips in 67.6% of cases when provided with distinct evidence, but this rate jumps to 76.5% when exposed to paraphrased variations of a single document."
[^c4]: arxiv-2601-06189 — "suggesting that in long-context windows, LLMs conflate repetition with consensus."
[^c5]: arxiv-2601-06189 — "In the low-evidence regime (1–2 documents), distinct evidence (solid"
[^c6]: arxiv-2601-06189 — "However, this result is only consistent for"
[^c7]: arxiv-2601-06189 — "reasoning traces function primarily as posthoc rationalizations rather than corrective inference steps"
[^c8]: arxiv-2601-06189 — "Our results indicate that Llama-3.1-70B is faithful on"
[^c9]: arxiv-2601-06189 — "y = 0.180 · x−0.097"
[^c10]: arxiv-2601-06189 — "this primacy"
[^c11]: arxiv-2601-06189 — "Our analysis focuses on binary"
