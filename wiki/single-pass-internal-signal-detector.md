---
description: "A supervised detector reads a frozen VLM's token entropy, log-likelihood, hidden states and visual features in one forward pass, so detection needs no sampling or external verifier."
aliases: ["single-pass hallucination detector", "internal-signal fusion detector", "model-internal hallucination detection", "FaithSCAN-style detector"]
sources: ["arxiv-2601-00269", "arxiv-2512-24562", "doi-10-48550-arxiv-2603-05471"]
---
# Single-pass internal-signal detector

A hallucination detector can be a small supervised classifier that reads the answering model's own internal states, all taken from one forward pass of the frozen model. The paper treats faithfulness hallucination in VQA as binary classification of an (image, question, answer) triple, and frames the detector as learning "uncertainty are extracted from a single forward pass of a VLM".[^c1] The point of the design is that no answer is resampled and no external verifier is called at inference.

The mechanism has three sources of signal. The first is token-level, taken at each decoding step: the log-likelihood of the generated token, the entropy of the predictive distribution, and a hidden embedding of the generated token from one decoder layer.[^c2] The second is the visual patch embeddings from the vision backbone, taken before any language conditioning. The third is the aligned visual tokens that the language model actually attends to during decoding.[^c3] Each source is a variable-length sequence, so each gets its own branch encoder that compresses it to a fixed 64-dimensional vector. The branch vectors are combined by attention over branches, passed through a tanh-gated residual, and a sigmoid gives a hallucination probability. Training uses binary cross-entropy while the VLM stays frozen.[^c4]

The branch encoders are deliberately weak. They are "lightweight sequence compression modules rather than deep semantic encoders", with the stated aim of "representational capacity to reduce overfitting".[^c5] So the detector's skill is supposed to come from which signals it is fed, not from its own depth.

What the ablations show, as reported. Visual-only signals "alone generally yield limited discriminative power across" datasets, while "token-level uncertainty consistently provides a strong baseline".[^c6] Within the token-level group the hidden embeddings are the strongest input, then entropy, and "entropy, while log-likelihood contributes marginally" gives the weakest member.[^c7] "Combining these signals consistently improves performance across" datasets and models, and "attention-based fusion" beat simple concatenation.[^c7] The abstract says "FaithSCAN significantly outperforms existing methods" on the four VQA datasets it used.[^c8]

Why supervision rather than a score with a threshold. The authors argue that uncertainty methods which estimate or calibrate a score still need a threshold to turn it into a decision, and that this "limits practical utility".[^c9] A supervised head maps signals straight to labels, so the learning problem is "extracting useful internal signals rather than output-space confidence modeling".[^c10] This is the authors' argument. The excerpt I read does not include a run where a calibrated threshold on the same signals is compared against the trained head, so the claim is not tested in the text I checked.

Read against a neighbouring note. A single token-probability scalar is a weak detector on its own: [[sequence-likelihood-confidence]] reports AUROC 0.65 to 0.81 for a domain-adapted model's answer likelihood. The log-likelihood's marginal contribution here fits that picture. My inference, not the paper's: the gain comes from the hidden embedding and from combining sources, not from any one scalar.

The text-QA sibling. HaluNet applies the same single-pass idea to question answering, and its own text is the source the VQA note cited only secondhand. It keeps the signals as separate views before fusion: log-likelihood and entropy are averaged over the generated sequence and passed through a small MLP, while the hidden-state trajectory goes through a shallow convolutional branch and attention fusion.[^c14][^c15][^c16] On a 300-example human evaluation, it reports that "HaluNet achieves the strongest human-aligned ranking, with 0.874 AUROC, 0.869 AUPRC" against baselines rerun under the same protocol.[^c17][^c23] Its ablation agrees with the VQA ordering on one point: "likelihood and entropy alone provide useful but limited evidence, while embedding-based variants are consistently stronger."[^c18] My inference, not the paper's: two papers on different tasks point the same way on the hidden-state branch, and neither tests the other's setting.

## Limits

- The detector is model-specific by design: "Notably, the detector is model-dependent", and its inputs are "determined by the architecture of the underlying VLM".[^c11] A head trained on one backbone's signals is not a drop-in for another. The paper evaluates three backbones (IB-T5-XL, LLaVA-8B, Qwen3-VL-8B), so the transfer question is not settled across architectures in general.[^c13]
- It needs white-box access: logits, decoder hidden states and vision-backbone features. An answerer that exposes only text is outside the method. This is inference from the design, not a stated limit of the paper.
- Its labels are not human labels. They come from a judge model at dataset construction (see [[visual-nli-hallucination-labels]]), so the detector learns to reproduce that judge's judgments on the target model's answers.
- The efficiency claim is relative to sampling-based and external-verifier methods. I read no latency numbers in the excerpt, so "efficient" is the authors' word, not a measured figure I can quote.
- The method targets faithfulness hallucination on VQA. Its text-QA cousin HaluNet is described as studying "detection in text-based question answering using internal uncertainty signals",[^c12] and the transfer between the two settings is the paper's own framing, not a test.
- The text-QA version's labels come from the answering backbone itself, not a separate judge: "The original LLM-as-a-Judge labels are produced by the answer-generating backbone via three repeated judge rounds and majority voting."[^c19] The detector therefore learns that backbone's self-judgments, a sharper form of the label dependence noted above.
- HaluNet is evaluated "mainly on singleturn QA with relatively short answers",[^c20] on "two backbone LLMs".[^c21] Its transfer is uneven: "source–target match still affects transfer."[^c22]

- The strength of token-level uncertainty depends on the task. Where the claim is an atomic fact from any source, not a VQA answer or a QA response, a study of retrieval-free verification finds that "logit-based approaches often underperform compared to those that leverage internal model representations."[^c24] The baseline-strength reading above does not carry over unchanged; the two results differ in setting, and neither tests the other.

## Related

- [[retrieval-free-fact-checking]] — the claim-verification setting in which output-probability signals were the weaker family, against probes on internal states

- [[semantic-entropy]] — the sampling-based uncertainty this design is set against; it needs many generations per answer
- [[entropy]] — the predictive-entropy formula used as one of the token-level signals
- [[sequence-likelihood-confidence]] — a single likelihood scalar, weak alone, consistent with the marginal log-likelihood contribution here
- [[internal-prober]] — a supervised readout of internal state, for a different target
- [[pre-generation-success-probe]] — a probe on activations before the answer is written, where this detector reads them during and after generation
- [[visual-nli-hallucination-labels]] — the judge-based labels this detector is trained on
- [[top-risk-error-lift]] — the Lift@20 metric HaluNet reports beside AUROC for its human-labelled ranking

[^c1]: arxiv-2601-00269 — "uncertainty are extracted from a single forward pass of a VLM"
[^c2]: arxiv-2601-00269 — "the entropy of the predictive distribution"
[^c3]: arxiv-2601-00269 — "The aligned visual tokens directly participate in the autoregressive decoding of"
[^c4]: arxiv-2601-00269 — "frozen, using a binary cross-entropy loss over the hallucination"
[^c5]: arxiv-2601-00269 — "lightweight sequence compression modules rather than deep semantic encoders"
[^c6]: arxiv-2601-00269 — "token-level uncertainty consistently provides a strong baseline"
[^c7]: arxiv-2601-00269 — "entropy, while log-likelihood contributes marginally"
[^c8]: arxiv-2601-00269 — "FaithSCAN significantly outperforms existing methods"
[^c9]: arxiv-2601-00269 — "carefully chosen thresholds, limiting practical utility"
[^c10]: arxiv-2601-00269 — "learning focuses on extracting useful internal signals rather than output-space confidence modeling"
[^c11]: arxiv-2601-00269 — "Notably, the detector is model-dependent"
[^c12]: arxiv-2601-00269 — "detection in text-based question answering using internal uncertainty signals"
[^c13]: arxiv-2601-00269 — "We evaluate FaithSCAN on three vision–language backbones"
[^c14]: arxiv-2512-24562 — "HaluNet jointly models token likelihood, predictive entropy, and hidden-state information"
[^c15]: arxiv-2512-24562 — "For scalar probabilistic signals, log likelihood and entropy are first averaged over the generated sequence and then projected with a small MLP"
[^c16]: arxiv-2512-24562 — "The branch encoder is intentionally shallow"
[^c17]: arxiv-2512-24562 — "HaluNet achieves the strongest human-aligned ranking, with 0.874 AUROC, 0.869 AUPRC"
[^c18]: arxiv-2512-24562 — "likelihood and entropy alone provide useful but limited evidence, while embedding-based variants are consistently stronger"
[^c19]: arxiv-2512-24562 — "The original LLM-as-a-Judge labels are produced by the answer-generating backbone via three repeated judge rounds and majority voting."
[^c20]: arxiv-2512-24562 — "HaluNet is evaluated mainly on singleturn QA with relatively short answers."
[^c21]: arxiv-2512-24562 — "Our experiments cover three QA benchmarks, two backbone LLMs"
[^c22]: arxiv-2512-24562 — "source–target match still affects transfer"
[^c23]: arxiv-2512-24562 — "On a 300-example human evaluation, HaluNet achieves 0.874 AUROC and 0.869 AUPRC"
[^c24]: doi-10-48550-arxiv-2603-05471 — "logit-based approaches often underperform compared to those that leverage internal model representations."
