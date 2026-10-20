---
description: "Maximum-likelihood SFT keeps output-probability confidence calibrated, while RL and DPO sharpen it; a post-RL SFT pass on self-distilled labels restores confidence-correctness alignment."
aliases: ["post-RL SFT", "MLE-versus-reward calibration", "self-distillation calibration repair"]
sources: ["arxiv-2603-06604"]
---
# Post-RL SFT calibration restoration

A model's confidence is only as trustworthy as the objective that last shaped its output probabilities. Xie, Liu & Yao (2026) read confidence off anchor-token probabilities: the class label for structured tasks, or the Yes/No answer to a self-evaluation prompt for open-ended generation. They then ask how the training paradigm changes that signal.

## Mechanism

Supervised fine-tuning minimizes cross-entropy, which equals minimizing the KL divergence from the data distribution to the model, so it performs maximum-likelihood estimation. The paper argues this "naturally promotes calibration": output probabilities track empirical frequencies in training data.[^c1]

Trust-region RL (PPO, GRPO) optimizes a different object. The advantage weighting "concentrate[s] probability mass on high-reward actions", so slight positive advantages compound toward near-certainty.[^c2] The probabilities then reflect reward optimization rather than data frequencies.[^c3] DPO is also likelihood-based, but over preference probabilities, not output probabilities; it cares only about the ratio to a reference model, which pushes absolute probabilities of preferred outputs upward.[^c4] This is the authors' theoretical argument, not a formal proof of a bound.

## Measurements

On Qwen3-4B-Instruct over seven tasks plus self-evaluation variants:

- SFT reached average AUROC 0.879 and ECE 0.034.[^c5]
- GRPO left AUROC essentially flat (0.809 vs 0.806 baseline) and lowered ECE only to 0.135 from 0.163. The paper attributes the ECE drop to higher accuracy, which "mechanically reduced the confidence-accuracy gap without addressing the underlying calibration issue".[^c6]
- DPO's AUROC fell to 0.785.[^c7]

So lower ECE alone can be an accuracy artifact; AUROC, the ability to rank correct above incorrect, is what shows whether the discrimination improved. Qwen3 already ends with GRPO, so the SFT result is a restoration of an RL-degraded model.[^c8]

For generation tasks the labels are self-distilled: the model's own correct reasoning traces are kept. This protects accuracy. Fine-tuning on the original GSM8K labels dropped accuracy from 92.5% to 83.09%, versus 94.62% with self-distilled labels.[^c9]

## Why it matters for asking and answering

A calibrated confidence is what lets a system decide when to retrieve, escalate or defer. The paper's adaptive RAG consults retrieval only when the confidence of a context-free answer is below a threshold, and keeps the higher-confidence answer.[^c10] That use depends on the signal being calibrated, not merely accurate.

## Limits

- One main model family (Qwen3-4B) carries the training comparison; the SFT versus RL versus DPO ranking is not shown across sizes or families here.
- The theory is an informal argument about objectives. It does not predict the magnitude of degradation.
- SFT data covers the same seven tasks as evaluation; transfer of restored calibration to unseen tasks was not tested in what I read.
- Whether SFT's restoration costs reward-optimized abilities beyond accuracy on these tasks is not established.
- The "RL" in the paper means trust-region methods only.

## Related

- [[reward-only-advantage-miscalibration]] — a formal proof for GRPO that complements this informal mechanism
- [[calibration]] — the general concept being restored
- [[calibration-training]] — other training routes to calibration
- [[token-regeneration-probability-confidence]] — another probability-derived confidence readout
- [[rlhf-sycophancy-amplification]] — another RL side effect on model behavior

[^c1]: arxiv-2603-06604 — "This MLE objective naturally promotes calibration: the model’s output probabilities reflect"
[^c2]: arxiv-2603-06604 — "The advantage weighting Ât causes the model to"
[^c3]: arxiv-2603-06604 — "their confidence estimates reflect reward optimization rather than data distribution matching"
[^c4]: arxiv-2603-06604 — "DPO only cares"
[^c5]: arxiv-2603-06604 — "model achieves average AUROC of 0.879 and ECE of 0.034"
[^c6]: arxiv-2603-06604 — "mechanically reduced the confidence-accuracy gap without"
[^c7]: arxiv-2603-06604 — "AUROC drops"
[^c8]: arxiv-2603-06604 — "demonstrate that post-RL SFT can restore well-calibrated"
[^c9]: arxiv-2603-06604 — "causes accuracy to drop from"
[^c10]: arxiv-2603-06604 — "if ĉ1 < τ then"
