---
description: "An internal critic interrogates each candidate evaluation metric along four fixed axes and issues a PASS, FLAG or REJECT verdict, pruning a metric portfolio with no labels."
aliases: ["self-review", "adversarial validity questions"]
sources: ["gupta-2026-litmus"]
---
# Adversarial metric self-review

> A second, inward-facing interrogation channel: after candidate metrics
> are drafted, an LLM critic questions each one against a fixed checklist
> before it is allowed into the exported portfolio.

## Definition / Mechanism

Litmus drafts candidate metrics from the confirmed facts its
practitioner-facing interrogation produced, then subjects each candidate
to a second round of targeted questions the practitioner never sees.
"After drafting candidate metrics, Litmus interrogates each one along
four axes — pipeline fit, validity conditions, data assumptions, and
direction of goodness — and emits a verdict of PASS, FLAG, or REJECT."[^c1]

On the scientific-QA pipeline this yield was reported in full: "On the
scientific-QA pipeline this self-review passed 36, flagged 10, and
rejected 11 of the candidate metrics."[^c2]

A representative resolved question shows the axis in use: "'Does RAG
Context Precision measure the component it is attached to?' REJECT: the
component is a PDF reader/parser that extracts text; it performs no
query-based retrieval, so a retrieval-quality metric cannot apply."[^c3]

## Why it matters

It separates two interrogation targets on the same stall: the
practitioner-facing channel resolves what a metric *should* measure
([[goal-elicitation-by-interrogation]]), while this channel checks
whether a metric, once drafted, is actually *valid* for the component it
is attached to — without needing a labelled dataset or a human in the
loop for that second check.

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | LLM-as-judge / adversarial critique of a model's own output | self-critique of a candidate evaluation metric before export |
| What survives | an LLM is used to interrogate a candidate against explicit criteria rather than score it holistically | the criteria are fixed to four named axes (pipeline fit, validity conditions, data assumptions, direction of goodness), applied uniformly across candidates |
| What does not | independent verification of the critic's own judgement | the self-review's verdict accuracy is not separately measured against ground truth — only the downstream portfolio's label-validity is reported |

## Limits

The critic is drawn from the same model family that authored the
candidate metrics it is checking, a bias the paper names directly:
"three of our axes (coverage, grounding, and redundancy) are themselves
LLM-assessed by the same model family that powers Litmus, risking
judge–system alignment bias." No experiment isolates how many of the
36/10/11 verdicts on the scientific-QA pipeline a different judge family
would reverse.[^c4]

## Related

[[goal-elicitation-by-interrogation]] · [[expected-information-gain]] · [[defect-localization]]

[^c1]: gupta-2026-litmus — "After drafting candidate metrics, Litmus interrogates each one along four axes —pipeline fit, validity conditions, data assumptions, and direction of goodness —and emits a verdict of PASS, FLAG, or REJECT."
[^c2]: gupta-2026-litmus — "On the scientific-QA pipeline this self-review passed 36, flagged 10, and rejected 11 of the candidate metrics."
[^c3]: gupta-2026-litmus
[^c4]: gupta-2026-litmus
