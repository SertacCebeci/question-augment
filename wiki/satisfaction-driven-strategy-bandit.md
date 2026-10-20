---
description: "A contextual bandit picks how to answer each query (direct or chain-of-thought, tool, domain) and learns the choice from thumbs-up or thumbs-down alone, with no labelled answers."
aliases: ["contextual Thompson sampling for strategy selection", "contextual bandit answer-strategy selection", "feedback-driven agent strategy routing"]
sources: ["arxiv-2512-03065"]
---
# Satisfaction-driven strategy bandit

The answering agent is treated as a set of choices, and the only teacher is the user's satisfaction signal. Each query is mapped to a small feature vector, a contextual bandit selects one option from a fixed set, the user rates the reply up or down, and the rating updates the bandit. The paper uses three kinds of choice. The first is generation strategy: "The first optimization target focuses on selecting the appropriate reasoning strategy for response generation", either a direct answer or step-by-step reasoning.[^c1] The second is tool use, where "The tool selection problem presents greater complexity than strategy selection for several" reasons.[^c2] The third is domain routing to a specialist, where "Domain routing proves particularly important in life sciences because specialized knowledge" changes response quality.[^c3]

The mechanism is simple. The query becomes a feature vector: counts of complexity keywords ("how", "why", "explain"), counts of domain keywords, and a length term. The keyword sets "are complexity keywords" and domain keywords, so the features are surface cues, not semantic judgements.[^c4] Each action keeps a Beta posterior over success, built from "Thompson Sampling with Beta-Bernoulli conjugate priors".[^c5] A thumbs-up is reward 1 and a thumbs-down is reward 0, the binary form the paper uses in its experiments.[^c6] The learning rule is what the paper sells: "learn optimal decision-making strategies from user feedback alone" is the stated aim, with no ground-truth answers needed.[^c7] Thompson sampling supplies the exploration: "Thompson Sampling achieves automatic exploration through stochastic sampling", so an action is tried in proportion to its chance of being best and no separate exploration parameter is tuned.[^c21]

What was measured. Over 30 queries the paper reports a success rate, meaning the share of positive ratings, of "The contextual bandit achieves an average success rate of 76.7% compared to the" random baseline's 49.0%.[^c8] The text calls this "statistically significant and practically meaningful"[^c9], but names no test. Learning speed is reported as "requiring approximately 18 queries on average to reach the 70% success rate threshold".[^c10] The learned policy is reported per query type, with the text stating: "Use direct answers for simple queries (85% vs. 50% random)".[^c13] The analysis credits the complexity keywords most: "The complexity score emerges as the dominant feature for strategy selection".[^c14]

## Limits

The reward is coarse and noisy, and the paper says so. "The coarse granularity cannot distinguish between responses that are merely adequate and those that are excellent."[^c15] Users give feedback unevenly and not neutrally: the paper notes "bias in their feedback patterns, being more likely to provide negative feedback than positive".[^c16] Its own proposed fixes, implicit signals and composite rewards, are described but not evaluated in the text I read.

The baseline is weak. Random selection sits near 50% because the reward is a coin-flip base rate: the paper says the figure "aligns with our binary reward structure where approximately half of responses receive positive feedback".[^c17] So the 27.7-point gain is a gain over a policy that ignores the query, not over a fixed strategy or a rule-based router. The paper defines a fixed-strategy baseline in its experimental setup, but the tables I read do not report it. The abstract's "15-30%" range is also not the Table 1 figures, which are 23 to 33 percent per mode; my reading is that the two summaries use different measures, and the text does not say which.

The text does not say how the 30-query runs obtained their ratings: whether real users, a simulator, or a fixed labelled set produced the thumbs. That matters, because the no-labels claim concerns the learning rule and not the evaluation's feedback source. This is my inference from the text, not a finding of the paper.

The regret statement is asserted rather than derived. "Cumulative regret grows sublinearly, indicating effective learning"[^c11], and it is said to match "the theoretical bound for contextual bandits with linear reward models".[^c12] The bound is cited, not worked out for this algorithm. My reading is that the contextual step in the algorithm (context-weighted counts, α transposed times x) is a heuristic rather than a posterior derived from a stated model, so the cited bound does not transfer automatically. Guarantees of this kind are averages over many periods and say nothing about one run; see [[thompson-sampling]].

The features are weak. "Simple keyword matching misses semantic nuances".[^c18] Preferences are assumed to be stable enough for the posterior to settle, yet the paper concedes "User preferences may change over time"[^c19]; its remedy, a sliding window, is sketched, not tested in the slices I read. The cold start is handled by an optimistic prior "to slightly favor exploration"[^c20] and a keyword rule for the first five queries, so the earliest answers are not bandit choices at all.

Scope. The domain is life-science queries, and the action set is five-by-five-by-two. The paper itself notes that a joint action space would grow to about 50 and need "more sophisticated exploration strategies". Nothing here shows the approach at that size, or outside a single domain.

## Related

- [[thompson-sampling]] — the algorithm used; its regret guarantees are averages over the prior and do not describe a single run, which is the caveat for the regret claim above.
- [[complexity-tiered-strategy-routing]] — also a per-query choice of reasoning strategy, but trained as a reinforcement-learning policy on outcome rewards, with a tier scale instead of a bandit over fixed options.
- [[fable-execution-policy]] — another linear contextual bandit choosing an action, here in an execution setting rather than for answer strategy.

[^c1]: arxiv-2512-03065 — "The first optimization target focuses on selecting the appropriate reasoning strategy for response generation"
[^c2]: arxiv-2512-03065 — "The tool selection problem presents greater complexity than strategy selection for several"
[^c3]: arxiv-2512-03065 — "Domain routing proves particularly important in life sciences because specialized knowledge"
[^c4]: arxiv-2512-03065 — "are complexity keywords"
[^c5]: arxiv-2512-03065 — "We use Thompson Sampling with Beta-Bernoulli conjugate priors"
[^c6]: arxiv-2512-03065 — "we employ a simple binary reward based on explicit user"
[^c7]: arxiv-2512-03065 — "learn optimal decision-making strategies from user feedback alone"
[^c8]: arxiv-2512-03065 — "The contextual bandit achieves an average success rate of 76.7% compared to the"
[^c9]: arxiv-2512-03065 — "This improvement is statistically significant and practically meaningful"
[^c10]: arxiv-2512-03065 — "requiring approximately 18 queries on average to reach the 70% success rate threshold"
[^c11]: arxiv-2512-03065 — "Cumulative regret grows sublinearly, indicating effective learning"
[^c12]: arxiv-2512-03065 — "This matches the theoretical bound for contextual bandits with linear reward models"
[^c13]: arxiv-2512-03065 — "Use direct answers for simple queries (85% vs. 50% random)"
[^c14]: arxiv-2512-03065 — "The complexity score emerges as the dominant feature for strategy selection"
[^c15]: arxiv-2512-03065 — "The coarse granularity cannot distinguish between responses that are merely adequate and those that are excellent"
[^c16]: arxiv-2512-03065 — "bias in their feedback patterns, being more likely to provide negative feedback than positive"
[^c17]: arxiv-2512-03065 — "binary reward structure where approximately half of responses receive positive feedback"
[^c18]: arxiv-2512-03065 — "Simple keyword matching misses semantic nuances"
[^c19]: arxiv-2512-03065 — "User preferences may change over time"
[^c20]: arxiv-2512-03065 — "Initialize α0 = 2, β0 = 1 to slightly favor exploration"
[^c21]: arxiv-2512-03065 — "Thompson Sampling achieves automatic exploration through stochastic sampling"
