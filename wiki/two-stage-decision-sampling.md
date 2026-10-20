---
description: "A reasoning policy splits into sampling (propose an answer) and decision (stop or resample); self-correction is the decision stage discriminating right from wrong, not reflective wording."
aliases: ["two-stage decision-sampling hypothesis", "DS hypothesis", "sampling-decision decomposition", "sampling and decision policies"]
sources: ["arxiv-2601-01580"]
---
# Two-stage decision-sampling decomposition

A reasoning model's single policy can be read as two functions run in sequence. The sampling policy π_sample produces a candidate solution with its reasoning trace. The decision policy π_d then either stops, accepting the answer, or resamples, starting another attempt. The work calls this the Two-Stage Decision-Sampling (DS) Hypothesis and states its status plainly: "The decomposition is analytical, not architectural, the model remains a single" next-token predictor.[^c1] Decision steps are found in the text by proxy: verification and revision phrases mark them, and a resample is a revision marker followed by a new attempt.[^c2]

The reason for the split is to separate two things a reflective trace can do. A model can produce verification-like text fluently while its decision stage ignores whether the answer is right. The work therefore measures three quantities. p_s is the probability that a sample is correct, approximated by first-attempt accuracy. p_d|C is the probability of stopping given a correct answer. p_d|W is the probability of resampling given an incorrect one. "The parameter pd|C captures the probability of correctly accepting a correct answer; pd|W captures" the probability of correctly rejecting a wrong one.[^c3] Only the second kind of number is self-correction: a stop-rate on correct answers can be high for a model that never revises anything.

On arithmetic, with all models based on Qwen2.5-7B-Instruct,[^c4] the RL-trained model holds up out of distribution where the SFT model with reflection does not: "RL maintains 90% accuracy while SFT (reflection) drops to 49%" on the 3×6 tasks.[^c5] The calibration locates the difference in the decision stage. Sampling accuracy p_s falls steadily with difficulty for both. For RL, p_d|W stays in a usable range, "sustaining 40 60% even far out-of-distribution"; for SFT, "pd|W collapses toward zero on OOD tasks", so the model accepts its first answer and echoes it.[^c6] The paper's summary is that "RL’s superior generalization stems primarily from improved decision-making" rather than from better sampling.[^c7]

The decomposition also gives a frame for a prior result. Kang et al., as cited, found that for SFT "p(F → T ) remains flat at 3–5% regardless of data composition": training on more corrective transitions did not raise the rate at which a wrong answer is changed to a right one.[^c8] Read through the decomposition, SFT taught the sampling stage to write reflection-like text while leaving p_d|W untrained. The arithmetic model in the work is a calibration fit, so the account is a reading of two curves, not a measurement of two separate modules.

## Limits

- The evidence is one task family, multiplication, with a training range of 4×5 and 5×4 and tests on 3×3 to 3×9. "We adopt mathematical reasoning as our empirical context for its clarity" — the claim that the framework is domain-agnostic is not tested. "Extending the calibration-style decomposition of πsample and πd to these domains remains an important direction for future work."[^c9]
- The decision stage is operationalised by lexical proxies. "decision actions can be operationalized through identifiable proxy tokens that signal verification or revision intent"[^c2] — so p_d measures how a model acts on marker phrases, not an internal decision variable. A model could emit the marker without the discrimination, and the proxy would not separate the two.
- The calibration uses p_s from first-attempt accuracy and the decision parameters from observed stopping and resampling conditioned on correctness.[^c10] The fit is per model and per difficulty bin; I did not read the appendix with the intervals.
- The printed accuracy formula is a function of p_d|W with a sign that the stated definitions do not obviously give (my inference, not a quote): a higher probability of resampling a wrong answer appears to lower accuracy in that formula unless a resample is assumed to fail. I did not verify the derivation, so the formula should not be used as stated.
- The work analyses binary correctness rewards only.[^c11] Whether the same decision-stage split holds under partial credit or process rewards is not shown.
- The contrast with SFT rests on one SFT setup with the RL and SFT models sharing a base. Whether other factors, such as the on-policy nature of RL data, account for part of the gap is not separated here.

## Related

- [[length-weighted-kl-attribution]] — the training-side account of why the decision stage can be under-trained relative to sampling
- [[detection-recovery-gap]] — detecting a wrong trajectory does not predict recovery under intervention; p_d|W is a detection-and-resample measure, so the two should be read together
- [[solve-verify-detection-gap]] — the same split between producing an answer and checking one, seen in a different setting
- [[spontaneous-reasoning-shift-illusion]] — mid-trace pivots read as symptoms; the decision view explains why such text is not, by itself, correction
- [[entropy-gated-forced-reconsideration]] — forced reconsideration helps where first-pass entropy is high, a test of how a decision cue acts on sampling
- [[second-pass-gain-decomposition]] — the same accounting move: a second pass's gain split into counterfactual components
- [[two-stage-abstention-paradigm]] — shares only the two-phase form; its stages are report and commit, not sample and decide

[^c1]: arxiv-2601-01580 — "The decomposition is analytical, not architectural, the model remains a single"
[^c2]: arxiv-2601-01580 — "decision actions can be operationalized through identifiable proxy tokens that signal verification or revision intent"
[^c3]: arxiv-2601-01580 — "The parameter pd|C captures the probability of correctly accepting a correct answer; pd|W captures"
[^c4]: arxiv-2601-01580 — "All models are based on Qwen2.5-7B-Instruct"
[^c5]: arxiv-2601-01580 — "RL maintains 90% accuracy while SFT (reflection) drops to 49%"
[^c6]: arxiv-2601-01580 — "pd|W collapses toward zero on OOD tasks"
[^c7]: arxiv-2601-01580 — "RL’s superior generalization stems primarily from improved decision-making"
[^c8]: arxiv-2601-01580 — "p(F → T ) remains flat at 3–5% regardless of data composition"
[^c9]: arxiv-2601-01580 — "remains an important direction for future work"
[^c10]: arxiv-2601-01580 — "ps from first-attempt accuracy"
[^c11]: arxiv-2601-01580 — "We analyze binary correctness rewards"
