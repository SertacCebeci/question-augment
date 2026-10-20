---
description: "Scaling a model's stated confidence by its self-measured inconsistency cuts ECE by compressing overconfidence but does not improve ranking; ensemble fusion supplies the discrimination."
aliases: ["Two-Phase Verification confidence", "S-score", "consistency-derived confidence", "calibration-discrimination dissociation"]
sources: ["arxiv-2603-24481"]
---
# Inconsistency-penalized confidence

A label-free way to repair an overconfident model. The model answers with a stated confidence C. It then extracts four factual claims from its own reasoning and answers each claim twice, once without and once with its reasoning in context. The fraction I of claim pairs whose two answers disagree (token-overlap threshold 0.4) is the inconsistency. The reported score is S = C · (1 − I). The paper's own wording: "This multiplicative formula penalizes initial confidence proportionally to measured inconsistency".[^c1]

## What it does to calibration

Unverified Qwen2.5-7B specialists on high-disagreement medical multiple-choice questions were far overconfident. Their confidence distributions were "heavily right-skewed confidence distributions with" means near 0.90, against "actual accuracy of 43–57%".[^c2] Applying the penalty to a single agent cut ECE by 51%, 50%, 31% and 42% across four settings, with no change in accuracy.[^c3] The mechanism is compression: "Two-Phase Verification improves calibration by compressing all confidence scores toward" the model's actual accuracy level.[^c4] It needs no calibration labels, so it works where temperature scaling cannot be fitted.

## What it does not do: discrimination

Calibration (ECE) asks whether confidence matches average accuracy. Discrimination (AUROC) asks whether confidence ranks correct above wrong. The penalty moved the first and not the second: "Two-Phase Verification alone (C2) produces negative AUROC change on three of four datasets".[^c5] The paper's explanation is that inconsistency is a weak proxy for error: "A specialist that produces a self-consistent but wrong answer still receives a high S-score".[^c6] Consistency tracks stability, not truth, so the score shrinks uniformly without reordering.

## Where discrimination came from

Four specialist prompts (respiratory, cardiology, neurology, gastroenterology) answered independently. Their votes were fused as vote count times mean S-score. This ensemble supplied the AUROC gain: on MedQA-250, multi-agent fusion alone gave +0.013 AUROC and +2.8 pp accuracy with only a 5.4% ECE cut. Verification added to the ensemble cut ECE by 72.9%. The full system reached ECE 0.091 (a 74.4% cut) and AUROC 0.630 (+0.056) at 59.2% accuracy.[^c7] The authors' account is that a correct answer is more likely to draw self-consistent reasoning from diverse agents, not that verification detects correctness directly. This is a reading, not a tested mechanism.

The two components therefore address different failure modes: verification fixes the level of confidence, and the ensemble fixes its order. The same split appears elsewhere in the wiki: self-verification can raise AUROC while worsening ECE in [[same-model-self-verification-conditional-confidence]].

## Limits

- Evaluation is on subsets filtered to questions where the four specialists initially disagreed, and the authors say the results "should not be extrapolated" to full benchmarks.[^c8]
- One 7B model, 100 and 250 questions per set, 5 ECE bins. The 100-question ECE estimates are noisy by the paper's own caveat. No statistical tests were run.
- Config 1 is a single respiratory specialist. No sampled self-consistency baseline was compared, and post-hoc methods were excluded for lack of labels.
- On MedMCQA the multi-agent fusion without verification (Config 3) had the best accuracy, and verification did not help recall-bound questions. The ECE gain there does not imply that answers improved.
- Whether the confidence is good enough to trigger clinical deferral was not tested. The decomposition "may generalize" is the authors' conjecture.
- The Jaccard consistency check is crude, and the multiplicative form was chosen over alternatives in unreported preliminary runs.

## Related

- [[calibration]] — the property ECE measures; here it is separable from ranking.
- [[score-separability]] — the ranking property that abstention needs, which this penalty alone does not supply.
- [[same-model-self-verification-conditional-confidence]] — another same-model check where ranking and calibration diverge.
- [[roc-curve]] — the AUROC metric used for discrimination.
- [[role-differentiated-parallel-elicitation]] — role-prompted parallel agents, the ensemble side of this design.

[^c1]: arxiv-2603-24481 — "This multiplicative formula penalizes initial confidence proportionally to measured inconsistency"
[^c2]: arxiv-2603-24481 — "The unverified configurations (C1, C3) produce heavily right-skewed confidence distributions with"
[^c3]: arxiv-2603-24481 — "ECE drops by 51% on MedQA-100, 50% on MedQA-250, 31%"
[^c4]: arxiv-2603-24481 — "Two-Phase Verification improves calibration by compressing all confidence scores toward"
[^c5]: arxiv-2603-24481 — "Two-Phase Verification alone (C2) produces negative AUROC change on three of four datasets"
[^c6]: arxiv-2603-24481 — "A specialist that produces a self-consistent but wrong answer still receives a high S-score"
[^c7]: arxiv-2603-24481 — "system achieves ECE = 0.091 (74.4% reduction over the single-specialist baseline)"
[^c8]: arxiv-2603-24481 — "should not be extrapolated to the"
