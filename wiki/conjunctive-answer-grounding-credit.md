---
description: "A video answer earns credit only if its spatial or temporal evidence is also localized, and under that joint credit models that order actions well still miss when they happen."
aliases: ["know-and-show credit", "joint answer and localization accuracy", "grounded reasoning accuracy", "show-what-you-know scoring"]
sources: ["arxiv-2512-05513", "arxiv-2512-01045"]
---
# Conjunctive answer-grounding credit

An answer can be scored as one event rather than two. It counts only when the answer is right and the place or time it points to in the input is also right. The Know-Show benchmark builds the score this way. The benchmark asks a model to "infer the correct outcome and to justify it by providing the relevant spatial and temporal cues in the video."[^c1] A model "receives credit only when it succeeds in both reasoning and localization, demonstrating a true" know-and-show capability.[^c2]

The score is a conjunction of two indicators per item. For spatial items, the predicted box must reach an IoU threshold with a ground-truth box, "where τ = 0.25 is the IoU threshold," and the timestamp must fall inside the action window.[^c3] For temporal items, the action label must match, and the predicted time must lie within a window δ of the ground truth. "A prediction is considered correct within a temporal window" with δ in {2, 4, 6} seconds.[^c4] My reading of the formulas is that the item counts only when both terms hold. The paper also reports the two terms separately, so a failed conjunction can be traced to one of them.

The separate reporting is what makes the score informative. In the temporal results, "although AAcc is high" the timestamp hit rate drops sharply under stricter windows.[^c5] The paper's summary is that models "exhibit relative temporal awareness but struggle" with absolute timing.[^c6] An answer can be right about the order of actions and still earn no joint credit, because the time it gives is too far off. In the spatial results, a consistent gap in AccSGR between IoU@0.25 and IoU@0.5 is read as models relying on "coarse, region-level localization rather than" boundary-accurate grounding.[^c7][^c8] The joint score therefore moves with the threshold chosen, not only with the model.

The conjunction does not close with a better prompt. The authors compare chain-of-thought and zero-shot prompting and report no meaningful difference between the two configurations.[^c9] They conclude that prompt engineering "alone is insufficient to improve grounded reasoning in Video-LMs."[^c10] Human annotators score above 75% on the same joint measure, which gives the score a reference point.[^c11]

What may transfer is the evaluation principle, not the video machinery. An answer is credited only when the input it cites supports it. In a text setting this would mean scoring an answer together with the span it cites. That step from video to text is my inference; the paper tests only video.

A construction paper on medical instructional video reports the same split between answering and grounding, from the other side. Med-CRAFT scores several models on overall accuracy and on a separate grounded QA score. The grounded score is lower for every model in its Table 9, by roughly 0.07 to 0.12 points: the domain medical model reaches 0.78 overall and 0.71 grounded, and the text-only baseline 0.45 and 0.35.[^c14] The authors draw the moral directly: "answering correctly is not equivalent to grounding the answer in the designated evidence."[^c15] The text read does not define the grounded QA score, so whether it is an all-or-nothing conjunction like the one above is not known from this text (my reading).

## Limits

- The score tests whether the located region matches an annotated region. It does not test whether the answer was produced from that region. The paper's grounding is an overlap measure, and whether the reasoning uses the evidence it points to is not checked here (my reading).
- The threshold matters. τ = 0.25 is a loose overlap, and the paper's own IoU@0.5 numbers are lower. The text I read gives no argument for one threshold over another, so the joint accuracy is only as stable as that choice.
- The benchmark inherits annotation error. The authors report that "some temporal annotations were imprecise or unrealistic."[^c12] A conjunction over noisy labels can mark a correct answer as wrong. The text I read does not say how such annotations were handled in scoring.
- The text I read does not compare the conjunctive score with a graded or separately weighted score. Whether the all-or-nothing rule is the right way to combine the two terms is not shown.
- The benchmark is built from Charades, Action Genome and Ego4D.[^c13] Transfer to other domains, and to text questions, is not tested.

## Related

- [[evidence-localization-gap]] — vision-language models over-include panels when asked to localize evidence; localization is a separate capability that the conjunction depends on.
- [[process-outcome-consistency-verification]] — rewards an answer only when its derivation agrees with it; the checked object there is the derivation, while here it is the located evidence.
- [[outcome-credit-through-explanation]] — routes credit to an explanation through the label during training; this note is the evaluation-side version of tying an answer to what supports it.

[^c1]: arxiv-2512-05513 — "to infer the correct outcome and to justify it by providing the relevant spatial and"
[^c2]: arxiv-2512-05513 — "when it succeeds in both reasoning and localization, demonstrating a true"
[^c3]: arxiv-2512-05513 — "where τ = 0.25 is the IoU threshold."
[^c4]: arxiv-2512-05513 — "A prediction is considered correct within a temporal window"
[^c5]: arxiv-2512-05513 — "although AAcc is high"
[^c6]: arxiv-2512-05513 — "exhibit relative temporal awareness but struggle"
[^c7]: arxiv-2512-05513 — "a consistent gap in AccSGR between IoU@0.25 and"
[^c8]: arxiv-2512-05513 — "models rely on coarse, region-level localization rather than"
[^c9]: arxiv-2512-05513 — "meaningful performance difference between the two configurations"
[^c10]: arxiv-2512-05513 — "alone is insufficient to improve grounded reasoning in Video-LMs."
[^c11]: arxiv-2512-05513 — "human performance exceeds 75% across all metrics"
[^c12]: arxiv-2512-05513 — "some temporal annotations were imprecise or unrealistic"
[^c13]: arxiv-2512-05513 — "Built from Charades, Action Genome, and"
[^c14]: arxiv-2512-01045 — "the highest grounded QA score (0.71)"
[^c15]: arxiv-2512-01045 — "answering correctly is not equivalent to grounding the"
