---
description: "A non-target persona attribute declared with a direction stops leaking into the target response, but declared neutral it keeps leaking: a neutrality gap in persona prompts."
aliases: ["neutral-declaration leakage", "directional versus neutral non-target preservation", "non-target preservation gap"]
sources: ["doi-10-48550-arxiv-2609-35036"]
---
# Neutrality gap

A persona prompt sets a target attribute, say risk preference, and the question is whether its effect stays on that target. A second attribute the prompt does not otherwise constrain, say colour saturation, is the non-target. What the prompt says about the non-target changes how well it is kept still. The paper separates three states: the non-target left unspecified, declared directional, or declared neutral. A directional declaration gives the non-target a signed value, as in "The user strongly prefers muted, understated finishes." A neutral declaration says the user has "no consistent leaning in colour saturation."[^c1]

The gap is the difference between the two declared states under otherwise identical prompts. The authors define it that way: "We define the neutrality gap as this difference".[^c2] Directional declarations work. Models "follow a stated direction but do not preserve a declared" neutral state, which is the asymmetry in one line.[^c3] In a post hoc analysis of independent items, neutral declarations left 51–81% of items target-sensitive, with the no-declaration baseline at 67–93%, against at most 1 of 320 item–pole comparisons under directional declarations.[^c4] The non-target answer was stable under a direction and not under neutrality, so the target was still moving the answer that the prompt had declared it should not move.

The mechanism the paper offers is trait-conditioned completion. The target trait is read as evidence about the user and carried into unstated attributes the model associates with it.[^c5] The paper does not establish why a direction blocks this while a neutral declaration does not. My inference, which the paper does not test: a direction gives the model a value to follow, which overrides the inferred profile; a neutral declaration gives it nothing to follow, so the inferred profile fills the slot. This is a conjecture and should be read as one.

The gap changes how a persona test is read. A directional test can be passed by following the persona, so a model that moves only the target and a model that also drags the non-target both pass it. The neutral state is the case that separates them. The paper's phrasing is that a model "can play the described user faithfully and still change more than the intended attribute."[^c6]

## Limits

- The field audit covers one attribute pair. "The field audit covers one attribute pair," and the neutral-declaration and internal analyses run on five open-weight checkpoints only, because the black-box APIs do not uniformly expose the answer probabilities or hidden states they need.[^c7]
- The 51–81% figure comes from a post hoc analysis of independent items, not from a pre-specified test of the gap.[^c8]
- No tested prompt design reliably preserves a declared neutral state. "Preserving declared neutrality is the open problem these results pinpoint."[^c9] The one remedy tested in ten-turn dialogues, a scope-and-default instruction, reduced the influence on all eight black-box models, yet kept it below the prespecified floor at every measured turn on only three of them (my reading of the appendix summary).
- Materials are English and text-only.[^c10] The gap is defined by what the prompt states, so it says nothing about whether the inferred preferences match real people.

## Related

- [[persona-attribute-confounding]] — the mechanism-level account of leakage from one attribute into correlated ones; the neutrality gap is its measured, declaration-dependent form
- [[selective-persona-control]] — the requirement the gap violates: the target moves, the non-target must not

[^c1]: doi-10-48550-arxiv-2609-35036 — "no consistent leaning in colour saturation"
[^c2]: doi-10-48550-arxiv-2609-35036 — "We define the neutrality gap as this difference"
[^c3]: doi-10-48550-arxiv-2609-35036 — "models follow a stated direction but do not preserve a declared"
[^c4]: doi-10-48550-arxiv-2609-35036 — "51–81% of items target-sensitive"
[^c5]: doi-10-48550-arxiv-2609-35036 — "Trait-conditioned completion then carries the stated trait into unstated attributes the model associates with"
[^c6]: doi-10-48550-arxiv-2609-35036 — "A model can play the described user faithfully and still change more than the intended attribute"
[^c7]: doi-10-48550-arxiv-2609-35036 — "The field audit covers one attribute pair"
[^c8]: doi-10-48550-arxiv-2609-35036 — "In a post hoc analysis of independent items"
[^c9]: doi-10-48550-arxiv-2609-35036 — "Preserving declared neutrality is the open problem these results pinpoint"
[^c10]: doi-10-48550-arxiv-2609-35036 — "Materials are English and text-only"
