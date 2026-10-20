---
description: "Training questions are sorted by the semantic entropy of the starting policy's sampled answers, low to high, so RL meets low-dispersion questions first and high-dispersion ones later."
aliases: ["semantic entropy curriculum", "SE curriculum", "entropy-ordered curriculum", "semantic-entropy-guided curriculum learning"]
sources: ["arxiv-2512-04359"]
---
# Semantic entropy curriculum

A curriculum orders the training set before training begins. The difficulty of each question is read off the policy's own answers: sample several responses to the question, group the responses by the answer they reach, and take the entropy over those groups. A question whose samples all agree scores low; one whose samples scatter over many answers scores high. The paper's reading of the score is that "queries with high semantic entropy exhibit diverse solution distributions and require more exploration."[^k1]

The procedure has three steps. First, "Before training, we compute the semantic entropy" for each query, using the initial policy, which is typically the SFT model.[^k2] Second, "we sort the training dataset in ascending order of" that score.[^k3] Third, the sorted data is cut into stages and trained in turn: "we divide the sorted dataset into N curriculum stages and train the policy progressively."[^k4] Low-entropy questions come first because they are "easier problems with more consistent solutions".[^k5]

For tasks with a checkable final answer, the equivalence used to group responses is answer identity: "two responses oi and oj are semantically equivalent if they yield the same final answer."[^k6] The score is then the entropy over the distribution of final answers, which is the general semantic-entropy measure of [[semantic-entropy]] with answer identity in place of entailment. The paper's stated purpose for the ordering is that it "prevents the model from encountering overly challenging problems prematurely."[^k7]

The paper reports the effect as an ablation: "integrating curriculum learning yields substantial performance gains on the Avg@16 metric relative to GRPO."[^k8] The ablation compares GRPO, GRPO with the curriculum, and configurations with token-level constraints, with and without the curriculum. The paper says that adding the curriculum to the token-level method "yields additional performance gains, particularly evident in average performance metrics."[^k11]

Set against [[rollout-dispersion-curriculum]], which reweights prompt groups inside each update, this is a static sort done once before training. My inference: the two use related signals (how much a question's answers disperse), but one fixes the order of the data and the other re-weights the gradient at every step.

## Limits

- The paper's score is measured on the starting policy. How the ordering should change as the policy changes is left open; the paper's own stated next step is to "explore adaptive curriculum strategies that can dynamically adjust difficulty progression based on real-time learning signals."[^k9]
- The paper says the effect "depends on the quality of entropy estimation, which may vary across different types of reasoning tasks."[^k10] The estimate uses a finite number of sampled responses per query, so a question with few samples can be mis-ranked (my inference).
- The score is the model's own answer dispersion. A policy that is consistently and confidently wrong on a question scores low, so the curriculum would schedule it early as an easy question. This is the failure mode [[semantic-entropy]] already names for its own use; the curriculum inherits it (my inference).
- I found no run in the parts I read that compares the low-to-high order with a random or reversed order. The ablation shows the curriculum added to GRPO, not the order's contribution on its own.
- The number of stages N is set by the paper and analysed in a section I did not read, so the sensitivity to N is not part of what I can report.
- The evidence is on mathematical reasoning benchmarks with verifiable answers. The paper names other domains as future work; they were not tested.

## Related

- [[semantic-entropy]] — the measure itself; here it is taken over the training policy's answer classes, per query
- [[rollout-dispersion-curriculum]] — a per-step weight on prompt groups by solution dispersion, where this note is a one-off sort
- [[rlvr-entropy-collapse]] — the collapse this ordering is meant to slow, from the data side
- [[entropy-covariance-token-selection]] — the token-level half of the same method

[^k1]: arxiv-2512-04359 — "queries with high semantic entropy exhibit diverse solution distributions and require more exploration"
[^k2]: arxiv-2512-04359 — "Before training, we compute the semantic entropy"
[^k3]: arxiv-2512-04359 — "we sort the training dataset in ascending order of"
[^k4]: arxiv-2512-04359 — "we divide the sorted dataset into N curriculum stages and train the policy progressively."
[^k5]: arxiv-2512-04359 — "easier problems with more consistent solutions"
[^k6]: arxiv-2512-04359 — "two responses oi and oj are semantically equivalent if they yield the same final answer"
[^k7]: arxiv-2512-04359 — "This curriculum design prevents the model from encountering overly challenging problems prematurely"
[^k8]: arxiv-2512-04359 — "integrating curriculum learning yields substantial performance gains on the Avg@16 metric"
[^k9]: arxiv-2512-04359 — "explore adaptive curriculum strategies that can dynamically adjust difficulty progression based on real-time learning signals"
[^k10]: arxiv-2512-04359 — "depends on the quality of entropy estimation, which may vary across different types of reasoning tasks"
[^k11]: arxiv-2512-04359 — "yields additional performance gains, particularly evident in average performance metrics"
