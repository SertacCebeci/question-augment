---
description: "Conditioning answer correctness on evidence recall separates retrieval failure from synthesis failure in agent QA, exposing models with equal accuracy but opposite bottlenecks."
aliases: ["conversion rate", "recall-conditioned accuracy", "retrieval-versus-synthesis decomposition"]
sources: ["doi-10-48550-arxiv-2609-34428"]
---
# Recall-gated conversion rate

A single accuracy score for a tool-using question-answering agent mixes two different failures: never reaching the evidence, and reaching it but not combining it. AgentHop splits them with two metrics computed on the same run. Paper recall asks whether the agent obtained the gold evidence; conversion rate is P(correct | recalled).[^c1] "Because the denominator is gated on recall, conversion isolates the synthesis ability from retrieval."[^c2]

## Mechanism

Reading the two together gives profiles a one-number score hides. High recall with low conversion means the model "can locate the evidence but cannot combine it"; low recall with high conversion means its "accuracy ceiling is set by retrieval rather than by reasoning".[^c3]

The paper crosses recall with conversion on 19 models and finds three profiles. Synthesis-bottlenecked models reach gold papers at open-frontier rates but lose conversion when two papers must be combined (MiniMax-M2.7 drops 17 points from single-target to multi-target conversion; Kimi-K2.5 drops 11). Retrieval-bottlenecked models show the inverse: Gemma-4-31B converts 0.861 where it finds both gold papers, despite a 0.521 multi-target recall ceiling. Floor models fail at reaching papers before either axis matters.[^c4]

The same decomposition separates models that tie on accuracy. Claude Opus 4.6 and Sonnet 4.6 land within one accuracy point yet differ, with Opus retrieving more and Sonnet synthesizing better.[^c5]

Which axis carries information depends on tier. Recall discriminates in the middle and bottom of the panel, and its closed-frontier range is narrow (0.71 to 0.83). Conversion separates frontier models sharply (Pro 0.96, Opus 0.86) but compresses at the bottom, where few samples satisfy recall and the denominators are small.[^c6]

For asking and answering, the point is that "was the evidence found" and "was it used correctly" are separately measurable, so a wrong answer does not by itself say which to fix. That reading is mine; the paper states it as a developer's need to know "which stage is binding".[^c7]

## Limits

- The conversion estimate rests on the recall gate. Paired same-item tests could order only the extremes; the four middle checkpoints formed a cluster that could not be ordered at n of about 200.[^c8]
- Behavioral findings are correlational: trajectory data cannot show that a pattern causes an accuracy level.[^c9]
- Recall is judged by delivered paper or section content from a seven-tool sandbox over arXiv citation chains, with multiple-choice answers. Whether conversion means the same thing for open-ended answers or other corpora is untested here. Multiple-choice guessing could inflate conversion; I did not find the paper correcting for it.
- Results characterize model plus serving interface, not the model alone.

## Related

- [[verification-aware-stopping]] — decides when evidence suffices to stop; recall is the quantity such a stop rule tries to certify
- [[search-decision-boundary-misalignment]] — search too much or too little as a calibration failure, adjacent to the over-search and early-commit signatures
- [[second-pass-gain-decomposition]] — another splitting of a single accuracy gain into parts
- [[evidence-chain-question-generation]] — building multi-hop questions with known gold evidence, which recall needs

[^c1]: doi-10-48550-arxiv-2609-34428 — "Conversion rate is P (ci = 1 | ri = 1): among samples on which"
[^c2]: doi-10-48550-arxiv-2609-34428 — "Because the denominator is gated"
[^c3]: doi-10-48550-arxiv-2609-34428 — "can locate the evidence but cannot combine it"
[^c4]: doi-10-48550-arxiv-2609-34428 — "Gemma-4-31B converts"
[^c5]: doi-10-48550-arxiv-2609-34428 — "Opus retrieving more and Sonnet synthesizing better"
[^c6]: doi-10-48550-arxiv-2609-34428 — "but compresses at the bottom where recall denominators are small"
[^c7]: doi-10-48550-arxiv-2609-34428 — "needs to know"
[^c8]: doi-10-48550-arxiv-2609-34428 — "pairwise testing cannot order at n ≈ 200"
[^c9]: doi-10-48550-arxiv-2609-34428 — "trajectory data alone cannot establish that a particular tool-use pattern causes a particular accuracy level"
