---
description: "RL on a logarithmic-scoring-rule reward over only the confidence tokens calibrates a model's stated confidence without touching task output, and beats supervised tuning on confidence values."
aliases: ["ConRad", "scoring-rule RL for verbalized confidence", "log-score confidence reward", "proper-scoring-rule confidence reward", "Brier-type confidence reward"]
sources: ["arxiv-2603-29492", "doi-10-48550-arxiv-2604-05306"]
---
# Log-score reward for verbalized confidence

A model that writes a number next to its answer can be trained to make that number true by rewarding it with a strictly proper scoring rule, applied to the confidence tokens alone.

## Mechanism

Calibration is defined as expected correctness matching stated confidence: "E[s | p̂ = x] = x".[^c1] The reward is the logarithmic score against a correctness target s in [0,1] (report level) or a binary fi per sentence (sentence level, averaged over sentences). The log rule is "a strictly proper scoring rule where the expected reward is uniquely maximized if and only if the predicted probability matches the true distribution".[^c2] So the reward is maximized only by saying what one believes the chance of being right is. This is the same incentive as any [[calibration]] scoring, here used as an RL reward.

Three design choices carry the result in the radiology-report study (ConRad, a 4-bit MedGemma-4B tuned with LoRA and GRPO on MIMIC-CXR):

- **Loss only on confidence tokens.** "We therefore only calculate a loss for the tokens involved in confidence expression, ensuring that the task performance remains stable."[^c3] The GREEN report-quality control stayed at 0.252 against 0.257 for prompted verbalization.[^c4]
- **Continuous reward over ordinal numbers.** Supervised tuning "treats numerical confidence tokens as independent categorical labels and can ignore their ordinal structure"; the RL reward varies with distance so near-misses beat large misses.[^c5] The authors report that the RL-trained model puts probability on adjacent levels, while the supervised one gives an incoherent pattern.
- **An automated correctness signal.** The target comes from a judge metric (GREEN) against the reference report, so no human confidence labels are needed. At sentence level an adapted "Precision GREEN" gives a binary target.

A quadratic, Brier-type reward on the same kind of output has been trained the same way. In arXiv:2604.05306 the confidence-aware reward is 2p − p² when the final answer is correct and −p² otherwise, and it "penalizes overconfident errors, and is applied only after the full reasoning trajectory is" completed.[^c11] By my reading, and the paper does not use the term, this is a proper scoring rule: its expected value is largest when the stated p equals the probability of being correct. On the paper's calibration evaluation, ECE falls "from 0.383 to 0.049" and the Brier score "from 0.504 to 0.166".[^c12][^c13] These are the same kind of reward as the log rule above, with a different rule and a different model family, so they support the mechanism without measuring the log rule against the quadratic one.

## What was measured

Report level (ECE, lower is better): prompted base 0.642; supervised on GREEN scores 0.206; trained probe on hidden states 0.121; ConRad 0.106, with the highest Pearson correlation to correctness (0.431 against 0.372 for the probe).[^c6] Sequence probability, P(True) and self-consistency were worse (ECE 0.40 to 0.53). Sentence level is harder: ECE 0.239 against 0.438 for prompted verbalization and AUROC 0.633 against 0.558; the supervised variant (0.446) was no better than prompting, which the authors attribute to binary targets that SFT can only reproduce.[^c7] Zero-shot on IU-Xray, ECE went from 0.310 to 0.034.[^c8]

Use as a filter: precision of kept sentences rose monotonically with the threshold for ConRad (0.421 all, 0.560 at confidence at least 8, 0.642 at 10), whereas the base model's stated confidence barely moved precision (0.425 to 0.447). The cost is coverage: only 53 sentences survived at 10, and report GREEN fell from 0.262 to 0.097, so the authors say low-confidence sentences "should be flagged for human review rather than automatically removed".[^c9]

In a small clinical check (50 reports, three raters), ConRad's report confidences aligned better with clinician ratings than the prompted baseline's.[^c10]

## Limits

- One model, one task (chest X-ray findings), one correctness judge. Calibration is relative to the judge's score against a reference report, which is not clinical truth; the study itself calls the clinical check "small-scale".
- Sentence-level calibration remains weak (ECE 0.239), and the sentence-level and trained-probe comparisons use different training sizes (1500 and 3000 samples).
- The 53-sentence cell at confidence 10 is too small to settle a precision claim; precision is judged by an LLM against a reference, so unreferenced but true findings count as errors.
- The guarantee of optimal calibration is the property of the scoring rule under reward maximization; it is not shown that GRPO on a 4B model reaches the optimum, only that ECE falls.
- Another work found that folding a Brier confidence term into a single GRPO reward collapsed confidence toward high values (see [[decoupled-claim-calibration-training]]). This work avoids that by masking the loss to confidence tokens, but the two were not compared head to head.
- Whether confidence trained this way changes what a model asks or when it stops is not tested.
- Tension with the joint-reward result. The quadratic-reward work applies its confidence reward inside GRPO and reports no collapse toward high confidence (ECE 0.049), which sits against the collapse reported in [[decoupled-claim-calibration-training]]. Its own intuition is that "GRPO should suppress confident wrong trajectories and amplify" them.[^c14] Whether that work's reward is a single joint term, as in the staged-versus-joint comparison, is not clear from the text read here, and the two were not compared head to head.

## Related

- [[calibration]] — the property being trained.
- [[calibration-training]] — human training by scored feedback; here the scored feedback is an RL reward.
- [[decoupled-claim-calibration-training]] — a staged alternative that reports joint-reward collapse.
- [[savor-calibration-abstention-reward]] — another reward-shaped route to calibrated abstention.
- [[delayed-outcome-brier-reward]] — a Brier-type reward used on delayed outcomes.

[^c1]: arxiv-2603-29492 — "E[s | p̂ = x] = x,"
[^c2]: arxiv-2603-29492 — "a strictly proper scoring rule where the expected reward is uniquely maximized if and only if the predicted probability matches the true distribution"
[^c3]: arxiv-2603-29492 — "We therefore only calculate a loss for the tokens involved in confidence expression, ensuring that the task performance remains stable."
[^c4]: arxiv-2603-29492 — "report correctness remains stable compared to Verbalize Base during training"
[^c5]: arxiv-2603-29492 — "treats numerical confidence tokens as independent categorical labels and can ignore their ordinal"
[^c6]: arxiv-2603-29492 — "ConRad outperforms all baselines, reducing the ECE by over 80% compared to the base model and achieving the"
[^c7]: arxiv-2603-29492 — "sentence-level calibration remains more challenging than report-level calibration, where we observe stronger overall results."
[^c8]: arxiv-2603-29492 — "ECE improving"
[^c9]: arxiv-2603-29492 — "This suggests that low-confidence sentences should be flagged for human review rather"
[^c10]: arxiv-2603-29492 — "indicating that the calibration gains of ConRad"
[^c11]: doi-10-48550-arxiv-2604-05306 — "penalizes overconfident errors, and is applied only after the full reasoning trajectory is"
[^c12]: doi-10-48550-arxiv-2604-05306 — "ECE drops from 0.383 to 0.049"
[^c13]: doi-10-48550-arxiv-2604-05306 — "Brier score from 0.504 to 0.166"
[^c14]: doi-10-48550-arxiv-2604-05306 — "GRPO should suppress confident wrong trajectories and amplify"
