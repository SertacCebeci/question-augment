---
description: "With no simulator, the outcome of the next question can be sampled from similarity-weighted past cases, and an ensemble of tree searches picks which test to run or whether to stop."
aliases: ["IBMDP", "Implicit Bayesian Markov Decision Process", "case-guided planning", "analog-guided sequential experiment selection"]
sources: ["arxiv-2601-14710"]
---
# Case-guided sequential assay planning

The problem: choose which costly test (an assay) to run next, or stop, when no model of how outcomes follow actions exists and only a static table of past cases is available. The work's answer is a planner that builds its transition model from the cases themselves.[^c1]

## Mechanism

At each step a categorical distribution is formed over historical records, using a variance-normalized distance kernel. Plausible outcomes of an assay are sampled from it, conditioned on the partial evidence already observed for the current candidate.[^c2] Because the weights depend on what has been observed so far, the implicit dynamics shift as evidence accumulates: the belief is non-stationary but derived from static data.[^c3]

Planning over this sampler uses Monte Carlo Tree Search with double progressive widening. Several planners are run and majority-voted, giving a "Maximum-Likelihood Action-Sets Path" that is stable across uncertainty levels.[^c4] The stopping logic is explicit: a sequence ends when posterior entropy on the target is at most a threshold and the likelihood of the desired outcome is at least a threshold.[^c5] The next assay is recommended only if the expected uncertainty reduction toward the desirable state is large enough, which ties the question to cost-weighted information gain (see [[expected-information-gain]] and [[value-of-information]]).

## What was measured

In a brain-penetration task with 220 fully measured historical compounds, a cheap in vitro assay cost $400 and the decisive in vivo assay $4,000. The conventional full panel cost $5,200.[^c6] Over four representative compounds the planner reached the same or higher decision confidence with up to a 92% cut in resource use.[^c7] It also caught a case where a rule-based QSAR heuristic would have wrongly discarded a good compound.

On a synthetic benchmark with a computable optimal policy, over 100 trials the ensemble's top action matched the optimum 47% of the time, and the top two covered it 66%. The deterministic value-iteration variant on the same similarity model matched 36%.[^c8] The authors attribute the gap to ensembles surfacing several near-equivalent actions, where deterministic planning commits to one. That attribution is theirs, not isolated by an ablation.

## Limits

- The authors state that the method "trades formal convergence guarantees for practical applicability."[^c9]
- The real-world evidence is four hand-picked scenarios from one task and 220 compounds; resource savings are compared with a simple rule heuristic, not another planner.
- Top-1 agreement with the optimum is under 50%; the claim is relative to one baseline, in a synthetic setting.
- Whether the similarity kernel stays reliable when the new case lies outside the historical distribution is not shown.
- It is a planning method for experiments, not a study of human or LLM questioners; the transfer to question-asking is my inference.

## Related

- [[expected-information-gain]] — the uncertainty-reduction quantity the planner trades against cost
- [[value-of-information]] — the stop-or-continue decision is a value-of-information decision
- [[bayesian-experimental-design]] — the simulator-based counterpart this approach replaces
- [[amortised-sequential-information-gathering]] — another sequential selector of the next query

[^c1]: arxiv-2601-14710 — "planning must rely solely on a static database of historical"
[^c2]: arxiv-2601-14710 — "forms a categorical distribution over historical compound records using a variance-normalized distance kernel"
[^c3]: arxiv-2601-14710 — "non-stationary but principled state transitions from static historical data"
[^c4]: arxiv-2601-14710 — "majority voting across runs yields a MaximumLikelihood Action-Sets Path (MLASP) that is stable across uncertainty levels"
[^c5]: arxiv-2601-14710 — "An experimental sequence terminates when the planner reaches a state of sufficient confidence"
[^c6]: arxiv-2601-14710 — "comprises N = 220 compounds with complete measurements for all relevant assays"
[^c7]: arxiv-2601-14710 — "level of decision confidence with up to 92% reduction in resource consumption."
[^c8]: arxiv-2601-14710 — "the deterministic VI-Sim approach achieved only 36% alignment"
[^c9]: arxiv-2601-14710 — "IBMDP trades formal convergence guarantees for practical applicability in simulator-free settings"
