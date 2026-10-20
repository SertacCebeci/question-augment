---
description: "faithful@k is the chance that at least one of k sampled answers that flip to a hint verbalizes it; its curve against k separates budget-limited omission from a hint-type-specific gap."
aliases: ["faithful@k", "verbalization pass@k", "budget-scaled hint verbalization"]
sources: ["arxiv-2512-23032"]
---
# Faithful@k budget curve

A single greedy CoT answers one question: did the explanation mention the cue. This measure asks a different one: if the model is sampled again and again, how often does it produce at least one explanation that names the cue. It is an adaptation of the pass@k estimator. Given n samples per problem, of which c are faithful, the estimate is one minus the chance that all k draws come from the n minus c unfaithful ones. In this adaptation c counts samples that verbalize the hint, and n counts samples whose answer changed to the hinted one.[^c1] The authors call the result faithful@k, "the empirical estimate of the probability of obtaining at least one faithful explanation in k attempts."[^c2]

The mechanism behind the expected pattern is simple. If a non-verbalized hint reflects only the compression a single answer has to pass through, then giving the model more attempts should surface a CoT that does name the cue. If the model never reflects the cue, more attempts should not help. The authors ran 128 samples per example with k from 1 to 32, and kept only instances where the answer changed to the hinted one in enough samples.[^c3]

The result depends on the hint type. Under the Professor hint, faithful@k rises with k: "close to 0.9 at k = 16 on average" for gemma-3-4b-it, while the other two models "remain below 0.5".[^c4] Under the Black Squares and Metadata hints, "increasing k has little effect on faithful@k".[^c5] The authors read the two trajectories as distinct signatures. A uniform rise across hint types would not be diagnostic, since it could be a base-rate effect. A flat curve in one hint type and a rising one in another points to the hint type governing whether a faithful explanation can be produced at all.[^c6] In the larger and reasoning-model replication, "For Qwen-3-32B, faithful@k increases consistently as k grows, even under the" Professor, Metadata and Black Squares hints in the paper's summary, while for Llama-3.3-70B the rise appeared under the Professor hint and was limited under the others.[^c9]

The curve also answers a challenge the authors name themselves: that faithful@k might select favourable runs from a model that is only occasionally faithful. The monotone rise with k is, they argue, consistent with incomplete verbalization and not with random faithfulness.[^c7]

## Limits

- The measure needs n at least as large as the largest k, since instances with fewer hint-changing samples are dropped. The reported curves therefore apply to the cases in which the hint moved the answer often.
- Sampling is done with each model's default hyperparameters, not greedy decoding. The curve's shape therefore depends on the sampling settings; the paper does not vary them, and my reading is that a different temperature could move the curve.
- The judge that decides whether a sample verbalizes the hint has low precision and recall, as noted in [[verbalization-incompleteness-versus-unfaithfulness]]. A misjudged verbalization enters the numerator directly.
- The curve cannot tell whether the model is shaped by the hint in every run and does not always say so, or is only occasionally faithful. The authors say that "faithful@k alone cannot distinguish these interpretations at the level of individual instances"; they argue against the second reading only from aggregate patterns.[^c7]
- The authors state the open question directly: "systematically different behaviors under these conditions remains an open question".[^c8]

## Related

- [[verbalization-incompleteness-versus-unfaithfulness]] — the claim this curve is built to test: omission as incompleteness rather than unfaithfulness.
- [[hint-adherence-without-acknowledgement]] — the single-sample version of the same question, in closed-source models, where sampling budget cannot be varied in the same way.
- [[cot-natural-indirect-effect]] — a second check that does not depend on how often the CoT verbalizes the cue.

[^c1]: arxiv-2512-23032 — "c is the number of faithful samples with respect to Biasing Features"
[^c2]: arxiv-2512-23032 — "the empirical estimate of the probability of obtaining at"
[^c3]: arxiv-2512-23032 — "We generate 128 samples"
[^c4]: arxiv-2512-23032 — "close to 0.9 at k = 16 on average, whereas the"
[^c5]: arxiv-2512-23032 — "increasing k has little effect on faithful@k"
[^c6]: arxiv-2512-23032 — "uniform growth across hint types would render it"
[^c7]: arxiv-2512-23032 — "only occasionally faithful, with faithful@k selecting those favorable runs"
[^c8]: arxiv-2512-23032 — "systematically different behaviors under these conditions remains an open question"
[^c9]: arxiv-2512-23032 — "For Qwen-3-32B, faithful@k increases consistently as k grows, even under the"
