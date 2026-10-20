---
description: "After clean post-training, SFT widens a contaminated model's lead only on the leaked benchmark while GRPO also widens it on an uncontaminated counterpart."
aliases: ["contamination transfer to uncontaminated counterparts", "SFT versus GRPO contamination gap", "over-estimation versus generalization under post-training"]
sources: ["arxiv-2601-06103"]
---
# Post-training recipe decides whether leaked gains transfer

Measuring a contaminated model's gain on the leaked benchmark alone cannot separate two things: a model that memorized the test items, and a model that became better at the underlying task. The paper's device is a counterpart. For each leaked benchmark there is an uncontaminated benchmark meant to measure the same ability: GSMPlus for GSM8K, and HumanEval for MBPP. The counterpart exists to answer one question: "These datasets basically help us answer how much of the improvement is actually over-estimation."[^c1]

The measure is the contamination gap, the contaminated model's advantage over the clean model, taken on the leaked benchmark and again on its counterpart. If the counterpart gap stays flat, the leaked-benchmark gain is over-estimation. If it rises, some of the gain is a capability that the leak helped teach.

The two recipes come apart here. After SFT the leaked-benchmark gap is larger, and the counterpart does not move: "the impact of contamination on an external benchmark remains constant."[^c2] After GRPO the points move diagonally, and the gap "grow[s] for both the contaminated and the uncontaminated models."[^c3] The authors read this as "generalizable improvements from the contamination that is included in the pre-training."[^c4] The abstract states the split directly: "SFT inflates scores only on the contaminated tasks, whereas GRPO also" does so on "uncontaminated counterparts (GSMPlus, HumanEval)."[^c5] At the base checkpoint the two benchmarks behave alike, "the Base models behave roughly the same on the contaminated and uncontaminated datasets."[^c6]

The result also depends on scale, in opposite directions for the two recipes. For the base and SFT models, "the contamination-gap difference increases as model scale increases," which the authors read as more over-estimation with size.[^c7] For GRPO, "the contamination-gap difference is smaller" as the model grows, and it can turn negative.[^c8] The paper's own account of why GRPO transfers is a suspicion, not a test: "We suspect that this is a combination of higher quality data" and the fact that the evaluation prompt matches the inserted contamination.[^c9] The same split fits the older claim that "SFT is more prone to causing memorization" than RL.[^c10] That claim is about memorization in general; this paper's counterpart test is a narrower way to check it under contamination (my inference on the mapping).

## Limits

- The counterpart is not a clean control. GSMPlus is built from GSM8K by adversarial edits, so it shares source and domain with the leaked test set. Any overlap or shared structure could carry leakage into it. The paper calls it uncontaminated and does not test that (my inference). HumanEval and MBPP differ in difficulty: "While the levels of difficulty are not directly comparable."[^c11]
- The comparison is relative. "Here we are looking at the relative advantage the contaminated model" has over the clean one, "and not absolute performance."[^c12]
- The RL arm is one setting: "our RL setting uses synthetic rule-based rewards," and human-annotated preference signals "might have different effects."[^c13]
- The scale trend rests on Qwen2.5 and Gemma3 at 0.5B to 4B. The authors say "the analysis is still very local and there are potentially mixed signals."[^c14]
- The fine-tuning was on clean post-training data, with one run per cell. The counterpart gap is a difference of small accuracy gaps, and its error bars cover evaluation noise only.

## Related

- [[dormant-contamination-resurfacing]] — the same experiment's timing claim: the gap is hidden after pre-training and revealed by post-training; this note asks which recipe lets the revealed gain carry over
- [[post-rl-sft-calibration-restoration]] — another account of how RL and SFT differ, in confidence calibration rather than in recall of leaked items
- [[evidence-degradation-test-for-memorization]] — another way to separate recall from reasoning, which the counterpart test here also tries to do

[^c1]: arxiv-2601-06103 — "basically help us answer how much of the improvement is actually over-estimation."
[^c2]: arxiv-2601-06103 — "the impact of contamination on an external benchmark remains constant."
[^c3]: arxiv-2601-06103 — "grow for both the contaminated and the uncontaminated models."
[^c4]: arxiv-2601-06103 — "generalizable improvements from the contamination that is included in the pre-training."
[^c5]: arxiv-2601-06103 — "inflates performance on uncontaminated counterparts (GSMPlus, HumanEval)."
[^c6]: arxiv-2601-06103 — "the Base models behave roughly the same on the contaminated and uncontaminated datasets"
[^c7]: arxiv-2601-06103 — "the contamination-gap difference increases as model scale increases,"
[^c8]: arxiv-2601-06103 — "the contamination-gap difference is smaller"
[^c9]: arxiv-2601-06103 — "We suspect that this is a combination of higher quality data"
[^c10]: arxiv-2601-06103 — "Previous work suggests that SFT is more prone to causing memorization"
[^c11]: arxiv-2601-06103 — "While the levels of difficulty are not directly comparable"
[^c12]: arxiv-2601-06103 — "here we are looking at the relative advantage the contaminated model"
[^c13]: arxiv-2601-06103 — "our RL setting uses synthetic rule-based rewards"
[^c14]: arxiv-2601-06103 — "very local and there are potentially mixed signals"
