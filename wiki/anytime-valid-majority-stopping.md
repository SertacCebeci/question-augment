---
description: "Keep sampling rollouts until the leader beats its runner-up and all others under e-processes valid at any stopping time, so the stopped vote errs with probability at most epsilon."
aliases: ["Martingale Majority Certificate", "MMC", "sequential self-consistency stopping rule", "anytime-valid majority certificate"]
sources: ["doi-10-48550-arxiv-2510-17472"]
---
# Anytime-valid majority stopping

A fixed-n majority vote needs n chosen in advance, and the error bound in [[majority-vote-mode-certificate]] depends on a margin that is unknown until sampling is done. The stopping rule answers the practical question: how many rollouts are enough. The paper's Martingale Majority Certificate (MMC) is "a sequential procedure based on e-values and Ville" 's inequality, and it works in the way the paper states: "Rather than fixing n in advance, MMC updates after each new sample and stops" once the evidence is sufficient.[^c1]

The mechanism is a pair of e-processes. Before each draw the rule fixes the current leader A and runner-up B, and it keeps predictable counts: leader hits, runner-up hits, and hits on all other answers. One e-process tests leader against runner-up, and a second tests leader against the rest. Each multiplies a per-round factor 2θ when the leader is drawn, or 2(1−θ) when the runner-up is drawn, with θ the leader's share of the two-way mass, averaged over a prior on θ. Under the null that the leader is no more likely than its rival, the process is a test supermartingale. Ville's inequality then bounds the chance that it ever exceeds 1/ε by ε, so the stopping time can be data-dependent. The paper states this as: "the e-processes defined above provide anytime-valid tests."[^c2] The rule "stop[s] only when both conditions are satisfied with high probability", which is what gives the stopped vote an error at most ε.[^c3]

The cost of certification is set by the margin. The paper gives the expected stopping time as "the expected stopping time of the MMC scales approximately as" a quantity of order 2(p + q)/(p − q)² · log(1/ε), with p and q the leader and runner-up probabilities.[^c4] The paper's gloss is that "small mode margins lead to rapidly increasing sample requirements."[^c5] So the stopping rule turns the margin from a quantity to be guessed into a quantity that is paid for in draws: a wide margin ends sampling early, a near-tie makes it run long.

## Limits

- The stopping-time formula is an approximation: the text says "approximately", and the derivation is a heuristic that assumes the informative-round parameter is tracked well by a plug-in estimate. It is not a theorem.
- The main text works the case of two leading answers: "we focus on the case m = 2". The general case with several runner-ups is in an appendix the section read did not cover.[^c6]
- The rollouts are assumed conditionally i.i.d.; the paper lists correlated rollouts as open: "Future work will explore applying anytime-valid certificates to correlated rollouts".[^c7]
- Answers must be grouped into classes first. The paper says free text "would still require some degree of response canonicalisation", and that a reformulation avoiding the grouping is future work.
- The empirical claims are for "the simplified setting of problems with discrete, multiple-choice outputs."[^c8]
- Efficiency is not free: "Although anytime-valid stopping improves expected efficiency" the paper adds that generating multiple trajectories "still incurs substantial compute cost."[^c9] Stopping early saves draws, not the cost of the draws it needs.
- My inference, not the paper's: a stopping rule for one fixed prompt does not by itself bound the error across a stream of prompts. The per-prompt guarantee is what is stated.

## Related

- [[majority-vote-mode-certificate]] — the fixed-n error bound that this rule makes sequential.
- [[e-detector]] — uses the same e-process building block, but for change detection instead of a fixed null on a margin.
- [[robust-log-optimal-e-value]] — chooses the e-value by growth rate, so the stopping time is set by a rate constant; a different route to a short stopping time.
- [[conformal-test-martingale]] — another test martingale, with an exchangeability null rather than a two-way share null.

[^c1]: doi-10-48550-arxiv-2510-17472 — "Rather than fixing n in advance, MMC updates after each new sample and stops"
[^c2]: doi-10-48550-arxiv-2510-17472 — "the e-processes defined above provide anytime-valid tests"
[^c3]: doi-10-48550-arxiv-2510-17472 — "We stop only when both conditions are satisfied with high probability"
[^c4]: doi-10-48550-arxiv-2510-17472 — "the expected stopping time of the MMC scales approximately as"
[^c5]: doi-10-48550-arxiv-2510-17472 — "lead to rapidly increasing sample requirements"
[^c6]: doi-10-48550-arxiv-2510-17472 — "we focus on the case m = 2"
[^c7]: doi-10-48550-arxiv-2510-17472 — "Future work will explore applying anytime-valid certificates to correlated rollouts"
[^c8]: doi-10-48550-arxiv-2510-17472 — "in the simplified setting of problems with discrete, multiple-choice outputs"
[^c9]: doi-10-48550-arxiv-2510-17472 — "Although anytime-valid stopping improves expected efficiency"
