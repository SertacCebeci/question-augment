---
description: "A verifier that picks the best of k well can still send RL a bad signal: discrimination (AUC) and calibration (ECE) are separate properties that top-1 selection misses."
aliases: ["AUC and calibration of verifiers", "reward-model quality beyond TTS", "versatile reward model criteria"]
sources: ["arxiv-2512-21919"]
---
# Verifier discrimination and calibration

A verifier is usually scored by top-1 selection: sample k candidates, keep the one with the highest score, and check whether it is correct. This is test-time scaling (TTS). The SWE-RM study shows that this number does not say how a verifier behaves when its score is used as a reward in reinforcement learning. Two verifiers with nearly the same TTS gain (+4.7% and +4.5% on SWE-Bench Verified) gave very different RL runs: one improved smoothly, the other was unstable, "failing to provide reliable learning signals and eventually causing RL training to collapse."[^r1] The two differed in discrimination: "yet their AUC scores differ by 0.095."[^r2]

The paper names two properties that top-1 selection leaves out. *Discrimination* is how well the score separates resolved from unresolved trajectories across the whole distribution; it is measured by AUC.[^r3] *Calibration* is whether a score's value matches the empirical chance of being correct; it is measured by expected calibration error (ECE), a binned average of the gap between confidence and accuracy.[^r4] TTS, by contrast, "only measures a narrow slice of verifier capability": it asks only whether the single best candidate is ranked first.[^r5]

The paper's own account of why each matters for RL is a short derivation in its appendix, not a measured result. Compare the policy gradient weighted by the verifier score with the ideal gradient weighted by the true label.

- *Discrimination enters through pairs.* A correct trajectory ranked below an incorrect one gives a reversed contribution to the update; the paper states that "Mis-rankings imply reversed gradient contributions."[^r6] Since AUC is the fraction of correctly ordered positive–negative pairs, the fraction of reversed updates grows with 1 − AUC.
- *Calibration enters through magnitude.* When the score is used as the reward size, a systematic gap between score and frequency of correctness becomes a bias in the expected update. The paper defines the calibration bias at score α as the difference between the observed success rate and α, and says that ECE "is then a binned approximation of the expected magnitude of" this bias.[^r7] If the score is calibrated, "the RM induces no systematic bias in the expected gradient."[^r8] The paper's illustration: a normalized score of 0.9 that corresponds to a 60% chance of correctness misleads the policy about the value of its actions.[^r9]
- *Top-1 selection enters at the extreme.* If the top-ranked candidate is wrong, the batch contains a negative with the largest reward weight: "This does not imply that negatives have larger average rewards than positives, but it does imply that" the batch holds such a negative.[^r10]

The three can come apart. A verifier can rank the best candidate first and still have poor AUC, or discriminate well and be badly calibrated. In the paper's example, one verifier "suffers from widespread over- and under-confidence" while the other is about three times better on ECE, yet both had the same TTS.[^r11] So a single top-1 number cannot rank verifiers for RL use, and two numbers (AUC and ECE) are needed beside it. Whether the reversed-gradient fraction predicts the RL curves beyond the two-verifier comparison is the paper's claim, and this note has not checked it.

## Limits

- The motivating comparison is two early, small verifier variants. The paper itself says that "the discussion of metrics in this section is limited to using early, small-scale RM variants as illustrative examples."[^r12]
- The calibration and score-distribution analyses use trajectories from one policy, "sampled from Qwen3-Coder-Max."[^r13] A calibration gap may depend on the policy that generated the trajectories.
- The labels are themselves execution verdicts: trajectories are "labeled as positive or negative based on their execution results with the provided fail2pass test."[^r14] The reference for "correct" inherits the limits of the tests, which the paper raises against execution-based feedback in general.
- The gradient analysis uses plain policy gradient. The paper says "one can simply extend the analysis to GRPO setting," but the note does not check that extension.[^r15]
- AUC and ECE are not sufficient for usefulness. ECE can be low for a score that carries no information (see [[calibration]]), so calibration is necessary but not enough.

## Related

- [[calibration]] — ECE is the binned calibration measure; this note adds its reading as the bias of a reward-weighted update
- [[roc-curve]] — AUC as the probability that a correct item outranks an incorrect one
- [[score-separability]] — the same requirement that a score discriminate, here for abstention rather than for a reward
- [[reward-benchmark-downstream-correlation]] — whether a reward benchmark's ranking of models matches the ranking produced downstream; the question this note asks of a single verifier
- [[reward-only-advantage-miscalibration]] — GRPO's gradient read as AUC optimization, the policy-side view of the same ranking quantity

[^r1]: arxiv-2512-21919 — "failing to provide reliable learning signals and eventually causing RL training to collapse"
[^r2]: arxiv-2512-21919 — "yet their AUC scores differ by 0.095"
[^r3]: arxiv-2512-21919 — "AUC (Bradley, 1997) evaluates discriminative ability by measuring how well the verifier separates"
[^r4]: arxiv-2512-21919 — "a lower ECE means there is lower mismatch between confidence and accuracy"
[^r5]: arxiv-2512-21919 — "TTS only measures a narrow slice of verifier capability"
[^r6]: arxiv-2512-21919 — "Mis-rankings imply reversed gradient contributions"
[^r7]: arxiv-2512-21919 — "ECE is then a binned approximation of the expected magnitude of"
[^r8]: arxiv-2512-21919 — "meaning the RM induces no systematic bias in the expected gradient"
[^r9]: arxiv-2512-21919 — "a normalized score of 0.9 reflects only a 60% probability of being actual correct"
[^r10]: arxiv-2512-21919 — "This does not imply that negatives have larger average rewards than positives, but it does imply that"
[^r11]: arxiv-2512-21919 — "verifier B suffers from widespread over- and under-confidence"
[^r12]: arxiv-2512-21919 — "The discussion of metrics in this section is limited to using early, small-scale RM variants as illustrative examples"
[^r13]: arxiv-2512-21919 — "The trajectories used for calibration and score distribution analysis are sampled from Qwen3-Coder-Max"
[^r14]: arxiv-2512-21919 — "based on their execution results with the provided fail2pass test"
[^r15]: arxiv-2512-21919 — "one can simply extend the analysis to GRPO setting"
