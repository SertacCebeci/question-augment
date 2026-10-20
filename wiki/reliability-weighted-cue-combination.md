---
description: "Two noisy cues about one magnitude are best combined with weights inverse to their variances; some LLMs fail to down-weight the noisier cue, even at top accuracy."
aliases: ["Bayes-optimal cue combination", "inverse-variance cue combination", "BLUE combiner", "reliability-weighted fusion of cues"]
sources: ["arxiv-2512-02719"]
---
# Reliability-weighted cue combination

When one magnitude can be read from two channels with different noise, averaging the two readings equally wastes the better channel. The normative rule weights each cue by its reliability. For independent, unbiased, Gaussian noise that reliability is the inverse variance: each cue's weight is its inverse variance divided by the sum of both inverse variances. The paper calls this rule "the optimal linear unbiased combiner" under linear-Gaussian assumptions.[^r1] In its Table 1 the variances are "in the text-only and image-only conditions respectively", estimated from the model's own responses in each condition.[^r2]

The mechanism is simple to state and easy to test. Adding noise to one channel raises that channel's variance, so the rule must move weight to the other channel. The paper applies this with Gaussian blur on the image: the noise ablation is "aimed at studying how LLMs may reweight information in the presence of noise".[^r3] Several models do this. On the line-length ratio task, "many LLMs are able to downweigh the image modality in" the presence of noise, which the authors read as Bayes-consistent adaptation.[^r4]

Some models do not. GPT-5 Mini reaches near-perfect text accuracy on the maze task, where a Bayes-optimal combiner would nearly drop the image. The paper says "a Bayes-optimal combination must significantly" down-weight the image there, and that GPT-5 Mini "appears unable to downweight its image input to" that extent.[^r5] The abstract puts it as a capability failure: the model "fails to integrate visual cues efficiently."[^r6] The lesson for a reader is that accuracy in the text channel alone does not show that the two channels are combined well. The paper measures this with a cue-combination efficiency, and GPT-5 Mini "shows poor" efficiency despite its strong error figure.[^r7]

The linear rule is a yardstick, not a ceiling. Llama-4 Maverick does better than the linear reliability-weighted combiner, which the paper reads as use of more than linear fusion: the model "may be leveraging additional non-linear properties not assumed under our linear baseline."[^r8] A nonlinear random forest fits its multimodal responses better than linear variants.[^r9] The paper's own conclusion is that under linear-Gaussian noise the combiner "provides a natural" benchmark for improvement.[^r10]

What survives the transfer, as my inference: inverse-variance weighting is a reference for any two numeric estimates of one quantity whose noise can be measured. What does not survive automatically is the variance itself. For a free-text answer there is no obvious variance, and the paper uses sampled numeric responses to get one. The reward-fusion note [[reliability-weighted-signal-fusion]] uses the same inverse-variance rule as one label-free reliability proxy, but there it weights reward signals, not two estimates of one magnitude, and it does not test that the rule tracks correctness.

## Limits

- The evidence is numeric magnitude estimation on three multimodal tasks, nine models, and one kind of noise. The paper chose Gaussian noise "for its tractability and ubiquity," so other noise types (occlusion, compression, text corruption) are not tested.[^r11]
- Both combiner variants depend on variance estimates from the same model's responses. The paper reports "Oracle (calibrated, covariance-based) and NonOracle (uncalibrated, variance-based) variants", so the reference itself is an estimate.[^r12]
- The Gaussian assumption is not checked for LLM responses. The nonlinear fit above shows that the linear model misses structure in at least one model, so a low efficiency score can reflect a wrong reference as well as a wrong weight.
- The human comparison is partial: the paper "ran a human baseline study for comparison on all our tasks", as a reference point and not as a main result.[^r13]
- Not tested for verification or retrieval channels. The wiki's [[cross-modal-aggregation-gap]] note records a different task, claim verification from a figure and its caption, where the two channels are not combined into one judgment. This paper does not test that task, so the two results are a comparison, not a replication (my reading).

## Related

- [[precision-weighted-prior-pull]] — the same precision weighting, with a prior in place of a second cue
- [[reliability-weighted-signal-fusion]] — inverse-variance reliability reused as a label-free weight for reward signals
- [[cross-modal-aggregation-gap]] — figure and caption not combined into one verdict in claim verification, a failure to combine channels in a different task
- [[text-prior-over-visual-evidence]] — the text channel dominating a multimodal answer when the image is hard to use

[^r1]: arxiv-2512-02719 — "This fusion is the optimal linear unbiased combiner"
[^r2]: arxiv-2512-02719 — "in the text-only and image-only conditions respectively"
[^r3]: arxiv-2512-02719 — "how LLMs may reweight information in the presence of noise"
[^r4]: arxiv-2512-02719 — "many LLMs are able to downweigh the image modality in"
[^r5]: arxiv-2512-02719 — "it appears unable to downweight its image input to"
[^r6]: arxiv-2512-02719 — "fails to integrate visual cues efficiently"
[^r7]: arxiv-2512-02719 — "GPT-5 Mini, despite its strong NRMSE performance, shows poor"
[^r8]: arxiv-2512-02719 — "may be leveraging additional non-linear properties not assumed under our linear baseline"
[^r9]: arxiv-2512-02719 — "a nonlinear random forest is indeed better able to fit its multimodal responses"
[^r10]: arxiv-2512-02719 — "Under linear-Gaussian noise, the Bayesian cue combiner is optimal and thus provides a natural"
[^r11]: arxiv-2512-02719 — "We chose gaussian noise for its"
[^r12]: arxiv-2512-02719 — "Oracle (calibrated, covariance-based) and NonOracle (uncalibrated, variance-based) variants"
[^r13]: arxiv-2512-02719 — "ran a human baseline study for comparison on all our tasks"