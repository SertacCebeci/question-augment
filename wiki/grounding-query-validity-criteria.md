---
description: "A video-grounding query is valid only if the event it names exists, is unique among the video's queries, is unambiguous, and does not leak its own timestamp."
aliases: ["temporal grounding query criteria", "query quality criteria for temporal grounding", "query uniqueness and leakage"]
sources: ["arxiv-2512-14698"]
---
# Grounding query validity criteria

A query in temporal grounding names one event and asks where it is: given a video and a sentence, return the start and end times of the segment that matches. The sentence is a question in all but form, and its answer is a segment. TimeLens treats the sentence as valid only under four conditions, stated as input criteria before any model is scored. The described event must exist: "must genuinely exist within the video content."[^c1] The query must be clear: "The query must be clear, precise, and unambiguous for accurate and definitive grounding."[^c2] The query set must be unique: the authors list "Query uniqueness" as a criterion, and "The presence of multiple nearly identical queries" describing one event is a defect.[^c3] And the query must not leak: "Queries like 'ending credits' leak their temporal position, allowing the model to answer via shortcut."[^c4]

The mechanism is that these conditions fix what a score measures. A segment answer is graded against one reference span. If the sentence names an event that is absent, or names it so loosely that several spans fit, the reference is not the only correct answer and a correct model is marked wrong. If two queries in the same video describe the same event, the event is counted twice and carries double weight in the metric: "this is equivalent to duplicating or weighting certain samples, leading to biased metrics."[^c5] If the wording carries the position, a model can score by a prior over times rather than by finding the event in the video.[^c4] Each failure moves the score without moving the capability it is meant to measure.

The authors measured how often these failures occur in existing data rather than assuming it. Their repair procedure is diagnose-then-refine: an annotator reviews the video against the error types, then "revise the query or choose a new valid event to describe," and only then annotates the segment.[^c6] They group all queries from one video together so that uniqueness violations can be seen.[^c7] On Charades-STA, "we find that 20.6% of samples violate query uniqueness, while 34.9% exhibit annotation accuracy issues," and the authors conclude that "Such severe errors will lead to unreliable evaluation results and misguide research efforts."[^c8][^c9] The re-annotated benchmark also changed model rankings: "Our analysis reveals dramatic model re-rankings compared to legacy benchmarks."[^c10]

The criteria are also a plain account of what a good question must do before it is answered. A question that picks out a target by description should (a) name something present, (b) not duplicate another question about the same thing, (c) pick out one answer, and (d) not contain its answer. The first three are checks an asker can run on the request. The fourth is a check on whether the answer that comes back is earned. (This transfer is my inference: the paper states the criteria for video segments, not for questions in general.)

## Limits

- The evidence is one task: single-event localization in video, on three benchmarks (Charades-STA, ActivityNet Captions, QVHighlights). The rates above are reported for Charades-STA; the error composition of the other two is in a figure whose numbers I did not read from the text.
- Clarity and existence are judged by annotators. The text I read gives examples ("the game continues" is named as a counterexample) but no formal test that computes them.
- Leakage is named as a criterion, and the authors note that "annotators tend to label such queries since they are easy to identify." I did not find a measured rate of leaked queries or a model-level effect of removing them in the sections I read.
- The re-ranking result compares the refined benchmark with legacy ones. It does not separate how much of the shift comes from each criterion, so which criterion moves rankings most is not shown.
- Whether the four conditions are sufficient for open-ended questions, where the answer is not a span in a timeline, is untested here.

## Related

- [[ambiguity-taxonomy]] — the kinds of unclear wording; the clarity criterion is one place where those kinds decide validity
- [[referent-match-set-ambiguity]] — counts how many objects a description matches; uniqueness here is the same kind of count, taken over the events a query set describes
- [[reference-answer-defect-audit]] — another audit showing that a flawed benchmark apparatus can make low scores reflect the benchmark, not the answerer

[^c1]: arxiv-2512-14698 — "must genuinely exist within the video content"
[^c2]: arxiv-2512-14698 — "The query must be clear, precise, and unambiguous for accurate and definitive grounding"
[^c3]: arxiv-2512-14698 — "The presence of multiple nearly identical queries"
[^c4]: arxiv-2512-14698 — "leak their temporal position, allowing the model to"
[^c5]: arxiv-2512-14698 — "weighting certain samples, leading to biased metrics"
[^c6]: arxiv-2512-14698 — "revise the query or choose a new valid event to describe"
[^c7]: arxiv-2512-14698 — "we group all queries from the same video together"
[^c8]: arxiv-2512-14698 — "we find that 20.6% of samples violate query"
[^c9]: arxiv-2512-14698 — "Such severe errors will lead to unreliable evaluation results"
[^c10]: arxiv-2512-14698 — "Our analysis reveals dramatic model re-rankings compared to legacy"
