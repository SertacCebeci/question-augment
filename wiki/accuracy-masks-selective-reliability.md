---
description: "On SciFact and PubMedQA, six LLMs have near-equal accuracy but differ in risk at fixed coverage; abstention, not model choice, drives reliability."
aliases: ["abstention dominates model choice", "risk-coverage evaluation of scientific reasoning"]
sources: ["arxiv-2602-14189"]
---
# Accuracy masks selective reliability

Unconditional accuracy forces every system to answer every input, so it cannot see whether a system knows when its evidence is insufficient. Abdaljalil et al. extend the label space to Y ∪ {⊥} and treat the system as a selective classifier (F, g), where g decides whether to answer.[^c1] They score it by selective risk (loss among answered items) against coverage (the fraction answered), plus AURC and Risk@0.8 and Risk@0.9.[^c2]

## What was measured

Six language models (an encoder-decoder, open-weight chat models and proprietary APIs) were run through a pipeline. It splits a claim into minimal conditions, audits each against evidence with an NLI verifier, and then supports, refutes or abstains. Evaluation was on SciFact and PubMedQA.[^c3]

Three patterns are reported:

- Raw accuracy varies only within a narrow band across architectures. Larger or proprietary models do not reliably beat smaller or open ones.[^c4]
- Confidence-based abstention cuts risk sharply at moderate coverage, even where accuracy barely moves.[^c4]
- At matched coverage the models' risk differences narrow. A smaller or instruction-tuned model at reduced coverage can reach lower risk than a larger model forced to answer everything.[^c5]

The instruction-tuned encoder-decoder FLAN-T5 had among the lowest AURC despite accuracy comparable to or lower than the chat models. The authors attribute this to more conservative answering. Larger chat models keep coverage high at the cost of risk, a tradeoff that "is not penalized under standard accuracy metrics but becomes visible under risk–coverage analysis".[^c6] The attribution to conservatism is the authors' interpretation, not an isolated test.

## Abstention as the active ingredient

When abstention was disabled, the system had to answer every query. That gave the highest risk and worst selective metrics, with Risk@0.8 and Risk@0.9 approaching one in several settings.[^c7] The authors conclude that abstention is the primary mechanism controlling error, while decomposition and auditing shape how evidence is evaluated.[^c7]

The appendix gives a monotonicity condition. If the confidence score is rank-calibrated, raising the threshold cannot increase risk among accepted predictions. This explains the monotone risk-coverage curves, and without structured confidence, thresholding is disconnected from risk reduction.[^c8] Estimates of selective risk also become unstable at very low coverage, which is why evaluation focuses on moderate coverage.[^c9]

My reading, not the paper's claim: a ranking of models by accuracy and a ranking by selective risk can disagree. A comparison that fixes only one of the two answers a different question than the one a reader of a scientific claim cares about.

## Limits

- Only two biomedical and scientific benchmarks, with one NLI verifier. The paper notes that NLI errors propagate downstream.
- The paper itself says it provides no distribution-free guarantee. Monotonicity depends on the confidence score being rank-calibrated, which is assumed and not guaranteed for LLM confidence.
- Abstention is evaluated through thresholds on confidence, not through whether a model's stated reasons for abstaining are right.
- "Abstention dominates model choice" is a within-pool finding on six models. It is not a claim that model choice never matters.
- Risk at very low coverage is noisy, so claims hold only at moderate coverage.

## Related

- [[abstention]] — the general concept; this note supplies the evaluation finding on scientific claims
- [[calibration]] — rank calibration of confidence is what makes thresholding reduce risk
- [[evaluation-choices-encode-error-priorities]] — the choice of accuracy over risk-coverage encodes a priority on answering
- [[context-dominates-model-choice]] — another finding that model choice explains little once the key factor is fixed
- [[sage-abstention-evaluation]] — a different abstention evaluation built on the same risk-coverage idea

[^c1]: arxiv-2602-14189 — "the prediction space is extended to Y ∪ {⊥}, where ⊥ denotes abstention."
[^c2]: arxiv-2602-14189 — "and Risk@0.9 denote risk at 0.8 and 0.9 coverage, respectively."
[^c3]: arxiv-2602-14189 — "Experiments are conducted with six diverse language models"
[^c4]: arxiv-2602-14189 — "First, across models and datasets, unconditional accuracy varies within a relatively narrow range."
[^c5]: arxiv-2602-14189 — "Once coverage is controlled, performance differences between models narrow substantially."
[^c6]: arxiv-2602-14189 — "This tradeoff is not penalized under standard accuracy metrics but becomes visible under risk–coverage analysis."
[^c7]: arxiv-2602-14189 — "This confirms that abstention is the primary mechanism by which the system controls error."
[^c8]: arxiv-2602-14189 — "Abstention without structured confidence breaks the connection between thresholding and risk reduction."
[^c9]: arxiv-2602-14189 — "This result formalizes the intuition that selective risk estimates become unstable at very low coverage"
