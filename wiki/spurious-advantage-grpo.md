---
description: "GRPO's advantage magnitude depends only on the in-group correct and wrong counts, so a guessed correct answer gets the same weight as a reasoned one, most where answer sets are small."
aliases: ["spurious advantage", "guess-driven advantage component"]
sources: ["doi-10-48550-arxiv-2609-04063"]
---
# Spurious advantage in GRPO

GRPO standardises each rollout's verifier reward within its group of G rollouts. For a binary reward, the per-rollout advantage comes from within-group statistics alone, so the magnitude a correct rollout receives is set by the group's correct and wrong counts, n+ and n−.[^c1] The magnitude is "a function of (n+ , n− ) alone".[^c2] The estimator therefore does not separate a correct rollout that reasoned its way to the answer from one that guessed it.[^c3]

The work's argument is about what those counts contain. Split the per-prompt success probability pq into the part that comes from reasoning, pr, and the part that comes from any other route, pg, so that pq = pr + (1 − pr)·pg. The count n+ is Binomial(G, pq), so its expectation carries both components.[^c4] The extra push that a rare correct rollout receives in an imbalanced group is then a reasoning signal plus a term driven by pg. The work calls that second term the spurious advantage.[^c5]

The size of the term follows pg. When pg is near zero the term vanishes, which the work says holds for open-answer mathematics.[^c6] It becomes sizeable when pg is not small.[^c7]

A note on the magnitude. The extracted text drops a square root from the paper's Eq. (5). The paper's own example (G = 16, n+ = 1, n− = 15) gives a magnitude of 3.87, which is √15, so the magnitude is √(n−/n+). This reading is mine, checked against the 3.87 figure.

## Three cases where pg is large

**Bounded answer sets.** With k options and a policy that picks one at random, pg ≈ 1/k. For four options and G = 16, a policy with no reasoning at all gives a baseline of four correct rollouts.[^c8] A group with one correct rollout sits below that baseline, yet the rollout gets the magnitude √15 ≈ 3.87 "even though the verifier reward is the same."[^c9] Under the work's Eq. (7), the share of that magnitude that reflects reasoning is pr/(pr + (1 − pr)/k), which the work says "is small whenever pr is comparable to or below 1/k."[^c10]

**Open-answer sets with bounded sub-cases.** A nominally open-answer training set can contain a large closed-form part. The work sorts MATH-7.5K into 11 answer-shape categories and finds that five of them, covering "55.95% of MATH-7.5K, indicating that even an" open-answer benchmark, have a closed answer form.[^c11] Those problems give pg a non-trivial value even though the benchmark looks open.

**Multi-turn search agents.** With outcome-only reward, trajectories with different numbers of turns and different searches can end on the same correct answer. The magnitude formula "assigns the identical magnitude" to all of them.[^c12] Many of these paths "involve redundant or invalid" searches that still count as correct.[^c13] Here pg includes the probability of reaching the correct answer by any trajectory, which the work says "can be sizeable when B is not small, since the space of" trajectories grows with the search budget B.[^c14]

## Clipping does not remove it

The PPO-style clip in the surrogate bounds the importance ratio, not the advantage magnitude. "the PPO-style clip in Eq. (2) bounds the" ratio, and the work's reading is that the clip therefore hardly removes the per-rollout amplification it describes. In the common early-update case the importance ratio is close to 1, so the full magnitude enters the gradient.[^c15]

## Evidence

The work runs the same comparison with the advantage as the only controlled variable. Its variant, which drops the dependence on the count mix, "beats it on bounded-answer math at both 0.5B and" 3B.[^c16] That is evidence that the count-dependent magnitude matters on its benchmarks. It is not a direct measurement of how much of the gradient is spurious.

## Limits

- The split pq = pr + (1 − pr)·pg is a model. For bounded sets pg rests on an answer-space argument and a uniform-guess assumption (see [[guess-share-of-correct-rollouts]]). For search agents pg is not measured; the work only says the term "can be sizeable".[^c14]
- A policy that guesses non-uniformly, for instance by favouring popular answer strings, sits outside the uniform-guess calculation.
- The work says it "ha[s] not yet quantitatively measured the resulting" growth in reasoning ability.[^c17] So the paper shows accuracy differences on its benchmarks, not that the policy reasons better.
- Experiments use Qwen2.5 models at 0.5B, 3B and 7B on MATH-7.5K and a Search-R1-style QA setup. In the parts I read I did not find multi-seed variance for the main comparison.
- The claim that tool selection from a finite library suffers the same problem is the work's conjecture: "canonical GRPO may likewise suffer".[^c18] It is untested.

## Related

- [[distractor-strength-reward-signal]] — on the reward side, weak distractors let a multiple-choice question be solved by guessing. Here the reward is already right; the problem is how the estimator weights a guessed success.
- [[process-outcome-consistency-verification]] — a "lucky guess" also appears there, but as a verifier error: a correct final answer reached by a wrong derivation gets reward. This note concerns what happens after a correct reward is given.
- [[hop-grouped-advantage-baseline]] — also changes GRPO's group statistics, but to reduce the cost and variance of proposer rewards, not to remove guessing.

[^c1]: doi-10-48550-arxiv-2609-04063 — "The per-rollout advantage is computed by"
[^c2]: doi-10-48550-arxiv-2609-04063 — "to any rollout is thus a function of (n+ , n− ) alone"
[^c3]: doi-10-48550-arxiv-2609-04063 — "not distinguish the two."
[^c4]: doi-10-48550-arxiv-2609-04063 — "on a count n+ whose expectation Gpq inherits both"
[^c5]: doi-10-48550-arxiv-2609-04063 — "to the latter component as the spurious advantage"
[^c6]: doi-10-48550-arxiv-2609-04063 — "When pg ≈ 0, the second term of Eq. (6) vanishes and the spurious advantage is small."
[^c7]: doi-10-48550-arxiv-2609-04063 — "The spurious advantage becomes sizeable when pg is not small;"
[^c8]: doi-10-48550-arxiv-2609-04063 — "gives a baseline expectation of G · pg = 4 correct"
[^c9]: doi-10-48550-arxiv-2609-04063 — "even though the verifier reward is the same."
[^c10]: doi-10-48550-arxiv-2609-04063 — "which is small whenever pr is comparable to or"
[^c11]: doi-10-48550-arxiv-2609-04063 — "55.95% of MATH-7.5K, indicating that even an"
[^c12]: doi-10-48550-arxiv-2609-04063 — "assigns the identical magnitude"
[^c13]: doi-10-48550-arxiv-2609-04063 — "many of these paths involve redundant or invalid"
[^c14]: doi-10-48550-arxiv-2609-04063 — "sizeable when B is not small, since the space of"
[^c15]: doi-10-48550-arxiv-2609-04063 — "removes the per-rollout amplification we describe,"
[^c16]: doi-10-48550-arxiv-2609-04063 — "beats it on bounded-answer math at both 0.5B and"
[^c17]: doi-10-48550-arxiv-2609-04063 — "have not yet quantitatively measured the resulting"
[^c18]: doi-10-48550-arxiv-2609-04063 — "canonical GRPO may likewise suffer"
