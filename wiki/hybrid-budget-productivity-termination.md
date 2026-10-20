---
description: "Ends a generative question session on the first of three independent triggers: a hard question-count cap, a productivity heuristic over remaining candidates, or the user's own choice."
aliases: ["PrivacyAkinator termination", "Akinator-inspired stopping"]
sources: ["arxiv-2605-20206"]
---
# Hybrid budget-productivity termination

> Three independent reasons to stop asking — a hard cap, a sign that
> nothing left is worth asking, and the user saying so — any one of which
> ends the session, with the choice to keep going always offered back.

## Definition / Mechanism

Li et al. (2026)'s PrivacyAkinator ends a
question-generation session on whichever of three triggers fires first,
explicitly modelled on a guessing game: "Inspired by the Akinator game,
PrivacyAkinator provides three ways to end question generation. First, it
imposes a hard limit of 25 questions to avoid overwhelming users."[^c1]

The second trigger reuses the same statistics that
[[corpus-cooccurrence-question-ranking|rank the candidate pool]], turned into a sufficiency test rather than a
ranking — it applies heuristics to stop early "when enough information has
been gathered or further questions seem unproductive (i.e., no new nodes
are likely to be added and all potential design decisions have low
co-occurrence statistics)." This makes stopping a read-out of the same ranking signal at its floor, not a
separate learned criterion — when every remaining candidate scores low,
there is nothing left worth spending a turn on.

The third trigger is unconditional user override, and termination itself
is soft rather than a hard exit: "the user can end the session at any time
if they feel their design is complete or no longer want to continue. When
termination is triggered, PrivacyAkinator prompts the user to either
proceed with more questions to refine details or start the assessment
process."[^c3]

## Why it matters

None of the three triggers alone would be adequate: a pure count cap
ignores whether the session is still productive; a pure productivity
heuristic (all candidates score low) can be wrong early, before the corpus
prior has been narrowed by [[response-triggered-explore-exploit-switching|enough exploratory answers]]; a pure
user-driven stop asks novices — the population this tool targets — to
judge sufficiency themselves, the exact skill the paper's formative study
found they lacked. Layering a budget, a diminishing-returns signal, and a
reversible user choice covers each failure mode of the other two.

## Limits

- The productivity heuristic ("no new nodes are likely to be added")
  is not separately validated — it borrows the ranking's own low-score
  read-out, so a corpus-coverage gap (see [[corpus-cooccurrence-question-ranking]]'s
  limits) that under-scores a real decision also under-triggers useful
  continuation, not just stopping.
- The hard cap of 25 is fixed, not derived from task complexity or scaled
  to the system being described; no sensitivity analysis over this number
  is reported in the extract read here.
- Evaluated only as part of the whole tool; stopping behavior itself is
  not measured against an independent notion of "should have stopped."

## Related

[[corpus-cooccurrence-question-ranking]] · [[response-triggered-explore-exploit-switching]] · [[bayesian-experimental-design]]

[^c1]: arxiv-2605-20206
[^c3]: arxiv-2605-20206 — "the user can end the session at any time if they feel their design is complete or no longer want to continue. When termination is triggered, PrivacyAkinator prompts the user to either proceed with more questions to refine details or start the assessment process."
