---
description: "Per-topic Beta posteriors over whether a generated question lands near the solver's capability boundary, sampled by Thompson sampling, steer a self-play question generator to learnable topics."
aliases: ["posterior-guided tree exploration", "learnability-guided curriculum", "difficulty-shaped challenger reward"]
sources: ["arxiv-2603-22352"]
---
# Learnability-posterior curriculum

In a self-play loop where one model both writes questions (Challenger) and answers them (Solver), the open problem is which topic to generate questions about next. WIST answers it by keeping, for every node of a domain tree, a Beta posterior over a single quantity: the probability that sampling that subtree yields a learnable training instance.[^c1]

## Mechanism

**Learnability as a Bernoulli event.** For each valid generated question the Solver answers K times; the empirical accuracy p̂ gives a variance p̂(1−p̂). A question counts as learnable (g = 1) when that variance reaches a threshold. In the paper's words, g = 1 means the question is likely near the current boundary and so training-effective, while g = 0 means too easy, too hard, or unreliable.[^c2] The variance is zero when all answers agree, so both trivially easy and hopeless questions score zero. Documents where every question has zero variance are skipped for policy updates.

**Difficulty-shaped Challenger reward.** The question writer is itself rewarded with a Gaussian bump on that variance, centred at 0.25 (p̂ = 0.5), so it is paid for questions of moderate difficulty and penalized (ρ < 0) for malformed or unverifiable ones.[^c3] This is the same boundary-seeking idea as the g signal, used as a reward instead of a routing statistic.

**Posterior update along the path.** The observation g is credited to every node on the sampled root-to-leaf path with a Beta–Bernoulli conjugate update. Next path selection runs [[thompson-sampling]] at each depth: draw a score from each child's posterior and take the largest, which trades off exploiting high-learnability regions against exploring uncertain ones.[^c4]

**Sliding window.** Because learnability changes as the policy improves, accumulating statistics over the full history would bias exploration toward early observations; the paper uses only the most recent µ observations per node (µ = 5 in the experiments) to form the sampling parameters.[^c5] This is a departure from the stationary-reward assumption of textbook Thompson sampling.

**Tree growth.** A special "unk" child lets sampling trigger creation of a new sibling subtopic, so the topic space is not enumerated in advance; non-leaf expansions are checked against Wikipedia titles to suppress hallucinated concepts.

## What was measured

In a 50-step run on Qwen3-4B-Base in mathematics, posterior-guided ("reward") exploration and uniformly random exploration performed similarly early and then diverged, with the guided variant giving a more stable trajectory and better final performance.[^c6] The authors read this as evidence that unguided expansion disperses effort across the enlarged search space, and that the gain comes from directing exploration, not merely from broader exploration. The same ordering is reported in medicine across model sizes. The whole system (with web-grounding and the tree) raised the Overall score of Qwen3-4B-Base from 33.3 to 43.1, against 40.6 for R-Zero and 41.8 for SPICE; these full-system numbers do not isolate the curriculum's share.[^c7]

## Limits

- The ablation compares guided against uniform-random expansion only; it does not compare against a flat (treeless) bandit, a fixed easy-to-hard schedule, or a non-Thompson rule, so the specific value of Beta posteriors is not isolated.
- Learnability is defined by a Solver-variance threshold from K samples; with small K the variance is noisy, and the paper does not report sensitivity to K as a source of mislabeling (my observation).
- The signal measures solver-side learnability, not whether the question is correct or useful; unverifiable items are handled by a rule-based validator, and answer correctness is checked against the Challenger's own reference answer.
- Results are for verifiable-answer math, general reasoning and a few science benchmarks; nothing here concerns open-ended or clarifying questions.
- On the smaller OctoThinker-3B the full system scored slightly below SPICE (24.5 vs 25.2), which the authors attribute to noisy open-web content for a weaker model.[^c8]
- Attributing one outcome to every node on a path is a credit-assignment simplification; internal nodes share credit regardless of which one caused the signal (my inference).

## Related

- [[thompson-sampling]] — the selection rule; here run with windowed, non-stationary posteriors
- [[pretraining-grounded-rubric-self-play]] — another self-play loop whose questions are grounded in an external corpus
- [[scenario-curriculum-rl]] — curriculum over generated scenarios for RL
- [[question-generation-as-policy]] — treating the question writer as a trained policy
- [[forgetting-factor-beta-bernoulli]] — the discounted alternative to the window: past observations decay by a factor γ rather than being dropped after µ

[^c1]: arxiv-2603-22352 — "where M(Di,j ) represents the node-wise learnability, i.e. the probability that sampling the subtree"
[^c2]: arxiv-2603-22352 — "g = 1 indicates that the QA is likely near the current boundary and thus training-effective, whereas"
[^c3]: arxiv-2603-22352 — "We assign a difficulty-shaped reward based on"
[^c4]: arxiv-2603-22352 — "We use Thompson sampling for path selection."
[^c5]: arxiv-2603-22352 — "Because learnability is non-stationary as the policy"
[^c6]: arxiv-2603-22352 — "Reward-guided exploration yields a"
[^c7]: arxiv-2603-22352 — "outperforming R-Zero (40.6)"
[^c8]: arxiv-2603-22352 — "WIST achieves an Overall score of 24.5, slightly below SPICE’s 25.2"
