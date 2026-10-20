---
description: "Adding a system-generated third option raised its adoption from 2.7% to 20.0% over control in one decision study, so an alternative a person never articulated can enter the set they weigh."
aliases: ["choice expansion", "expanded choice architecture", "consideration set enlargement"]
sources: ["arxiv-2512-05397"]
---
# Consideration-set expansion

A choice is made from a consideration set: the options a person actually weighs. That set can be much narrower than the options that exist, because the person has not thought of them. The paper frames its question this way: whether AI can "expand participants’ consideration sets by introducing novel alternatives beyond their initially articulated options".[^c1] The mechanism under test is supply. Someone else puts an option into the set, rather than the chooser searching for it.

The paper's test is concrete. Participants first gave a pending decision, "providing two options" they were actively weighing.[^c13] In the expanded arm a third option was produced by the system, "introducing a novel Option C algorithmically generated from" the participant's stated goals and values.[^c2] Its example is a person weighing "Be a doctor" against "Be an engineer", offered a third path such as a bioengineering professor.[^c12] The paper's abstract states the claim as "surfacing previously unconsidered life paths".[^c3]

## What was measured

Against the control arm, the third option was taken up far more often. The paper reports that participants in the three-avatar condition chose the novel option more often: "participants in the three-avatar condition selected the novel third" option, "option at significantly higher rates (20.0%) compared to control participants (2.7%), p = 0.019, p < 0.05."[^c4][^c5] The authors read this as "a more than seven-fold increase in consideration" of alternatives outside the original pair: "than seven-fold increase in consideration of alternatives beyond the".[^c6]

The mechanism the paper proposes is legitimation as well as discovery: the avatars "introduce and legitimize novel decision paths that participants" which a person "may not have independently considered, thereby expanding the".[^c7][^c14] The paper does not separate these two. Its design gives no arm where the third option is offered as plain text without a vivid future self.

## Limits

- Selecting an option is not the same as considering it. The paper equates the two in its wording ("consideration of alternatives"), but the outcome is a choice. A person can weigh a path and reject it, which this measure would count as no expansion. My inference, not the paper's claim.
- The comparison is bundled. The third option arrived with a third avatar, and the control was guided imagination, with participants "assigned to control (guided imagination) or one of four avatar conditions".[^c8] The effect cannot be credited to the option alone, since the arms differ in the presence of a vivid, conversable future self as well as in the extra option.
- The generation method was one prompt: "our Option C generation relied on a single prompting".[^c15] The authors add that it "suggests substantial headroom for improvement."[^c9] So the 20% is a floor for this method, and it says nothing about what a better generator would add or whether a poor one would hurt.
- The outcome is intention, not behaviour: "we assessed decision intentions rather than implemented" choices.[^c10] Whether the new path was pursued is not measured.
- The sample is small per cell. The study has N=192: "(N=192) using multimodal synthesis".[^c11] Split across five arms, that is roughly 37 to 38 people per arm. My arithmetic: 2.7% and 20.0% are near 1 and 7 of about 37. The control rate may rest on a single participant, so the size of the jump is weakly estimated even though it is reported as significant.
- The paper's result is one population: young adults aged 18 to 28, with a decision drawn from each participant's own list. It does not show expansion for a decision a person has already settled, or for people who have no open options.

## Related

- [[future-self-simulation]] — the avatar that carries the third option in this study; the expansion result is one arm of the same design

[^c1]: arxiv-2512-05397 — "expand participants’ consideration sets by introducing novel alternatives beyond their initially articulated options"
[^c2]: arxiv-2512-05397 — "introducing a novel Option C algorithmically generated from"
[^c3]: arxiv-2512-05397 — "surfacing previously unconsidered life paths"
[^c4]: arxiv-2512-05397 — "participants in the three-avatar condition selected the novel third"
[^c5]: arxiv-2512-05397 — "option at significantly higher rates (20.0%) compared to control participants (2.7%), p = 0.019, p < 0.05."
[^c6]: arxiv-2512-05397 — "than seven-fold increase in consideration of alternatives beyond the"
[^c7]: arxiv-2512-05397 — "introduce and legitimize novel decision paths that participants"
[^c8]: arxiv-2512-05397 — "assigned to control (guided imagination) or one of four avatar conditions"
[^c9]: arxiv-2512-05397 — "suggests substantial headroom for improvement."
[^c10]: arxiv-2512-05397 — "we assessed decision intentions rather than implemented"
[^c11]: arxiv-2512-05397 — "(N=192) using multimodal synthesis"
[^c12]: arxiv-2512-05397 — "Be a doctor"
[^c13]: arxiv-2512-05397 — "providing two options"
[^c14]: arxiv-2512-05397 — "may not have independently considered, thereby expanding the"
[^c15]: arxiv-2512-05397 — "our Option C generation relied on a single prompting"
