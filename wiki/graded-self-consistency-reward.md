---
description: "A solver's self-reward graded by the share of its own samples that agree, instead of a bonus only at majority, keeps a learning signal when answers split."
aliases: ["continuous self-consistency reward", "agreement-proportional reward", "continuous self-consistency signal"]
sources: ["arxiv-2511-16672"]
---
# Graded self-consistency reward

A solver is sampled several times on the same question, and each sample is rewarded from the other samples. A discrete version of this reward is a function of the majority count, so a split vote earns little or nothing. The graded version scales each sample's reward with how much of the sample set agrees with it. In EvoLMM each Solver sample $y_i$ is rewarded by its empirical agreement share $p(y_i \mid x, q)$, multiplied by a brevity factor that is 1 minus a length weight times $\max\{0, (w_i-\tau)/\tau\}$, where $w_i$ counts the words before the answer tag. The authors' summary of the effect: "This yields dense, bounded rewards that preserve" gradient flow even without a clear majority, and the reward encourages "stable reasoning (high agreement among outputs)".[^c1]

The motivation is stated against a language-only method. SQLM, which generates its own questions and reinforces answer agreement, "relies on a discrete majority-vote reward".[^c2] The authors' claim is that on images the early Solver outputs are so variable that this reward is zero on most updates, which "prevents the model from making gradual progress". Their Figure 3 describes the discrete Solver reward as one that "increases linearly only with majority count and does not reflect partial progress".[^c3] The graded reward gives a partial split a positive value: "Even partial agreement (e.g., 2 out of 5 consistent samples) produces a meaningful positive reward" in the authors' words, and the reward is "a graded score proportional to the empirical agreement among Solver outputs".[^c4]

What the paper measured is a training-curve comparison and one table. In the training curves, "The discrete majority-vote reward (red) remains low and unstable during training".[^c5] In the table, Qwen2.5-VL-7B trained with the continuous reward is compared with the same model trained with the discrete reward and with the untrained baseline.[^c6] Reading the table layout, ChartQA goes from 84.00 (baseline) to 84.62 (discrete) to 86.70 (continuous).[^c7] On MathVista the same reading gives 68.46, 68.88 and 70.52. The difference between the two reward forms is therefore about 2.1 points on ChartQA and 1.6 on MathVista, by my arithmetic on those cells. The authors read the curves as showing that the discrete reward causes stagnation, "avoiding stagnation observed in the discrete-reward self-questioning scheme".[^c8]

What transfers from the language setting is the estimator: agreement among sampled answers, with no judge and no gold label. What is changed is only the reward's shape, from a threshold to a proportion. The reason given for the change is specific to images, where the Solver's answers vary more. Where the samples already agree, the two shapes should give nearly the same signal; that follows from the formula and is my inference, not a result the paper reports. The reward also carries a length term, and the paper describes it as a term that "gently penalizes verbosity".[^c9]

## Limits

- All the evidence is the authors' own. The comparison in the table is on one backbone family, Qwen2.5-VL-7B, with one discrete baseline. The slices I read report no seed variance, so the 1.6 to 2.1 point gap is not shown to be stable.
- The graded reward is not isolated from the brevity term. The authors do not, in what I read, run the graded agreement with the length factor removed, so the gain cannot be credited to agreement alone. This is my reading.
- The sample count is small. The figures use "responses N =5",[^c10] so agreement comes in steps of one fifth. How the graded reward behaves at larger N is not in the text I read.
- "Collapse" is argued from the curves, not measured as a collapse rate. The claim that the discrete reward stagnates rests on Figure 4.
- Agreement is agreement with the Solver's own answers. A consistent wrong answer earns the full graded reward as readily as a right one. The paper does not test this case. This is my inference, and it is the same blind spot as in [[self-consistency-difficulty-score]], where the text notes that a consistent-but-wrong solver looks stable.
- The gain is measured on visual math benchmarks. Whether a graded agreement reward helps on tasks with open answers, where agreement is hard to define, is not tested here.

## Related

- [[majority-vote-mode-certificate]] — the discrete majority vote this reward grades; the bound on that vote says how many samples a majority needs to be reliable
- [[zero-variance-group-waste]] — a binary reward that leaves a group with no signal, the same failure seen in group-relative RL
- [[consensus-reward-tilting]] — rewarding agreement with the majority under a KL penalty, a different analysis of the same vote
- [[self-consistency-difficulty-score]] — the same agreement fraction read as a difficulty measure rather than as a reward
- [[uncertainty-peaked-challenge-reward]] — the questioner-side reward built on the same vote

[^c1]: arxiv-2511-16672 — "This yields dense, bounded rewards that preserve"
[^c2]: arxiv-2511-16672 — "relies on a discrete majority-vote reward"
[^c3]: arxiv-2511-16672 — "increases linearly only with majority count and does not reflect partial progress"
[^c4]: arxiv-2511-16672 — "yields a graded score proportional to the empirical agreement among Solver outputs"
[^c5]: arxiv-2511-16672 — "remains low and unstable during training"
[^c6]: arxiv-2511-16672 — "Qwen2.5-VL-7B + Discrete Reward"
[^c7]: arxiv-2511-16672 — "86.70"
[^c8]: arxiv-2511-16672 — "avoiding stagnation observed in the discrete-reward self-questioning scheme"
[^c9]: arxiv-2511-16672 — "gently penalizes verbosity"
[^c10]: arxiv-2511-16672 — "responses N =5"
