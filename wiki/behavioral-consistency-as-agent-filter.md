---
description: "Agreement across repeated agent runs predicts failure better than verbalized confidence and works as an abstention filter, but not as a voting aggregator, because agentic errors are systematic."
aliases: ["behavioral consistency", "agent run agreement score", "consistency as filter not aggregator"]
sources: ["arxiv-2602-11619"]
---
# Behavioral consistency as an agent filter

Run the same ReAct-style agent k times on one task at fixed temperature. The agreement score is the fraction of runs giving the plurality answer; the paper also counts unique action sequences, step-count spread and the first step where runs diverge. Tasks are admitted only when agreement passes a threshold, which is selective classification applied to a multi-step agent.[^c1]

## What was measured

Across 8,000 runs of four models, tasks with at most 2 unique action sequences were 82-87% correct, tasks with 4 or more were 41-65% correct, and the gap was significant for every model.[^c2] As a failure detector, consistency features gave AUROC 0.62-0.78.[^c3] Against a post-hoc 0-100 verbalized self-rating, behavioral agreement won for all three models tested (for example Llama 0.739 vs 0.481), and combining them did not beat behavioral alone.[^c4]

## Filter, not aggregator

In single-turn chain-of-thought, majority voting adds 5-17 points. Here voting added only 0-2 points, since "agentic errors are systematic: an early wrong action commits the agent to an incorrect trajectory". Answering only when all three runs agree gave 87-88% accuracy at 54-62% coverage for three models.[^c5] The outcome split is a 2x2: consistent-correct, inconsistent-wrong (rightly excluded), inconsistent-lucky, and consistent-wrong, which filtering cannot remove. 61% of Claude's errors were consistent-wrong against 25% of Llama's, which is why Llama gains most from voting.[^c6]

## Difficulty confound

Task difficulty drives both consistency and correctness. Controlling for it, the gap shrank; partial correlations stayed significant for three of four models but not for Claude, which is near ceiling. On hard tasks the gap reversed under fuzzy matching, but about 30% of those cases were surface-form false negatives, and under token F1 the gaps were non-negative.[^c7]

## Why it matters for asking and answering

Agreement is a confidence signal that needs no logits and no self-report. It detects instability, not truth: a stable wrong trajectory passes the filter. This is the same split as in [[inconsistency-penalized-confidence]], where self-consistent wrong answers still scored high. The cost is k times the compute (k = 3 here).[^c8]

## Limits

- Benchmark is HotpotQA-style question answering with a fixed corpus and stateless tools; the paper claims cross-benchmark stability on a smaller coding set, which I did not read.
- The i.i.d. assumption behind the concentration bound holds only for independent runs without shared state.
- Tests were uncorrected for multiple comparisons in the main text (Holm correction was applied to the four gap tests only), and one annotator judged the false negatives.
- Verbalized-confidence comparison covers three models and 100 questions; AUROC differs between subsets.
- Consistent-wrong tasks (5.5-10%) cap what any agreement filter achieves.

## Related

- [[self-consistency-difficulty-score]] — agreement among samples used as a difficulty signal.
- [[inconsistency-penalized-confidence]] — consistency shrinks confidence but cannot detect confidently wrong answers.
- [[calibration]] — the property a verbalized rating fails here.
- [[score-separability]] — ranking quality the agreement score supplies for abstention.
- [[trajectory-uncertainty-quantification]] — uncertainty at the trajectory level.

[^c1]: arxiv-2602-11619 — "We formalize behavioral consistency within the selective"
[^c2]: arxiv-2602-11619 — "consistent tasks (≤2"
[^c3]: arxiv-2602-11619 — "consistency metrics achieve AUROC 0.69–0.78"
[^c4]: arxiv-2602-11619 — "combining the two does not improve over behavioral consistency"
[^c5]: arxiv-2602-11619 — "agentic errors"
[^c6]: arxiv-2602-11619 — "61% of Claude’s errors are consistent-wrong vs."
[^c7]: arxiv-2602-11619 — "confirming that the reversal is a fuzzy-match artifact"
[^c8]: arxiv-2602-11619 — "The computational cost of k = 3 runs is 3× the single-run"
