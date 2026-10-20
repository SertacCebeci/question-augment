---
description: "Judging every pair of a group's rollouts under each rubric turns each rollout into a vector of win fractions, keeping its relative quality per criterion instead of one pointwise score."
aliases: ["rollout-by-rubric win-rate matrix", "pairwise rubric win matrix", "rubric-wise pairwise win profile"]
sources: ["doi-10-48550-arxiv-2610-00389"]
---
# Rollout-by-rubric win matrix

Take a group of G sampled responses to one prompt and K rubrics. A judge compares every pair of responses under each rubric and records a win, a loss or a tie, with a tie counting as half a win.[^c1][^c2] Each response then has, for each rubric, the fraction of the other G−1 responses it beats. Stacked, these fractions form a G-by-K matrix M with entries in [0, 1]. "Row i gives the win rates" of response i under all K rubrics, and each column gives every response's standing under one rubric.[^c3] The reward is built from this matrix rather than from one scalar per response.

The case for the pairwise step rests on an ablation. The paper keeps its reward mapping fixed and changes only how M is filled: building M from independent absolute scores per rollout and rubric gives an average of 57.86, "5.16 points below the pairwise MatrixReward variant."[^c4] Because the downstream stages are held fixed, the gap is attributed to the observation step. That attribution is my reading of the design, not a separate test the paper runs.

The pairwise protocol costs one judge verdict per pair per rubric. The paper describes an implicit alternative that "asks for all K rubric verdicts in one request per pair and fills the same matrix" with G(G−1)/2 requests instead of K times as many.[^c5] To reduce display-position bias, "either protocol can judge each pair twice, once in each display order."[^c6]

## Limits

- The matrix is relative to its group. A row says how a response fares among its siblings, not on an absolute scale. The same response scored against a different group can have a different row (my inference from the definition).
- Ties count half, so a judge that ties often pushes rows toward one half and narrows the columns. The paper's ablations do not isolate this effect in the parts read (my inference).
- Each entry rests on one judge verdict per pair, or two with the order swapped. Judge noise enters every column directly; the consequence for weights is treated in [[dispersion-redundancy-criterion-weights]].
- The evidence is one policy model and four open-ended benchmarks. The paper's own summary is that the method "leads on AlpacaEval 2, Arena-Hard v2, and" its other benchmarks.[^c7] Its 63.02 average, against a 1.23-point lead over the strongest pairwise baseline, is reported for Qwen3-8B only.[^c8] Other judges, rubric sets and group sizes were not checked here.

## Related

- [[within-group-ordinal-utility-aggregation]] — the closest neighbour: the same pairwise outcomes per criterion, but that work fits a Bradley-Terry utility per criterion, while this keeps the raw win fraction
- [[bradley-terry-preference-model]] — the fit the neighbour uses and this matrix does not
- [[group-relative-advantage]] — the group-normalized advantage that a scalar reward from these rows would feed
- [[dispersion-redundancy-criterion-weights]] — derives one weight per rubric from this matrix's columns
- [[ideal-solution-distance-reward]] — turns each row, once weighted, into a scalar by distance to observed ideal profiles

[^c1]: doi-10-48550-arxiv-2610-00389 — "We compare every pair of the G responses once under each rubric."
[^c2]: doi-10-48550-arxiv-2610-00389 — "counting a tie as half a win, and divide by"
[^c3]: doi-10-48550-arxiv-2610-00389 — "Row i gives the win rates"
[^c4]: doi-10-48550-arxiv-2610-00389 — "Its 57.86 average is 5.16 points below the pairwise MatrixReward variant,"
[^c5]: doi-10-48550-arxiv-2610-00389 — "asks for all K rubric verdicts in one request per pair"
[^c6]: doi-10-48550-arxiv-2610-00389 — "To mitigate display-position bias, either protocol can judge each pair twice,"
[^c7]: doi-10-48550-arxiv-2610-00389 — "It leads on AlpacaEval 2, Arena-Hard v2, and"
[^c8]: doi-10-48550-arxiv-2610-00389 — "yields a 63.02 average across four benchmarks"
