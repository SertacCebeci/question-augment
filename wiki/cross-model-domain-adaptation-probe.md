---
description: "A non-factuality probe fit on one LLM's question representations moves to other LLMs by unlabeled domain adaptation, if the label-given-representation mapping is shared."
aliases: ["cross-LLM FacLens", "unsupervised cross-model probe adaptation", "shared non-factuality pattern"]
sources: ["doi-10-48550-arxiv-2406-05328"]
---
# Cross-model domain adaptation of a probe

A probe is normally refit for each model it reads. FacLens, a predictor of non-factual answers to short fact-seeking questions, instead treats the hidden question representations from one LLM as a *data domain*: "a collection of hidden question representations sourced from a certain LLM."[^c1] The move rests on a premise from transfer learning. Source and target domains may have different marginal distributions P(X), but are assumed to share the conditional P(y|X): "probability distributions P (y|X) (i.e., no significant concept shift)."[^c2]

When the premise holds, a probe trained with labels on one model's domain can be moved to another model without new labels. The target model's unlabeled questions are aligned to the source by an MMD loss with a linear kernel, and the authors report that this makes the cross-LLM probe "work much better in the target domain."[^c3] The point of the move is cost: the labels require the source model to answer the questions, and the authors contrast this with each new LLM having "to conduct costly response generation."[^c4][^c5]

## The premise was checked by a mixture

To test the premise, the authors train one probe on a mixture of the M LLMs' domains, with equal weights, and compare it with probes trained on single domains. "Similar performance suggests no significant concept shift across different domains."[^c6] My inference: matching performance is consistent with a shared P(y|X), but it does not show the two conditionals are equal. A shared probe can score well on a test set while the models' conditionals differ in regions that set does not sample.

## Alignment is required, and scale matters

Without adaptation, cross-model transfer does poorly: the unadapted results are described as "unsatisfactory."[^c7] Training also needs a question-aligned minibatch strategy: "Question-aligned strategy is necessary to minibatch training of cross-LLM FacLens."[^c8] Transfer is better between models of similar size: "FacLens shows better transferability between LLMs of similar scales."[^c9]

## What survives from transfer learning

The covariate-shift assumption and the distribution-matching step survive the import. What changes is the meaning of "domain". In classical domain adaptation the domains are different data sets. Here the same questions go to different models, and the shift lies entirely in the coordinates each model produces for them. Alignment therefore corrects a difference in representation geometry, and the premise then says the label function is still shared. That is a claim about model internals; the transfer results are the only evidence in the text for it. My inference.

The motivation is an analogy to human cognition, but the stated reason for expecting shared patterns is structural: LLMs "generally follow the Transformer" architecture and "share overlapping training corpora."[^c10] That is a hypothesis about why the premise might hold, not a test of it.

## Limits

- The models are four instruction-tuned LLMs, one 1.5B and three at 7–8B: "and Qwen2-1.5B-Instruct (Yang et al., 2024a) are used for experiments."[^c11] Transfer across very different scales is named as untested: "LLMs of very different scales."[^c16]
- Labels mark a response non-factual when no substring matches a gold answer.[^c15] The authors checked a sample of negatives by hand and report 97.0% correct labels; "manually checked their labels’ quality."[^c12]
- Decoding is greedy. The authors ran sampling and say the conclusions "still hold true."[^c13]
- The method is white-box: "This paper assumes access to the parameters of" the LLM.[^c14] Black-box models are outside the claim.
- The transfer results I read use only the MMD variant. Other adaptation methods are not compared here.
- Three QA datasets of short factual questions. Open-ended questions are not tested.

## Related

- [[pre-generation-success-probe]] — the same pre-generation readout of a model's own success, applied to math and code; FacLens applies it to fact-seeking QA and adds the cross-model step.
- [[correctness-probe-transfer-needs-joint-training]] — reports that correctness probes transfer poorly across datasets and between models unless trained jointly; the contrast is the setting, a question-level label with unlabeled alignment.

[^c1]: doi-10-48550-arxiv-2406-05328 — "D refers to a collection of hidden question representations sourced from a certain LLM."
[^c2]: doi-10-48550-arxiv-2406-05328 — "probability distributions P (y|X) (i.e., no significant concept shift)"
[^c3]: doi-10-48550-arxiv-2406-05328 — "(MMD loss with linear kernel), the cross-LLM FacLens can work much better in the target domain,"
[^c4]: doi-10-48550-arxiv-2406-05328 — "to rapidly apply FacLens to other LLMs without collecting new labels"
[^c5]: doi-10-48550-arxiv-2406-05328 — "to conduct costly response generation"
[^c6]: doi-10-48550-arxiv-2406-05328 — "Similar performance suggests no significant concept shift across different domains."
[^c7]: doi-10-48550-arxiv-2406-05328 — "Figure 6 are unsatisfactory."
[^c8]: doi-10-48550-arxiv-2406-05328 — "Question-aligned strategy is necessary to minibatch training of cross-LLM FacLens."
[^c9]: doi-10-48550-arxiv-2406-05328 — "transferability between LLMs of similar scales."
[^c10]: doi-10-48550-arxiv-2406-05328 — "share overlapping training corpora (Gao"
[^c11]: doi-10-48550-arxiv-2406-05328 — "and Qwen2-1.5B-Instruct (Yang et al., 2024a) are used for experiments."
[^c12]: doi-10-48550-arxiv-2406-05328 — "manually checked their labels’ quality."
[^c13]: doi-10-48550-arxiv-2406-05328 — "experimental conclusions still hold true."
[^c14]: doi-10-48550-arxiv-2406-05328 — "This paper assumes access to the parameters of"
[^c15]: doi-10-48550-arxiv-2406-05328 — "mark an LLM’s response as non-factual (i.e., y = 1) if no sub-string"
[^c16]: doi-10-48550-arxiv-2406-05328 — "LLMs of very different scales."
