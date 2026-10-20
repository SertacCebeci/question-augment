---
description: "The question that names a target best (semantic match) need not produce the score that best predicts it; a related, indirect question can predict better."
aliases: ["direct prediction fails", "semantic alignment versus predictive alignment"]
sources: ["arxiv-2604-06820"]
---
# Semantic-predictive misalignment

> Deciding what to ask may be as important as refining how to ask it.

## Definition / Mechanism

Xu, Zheng, Wu & Ma (2026) test a default assumption
of using an LLM to estimate a human response: that asking the model the
question whose wording names the target produces the score that best
predicts that target. Eight LLM evaluators and 317 human participants
rated 290 deceptive articles on two related properties — perceived
credibility and willingness to share — using the same wording and scale.
For credibility the assumption held: the credibility question's score
was the better predictor of human credibility for all eight evaluators.
For sharing it failed: "For every evaluator, credibility scores track
human sharing at least as closely as sharing scores, while sharing
scores offer no detectable benefit beyond credibility when predicting
responses to unseen scenarios."[^c1]

The paper names the general distinction this reversal exposes: "This
finding distinguishes semantic alignment between a question and its
intended target from predictive alignment between the resulting score
and human ratings. A question can match the target in meaning while a
related question produces a score that predicts it better."[^c2]

Two structures over a set of candidate questions can therefore diverge:
which question is *about* the target (semantic structure, fixed by
meaning) and which question's score best *predicts* the target
(predictive structure, an empirical fact about the evaluator and the
population). Selecting the next question to ask by the first structure
alone — pick the question that names the thing you want — silently
assumes the two structures coincide; this work is a case where they do
not, and the divergence is undetectable from the sharing score's
behavior alone, since that score still correlates positively with human
sharing.[^c3]

The result is not an artifact of prompt order or of asking both questions
together: "This pattern persists when the questions are asked separately
or in reversed order," and it holds across recruitment waves, clustered
statistical models, and all three article generators.[^c4]

## Why it matters

For a system choosing which question to route to a source (human or
model) in order to predict or elicit a target quantity, this work
supplies the selection criterion that a semantically-matched question
lacks a guarantee for: held-out predictive validity against the actual
target distribution, measured empirically, not assumed from the
question's wording. It reframes "which question to ask next" (this
category) as a question that can require testing an indirect route — a
related judgment used as a proxy — against the direct one, rather than
defaulting to the direct route because it is the one that names the
target. The credibility-question-for-sharing case is a positive
existence proof that an indirect route can strictly dominate a direct
one on a held-out prediction criterion, not merely tie it.

## Limits

- Demonstrated on one domain (misinformation risk), one paired outcome
  (credibility/sharing), English news-style articles, and a Prolific
  sample; the source itself: "The applicability of the findings to
  other content forms, languages, populations, and behavioral outcomes
  remains to be established."[^c5]
- Measures *stated* willingness to share, not observed sharing
  behavior, so the target itself is a self-report, not the behavior it
  stands for.
- A null result for incremental value (sharing adds nothing once
  credibility is known) is evidence of absence only under the tested
  procedure: "The absence of a detectable held-out improvement here
  does not establish that sharing scores contain no independent
  information under every setting."[^c6]
- The paper diagnoses the divergence between semantic and predictive
  structure but does not give a procedure for predicting, without first
  collecting held-out human data, which of several semantically
  plausible questions will turn out predictively best — the finding
  motivates testing, not a way to skip it.

## Related

Selection · [[query-misalignment-framework]] ·
[[expected-information-gain]] · [[calibration]]

[^c1]: arxiv-2604-06820 — "For every evaluator, credibility scores track human sharing at least as closely as sharing scores, while sharing scores offer no detectable benefit beyond credibility when predicting responses to unseen scenarios."
[^c2]: arxiv-2604-06820 — "This finding distinguishes semantic alignment between a question and its intended target from predictive alignment between the resulting score and human ratings. A question can match the target in meaning while a related question produces a score that predicts it better."
[^c3]: arxiv-2604-06820 — "Sharing scores nevertheless remained positively correlated with human sharing, showing why comparisons limited to correspondingly named scores and responses can miss this outcome misalignment."
[^c4]: arxiv-2604-06820 — "This pattern persists when the questions are asked separately or in reversed order."
[^c5]: arxiv-2604-06820 — "The applicability of the findings to other content forms, languages, populations, and behavioral outcomes remains to be established."
[^c6]: arxiv-2604-06820 — "The absence of a detectable held-out improvement here does not establish that sharing scores contain no independent information under every setting."
