---
description: "Self-generated rubrics move a verifier's confidence in the gold label mostly not at all; good rubrics raise accuracy and misleading ones push it below rubric-free judging."
aliases: ["two-sided rubric effect", "helpful and misleading rubrics", "rubric confidence shift", "failure of cooperation in rubric generation"]
sources: ["openalex-org-w7154789980"]
---
# Two-sided rubric influence

A rubric handed to a verifier is context, and context can help or hurt. The measure the work uses is a shift: for one sampled rubric, the probability the trained verifier assigns to the gold label with the rubric, minus the same probability without it. A positive shift means the rubric "indicates that the rubric steers the verifier toward the correct decision"; a negative shift means it pushes the verifier away.[^c1]

Measured this way, the effect is concentrated at zero. The distribution is heavy at zero "indicating that most self-generated rubrics barely affect" verifier confidence.[^c2] The tails differ between the two base models the work tests: for one, "negative shifts substantially outnumber" positive ones; the other is more balanced; but "yet beneficial rubrics remain rare for" both.[^c3] The paper's own summary of its first experiment is that "Naive self-generation thus offers little" benefit over rubric-free verification.[^c4]

The two-sided part is what the work calls a failure of cooperation. High-quality rubrics are "discriminative and consistent with" the question's intent, and they make verifiers far more accurate. Vague or misaligned rubrics do the reverse: they "can severely distort verifier reasoning, pushing it toward incorrect judgments even" when the verifier would have judged correctly without one.[^c5] The contributions list states the shape in one line: "most have negligible impact, but high-quality ones substantially improve accuracy whereas low-quality" ones hurt.[^c6] The abstract puts the same point as "lowquality rubrics actively mislead reward models rather than help."[^c7]

The mechanism, as I read the text: whether a rubric helps depends on whether its criteria point at the correct decision for that pair, not on whether a rubric is present at all. A generator that writes criteria without checking them will produce both kinds, and an average over its rubrics mostly cancels them. That is why the average looks like "little benefit" while the individual rubrics vary widely. This reading is mine; the paper states the two-sided result, not the cancellation argument.

The work's response is not to remove bad rubrics beforehand. It trains the generator to produce the helpful kind (see [[shift-labelled-rubric-contrast]]) and lets the verifier discard the rest at inference (see [[selective-rubric-trust]]).

## Limits

- The measurement uses one sampled rubric per example, scored by a verifier that the same paper trained.[^c8] The shift is therefore relative to that verifier, not to a neutral judge, and it says nothing about a verifier that never saw rubrics in training.
- "High-quality" and "low-quality" are the paper's terms, defined by discriminativeness and fit to intent. I did not establish from the parts of the text read how each rubric was assigned to one group.
- Two base models and the sample sizes behind the tail counts are the whole evidence for the shape. The claim that rubric quality "decisively affects verifier judgments" is an observation on these models, not a law.
- The result does not reconcile with every other measurement in the wiki. [[rubric-formation-gap]] reports that self-generated rubrics beat no rubric by a wide margin on hard pairwise comparisons. That is a different quantity (accuracy of a fixed judge, averaged over items), so the two are not contradictory, but neither paper tests the other's setting.
- The paper says weaker models may fail to separate helpful from misleading rubrics: "weaker models may struggle to reliably distinguish helpful from misleading".[^c9] Where that holds, the two-sided effect is not tamed by the verifier, and the note's claim about the tails applies to the stronger base models only.

## Related

- [[rubric-formation-gap]] — same domain; that note measures accuracy with the judge fixed, this one measures the per-example shift
- [[selective-rubric-trust]] — how the verifier responds to a rubric it judges misleading
- [[shift-labelled-rubric-contrast]] — how the shift becomes a training label for helpful and misleading rubrics
- [[rubric-verifier-failure-modes]] — a different failure of rubric verifiers, under reinforcement learning rather than at inference
- [[controlled-degradation-contrast]] — another way of building labelled pairs without annotators, by construction rather than by measured effect

[^c1]: openalex-org-w7154789980 — "indicates that the rubric steers the verifier toward the correct decision"
[^c2]: openalex-org-w7154789980 — "indicating that most self-generated rubrics barely affect"
[^c3]: openalex-org-w7154789980 — "negative shifts substantially outnumber"
[^c4]: openalex-org-w7154789980 — "Naive self-generation thus offers little"
[^c5]: openalex-org-w7154789980 — "misaligned rubrics can severely distort verifier reasoning, pushing it toward incorrect judgments even"
[^c6]: openalex-org-w7154789980 — "most have negligible impact, but high-quality ones substantially improve accuracy whereas low-quality"
[^c7]: openalex-org-w7154789980 — "lowquality rubrics actively mislead reward models"
[^c8]: openalex-org-w7154789980 — "For each example, we sample one rubric"
[^c9]: openalex-org-w7154789980 — "weaker models may struggle to reliably distinguish helpful from misleading"
