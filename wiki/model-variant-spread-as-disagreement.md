---
description: "Spread across model variants, taken as the standard deviation of continuous relatedness scores, tracks human annotator disagreement better than spread over discrete labels."
aliases: ["models as annotators", "virtual annotators", "model-manipulation spread", "ensemble spread as disagreement"]
sources: ["doi-10-48550-arxiv-2411-12147"]
---
# Model-variant spread as a disagreement proxy

Human annotators who disagree about a word pair leave a trace in the data: their judgments spread out. A system without annotators can try to reproduce that spread by treating its own variants as annotators. The CoMeDi shared-task system paper does this directly: "we treat each model or its manipulation as an annotator and use three measures to reflect uncertainty."[^c1] Each variant (a different pretrained encoder, a different layer, or the same model under a different [[embedding-anisotropy-removal|anisotropy correction]]) yields a relatedness score for a word pair in context. The spread of those scores across variants is the disagreement estimate.

Three measures are compared: the standard deviation (STD) of continuous relatedness scores, the mean pairwise absolute difference (MPD) of discrete labels, and the variation ratio (VR), the share of labels not equal to the mode. The continuous measure wins in most cases: "In most cases, STD on a continuous similarity score outperforms the others."[^c3] The authors' reason is that a discrete label is "a discretization of the continuous counterpart, leading to a loss of precision."[^c4] The abstract puts the central finding the same way: spread "on continuous relatedness scores among different model manipulations correlates with human disagreement annotations compared to metrics on aggregated discrete labels."[^c2]

The second part of the mechanism is which variants enter the pool. Homogeneous pools, one model under many layer and correction settings, beat mixed pools, and pools that combine different models do worst. "Homogeneous model manipulations (homo) outperform mixed ensembles, while combining different models yields the worst performance."[^c5] The authors read this as showing that "model variance can still serve as an effective alternative,"[^c6] tying it to dropout-based uncertainty estimation (Gal, 2016). That tie is cited, not tested in the paper.

What survives the transfer from annotators to models is a design rule: measure the spread on the graded quantity before it is cut into bins. What does not obviously survive is the premise that variants are independent annotators. A homogeneous pool is one model's layers and corrections, so its members are strongly correlated; my inference is that the spread then measures how much the pool's settings disagree, which may be a narrower thing than how much people disagree. [[effective-independent-votes]] measures the same kind of correlation for an LLM-judge panel, where a 16-vote panel comes out near two effective votes.

## Limits

- One shared task. CoMeDi covers lexical relatedness in seven languages from one annotation campaign. Whether the correlation holds for other kinds of disagreement is not tested here.
- The ablation ranks the three measures over 500 random runs of a mixed pool. The text read gives no coefficient of spread against the human disagreement labels themselves, so the correlation claim rests on the abstract and the ranking (my reading).
- For Subtask 2 the authors use the median of all annotations as a separate label, and they flag the cost: "This approach may introduce inconsistencies with our formulation of models as annotators."[^c7]
- The margins among pool strategies are narrow. The top five groups in the paper's Table 3 are close to one another,[^c8] so the choice of strategy is a small difference.
- Pool members were chosen on the development set,[^c9] so the reported pool is itself selected on data that resembles the test.
- The pool's measures do not separate data noise from model variance. The paper's own framing treats disagreement as label noise: "Annotator disagreement can be viewed as label noise, contributing to data uncertainty."[^c10] The spread it measures mixes that data part with model variance (see [[uncertainty-decomposition]]; my inference).

## Related

- [[annotator-disagreement-calibration]] — the reverse use: annotator spread trains a detector's confidence; here a model's spread stands in for annotator spread.
- [[annotator-distribution-target]] — the soft-label target that uses the human label distribution directly; a model-spread proxy is what one reaches for when no such distribution exists at test time.
- [[effective-independent-votes]] — how many votes of a judge panel are independent; the pool's spread is only informative to the extent its members are not redundant, which this note does not measure.
- [[uncertainty-decomposition]] — the aleatoric and epistemic cut that the pool spread does not separate.
- [[embedding-anisotropy-removal]] — the corrections that make up part of each pool; the choice of correction moves the spread.

[^c1]: doi-10-48550-arxiv-2411-12147 — "we treat each model or its manipulation as an annotator and use three measures to reflect uncertainty"
[^c2]: doi-10-48550-arxiv-2411-12147 — "on continuous relatedness scores among different model manipulations correlates with human disagreement annotations compared to"
[^c3]: doi-10-48550-arxiv-2411-12147 — "In most cases, STD on a continuous similarity score outperforms the others"
[^c4]: doi-10-48550-arxiv-2411-12147 — "as a discretization of the continuous counterpart, leading to a loss of precision"
[^c5]: doi-10-48550-arxiv-2411-12147 — "Homogeneous model manipulations (homo) outperform mixed ensembles, while combining different models yields the worst performance."
[^c6]: doi-10-48550-arxiv-2411-12147 — "model variance can still serve as an effective alternative"
[^c7]: doi-10-48550-arxiv-2411-12147 — "This approach may introduce inconsistencies with our formulation of models as annotators."
[^c8]: doi-10-48550-arxiv-2411-12147 — "Table 3: Top five groups for strategies of model selections"
[^c9]: doi-10-48550-arxiv-2411-12147 — "we selected models based on the development set"
[^c10]: doi-10-48550-arxiv-2411-12147 — "Annotator disagreement can be viewed as label noise, contributing to data uncertainty"
