---
description: "A controlled study found that letting an informant decide unprompted what to teach costs more self-reported effort than a system that raises the question itself, though overall workload is unchanged."
aliases: ["gap-monitoring burden", "knowledge-gap monitoring burden"]
sources: ["hu-2026"]
---
# Gap-monitoring burden

> Leaving the informant to notice on their own what a system still does not
> know is itself a cost — separate from, and larger than, the cost of
> answering once asked.

## Definition / Mechanism

Hu et al. (2026) ran a within-subjects study (N = 18) comparing
three teaching conditions for a household robot learning personalized
object facts: User-Led Teaching (the user decides what to teach and when),
Post-Task Questioning (the robot asks after the task), and In-Task
Questioning / EgoAsk (the robot asks during the task, selected by
[[activity-relevance-gap-selection|activity relevance]]). A 3-item scale
("gap-monitoring burden," Cronbach's α = .84) measured the reported need to
"continually assess missing information, worry about omissions, and
proactively supply or confirm information."[^c1]

Scores differed across conditions (Friedman χ²(2) = 11.58, p = .003):
User-Led Teaching (M = 4.67) was rated higher-burden than both Post-Task
Questioning (M = 2.87, p = .002, r = .74) and EgoAsk (M = 2.72, p = .007,
r = .64); the two robot-initiated conditions did not differ from each other
(p = .648). Overall workload (the six NASA-TLX dimensions) did not differ
significantly across the three conditions (χ²(2) = 1.21, p = .546).[^c2]

Timing carried a separate cost: on the single item measuring need to
reconstruct the handling context, Post-Task Questioning (M = 5.33) scored
higher than both EgoAsk (M = 3.56, p = .004, r = .68) and User-Led Teaching
(M = 3.94, p = .018, r = .56), with no significant difference between
User-Led Teaching and EgoAsk (p = .204). 11 of 18 participants (61%) ranked
EgoAsk first overall.[^c3]

## Why it matters

This gives stall 2 a cost argument, not just a value argument: who selects
the axis changes not only what gets asked but how much *unprompted
monitoring* the informant must do to notice a gap exists at all — a cost
that sits outside [[expected-information-gain]] or [[value-of-information]]
accounting, both of which price the answer, not the labor of noticing the
question is needed.

## Limits

- Single 2026 arXiv preprint, not independently verified by this wiki [?];
  `replicated: false` — one lab study, N = 18, in one domain (household
  object-tidying via smart glasses).
- Self-report burden on a study-specific 3-item scale, not a behavioral or
  time measure; the paper itself found a companion 3-item scale
  (context-reconstruction) had low internal consistency (α = .28) and had
  to be analyzed item-by-item, so the instrument's [[calibration|reliability]] is uneven
  across its own subscales.
- The two robot-initiated conditions were statistically indistinguishable
  on this measure (p = .648); the finding supports "system asks" over
  "informant self-monitors," not any claim about *when* within a task the
  system should ask.
- Timing trades one cost for another: In-Task Questioning had the numerically
  highest interruption burden of the three conditions (M = 3.20), though the
  omnibus test on interruption did not reach significance (p = .096).

## Related

[[activity-relevance-gap-selection]] · [[value-of-information]] · [[proactive-expertise-clarification]] · [[intervention-advantage]]

[^c1]: hu-2026 — "We recruited 18 participants through laboratory convenience sampling for a study on teaching a household robot about personal objects with smart glasses."
[^c2]: hu-2026 — "User-Led Teaching (𝑀 = 4.67) was higher than Post-Task Questioning (𝑀 = 2.87, 𝑝 = .002, 𝑟 = .74) and EgoAsk (𝑀 = 2.72, 𝑝 = .007, 𝑟 = .64). No significant difference was detected between Post-Task Questioning and EgoAsk (𝑝 = .648)."
[^c3]: hu-2026 — "Post-Task Questioning (𝑀 = 5.33) was higher than EgoAsk (𝑀 = 3.56, 𝑝 = .004, 𝑟 = .68) and User-Led Teaching (𝑀 = 3.94, 𝑝 = .018, 𝑟 = .56)."
