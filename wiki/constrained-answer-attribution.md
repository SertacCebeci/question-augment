---
description: "*This wiki's inference, not a result.* A reply that arrives through a schema Three measurements about masked answering, none of them about each other: answerer and the grammar's shape,"
aliases: []
sources: ["beurer-kellner-2024", "bishop-1986", "park-2024", "tam-2024"]
---
# Attributing a masked answer

> *This wiki's inference, not a result.* A reply that arrives through a schema
> has two authors, and unlike a human respondent a masked answerer can be
> re-run — so the split ballot that survey methodology cannot afford is
> available here, one answer at a time.

## The inference

Three measurements about masked answering, none of them about each other:[^s1][^s2][^s3][^s4]

- the rate at which each admissible answer comes back is set jointly by the
  answerer and the grammar's shape, because masking replaces the lookahead
  term with a yes/no test (Park et al. 2024 → [[expected-future-grammaticality]]);
- a mask computed on a vocabulary misaligned with the model's subwords
  "significantly impair[s] task accuracy" (Beurer-Kellner, Fischer & Vechev
  2024);
- 100% of JSON-mode replies put the answer key before the reason key, and on
  the same runs GPT-3.5-Turbo fell from 76.60% to 49.25% on GSM8K (Tam et al. 2024). That the field order *caused* the loss — that the schema made the
  answerer commit before it derived — is an inference, and its sign is
  contested; [[format-restriction-effect]] holds that dispute.

Composed, they say that the thing recorded as a constraint is a joint product
of answerer and instrument — the same structure [[survey-response-model]]
establishes for human respondents, where pressure to answer produced opinions
on fictitious legislation in about 30% of respondents (Bishop, Tuchfarber & Oldendick 1986). **This wiki's proposal is that the attribution is
measurable here in a way it is not there**, because the instrument can be
removed and the same respondent asked again: decode the same prompt once
masked and once free, and record, beside the filled field, the answerer's
*unconstrained* probability mass on the cell the mask selected —
$P(w \in L(G_c))$ for the sub-grammar $G_c$ of that one cell, estimated from
free samples. (In Park et al.'s notation this is the expected future
grammaticality of the *empty* prefix with $G$ replaced by $G_c$; it is not
$c(w_{1:i})$ for the masked prefix, which is defined against the whole
grammar and so pools every admissible answer — the pooled quantity is
precisely the one this proposal does not want.) A cell chosen with near-zero
unconstrained mass is the token-level candidate for Bishop et al.'s
pseudo-opinion: an answer that exists because it had to.

The design rule that follows — the corrective and the no-opinion branch must
be members of the grammar — is [[constrained-decoding]]'s, not this note's.
What this note adds is the number that goes with it: the unconstrained mass
on that branch is what tells the asker whether a selected no-opinion or
corrective was the answerer's or the grammar's.

## Transfer

| | |
|---|---|
| **In its home field** | Survey methodology: the split ballot. Randomise wordings across many respondents; the difference between arms is the instrument's contribution. It needs a population, which is why [[survey-response-model]] names it as not surviving the import to an agent asking once. |
| **Here** | One answerer, one question, two decodings of the same prompt — masked and free — plus the unconstrained mass the model assigns to the selected cell. |
| **What survives** | The logic that an answer is a joint product of instrument and respondent, and the requirement of an explicit no-knowledge branch in the instrument. |
| **What does not** | The identification. Two decodings are not two randomised arms: the difference confounds the mask with sampling noise unless many samples are drawn, and the free decoding may not be parseable into the same cells at all — which is exactly the parser confound Kurt (2024) charges against the studies in [[format-restriction-effect]]. |

## Limits

- **The proposal rests on reading the model's unconstrained mass as the
  answerer's belief.** [[calibration]] denies that in general; under a
  miscalibrated $P$, low mass on a cell is not evidence that the answerer did
  not hold it.
- **The quantity is an estimate, and the estimator is the weak point.**
  $P(w \in L(G_c))$ over free samples is a rare-event probability exactly in
  the case the proposal cares about — the near-zero cell — so the sample size
  needed grows as the signal gets interesting.
- No source measures whether low unconstrained mass predicts a wrong or
  unheld answer. Park et al. measure divergence from the ideal conditional,
  not answer quality, and report that correcting the divergence has no strong
  effect on task success — which is evidence against the operational value of
  this proposal as much as for it.
- The human end of the analogy is human. No cited work measures a
  pseudo-opinion rate for a masked model; the correspondence is structural,
  and this note is typed `conjecture` for that reason.
- The two decodings must differ only in the mask. In deployed systems the
  prompt and the schema change together, so the quantity is measurable only
  in a setup built for it.

## Related

[[expected-future-grammaticality]] · [[constrained-decoding]] · [[format-restriction-effect]] · [[survey-response-model]] · [[question-as-partition]] · [[calibration]]

[^s1]: beurer-kellner-2024
[^s2]: bishop-1986
[^s3]: park-2024
[^s4]: tam-2024
