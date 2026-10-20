---
description: "Stable rank of a response's final-layer hidden-state matrix, the ratio of total to dominant-direction variance, is an annotation-free quality signal for reward and selection."
aliases: ["SR(H)", "effective dimensionality of hidden states", "stable rank of hidden states", "hidden-state stable rank"]
sources: ["arxiv-2512-02807"]
---
# Stable rank

Stable rank is a matrix measure of how many directions a matrix's energy spreads over. For a matrix H with singular values σ1 ≥ σ2 ≥ … it is the sum of the squared singular values divided by the squared largest one, so it equals the squared Frobenius norm over the squared spectral norm.[^s1] Applied to an LLM, H is the matrix of hidden states for the tokens of one response, taken from the final layer after a forward pass over the prompt-response pair. "Stable rank measures the effective dimensionality of H"[^s2] — when one singular value dominates the score falls toward 1, which the paper reads as representation collapse, and when the singular values are balanced it approaches rank(H).

The mechanism the work proposes is that the shape of that spectrum tracks response quality. A response whose tokens cluster along a few dominant directions has a low value, and one whose tokens spread across the embedding space has a high value. The motivation is a rank-collapse argument: the softmax-bottleneck line of work says expressive language modeling needs high-rank representations, and collapse into a narrow cone is associated with degraded generation.[^s3] The score is then used in three ways, each without any labels: as a zero-shot judge of which of two responses is preferred, as the selection rule in Best-of-N sampling, and as the reward in a GRPO-style policy update.[^s4]

The reported numbers are these. On RewardBench, with Qwen3-8B, the paper states that "stable rank achieves 84.04% accuracy on RewardBench and improves task accuracy by an average of 11.3 percentage points over greedy decoding via Best-of-N sampling."[^s5] The advantage is largest on small models: pointwise LLM-as-judge scoring falls to "37.15% on Qwen2.5-1.5B", while stable rank reaches 75.95% there.[^s6] In Best-of-N selection over four models, the paper reports that random selection "often degrades performance below greedy decoding", while stable rank selection does not.[^s7] Used as a reward, the frozen reference matters to the authors: "Using a frozen model is critical: it provides a stationary reward signal that the policy cannot manipulate by changing its own internal geometry."[^s8] The cost is small by the paper's own accounting, since "computing stable rank requires O(T d) operations", which it calls negligible next to the forward pass.[^s9]

What the score correlates with is a separate finding. Across 37 text metrics, the paper finds it tracks coherence and information density, and that it is negatively related to length: "Instead, stable rank favors information density."[^s10] Contrastive and causal connectives correlate positively, while enumeration and additive markers correlate negatively.[^s11]

## Limits

- The correlations are moderate. The paper's own words are "While these correlations are moderate in magnitude (|ρ| ≈ 0.2–0.4)", and they are sample-level, not a demonstration that the score causes quality.[^s12]
- The RewardBench figures are pairwise accuracies under the paper's protocol: the response with the higher stable rank is predicted to be preferred. They say nothing about whether a single absolute threshold on the score is meaningful for one response on its own.
- Length is not fully neutralized. The paper argues the score penalizes verbosity, but its evidence is a negative correlation with token and sentence counts. I did not find a test in the parts I read where a policy is optimized against the score and then checked for gaming.
- The score needs the whole response. The paper reports truncation loss: "Code suffers the largest degradation (87.91% to 24.80%)" when the input is cut to 128 tokens.[^s13]
- The link to correctness is inferred from benchmark gains. The paper writes that its results "confirm that stable rank captures quality signals that correlate strongly with correctness", but the slices I read report accuracy on benchmarks, not a per-response correlation with correctness.[^s14]
- The method needs white-box access to final-layer hidden states. It cannot be applied to an API-only model; that restriction is my inference from the design, not a limit the paper states.
- The alignment experiments are small: two 1.5B-scale models trained with LoRA. Larger policies and other reward regimes are not tested in what I read.
- The layer choice is a finding about this task. The paper's cross-layer analysis "confirms that the final layer embeddings yield the strongest quality signal".[^s15] This is a different question from which layer carries uncertainty information, where middle layers are reported as more informative.

## Related

- [[representation-geometry-calibration]] — the same dominant-direction idea, used per token as an angle to a cone for abstention, where this note uses one spectral scalar over the whole response.
- [[cross-layer-probe-ensemble]] — also reads hidden states across depth; it finds middle layers informative for probes, where this measure's authors find the final layer best for response quality.
- [[lsde-response-quality-signal]] — another annotation-free response score used as a reward, built from surface features rather than hidden-state geometry.
- [[test-time-scaling]] — Best-of-N selection is the setting where this score is used to pick among samples.
- [[nonlinear-hidden-state-probe]] — the supervised alternative: a probe trained on labels reads the same kind of states, where stable rank needs no labels.

[^s1]: arxiv-2512-02807
[^s2]: arxiv-2512-02807 — "Stable rank measures the effective dimensionality of H"
[^s3]: arxiv-2512-02807 — "generation quality degrades"
[^s4]: arxiv-2512-02807 — "we employ stable rank as a live reward"
[^s5]: arxiv-2512-02807 — "stable rank achieves 84.04% accuracy on RewardBench and improves task accuracy by an average of 11.3 percentage points over greedy decoding via Best-of-N sampling"
[^s6]: arxiv-2512-02807 — "on smaller ones (37.15% on Qwen2.5-1.5B)"
[^s7]: arxiv-2512-02807 — "Notably, random selection often degrades performance below greedy decoding"
[^s8]: arxiv-2512-02807 — "Using a frozen model is critical: it provides a"
[^s9]: arxiv-2512-02807 — "Computing stable rank requires O(T d) operations"
[^s10]: arxiv-2512-02807 — "Instead, stable rank favors information density."
[^s11]: arxiv-2512-02807
[^s12]: arxiv-2512-02807 — "While these correlations are moderate in magnitude"
[^s13]: arxiv-2512-02807 — "Code suffers the largest degradation (87.91% to 24.80%)"
[^s14]: arxiv-2512-02807 — "These results confirm that stable rank captures quality signals that"
[^s15]: arxiv-2512-02807 — "confirms that the final layer embeddings yield the strongest"
