---
description: "Under RLVR with group-relative policy gradients, policy entropy falls steeply, which narrows exploration and the diversity of sampled responses; a covariance term drives the fall."
aliases: ["entropy collapse", "policy entropy collapse", "RLVR entropy collapse", "exploration collapse under verifiable rewards"]
sources: ["arxiv-2512-04359", "arxiv-2511-16231"]
---
# RLVR entropy collapse

Reinforcement learning with verifiable rewards (RLVR) trains a model on a checkable outcome. The accuracy signal alone has a side effect: the policy's entropy falls during post-training. The paper's account is that this "purely accuracy-based learning paradigm decreases exploration and may lead to local optima",[^e1] and that entropy "drops sharply during training, resulting in generated responses that lack diversity and further limiting exploration."[^e2] Entropy here is the per-token Shannon entropy of the policy's next-token distribution, averaged over the response, so the collapse is a loss of spread in what the model is willing to write.

The paper's Fig. 1 contrasts three runs. The GRPO baseline shows the collapse. A variant that adds an entropy-maximisation objective "encounters entropy explosion, resulting in policy instability."[^e3] So the collapse is the default direction of the plain objective, and the obvious counter-term over-corrects. Any remedy has to act on the mechanism, not only push entropy up.

The mechanism the paper adopts from earlier work is a covariance identity. The change in policy entropy between two steps is, to first order, "the change of policy entropy approximately equals the negative covariance between log-probability of the action and the change of logits."[^e4] Under a policy-gradient update the logit change is proportional to the action probability times its advantage. The sign of the entropy change therefore follows whether likely tokens carry high advantage. The paper says that in training this covariance "is predominantly positive during training (high-probability tokens with high advantages), leading to monotonic entropy decrease."[^e5] [[entropy-covariance-token-selection]] turns this covariance into a per-token rule.

The paper pairs the token-level remedy with a data-side one, a [[semantic-entropy-curriculum]] that orders training questions by their difficulty. Both target the same fall, from different ends.

A second, analytic account in the same setting concerns the gap between pass@k and pass@1 rather than entropy. A mode whose probability falls below a threshold is "statistically likely to miss it entirely," and the policy then "concentrates exclusively on the already discovered mode."[^e7] On the paper's two-mode model, with the dominant mode carrying 1 − δ, the gap is δ − δ^k, so it closes as the mass concentrates: "pass@k provides diminishing returns and converges to pass@1."[^e8] The paper ties this to the entropy fall: standard RLVR induces entropy collapse, "actively eroding the sample diversity required for pass@k to be meaningful."[^e9] Why the pass@k objective itself gives little signal is in [[pass-at-k-gradient-reweighting]].

## Limits

- The collapse is shown on one training curve in Fig. 1, for one reasoning setup. The claim that it is general to RLVR rests on the paper's introduction and the works it cites, which I did not read (my reading).
- The covariance account is a first-order approximation. The paper's entropy-change result is stated "under first-order approximation", so it is a statement about the sign of one step's change, not about the trajectory over a run.[^e6]
- Entropy measures spread, not correctness. A policy can keep high entropy and be wrong, and a low-entropy policy can be right; the paper's gains are reported on accuracy and Pass@16, not on entropy alone (my inference). See [[confidently-wrong-low-entropy-regime]].
- The paper gives no account of collapse under other objectives, other model families, or much longer training than the runs it shows; these were not tested in the parts I read.
- The pass@k gap argument is a two-mode model. It uses a first-order bound for the discovery probability and a gradient approximation for the mass update, and it assumes "Assuming correctness is defined by falling into the dominant mode."[^e10] The text read has no trained-policy run that measures the gap closing; the claim is analytic (my reading).

## Related

- [[entropy-covariance-token-selection]] — the covariance criterion, turned into a per-token KL rule meant to slow this collapse
- [[semantic-entropy-curriculum]] — the data-side intervention the same paper combines with the token-level one
- [[rollout-dispersion-curriculum]] — another diversity-aware weighting of RLVR prompt groups; there the collapse sits in the group's own rollouts
- [[confidently-wrong-low-entropy-regime]] — low entropy does not certify a correct answer
- [[entropy]] — the Shannon quantity that collapses here, taken per token
- [[selection-reinforcement-bias]] — a sequence-level account of a narrowing toward likely correct answers, from the objective's selection and reinforcement terms; the two accounts were not compared in the parts read
- [[pass-at-k-gradient-reweighting]] — the same paper's gradient analysis: pass@k as a training target is the pass@1 gradient with a per-prompt weight, which vanishes when no sample is correct

[^e1]: arxiv-2512-04359 — "this purely accuracy-based learning paradigm decreases exploration and may lead to local optima"
[^e2]: arxiv-2512-04359 — "drops sharply during training, resulting in generated responses that lack diversity and further limiting exploration."
[^e3]: arxiv-2512-04359 — "encounters entropy explosion, resulting in policy instability"
[^e4]: arxiv-2512-04359 — "the change of policy entropy approximately equals the negative covariance between log-probability of the action and the change of logits"
[^e5]: arxiv-2512-04359 — "This covariance term is predominantly positive during training (high-probability tokens with high advantages), leading to monotonic entropy decrease."
[^e6]: arxiv-2512-04359 — "under first-order approximation"
[^e7]: arxiv-2511-16231 — "statistically likely to miss it entirely"
[^e8]: arxiv-2511-16231 — "pass@k provides diminishing returns and converges to pass@1"
[^e9]: arxiv-2511-16231 — "actively eroding the sample diversity required for pass@k to be meaningful"
[^e10]: arxiv-2511-16231 — "Assuming correctness is defined by falling into the dominant mode"
