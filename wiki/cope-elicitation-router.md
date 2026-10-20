---
description: "COPE is a mixture-of-experts conversational recommender whose hierarchical router selects, per dialogue turn, whether to elicit, recommend, or converse, and which elicitation strategy to use."
aliases: ["COPE", "COnversational Preference Elicitation via Mixture of Experts"]
sources: ["xia-2026"]
---
# COPE (conversational preference elicitation via mixture of experts)

> An architecture that turns "when and how to ask" into a per-turn routing
> decision made by a small classifier sitting on top of a frozen LLM.

## Definition / Mechanism

Xia, Zhang & Wang (2026) describe COPE as a set of
task-specialized experts sharing one frozen LLM [[backbone-of-a-formula|backbone]]: "COPE integrates
multiple expert modules to explicitly model heterogeneous behaviors in
CRSs. All experts share a common LLM backbone and differ only by
lightweight, expert-specific parameters that are added alongside the frozen
weights."[^c1]

A hierarchical router, computed from the backbone's final hidden state at
each turn, decides which expert fires: "we introduce a learned two-stage
router (task and elicitation) that dynamically determines which expert is
activated at each conversational turn, as well as the choice of strategies
if preference elicitation is predicted to be necessary."[^c2]

The first stage picks among {elicit, recommend, general interaction}; only
when it picks "elicit" does the second stage pick among {attribute-based,
item-based, hybrid}. Training uses teacher-forced routing (the
ground-truth turn label activates the expert, so each expert trains only on
its own behavior); at inference the router's own prediction selects the
expert instead.

On the authors' InPE benchmark, "COPE achieves the highest recall across
all 𝑘 values, consistently outperforming baselines from all three
categories" of prior conversational-recommendation systems.[^c3]

## Why it matters

COPE operationalizes [[stage-dependent-elicitation-strategy]]: rather than
committing a system to one elicitation style, it makes "attribute question,
item comparison, or no question at all" a learned, per-turn decision
conditioned on dialogue context, trained on human-labeled turns rather than
a hand-written heuristic for stage detection.

## Limits

Evaluated on one dataset (InPE, derived from INSPIRED, a single domain and
one LLM backbone, Qwen3-8B with LoRA adapters); the routing labels the
router is trained to predict come from the same crowd-annotation process
used to build the training data, so the reported recall gain reflects
imitating those annotators' strategy choices, not an independent measure of
which strategy actually shortens the path to a satisfied user. The paper
gives no ablation isolating the router's contribution from the underlying
LLM backbone's capacity in the extract read here.

## Related

[[stage-dependent-elicitation-strategy]] · [[adaptive-submodularity]] · [[optimal-decision-tree]]

[^c1]: xia-2026 — "COPE integrates multiple expert modules to explicitly model heterogeneous behaviors in CRSs. All experts share a common LLM backbone and differ only by lightweight, expert-specific parameters that are added alongside the frozen weights."
[^c2]: xia-2026 — "we introduce a learned two-stage router (task and elicitation) that dynamically determines which expert is activated at each conversational turn, as well as the choice of strategies if preference elicitation is predicted to be necessary."
[^c3]: xia-2026 — "COPE achieves the highest recall across all 𝑘 values, consistently outperforming baselines from all three categories."
