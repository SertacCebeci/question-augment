---
description: "Point adjustment credits a whole anomaly segment when one point inside it is flagged, so a lucky hit validates it and random predictors score high; coverage constraints counter this."
aliases: ["point-adjusted F-score", "PA", "PAF-beta", "point-adjusted evaluation"]
sources: ["arxiv-2511-18739"]
---
# Point adjustment

Point adjustment is a rule that turns point-wise predictions into segment-level credit. The original predictions are kept, but for each ground-truth anomalous segment the adjusted prediction is rewritten: the predictions are adjusted "within each ground-truth segment as follows", so that once any point in a segment is flagged, every point of that segment counts as detected.[^p1] The F-score is then computed on the adjusted predictions. The consequence the authors name is that "a single predicted point can validate an entire anomaly segment."[^p2]

The rule is a granularity choice. It treats the segment as the unit of detection, and the paper's general statement about such designs is that "event-adjusted metrics are more vulnerable to random inflation if they treat entire segments as atomic units."[^p3] Under a random predictor, a few scattered flags can land in many segments, and each landing is credited in full. That interaction with segment length is my inference from the mechanism, not a measurement in the text.

The measured effect is the one in [[random-score-inflation]]. For the Point-Adjust F-score, the genuine and random averages were 0.842 and 0.433, with an effect size of 3.715 and an AUC of 0.930, so the metric still separates detectors from chance but with a "modest effect size".[^p4] The authors list Point-Adjust among "widely used metrics" that "may still obtain relatively high scores under random predictions."[^p5]

The remedy the paper describes is a coverage constraint. The K%-point-adjusted F-score "enforces a minimum coverage constraint": a predicted segment counts only if it covers at least K% of the segment. The authors put it as "this binary shortcut by enforcing a quantitative threshold," which replaces the existence of any overlap with a test of its adequacy.[^p6] The price is stated in the same passage: "this strictness introduces sensitivity to segment length and threshold selection", and "coverage constraints may underestimate" detections when anomalies are intrinsically short.[^p7]

## Limits

- The inflation figures come from one experimental pipeline with synthetic and three univariate benchmark series; the Point-Adjust numbers are not a general constant.[^p8]
- The text gives the coverage remedy's trade-off qualitatively. The passages read do not report how often short true anomalies are lost under a given K%, so the size of that cost is not established here.
- Point adjustment is defined for binary point predictions over labelled segments. Whether a segment-level credit rule has an analogue in answer grading, where a "segment" is a span of a reasoning trace or an answer, is my inference and is untested.
- A segment-credit rule is not the only cause of random inflation; the authors also attribute it to the fundamental granularity of correctness, which Point-Adjust does not fully define (see [[random-score-inflation]]).

## Related

- [[random-score-inflation]] — the failure this rule produces, and the separation test that measures it
- [[three-test-metric-validity-audit]] — another way to audit a metric by what it rewards, here by sensitivity tests rather than by a random baseline

[^p1]: arxiv-2511-18739 — "within each ground-truth segment as follows"
[^p2]: arxiv-2511-18739 — "a single predicted point can validate an entire anomaly segment"
[^p3]: arxiv-2511-18739 — "Event-adjusted metrics are more vulnerable to random inflation if they treat entire segments as atomic"
[^p4]: arxiv-2511-18739 — "close (0.842 vs. 0.433), resulting in a modest effect size of"
[^p5]: arxiv-2511-18739 — "Experimental results show that some widely used metrics (e.g., Point-Adjust or NAB) may still obtain relatively"
[^p6]: arxiv-2511-18739 — "this binary shortcut by enforcing a quantitative threshold"
[^p7]: arxiv-2511-18739 — "this strictness introduces sensitivity to segment length and threshold selection"
[^p8]: arxiv-2511-18739 — "three widely-used univariate time series (UTS) anomaly"
