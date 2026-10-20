---
description: "Best-of-N that picks the candidate with the highest lower confidence bound on its learned reward, not the highest point estimate, so poorly measured candidates are penalised."
aliases: ["pessimistic best-of-N", "pBoN", "lower-confidence-bound best-of-N", "pessimistic selection under reward uncertainty"]
sources: ["arxiv-2512-03208"]
---
# Pessimistic lower-bound selection

Best-of-N (BoN) generates N candidate answers for a prompt and returns the one with the largest estimated reward. The point estimate treats every candidate as measured equally well, and it is not. The paper's starting point is that "Traditional BoN strategies use point estimates of rewards without accounting for uncertainty."[^p1] Two candidates with the same estimate can rest on very different amounts of support in the data, and the plain argmax cannot tell them apart.

The mechanism replaces each estimate by its lower confidence bound. The paper's bound comes from an asymptotic normal approximation: the estimate minus a normal quantile times an estimated standard deviation, where the standard deviation is the square root of the feature vector's quadratic form in the plug-in inverse information, divided by the sample size (my reading of the interval in eq. 8).[^p2] The selected answer maximises that bound. A candidate whose features lie in poorly covered regions gets a wide interval, so its lower bound falls; a candidate the data supports keeps most of its estimate. The penalty comes from the reward's own uncertainty, not from the number of candidates or from disagreement between judges.

The borrowing is from offline reinforcement learning, where the same idea handles limited coverage: "Pessimistic policies are often used to mitigate this issue." The paper modifies the BoN objective the same way, to "maximize the lower confidence bound of the reward rather than its point estimate."[^p3] Pessimism is therefore a shrinkage rule: choose the candidate whose worst plausible reward, at the chosen level, is highest.

What the paper reports: "the expected suboptimality of the pessimistic BoN policy" decreases at rate $1/\sqrt{n}$ in the reward-model sample size, with suboptimality measured against an oracle policy.[^p4] Its experiments say that "we empirically demonstrate the pessimistic BoN policy in (3) can improve" the standard approach across several BoN settings.[^p5]

## Limits

- The $1/\sqrt{n}$ rate concerns the sample size used to fit the reward model. What I read does not say how the guarantee depends on $N$, the number of candidates, and the result is asymptotic (my reading).
- The interval is a normal plug-in from the inverse information matrix. It inherits the assumptions of the linear reward model with bounded features, and it depends on the rationality model being right, since the scale's uncertainty widens it (see [[annotator-rationality-scale]]).
- The bound is applied to each candidate separately. The part read discusses no multiplicity correction for comparing N intervals at once, so the selected maximum may still be optimistic (my inference).
- The level $\alpha$ is a free choice. The part read does not say how to set it against the cost of choosing a worse answer.
- The empirical gains are cited from the paper's summary; the experiments section was not read in this pass.
- Pessimism here bounds the estimator's uncertainty. Pessimism over judges by taking a minimum is a different object, covered in [[pessimistic-min-judge-aggregation]].

## Related

- [[annotator-rationality-scale]] — supplies the variance this bound uses; a rater model with a scale near zero widens the interval.
- [[upper-confidence-bound-index]] — the optimistic mirror: a bandit adds an exploration bonus to the estimate, where this subtracts an uncertainty penalty.
- [[pessimistic-min-judge-aggregation]] — pessimism across judges through a minimum; here pessimism across an estimator's own uncertainty through a bound. The principle is shared, the object is not.
- [[optimistic-pessimistic-strategy]] — pessimistic states used to choose queries in preference elicitation, a separate use of the same idea.
- [[logic-only-reranking-drift]] — selection on a point score that degrades as N grows. Whether a lower bound would help there is my inference and is untested in either note.

[^p1]: arxiv-2512-03208 — "Traditional BoN strategies use point estimates of rewards without accounting for uncertainty."
[^p2]: arxiv-2512-03208 — "pessimistic BoN (pBoN) policy that maximizes the lower bound of the reward is"
[^p3]: arxiv-2512-03208 — "confidence bound of the reward rather than its point estimate."
[^p4]: arxiv-2512-03208 — "the expected suboptimality of the pessimistic BoN policy"
[^p5]: arxiv-2512-03208 — "we empirically demonstrate the pessimistic BoN policy in (3) can improve"
