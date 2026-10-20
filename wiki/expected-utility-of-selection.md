---
description: "Expected Utility of Selection scores a choice set by the expected utility of the option the user picks from it; greedy building has a (1-1/e) guarantee when answers are noiseless."
aliases: ["EUS", "expected utility of a choice set"]
sources: ["doi-10-48550-arxiv-2205-13743"]
---
# Expected utility of selection

A system that asks a user to pick one item from a small set has to decide which set to show. Expected Utility of Selection (EUS) scores the whole set, not its members. Under a posterior over the user's preference weights $w$, it is the expectation of the utility of the element the user would most prefer in the set: "under the uncertainty over w, of the utility of its most preferred element".[^e1] Here utility is minus cost; that is this note's reading of the paper's expected utility of an intervention, not a quoted formula. A response model gives the probability that a user with weights $w$ picks an item from the set, and the set's score weights each item's utility by that probability.[^e2] Under the noiseless response model, "the user always prefers the" cheapest option.[^e3]

The paper calls EUS closely related to the value of information, not identical to it: "Expected Value of Information (EVOI), and frequently used in Bayesian PE".[^e4] My reading of the difference is this: [[value-of-information]] scores a question by how much it changes the best action after the answer, while EUS is a single expectation over a set of options before any answer arrives. The two share the expected-utility rule of [[expected-utility]]; that the EUS of a set equals a value of information is not something the paper proves.

## How it is used

The set is chosen to maximise the expected posterior utility, "thus reducing as much as possible the regret one step ahead".[^e5] This is a one-step, myopic choice. The sequential value of a whole questioning plan is, the paper says, "which may be more efficient but intractable in general".[^e6]

Choosing the best set is hard: "Finding a choice set O maximizing the EUS is intractable in general".[^e7] The procedure therefore fixes the posterior mean of the weights, generates candidate interventions with a planner under that mean, and adds one candidate at a time, each the one that most raises the set's score.[^e8] The experiments use a logistic response model, in which "we implement a logistic response model".[^e9] The paper states that "the EUS becomes submodular and monotonic" under some response models, and the noiseless one is the case it covers; for the logistic model it gives no such guarantee.[^e10] For the noiseless score, "greedy optimization is sufficient to find a choice set O that achieves high" value, with a classical approximation guarantee of (1 − e⁻¹) against the best set.[^e11]

For the logistic model the paper does not optimise the score directly. It optimises the noiseless score greedily, relying on the gap between the two scores being "always smaller than a problem independent (tight) bound",[^e12] and so "we can compute a high-quality choice set by greedily maximizing" the noiseless score.[^e13] So the greedy set under noisy answers is justified by a bound on the gap, not by its own guarantee.

In simulation with set sizes 2 and 4, "After a few questions, PEAR reaches a low regret in all settings".[^e14] The paper also reports the trade-off that a larger set means "regret, irrespective of the response model, with the downside of increasing the cognitive burden for the user".[^e15]

## What survives the transfer

The principle carries over: a question is worth the expected quality of the best answer it can lead to, averaged over what the answerer might want, and a set of options is scored as a whole rather than item by item. What does not carry over is the identity of utility with negative cost, which is specific to recourse, where the cost is "linear, enabling PEAR" to use known elicitation algorithms.[^e16] In a setting without a cost model, the utility must be elicited too, and the score has nothing to be minus.

## Limits

- The results are simulated. Regret is measured against a ground truth that is itself estimated: "Here the ground-truth intervention I GT (which is unknown) is approximated" by running the method with the correct costs.[^e17] No real person picked from these sets in the paper.
- The method is myopic. The paper names the sequential version as an open theoretical challenge, not something it solves.
- The greedy guarantee is proved for noiseless answers only; for the noisy model used in the experiments, the set is justified by a bound on the gap.
- The score is only as good as the cost model. Because EUS is an expectation of the negative cost, a misspecified cost gives a set optimised for the wrong utility. This note did not check the paper's robustness table for corrupted cost graphs.
- The posterior expectation is approximated by Monte Carlo sampling.[^e18]
- Set size is not in the objective. The score never charges for the extra burden of a bigger set, so the size k is set by hand (2 and 4 were tested).
- The set can contain only candidates the planner produced under the posterior mean; an item it never generated cannot be offered.
- The paper's framing of choice queries is that the user "has to select a preferred item from a small set of alternatives";[^e19] EUS itself does not model how the burden grows with set size.

## Related

- [[expected-utility]] — the decision rule EUS applies to a set of options; the source of "expected" here.
- [[value-of-information]] — the paper's EVOI relative; the two score a question differently, as described above.
- [[expected-information-gain]] — the other common criterion for choosing a question from a posterior, which needs no utility at all.
- [[adaptive-submodularity]] — the property that makes greedy selection of questions carry a guarantee, and the setting where the noiseless case sits.
- [[multi-choice-preference-query]] — the same set-size trade-off (more options, more burden) measured in another preference-query setting.
- [[bayesian-experimental-design]] — the wider framework in which choosing informative questions from a posterior is posed.

[^e1]: doi-10-48550-arxiv-2205-13743 — "under the uncertainty over w, of the utility of its most preferred element"
[^e2]: doi-10-48550-arxiv-2205-13743 — "is the probability that a user with weights w picks I from O"
[^e3]: doi-10-48550-arxiv-2205-13743 — "according to which the user always prefers the"
[^e4]: doi-10-48550-arxiv-2205-13743 — "Expected Value of Information (EVOI), and frequently used in Bayesian PE"
[^e5]: doi-10-48550-arxiv-2205-13743 — "thus reducing as much as possible the regret one step ahead"
[^e6]: doi-10-48550-arxiv-2205-13743 — "which may be more efficient but intractable in general"
[^e7]: doi-10-48550-arxiv-2205-13743 — "Finding a choice set O maximizing the EUS is intractable in general"
[^e8]: doi-10-48550-arxiv-2205-13743 — "Generate the candidate interventions I with W-FARE using A and w̄"
[^e9]: doi-10-48550-arxiv-2205-13743 — "in PEAR we implement a logistic response model"
[^e10]: doi-10-48550-arxiv-2205-13743 — "the EUS becomes submodular and monotonic"
[^e11]: doi-10-48550-arxiv-2205-13743 — "greedy optimization is sufficient to find a choice set O that achieves high"
[^e12]: doi-10-48550-arxiv-2205-13743 — "always smaller than a problem independent (tight) bound"
[^e13]: doi-10-48550-arxiv-2205-13743 — "we can compute a high-quality choice set by greedily maximizing"
[^e14]: doi-10-48550-arxiv-2205-13743 — "After a few questions, PEAR reaches a low regret in all settings"
[^e15]: doi-10-48550-arxiv-2205-13743 — "regret, irrespective of the response model, with the downside of increasing the cognitive burden for the user"
[^e16]: doi-10-48550-arxiv-2205-13743 — "the cost function is linear, enabling PEAR"
[^e17]: doi-10-48550-arxiv-2205-13743 — "Here the ground-truth intervention I GT (which is unknown) is approximated"
[^e18]: doi-10-48550-arxiv-2205-13743 — "an efficient Monte Carlo approximation"
[^e19]: doi-10-48550-arxiv-2205-13743 — "user has to select a preferred item from a small set of alternatives"
