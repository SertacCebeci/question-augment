---
description: "With rare large rewards, the KL divergence between two arms reduces to a sum of Poisson-type terms, which makes the best-arm lower bound cheaper to compute."
aliases: ["compound Poisson approximation of bandit rewards", "rare-event Poisson KL approximation", "rarity framework for best-arm identification", "Poisson limit of rare rewards"]
sources: ["doi-10-48550-arxiv-2303-07627"]
---
# Poisson approximation of KL divergence for rare rewards

A rare-reward arm is one whose pulls almost always return zero, while its nonzero payoffs are large and occur with small probability. The paper fixes a small rarity parameter γ and lets each positive payoff level have a probability that scales as a power of γ, with the payoff scaling as the inverse power, so that "the expected rewards across arms are comparable."[^c1] Under this setting the reward is zero with probability close to one.[^c2] The rewards from many pulls of one arm can therefore "be well modelled as a Compound Poisson process."[^c3]

The mechanism is a counting limit. Over about tγ^−α pulls, the number of times each positive payoff level appears converges to a Poisson count with mean proportional to t, and the counts at different payoff levels are independent.[^c4] Pulls are i.i.d., so the KL divergence over m pulls is m times the per-pull KL. Substituting the Poisson laws for the count vector gives a per-pull divergence of the form γ^α times a sum over payoff levels j of p_j log(p_j/p̃_j) + (p̃_j − p_j), where p are the reference probabilities and p̃ the alternative ones. The paper states this as the KL divergence between two arms of the same rarity being "approximated by a sum of KL divergences between independent Poisson variables."[^c5]

Why this helps is a computational point. The lower bound on sample complexity for δ-correct best-arm identification is a max-min problem that must be re-solved at each stage of a track-and-stop loop. The paper says that these exact algorithms "are computationally prohibitive, especially since in our rare advertising settings" the informative nonzero samples are rare.[^c6] Under the Poisson form the alternative distributions are searched over a fixed grid, the support of the reference arm extended by the upper bound, rather than over all distributions on the bounded interval. The paper says it "limited its support to that of pi extended to allow point" B_i γ^−α.[^c7] The dual quantities that appear then "have bounded well-defined limits" as γ → 0, so the inner problem can be reduced to a short scalar computation.[^c8] This is the source of the speed-up. (The inference that the grid restriction is what makes the inner problem cheap is mine; the paper reports the restriction and the speed-up but does not isolate which step causes it.)

## Limits

- The approximation is asymptotic. "The Poisson approximation can be seen to be tight as" γ → 0,[^c9] and the paper's deviation bounds are powers of γ, valid "for γ small enough."[^c10] No finite-γ error certificate is given beyond these bounds.
- It needs a known upper bound on each arm's rewards: "We assume that arm specific upper bounds on rewards are available to us."[^c11]
- The sample-complexity cost is small but positive. The paper's asymptotic upper bound shows that "the increase in sample complexity is marginal compared to the computational benefit,"[^c12] and its experiments report "a small increase (1-13 %) in sample complexity" alongside a 6 to 12 times speed-up over the exact track-and-stop algorithm.[^c13] These are a few settings from one simulation study, with runtimes "reported in seconds" on the authors' machine.[^c14] They do not show that the trade-off holds for other reward structures.
- The result is about a statistical approximation of a bandit lower bound. It does not test any question-asking or answer-eliciting setting. Whether such settings have rare, large, informative answers is not established here (my inference).

## Related

- [[kl-divergence]] — the quantity being approximated; the Poisson form is its limit for rare-count laws
- [[pac-best-arm-sample-complexity-lower-bound]] — a different lower bound for best-arm identification, stated for a fixed gap in the PAC setting; the rare-reward work concerns the fixed-confidence δ-correct bound
- [[plug-in-glr-stopping-rule]] — another stopping rule for best-arm identification; the Poisson form targets the lower-bound computation that track-and-stop allocators repeat

[^c1]: doi-10-48550-arxiv-2303-07627 — "the expected rewards across arms are comparable"
[^c2]: doi-10-48550-arxiv-2303-07627 — "Concretely, suppose that γ is a small positive value (say of order 10−2 or lower)"
[^c3]: doi-10-48550-arxiv-2303-07627 — "can be well modelled as a Compound Poisson process"
[^c4]: doi-10-48550-arxiv-2303-07627 — "is a collection of mutually independent random variables"
[^c5]: doi-10-48550-arxiv-2303-07627 — "can be approximated by a sum of KL divergences between independent Poisson variables"
[^c6]: doi-10-48550-arxiv-2303-07627 — "these algorithms are computationally prohibitive, especially since in our rare advertising settings"
[^c7]: doi-10-48550-arxiv-2303-07627 — "we limited its support to that of pi extended to allow point"
[^c8]: doi-10-48550-arxiv-2303-07627 — "have bounded well-defined limits"
[^c9]: doi-10-48550-arxiv-2303-07627 — "The Poisson approximation can be seen to be tight as"
[^c10]: doi-10-48550-arxiv-2303-07627 — "for γ small enough"
[^c11]: doi-10-48550-arxiv-2303-07627 — "We assume that arm specific upper bounds on rewards are available to us."
[^c12]: doi-10-48550-arxiv-2303-07627 — "illustrating that the increase in sample complexity is marginal compared to the computational benefit"
[^c13]: doi-10-48550-arxiv-2303-07627 — "for realistic rare event probabilities and reward structure, our algorithm is 6-12 times faster than the TS algorithm with a small increase (1-13 %) in sample complexity"
[^c14]: doi-10-48550-arxiv-2303-07627 — "The computational runtime is reported in seconds (s)."
