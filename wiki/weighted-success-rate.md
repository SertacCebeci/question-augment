---
description: "A navigation-success metric that discounts task success by the exponentiated cumulative cost of the questions the agent asked en route."
aliases: ["Weighted Success Rate", "WSR"]
sources: ["zhao-2026"]
---
# Weighted Success Rate

> A success metric for interactive navigation that prices every question the agent asked, so an agent that reaches the goal by asking cheaply outscores one that reaches it by asking heavily — success alone (SR) cannot tell them apart.

## Definition / Mechanism

For an episode $e$ with final distance $d_e$, success threshold $\tau$, and questions $q_{e,1},\dots,q_{e,N_e}$ of types $\mathrm{type}(q_{e,i})$ each carrying a locked per-type cost $w_t$:

$$\mathrm{WSR}_e(\tau) = \mathbf{1}[d_e \le \tau]\cdot \exp\Big(-\sum_{i=1}^{N_e} w_{\mathrm{type}(q_{e,i})}\Big)$$

"Standard SR ignores how much oracle information was consumed. We therefore charge each question by its per-type cost wt from Eq. (2) and define the episode score" — "The discount lies in [0,1], repeated questions are charged repeatedly, and successful no-question episodes reduce to plain success. Failed episodes receive zero."[^c1]

On the paper's own benchmark, the ranking WSR produces differs from the ranking plain SR would: "TANDEM achieves 35.3 SR@1.5 and 21.4 Weighted SR, consistently outperforming prior approaches" while baselines that ask more questions under unconstrained interaction do not translate the extra queries into a corresponding SR gain, and score far lower once those queries are priced.[^c2]

## Known as

| Field | Name there | Match |
|---|---|---|
| Robotics / VLN | Weighted Success Rate | exact |
| Robotics / VLN | WSR | exact (abbreviation) |

## Why it matters

It answers, for one stall of this wiki, not "is $|W|$ small enough" but "did the interaction that got you there pay for itself" — a per-episode, retrospective price on the whole question sequence rather than a per-question value like [[value-of-information]] or [[expected-information-gain]].

## Limits

The metric depends entirely on the per-type costs $w_t$, which are mined from five navigation corpora and locked for this benchmark's four question types (Table 1 of Zhao (2026)); WSR numbers are comparable only across agents scored under the same locked taxonomy and threshold $\tau$, not as an absolute or cross-domain currency. The exponential discount is a design choice for this benchmark, not derived from a decision-theoretic axiom the way [[value-of-information]] is from [[expected-utility|expected utility]] — it penalizes every extra question multiplicatively regardless of whether that question was the one that mattered.

## Related

[[value-of-information]] · [[expected-information-gain]] · [[sensitivity-weighted-question-score]] · [[cross-type-eig]]

[^c1]: zhao-2026 — "Standard SR ignores how much oracle information was consumed. We therefore charge each question by its per-type cost wt from Eq. (2) and define the episode score:"
[^c2]: zhao-2026 — "TANDEM achieves 35.3 SR@1.5 and 21.4 Weighted SR, consistently outperforming prior approaches."
