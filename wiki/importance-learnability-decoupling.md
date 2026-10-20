---
description: "Human-assigned rubric weight and a criterion's usefulness as a group-relative training signal come apart: saturated or unreachable criteria can carry high weight and teach nothing."
aliases: ["static rubric weighting", "rubric weight conflation", "training pressure allocation", "weight versus learnability"]
sources: ["doi-10-48550-arxiv-2605-20164"]
---
# Importance-learnability decoupling

A rubric grades a response against several prompt-specific criteria, each with a human weight, and the standard reward in prior work is the static weighted sum of the weights of the criteria a judge marks as passed.[^c1] The weight is meant to say how much a criterion matters in the final answer. Once the sum is used as a training reward, the same number also decides how strongly the criterion pushes the policy, and those two roles can come apart.

The mechanism sits in group-relative RL. The advantage of a rollout is its reward standardized within the group of rollouts for one prompt. A criterion that every rollout passes, or that no rollout passes, "adds the same constant to every reward and cancels out of the advantage; only" criteria whose pass rate lies between the extremes can teach the current policy.[^c2] The zero-variance logic that makes a fully agreed group contribute no gradient ([[zero-variance-group-waste]]) applies to each criterion here. The new point is what the weight does on top of it: "can therefore be important for evaluation while still producing no gradient signal right now."[^c3] A high weight says nothing about whether the criterion currently varies across rollouts.

The paper measures how often this happens. On 1,300 prompts from its multimodal set and HealthBench English, sampled from two frozen base policies, every criterion was judged on every rollout. For a fresh policy, "are non-contrastive for a fresh policy: 17–26% are saturated and 20–33% are dead, leaving only the" remaining criteria able to produce a contrastive gradient.[^c4] The static sum therefore sends "within-category training pressure to criteria that cannot move the policy, and the problem is not confined" to low-weight criteria.[^c5] The authors report that "human weight and rollout variance are essentially uncorrelated," and that "half of the highest-weight criteria already carry" zero variance.[^c6] "These shares change by only a few points across" the four model and dataset combinations, so the authors read the pattern as a property of static aggregation, not of one policy or domain.[^c7]

The distinction the paper draws is between two objects. The weight is a prior about the end state. Learnability is a property of the policy at a given point in training, measured on the current rollout group. The static sum assumes they are the same: one human-assigned weight is taken to express both "desired importance in the final answer and its current usefulness as a training signal. The two are not" the same thing.[^c8] The paper's own answer keeps the human weights as the stated target and lets the training signal be reallocated; this note takes only the separation, not that practice.

What transfers beyond RL is the separation itself. An evaluation criterion that every answer meets, or that none meets, does not distinguish answers, whatever its weight in a score. My inference: for anyone building a rubric to judge answers, a criterion's weight and its power to separate candidate answers are two quantities, and a rubric can be dominated by high-weight criteria that separate nothing. The paper does not test this in a non-RL evaluation.

## Limits

- The measurements are a snapshot of frozen base policies before training. The paper's claim about training dynamics rests on reward spread and step counts from separate runs, not on the same table.
- The multimodal dataset is the authors' own, drawn from a contributor-authored prompt pool, and every verdict comes from an LLM judge scoring binary criteria. Dead and saturated shares therefore depend on the judge's verdicts. A judge that is noisy on a criterion would also produce variance; the paper's shares do not separate judge noise from real contrast (my inference).
- The held-out evaluation on the multimodal set scores the static weighted sum: "For MM the rubric reward is the static weighted aggregation." [^c9] So the target the weights define is the one used to judge any reallocation of them, which the paper does not treat as a neutral check.
- Results are wins on 24 of 30 base-policy and metric comparisons against the authors' own baselines. I did not read the run-to-run variance behind those cells, and the claim of reaching the same plateau in 2.5 to 4 times fewer steps comes from the same runs.
- Nothing here shows that the decoupling matters for answer quality outside group-relative training, for static evaluations, or for human graders.

## Related

- [[zero-variance-group-waste]] — the zero-advantage event that makes a criterion with no within-group variance contribute nothing; this note adds what the weight does on top of that
- [[rubric-difficulty-evolution]] — keeps criteria informative by regenerating them against each group's rollouts, a different route to the same zero-signal problem
- [[recursive-rubric-decomposition]] — the same concern at rubric-writing time: a rubric satisfied by many responses is too broad to discriminate
- [[multi-objective-advantage-aggregation]] — another aggregation step before the advantage, which also decides what a multi-part reward teaches

[^c1]: doi-10-48550-arxiv-2605-20164 — "reward used in prior work is the static weighted sum"
[^c2]: doi-10-48550-arxiv-2605-20164 — "adds the same constant to every reward and cancels out of the advantage; only"
[^c3]: doi-10-48550-arxiv-2605-20164 — "can therefore be important for evaluation while still producing no gradient signal right now."
[^c4]: doi-10-48550-arxiv-2605-20164 — "are non-contrastive for a fresh policy: 17–26% are saturated and 20–33% are dead, leaving only the"
[^c5]: doi-10-48550-arxiv-2605-20164 — "within-category training pressure to criteria that cannot move the policy, and the problem is not confined"
[^c6]: doi-10-48550-arxiv-2605-20164 — "human weight and rollout variance are essentially uncorrelated"
[^c7]: doi-10-48550-arxiv-2605-20164 — "These shares change by only a few points across"
[^c8]: doi-10-48550-arxiv-2605-20164 — "desired importance in the final answer and its current usefulness as a training signal. The two are not"
[^c9]: doi-10-48550-arxiv-2605-20164 — "For MM the rubric reward is the static weighted aggregation"
