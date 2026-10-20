---
description: "Reported gains of a domain-fine-tuned LLM can come from instruction and output-format familiarity plus leakage; lift over a majority baseline and a no-domain-exposure control separate them."
aliases: ["imbalance riders", "lift over majority baseline", "instruction-tuning control for domain gains"]
sources: ["arxiv-2602-04031"]
---
# Format-familiarity confound in fine-tuned gains

A model fine-tuned on a domain (here serialized tables) and then scored on that domain's benchmark can look as if it learned the domain. Gorla and Puduppully (2026) re-evaluate Tabula-8B on 165 UniPredict datasets and show that three artifacts account for most of the apparent skill: class imbalance, instruction and output-format familiarity, and train-test leakage.

## Mechanism 1: raw accuracy hides imbalance

Computing the majority-class accuracy for every dataset and reporting lift over it exposes "imbalance riders": datasets where class imbalance inflates raw accuracy while lift stays negligible or negative.[^c1] On a stroke-prediction dataset the model reached 94.9% accuracy, which is near what always predicting the majority class gives.[^c2] Binary and categorical tasks have near-zero median lift (categorical about -0.3); the aggregate strength comes from quartile-bin tasks, with a median lift of 32.6 points.[^c3]

## Mechanism 2: a parallel control with no domain exposure

Tabula-8B and Alpaca are parallel fine-tunings of the same base Llama, so Alpaca (general instructions only) isolates what instruction-tuning contributes.[^c4] Alpaca exceeded the majority baseline on 39.5% of datasets (base Llama: 24.4%) and reached 92.2% of Tabula-8B's mean accuracy without ever seeing tabular data.[^c5] A further control, Alpaca+Q, adds only quartile-format examples and closes 71.3% of the gap on quartile tasks, so the advantage there mostly reflects familiarity with the output format.[^c6] The remaining 8.2 points concentrate on datasets at high contamination risk (a 17.9-point advantage on one risky stratum).[^c7]

The design generalizes as a decomposition: total gain = (base to instruction-tuned) + (format exposure) + (residual, then checked for leakage). Each term is measured by a control that differs from the target in one factor, with identical 4-shot prompts and greedy decoding.[^c8]

## What it changes for question and answer design

An accuracy number only answers "did the model learn the domain?" after the task's trivial solution (majority class), the model's generic instruction-following, and the label format have each been given a control. This is my reading of the paper's recommendation to report "performance relative to" baselines, not a quoted rule.

## Limits

- One model family (Llama-3-8B), one benchmark (UniPredict); transfer to other tabular models or other domains is untested.
- The authors say the mechanism by which instruction-tuning helps "remains unclear"; their account (comprehending task descriptions and mapping inputs to outputs) is a hypothesis.[^c9]
- The residual attributed to contamination is shown by stratification, not by a clean-data re-run; "likely" is the authors' word for the whole conclusion.
- Near-zero median lift shows no gain over majority class, not that no tabular structure was learned in cases with balanced difficulty.

## Related

- [[benchmark-contamination-convergent-audit]] — probes for the leakage term of this decomposition
- [[llm-judge-biases]] — another case where a score diverges from the capacity it claims to measure
- [[adversarial-unanswerable-questions]] — items built so that shortcuts fail

[^c1]: arxiv-2602-04031 — "accuracy while lift over baseline remains"
[^c2]: arxiv-2602-04031 — "achieves 94.9% accuracy, which appears impressive until"
[^c3]: arxiv-2602-04031 — "quartile classification achieves a median lift of 32.6 percent"
[^c4]: arxiv-2602-04031 — "are parallel fine-tunings from the same Base Llama (Section 3), this structure decomposes Tabula-8B’s performance"
[^c5]: arxiv-2602-04031 — "Llama’s 24.4%) and achieves 92.2% of Tabula-8B’s mean"
[^c6]: arxiv-2602-04031 — "closing 71.3% of the gap to Tabula. This demonstrates that"
[^c7]: arxiv-2602-04031 — "reveals that Tabula retains a 17.9 point advantage on stock/-"
[^c8]: arxiv-2602-04031 — "All models use greedy decoding and 4-shot"
[^c9]: arxiv-2602-04031 — "While the precise mechanism remains"
