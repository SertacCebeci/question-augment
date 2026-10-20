---
description: "A greedy ridge head selects which EMA item to ask and when; adding an LM layer on top changed half the item sets but did not raise measured selection utility, though an expert preferred it."
aliases: ["EMA-E4B", "adaptive ecological momentary assessment", "hybrid ridge+LM question and timing selection"]
sources: ["ahmadi-2026"]
---
# Adaptive EMA item and timing selection (EMA-E4B)

> A deployed system that answers stall 2 twice over — which of 18 recurring
> items to ask next, and when — with a fitted greedy score, then tests
> whether wrapping that score in a language model helps. It does not, on the
> metric the system itself defines; a human reviewer preferred it anyway.

## Definition / Mechanism

Two ridge-regression models, fit on 2,640 historical ecological momentary
assessment (EMA) cases, produce the two actions separately. The **question
head** scores each candidate item by a weighted sum of predicted response
change, deviation from the person's own mean, a construct-level "need"
score, a fixed focal weight, and a recent-trend flag; items are then chosen
by greedy marginal selection against a value function that subtracts a
penalty for correlated items already in the set, so a second item from an
already-covered construct adds less. Ahmadi, Shi & Banad (2026):
"the reference 𝑆 𝑔 is built through greedy marginal selection under the same
budget. We report question utility 𝑄(𝑆) = min(𝑉 (𝑆)/𝑉 (𝑆 𝑔 ), 1), which ranges
from zero to one and is higher when more of the greedy reference value is
retained."[^c1]

The **timing head** maps a separately fitted urgency score to one of five
fixed delays: "The rule maps ℎ ≥ .75 to 30 minutes, ℎ ≥ .60 to 60, ℎ ≥ .38 to
180, ℎ ≥ .20 to 240, and lower values to 720."[^c2]

A supervised, LoRA-adapted instruction language model (Gemma 4 E4B) then
receives the head's proposal and observed history and returns a final item
set, delay, and rationale — the **hybrid**.

## Known as

| Field | Name there | Relation |
|---|---|---|
| Human-AI interaction (this paper) | EMA-E4B | exact — the specific fitted system this note describes |
| Psychology / EMA research | adaptive ecological momentary assessment | close — the general design class (adapting item set and/or timing to the respondent); other systems in this class (JITA EMA, Ask Less Learn More) use different mechanisms and are not this note's object |
[^c3]

## Why it matters

On the reused 75-case development cohort, the LM layer changed the head's
proposed item set in roughly half the cases but did not raise the metric the
system itself is scored on: "Hybrid minus head question utility was −0.020,
with a descriptive participant resampling range of [−0.041, 0.002]. The
hybrid preserved the head delay in every case but preserved the head
question set in 38 of 75 cases, or 50.7%."[^c4]

Despite that null result on the quantitative endpoint, a domain-expert
reviewer preferred the hybrid's complete response over the head-driven
baseline in most decisive pairwise comparisons: "The reviewer selected
EMA-E4B in 15 cases, original E4B in five cases, and a tie in two cases. The
decisive hybrid preference was 75%."[^c5]

For a stall-2 practitioner this is a caution about what "helps with
selection" means: a wrapper can be preferred on the complete response
(rationale, framing, forecast) while leaving the underlying axis-choice
unchanged or slightly worse by the system's own utility score — the two
endpoints must be measured separately, not inferred from one another.

## Limits

The expert comparison rests on **one non-blinded reviewer who is a study
co-author**, 22 cases, no registered stopping rule: "The available review
record does not establish response identity masking or randomized display
order, and the retained portal interface identifies the training
conditions. We therefore do not claim a blinded expert comparison."[^c6]
The item- and timing-utility coefficients (0.42, 0.23, 0.20, …) are
researcher-specified, not derived from a validated information- or
decision-theoretic criterion, and the 75-case benchmark reuses cases already
seen while preparing the expert review, so it is descriptive, not a fresh
confirmatory test. The population is 79 psychology students in one 2020
lockdown study; nothing here bears on generalization past that setting or
past mental-health EMA items.

## Related

[[generalized-binary-search]] · [[adaptive-submodularity]] · [[value-of-information]]

[^c1]: ahmadi-2026 — "the reference 𝑆 𝑔 is built through greedy marginal selection under the same budget. We report question utility 𝑄(𝑆) = min(𝑉 (𝑆)/𝑉 (𝑆 𝑔 ), 1), which ranges from zero to one and is higher when more of the greedy reference value is retained."
[^c2]: ahmadi-2026 — "The rule maps ℎ ≥ .75 to 30 minutes, ℎ ≥ .60 to 60, ℎ ≥ .38 to 180, ℎ ≥ .20 to 240, and lower values to 720."
[^c3]: ahmadi-2026 — "We present and retrospectively evaluate EMA-E4B, a hybrid framework for question selection and prompt timing."
[^c4]: ahmadi-2026 — "Hybrid minus head question utility was −0.020, with a descriptive participant resampling range of [−0.041, 0.002]. The hybrid preserved the head delay in every case but preserved the head question set in 38 of 75 cases, or 50.7%."
[^c5]: ahmadi-2026 — "The reviewer selected EMA-E4B in 15 cases, original E4B in five cases, and a tie in two cases. The decisive hybrid preference was 75%."
[^c6]: ahmadi-2026 — "The available review record does not establish response identity masking or randomized display order, and the retained portal interface identifies the training conditions. We therefore do not claim a blinded expert comparison."
