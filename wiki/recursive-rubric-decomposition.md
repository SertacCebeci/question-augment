---
description: "Splitting any rubric that most sampled responses satisfy into finer criteria, filtering misaligned and redundant ones, and whitening weights makes rubric judges more accurate and rewards stronger."
aliases: ["RRD", "recursive decompose-filter rubric refinement", "whitened uniform rubric weighting"]
sources: ["arxiv-2602-05125"]
---
# Recursive rubric decomposition

A rubric-based judge scores each response as a weighted sum of binary criteria. Rubric quality then decides judge accuracy, and unrefined rubrics can hurt: naively generated rubrics dropped GPT-4o on JudgeBench from 55.6% to 42.9%, below using no rubrics.[^c1]

## Mechanism

Recursive Rubric Decomposition (RRD) starts from an LLM proposal conditioned on the task prompt and 8 sample responses. Its premise is that distinct responses must differ somewhere, so a rubric satisfied by many of them is too coarse. Any rubric matching more than n = 2 responses is recursively decomposed into finer sub-criteria.[^c2]

Each round of new criteria passes two filters. The misalignment filter discards rubrics that prefer a weaker model's output (Llama3-8B) to a stronger one's (GPT-4o), a proxy for a wrong preference direction. The redundancy filter removes rubrics that overlap existing ones.[^c3] The loop stops when accumulated rejected proposals pass a threshold (15 in the experiments). Rubric-set size therefore follows prompt complexity. Counts grew from about 7.4 to a plateau near 20 by iteration 3, with more variance across tasks.[^c4]

## Why correlation-aware weights

The paper bounds the judge's misclassification probability exponentially. The bound improves as (w^T mu)^2 / (w^T Sigma w) grows, where mu are the criteria's edges and Sigma their noise covariance. This gives four moves: decompose, drop negative-edge criteria, prune redundancy, and weight against correlation.[^c5] It assumes each rubric has a positive edge and bounded pairwise correlation.[^c6]

Edges need ground-truth labels, which are unavailable. RRD instead whitens the rubric space with Sigma^(-1/2) and weights equally there. This is label-free because Sigma is a property of the rubric set, and it can be estimated from unlabeled data.[^c7] LLM-assigned weights work only when one dominant rubric exists, and open-ended quality is spread over many criteria.[^c8]

## Measured effects

- RRD with whitened uniform weights (RRD-WU) raised GPT-4o on JudgeBench from 55.6% to 73.3%.[^c9]
- Whitened weighting beat uniform and LLM-assigned weighting. At a termination threshold of 20, plain RRD plateaued or slipped, but RRD-WU stayed high.[^c10]
- Sample responses from two strong frontier models worked best. Swapping one for a smaller model reduced accuracy, because decomposition needs strong samples that reveal when a rubric is too coarse.[^c11]
- As an RFT reward on WildChat, RRD-WU reached roughly 150-160% reward improvement against about 10-20% for baselines.[^c12]

## Limits

- Theory rests on assumptions A1 and A2. Whether LLM-judge rubric verdicts satisfy them was not tested by me in the slices read.
- The misalignment filter uses a weak-versus-strong model pair as the label proxy, not human preference.
- Over-decomposition is a named failure mode, controlled only by a rejection threshold.
- Gains were shown on JudgeBench, PPE, and WildChat-trained small policies. I did not read how far they extend to other judges or domains.
- Reward gains are relative to the policy's own rubric reward, not an independent measure.

## Related

- [[llm-judge-biases]] — the brittleness of holistic judges that rubrics try to fix
- [[rubric-complexity-normalized-reward]] — another way to turn rubric judgments into a reward
- [[pretraining-grounded-rubric-self-play]] — rubrics as training signal from a different source
- [[rubric-formation-gap]] — the difficulty of forming good rubrics

[^c1]: arxiv-2602-05125 — "we show that naively generated rubrics degrade GPT-4o’s judgment accuracy from 55.6% to 42.9% (Figure 1)"
[^c2]: arxiv-2602-05125 — "a rubric satisfied by many responses is too broad-brush and insufficiently discriminative."
[^c3]: arxiv-2602-05125 — "which discards rubrics that prefer outputs from a weaker model (Llama3-8B) over a stronger model (GPT-4o) as a proxy for incorrect preference direction"
[^c4]: arxiv-2602-05125 — "the initial average of 7.4 rubrics grows rapidly and plateaus at approximately 20 by iteration"
[^c5]: arxiv-2602-05125 — "Weight Optimization: Prevent over-representation of highly correlated rubrics via weight optimization."
[^c6]: arxiv-2602-05125 — "(A2) assumes that individual rubric’s noise is bounded and rubrics are not repetitive"
[^c7]: arxiv-2602-05125 — "This yields a simple, label-free, and correlation-aware weighting scheme"
[^c8]: arxiv-2602-05125 — "This strategy is effective only"
[^c9]: arxiv-2602-05125 — "On JudgeBench, RRDWU improves GPT-4o’s accuracy from 55.6% to 73.3% (+17.7 points)."
[^c10]: arxiv-2602-05125 — "In contrast, RRDWU is notably robust: accuracy remains high even"
[^c11]: arxiv-2602-05125 — "tends to reduce performance"
[^c12]: arxiv-2602-05125 — "RRDWU reaches roughly 150–160% reward improvement by the end of training"
