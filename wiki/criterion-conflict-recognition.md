---
description: "A judge can give one response pair the same preference on every criterion and hide real conflicts between them; trade-off sensitivity and conflict matching rate measure whether it sees them."
aliases: ["criterion-level trade-off sensitivity", "criterion conflict matching rate", "criterion-agnostic judging", "pluralistic conflict recognition"]
sources: ["arxiv-2511-21662"]
---
# Criterion-level conflict recognition

Two criteria can disagree about the same pair of responses. One answer may be better on visual grounding and worse on conciseness, or better on logic and worse on hallucination. A single overall preference label erases that disagreement. A judge that answers one overall question can therefore look accurate while never registering that the criteria pull in opposite directions. The Multi-Crit benchmark makes the disagreement itself a thing to be measured. Its authors judge each criterion on its own and then ask whether the judge's criterion-level answers track the human answers, including where the humans split.[^c1]

Two quantities carry this. Trade-off sensitivity (TOS) is computed over the instances that contain at least one ground-truth conflict. An instance counts as sensitive when the judge assigns different preferences to some pair of conflicting criteria within it.[^c2] The paper reads a high TOS as a sign that the judge is "less criterion-agnostic or overconfident in assigning identical preferences across all criteria."[^c3] Conflict matching rate (CMR) is the stricter one. A conflicting criterion pair counts as matched only when the judge predicts both criteria in agreement with the human labels, so a judge must both detect the conflict and resolve it the way people do.[^c4] The paper describes CMR as "evaluating whether the judge not only detects but also resolves conflicts consistently with humans."[^c5]

The format of the question matters. When the criteria are asked about in one inference pass, the trade-off sensitivity of most models falls. The paper's explanation is that generating several criterion judgments in one pass "inevitably induces inter-criterion dependencies, making the judge model more likely to assign the same preference direction across criteria for the same pair of responses."[^c6] So the joint format pushes a judge toward the criterion-agnostic answer that the metric is built to catch. The effect is not uniform. GPT-4o drops on every metric under joint judging, while "GPT-5, in contrast, benefits from the joint setting."[^c7] The same joint format is therefore a different mechanism for different models, not one fixed cost.

A second finding bears on training. Reasoning fine-tuning "weakens models' ability to recognize trade-offs" in the paper's account, even where it helps on the reasoning split.[^c8] Judges fine-tuned on holistic, single-preference data improved visual grounding but "generalize poorly to pluralistic, criterion-driven evaluation." The transfer lost is the one this note is about: a holistic label cannot teach a judge that criteria can disagree.

## Limits

The benchmark has 425 prompts and 1,425 criterion-level human judgments, of which 315 prompts contain criterion-level conflicts, forming 782 conflicting criterion pairs.[^c9] The prompts were filtered to keep conflicts: "prompt-level filtering primarily retains pairs exhibiting criterion-level conflicts and balances the number of samples across all criteria."[^c10] So every instance in the TOS and CMR denominators contains a conflict by construction. The base rate at which real evaluations present conflicting criteria is not measured here.

A high TOS does not by itself show that a judge perceives trade-offs. The paper says TOS indicates "flexibility rather than absolute accuracy."[^c11] A judge that flips its answers at random would also score well on TOS. This is my inference from the definition, not a result the paper tests; CMR is the guard against it, because a random flip is unlikely to match the human resolution.

The labels come from nine annotators who each judged one criterion at a time, with pairwise agreement of "0.718 on open-ended generation tasks and 0.805 on verifiable reasoning tasks."[^c12] Where humans split, the gold preference is itself a judgment, and the conflict label inherits that noise. The joint-judgment comparison covers four proprietary models only, and the paper does not report it for open-source judges in the sections read.[^c13] Whether the same loss of conflict sensitivity holds for other criterion sets, or for judges that generate their own criteria, is not tested.

## Related

- all-criteria-instance-accuracy — the conjunctive score the same benchmark reports next to these two; it counts an instance correct only if every criterion is.
- [[llm-judge-validation-gap]] — the case for validating a judge per criterion; conflict recognition is a finer check that a per-criterion validation can still miss.
- [[suppressed-criteria]] — a scalar reward also collapses several criteria into one signal, at training time rather than at judging time.

[^c1]: arxiv-2511-21662 — "identify criterion-level trade-offs, and capture preference conflicts within response pairs"
[^c2]: arxiv-2511-21662 — "reflects whether the judge can perceive criterion-level tradeoffs within an instance"
[^c3]: arxiv-2511-21662 — "less criterion-agnostic or overconfident in assigning identical preferences across all criteria."
[^c4]: arxiv-2511-21662 — "A conflict is considered matched only if the model predicts both criteria in agreement with the ground truth preference"
[^c5]: arxiv-2511-21662 — "evaluating whether the judge not only detects but also resolves conflicts consistently with humans."
[^c6]: arxiv-2511-21662 — "more likely to assign the same preference direction"
[^c7]: arxiv-2511-21662 — "GPT-5, in contrast, benefits from the joint setting"
[^c8]: arxiv-2511-21662 — "weakens models’ ability to recognize trade-offs"
[^c9]: arxiv-2511-21662 — "including 315 prompts with criterion-level conflicts that together constitute 782 conflicting criterion pairs"
[^c10]: arxiv-2511-21662 — "primarily retains pairs exhibiting criterion-level conflicts and balances the number of samples across all criteria"
[^c11]: arxiv-2511-21662 — "indicating its flexibility rather than absolute accuracy"
[^c12]: arxiv-2511-21662 — "achieving 0.718 on open-ended generation tasks and 0.805 on verifiable reasoning tasks"
[^c13]: arxiv-2511-21662 — "proprietary LMMs—GPT-4o, GPT-5, o4-mini, and Gemini2.5-Pro—under the joint multi-criterion judgment setting"
