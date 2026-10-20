---
description: "Reliability of an attention-located region can be scored by how consistently its attention holds across answer tokens; a word label beat a number, by small margins."
aliases: ["attention consistency score", "hint reliability score", "token-to-token attention agreement", "consistency-based reliability"]
sources: ["arxiv-2511-17106"]
---
# Attention-consistency reliability

Attention can say where a model looked without saying how firmly. A region that receives the highest average attention may still be a poor guide, because the attention that picked it can be unstable from one output token to the next. The ChainV paper states the problem directly: "A high similarity sum does not ensure stable attention across individual answer tokens."[^a1] Its answer is a second score for each candidate region, computed from the same attention maps, which asks whether the answer tokens agree on which pixels matter. "we employ the consistency of visual attention across different answer tokens within the visual hint region as an indicator of that region reliability."[^a2]

The computation has three steps. For each answer token, the attention over the pixels of a candidate region is normalised. The normalised distributions for pairs of answer tokens are compared with the Pearson correlation, which the paper describes as "the widely-used Pearson correlation."[^a3] A region's consistency score is the sum of these pairwise correlations over pairs of tokens, with the pair index running over i < j.[^a4] The three candidate atomic hints for a step are then ranked and given labels of high, medium or low.[^a5] The hint that is finally inserted is still the one with the highest average attention, and the label is attached to it. So the two quantities, how much attention a region gets and how stable that attention is, are separate, and the method uses both.

The mechanism the paper proposes is a stability test on evidence. A region counts as reliable when the answer tokens that depend on it agree about its pixels. The paper's use of the label is to tell the reasoning model how much to rely on the hint. "If the hint is highly reliable, little additional reflection is needed; otherwise, more reasoning is required."[^a6] That is the design intent. Its measured effect is small. In the ablation, adding reliability scoring gave about 0.2 to 0.3 points on the two benchmarks used, at a cost of about 0.1 s, and the paper credits the cheap cost to "the low computational cost of our Pearson correlation."[^a7]

Words beat numbers, on the paper's own comparison. The authors gave the reliability to the model either as a continuous number or as a word such as high or medium, and report that "using qualitative descriptions consistently yields better reasoning accuracy."[^a8] On MathVista the word form moved accuracy "from 83.0 to" 83.3, with reduced inference time, and the paper says "Similar trends are observed on the OlympiadBench."[^a9]

## Limits

- The effect size is small. The reliability gain is 0.2 to 0.3 points in an ablation on two benchmarks, from a single model in the sections I read. Differences of this size are not tested for significance in the text I read, and I did not find a variance for the ablation rows.
- The score is a property of attention, not of correctness. The text read does not show that low consistency predicts a wrong answer, or that high consistency predicts a right one. The score is a stability measure; whether stability tracks the model actually using the region is assumed. My inference.
- Pearson correlation measures agreement in the shape of two distributions, not their size or where their mass lies on the region. The sections read do not compare it with other agreement measures, so the choice is a design decision, not a shown advantage.
- The qualitative advantage is a single comparison on one model. The authors offer a hypothesis for why words beat numbers, but the sections I read do not test it, and I do not repeat it as a finding.
- Attention maps are themselves an approximation of influence. Whatever the consistency score measures, it inherits the limits of the attention it is computed from.

## Related

- [[visual-hint-insertion]] — the hint this score labels; the score decides how much reflection the model is asked to spend after it
- [[counterfactual-image-grounding-audit]] — blank and shuffled image probes that test whether visual reliance is real, a behavioural check that an attention-stability score does not provide
- [[text-visual-attention-entropy-ratio]] — another attention statistic over a trace, which splits attention between text and vision rather than measuring its stability across tokens

[^a1]: arxiv-2511-17106 — "A high similarity sum does not ensure stable attention across individual answer tokens."
[^a2]: arxiv-2511-17106 — "we employ the consistency of visual attention across different answer tokens within the visual hint"
[^a3]: arxiv-2511-17106 — "We then adopt the widely-used Pearson correlation"
[^a4]: arxiv-2511-17106 — "the consistency score is defined as"
[^a5]: arxiv-2511-17106 — "we rank them and assign them labels of high, medium, or low"
[^a6]: arxiv-2511-17106 — "If the hint is highly reliable, little additional reflection is needed"
[^a7]: arxiv-2511-17106 — "thanks to the low computational cost of our Pearson correlation"
[^a8]: arxiv-2511-17106 — "using qualitative descriptions consistently yields better reasoning accuracy"
[^a9]: arxiv-2511-17106 — "the qualitative form improves accuracy from 83.0 to"
