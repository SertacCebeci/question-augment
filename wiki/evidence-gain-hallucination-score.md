---
description: "A deterministic answer-level hallucination score from the model's own log-probs: token-level confidence variance, amplified by how much removing the image shifts the answer's probability."
aliases: ["CEBaG", "Confidence-Evidence Bayesian Gain", "image-ablated pointwise mutual information", "token log-probability variance signal"]
sources: ["arxiv-2603-21693"]
---
# Evidence-gain hallucination score

**What it is.** For a short-form medical VQA answer r to question x_q about image x_v, score the same generated answer twice by teacher forcing: once with the image, once with the image removed. The difference of the two sequence log-probabilities is the evidence gain G = log P(r | x_v, x_q) − log P(r | x_q). By Bayes' rule this equals log P(x_v | r, x_q) − log P(x_v | x_q), so G is the pointwise mutual information between answer and image given the question.[^c1] The text-only probability plays the role of a language prior and the multimodal one the updated belief; the authors say this is information-theoretic, not Bayesian inference over parameters.[^c2]

**The score.** Two signals are combined: σ, the standard deviation of per-token log-probabilities in the with-image pass (high when confident function words sit beside low-confidence content tokens), and E = |G|/L, the mean absolute per-token shift caused by the image. The score is σ · (1 + E).[^c3] It reduces to σ when the image changes nothing, so visual evidence can sharpen but not override the uncertainty estimate, and the multiplicative form needs no coefficient to reconcile the scales of σ and E.[^c4] Cost is one greedy generation plus two scoring passes, no sampling, no external NLI model; the baselines Semantic Entropy and VASE need 10 to 20 stochastic generations plus an NLI model.[^c5]

**Measured.** Across four medical MLLMs and three VQA benchmarks (16 settings), with GREEN-score labels, it had the best AUC in 13 of 16 settings, averaging 67.9% against 59.6% for VASE, 57.4% for SE and 57.8% for RadFlag.[^c6] Ablation: σ alone reaches 67.0% average AUC, already above every baseline; E alone reaches 59.0%.[^c7] So most of the signal is in the variance of the model's own confidence across tokens; the image-shift term adds a smaller, complementary gain.

**Why it matters for asking and answering.** An answer's reliability can be read from how unevenly confident it is and whether the image actually moved the decisive tokens. In the paper's example, the image lifts a decisive token from near 0 to 90% for a grounded answer, but only to 3% for a hallucinated "Yes".[^c8] The reading that a model answering from its language prior alone (G near 0) is unreliable is the authors' framing; the ablation shows E alone is a weak detector.

## Limits

- Scope is short-form, answer-level detection in medical VQA; it is not claimed for long responses or sentence-level localization.
- Ground truth is the GREEN model's score below 1.0, so labels are themselves model-produced; the method was stable for thresholds 0.4 to 0.8.[^c9]
- Adding (1 + E) lowered AUC in under half the settings, usually marginally (e.g. −1.4 on LLaVA-Med SLAKE); because σ and E are unnormalized, their relative influence varies by model.[^c10]
- A tuned oracle variant reached 71.9% but the optimal weight was unstable (−5 to +2.75) and needs test labels; the gap is not recoverable parameter-free.[^c11]
- Point estimates only, no confidence intervals; four models, three datasets. Requires access to token log-probabilities, so it does not apply to closed models.
- The sign claim (negative G means contradiction) is interpretation; the score uses |G|.

## Related

- [[text-modality-dominance]] — models leaning on text over other modalities is the failure G ≈ 0 is meant to expose
- [[visual-evidence-scoring]] — another way to score how much visual evidence supports an answer
- [[gradient-norm-epistemic-uncertainty]] — another sample-free uncertainty signal from the model itself
- [[calibration]] — confidence signals are only useful if they track correctness

[^c1]: arxiv-2603-21693 — "Thus, G is the Pointwise Mutual Information (PMI) between the response"
[^c2]: arxiv-2603-21693 — "This is distinct from Bayesian inference over model parameters;"
[^c3]: arxiv-2603-21693 — "the absolute per-token log-probability"
[^c4]: arxiv-2603-21693 — "so visual evidence can only sharpen, never override, the uncertainty estimate."
[^c5]: arxiv-2603-21693 — "requires only one generation and two scoring passes, uses no external models, and is fully deterministic"
[^c6]: arxiv-2603-21693 — "CEBaG achieves the best AUC in 13 of 16 settings"
[^c7]: arxiv-2603-21693 — "σ-only achieves 67.0% average AUC, above all"
[^c8]: arxiv-2603-21693 — "Image moves the decisive token 0→90%"
[^c9]: arxiv-2603-21693 — "stable detection performance across GREEN thresholds between 0.4 and 0.8"
[^c10]: arxiv-2603-21693 — "In the rest, (1 + E) lowers"
[^c11]: arxiv-2603-21693 — "the optimal λ is unstable, ranging from −5 to +2.75."
