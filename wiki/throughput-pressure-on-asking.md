---
description: "**This wiki's conjecture.** An answerer scored per completed transaction The claim is a composition of two literatures that do not cite each other."
aliases: ["credit-unit account of the ask-rate deficit"]
sources: ["gers-1985", "radford-2011", "ross-1998", "zhang-2025-future-turns"]
---
# Throughput pressure on asking

> **This wiki's conjecture.** An answerer scored per completed transaction
> rather than per resolved need will stop clarifying — whatever it is made of.
> The low ask-rate of language models may be over-determined, and the
> preference signal is only one of the two mechanisms that produce it.

## Definition / Mechanism

The claim is a composition of two literatures that do not cite each other.[^s1][^s2][^s3][^s4]

| Side | What is measured | Where |
|---|---|---|
| Human professional answerers, trained and bound by written guidelines | a clarifying question in ~49% of face-to-face encounters (Gers & Seward 1985 [?], via Radford et al. 2011; 49% again across 261 Library Visit Study visits, Ross & Nilsen 2004); open questions in 33% of clarifications (Radford et al. 2011); the follow-up question in 12% (Gers & Seward [?]) to 50% (Radford et al.); unmonitored referral in 37% (Ross & Nilsen 2004) | [[query-clarification-rate]], [[negative-closure]] |
| Language models | [[efe-planning-as-variational-inference|ambiguity]] is detected and the answer is produced anyway, on items labelled as needing a question | [[clarification-benchmarks]] |
| The candidate mechanism already on file for models | the preference signal penalises withholding, hedging and deferral | [[preference-signal-against-asking]] |

Ross & Dewdney (1998) state a mechanism for the human side that has nothing to
do with preference training: negative closure occurs when the answerer's
primary goal is "to satisfy system demands by moving on to the next question."
The structural feature the two sides share is the **unit of credit**: one
completed response, not one resolved need. A clarifying turn spends the unit
without completing it.

**What follows if the conjecture holds.** The intervention is not a better
ambiguity detector and not only a debiased reward: it is changing what a
transaction is scored as. The one manipulation on record is on the model side
— Zhang, Knox & Choi (2025) relabel preference data by simulating the turn a
clarifying question enables, and gain +3 accuracy on the ask-versus-answer
judgment itself. Read through this note, that is not a labelling fix but a
change of the credit unit from the turn to the exchange.

**What would refute it.** An answerer whose credit unit is the resolved need —
scored on the exchange, not the response — and whose ask-rate stays at the
observed floor. Or a human study that varies queue pressure at a service desk
and finds the clarification rate unmoved.

## Known as

| Name | Field | Relation |
|---|---|---|
| credit-unit account of the ask-rate deficit | — | exact — this wiki's own name for its own conjecture; neither literature names the composition |
| negative closure | LIS | *not* this concept — the measured human behaviour this conjecture generalises ([[negative-closure]]) |
| the preference signal against asking | LLM alignment | *not* this concept — the rival (or containing) mechanism ([[preference-signal-against-asking]]) |

## Why it matters

1. **It separates two remedies that look alike.** Removing the sycophancy and
   hedging penalties leaves the credit unit intact; a system still scored per
   response should keep its ask-rate. Only the second remedy predicts a change.
2. **It makes the human rate a reference point rather than a curiosity.** If
   answerers under explicit written guidelines clarify on the order of half of
   *all* encounters, then an ask-rate well under 100% is the normal operating
   point of a working reference desk, and a model deficit is not established by
   the shortfall alone. This is an order-of-magnitude comparison only: the
   human denominator is every encounter, the benchmark denominator is the
   ambiguous items, so it does not say what score an ambiguity-labelled
   benchmark should target (see Limits).
3. **It puts the asker's cost back in the loop.** [[question-budgets]] prices
   the asker's attention; this note says the *answerer's* throughput is priced
   too, by whoever runs the desk, and that price is invisible in every
   single-transaction evaluation.

## Transfer

| | |
|---|---|
| **Home field** | library and information science: a human at a service desk with a queue, a supervisor, and statistics kept per question answered |
| **Here** | a model or agent whose training signal and whose deployment metrics are both defined on a single response |
| **What survives** | the structural argument — an answerer whose credit unit is smaller than the need will terminate before the need is resolved — and the prediction that moving the unit moves the rate |
| **What does not** | the mechanism's substrate. A librarian's incentive is a conscious work pressure with an employer behind it; a model's is a gradient. Nothing here shows the two produce the same functional form, and the human rates were measured with instruments that cannot be run on a model |

## Limits

- **No source tests the composition.** No study varies throughput pressure and
  measures a clarification rate, on either side; the incentive claim on the
  human side is Ross & Dewdney's interpretation of accounts.
- **The human and model rates are not on one denominator.** The LIS figures are
  over *all* encounters, whether or not the question needed clarifying; the
  model ask-rate in [[clarification-benchmarks]] is over items labelled as
  needing a question — that note's own Limits says so. Point 2 is therefore an
  order-of-magnitude statement about answerers working under written
  guidelines, not a claim that ~50% is the correct target for an
  ambiguity-labelled benchmark, and no arithmetic comparison of the two numbers
  is licensed here. [[query-clarification-rate]] records the same mismatch in
  its `## Known as` row for "ask-rate".
- **Two of the four human figures are second-hand and unverified.** The ~49%
  face-to-face rate and the 12% follow-up floor are Gers & Seward (1985),
  quoted through Radford et al. (2011); the 1985 article was not read in this
  pass and the verifier could not confirm it against an official listing —
  `gers-1985` is `[?]`. Ross & Nilsen (2004) independently report 49% over 261
  visits, which is what point 2 leans on if the 1985 figures fall.
- The human rates otherwise come from four instruments with different
  denominators and cannot be pooled into "the human ask-rate."
- Zhang et al.'s result is offered by them as an improvement to preference
  labelling. Reading it as evidence about the credit unit is this note's
  reading, and +3 accuracy is a small effect from one relabelling scheme.
- The two mechanisms are not shown to be independent: a preference signal
  collected from annotators judging single responses *is* a credit unit, so
  [[preference-signal-against-asking]] may be a special case of this note
  rather than a rival to it. The note cannot currently tell which.
- Nothing here says what the right ask-rate is; a credit unit set at the
  resolved need is as Goodhartable as one set at the response.

## Related

[[query-clarification-rate]] · [[negative-closure]] ·
[[clarification-benchmarks]] · [[preference-signal-against-asking]] ·
[[question-budgets]]

[^s1]: gers-1985
[^s2]: radford-2011
[^s3]: ross-1998
[^s4]: zhang-2025-future-turns
