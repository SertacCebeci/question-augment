---
description: "Fixed-budget best-arm identification has an exact asymptotic minimax constant for simple regret, set by near-tie instances where the top arms' means differ by order T^-1/2."
aliases: ["fixed-budget best-arm identification", "ordinal optimization", "adaptive experimental design for policy choice", "minimax simple regret constant"]
sources: ["doi-10-48550-arxiv-2506-24007"]
---
# Minimax simple regret constant in fixed-budget best-arm identification

In fixed-budget best-arm identification the experimenter has a total of T samples. The procedure samples arms round by round, and after the last round it recommends one arm. The loss is the simple regret: the gap between the best arm's mean and the mean of the recommended arm. "This quantity is the mean gap between the best arm and the recommended arm, averaged over the experiment."[^c1] The criterion scores how much expected value is lost by the recommendation, not whether the recommendation is exactly right.

The minimax version fixes the outcome families and takes the worst case over mean vectors. "The minimax criterion takes the worst case over" the admissible means.[^c2] The question is then the smallest constant such that every strategy's worst-case regret, scaled by the budget, is at least that constant asymptotically, and some strategy reaches it. Kato's answer is an exact constant, written Γ(P), together with a strategy that attains it. The lower bound "holds over every adaptive experiment," and the upper bound matches it including the constant term.[^c3] The constant is not an order of magnitude; it is a specific number that the matching strategy achieves.

Where the worst case sits is the mechanism. "Minimax regret is governed by near ties with gaps of order" T^-1/2.[^c4] The least favorable instances are the ones where the top means are almost equal: "Least favorable instances are near ties."[^c5] At such an instance the competing arms share a common limiting mean, so their standard deviations are evaluated at that one value. The worst case is therefore driven by the variances at a near tie, not by a fixed gap between arms.

For two arms the constant has a closed form. "For K = 2, the constant has the closed form" Γ(P) equal to the supremum over the means of (σ1 + σ2) times a fixed number, where the number is "cmm = sup xΦ(−x) ≈ 0.1699712."[^c6] So in the two-arm case the worst-case regret is set by the largest combined standard deviation at a tie, and it is attained by the Neyman split of samples, described in [[neyman-allocation]].

The Bayes version of the same problem puts the mass in a different place. "Bayes regret under regular priors is governed by pairwise near ties between the best and second-best arms."[^c7] For a prior with a bounded, uniformly continuous density, "the constant in the Bayes lower bound is determined by the prior" density on the pairwise tie sets.[^c12] The same strategy attains both the minimax and the Bayes constant, though the two criteria are determined by different local mean vectors.

## Limits

- The constant is an asymptotic statement, as the budget T goes to infinity. The parts of the text read here give no finite-budget values. The display of the limit in the extracted text lost its scaling factor. I read the order as T^-1/2 from the near-tie gap, which is my inference, not a quoted formula, and it should be checked against the full display.
- For K ≥ 3 the constant is "an exact characterization of the constant rather than a closed-form formula."[^c8] Adaptivity can matter there. The static value "is at least as large because static policies form a subclass of adaptive policies," and the appendix gives a three-arm example where the inequality is strict.[^c9] So for three or more arms a sampling rule that responds to outcomes is part of what the constant measures; for two arms it is not (see [[neyman-allocation]]).
- The class is mean-parameterized canonical exponential families on a compact mean interval, with variance bounds. The model "also allows mean-dependent variances," and it includes Bernoulli outcomes on a compact subinterval of (0,1).[^c10] Outcomes outside this class, such as heavy-tailed or unbounded ones, are not covered by the statements read here. That is my reading of the setup, not something the text tests.
- The strategy needs the constants of its assumption, since it "uses only the seven constants" named there.[^c11] It does not need the outcome families or the prior, but the constants themselves are supplied.
- I read the introduction, the Gaussian game summary and parts of the Bernoulli section. No experiments were checked, and the proofs were not followed.

## Related

- [[neyman-allocation]] — the two-arm sampling rule that attains this constant, and why it does not extend to three arms
- [[pac-best-arm-sample-complexity-lower-bound]] — the fixed-confidence counterpart: samples needed for an ε-good arm with probability 1−δ, not the regret constant at a fixed budget

[^c1]: doi-10-48550-arxiv-2506-24007 — "This quantity is the mean gap between the best arm and the recommended arm, averaged over"
[^c2]: doi-10-48550-arxiv-2506-24007 — "The minimax criterion takes the worst case over"
[^c3]: doi-10-48550-arxiv-2506-24007 — "lower bound holds over every adaptive experiment"
[^c4]: doi-10-48550-arxiv-2506-24007 — "Minimax regret is governed by near ties with gaps of order"
[^c5]: doi-10-48550-arxiv-2506-24007 — "Least favorable instances are near ties"
[^c6]: doi-10-48550-arxiv-2506-24007 — "For K = 2, the constant has the closed form"
[^c7]: doi-10-48550-arxiv-2506-24007 — "Bayes regret under regular priors is governed by pairwise near ties between the best and"
[^c8]: doi-10-48550-arxiv-2506-24007 — "is an exact characterization of the constant rather than a closed-form formula"
[^c9]: doi-10-48550-arxiv-2506-24007 — "The static value is at least as large because static policies form a subclass of adaptive policies"
[^c10]: doi-10-48550-arxiv-2506-24007 — "also allows mean-dependent variances"
[^c11]: doi-10-48550-arxiv-2506-24007 — "It uses only the seven constants"
[^c12]: doi-10-48550-arxiv-2506-24007 — "the constant in the Bayes lower bound is determined by the prior"
