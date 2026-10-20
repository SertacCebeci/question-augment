---
description: "A linear probe on a model's pre-generation activations predicts its own success; that signal is model-relative, diverges from human difficulty, and weakens as reasoning budget grows."
aliases: ["pre-generation activation probe", "model-relative difficulty", "success prediction from activations", "non-factuality prediction (NFP)", "ante-hoc non-factuality prediction"]
sources: ["arxiv-2602-09924", "doi-10-48550-arxiv-2406-05328", "arxiv-2601-01011", "doi-10-48550-arxiv-2506-09669", "arxiv-2511-22749"]
---
# Pre-generation success probe

Whether a model will answer a question correctly can be read from its hidden state before it writes a token. The authors train linear probes on residual-stream activations at the end of the prompt (the chat-template suffix position is among the swept positions) to predict policy-specific success on math and code tasks.[^c1] Targets differ: expected success rate over K rollouts (regression), and binary success under greedy, Maj@K or Pass@K decoding (logistic regression).[^c2] These are distinct targets, because they are "different transformations of the full answer distribution".[^c3]

## Model difficulty is not human difficulty

On E2H-AMC, which has human IRT difficulty and model accuracy for the same problems, probes recover both signals: Spearman 0.83-0.87 for human difficulty and 0.40-0.64 for model difficulty.[^c4] Yet the probe's model-difficulty prediction beats human IRT labels at predicting Maj@5 failure in every reasoning mode, so the model encodes "a model-relative notion of difficulty that is distinct from, and more predictive of their own performance than, human difficulty."[^c5]

## Extended reasoning decouples the two

For GPT-OSS-20B, raising reasoning level from low to high lowers linear-probe AUROC from 0.78 to 0.64 under fixed Maj@5, while accuracy rises.[^c6] Correlation of probe-predicted difficulty with human IRT drops from about 0.65 to 0.45.[^c7] Chain-of-thought length tracks human difficulty and falls with empirical success, so the model spends tokens on problems humans find hard even when well within its competence.[^c8] A non-linear MLP probe partly recovers the loss (0.76 vs 0.64 at high reasoning), so the signal is "less linearly separable" rather than gone.[^c9]

## Use: routing

The probe's estimate can route queries across a pool of models. The authors report matching the best single model at up to 70% lower cost on MATH, and say routing is limited by estimate reliability, not routing policy.[^c10] My reading: for asking and answering, the questioner's own difficulty estimate depends on who is answering; human-labeled difficulty is a weak proxy for an answerer's chance of failing.

## Short fact-seeking questions

The readout has also been applied to fact-seeking questions with short answers. FacLens takes the hidden state of the last input token at one layer as the question's representation, encodes it with a small MLP, and classifies it with a linear layer.[^c11] Its label marks a response non-factual when no substring matches a gold answer.[^c15] Across four LLMs and three QA sets, the authors report it "outperforms baselines in terms of AUC metric and runtime."[^c12] Against post-hoc detectors that read the generated response, which have more information, it shows "comparable and even better performance."[^c13] My inference: this is the same claim as the math and code results, a readout before generation, now scored against a string-match label. The AUC therefore measures agreement with that label, not correctness in a stronger sense.

## Recoverability can outrun the commitment

Vera's intention-collapse study runs the same readout on the state just before the first token, which it calls recoverability, Recov(I; Z): a logistic probe on the hidden states predicting eventual correctness, scored by AUROC on item-level splits.[^c16] For three 7–8B instruct models on GSM8K, ARC-Challenge and AQUA-RAT, with n = 200 items per cell, the probe is above chance only in a subset of cells. The dissociation shows up on ARC-Challenge, where Qwen's probe AUROC is high "while CoT accuracy drops substantially in the same setting."[^c17] The author reads this as a signal that is present in the state but not turned into a valid final choice under a multiple-choice format.[^c18] My inference: a probe score is a measure of separability, not of competence. The paper says as much, since "Recoverability measures separability in representations; it does not guarantee that" the collapse policy will express the signal.[^c19] Shuffled-label probes stay near chance, which the paper takes as evidence that the pipeline is not inventing the separation, not that the signal is causal.[^c20]

## Limits

Probes are supervised and need labeled pass/fail data per model and policy; they need white-box access, so they do not apply to API-only answerers. Tasks are math and code with checkable answers; open-ended questions are untested. Probe AUROC is moderate (above 0.7 for several models, not near 1). Greedy targets are less noisy than Maj@5, so comparisons across decoding targets are confounded by label noise (the authors say "likely"). The causal account of length tracking human difficulty is correlational. Routing gains were measured on benchmarks with a fixed pool of models. The fact-seeking extension is also white-box: the method "assumes access to the parameters of" the LLM.[^c14] A training-free counterpart reads a yes/no self-assessment across layers with no labelled pass/fail data; the paper proposing it calls it "a novel, training-free method called Internal Confidence".[^c21]

## Related

- [[model-dependent-benchmark-difficulty]] — difficulty rankings also shift with the model in a negotiation benchmark.
- [[procedural-hallucination-readout-routing]] — another internal readout used to route.
- [[trajectory-geometry-uncertainty-probe]] — probing activations for uncertainty during generation rather than before.
- [[reasoning-contamination-of-verbalized-confidence]] — reasoning also degrades confidence signals.
- [[cross-model-domain-adaptation-probe]] — the same readout moved to other LLMs by unlabeled domain adaptation on fact-seeking questions.
- [[model-specific-difficulty-dispatch]] — the same per-model difficulty, read from the task text by an external classifier rather than from the model's activations, so it reaches answerers whose internals are closed; the model-specific signal then survives only in the outcome labels.[^c22][^c23]

[^c1]: arxiv-2602-09924 — "We train linear probes on pre-generation activations to predict policy-specific success on math and coding tasks"
[^c2]: arxiv-2602-09924 — "For expected success rate and human IRT difficulty we use the MSE loss and for"
[^c3]: arxiv-2602-09924 — "different transformations of the full answer distribution"
[^c4]: arxiv-2602-09924 — "ρ = 0.83–0.87 for human difficulty, 0.40–0.64 for model difficulty"
[^c5]: arxiv-2602-09924 — "a model-relative notion of difficulty that is distinct from, and more predictive of their own performance than, human difficulty."
[^c6]: arxiv-2602-09924 — "level from low to high decreases AUROC from 0.78 to 0.64 even under fixed Maj@5"
[^c7]: arxiv-2602-09924 — "ρ drops from ∼0.65 to ∼0.45"
[^c8]: arxiv-2602-09924 — "the model spends more tokens on problems"
[^c9]: arxiv-2602-09924 — "the underlying success signal remains"
[^c10]: arxiv-2602-09924 — "Critically, we find that routing effectiveness is limited by the reliability of the underlying"
[^c11]: doi-10-48550-arxiv-2406-05328 — "hidden states corresponding to the last input token"
[^c12]: doi-10-48550-arxiv-2406-05328 — "baselines in terms of AUC metric and runtime."
[^c13]: doi-10-48550-arxiv-2406-05328 — "comparable and even better performance."
[^c14]: doi-10-48550-arxiv-2406-05328 — "This paper assumes access to the parameters of"
[^c15]: doi-10-48550-arxiv-2406-05328 — "mark an LLM’s response as non-factual (i.e., y = 1) if no sub-string"
[^c16]: arxiv-2601-01011 — "Recov(I; Z) ≜ AUROC fϕ (I), Z"
[^c17]: arxiv-2601-01011 — "while CoT accuracy drops substantially in the same setting."
[^c18]: arxiv-2601-01011 — "high AUROC can co-occur with degraded CoT accuracy in multiple-choice regimes"
[^c19]: arxiv-2601-01011 — "Recoverability measures separability in representations; it does not guarantee that"
[^c20]: arxiv-2601-01011 — "remains near chance across cells, supporting pipeline validity"
[^c21]: doi-10-48550-arxiv-2506-09669 — "we propose a novel, training-free method called Internal Confidence"
[^c22]: arxiv-2511-22749 — "where internal hidden states are inaccessible"
[^c23]: arxiv-2511-22749 — "While these cannot capture model-specific architectural biases"
