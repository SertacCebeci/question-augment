---
description: "Querying the highest-variance proposition beats random queries while the world is stable, lags them just after a flip, and overtakes them later under skewed access; one simulation."
aliases: ["uncertainty sampling after a regime shift", "re-calibration penalty"]
sources: ["arxiv-2512-20884"]
---
# Uncertainty sampling under regime shift

The query rule is simple: among the propositions an agent tracks, ask about the one whose belief has the largest variance. Under the forgetting-factor posterior of [[forgetting-factor-beta-bernoulli]], that variance has a positive floor, so the rule never stops selecting. The paper compares this rule with uniformly random queries in a simulation of 100 propositions whose truth flips once, at t = 501.

With uniform access and γ = 0.999, the variance-targeting agent drives error down faster than random sampling before the flip; the text says it drives "MSE significantly lower than" the random agent.[^c1] Right after the flip the order reverses. The paper reports that the uncertainty agent "spikes to a higher" error than random sampling and lags behind it.[^c2] Its explanation is that the agent has built strong beliefs in the old regime and must take them apart, so it "effectively over-thinking the shift" on the ambiguous transition, while "random agent benefits from broader exploration".[^c3][^c4]

With Zipfian access (s = 1.1), a skewed head of propositions gets most queries. The random agent "performs poorly throughout", because it spends most of its budget on rarely queried propositions.[^c5] The uncertainty agent shows the same initial penalty, but "Around t = 900, it crosses" below the random agent and keeps falling.[^c6] The authors conclude that "uncertainty sampling is the only viable" strategy for a high-fidelity belief state in skewed, changing environments.[^c7]

## Mechanism of the lag

Two things could produce the lag, and the paper does not separate them. One is the decay itself: with γ = 0.999 the effective count is near 1000, so a flip needs on the order of that many observations to dominate the posterior. The paper's first experiment shows this inertia for the high-γ agent. The other is the query rule: a proposition whose belief is confident has low variance, so the rule has little reason to revisit it. Its attention moves to propositions whose mean sits near 0.5, which after the flip are the ones in transition. My inference is that both contribute; no run isolates either.

## Limits

- One simulated setup. The sections read report no seeds, repetitions or error bands, so the crossing at "around t = 900" is read from a single run's figure.
- Only two query rules are compared, variance-targeted and random. The paper says a full analysis of uncertainty against random selection "is beyond the scope of this paper".[^c8] Thompson sampling, information-gain rules and the positive-first alternatives are not tried.
- The Zipfian experiment does not restate γ in the sections read, so the crossing point cannot be reproduced from the text alone.
- The remedy for the lag is proposed, not tested: "future architectures could employ a surprisal reset" of the effective count when a prediction error passes a threshold.[^c9] The text gives no threshold and no run.
- The propositions are independent, so the result says nothing about correlated knowledge, where a shift in one belief would move others.

## Related

- [[forgetting-factor-beta-bernoulli]] — the decay whose time constant sets how long the old regime is remembered
- [[expected-information-gain]] — the score that uncertainty sampling approximates; not compared with it here
- [[noise-seeking-uncertainty-sampling]] — a different known failure of uncertainty sampling, from noisy labels rather than from a shift
- [[thompson-sampling]] — explores by a posterior draw rather than by maximal variance; no comparison is made in this paper

[^c1]: arxiv-2512-20884 — "driving MSE significantly lower than"
[^c2]: arxiv-2512-20884 — "the uncertainty agent spikes to a higher"
[^c3]: arxiv-2512-20884 — "effectively over-thinking the shift"
[^c4]: arxiv-2512-20884 — "random agent benefits from broader exploration"
[^c5]: arxiv-2512-20884 — "performs poorly throughout"
[^c6]: arxiv-2512-20884 — "Around t = 900, it crosses"
[^c7]: arxiv-2512-20884 — "uncertainty sampling is the only viable"
[^c8]: arxiv-2512-20884 — "beyond the scope of this paper"
[^c9]: arxiv-2512-20884 — "surprisal reset mechanism"
