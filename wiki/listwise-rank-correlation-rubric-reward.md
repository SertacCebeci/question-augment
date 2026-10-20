---
description: "A rubric generator earns reward by how well the ranking its rubric induces over a slate of candidate actions matches a multi-judge consensus, scored with Spearman rank correlation."
aliases: ["listwise Spearman reward", "rank-correlation rubric reward", "listwise GRPO rubric objective", "slate ranking reward", "Spearman reward for rubric generator"]
sources: ["doi-10-48550-arxiv-2605-23590"]
---
# Listwise rank-correlation rubric reward

A rubric can read well and still not separate good actions from bad ones. The reward used to train the Co-ReAct rubric generator is built to catch that. It does not score the rubric's text. It scores the order the rubric induces over a slate of candidates, and checks that order against a consensus. The paper's reason is direct: "A rubric is useful only if it can discriminate"[^l1] good actions from bad ones at the same branching point.

The construction has three parts. First, at each branching point a slate is formed. "The four candidates are randomly permuted" and relabelled with neutral identifiers, so that position carries no information[^l2]. Second, the consensus: "Each judge returns a full ranking" of the slate[^l3], from several frontier LLM judges "drawn from different model families"[^l4], and "We aggregate the rankings via Borda count"[^l5]. The consensus ranking is the permutation that Borda sorting induces. Third, the rubric-induced ranking: an evaluator LLM returns "the weighted fraction of rubric criteria the action satisfies"[^l6] for each candidate, and sorting these scores gives a second ranking.

The reward is the Spearman rank correlation between the two rankings, rescaled "to [0, 1]"[^l7]. The scale is anchored: "a random ranking gets 0.5 in expectation, and perfect agreement gets 1"[^l12], and an anti-correlated ranking gets 0. The paper states the consequence: "a plausible-sounding rubric that cannot sort candidates in the expert order earns no credit above chance"[^l8]. Two shaping terms, for atomicity of criteria and for output format, are added with much smaller weight, so the rank term "drives learning" and the others "only refine how the" rubric is phrased[^l9].

The listwise choice is argued against the alternatives. The authors contrast their objective with "pairwise or binary preference formulations"[^l10]. In their ablation, switching to pairwise GRPO lowers the score (74.04 on SQA-CS-V2 in the paper's Table 2), and the stated reason is that "optimization provides richer gradient signals across full rankings"[^l13].

What transfers from the statistics. Spearman's rho is a statistic on whole orderings. What survives the transfer is that it rewards getting the order right and is indifferent to the size of the score differences between candidates. What does not survive is the ground truth: the "expert" order is itself the output of LLM judges, so the reward is a correlation with a model consensus, not with outcomes.

## Limits

- The consensus is LLM judges, not human experts. The paper's phrase "expert consensus" refers to them. A Borda aggregate averages one judge's idiosyncrasies away, but a bias the judges share passes straight into the reward. (my inference)
- The slate is four candidates. With four items there are 24 possible orders, and a single adjacent swap moves rho from 1 to 0.8 (my arithmetic). The reward is therefore coarse at this size, and a few noisy consensus pairs can move it a lot. Larger slates are not tested in the parts I read.
- The rubric's criteria are scored by an evaluator LLM. The reward inherits that evaluator's reading of each criterion, so a rubric whose criteria the evaluator misreads is penalised for the evaluator's error. (my inference)
- The ablation compares listwise with pairwise training only. Whether a binary accept/reject reward, the other alternative the paper names, does worse was not measured in the parts I read.
- The rank term carries most of the weight, but the weighting itself was not varied in the parts I read; the claim that shaping "only refine[s]" the rubric is the authors' design choice.

## Related

- [[step-level-rubric-guidance]] — the rubric this reward trains is injected into the agent before each action, so the ranking it earns is the one the agent is steered by
- [[preference-consistency-rubric-reward]] — the pairwise version: a rubric rewarded for placing the preferred report above the rejected one
- [[co-evolving-rubric-generator]] — a rubric reward from the spread of scores across candidate answers, trained alongside the policy rather than against a consensus
- [[pessimistic-min-judge-aggregation]] — the minimum over judges as an alternative to Borda consensus, which requires agreement before reward
- [[within-group-ordinal-utility-aggregation]] — another route from ordinal judgments over a group of samples to a reward

[^l1]: doi-10-48550-arxiv-2605-23590 — "A rubric is useful only if it can discriminate"
[^l2]: doi-10-48550-arxiv-2605-23590 — "The four candidates are randomly permuted"
[^l3]: doi-10-48550-arxiv-2605-23590 — "Each judge returns a full ranking"
[^l4]: doi-10-48550-arxiv-2605-23590 — "drawn from different model families"
[^l5]: doi-10-48550-arxiv-2605-23590 — "We aggregate the rankings via Borda count"
[^l6]: doi-10-48550-arxiv-2605-23590 — "the weighted fraction of rubric criteria the action satisfies"
[^l7]: doi-10-48550-arxiv-2605-23590 — "rescaled to [0, 1]"
[^l8]: doi-10-48550-arxiv-2605-23590 — "that cannot sort candidates in the expert order earns no credit above chance"
[^l9]: doi-10-48550-arxiv-2605-23590 — "so the rank-correlation signal drives learning and the shaping terms only refine how the"
[^l10]: doi-10-48550-arxiv-2605-23590 — "our objective optimizes a list-wise Spearman rank-correlation reward"
[^l11]: doi-10-48550-arxiv-2605-23590 — "switching listwise to pairwise GRPO degrades performance"
[^l12]: doi-10-48550-arxiv-2605-23590 — "a random ranking gets 0.5 in expectation, and perfect agreement gets 1"
[^l13]: doi-10-48550-arxiv-2605-23590 — "optimization provides richer gradient signals across full rankings"
