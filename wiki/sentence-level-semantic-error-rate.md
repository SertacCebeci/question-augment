---
description: "A binary, LLM-judged sentence-level metric for ASR meaning-preservation, contrasted with token-level WER/CER and stabilised by a three-round bidirectional voting protocol."
aliases: ["S2ER", "Sentence-level Semantic Error Rate"]
sources: ["jiang-2026-towards"]
---
# Sentence-level Semantic Error Rate (S2ER)

> Whether a transcription is usable does not track how many tokens it got
> wrong: S2ER scores one bit per utterance — did the meaning survive — and
> asks an LLM judge that bit three times, in both orders, to trust the
> answer.

## Definition / Mechanism

**Jiang, Zhu, Wang et al. (2026)** define S2ER over
$N$ utterances as $\mathrm{S^2ER} = \frac{1}{N}\sum_i (1-\hat z_i)$, where
$\hat z_i \in \{0,1\}$ indicates whether ASR hypothesis $Y_i$ is judged
semantically equivalent to the reference $Y_{GT,i}$: $\hat z_i$ measures
"whether the hypothesis preserves sufficient meaning for correct intent
execution," ignoring disfluencies, filler words and punctuation, so S2ER
measures the proportion of utterances whose transcriptions fail to
preserve intended meaning.[^c1]

To reduce order sensitivity in the LLM judge, the protocol queries the
judge twice per round with the pair's order reversed and counts the round
positive only if both orderings agree, then majority-votes across three
rounds: "To improve robustness and reduce order sensitivity, we adopt a
three-round bidirectional voting protocol."[^c2]

In a 120-utterance human–AI alignment study (25 non-expert annotators, 5
domain experts) across GigaSpeech, WenetSpeech and ASRU2019, the LLM
judge's correlation with the averaged human reference score exceeded 0.80
on every dataset and was slightly higher than the domain experts' own
correlation with that same reference.[^c3]

The same judge, applied round by round inside the paper's Interactive
Simulation System, doubles as a per-turn stopping test: a sample's
remaining rounds are marked successful the first round its S2ER label
turns positive, so S2ER supplies both a batch evaluation number and an
online stopping signal for the same underlying judgment.

## Why it matters

S2ER separates two things token metrics conflate: how much of the surface
form changed, and whether the change broke the intended meaning. A
transcription can have high WER from dropped filler words and be
semantically perfect, or have low WER with one substituted named entity
and be semantically broken — the paper's own contrast is that interaction
gains show up far more in S2ER than in WER/CER/MER, because iterative
correction mainly repairs the meaning-critical errors rather than
polishing surface form. For a wiki concerned with whether a returned
answer constitutes a real constraint (stall 5) and whether enough has been
gathered to stop (stall 7), S2ER is a worked instance of a computable,
LLM-judged [[sufficient-statistic|sufficiency]] test — one that only works because a ground-truth
reference $Y_{GT}$ exists to compare against.

## Transfer

| | |
|---|---|
| **Home field** | ASR evaluation: a reference transcript is known, and the question is whether a hypothesis matches it in meaning |
| **Here** | judging whether a received answer/response carries the meaning an asking system needs, as a stopping or acceptance test |
| **What survives** | binary functional-equivalence judgment via LLM-as-judge, with order-reversal and multi-round voting against judge instability |
| **What does not** | the reference-based setup itself — S2ER compares a hypothesis to a *known* ground truth $Y_{GT}$; an open-ended asking loop has no such reference to judge against, so the metric does not transfer without one |

## Limits

- Validated only against 120 hand-annotated utterances across three
  datasets (English, Mandarin, code-switching); the correlation-above-0.8
  claim does not extend past these conditions without further study.
- The judge and the correction-generating LLM in the paper's own pipeline
  are both instances of the same model family (Qwen3-32B), so the
  human-alignment check does not rule out shared blind spots between judge
  and corrector that a different judge model might expose.
- The "task-critical content" criterion is a binary label from a concise
  prompt specification, not an explicit rubric; graded partial-meaning
  loss is outside what the metric reports.

## Related

[[agentic-asr]] · [[clarification-benchmarks]] · [[final-sufficiency]] · [[sufficient-statistic]]

[^c1]: jiang-2026-towards — "where ẑi ∈ {0, 1} indicates whether ASR hypothesis Yi is semantically equivalent to reference YGT,i"
[^c2]: jiang-2026-towards — "To improve robustness and reduce order sensitivity, we adopt a three-round bidirectional voting protocol, following the LLM-as-a-Judge stability practices discussed in Section II-C."
[^c3]: jiang-2026-towards — "Table I shows that the LLM Judger tracks human semantic judgments reliably across all three datasets. Its correlation with the human reference scores remains above 0.8 throughout, and it is consistently slightly higher than that of the domain experts."
