---
description: "A DPO pair is kept only if the judge-score gap between its chosen and rejected answers clears a threshold θ; raising θ from 0.3 to 0.7 cut pairs from 983 to 341 with marginal score differences."
aliases: ["minimum score-gap threshold", "θ-thresholded preference pairs", "margin-filtered preference pairs", "score-gap pair filter"]
sources: ["arxiv-2512-13059"]
---
# Score-gap threshold on preference pairs

A preference pair for DPO needs a chosen answer and a rejected one. When a judge produces the ranking by scoring each answer on a scale, two answers can receive nearly equal scores. A pair whose sides differ only by the judge's noise teaches little about which answer is better. One remedy is to drop such pairs before training.

The MMU-RAG deep-research system in arxiv-2512-13059 builds its pairs this way. Answers to each training question are scored by an LLM judge, and the scores are summed across aspects after normalization: on Researchy Questions all three aspects (clarity, insightfulness, factuality) are scored, and on the other sets only clarity and insightfulness.[^c1][^c2] The highest-scored answer becomes the chosen response and the lowest-scored one the rejected response.[^c3] Then the authors "retain only preference pairs with a meaningful score gap" by setting a minimum threshold θ on the difference and keeping only pairs that clear it.[^c4]

The mechanism is a precision knob on the pairs. A higher θ keeps only pairs where the judge separates the two answers clearly, and it removes data in the process. The threshold also interacts with a tie-break. When two answers share a score, the authors "select the answer with more search queries as the chosen" one.[^c5] Pairs with formatting errors, such as incorrect citation of the source, are dropped first.[^c6]

The data cost is concrete. For θ ∈ {0.3, 0.5, 0.7} the paper reports "yielding datasets with 983, 828, and 341 pairs", trained for one epoch each, "resulting in 56, 47, and 20 training steps".[^c7][^c8]

The effect on outcomes is the weak part of the evidence. All tuned models beat the untuned VANILLA model on the judged metrics, and the authors describe the tuned models as differing "with only marginal differences among them".[^c9] They submitted the θ = 0.3 model, which keeps the most data.[^c10] So the comparison that the text reports is between tuned models and the untuned baseline, and between thresholds that barely separate in outcome.

## Limits

- No run without the filter is reported in the text I read. Every comparison is between thresholds 0.3 to 0.7 and the untuned model, so the filter's own contribution is not isolated from the DPO step.
- Pair count and training length move together. With one epoch, a higher θ also means fewer optimizer steps (56, 47, 20). The threshold is therefore confounded with how much the model trains. This is my inference from the numbers; the authors do not discuss it.
- The gap is taken on a sum of normalized scores, but the normalization is not described in the text I read. The factuality term is absent for two of the three training sources, because "clarity and insightfulness for Natural Questions and the validation set" are the only aspects scored there.[^c11] A gap of the same size therefore means different things across sources.
- One judge (o3-mini), one sampling run per question, and no seeds or variance for the tuned models. The text reports no agreement between the judge's gaps and human rankings, so whether a large gap marks a real quality difference is not tested.
- The tie-break rewards more searches. The tuned model "also performs more searches on average",[^c12] and the search count rose from 1.03 to 1.20 in Table 1. Whether the tie-break produces that rise, or the rise reflects something else, is not separated. This is my reading.
- A gap threshold works as a noise filter only if the judge's scores are informative near the margin. The text does not test that.

## Related

- [[execution-verified-preference-pairs]] — pairs labelled by an executable check need no gap threshold; a judge's pairs need one, because the judge's gap is what decides whether a pair enters training.
- [[within-group-ordinal-utility-aggregation]] — also discards a raw score gap, through a tie margin in advantage aggregation; here the gap decides whether a whole pair is trained on.
- [[weighted-nugget-recall]] — another judge-scored, partial-credit measure of answer content, and the family the factuality term here belongs to.

[^c1]: arxiv-2512-13059 — "we evaluate all three metrics on Researchy Questions"
[^c2]: arxiv-2512-13059 — "to assign preference scores to the"
[^c3]: arxiv-2512-13059 — "is selected as the chosen response, and the one with the lowest score as the rejected response."
[^c4]: arxiv-2512-13059 — "to retain only preference pairs with a meaningful score gap"
[^c5]: arxiv-2512-13059 — "we select the answer with more search queries as the chosen"
[^c6]: arxiv-2512-13059 — "We then filter out answers containing formatting errors, such as incorrect citation of the source."
[^c7]: arxiv-2512-13059 — "yielding datasets with 983, 828, and 341 pairs"
[^c8]: arxiv-2512-13059 — "resulting in 56, 47, and 20 training steps"
[^c9]: arxiv-2512-13059 — "with only marginal differences among them"
[^c10]: arxiv-2512-13059 — "We selected the model tuned with θ = 0.3 for competition submission."
[^c11]: arxiv-2512-13059 — "clarity and insightfulness for Natural Questions and the validation set"
[^c12]: arxiv-2512-13059 — "The tuned model also performs more searches on average"
