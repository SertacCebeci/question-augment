---
description: "Stating success probability before answering, trained against the policy's own group success rate with separate advantages per segment, calibrates confidence cheaply and avoids reward hacking."
aliases: ["CoCA", "confidence-first paradigm", "segmented GRPO for confidence and answers", "group-wise empirical success rate target"]
sources: ["arxiv-2603-05881", "arxiv-2512-14273"]
---
# Confidence-first training with segmented credit

Most uncertainty estimates are answer-first: confidence is produced after a response and scores that one response. A confidence-first model instead writes a number before answering, read as its probability of answering the question correctly under its current policy.[^c1] CoCA trains this with GRPO, and three design choices carry it.

## Mechanism

**Dynamic target.** For each prompt the policy samples a group of G outputs. The confidence target is the group-wise empirical success rate (GESR), the fraction of those samples whose answer is correct.[^c2] Because the target is recomputed from current rollouts, it tracks the model as it changes; frozen correctness labels are what the authors blame for predictors learning surface features such as problem difficulty.[^c3]

**Brier-type reward.** The confidence segment is rewarded with the negative squared gap between the parsed stated score and GESR, so confident-but-wrong and hesitant-but-right outputs are penalised hardest.[^c4] The answer segment gets a 0/1 correctness reward.

**Segmented credit.** The output has a fixed format, confidence tags then answer. Separate group-normalised advantages are computed for the two rewards and each is applied only to its own token span.[^c5] The reason given: if accuracy is trained first and confidence second, "the model may improve the confidence objective by altering answer behavior (e.g., refusal or evasiveness)".[^c6] Training both at once with span-restricted advantages anchors answer quality while confidence is learned.

The same span restriction appears outside confidence training. In a video grounded question-answering paper, the standard GRPO advantage gives "an identical reward (advantage) to every token in a sequence", and a token-selective variant "selectively attributes credit to tokens specifically for temporal grounding or question answering".[^c13] Its component-level gain is modest: NExT-GQA mIoU went "35.3→36.9" over baseline GRPO.[^c14] See [[coarse-to-fine-evidence-zoom]].

## What was measured

- Trained on math only, Qwen2.5-3B-Instruct went from ECE 0.54 to 0.09 on math and 0.66 to 0.14 on factual QA, outperforming confidence-first baselines.[^c7]
- Because confidence arrives in about 10 tokens, the confidence-estimation token cost is cut by more than 92 percent against answer-first methods, which allows early routing or termination.[^c8]
- Sequential confidence training shows reward hacking: confidence reward climbs while response length collapses, with degenerate outputs such as a near-zero confidence followed by a request for more context.[^c9]
- Against a joint reward applied to the whole sequence, segmented rewards raised the confidence reward more while accuracy reward stayed comparable, and gave lower ECE and Brier score on out-of-domain code and factual QA.[^c10]
- AUROC differences against answer-first baselines were small, so the gain is mainly calibration and cost, not better discrimination (the paper's own reading, not tested further).[^c11]

## Limits

- Training uses automatically verifiable math and code only; the authors state that open-ended QA, summarization or dialogue, where correctness is ambiguous, is not covered.[^c12]
- Hard-math test sets are small, so AUROC and calibration vary with training stochasticity and checkpoint choice.[^c12]
- GESR is a noisy estimate from G samples of one prompt; how sensitive the result is to G was not something I checked in the slices read.
- A pre-answer number cannot use anything learned while reasoning; whether this costs discrimination on questions whose difficulty only shows during solution is my inference, not measured here.
- Another work reports that folding a Brier term into a single reward collapsed confidence; this paper's joint-versus-segmented ablation is consistent with that, though the setups differ.

## Related

- [[log-score-verbalized-confidence-reward]] — also trains confidence tokens alone with a proper-scoring reward; there the target is a judge score, here the policy's own success rate.
- [[decoupled-claim-calibration-training]] — staged alternative that reports joint-reward collapse.
- [[calibration]] — the property being trained.
- [[coarse-to-fine-evidence-zoom]] — a video grounding paper that uses the same span-restricted credit for grounding tokens and answer tokens, with a reward that checks the localized evidence.
- [[reasoning-contamination-of-verbalized-confidence]] — confidence stated after reasoning is shaped by it; confidence-first avoids that ordering.

[^c1]: arxiv-2603-05881 — "interpreting this score as the model’s probability of answering the question correctly under its current policy."
[^c2]: arxiv-2603-05881 — "we align confidence targets to group-wise empirical success rates (GESR) observed during policy rollouts."
[^c3]: arxiv-2603-05881 — "Training on frozen correctness labels usually causes predictors to overfit to superficial patterns"
[^c4]: arxiv-2603-05881 — "This quadratic form amplifies penalties"
[^c5]: arxiv-2603-05881 — "computing separate advantages"
[^c6]: arxiv-2603-05881 — "the model may improve the confidence objective by altering answer behavior (e.g., refusal or evasiveness)."
[^c7]: arxiv-2603-05881 — "it reduces"
[^c8]: arxiv-2603-05881 — "cutting confidence-estimation token cost by >92% across all categories."
[^c9]: arxiv-2603-05881 — "sequential confidence training exhibits reward hacking, where"
[^c10]: arxiv-2603-05881 — "segmented rewards produce more generalizable confidence estimates, with lower ECE"
[^c11]: arxiv-2603-05881 — "AUROC values are broadly comparable"
[^c12]: arxiv-2603-05881 — "This does not fully"
[^c13]: arxiv-2512-14273 — "an identical reward (advantage) to every token in a sequence"
[^c14]: arxiv-2512-14273 — "NExT-GQA mIoU 35.3→36.9"
