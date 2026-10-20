---
description: "Paraphrased test items in training evade likelihood and edit-distance detectors; the variance of tail-token difficulty across temperature samples separates them (AUC about 0.67-0.77)."
aliases: ["variant contamination", "DVD", "Detection via Variance of generation Distribution", "variance of synthetic difficulty"]
sources: ["arxiv-2601-04895"]
---
# Variant contamination and detection by generation variance

Benchmark contamination is usually pictured as verbatim leakage. Variant contamination is the case where training data holds items that are logically equivalent to test items but rewritten on the surface. Liang et al. (2026) define it as v = τ(x) with f(v) = f(x), where f extracts the core informational content, and call a model contaminated on x if such a v is in its training corpus.[^c1] Variants may differ in vocabulary, phrasing or narrative structure while keeping the same knowledge, logical dependencies and solution trajectory.

## Why existing detectors fail

Perplexity, loss, Zlib, Min-K%, edit-distance (CDD) and embedding similarity read surface-level features of one output or of the answer's likelihood. After rewriting, those cues weaken. In the authors' fine-tuning simulation, Loss, Perplexity and Zlib sit below chance (AUC 0.33 to 0.5) on SuperGPQA, meaning their ranking is inverted, and CDD stays near 0.50 on Omni-MATH.[^c2] Min-K%++ is the strongest baseline on Omni-MATH but falls as low as 0.278 on SuperGPQA.[^c3] The point for anyone auditing a benchmark: a detector that works on exact copies can be worse than a coin on paraphrased ones, and its sign can flip across datasets.

## The mechanism: variance of tail-token difficulty

DVD samples N = 50 responses at temperature from a fixed prompt. For each response it takes the k = 20 least probable tokens, sums their log-likelihoods and divides by length; this is "synthetic difficulty" D. The detection score is the sample variance of D across the N responses.[^c4]

The account is a two-state mixture. A contaminated item makes generation alternate between memory adherence (following a memorized template) and perturbation drift (free exploration driven by sampling noise); an uncontaminated item stays in drift only.[^c5] By the within/between decomposition of a mixture's variance, two states with different means inflate total variance above that of either state alone, so contaminated items score high.[^c6] The method is training-free, single-sample (per item) and needs token probabilities, so it excludes closed models.

## What was measured

Contamination was simulated: GPT-4o generated variants by entity substitution, scenario transformation, numerical rewriting and narrative restructuring, filtered by a GPT-4o check for unchanged information and solution quality, and injected into fine-tuning data for Qwen2.5 (1.5B to 32B) and Llama3.1-8B, on Omni-MATH and SuperGPQA, with full fine-tuning (1 epoch) and LoRA (10 epochs).[^c7] DVD's AUC was 0.667 to 0.747 on Omni-MATH under full fine-tuning and reached 0.771 on Qwen-1.5B with LoRA, where the next best baseline reached 0.646.[^c8] Averages over ten runs per epoch stayed high across epochs 1 to 10 and across scales.

## Limits

- Contamination is simulated by fine-tuning on GPT-4o variants of the test items; no naturally contaminated pretrained model was tested. Real pretraining exposure is far more diffuse, so the bimodal-mixture picture may not hold.
- The mixture argument is a modelling assumption; the paper states the memory state's mean difficulty "empirically" differs, but bimodality is shown by an illustrative figure, not a tested statistic (my reading).
- AUC of 0.67 to 0.77 is better than baselines but far from reliable per-item classification.
- Closed-source models are excluded; only two domains (maths, multiple-choice general reasoning); one variant generator and one filter.
- Hyperparameters (k = 20, N = 50) are fixed at one setting in the quoted comparison; the 50 sampled responses per item are a cost.
- Whether high variance arises from memorization specifically, versus any instability such as a hard item, is not separated here (my inference).

## Related

- [[benchmark-contamination-convergent-audit]] — the audit side: probes that estimate exposure by overlap and rewording; DVD targets rewording-evading exposure
- [[post-cutoff-corpus-benchmark-isolation]] — avoiding contamination by construction instead of detecting it
- [[evidence-degradation-test-for-memorization]] — another way to separate recall from reasoning
- [[contamination-robust-selective-calibration]] — handling contaminated evaluations downstream

[^c1]: arxiv-2601-04895 — "If such a variant v appears in the training corpus of model M , we say that M is"
[^c2]: arxiv-2601-04895 — "Similarly, Perplexity and"
[^c3]: arxiv-2601-04895 — "where it drops as low as 0.278 (Table 3). This indicates that while focusing on outlier token probabilities helps in structured mathematical domains,"
[^c4]: arxiv-2601-04895 — "This statistic captures local uncertainty in the"
[^c5]: arxiv-2601-04895 — "these two states, producing substantial variability"
[^c6]: arxiv-2601-04895 — "According to the variance decomposition principle for mixture distributions, if"
[^c7]: arxiv-2601-04895 — "covering four categories: entity substitution, scenario conversion, numerical rewriting, and narrative restructuring. Through these surface-level"
[^c8]: arxiv-2601-04895 — "DVD achieves an AUC of 0.771 on Qwen-1.5B,"
