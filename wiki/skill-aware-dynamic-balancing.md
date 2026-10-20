---
description: "A reward bonus scaled to how far a skill's recent frequency falls below average, pushing a self-training questioner away from over-rewarded skills toward broad coverage."
aliases: ["skill-aware dynamic balancing", "skill bonus", "skill-stratified sampling"]
sources: ["xu-2026-rise"]
---
# Skill-aware dynamic balancing

> In a self-evolving questioner-solver loop, mode collapse toward a few
> easy-to-reward question types is countered by rewarding under-represented
> skill categories in proportion to how far below average their recent
> frequency has fallen, and by stratifying the final training set across
> categories.

## Definition / Mechanism

Xu et al. (2026) observe that without intervention, a
questioner trained to maximize a difficulty/validity reward drifts toward
whichever question types pay off most easily: "During self-evolution, the
questioner tends to gradually favor a few skills that yield higher reward
more easily, such as counting or math. Such mode collapse makes the
generated questions increasingly narrow and limits the range of reasoning
skills the model can acquire."[^c1]

Over a fixed skill set $K$ of six declared categories (coarse perception,
fine-grained perception, instance reasoning, logical reasoning, math &
counting, science & technology), the method tracks each skill's recent
question count $n_k$, computes the average $\bar n$ across $K$, and adds to
the questioner's reward a bonus $b_{skill}(k) = \max(\bar n - n_k, 0)/\bar n$
for a question declared as skill $k$: "only relatively under-represented
skills receive additional reward, while dominant skills receive no extra
encouragement."[^c2]

The same balancing is applied a second time, downstream of generation: "We
further apply skill-stratified sampling when constructing the final
pseudo-labeled data, by drawing approximately equal-sized subsets from the
six skill categories, so that skill balancing affects both question
generation and solver training."[^c3]

## Why it matters

For this stall, mode collapse is a selection failure at the level of the
*axis*, not the individual question: a criterion that only scores
questions one at a time ([[mutual-information|mutual information]], EIG, self-consistency
difficulty) has no memory of which axis has already been oversampled, so
nothing in a per-question score alone stops the same axis from being
picked every round. This method adds that memory explicitly, as a
frequency-tracking correction layered on top of a per-question reward
rather than replacing it.

## Limits

The skill taxonomy is fixed and hand-declared (six categories, tagged by
the questioner itself as part of its output), so the correction can only
balance across axes the system already names — an emergent skill outside
$K$ is invisible to $b_{skill}$ the same way an unmodelled axis is invisible
to any selection criterion. Results are reported only for the full RISE
pipeline (fine-grained alternation + quality supervisor + skill balancing
together) on two Qwen-VL backbones; the extract read here does not isolate
skill-aware balancing's own contribution with an ablation.

## Related

[[self-evolving-visual-questioner]] · [[self-questioning-vlm-grpo]] · [[adaptive-submodularity]] · [[expected-information-gain]]

[^c1]: xu-2026-rise — "During self-evolution, the questioner tends to gradually favor a few skills that yield higher reward more easily, such as counting or math. Such mode collapse makes the generated questions increasingly narrow and limits the range of reasoning skills the model can acquire."
[^c2]: xu-2026-rise — "only relatively under-represented skills receive additional reward, while dominant skills receive no extra encouragement."
[^c3]: xu-2026-rise — "We further apply skill-stratified sampling when constructing the final pseudo-labeled data, by drawing approximately equal-sized subsets from the six skill categories, so that skill balancing affects both question generation and solver training."
