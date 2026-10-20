---
description: "In a two-week deployment, immediate LLM-interaction ratings diverged from later ratings of the same interaction, most on accuracy and clarity, with trust shifting upward significantly."
aliases: ["temporal preference divergence", "immediate vs delayed preference shift", "directional asymmetry index"]
sources: ["gebreegziabher-2026"]
---
# Immediate–delayed preference divergence

> A rating collected right after an LLM reply is not a stand-in for the
> rating the same person gives once they have acted on it — and the two
> do not drift apart uniformly across dimensions.

## Finding

Gebreegziabher, Sproul, Yang, Chen, Gómez-Zará & Li (2026)
deployed BITE (see [[outcome-aware-follow-up-elicitation]]) with 8
participants for two weeks, collecting an immediate rating after each of
182 LLM conversations and a delayed rating after a matched downstream
event. Comparing the two: "Across relevance and trust, rating differences
are generally centered slightly above zero... Accuracy and clarity
exhibited the largest variability in rating deltas. In particular,
accuracy shows a wide distribution spanning both positive and negative
values... In contrast, harmfulness ratings remain tightly clustered around
zero, with a slight shift toward negative values."[^c1]

The divergence is not uniform in direction either. Using a Directional
Asymmetry Index, $DAI = (N_{up}-N_{down})/(N_{up}+N_{down})$, computed per
dimension from the counts of upward and downward revisions, "only trust
exhibits a statistically significant shift between immediate and delayed
evaluations (Wilcoxon signed-rank test, p = 0.045). Trust ratings show
strong positive asymmetry (DAI = 0.60), with 80% of revisions increasing
compared to 20% decreasing."[^c2]

Harmfulness moved the opposite way: "harmfulness shows the opposite
pattern, with all observed changes reflecting increased perceived harm,"
though this trend did not reach significance (p = 0.083).[^c3]

## Why it matters

This is a measured counterexample to treating a single post-interaction
rating as the constraint an asking pipeline should optimize against
(stall 2's value-of-a-question criteria, e.g. [[expected-information-gain]],
implicitly assume the observed answer is stable): accuracy and trust are
the dimensions most likely to be re-scored once the user has acted, and
trust specifically moves in one direction (up) rather than merely
fluctuating with noise.

## Limits

- N = 8 participants, 182 conversations, one two-week window; only trust's
  shift reaches significance (p = 0.045) — clarity (p = 0.068) and
  harmfulness (p = 0.083) are reported as trends, not established effects.
- The divergence is measured only where a matched downstream Gmail event
  triggered a follow-up prompt (see [[outcome-aware-follow-up-elicitation]]);
  interactions with no detected downstream event are not represented in
  this comparison, so the finding cannot be read as a base rate over all
  LLM interactions.
- Homework/assignment use dominates the captured sample (69% of the 182
  conversations), so the divergence pattern may not generalize evenly
  across the nine tracked topics.
- Read from the archived arXiv preprint text extract only; unverified [?]
  as of this draft.

## Related

[[outcome-aware-follow-up-elicitation]] · [[value-of-information]] · [[expected-information-gain]] · [[preference-optimization-for-questions]]

[^c1]: gebreegziabher-2026
[^c2]: gebreegziabher-2026
[^c3]: gebreegziabher-2026 — "harmfulness shows the opposite pattern, with all observed changes reflecting increased perceived harm"
