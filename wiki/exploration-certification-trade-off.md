---
description: "Identifying the Condorcet winner from noisy pairwise duels costs an exploration term (finding an informative comparison) plus a certification term (confirming its sign); the split is intrinsic."
aliases: ["exploration/certification trade-off", "Condorcet winner identification sample complexity", "dueling bandit best-arm identification"]
sources: ["arxiv-2603-15189"]
---
# Exploration-certification trade-off

In stochastic dueling bandits a learner asks which of two options is preferred and gets a noisy binary answer. Option i has a gap Delta(i,j) = q(i,j) - 1/2 against option j. A Condorcet winner (CW) beats every other option in expectation. The task is to name it with probability 1 - delta using as few comparisons as possible.[^c1]

The older guarantee compares the winner only with each rival, at cost H_cw = log(1/delta) times the sum of 1/Delta(i*,i)^2. The paper notes this "can be overly conservative" when some arm is nearly tied with the winner, because it ignores comparisons among the suboptimal arms.[^c2] A rival can instead be ruled out by finding any strong opponent that beats it. That route has two costs.

- **Exploration/selection**: the effort to find, in each suboptimal row, a negative entry of size at least |Delta(i,(s_i))|. It depends on the number s_i of such entries and their magnitude, and not on delta except for a single arm.[^c3]
- **Certification**: the samples needed to confirm the sign of the chosen entries at confidence 1 - delta, of order log(1/delta)/Delta^2 per arm.

Small s_i makes certification cheap but exploration expensive, since a rare entry is hard to find among K. The upper bound takes the minimum of H_cw and the best split of the two costs over s. The algorithm does not need s as input and reaches the best split on its own.[^c4] The authors read the optimal s as an "effective sparsity" of the gap matrix, which also depends on delta.

The lower bound shows the split is not an artifact of the algorithm. A minimax bound on the (1 - delta)-quantile of the budget matches the sum of the two terms, so the trade-off is "unavoidable and intrinsic to the sample" complexity.[^c5] The proof reduces the problem to active multiple testing for a negative entry in a vector of size K - 1.

The practical consequence is that guarantees in expectation and in high probability differ. As log(1/delta) grows with K and the gaps fixed, the quantile bound has an extra term in K over s times Delta^2. The expected-budget bound of Karnin does not have it. The authors write that "there is a significant gap between guarantees in" the two senses, most of all when the gaps are heterogeneous.[^c6]

## Limits

I read the introduction and the statement of results, not the proofs. The bounds hide logarithmic factors and a log log(1/delta) term. The setting assumes a CW exists and answers are independent Bernoulli draws with fixed probabilities. Mapping this onto question asking, where a question probes which candidate answer or source is best, is my own inference. Real answers are neither independent nor stationary. The fixed-budget results are only mentioned here.

## Related

- [[pac-best-arm-sample-complexity-lower-bound]] — the standard-bandit lower bound; here the feedback is pairwise and structured
- [[one-bit-mean-estimation]] — another result on what adaptive sampling can and cannot save
- [[plug-in-glr-stopping-rule]] — a stopping rule for fixed-confidence identification
- [[thompson-sampling]] — a bandit heuristic without these non-asymptotic quantile guarantees

[^c1]: arxiv-2603-15189 — "We study best-arm identification in stochastic dueling bandits under the sole assumption"
[^c2]: arxiv-2603-15189 — "the bound (2) can be overly conservative when"
[^c3]: arxiv-2603-15189 — "Exploration/Selection cost. This term quantifies the effort required to select a negative entry"
[^c4]: arxiv-2603-15189 — "Importantly, our algorithm does not take s∗∆ as input and therefore automatically achieves"
[^c5]: arxiv-2603-15189 — "the exploration/certification trade-off unveiled in (4) is unavoidable and intrinsic to the sample"
[^c6]: arxiv-2603-15189 — "there is a significant gap between guarantees in"
