---
description: "Distractors anchored to a problem's own entities, attributes and events fall in three classes; related-entity ones break chain-of-thought models most (46-94% error)."
aliases: ["Related Entity Distractors", "Orthogonal Attribute Distractors", "Null-Effect Event Distractors", "structurally anchored distractors"]
sources: ["arxiv-2601-06853"]
---
# Anchored distractor taxonomy in math problems

Irrelevant sentences differ in how hard they are to discard. Randomly appended sentences can be removed by surface heuristics; distractors that reuse the problem's own entities, attributes or events cannot. The work builds such distractors in three classes and measures each separately on Bangla math problems.

**The three classes.** Related Entity Distractors give a number about the same kind of object as the query target but tied to a different entity or context. Orthogonal Attribute Distractors add a property of an entity already present, measured in a dimension different from the one asked. Null-Effect Event Distractors describe events with zero net effect: planned but not executed, done then reversed, or explicitly counterfactual.[^c1]

**Why anchoring matters.** Each inserted sentence references existing entities, events or attributes, so it is "semantically integrated into the problem and cannot be filtered through surface-level heuristics, unlike randomly appended irrelevant sentences."[^c2] The generator only proposes distractor sentences with insertion positions and does not rewrite the original text, so the answer is unchanged.[^c3]

**What it does to answerers.** Under 5-shot chain-of-thought, accuracy fell by up to 40.7 points (Qwen 2.5 3B, 53.7% to 13.0% on MSVAMP).[^c4] Related-entity distractors were the most disruptive (46-94% error), orthogonal-attribute 24-81%, null-effect 27-86%; the paper reads this as systematic rather than category-specific.[^c5] The first class is the entity-disambiguation failure: models cannot separate quantities about the focal entity from those about peripheral ones.[^c5]

A question writer can use the taxonomy as a checklist of what a wrongly relevant-looking sentence can be: wrong entity, wrong dimension, or cancelled event. This reading is my inference.

## Limits

Measured only on Bangla translations of MGSM and MSVAMP (3,685 problems) with seven 3B-12B open models. The classes were validated by GPT and human experts but the paper does not show that the three classes are exhaustive or independent. The ranking of classes is by error-rate ranges across models, not a controlled comparison of matched sentences. Whether the ordering holds in English or for larger models is untested here.

## Related

- [[distractor-strength-reward-signal]] — there distractor strength is measured by model choice frequency in multiple-choice answers; here by error rate by sentence class in the stem.
- [[entity-agnostic-reasoning-skeleton]] — another way of separating the reasoning structure from entity surface content.

[^c1]: arxiv-2601-06853 — "Null-Effect Event Distractors (NEED) introduces descriptions of events involving the problem’s main entities that have zero net impact on"
[^c2]: arxiv-2601-06853 — "they are semantically integrated into the problem and cannot be filtered"
[^c3]: arxiv-2601-06853 — "This ensures the core problem text and its"
[^c4]: arxiv-2601-06853 — "accuracy drops up to 40.7"
[^c5]: arxiv-2601-06853 — "are most disruptive (46–94% error rate)"
