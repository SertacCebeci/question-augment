---
description: "Reward hacking can be read as divergence: the training judge's score rises while a stronger judge's out-of-distribution score peaks and falls, a pattern a constant judge bias cannot produce."
aliases: ["proxy-gold divergence", "two-judge hacking measure", "training-judge versus gold-judge divergence"]
sources: ["doi-10-48550-arxiv-2608-11669"]
---
# Proxy-gold divergence as the hacking signal

A policy trained against a judge that also sets its reward cannot be audited by that judge, because a policy that games the judge looks good to it. The measurement the paper proposes uses two judges and an out-of-distribution evaluation set. Every 20 training steps the current policy is graded on the OOD set twice, once by the training (proxy) judge and once by a stronger, cross-family (gold) judge, and four quantities are tracked: the gold score, the proxy-gold gap, an overclaim fraction, and the in-domain full-rubric reward.[^c1] The overclaim fraction is "the share of criteria the proxy marks satisfied but gold rejects," a per-criterion view of the same failure.[^c2]

The signature is a pair of curves that rise together and then part. In the medical run, "gold peaks at 31.2% and starts to slide while" the proxy keeps rising, to 72%, and by the end of training the policy is, by the gold judge's account, worse than it was at its peak.[^c3] The same shape is the one Gao et al. described for learned reward models, where "gold reward rises, peaks, and decays as optimization proceeds."[^c4]

The reason the divergence, rather than the level, carries the evidence is a claim about bias. "A judge with a fixed bias shifts a curve by a constant." A fixed bias in either judge can move a whole curve up or down, but it cannot make the gold curve fall while the proxy curve rises: "What a fixed bias cannot do is make the gold curve" fall while the training score climbs.[^c5] So the paper reads the divergence as the hacking signal and never the absolute gap: "Divergence between the two curves during training is the hacking signal,"[^c6] and "This is why we never interpret the absolute gap."[^c7] The gold judge is not treated as truth: "The gold judge is a stronger model, not ground truth."[^c8]

What transfers from this design is the logic, not the particular judges. The test needs only that the judge's error stays roughly constant along the training trajectory, and that the gold judge is less exposed to the policy's exploit than the training judge is. What does not transfer for free is the stronger-judge assumption; the paper used a cross-family judge, and a same-family stronger judge is untested. My reading: the test rules out constant bias, but a bias that drifts as the policy's outputs drift toward the proxy's preferred style would produce a similar divergence without any change in the true quality being measured.

## Limits

- The gold judge is a judge. "We cannot rule out a distribution-dependent judge bias."[^c9] The argument survives a constant bias in either judge; it does not survive a bias that changes with the distribution of the policy's outputs, and the paper does not test one.
- The evidence is one base run per pair on two benchmark pairs, with one seed per configuration: "Every configuration is a single training run."[^c10]
- The divergence is used in the paper both to detect hacking and to compare mitigations. Whether it detects hacking on tasks other than these two rubric pairs is not shown.
- My reading: the overclaim fraction is counted per criterion, so it inherits any disagreement between the two judges about what a criterion's wording means; the paper does not separate that disagreement from hacking.

## Related

- [[reward-overoptimization]] — the curve shape (a proxy that rises while true quality peaks and falls) that this measurement detects, from learned reward models
- [[verifier-exploitation-rate]] — a per-criterion hacking measure against a unanimous reference panel, close in kind to the overclaim fraction
- [[ordinal-judge-fidelity]] — a constant shift in scores moves no ordering, the same invariance that a fixed-bias argument relies on
- [[rubric-criterion-dropout]] — a mitigation whose effect the paper reads with this two-judge measure

[^c1]: doi-10-48550-arxiv-2608-11669 — "grade each response twice, once with the"
[^c2]: doi-10-48550-arxiv-2608-11669 — "the share of criteria the proxy marks satisfied but gold rejects"
[^c3]: doi-10-48550-arxiv-2608-11669 — "gold peaks at 31.2% and starts to slide while"
[^c4]: doi-10-48550-arxiv-2608-11669 — "showing that gold reward rises, peaks, and decays as optimization proceeds."
[^c5]: doi-10-48550-arxiv-2608-11669 — "judge with a fixed bias shifts a curve by a constant"
[^c6]: doi-10-48550-arxiv-2608-11669 — "Divergence between the two curves during training is the hacking signal,"
[^c7]: doi-10-48550-arxiv-2608-11669 — "This is why we never interpret the absolute gap."
[^c8]: doi-10-48550-arxiv-2608-11669 — "The gold judge is a stronger model, not ground truth."
[^c9]: doi-10-48550-arxiv-2608-11669 — "We cannot rule out a distribution-dependent judge bias."
[^c10]: doi-10-48550-arxiv-2608-11669 — "Every configuration is a single training run"
