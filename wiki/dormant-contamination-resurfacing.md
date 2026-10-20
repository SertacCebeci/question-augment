---
description: "Continued clean pre-training can shrink a contaminated model's lead on leaked test items to near zero, yet SFT or GRPO afterwards brings the gap back: the leak is submerged, not erased."
aliases: ["submerged contamination", "latent leakage", "contamination masked by continued pre-training", "post-training resurfacing of leakage"]
sources: ["arxiv-2601-06103"]
---
# Dormant contamination resurfaced by post-training

A test item that leaks into pre-training makes a model look better on it, but that lift is not stable over the life of the model. Kocyigit and Yildirim inject five copies of GSM8K and MBPP test items into the first 2B tokens of a 25B-token extended pre-training mix. The contaminated model's advantage then decays as clean training continues. Their abstract puts it as contamination "causes performance spikes that are gradually diminished with continued pre-training," so that "the apparent performance inflation of contamination can become close to zero."[^c1] The spike-then-decay shape matches earlier pre-training work, where the contaminated model's accuracy "spikes at the time of contamination then decreases back to the same level as the clean model."[^c2] Measured at the pre-trained checkpoint, the leak is close to invisible. The paper reports that five copies of the test set "does not seem to cause measurable and consistent performance inflation" against an uncontaminated base.[^c3]

Post-training brings the gap back. SFT and GRPO were each run as a separate experiment on the clean training split, and the contaminated model led again. "After post-training the performance gap is above 2% for all models for both" the math and the coding benchmarks, the one exception being Qwen2.5-0.5B under SFT on GSM8K. The gap reaches 4% for the smallest model.[^c4] The authors' reading is that the leak is hidden rather than removed: "the leaked information is merely submerged not erased and is readily" rediscovered in post-training, since "the information is not forgotten and can be uncovered with task-specific" tuning.[^c5][^c6]

The mechanism the paper proposes is that continued clean training dilutes what the model says about the leaked items while the content stays in the weights, and a task-specific objective reads it out again. The measurements are accuracy gaps between contaminated and clean models; the paper does not inspect internal representations. "Stored but submerged" is therefore its interpretation of those gaps, not a measured internal state (my inference about what the gaps can carry).

The consequence for audits is a timing claim. A contamination check taken at the pre-trained checkpoint can report near-zero exposure for a model that a later fine-tune would show to be leaking. Whether the revealed gap is over-estimation or real capability depends on the post-training recipe, which is the subject of [[post-training-recipe-contamination-transfer]].

## Limits

- The exposure is a single late injection. "Our study purposefully isolates a 5-copy, late-injection contamination scenario."[^c7] The authors add that real leakage "can be multi-pass, paraphrased, or distributed throughout pre-training, and its effects may differ."[^c8] Neither a repeated nor a spread-out leak was tested, so the decay curve may not transfer.
- The scope is narrow: "we restrict model sizes to 4B parameters and focus on two open-weights families."[^c9] Only Qwen2.5 at 0.5B and 1.5B and Gemma3 at 1B and 4B were run.
- The post-training data was clean in these runs: "The applied post-training steps do not have any contamination." Whether the resurfacing grows when the post-training set itself carries leakage is not tested.[^c10]
- The pre-training was extended rather than full, "due to compute constraints," so the decay under a realistic full run is not measured.[^c11]
- The error bars cover evaluation noise only. They "do not include training-seed variability."[^c12] A gap of a few points from one training run per cell is a suggestive size, not a settled one.

## Related

- [[post-training-recipe-contamination-transfer]] — the same experiment; this note fixes the timing of the revealed gap, that note asks which recipe lets it carry over to uncontaminated tasks
- [[benchmark-contamination-convergent-audit]] — audits a finished model with three probes; this note's point is that a checkpoint-stage reading can miss leakage a later fine-tune exposes (my inference)
- [[post-cutoff-corpus-benchmark-isolation]] — avoids contamination by construction, so the decay question does not arise

[^c1]: arxiv-2601-06103 — "are gradually diminished with continued pre-training"
[^c2]: arxiv-2601-06103 — "performance of the contaminated model spikes at the time of contamination then decreases back to"
[^c3]: arxiv-2601-06103 — "does not seem to cause measurable and consistent performance inflation"
[^c4]: arxiv-2601-06103 — "After post-training the performance gap is above 2% for all models for both"
[^c5]: arxiv-2601-06103 — "the leaked information is merely submerged not erased and is readily"
[^c6]: arxiv-2601-06103 — "the information is not forgotten and can be uncovered with task-specific"
[^c7]: arxiv-2601-06103 — "Our study purposefully isolates a 5-copy, late-injection contamination scenario."
[^c8]: arxiv-2601-06103 — "can be multi-pass, paraphrased, or distributed throughout pre-training, and its effects may differ."
[^c9]: arxiv-2601-06103 — "we restrict model sizes to 4B parameters and focus on two open-weights families."
[^c10]: arxiv-2601-06103 — "The applied post-training steps do not have any contamination."
[^c11]: arxiv-2601-06103 — "constraints, we ran our experiments as extended pre-training runs."
[^c12]: arxiv-2601-06103 — "do not include training-seed variability"
