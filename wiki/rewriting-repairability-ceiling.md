---
description: "A best-of-8 rewriting upper bound shows 70-80% of a frozen discourse parser's errors cannot be fixed by any single-utterance rewrite, bounding how much asking-as-rewriting can ever help."
aliases: ["repairability ceiling", "best-of-8 repairability analysis"]
sources: ["liu-2026-beyond"]
---
# Rewriting repairability ceiling

> Before asking how well a clarifier rewrites, ask how many of the target
> errors a rewrite could ever fix — most cannot, at any generation budget.

## Definition / Mechanism

Liu et al. (2026) estimate an upper bound on how much
last-utterance rewriting can repair a frozen dialogue discourse parser's
errors: "we use the same L6-FREE strategy to sample 8 free-form rewrites of
the last utterance, rerun the frozen parser, and mark the example as
repairable if any rewrite yields the correct prediction. This estimates the
upper bound of recoverable errors under repeated rewriting, rather than the
performance of a practical clarifier."[^c1]

Across three SDRT datasets the ceiling is low: "the repairability ceiling
is low across all three datasets. Most parser errors remain unrepaired
even under candidate selection: 80.0% errors on STAC, 72.5% on Molweni,
and 71.8% on MSDC are not repaired by any of the eight sampled rewrites."[^c2]

Repairability is graded, not binary: on STAC the remaining errors split
6.6% moderately repairable and 2.4% highly repairable (3+ of 8 rewrites
succeed), with Molweni and MSDC showing larger repairable tails (9.1%/7.2%
and 14.1%/4.6%).[^c3]

## Why it matters

On stall 2 this is a precondition check that sits before any selection
criterion: a rewrite (a form of question/intervention aimed at one axis —
the last utterance) is only worth attempting if the target error is in the
repairable minority. A selection rule that spends effort ranking or
generating candidate rewrites for the 70-80% unrepairable majority is
solving the wrong problem regardless of how it scores candidates.

## Limits

- The bound is estimated with one generator (Qwen3-8B, free-form prompting,
  8 samples) and one rewrite point (the last utterance only); a different
  generator, larger sample, or a rewrite scope that reaches earlier context
  could move the ceiling, and the paper reports it as *this* setup's upper
  bound, not a universal constant.
- "Repairable" here means at least one of 8 sampled rewrites flips the
  parser's prediction to correct on the validation set — it is an oracle
  selection-of-best-of-8, not something a real clarifier can reproduce
  without knowing the ground truth in advance.[^c4]

## Related

[[abstention]] · [[selection-abstention-asymmetry]] · [[value-of-information]]

[^c1]: liu-2026-beyond
[^c2]: liu-2026-beyond — "the repairability ceiling is low across all three datasets. Most parser errors remain unrepaired even under candidate selection: 80.0% errors on STAC, 72.5% on Molweni, and 71.8% on MSDC are not repaired by any of the eight sampled rewrites."
[^c3]: liu-2026-beyond
[^c4]: liu-2026-beyond — "mark the example as repairable if any rewrite yields the correct prediction."
