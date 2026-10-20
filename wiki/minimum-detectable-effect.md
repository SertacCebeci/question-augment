---
description: "The smallest difference an agent evaluation can reliably separate from noise, fixed by variance, sample counts and error rates; a null result is only as informative as this resolution."
aliases: ["minimum detectable difference", "evaluation resolution", "power-based resolution", "MDE"]
sources: ["doi-10-48550-arxiv-2608-13867", "arxiv-2512-21326"]
---
# Minimum detectable effect

Before an evaluation is run, the first question is which differences its design can resolve at all.[^c1] The minimum detectable effect (MDE) is the smallest difference an experiment can reliably separate from noise: it is the resolution the design has. In Miller's worked example, sampling more responses per question lowered the MDE "from 13.2 percent to 7.5 percent." Neither the model nor the questions became more accurate: "Each question simply produced a less variable estimate."[^c2]

The calculation is a power analysis. It "relates sample size, variance, the false-positive rate, and the probability of detecting a specified difference."[^c3] Power is "the probability that an experiment detects the specified effect when that effect is present."[^c4] At fixed variance, a smaller target effect, a lower false-positive rate, or a higher desired detection probability each "increases the number of observations required."[^c3] The MDE is the same calculation read in reverse: fix the task set, repeat count, variance estimate and error rates, and it states what the experiment can resolve.[^c5]

Two design consequences follow. First, the target effect is set by the decision, not by the hoped-for result: the text says to set it to "the smallest change that would alter the engineering decision, not the difference you" expect to report.[^c6] Second, which count to raise depends on where the uncertainty sits. "More benchmark items reduce uncertainty about performance across items," "More independent runs reduce uncertainty from" execution variation, and more responses per question reduce answer-level variance.[^c7]

The stakes of ignoring this are stated in the text. Many published benchmark comparisons cannot support the distinctions their tables imply: Card et al. found that "many test sets lacked the resolution needed" to separate reported state-of-the-art gains.[^c8] "An underpowered study fails in two directions." Most real effects go unreported as inconclusive, and among the estimates that cross the threshold, "the observed effects tend to be exaggerated because unusually" large estimates are the ones that survive.[^c9]

The variance input comes from a pilot. The text recommends at least 20 pilot runs for the variance estimate, and adds that this is "a floor for the pilot estimate, not a claim that the estimate has stabilized."[^c10] Under-sized pilots fail quietly: "A small or unrepresentative pilot can understate variance and produce a design that appears adequate on paper but remains underpowered in practice."[^c11]

## Limits

- The MDE is conditional on the variance estimate, the task set and the error rates. A resolution stated for one configuration does not transfer to another; the text gives the calculation, not a universal number for agents.
- The worked examples come from other benchmarks (GLUE, a sampling study of responses per question). The text says the variance results "do not establish an equivalent variance rate for long-horizon agents"; the same caution applies to MDE figures.[^c12]
- The text does not measure an MDE for any agent benchmark. This note states the design rule and its arithmetic, not a field result.
- The variance term is not one quantity for averaging purposes. Wang splits it into prediction and data parts and notes that "While prediction variance can be reduced by averaging, the data variance is irreducible."[^c13] Repeated runs or more samples per question shrink only the first part, so, in my inference, an MDE computed with averaging alone has a floor set by the data part. See [[prediction-data-noise-decomposition]].
- My inference: an MDE says what a null result can rule out, not whether a real but small improvement is worth pursuing; that remains a decision about cost.

## Related

- [[run-to-run-spread]] — the repeat-run variation that enters the MDE as the variance term
- [[context-dominates-model-choice]] — a paired benchmark whose models are statistically indistinguishable, the situation an MDE is meant to state in advance
- [[multi-seed-bias-score-averaging]] — averaging over many seeds as the way to shrink the variance term
- [[prediction-data-noise-decomposition]] — the variance term split into prediction and data parts, and which part averaging can reach

[^c1]: doi-10-48550-arxiv-2608-13867 — "Before running a suite, the first question is which differences the design can resolve at all."
[^c2]: doi-10-48550-arxiv-2608-13867 — "effect from 13.2 percent to 7.5 percent. The minimum detectable effect is the smallest difference the"
[^c3]: doi-10-48550-arxiv-2608-13867 — "variance, the false-positive rate, and the probability of detecting a specified difference."
[^c4]: doi-10-48550-arxiv-2608-13867 — "Power is the probability that an experiment detects the specified effect when that effect is present."
[^c5]: doi-10-48550-arxiv-2608-13867 — "Fix the task set, repeat count, variance estimate, and error rates"
[^c6]: doi-10-48550-arxiv-2608-13867 — "difference to the smallest change that would alter the engineering decision, not the difference you"
[^c7]: doi-10-48550-arxiv-2608-13867 — "reduce uncertainty about performance across items."
[^c8]: doi-10-48550-arxiv-2608-13867 — "many test sets lacked the resolution needed"
[^c9]: doi-10-48550-arxiv-2608-13867 — "An underpowered study fails in two directions."
[^c10]: doi-10-48550-arxiv-2608-13867 — "recommend at least 20 pilot runs for estimating this variance"
[^c11]: doi-10-48550-arxiv-2608-13867 — "A small or unrepresentative pilot can understate variance"
[^c12]: doi-10-48550-arxiv-2608-13867 — "Those results do not establish an equivalent variance rate for long-horizon agents."
[^c13]: arxiv-2512-21326 — "While prediction variance can be reduced by averaging, the data variance is irreducible"
