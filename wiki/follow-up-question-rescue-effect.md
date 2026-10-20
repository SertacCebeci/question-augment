---
description: "In a deployed legal-intake classifier, a follow-up question elicited a classification-changing fact 69% of the time and rescued more wrong classifications than it corrupted, net positive."
aliases: ["FETCH classification flip experiment"]
sources: ["steenhuis-2026"]
---
# Follow-up-question rescue effect

> Asking one more question does not just add information in principle — in
> a deployed classifier it measurably fixes more answers than it breaks.

## Definition / Mechanism

Steenhuis & Harvey built a synthetic "flip" dataset of 200 legal-intake
scenarios, each split into a truncated setup and a hidden fact that should
change the correct classification. FETCH classified the truncated setup,
optionally asked a follow-up question, received the hidden fact as an answer
if an LLM judged it relevant to the question, and re-classified. Restricted
to the 138 scenarios where FETCH's question matched the hidden fact
("matched scenarios"): "when the litigant had a relevant fact that changed
classification, FETCH asked a question that elicited it 69% of the time.
This follow-up question rescued an incorrect classification 4.5 times more
often than it degraded a correct classification."[^c1]

The outcome counts over the 138 matched scenarios: 72 correctly unchanged,
26 correct-and-neutral, 4 correct-to-wrong (true degradation), 18
wrong-to-correct (rescued), 18 still wrong — net impact +14 (rescued minus
degraded). "Follow-up was 4.5× more likely to rescue a wrong classification
than to corrupt a correct one."[^c2]

## Why it matters

This is a measured, not assumed, answer to "does asking help here": for
stall 2's question of whether a system should spend a turn on a follow-up
question at all, the net effect in this deployed classifier is positive and
asymmetric — the downside (degrading a correct call) is rare relative to the
upside (rescuing a wrong one). It is a rare case of a downstream-accuracy
number attached to a real elicitation mechanism rather than a lab benchmark.

## Limits

- The 69% elicitation rate and 4.5× rescue ratio are pooled across case
  types; the paper's own per-pair breakdown (Table 5) shows this is not
  uniform — domestic-violence scenarios had only 10% follow-up coverage of
  the relevant fact, the weakest of any category, so the net-positive result
  should not be read as evenly distributed across legal domains.
- The rescue/degrade classification depends on an LLM judge (GPT-4.1) both
  for relevance-of-answer and for final classification comparison; no human
  ground-truth check of that judge's outcome labels is reported for this
  experiment.
- The scenarios are synthetic "flip" pairs generated with LLM assistance and
  attorney review, not observed real applicant intakes, so the 69%/4.5×
  figures describe this constructed test, not deployed-traffic incidence.

## Related

[[model-capacity-question-generation-gap]] · Selection · [[value-of-information]]

[^c1]: steenhuis-2026
[^c2]: steenhuis-2026
