---
description: "Model an expert's answers as noisy categorical draws given the hidden structure, then pick each local question by expected information gain on the answer; this beats uncertainty sampling."
aliases: ["causal preference elicitation", "CaPE", "expert-in-the-loop Bayesian elicitation"]
sources: ["doi-10-48550-arxiv-2602-01483"]
---
# Noisy-expert channel with local-query elicitation

Causal preference elicitation (CaPE) asks an expert about one variable pair at a time and updates a posterior over a whole directed graph. Three parts make it work. First, the expert is a noisy channel: a likelihood p(Y | W) maps each candidate graph W to a three-way answer (edge i to j, edge j to i, or no edge). Reliability and decisiveness are logistic parameters, so answers can be informative, heterogeneous and uncertain.[^c1] Second, the prior is any black-box posterior over graphs, represented by samples and reweighted after each answer. Third, the next pair is chosen by a BALD-style [[expected-information-gain]] criterion computed on the expert's categorical response.[^c2]

## Mechanism

Because the question is local (one pair) and the answer alphabet has three values, the information gain is cheap to compute even though the posterior lives on a combinatorial graph space. The paper's appendix shows the gain equals the expected KL divergence between each graph's predicted answer distribution and their mixture. It is zero when all candidate graphs agree on how the expert would answer, and large when they disagree sharply.[^c3] This is the [[query-by-committee]] disagreement idea expressed as a [[mutual-information]] on the answer. The posterior is kept as weighted samples with importance reweighting, resampling and light MCMC to keep acyclic diversity, a variant of [[particle-approximated-eig-selection]].[^c4]

The framework is positioned as complementary to [[bayesian-experimental-design]] for causal discovery. Intervention design picks actions and observes new data. Elicitation picks structural questions and observes a judgment through an expert channel. This matters where interventions are costly or fixed.[^c5]

## What was measured

On synthetic graphs, the Sachs protein-signaling data (11 variables) and a human gene-perturbation benchmark (CausalBench), the paper reports faster posterior concentration and better recovery of directed edges under small query budgets. A static one-shot expert baseline is competitive at small budgets but saturates. CaPE improves monotonically and beats all baselines by T of 100 queries or more. Naive uncertainty sampling gets worse as the budget grows.[^c6] In the CausalBench results all methods dip briefly at very small budgets, because early local feedback can disrupt global ranking before enough accumulates.[^c7] Under misspecified experts (heterogeneous reliability, directional bias, abstention bias, noisier answers), CaPE stayed better than or comparable to the baselines.[^c8]

## Limits

- The expert in all experiments is simulated from a reference graph. No human expert was queried; reliability of real people is an assumption (my reading of the setup).
- Misspecification tests are explicitly non-adversarial; adversarial or mutually disagreeing experts are not covered.[^c8]
- The identifiability and finite-time concentration result is stated informally and only under non-adversarial feedback, where the correct orientation gets strictly higher probability than any wrong one.[^c9]
- One query touches one pair, so resolving global uncertainty can take many rounds. Per-round cost is O(SD^2 + Sk) and is practical only to about 50 variables. Latent confounding is not modeled.[^c10]
- Whether the gain transfers to asking questions outside causal graph discovery (for example open-ended conversation) is untested here.

## Related

- [[expected-information-gain]] — the selection criterion, here on a three-way categorical answer
- [[particle-approximated-eig-selection]] — another sample-based posterior used to score questions
- [[query-by-committee]] — disagreement among hypotheses as the selection signal
- [[bayesian-experimental-design]] — the parent framework; CaPE queries judgments rather than running experiments
- [[mutual-information]] — the gain equals mutual information between graph and answer

[^c1]: doi-10-48550-arxiv-2602-01483 — "This allows expert feedback to be informative, heterogeneous, and uncertain"
[^c2]: doi-10-48550-arxiv-2602-01483 — "queries are selected by an efficient expected information gain criterion on the expert’s categorical response"
[^c3]: doi-10-48550-arxiv-2602-01483 — "EIG quantifies the degree of posterior disagreement about the expert’s answer in the probability simplex."
[^c4]: doi-10-48550-arxiv-2602-01483 — "is performed using a particle-based approximation updated"
[^c5]: doi-10-48550-arxiv-2602-01483 — "This distinction is important in domains where interventions are expensive, ethically"
[^c6]: doi-10-48550-arxiv-2602-01483 — "Naive uncertainty sampling"
[^c7]: doi-10-48550-arxiv-2602-01483 — "early expert"
[^c8]: doi-10-48550-arxiv-2602-01483 — "These experiments are not intended to cover"
[^c9]: doi-10-48550-arxiv-2602-01483 — "Proposition (informal)."
[^c10]: doi-10-48550-arxiv-2602-01483 — "does not explicitly"
