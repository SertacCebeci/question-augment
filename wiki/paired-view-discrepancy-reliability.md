---
description: "Scoring one output through a deployed view and a canonical view exposes reward inflation that no single scalar reward reveals; the gap shows differing views, not by itself an attack."
aliases: ["cross-view reward discrepancy", "deployed-canonical reward gap", "paired reward assessment"]
sources: ["doi-10-48550-arxiv-2609-36900"]
---
# Paired-view discrepancy as reliability

A reward model returns one scalar per output, and an inflated scalar looks exactly like an honest one. The paper's move is to score the same output twice. The deployed view is the representation the system actually uses, such as a token mapping that the reward model reads directly. The canonical view is a frozen rendering of the same output. Their difference, the deployed score minus the canonical score, is positive where the deployed reward credits something the canonical text does not support: "Positive D measures deployed-interface" reward of that kind.[^c1]

## Mechanism

The gap becomes a weight in three steps. First, on trusted benign outputs, a location and a scale are fitted to the gap in each context (a tokenizer pair, a task family, a response-length bin). Second, each new gap is standardized by that fit. Third, a conformal threshold is set on a separate calibration split, and a rollout whose standardized gap stays under the threshold keeps weight one, while one above it is downweighted exponentially at a chosen rate. The paper is explicit about what the number is: "The coefficient w controls optimization influence; it is not a posterior probability that the response is clean."[^c2]

Why two views rather than one? The paper's first result is an identification claim. For any probability law on the reward and any positive shift, there is a clean model and an attacked model with the same observed law, while the attacked canonical reward is smaller by that shift. The conclusion is that "no detector based only on Robs uniformly distinguishes the two models."[^c3] The pair carries information that a single observed reward does not. The paper's second result marks the edge of that information: an attack that adds the same random shift to every view leaves every pairwise difference unchanged, so that "every discrepancy-only test has type-I plus type-II error at least one."[^c4] The paired views therefore detect differential shifts only: "Paired views supply evidence about differential shifts."[^c5]

The threat model is written to match. It targets "reward inflation that is expressed as disagreement between two views of" the same rollout, and it requires that "the observed interface must be reachable by the deployed system."[^c6] [^c7]

## Transfer

The same move appears in [[generative-verification]], where a detection is scored by disagreement with an independent process that cannot see the detector's confidence. Here the second view is a canonicalizer in the token-interface experiment, and a rubric-free semantic judge in the rubric-proxy experiment. What survives: a shift shared by both views is invisible to their gap, so the second view must be one that the attack does not also move. What does not survive: in the second experiment the two views are different evaluators, not two renderings of one model. The paper says so itself: "The training discrepancy does not measure a tokenizer or serialization change within a single reward model." The gap there measures a disagreement between a proxy judge and an anchor judge, and inherits the biases of both. The paper scores its outcome with a third judge that is "never used in policy updates," which answers the bias question only for the outcome, not for the anchor.[^c8]

## Limits

- The calibration is small. "The STAR calibration run uses one sampled response per calibration prompt," which gives 1,000 observations across six contexts in the token-interface experiment.[^c9]
- The coverage claim is marginal and finite-sample: "The first claim is the standard finite-sample marginal split-calibration guarantee."[^c10] Downweighting of attacked outputs needs separation between the attacked and clean scores: "For separated attacked scores, the same weight map yields the exponential attenuation." Separation is a premise of that result, and the experiments read here do not check it (my reading).[^c11]
- The contexts must be fixed in advance: "rare-context merges, and unseen-context fallback rules are frozen before calibration."[^c12]
- A large gap is evidence of a difference between views, not of an attack. The paper says that paired views "do not by themselves establish that every observed discrepancy is an attack."[^c13]

## Related

- [[generative-verification]] — the same move in object detection: disagreement with an independent view that cannot see the first view's confidence
- [[reward-overoptimization]] — the gap between a proxy reward and the true objective that this discrepancy tries to expose
- [[reliability-inside-group-baseline]] — what the paper does with the weight once it has one
- [[verifier-exploitation-rate]] — reward hacking measured against a unanimous reference panel, a different reference for a similar gap
- [[conformal-prediction]] — the threshold on the gap is a split-conformal quantile

[^c1]: doi-10-48550-arxiv-2609-36900 — "Positive D measures deployed-interface"
[^c2]: doi-10-48550-arxiv-2609-36900 — "The coefficient w controls optimization influence; it is not a posterior probability that the response is clean"
[^c3]: doi-10-48550-arxiv-2609-36900 — "no detector based only on Robs uniformly distinguishes the two models"
[^c4]: doi-10-48550-arxiv-2609-36900 — "every discrepancy-only test has type-I plus type-II error at least one"
[^c5]: doi-10-48550-arxiv-2609-36900 — "Paired views supply evidence about differential shifts"
[^c6]: doi-10-48550-arxiv-2609-36900 — "reward inflation that is expressed as disagreement between two views of"
[^c7]: doi-10-48550-arxiv-2609-36900 — "The observed interface must be reachable by the deployed system"
[^c8]: doi-10-48550-arxiv-2609-36900 — "RQ2 uses a third judge that is never used in policy"
[^c9]: doi-10-48550-arxiv-2609-36900 — "The STAR calibration run uses one sampled response per calibration prompt"
[^c10]: doi-10-48550-arxiv-2609-36900 — "The first claim is the standard finite-sample marginal split-calibration guarantee"
[^c11]: doi-10-48550-arxiv-2609-36900 — "For separated attacked scores, the same weight map yields the exponential attenuation"
[^c12]: doi-10-48550-arxiv-2609-36900 — "rare-context merges, and unseen-context fallback rules are frozen before calibration"
[^c13]: doi-10-48550-arxiv-2609-36900 — "establish that every observed discrepancy is an attack"
