---
description: "Predicting from question text alone, with a calibrated model, which input fidelity will answer correctly lets a one-step value-of-information rule skip costly retrieval at 50-60% lower cost."
aliases: ["VOILA", "question-conditioned fidelity selection", "value-of-information fidelity selection"]
sources: ["arxiv-2602-03007"]
---
# Pre-retrieval fidelity selection

Before fetching any evidence, the question itself can predict how much evidence quality it needs. VOILA does this for visual question answering. A gradient-boosted regressor scores, from question-only features, how likely each fidelity of the image (caption, thumbnail, full resolution) is to give a correct answer. An isotonic regression then calibrates those scores per fidelity into probabilities.[^c1] The system then picks the fidelity that maximizes expected utility, which is anticipated accuracy gain minus acquisition cost. The paper calls this a one-step [[value-of-information]] rule.[^c2]

## Mechanism

The cost of a fidelity is a weighted sum of bandwidth, retrieval latency and storage-access penalty, normalized so that full resolution costs 120. The rule depends only on relative costs, so rescaling all costs uniformly leaves the routing unchanged as long as higher fidelities stay more expensive.[^c3] The probabilities come "from question features alone, without any VLM execution", so the decision is made before either retrieval or inference.[^c4]

The design rests on an observation about post-retrieval confidence. Escalating to a higher fidelity only when the model is unsure does not work, because incorrect answers from low-fidelity inputs often receive log-probabilities comparable to correct ones. The result is confident but wrong answers that never trigger escalation. The paper concludes that post-retrieval confidence is an unreliable indicator of context sufficiency, which motivates deciding before retrieval.[^c5] Calibration matters because the VLM's own probabilities overlap heavily between correct and incorrect predictions, while the calibrated question-conditioned probabilities separate them.[^c6]

Reported results: across four datasets and six VLMs (7B to 235B), accuracy stays within 2-6 points of always using full resolution, and normalized retrieval cost falls by roughly 50-60%.[^c7] The paper argues that scaling the model does not substitute for missing visual information, so this is a separate axis from model capacity. The routing policy also transfers across datasets, for example trained on VQA-v2 and tested on GQA, which suggests the minimum information needed is largely a property of the query rather than of the dataset.[^c8]

The paper states a near-Bayes-optimal claim: regret is bounded by calibration quality when the probability estimates are calibrated (its Appendix C). I did not read that appendix, so I treat it as the authors' claim.[^c9]

## Limits

- The reported advantage is against fixed-fidelity baselines. The accuracy and cost figures I read are for question-answering over images, with cost a proxy built from bandwidth and latency.
- The predictor uses only question features. If the needed detail depends on the image content (what is actually in the picture), a question-only score cannot see it. Failures of that kind are not characterized in the text I read.
- The retrieval-side finding that logit confidence is misaligned was shown on Pixtral-12B and VQA-v2. I did not verify it for other models.
- The cost weights and the full-resolution value of 120 are the paper's own design choices. Whether the 50-60% saving holds under other price structures was not tested beyond the paper's scaling-invariance argument.
- The decision rule is one-step. It does not model sequential escalation or stopping.

## Related

- [[value-of-information]] — the decision-theoretic rule VOILA instantiates
- [[voi-per-cost-modality-selection]] — a cost-ratio action choice; VOILA uses utility minus cost, not a ratio
- [[question-conditioned-evidence-acquisition]] — acquisition conditioned on the question
- [[expected-utility]] — the quantity maximized

[^c1]: arxiv-2602-03007 — "a gradientboosted regressor estimates correctness likelihood"
[^c2]: arxiv-2602-03007 — "yielding a one-step value-of-information decision rule"
[^c3]: arxiv-2602-03007 — "uniform rescaling of c(f ) does not affect routing behavior as long as higher fidelities remain more expensive"
[^c4]: arxiv-2602-03007 — "computed from question features alone, without any VLM execution"
[^c5]: arxiv-2602-03007 — "Post-retrieval confidence is thus an unreliable indicator of context sufficiency, motivating pre-retrieval decision mechanisms."
[^c6]: arxiv-2602-03007 — "The VLM’s own probabilities exhibit substantial overlap"
[^c7]: arxiv-2602-03007 — "In most cases, VOILA achieves accuracy within 2–6 percentage points of always using fullresolution images, yet reduces normalized retrieval cost by roughly 50–60 %."
[^c8]: arxiv-2602-03007 — "the minimum visual information required to answer a query is primarily determined by query characteristics rather than dataset-specific statistics"
[^c9]: arxiv-2602-03007 — "showing that VOILA implements a near Bayes-optimal"
