---
description: "Across eight AI advisory response styles, the most-preferred style gave no measurable accuracy gain, and the style with the largest gain ranked only mid-pack in preference."
aliases: ["accuracy-preference divergence", "preference does not track accuracy"]
sources: ["sabouri-2026"]
---
# Rhetorical-pattern accuracy-preference divergence

> A user's stated preference among an AI's response styles is not a proxy
> for which style makes them more correct.

## Definition / Mechanism

Sabouri et al. (2026) tested eight response rhetorics an AI advisor could
use on a fact-verification task (n = 98, within-subject), then asked
participants to rank all eight from most to least preferred after exposure
to every one. A Friedman test found preferences differed significantly
across patterns (χ²(7) = 160.4, p < 0.001); the direct-answer baseline
(Oracle) — the pattern with the largest significant accuracy gain — ranked
only mid-pack (mean rank 4.55 of 8), while the most-preferred pattern
(Alternative Framing, mean rank 2.52) produced no accuracy gain that
survived correction (p = 0.088).[^c1]

The authors state the result directly: "Oracle produced the largest
accuracy gains yet ranked only mid-pack, while the most-preferred pattern,
Alternative Framing, produced no accuracy gain that survived correction."
[^c2]

Participant comments attribute the preference to brevity and ease rather
than correctness: patterns were liked for being "short and sweet," "easy
to understand," and disliked for imposing extra reading or extra
questions — independent of whether they helped participants reach the
right answer.[^c3]

## Why it matters

For an answerer deciding how to phrase a response (stall 10: how much to
commit, and how to say the rest), this is a direct measurement that
optimising for what users say they want — brevity, confidence, no
follow-up questions — is not the same objective as optimising for
correctness, and the two can trade off in opposite directions within the
same interaction.

## Limits

- One study, one task domain (fact verification with hint-on-demand);
  preference was measured once, after exposure to all eight patterns in
  sequence, not per-claim, so order and fatigue effects on the ranking are
  not separated from genuine preference.
- The accuracy side of the divergence rests on the paper's own qualifier
  that its accuracy deltas are "directional signals rather than stable
  effect sizes" [?], so the size of the gap, not its direction, is the
  less certain part of this claim.
- Preference here is a post-hoc ranking of named styles, not a live choice
  under which style to request next; whether the divergence holds when
  users choose a style in advance is not tested.

## Related

[[socratic-questioning-response-pattern]] · [[value-of-information]] · [[expected-utility]]

[^c1]: sabouri-2026
[^c2]: sabouri-2026 — "Oracle produced the largest accuracy gains yet ranked only mid-pack, while the most-preferred pattern, Alternative Framing, produced no accuracy gain that survived correction"
[^c3]: sabouri-2026
