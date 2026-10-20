---
description: "Asking a user to pick the best N of K options, not 1 of 2, extracts more per question from a tolerable cognitive load, until K grows large enough that the user's picks turn unreliable."
aliases: ["N-out-of-K preferential feedback", "multiwise preference query", "multi-choice preferential Bayesian optimization"]
sources: ["arxiv-2602-02388", "doi-10-48550-arxiv-2205-13743"]
---
# Multi-choice preference query

**Setting.** A user holds a target in mind that language cannot specify (an image x*). A system can only learn about it by showing candidates and asking which is closer. The paper, MultiBO, treats the user's satisfaction as an unknown black-box function and asks the user for comparative judgments, not scores.

**Why comparisons, not ratings.** Numeric feedback is hard for people, who cannot quantify how much worse a candidate is than the target, while ranking is easy: "it is easier to express preferences between pairs or sets of K images".[^c1]

**Why more than two options.** A pairwise answer is thin evidence. In the pairwise Gaussian-process model, "An observed pair only provides information about" the function over two halves of the input space, so many answers are needed, and more as dimensionality grows.[^c2] Showing K candidates and letting the user choose N of them means each answer constrains the function over K partitions of the space. The authors model a pick as a multinomial-probit categorical likelihood. That likelihood has no closed form, so they approximate it as Chu and Ghahramani did for the pairwise case, and they redesign the acquisition function for it.[^c3] The claim is that the richer answer costs only "slight increase in user's cognitive load".[^c4]

**Measured effect.** In an ablation with the same budget of 50 feedback steps, the pairwise version "requires far more preference" feedback to model the function and find the optimum.[^c5] On target-based metrics, pairwise scored CLIP-I 0.81 and LPIPS 0.68. Multiwise scored CLIP-I 0.94 and LPIPS 0.55 (higher CLIP-I and lower LPIPS are closer to the target).[^c6] In a 30-volunteer evaluation, the full method won 70.82% of top-ranked comparisons against reward-model and training-free baselines, with Kendall's W of 0.65 for agreement.[^c7]

**The ceiling on K.** More options do not keep helping. Reliability of the user's preference drops as the choice set grows, and K = 10 gave worse metrics (LPIPS 0.64) than K = 4 (0.55). K = 6 (0.54) gave only marginal gains, out of proportion to the burden.[^c8] So the answer-side cost of a question is not only effort but accuracy: past some set size the answer itself degrades.

**Reading for question design (my inference, not the paper's claim).** The unit of a good question here is the information per answer a person can still give accurately. The sweet spot is a small set (about 4), found empirically for one task.

**Same direction, in a simulated recourse setting.** Personalised algorithmic recourse asks a simulated user to pick one intervention from a set, with sets of 2 or 4. "regret, irrespective of the response model, with the downside of increasing the cognitive burden for the user" describes the same trade: larger sets lowered regret and raised burden.[^c9] The burden is asserted, not measured, and the users are simulated, so this supports the direction of the trade-off, not the position of the sweet spot. The scoring rule behind such sets is in [[expected-utility-of-selection]].

## Limits

- One task (personalized image generation), one human-evaluated pool of 30 volunteers who rate final outputs, with targets chosen by a human. K = 4 as the optimum comes from a few settings of one system, not a general law.
- The ablation fixes budget in number of rounds, not in user time or effort. The paper does not measure whether picking N of K costs more per round than a pair, beyond asserting it is slight.
- The gains also bundle other design choices (low-dimensional attention-space optimization), so the pairwise-versus-multiwise comparison is the only clean isolate of the question format.
- The table's numbers are for few seeds and the paper does not report intervals; the K = 4 vs 6 difference is within what noise could produce.
- Users wait between rounds; the paper assumes this is tolerable.

## Related

- [[elicitation-protocols]] — a general account of how a system asks; this is one concrete query format with a measured information-versus-reliability tradeoff.
- [[pairwise-query-selective-classification]] — pairwise queries as the baseline format this note argues is information-poor.
- [[qeubo]] — another preferential Bayesian-optimization query design that picks comparisons by expected value of information.

[^c1]: arxiv-2602-02388 — "However, it is easier to express preferences between"
[^c2]: arxiv-2602-02388 — "An observed pair only provides information about"
[^c3]: arxiv-2602-02388 — "Picking choice ai out of {ai }j∈Zi , i = 1, . . . , M is"
[^c4]: arxiv-2602-02388 — "slight increase in user’s cognitive load of selecting N -outof-K images instead of 1-out-of-2."
[^c5]: arxiv-2602-02388 — "illustrate that PairwiseGPR requires far more preference"
[^c6]: arxiv-2602-02388 — "Table 3. PairwiseGPR vs MultiwiseGPR performance on"
[^c7]: arxiv-2602-02388 — "Kendall’s W = 0.65 indicates strong inter-rater"
[^c8]: arxiv-2602-02388 — "choices increases, the reliability of user preference drops as"
[^c9]: doi-10-48550-arxiv-2205-13743 — "regret, irrespective of the response model, with the downside of increasing the cognitive burden for the user"
