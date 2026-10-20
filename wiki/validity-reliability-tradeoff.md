---
description: "Design choices that make a bias test valid often make it less reproducible, and constraints that secure reproducibility narrow what it can detect; the tradeoff is rarely stated."
aliases: ["validity-reliability tradeoff", "validity versus reliability", "construct reliability tradeoff"]
sources: ["doi-10-48550-arxiv-2305-12757"]
---
# Validity-reliability tradeoff

Validity and reliability are different questions about a measurement. Validity asks whether it is right; construct reliability asks whether it can be repeated. The authors state that "Sometimes design choices that aid in establishing validity can threaten reliability, and vice versa."[^c1] The mechanism is that the two goals pull the same design in opposite directions, so a fix for one tends to cost the other.

The paper's first example runs one way. Many papers conceive bias as toxic content generation, use prompt continuation as the task, and measure bias as differences in toxicity across the generated output. This "reflects good predictive validity in testing whether, over a broad set of outputs, the model generates toxic content." The cost is reliability: "reliability may be threatened, as the test is brittle to choices such as decoding parameters."[^c2] Open-ended generation reaches the real output distribution, and that same openness makes the result depend on how the text was decoded.

The second example runs the other way. "tests using generation from a fixed set of N words are easier to replicate than less constrained generation, but at the cost that the set of phenomena that can be captured is narrower."[^c3] Fixing the inputs buys repeatability and removes the sampling that makes open tests hard to compare, and it narrows what the test can see.

The same pattern appears in the instruments. Sentiment and toxicity have many classifiers across languages, and many tests use an ensemble of them. The authors warn that because these classifiers "may differ in subtle ways and be frequently updated," tests that rely on them "may yield inconsistent results."[^c4] Regard is the contrast. It is scored by one classifier from Sheng et al. (2019), and "by virtue of there being exactly one regard classifier that does not change, tests using regard are broadly comparable."[^c5] The cost is the one the paper names for regard: as a paper's domain moves away from what the classifier was built for, "validity is increasingly threatened."[^c6] A fixed instrument keeps results comparable across papers, while its fit to the domain erodes.

The authors' conclusion is that "Such validity and reliability tradeoffs are rarely explicitly navigated."[^c7] In the sense used here, the tradeoff is a property of design, not of any one test: each choice that raises one property has a predictable cost to the other, and the paper argues that a test should state which side it chose.

## Limits

- The paper gives no measured size for either cost. The brittleness to decoding parameters is cited from Akyürek et al. (2022), not reproduced in this work, and the regard drift is described, not quantified.
- The claim that these tradeoffs are "rarely explicitly navigated" is a reading of how the 77 annotated papers describe their choices. It is not a test of whether the navigated cases did better.
- The reliability in question is repeatability of the test. It is not inter-rater agreement or the reliability of a confidence score, which are different measurements.
- A test can gain both properties, for instance by a fixed set of prompts scored by a validated classifier. The paper's examples are presented as tradeoffs, and it does not show that every design faces one.
- "Validity" here is measurement validity (see [[measurement-modelling]]), not the response validity of a confidence signal in [[validity-screening-protocol]].

## Related

- [[measurement-modelling]] — the framework that names the validity threats; this note adds the reliability axis that it does not score.
- [[sentiment-as-harm-proxy]] — a case where the instrument's fit to the domain, not its repeatability, is what erodes.
- [[multi-seed-bias-score-averaging]] — a reliability problem on the same kind of bias score: one generation pass scatters widely across seeds.
- [[answer-format-dependent-bias-measurement]] — a related operationalisation choice (response format) that changes the measured bias.

[^c1]: doi-10-48550-arxiv-2305-12757 — "Sometimes design choices that aid in establishing validity can threaten reliability, and vice versa."
[^c2]: doi-10-48550-arxiv-2305-12757 — "However, reliability may be threatened, as the test is brittle to choices such as decoding parameters"
[^c3]: doi-10-48550-arxiv-2305-12757 — "tests using generation from a fixed set of N words are easier to replicate than less constrained generation, but at the cost that the set of phenomena that can be captured is narrower."
[^c4]: doi-10-48550-arxiv-2305-12757 — "tests relying on them may yield inconsistent results"
[^c5]: doi-10-48550-arxiv-2305-12757 — "by virtue of there being exactly one regard classifier that does not change, tests using regard are broadly comparable."
[^c6]: doi-10-48550-arxiv-2305-12757 — "validity is increasingly threatened"
[^c7]: doi-10-48550-arxiv-2305-12757 — "Such validity and reliability tradeoffs are rarely explicitly navigated."
