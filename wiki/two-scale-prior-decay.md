---
description: "Keep a Beta posterior per training item and decay it at two rates: fast when the item is trained on, slow when it is skipped, so stale difficulty estimates fade without freezing unused items."
aliases: ["two-scale prior decay", "selection-conditioned forgetting"]
sources: ["arxiv-2511-18902"]
---
# Two-scale prior decay

A training item's difficulty can be tracked online as a Beta posterior over its probability of success under the current policy. Each rollout outcome adds to the counts: α gets the correct answers and β the incorrect ones. Adding counts forever lets old evidence win. The paper states the failure directly: "the historical data would eventually overwhelm the new evidence, leading to outdated estimates."[^c1]

The fix in VADE is to decay the counts before each update, but at two rates that depend on what happened to the item in that step. If the item is in the batch, with G rollouts and r correct, both counts are multiplied by a fast factor λ1 and then receive the new outcomes: α ← λ1·α + r and β ← λ1·β + (G − r). The reason given is that "When a sample is used for training, its response distribution shifts significantly, diminishing the value of past rollouts."[^c2] If the item is not in the batch, both counts are multiplied by a slower factor λ2 and nothing is added. The reason given is that "even unused samples are affected by generalization from trained data,"[^c3] so their old estimates go stale too, but more slowly. The paper frames the pair as covering "significant distribution shift when data is directly used for training" and "gradual generalization effects when data is not selected."[^c4]

The posterior is read by a sampler, not by a threshold. A value p̃ is drawn from each item's Beta posterior, the item's information score is computed at p̃, and the top items fill the batch. The posterior draw is what keeps uncertain items in play: the random sampling "gives those uncertain yet potentially valuable samples a chance of being selected."[^c5] This is the sampling rule of [[thompson-sampling]], applied to batch selection in training rather than to a single decision.

Two consequences follow from the update equations, and both are my reading rather than the paper's claims. First, an item that is never trained on has both counts shrink geometrically toward zero, so its posterior reverts to the uniform prior Beta(1, 1), and its uncertainty grows again. The rule therefore re-opens items that were dropped, which is the exploration side of the design. Second, a trained item keeps only a small effective count, since the fast factor discards most of its past, so its posterior stays wide. Both effects compare with the uniform discount in [[forgetting-factor-beta-bernoulli]], which applies one factor to every observation and gives every item a variance floor of the same kind. The two-scale version makes the floor depend on whether the item was used.

The decay is a response to non-stationarity, not a separate estimator. The static Beta update is exact only "under a stationary environment,"[^c6] and the two-scale rule is the paper's way of leaving that assumption. The same departure appears in [[learnability-posterior-curriculum]], which uses a sliding window over the last few observations instead of a geometric discount.

## Limits

- The two decay rates are inputs. The algorithm block takes them as parameters, and the method section I read gives no rule for choosing them.[^c7] Whether the gain depends on their values is not shown in the part I read.
- The paper reports one ablation number for the whole sampler-and-decay package. In the snippet I saw, the sentence "The performance gain of 1.65% demonstrates" follows a claim about tracking difficulty under non-stationarity, and I read that as the decay's effect.[^c8] I did not check the surrounding table, so the attribution is my reading.
- The case for the two rates is verbal: a used item's distribution shifts, an idle item drifts through generalization. Neither is measured in the text I read, and the paper does not separate the two decays in an experiment I saw.
- Equation 6 has no new evidence in it, so an item left alone for many steps returns to the uniform prior. Whether that reversion is wanted or an artifact is not discussed in the sections I read.
- The method runs on GRPO and GSPO with multimodal reasoning data. Nothing here tests the rule on other reward types or on text-only training.
- I did not find a regret or convergence bound for the decayed posterior in the sections I read. The stationary Thompson guarantees therefore do not transfer to this rule by the paper's own account.

## Related

- [[forgetting-factor-beta-bernoulli]] — one geometric discount applied at every observation; the two-scale rule makes the discount depend on whether the item was used
- [[learnability-posterior-curriculum]] — the other way to forget, a sliding window of the last µ observations per node
- [[thompson-sampling]] — the posterior-sampling rule that picks the batch from these per-item posteriors
- [[zero-variance-group-waste]] — why the item's success probability, and hence the posterior over it, decides whether a rollout group carries any gradient

[^c1]: arxiv-2511-18902 — "the historical data would eventually overwhelm the new evidence, leading to outdated estimates"
[^c2]: arxiv-2511-18902 — "When a sample is used for training, its response distribution shifts significantly, diminishing the value of past rollouts"
[^c3]: arxiv-2511-18902 — "even unused samples are affected by generalization from trained data"
[^c4]: arxiv-2511-18902 — "gradual generalization effects when data is not selected"
[^c5]: arxiv-2511-18902 — "gives those uncertain yet potentially valuable samples a chance of being selected"
[^c6]: arxiv-2511-18902 — "under a stationary environment"
[^c7]: arxiv-2511-18902 — "Require: Dataset D, batch size B, rollouts per sample G, decay rates"
[^c8]: arxiv-2511-18902 — "The performance gain of 1.65% demonstrates"
