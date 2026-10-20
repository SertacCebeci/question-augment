---
description: "Score clarification as one more candidate action on the shared ordinal scale used for navigation, so asking competes directly with acting at each step."
aliases: ["ACTION-RATING", "action rating", "self-gated clarification"]
sources: ["gao-2026"]
---
# ACTION-RATING

> Clarification is not a separate trigger bolted onto an agent's reasoning;
> it is one more action the agent scores on the same scale it uses for
> everything else it could do next.

## Definition / Mechanism

Gao, Kang, Wang & Woo (2026) model an agent navigating a
hierarchical taxonomy (30,000+ nodes) as an episodic MDP whose action set
includes `traverse_child`, `backtrack`, `jump`, `confirm`, and a dedicated
`need_clarify(q)` action. "We propose ACTION R ATING, a formulation that
addresses both problems by placing clarification inside the agent's own
action space... The agent scores candidate next actions, including a
dedicated clarification action, on a shared [0, 100] ordinal scale, so that
asking competes directly with acting at each decision point."[^c1]

Scoring the actions on one scale, rather than gating clarification on a
separate confidence threshold or a "ask if unsure" instruction, makes two
distinct information-seeking regimes fall out of the agent's own ratings
rather than being hand-labelled: "mandatory help, where clarification is
top-ranked and no navigation branch is viable, and opportunistic help,
where a leading branch exists but a targeted question can reduce residual
uncertainty before commitment."[^c2]

On Harmonized Tariff Schedule classification, turning the gate on (τ=10)
produces "a regime shift from mandatory to opportunistic clarification
(35.2%→13.9% mandatory; 0%→88.7% opportunistic)... Rating-only (τ=101)
retains the full scoring apparatus but disables the gating threshold so
that no clarification ever fires. Despite having the deliberation step, it
yields −0.9% and produces no opportunistic events, directly isolating
gating as the mechanism behind the regime shift."[^c3]

The scoring alone does nothing; the shared-scale competition together with
a threshold is what produces the mode split, not the volume of questions
asked. See [[information-seeking-effectiveness]] for the paper's local
usefulness measure of what each mode buys.

## Why it matters

Most clarification triggers in the literature (confidence thresholds,
sampling disagreement, prompted self-checks) sit outside the agent's
action-selection step and answer only "ask or not." ACTION-RATING makes
the *where* observable: mandatory asking marks a point with no viable
option at all, opportunistic asking marks a point with a leading option
whose uncertainty is still worth resolving before committing. That
distinction is exactly the stall-2 question of *which* decision point gets
a question, expressed as a byproduct of a single scoring pass rather than
a separate policy.

## Transfer

| | |
|---|---|
| Home field | Reinforcement learning / MDP action-value scoring, and LLM self-evaluation (rating a candidate output on a scale) |
| Here | An agent's per-step decision of whether to ask or to act at a hierarchical navigation choice point |
| What survives | Scoring every candidate action — including "ask" — on one shared scale, so the ask/act decision is read off the same ranking rather than a separate rule; the resulting mandatory/opportunistic split as an observable, not externally imposed, structure |
| What does not | The five-action taxonomy-navigation action set (`traverse_child`, `jump`, `confirm`, …), which presumes a discrete branching structure; "no viable branch" (mandatory mode) has no defined analogue outside a tree-structured action space |

## Limits

- The paper frames its own contribution as "a measurement protocol for
  self-gated information-seeking behavior under a controlled answer
  channel, not a deployment system; reported accuracy gains are upper
  bounds." The 50%→74% and mode-shift numbers this note reports depend on
  that controlled channel, not on real answer quality.[^c4]
- "Action scores are not calibrated. ACTION R ATING assumes the LLM
  produces meaningful ordinal scores but does not claim calibrated
  confidence estimation... τ may require re-tuning across models." The
  mandatory/opportunistic split is read from the model's own ratings, not
  from ground-truth epistemic states.
- Evaluated on one domain family (HTS classification, three benchmarks);
  generalization to structurally distinct taxonomies is stated as
  untested, and English-only.

## Related

[[value-of-information]] · [[entropy-threshold-clarification-trigger]] · [[clarification-request]] · [[information-seeking-effectiveness]]

[^c1]: gao-2026 — "We propose ACTION R ATING, a formulation that addresses both problems by placing clarification inside the agent’s own action space (Figure 1). The agent scores candidate next actions, including a dedicated clarification action, on a shared [0, 100] ordinal scale, so that asking competes directly with acting at each decision point."
[^c2]: gao-2026 — "mandatory help, where clarification is top-ranked and no navigation branch is viable, and opportunistic help, where a leading branch exists but a targeted question can reduce residual uncertainty before commitment."
[^c3]: gao-2026
[^c4]: gao-2026 — "We frame the contribution as a measurement protocol for self-gated information-seeking behavior under a controlled answer channel, not a deployment system; reported accuracy gains are upper bounds."
