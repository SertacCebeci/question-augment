---
description: "RL-trained reasoners attempt far more questions than their instruct bases, so headline accuracy and ECE gains partly reflect fewer abstentions, not better answers on the newly attempted items."
aliases: ["attempt inflation", "abstention-shift confound"]
sources: ["doi-10-48550-arxiv-2509-21882"]
---
# Attempt inflation

When a model is post-trained with verifiable-reward RL, the set of items it answers grows. A comparison of the post-trained model with its base on a metric computed over attempted items then mixes two things: whether answers got better, and whether the model simply stopped declining.

## Mechanism

The position paper calls this the dominant effect in its factual-QA control: "The dominant effect is attempt inflation: stronger RLVR policies attempt far more questions."[^c1] In its Table 1, the count of unattempted items falls from 480 for DeepSeek-V3 to 81 for DeepSeek-R1, while shared-item accuracy rises from 27.5% to 34.6% and shared ECE falls from 0.496 to 0.317.[^c2] The authors read this as largely an attempting effect: "accuracy on the newly attempted tail is modest, so reported gains depend on how one aggregates across attempted and unattempted items".[^c3]

A matched-SFT control shows the same direction at smaller scale. At 14B, unattempted items drop from 1136 (instruct) to 102 (reasoning SFT) and 103 (RL), while shared accuracy moves only 12.5 to 10.5 and 10.0.[^c4] The paper reports that at 14B/32B, reasoning SFT "sharply reduces abstentions but leaves shared accuracy flat and worsens calibration".[^c5]

The consequence for asking and answering: a drop in refusals is not evidence of knowledge. A model that answers an extra tail of questions at low accuracy looks more useful on coverage and can look better calibrated on the shared subset, while confident errors on the tail are what a user receives. The paper's own gloss is that overconfident hallucinations "inflate apparent utility".[^c6] It is the evaluation-side face of [[rlvr-answering-bias]], which measures the same abstention collapse inside one training run.

## Reporting implication (the paper's, not a measurement)

The authors recommend tracking not-attempted counts, shared-item accuracy and ECE together, and abstention alongside accuracy, rather than a single aggregate.[^c7] My reading: any metric that conditions on attempted items needs the attempt rate beside it, otherwise [[abstention]] and [[calibrated-accuracy]] cannot be separated.

## Limits

- The evidence is one factual-QA control with three model families; the 14B/32B rows compare different models (not one model before and after), and totals of evaluation items differ across families (the paper says so).
- Confidence is logit-derived from the extracted final answer, so ECE depends on that extraction.
- The hypothesised cause (sparse verifiable reward plus entropy pressure encouraging determinacy) is cited from other work, not tested here.
- DeepSeek-V3 to R1 differs in more than RL (data, recipe); attributing the change to RL alone is the paper's reading, not isolated.

## Related

- [[rlvr-answering-bias]] — the within-training measurement of the same abstention collapse
- [[abstention]] — the behaviour that attempt inflation erodes
- [[calibrated-accuracy]] — accuracy metrics that must account for what was declined
- [[calibration]] — ECE on shared items is the paper's calibration measure
- budget-matched-comparison — the sibling confound on the sampling side

[^c1]: doi-10-48550-arxiv-2509-21882 — "The dominant effect is attempt"
[^c2]: doi-10-48550-arxiv-2509-21882 — "DeepSeek-V3 (Instruct)"
[^c3]: doi-10-48550-arxiv-2509-21882 — "accuracy on the newly attempted tail is modest,"
[^c4]: doi-10-48550-arxiv-2509-21882 — "R1-Distill-Qwen-14B (SFT)"
[^c5]: doi-10-48550-arxiv-2509-21882 — "reasoning SFT sharply reduces abstentions but leaves"
[^c6]: doi-10-48550-arxiv-2509-21882 — "overconfident hallucinations inflate"
[^c7]: doi-10-48550-arxiv-2509-21882 — "refusal/abstention alongside accuracy"
