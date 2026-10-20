---
description: "In a physical-robot user study, naming the uncertain reward feature in a query yielded significantly better corrective demonstrations than an unguided request or a behavior rollout."
aliases: ["feature-based explanation query"]
sources: ["merker-2026"]
---
# Explanation-guided demonstration elicitation

> Telling a demonstrator, in words, which feature the robot is unsure
> about produces a better corrective demonstration than either asking
> plainly or showing the robot's current (mis)behavior.

## Definition / Mechanism

Twelve participants each gave corrective demonstrations to a real Franka
robot arm under three query conditions — Unguided (no context), Rollout
(the robot shows its current, misaligned behavior first), and Explanation
(a natural-language sentence naming the specific feature it is uncertain
about) — in a within-subjects design, reward [[recovery-postulate|recovery]] scored by
normalized ground-truth reward on the resulting demonstrations. A linear
mixed-effects model found a significant main effect of condition:
"We found a significant main effect of condition on normalized reward
improvement, F(2, 22) = 14.94, p < .001. Estimated marginal means revealed
that the Explanation condition (M = 0.021, SE = 0.005) yielded
significantly greater reward improvement than both Unguided (M = −0.018,
SE = 0.005; t = −6.31, p < .001) and Rollout (M = −0.016, SE = 0.005;
t = −6.06, p < .001). No difference was observed between Unguided and
Rollout."[^c1]

The advantage required weighting the resulting demonstrations by the
(known, in Explanation) fact that the demonstrator was told which feature
to attend to: "Within Explanation, all-weighted rewards (M = 0.021,
SE = 0.007) were higher than all-unweighted rewards (M = −0.017,
SE = 0.003), t(23) = 4.56, p < .001... when only all-weighted rewards were
analyzed, condition differences were not significant (all p ≥ .183),
leaving only a directional trend favoring Explanation."[^c2]

Cognitive workload (NASA-TLX) did not differ by condition: "We found no
significant effect of condition on NASA-TLX composite scores,
F(2, 22) = 0.76, p = .480."[^c3]

Subjective preference was split rather than favoring Explanation: "Five
of twelve participants preferred Explanation, five preferred Rollout, and
the remaining two preferred Unguided (exact multinomial vs. uniform:
χ² = 1.50, p = .616)."[^c4]

## Why it matters

This isolates the *formulation* half of a robot's question from its
*selection* half (see [[ambiguity-sensitive-querying]], which supplies the
feature this query names): even when the uncertain feature is correctly
identified beforehand, how that uncertainty is communicated to the
answerer changes the quality of the constraint that comes back — a
finding for the stall of turning a selected axis into an actual question,
not just for which axis to pick.

## Limits

N = 12, one task domain (tabletop manipulation), one robot, one fixed
explanation template ("I am uncertain about how to handle X"); the
Explanation condition's identification of the underspecified feature was
always correct by construction, so the result measures the effect of the
explanation's form, not of imperfect detection accuracy feeding into it.
The workload and preference null results are non-findings at this sample
size, not evidence of no effect.

## Related

[[ambiguity-sensitive-querying]] · [[value-of-information]] · [[clarification-request]] · [[target-ambiguity-triggers-clarification]]

[^c1]: merker-2026
[^c2]: merker-2026
[^c3]: merker-2026
[^c4]: merker-2026 — "Five of twelve participants preferred Explanation, five preferred Rollout, and the remaining two preferred Unguided (exact multinomial vs. uniform: χ2 = 1.50, p = .616)."
