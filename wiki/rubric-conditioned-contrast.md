---
description: "A rubric is scored by whether a policy writing under it produces answers that a judge prefers over answers written without it, so the rubric is rewarded for the answers it helps produce."
aliases: ["rubric-conditioned contrast", "RC contrast", "rubric utility by conditioned generation"]
sources: ["doi-10-48550-arxiv-2605-03871"]
---
# Rubric-conditioned contrast

A rubric can be judged by how it reads, or by what it does. The rubric-conditioned construction takes the second route. For a question q, the rubric generator writes a rubric r. The policy then writes two responses: a+ conditioned on both the question and the rubric, and a− conditioned on the question alone. The pair is labelled with a+ preferred, and the rubric generator is trained on whether the judge agrees. The paper calls this "direct signal about rubric utility": "This provides direct signal about rubric utility."[^r1] The reasoning given is that "responses are consistently better, the rubric contains actionable criteria."[^r2]

The consequence is that the rubric is rewarded for a causal effect. It is not enough for the criteria to be well formed or to look thorough; they have to change what the policy writes. In the paper's words, the generator "is thus incentivized to produce criteria that concretely improve response quality when" the rubric is provided to the policy.[^r3] The contrast therefore links a rubric to the answers written under it, which is the link an evaluation of answering needs and which a rubric judged on its own text does not test.

In the paper's ablation the source did not win on the policy. Rubric-conditioned pairs alone gave a RewardBench-2 score of 48.4 and a policy average of 68.6, against 46.0 and 69.3 for temporal pairs (my reading of the paper's Table 7). The source is reported as one of three that can be mixed, and no single one was the best for the downstream policy.

## Limits

- Answer leakage. A rubric that states the expected answer makes a+ better for reasons that have nothing to do with the rubric's quality. The paper reports that trained rubrics do embed expected values: in math, "the rubric concentrates 80% of the weight on a single criterion that embeds" the expected answer.[^r4] Under this contrast such a rubric would be rewarded, and the paper does not separate the two causes (my inference).
- The signal depends on the policy using the rubric. If the policy ignores the rubric text, a+ and a− differ only by sampling noise, and the contrast carries nothing (my inference).
- The construction was tested with one policy family and one training recipe. Whether the gain holds when the rubric is read by a human, not by a judge, is not tested.

## Related

- [[co-evolving-rubric-generator]] — its constructiveness term also scores a rubric by the policy's gain when it revises answers under the rubric, but against a human-written rubric rather than a contrast pair
- [[temporal-contrast-preference-pairs]] — the source that varies the policy over time instead of conditioning it on the rubric
- [[inferred-question-contrast]] — the source that varies the question instead of the rubric

[^r1]: doi-10-48550-arxiv-2605-03871 — "This provides direct signal about rubric utility"
[^r2]: doi-10-48550-arxiv-2605-03871 — "responses are consistently better, the rubric contains actionable criteria"
[^r3]: doi-10-48550-arxiv-2605-03871 — "is thus incentivized to produce criteria that concretely improve response quality when"
[^r4]: doi-10-48550-arxiv-2605-03871 — "the rubric concentrates 80% of the weight on a single criterion that embeds"
