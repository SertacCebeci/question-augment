---
description: "A rewording that drifts from the seed's meaning is an infinite loss, not a penalty, so a questioner cannot win by changing what was asked; intent is checked before any preference."
aliases: ["faithfulness gate", "intent-preserving attack gate", "seed-faithful rewrite reward"]
sources: ["arxiv-2512-20806"]
---
# Faithfulness-gated attack reward

A questioner that rewrites a seed can drift: the surface may stay while the request changes. Paulus et al. close this inside the reward rather than with a penalty term. Every attack query first passes through a judge that asks only whether it still means the seed: "use a binary pointwise faithfulness judge, which classifies"[^c1] attack queries as faithful or not. The stated purpose is that "the attacker does not completely change the underlying"[^c2] meaning of the original seed, so the rewording serves as a regulariser.

The gate is hard. "queries are treated as having infinite negative rewards, i.e.,"[^c3] an unfaithful attack, so "they will never be selected as the winner."[^c4] The defender side follows the same logic: when the attack is unfaithful, the paper gives no preference to learn from, because "query is not faithful to the seed query, we cannot give a"[^c5] meaningful choice between two responses.

**Mechanism, concretely.** Given two attack queries from the attacker, the comparison runs in three cases, as I read the paper's preference function (its Eq. 7): if only one attack is faithful, that one wins outright; if both are faithful, the judge compares their responses by category; if neither is faithful, the comparison is a tie at one half. Because an unfaithful attack can never win, the attacker's only route to a win is a rewording that keeps the seed's meaning and changes how the defender reads it.

**What transfers to asking (my inference).** A rewrite that introduces a different request, or quietly alters a constraint the answerer must honour, earns nothing under this scheme. The gate is on meaning, not on form. A question generator that is paid for an answer's failure would otherwise be free to drift toward whatever question is easiest to fail, and the gate removes that option.

**What does not transfer.** The gate needs a judge of meaning, and that judge is itself a model. The paper states that "in practice all our judge models are instantiated as a"[^c6] single model with varying templates, so the gate and the preference judge share one set of blind spots. Meaning-preservation in natural-language rewording is also a looser notion than the paper's binary check.

## Limits

- The text reports no ablation with the gate removed. The ablations in the sections I read cover the judge type, the moving-average generator, and a fixed attacker; the gate's contribution is not measured here.
- Faithfulness is binary and pointwise. Graded drift, where a question changes a little and then more, is either in or out, and the paper does not say where the line sits.
- The attacks are natural-language only: the approach "focuses exclusively on natural-language attacks that humans"[^c7] can read, so gradient-style or token-level rewrites fall outside the gate.
- The gate is defined relative to a seed and two classes (harmful, benign). A questioner without a seed, or with a continuous class, has no direct analogue.

## Related

- [[minimal-edit-prompt-attack]] — meaning-preserving rewording constrained by form (edit size and fluency), not by intent; the contrast is the point.
- [[non-zero-sum-attacker-reward]] — the other constraint on the same payoff: the attacker is paid for a category swap, not for any breakage.
- [[llm-red-teaming]] — the practice in which this gate is used.

[^c1]: arxiv-2512-20806 — "use a binary pointwise faithfulness judge, which classifies"
[^c2]: arxiv-2512-20806 — "the attacker does not completely change the underlying"
[^c3]: arxiv-2512-20806 — "queries are treated as having infinite negative rewards, i.e.,"
[^c4]: arxiv-2512-20806 — "they will never be selected as the winner."
[^c5]: arxiv-2512-20806 — "query is not faithful to the seed query, we cannot give a"
[^c6]: arxiv-2512-20806 — "in practice all our judge models are instantiated as a"
[^c7]: arxiv-2512-20806 — "focuses exclusively on natural-language attacks that humans"
