---
description: "A small student maps a prompt's hidden state to a density over answer embeddings, distilled from sampled answers; its entropy forecasts hallucination pre-generation and its likelihood checks answers."
aliases: ["SSD", "semantic distribution distillation", "prompt-conditioned semantic density"]
sources: ["arxiv-2602-04577"]
---
# Semantic self-distillation

Sampling-based semantic dispersion (see [[semantic-entropy]]) detects hallucination but needs many completions per prompt. Semantic Self-Distillation (SSD) pays that cost once, at training time. For each training prompt it takes the last-token hidden state h from one chosen layer, samples S completions from the base model, and embeds each with an off-the-shelf sequence-embedding model (then PCA). A mixture density network is fitted by conditional maximum likelihood to predict the distribution of those embeddings from h alone.[^c1]

At inference one forward pass yields a density over possible answers before any answer exists. Two readouts follow. The prompt-level readout is the order-2 Renyi entropy of the density, chosen because it has an exact closed form for Gaussian mixtures, so no sampling is needed at deployment.[^c2] The answer-level readout embeds a candidate answer and scores its log-likelihood under the density; low likelihood marks the answer as out-of-domain for that prompt.[^c3]

## What was measured

Against a "teacher dispersion" (the standard deviation of the teacher's 32 sampled embeddings), the student's entropy beat the teacher on AUROC for four of seven models on TriviaQA and on AUPRC for all seven, despite no inference-time sampling. The authors attribute this partly to smoothing: the finite-sample teacher statistic gives zero uncertainty where its samples happen to agree.[^c4]

Against other baselines, semantic entropy was best on TriviaQA and a supervised correctness probe was best on MMLU; SSD's pre-generation accuracy was "slightly weaker than specialized probes". Its distinct position is probe-level latency, no entailment-based target construction, and an explicit density.[^c5] Quality depends on the base model: TriviaQA AUROC was 74.9 for Ministral 8B but 67.7 for Qwen3 8B, which the authors trace mainly to how faithfully the semantic distribution can be predicted from the prompt representation.[^c6]

The likelihood readout separates a model's own answer from a random answer drawn from another prompt at AUROC above 0.95 for most models, and keeps 0.75-0.84 when the student is applied to the dataset it was not trained on.[^c7] As a post-generation hallucination predictor it is weak (about 0.6), and the authors do not advocate it standalone.[^c8]

The mechanism, in my reading: the object preserved is the shape of the answer space (which answers are plausible for this question), not a scalar risk, which is what lets one estimator both forecast risk and judge a specific answer. That reading is mine, not a tested claim.

## Limits

- Only short-form QA (TriviaQA, open-ended MMLU) and seven small open models were tested; the claim of generality to other sequence domains is stated, not shown.
- Correctness labels came from an LLM judge.
- Pre-generation performance trails specialised supervised probes, and varies by model with distillation fidelity.
- The student inherits the teacher's blind spots: it distils sampled dispersion, so a model that answers wrongly but consistently yields a confident, low-entropy density (compare [[confidently-wrong-low-entropy-regime]]). This is my inference; the paper does not test it.
- Depends on the choice of embedding model and layer, both treated as hyperparameters.

## Related

- [[semantic-entropy]] — the sampling-based teacher signal this distils into one pass.
- [[pre-generation-success-probe]] — a scalar probe on pre-generation activations; SSD keeps a distribution instead.
- [[internal-prober]] — another hidden-state predictor made before any answer is generated.
- [[confidently-wrong-low-entropy-regime]] — the regime where any entropy-based score, distilled or not, is blind.

[^c1]: arxiv-2602-04577 — "SSD trains a small student model to predict a prompt-conditioned distribution over semantic answer embeddings."
[^c2]: arxiv-2602-04577 — "We use Rényi-2 because it yields an exact closed form for Gaussian mixtures"
[^c3]: arxiv-2602-04577 — "We may treat answers with low likelihood as out-of-domain relative to the prompt context."
[^c4]: arxiv-2602-04577 — "SSD outperforms TD on four of the seven models investigated in terms of"
[^c5]: arxiv-2602-04577 — "SSD occupies a distinct regime: it matches probe-level inference latency, avoids entailment-based target construction during training, and preserves an explicit"
[^c6]: arxiv-2602-04577 — "AUROC of 74.9 for Ministral 8B but only 67.7 for Qwen3"
[^c7]: arxiv-2602-04577 — "retain AUROCs of 0.75–0.84 (Appendix B.3)."
[^c8]: arxiv-2602-04577 — "We therefore do not advocate the likelihood as a stand-alone"
