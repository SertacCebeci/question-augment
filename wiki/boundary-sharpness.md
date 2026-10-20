---
description: "A benchmark metric testing whether an answerer's abstention tracks the real knowledge boundary, by subtracting reliability on matched answerable items from abstention-zone reliability."
aliases: ["BS", "Boundary Sharpness"]
sources: ["arxiv-2606-26101"]
---
# Boundary sharpness

> A model that abstains on everything unfamiliar-looking scores high on raw
> abstention rate; boundary sharpness instead asks whether that same model
> also *keeps answering* the matched items it can actually answer — the gap
> between the two is the signal, not either rate alone.

## Definition / Mechanism

Meng et al. (2026) evaluate answerers under a four-state
decision protocol — `ANSWER`, `ABSTAIN_DONT_KNOW`, `REFUSE_POLICY`,
`PARSE_ERROR` — where "policy refusal and parser error never receive
productive-abstention credit." Reliability on a zone is the credited
rate of correct answers (for answer-expected zones) or correct epistemic
[[abstention]] (for the abstention-expected zone). Boundary sharpness
compares two such zone reliabilities directly: "Boundary sharpness is BS
= Rel_D − Rel_C." Zone C is answer-expected items obtained by
transforming Zone A/B public-salience items (harder phrasing, same
underlying facts); Zone D is build-time-constructed items with no gold
answer at all. Because C and D are matched in surface difficulty and
construction pipeline, subtracting Rel_C from Rel_D removes the part of
"the model abstains a lot" that is just conservatism, leaving the part
that responds to whether the item is actually unanswerable.

"Positive BS means the model gains reliability when moving from
transformed answerable items to abstention-expected items; it does not
by itself distinguish selective caution from a surface heuristic."[^c3]
A negative BS is diagnostic on its own: Llama-3-8B obtains zone
reliabilities "0.5066/0.2941/0.4037/0.1127, yielding boundary sharpness
−0.2910. The negative value shows that its standard-prompt policy does
not separate the abstention boundary, despite competitive public-question
accuracy."[^c4]

## Why it matters

Raw abstention rate on an unanswerable-only split is gameable by a
policy that just abstains often: "Qwen3-8B reaches perfect productive
abstention but answers only 64.01% of A–C questions and unnecessarily
abstains on 35.99%." A practitioner who reports Zone-D abstention
rate alone cannot tell this model apart from one that has actually
learned to detect the boundary; boundary sharpness forces the
comparison against a matched answerable zone into the same number, so
an answerer that abstains indiscriminately no longer looks identical to
one that abstains selectively.

## Limits

A positive BS is necessary but not sufficient evidence of genuine
boundary detection: the same construction pipeline that produces Zone D
leaves a lexical fingerprint, and "a character- and word-TF–IDF probe
distinguishes Zone D from A–C with AUROC 0.9825 and AUPRC 0.9488 on
held-out questions, exposing residual construction artifacts." A
model could therefore earn positive BS by keying on how a synthetic item
is phrased rather than on whether it is answerable, so BS should be read
alongside a construction-artifact probe on the same split, not alone.
The metric also inherits the matching assumption that zone C and zone D
are equated in everything except answerability; if that assumption
fails, BS conflates a difficulty gap with a boundary-detection gap.

## Related

[[abstention]] · [[calibration]] · [[mean-reliability-score]] ·
[[recognition-refusal-dissociation]]

[^c3]: arxiv-2606-26101 — "Positive BS means the model gains reliability when moving from transformed answerable items to abstention-expected items; it does not by itself distinguish selective caution from a surface heuristic."
[^c4]: arxiv-2606-26101 — "Llama-3-8B obtains 0.5066/0.2941/0.4037/0.1127, yielding boundary sharpness −0.2910. The negative value shows that its standard-prompt policy does not separate the abstention boundary, despite competitive public-question accuracy."
