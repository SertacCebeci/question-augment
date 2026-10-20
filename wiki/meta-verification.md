---
description: "A second check on a verifier's analysis: each issue it raises must exist and justify its score; rewarding that check raised analysis quality from 0.85 to 0.96 on validation."
aliases: ["meta-verifier", "verification of verification", "review of verifier analyses", "meta-verification reward"]
sources: ["arxiv-2511-22570"]
---
# Meta-verification

A verifier reads a proof and writes an analysis: a list of issues and a score. A meta-verifier does not judge the proof. It reads the analysis and asks whether the issues named there exist, and whether they logically justify the score under the same rubric. The paper's definition is that meta-verification is "a secondary evaluation process that assesses whether issues identified by the verifier indeed exist and whether these issues".[^m1]

The paper introduces it for one failure. A verifier trained only to match expert scores can be rewarded in full for a flawed proof when it gets the score right, even if the reasons it gives are invented. In the authors' words, "the verifier can receive full reward by predicting the correct scores while" hallucinating issues that are not there.[^m2] A score-only reward cannot see the reasons, so the reasons need their own check.

The mechanism is trained, not prompted. Experts first score the quality of verifier responses: "Mathematical experts scored the quality of verifier responses according to" the meta-verification rubric.[^m3] A meta-verifier is then trained on those scores with RL, using the same format and score reward structure as the verifier. "We trained a dedicated meta-verifier using RL to perform this evaluation."[^m4] The meta-verifier's judgement is folded into the verifier's reward, so an analysis with invented issues loses reward even when its score is right. On my reading of the paper's Eq. 3, the verifier's reward is a product of a format term, a score term and the meta term, which makes the meta-check a gate rather than a bonus. The resulting model does both jobs: "The resulting model can perform both proof verification and meta-verification tasks."[^m5]

The measured effect is on the paper's own meta-score. On a validation split of the verifier's training data, "improved from 0.85 to 0.96, while maintaining the same accuracy" in predicting proof scores.[^m6] The conclusion credits the method with "using meta-verification to largely reduce hallucinated issues."[^m7] The check is also reused as a filter in data generation. The authors note that "Meta-verification is also more sample-efficient for LLMs" to master than finding issues from scratch, which is why it can decide which verifier analyses count when proofs are auto-labelled; see [[scaled-verification-labeling]].[^m8]

The same check is applied to a generator's self-analysis in [[faithful-self-assessment-reward]], where the self-analysis is scored for accuracy before it earns reward.

## Limits

- The 0.85 to 0.96 figure is the meta-verifier's own score of analyses. The text read reports no independent test that the meta-verifier's judgements of issues are correct. The measure and the judge come from the same family of model, which is the setting the check is meant to audit.
- The gain is reported on a validation split of the verifier's own training distribution. The text does not test on held-out problem sources or on proofs from a different generator.
- The check audits the analysis, not the proof. An analysis whose issues are all real can still miss a flaw, and an analysis that cites a real issue can still give the wrong score. My inference: the meta-check narrows hallucination, not omission.
- The text read reports no ablation with the meta term removed, beyond the before-and-after on the validation split. How much of the final model's accuracy depends on it is not measured.
- Whether the same gate works in domains without a rubric, where "justify the score" has no fixed meaning, is not tested.

## Related

- [[hallucination-barrier]] — a model that checks its own output shares its noise with the generator; here the meta-verifier is a separately trained model, though the text does not test whether that separation removes the shared noise
- [[critique-consistency-reward]] — a step critique is rewarded when its verdict matches the answer; a meta-verifier rewards an analysis for whether its issues are real
- [[verifier-exploitation-rate]] — reward hacking measured on a rubric; the invented-issue failure is one way a score-only verifier reward can be exploited
- [[step-level-consensus-labels]] — majority vote over independent verifier runs as labels; the meta-check here filters runs before any vote
- [[generation-verification-gap]] — the premise that makes checking a check worth training

[^m1]: arxiv-2511-22570 — "that assesses whether issues identified by the verifier indeed exist and whether these issues"
[^m2]: arxiv-2511-22570 — "the verifier can receive full reward by predicting the correct scores while"
[^m3]: arxiv-2511-22570 — "Mathematical experts scored the quality of verifier responses according to"
[^m4]: arxiv-2511-22570 — "We trained a dedicated meta-verifier using RL to perform this evaluation."
[^m5]: arxiv-2511-22570 — "The resulting model can perform both proof verification and meta-verification tasks."
[^m6]: arxiv-2511-22570 — "improved from 0.85 to 0.96, while maintaining the same accuracy"
[^m7]: arxiv-2511-22570 — "using meta-verification to largely reduce hallucinated issues"
[^m8]: arxiv-2511-22570 — "Meta-verification is also more sample-efficient for LLMs"
