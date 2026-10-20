---
description: "A label's noise is a joint function of labeler accuracy and the sample's model entropy, rising with ambiguity even for accurate labelers; accuracy alone misstates it."
aliases: ["entropy-dependent label noise", "ambiguity-dependent annotation noise", "noise as a function of labeler accuracy and entropy"]
sources: ["arxiv-2512-12870"]
---
# Uncertainty-dependent label noise

A label returned by a labeler is wrong with some probability: its noise. The common bookkeeping takes that probability to be one minus the labeler's accuracy, so a labeler who is right 90 % of the time puts 10 % noise on every item. The OLAS paper separates the two. Accuracy a is "the probability of correctly labeling" a sample,[^u1] while the noise an actual label carries is a function ε(a, e) of that accuracy and of e, the entropy of the sample under the current classifier. The entropy is computed from the model's class probabilities (its Equation 1), and for more than two classes "entropy values are bounded to [0, 1] before being passed to the noise" function.[^u2]

The two monotonicity conditions define the object. Noise must fall as labeler accuracy rises and must rise with sample entropy. The paper asks only for these two properties: "it must be monotonically decreasing in the labeler accuracy a" and increasing in e.[^u5] The entropy half rests on a link cited from the uncertainty literature: samples with higher entropy "are more likely to receive incorrect labels from oracles".[^u3] The consequence is stated in one line: a reliable labeler "can still generate substantial noise on a highly ambiguous sample".[^u4] Take a labeler of accuracy 0.95 and a point the model cannot classify. Its single accuracy number does not carry the risk of that label; the risk belongs to the pair, labeler and sample, not to the labeler alone. (The 0.95 is my illustration, not the paper's.)

The noise enters the selection step as a ceiling. The joint model admits a sample to a labeler only when the noise is under a bound β, and the paper says β "controls the trade-off between sample informativeness and label quality".[^u9] So the noise function does more than diagnose a label after the fact; it decides which uncertainty is affordable from which labeler, which is the question [[worst-case-noise-labeler-assignment]] answers once the sample is chosen.

The framework does not depend on one shape for the function. The paper states that "the optimization framework and its closedform solutions hold for any noise function satisfying the two monotonicity conditions".[^u8] Its real-data check does not impose a shape: the noise is fitted as a classification task, "with two features", entropy and labeler accuracy, against a binary target of whether the label was correct.[^u6] On a crowdsourced music-genre dataset the fitted surface "is visibly decreasing in worker accuracy and increasing in sample entropy".[^u7]

For the asker's side, the transferable point is about what a question's answer will be worth. (My inference, not the paper's claim.) The most uncertain item is also the one whose answer is most likely to be mis-given, so "ask where I am least sure" and "ask where the answer will be reliable" pull apart. The paper does not test this for questions put to people or models; it is about labels.

## Limits

- The functional form is a simulation choice. The paper's first noise model is "a simple bilinear function in which noise increases linearly with sample entropy and decreases linearly with labeler accuracy".[^u10] The second is described as a stress test. Neither is derived from a labeling process.
- Most of the evidence uses labels drawn from the noise model itself. The one check on human labels is a single crowdsourced dataset, and it fits the surface rather than measuring a mechanism.
- The entropy is recomputed every cycle from the current model: it is "evaluated in each cycle of AL".[^u11] So the noise a sample carries moves as training proceeds. The paper does not measure how well an early, poor model's entropy predicts the noise.
- The reason uncertain samples are noisier is cited to Du and Ling (2010), not tested here. The paper needs only the monotone direction, and the note does not claim more.
- The accuracies must be known or estimated; "labeler reliability is typically unknown and must be estimated from data".[^u12]

## Related

- [[worst-case-noise-labeler-assignment]] — the assignment rule that uses this noise to decide which labeler sees which sample
- [[noise-seeking-uncertainty-sampling]] — the same uncertain points a query rule prefers; there the cost is labels spent where a mistake is cheap, here the same points carry the noisiest labels
- [[massart-tsybakov-noise]] — sample-dependent label flip rates in classical theory; there the noise is tied to the true conditional probability, not to a fitted model's entropy (my reading)
- [[abstention]] — refusing a query at a named cost is another way to keep high-noise points out of the label budget

[^u1]: arxiv-2512-12870 — "The accuracy of a labeler is defined as the probability of correctly labeling"
[^u2]: arxiv-2512-12870 — "entropy values are bounded to [0, 1] before being passed to the noise"
[^u3]: arxiv-2512-12870 — "are more likely to receive incorrect labels from oracles"
[^u4]: arxiv-2512-12870 — "can still generate substantial noise on a highly ambiguous sample"
[^u5]: arxiv-2512-12870 — "it must be monotonically decreasing in the labeler accuracy a"
[^u6]: arxiv-2512-12870 — "This problem can be framed as a simple classification task with two features"
[^u7]: arxiv-2512-12870 — "is visibly decreasing in worker accuracy and increasing in sample entropy"
[^u8]: arxiv-2512-12870 — "hold for any noise function satisfying the two monotonicity conditions"
[^u9]: arxiv-2512-12870 — "It controls the trade-off between sample informativeness and label quality"
[^u10]: arxiv-2512-12870 — "Noise Model 1 is a simple bilinear function in which noise increases linearly with sample entropy and decreases linearly with labeler accuracy"
[^u11]: arxiv-2512-12870 — "evaluated in each cycle of AL"
[^u12]: arxiv-2512-12870 — "labeler reliability is typically unknown and must be estimated from data"
