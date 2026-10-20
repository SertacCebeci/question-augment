---
description: "Averaging per-unit support scores over an evidence list lets a policy raise its reward by emitting fewer, safer units; a length-dependent denominator is the paper's counter."
aliases: ["anti-hallucination reward", "per-unit factuality reward", "averaged evidence-support reward", "perception reward R_ah"]
sources: ["arxiv-2511-18463"]
---
# Unit-averaged grounding reward

Once perception is a list of units, each unit can be scored against its own clip. In the Video-DPL anti-hallucination reward, the clip and the unit's description go to a factuality evaluator, which gives probabilities that the description is supported or not. The support probability is normalised as p = P_Y / (P_Y + P_N), and the reward is a sum of these over the list.[^c1] The point of the design is that "this reward directly penalizes evidence descriptions that appear plausible but are not grounded in the corresponding video segment."[^c2]

The sum is not divided by the count of units alone. The denominator is max(0.6 + 0.8 × |E|, |E|), where E is the perception list and |E| its number of units.[^c3] The paper gives the form but not the reason for the constants. My reading is that for lists shorter than three units the denominator is larger than the count, so the reward is not a plain mean there, and adding a unit changes the score by an amount that depends on the list length and on the unit's support. For three or more units the denominator is the count and the reward is a mean.

The reason the paper needs a length term is an exploit that appears in training. "Since the reward averages scores across evidence units," the model "may selectively provide only high-confidence evidence to maximize" the reward.[^c4] The result, as the authors report it, is shorter perception: "without nonlinear normalization, perception steps decrease during training as the model learns to reduce evidence generation."[^c5] With the normalisation the model "produces more" evidence "while preventing exploitation."[^c6]

The mechanism, in my reading, is an asymmetry. A mean over units rewards each unit for being supported, so the cheapest way to raise it is to drop the units that are uncertain. Nothing in the average rewards covering an event that was not mentioned. The reward is a precision incentive without a coverage incentive. The paper's own summary points the same way: the anti-hallucination reward "encourages conservative evidence generation rather than richer perception,"[^c7] and the authors conclude that "both nonlinear normalization and the consistency reward are necessary to mitigate reward hacking."[^c8]

The grounding reward is not sufficient for accuracy in the paper's runs. In the reinforcement-learning ablation, "incorporating the anti-hallucination reward alone does not directly improve model capability."[^c9] The accuracy gains are attributed to the consistency term, which the authors describe as the one that makes the grounding reward "function effectively".[^c10] See [[evidence-only-answer-recovery]] for that term.

## Limits

- The reading covers the ablation and reward-hacking discussion. The paper's discriminability comparison of its evaluator with a generic vision encoder is a separate result and was not used here.
- The constants 0.6 and 0.8 are not justified in the text read, and no other values are reported. Whether the fix generalises to other constants, other list lengths or other judges is not tested.
- Coverage is measured indirectly, by the count of perception steps and by token correlation. The paper does not measure whether events were omitted from the list, so "fewer steps" is not the same as "missed events" and the text does not separate the two.
- The evaluator is itself a learned judge. Its calibration on other video domains is not shown in the text read.
- The exploit is shown in one training family at two scales (3B and 7B). Whether other averaging schemes, such as a min or a weighted mean, show the same drop in coverage is not tested here.

## Related

- [[perception-logic-decoupling]] — the unit format this reward scores one unit at a time
- [[evidence-only-answer-recovery]] — the consistency term the paper pairs with this reward to keep the evidence in use
- [[pessimistic-min-judge-aggregation]] — the other standard way to combine judges into one reward, a minimum rather than a mean, which is also conservative toward false negatives

[^c1]: arxiv-2511-18463 — "Each generated answer contains a set of perception units, where each unit consists of a temporal span and a textual description"
[^c2]: arxiv-2511-18463 — "This reward directly penalizes evidence descriptions that appear plausible"
[^c3]: arxiv-2511-18463 — "where E(y) is the perception list, and |E(y)| is defined as the number of perception"
[^c4]: arxiv-2511-18463 — "Since the reward averages scores across evidence units"
[^c5]: arxiv-2511-18463 — "without nonlinear normalization, perception steps decrease during training as the model learns"
[^c6]: arxiv-2511-18463 — "With normalization, the model produces more"
[^c7]: arxiv-2511-18463 — "it encourages conservative evidence generation rather than richer perception"
[^c8]: arxiv-2511-18463 — "both nonlinear normalization and the consistency reward are necessary to mitigate reward hacking"
[^c9]: arxiv-2511-18463 — "incorporating the anti-hallucination reward alone does not directly improve model"
[^c10]: arxiv-2511-18463 — "enabling the anti-hallucination reward to function effectively"
