---
description: "Choosing which data source to sample while betting against a global null can match an oracle that knows the best source: same evidence growth rate and same expected rejection time as alpha goes to 0."
aliases: ["multi-armed sequential hypothesis testing", "SPRUCE", "global null testing with bandit allocation", "log-optimal e-process over arms"]
sources: ["arxiv-2603-17925"]
---
# Multi-armed testing by betting

The setting: at each step the statistician picks one of several data sources (arms) and sees only that arm's outcome. The null is global, meaning every arm is null. The alternative is that at least one arm is not.[^c1] Evidence is a wealth process, an e-process, built by betting. Sandoval, Waudby-Smith and Jordan ask for the strongest possible guarantee: performance as good as a test that knows in advance which arm yields the most evidence.[^c2]

## Mechanism

Two choices are made at every step, and both are adaptive. First, which arm to pull. Second, how to split the bet across e-values for that arm, which is a portfolio over the simplex. The optimal arm and portfolio under the true alternative Q are unknown but learnable. The algorithm, SPRUCE (Sublinear Portfolio Regret Upper Confidence Estimation), pulls the arm with the largest upper confidence bound. That bound is the best in-hindsight average log-wealth of the arm, plus a portfolio-regret term and an exploration bonus.[^c3] This is a modification of upper-confidence-bound algorithms for rewards that are not observed directly but are "estimable". The paper derives nonasymptotic concentration inequalities for optimal Kelly growth rates to make it work.[^c4]

Validity under the null does not depend on the allocation. The wealth is either Cover's universal portfolio, which is a test supermartingale, or a cheaper variant, "in-hindsight maximum minus a regret bound". The cheaper variant is pathwise below the universal portfolio, so it is an e-process.[^c5]

## What is proved

1. Evidence growth. Under any alternative Q in the class, the SPRUCE wealth has the same log growth rate as the oracle, which is the maximum over arm and portfolio of the expected log-increment.[^c6]
2. Expected rejection time. A lower bound holds for any process that chooses arms and portfolios predictably. SPRUCE and the oracle both achieve it in the high-confidence regime: expected rejection time divided by log(1/alpha) tends to the reciprocal of that maximal expected log-increment.[^c7] In words, the cost of not knowing the best arm vanishes relative to the cost of the evidence itself as the error level shrinks.
3. Allocation regret is logarithmic, as in classical UCB. This is shown with bespoke concentration inequalities because the usual bandit assumptions fail here.[^c8]

The lower-bound proof compares the wealth to an oracle-portfolio process, shows the difference is a supermartingale, and applies optional stopping and Wald's identity. The authors say the optional-stopping version they use "seems to be new".[^c9]

## Reading for asking

My own inference, not the paper's: when many candidate probes might each reveal that something is wrong, a questioner can concentrate its budget on the most informative probe and still keep a valid anytime error guarantee. The guarantee is paid for in exploration of the other probes, and the price is asymptotically negligible only when the error target is very strict.

## Limits

- The optimality is asymptotic in alpha. The exact constants are matched only as alpha goes to 0. Finite-alpha behaviour is covered only by nonasymptotic bounds that the note does not reproduce.
- The setting is a fixed finite arm set. Outcomes come from one joint law with no counterfactual observation. A bounded convex combination of e-values (Assumption 1) is required.
- It is a statistical result, tested in a treatment-effect simulation. Nothing was tested with questions, people or language models. The reading above is unverified.
- Rewards are log-wealth growth for a nonparametric portfolio. The result says nothing about arms whose evidence is non-stationary.

## Related

- [[sprt]] — the single-arm, simple-vs-simple ancestor; this note generalizes to composite hypotheses and several sources
- [[upper-confidence-bound-index]] — the allocation principle SPRUCE modifies
- [[e-detector]] — builds on the same e-process machinery, for change detection rather than a global null
- [[thompson-sampling]] — the other standard allocation rule for exploration against exploitation

[^c1]: arxiv-2603-17925 — "We consider the composite global null hypothesis P that all arms are null"
[^c2]: arxiv-2603-17925 — "seek e-processes and sequential"
[^c3]: arxiv-2603-17925 — "Select An = arg maxa∈A UCBa (n), breaking ties arbitrarily."
[^c4]: arxiv-2603-17925 — "we derive nonasymptotic concentration inequalities for optimal"
[^c5]: arxiv-2603-17925 — "Since P-e-processes are those nonnegative processes that are P-almost surely upper-bounded by"
[^c6]: arxiv-2603-17925 — "(ii) For every Q ∈ Q, Wn has an asymptotic growth rate given by"
[^c7]: arxiv-2603-17925 — "Theorem 4.2 demonstrates that in the high-confidence regime, the expected"
[^c8]: arxiv-2603-17925 — "namely having logarithmic allocation regret"
[^c9]: arxiv-2603-17925 — "as this result seems to be new to the literature."
