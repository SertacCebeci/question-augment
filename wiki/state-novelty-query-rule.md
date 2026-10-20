---
description: "Ask the expert only where a visited state's distance to its K-th nearest labelled neighbour exceeds a threshold, so queries track input-space coverage, not the learner's action disagreement."
aliases: ["CRSAIL querying rule", "kNN novelty query", "state-space coverage querying"]
sources: ["arxiv-2512-00453"]
---
# State-novelty query rule

A query rule decides, at each visited state, whether an expert label is worth its cost. The state-novelty rule answers from the inputs alone: it asks for a label where the labelled data are sparse, and skips where they are dense. The paper's own wording is that the expert is asked for an action "when the visited state is under-represented in the expert-labeled" dataset.[^s1]

## Mechanism

The score is the distance from a visited state x to its K-th nearest neighbour among the states already labelled by the expert. Equivalently it is the radius of the smallest closed ball centred at x that holds K labelled states.[^s2] A large radius means a sparse neighbourhood: "Larger scores indicate lower local data density and hence greater novelty".[^s3] The rule is then one cut. A visited state is queried when its score is above a threshold R, and skipped otherwise. The authors gloss it as: "if the neighborhood is sparse, we request the expert label."[^s4]

The neighbour order K changes the behaviour of the score. A larger K makes it "robust to outliers and accepting of duplicates."[^s5] So the rule is not triggered by one stray state, and a cluster of near-identical states does not each cost a label.

The threshold R is set by the conformal construction in [[conformal-prediction]]: the (1 − α) empirical quantile of the scores of unlabelled states visited by the initial policy. The paper calls α "a principled tuning knob for controlling the expected" query rate.[^s6] The calibration is done once, before training, on the initial behaviour-cloned policy.[^s7]

The queries are issued after each episode, not during it. The learner rolls out a full trajectory, and the scores are then computed for its states and the flagged ones are sent to the expert as one batch.[^s8] This is the property the abstract sets against gate-based methods: the approach "can be run without real-time expert takeovers."[^s9]

## What it contrasts with

Methods such as [[query-by-committee]]-style ensembles ask where the learner's outputs disagree. The paper's objection to action-space disagreement is that it "mixes epistemic uncertainty, which active methods aim to reduce with" data, with aleatoric randomness that does not shrink with data.[^s10] The aleatoric part "can be high even in well-covered regions, which weakens action-based novelty" tests.[^s11] This is the authors' argument. The paper does not separate the two components in an experiment, so the claim rests on the argument alone.

## What was measured

On MuJoCo tasks the abstract reports that CRSAIL reduces total expert queries "by up to 96% vs. DAgger and up to 65% vs. prior AIL methods, with" empirical robustness to α and K.[^s12] Per task, the body reports that on Inverted Double Pendulum and Pusher CRSAIL "requests 66.3% and 47.8% fewer expert labels respectively" than the previous best baseline, "without a meaningful loss of reward."[^s13]

## Limits

- Three MuJoCo tasks, each with one RL expert: "The expert for each task is an RL model trained with" Stable Baselines3.[^s14] Human labellers and expensive GPU simulators, the costs the introduction names, are not tested. Cost is counted as a number of labels, not as operator time or GPU hours.
- Hopper is the weak case. "On Hopper—our most challenging domain—CRSAIL remains modestly successful" with convergence in 24 of 25 runs.[^s15]
- The coverage statement is an idealised reference. The calibration states along one trajectory are correlated, so "distributed across time steps, so exchangeability is violated." The authors add that the statement "should be viewed as an idealized reference rather" than a strict guarantee.[^s16][^s17]
- One fixed R, calibrated once. The authors reject recalibrating with the current policy because it would hold the rate "the query rate to remain approximately constant rather than" decaying as coverage improves.[^s18] So α controls the rate at calibration time; how the rate evolves afterwards is a design consequence, not a tuned target.
- The distance ignores actions. Two states with the same coordinates but different needed actions count alike. The authors list this as future work: "Future work includes incorporating action similarity into" the distance metric.[^s19]
- Baselines were not always run with their own settings. "sweep the gating hyperparameters to span query rates from" near zero was used where the original papers did not cover the environment, so the comparison depends on that sweep.[^s20]
- The choice of K = 5 and α in a narrow band came from a coarse sweep on these tasks.[^s21] My inference: the robustness is shown on three low-dimensional MuJoCo state spaces; nothing here shows the nearest-neighbour distance remains informative in image or high-dimensional observation spaces.

## Related

- [[active-imitation-learning]] — the setting this rule is an admissible strategy for; the rule is judged by the imitation loss it reaches under a query budget
- [[conformal-prediction]] — the quantile construction that sets R, and its exchangeability assumption
- [[query-by-committee]] — asking where a committee disagrees, the disagreement-based family this rule is set against
- [[active-testing]] — another budgeted choice of which items to label, in evaluation rather than training

[^s1]: arxiv-2512-00453 — "when the visited state is under-represented in the expert-labeled"
[^s2]: arxiv-2512-00453 — "closed ball centered at x that contains at least K elements"
[^s3]: arxiv-2512-00453 — "Larger scores indicate lower local data density and"
[^s4]: arxiv-2512-00453 — "if the neighborhood is sparse, we request the expert label."
[^s5]: arxiv-2512-00453 — "robust to outliers and accepting of duplicates."
[^s6]: arxiv-2512-00453 — "into a principled tuning knob for controlling the expected"
[^s7]: arxiv-2512-00453 — "calibrate R using conformal prediction on unlabeled onpolicy states from the initial learner"
[^s8]: arxiv-2512-00453 — "Queries are issued post hoc in batch after each episode"
[^s9]: arxiv-2512-00453 — "can be run without real-time expert takeovers"
[^s10]: arxiv-2512-00453 — "Action-space disagreement mixes epistemic uncertainty, which active methods aim to reduce with"
[^s11]: arxiv-2512-00453 — "well-covered regions, which weakens action-based novelty"
[^s12]: arxiv-2512-00453 — "96% vs. DAgger and up to 65% vs. prior AIL methods, with"
[^s13]: arxiv-2512-00453 — "requests 66.3% and 47.8% fewer expert labels respectively"
[^s14]: arxiv-2512-00453 — "The expert for each task is an RL model trained with"
[^s15]: arxiv-2512-00453 — "On Hopper—our most challenging domain—CRSAIL remains modestly successful"
[^s16]: arxiv-2512-00453 — "distributed across time steps, so exchangeability is violated"
[^s17]: arxiv-2512-00453 — "should be viewed as an idealized reference rather"
[^s18]: arxiv-2512-00453 — "the query rate to remain approximately constant rather than"
[^s19]: arxiv-2512-00453 — "Future work includes incorporating action similarity into"
[^s20]: arxiv-2512-00453 — "sweep the gating hyperparameters to span query rates from"
[^s21]: arxiv-2512-00453 — "For CRSAIL we fix K = 5 and choose α"
