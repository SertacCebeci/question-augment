---
description: "Bradley-Terry models a pairwise preference as a sigmoid of a reward difference; RLHF reward models and DPO's loss rest on it, and its transitivity assumption fails in practice."
aliases: ["Bradley-Terry model", "pairwise preference model", "BT model", "Bradley-Terry preference model"]
sources: ["arxiv-2601-06108"]
---
# Bradley-Terry preference model

The Bradley-Terry model is the usual way to turn a pairwise human choice into a number that a learner can fit. The work calls it "the foundational preference model for RLHF."[^c1] Given a reward function r, the probability that one response is preferred to another for the same prompt is a sigmoid of the difference of their rewards.[^c2] The reward enters only through that difference, so it is defined up to an additive constant.

Two consequences matter for what follows. The first is that the reward is scale-free in the sense that only differences are identified. The second is that preferences are assumed transitive: if y1 is preferred to y2 and y2 to y3, then y1 is preferred to y3 with high probability. The work states that "Both assumptions are violated" in practice.[^c3]

The work lists several ways the assumption fails. Human preferences can be intransitive: "Intransitivity. Human preferences exhibit cycles:" when different attributes dominate different comparisons. Annotators can differ, and then "binary comparisons cannot identify latent annotator" types from pairs alone.[^c4] The work reports the identification result for heterogeneous annotators, citing Qin et al.: rankings "over three or more" responses are needed.[^c5]

Two extensions appear in the work. For ranking several responses, "Plackett-Luce model generalizes Bradley-Terry:" the probability of a full ranking is a product of softmax-style choices over the items not yet placed.[^c6] For nontransitive preferences, the work says that "When preferences are nontransitive, the goal shifts from reward maximization" to finding a Nash equilibrium of a two-player game.[^c7]

## Limits

- The work states the assumptions and their violations; it does not measure how often real preference data is intransitive or how much heterogeneity matters in a given dataset.
- The identification result is cited to another paper. The work does not prove it, and the rankings-of-three requirement is stated as necessary, not as a sharp bound.
- The Nash formulation drops the reward assumption, but the work reports no comparison of its performance against the reward-based approach.
- The work also names prospect-theoretic and game-theoretic preference models among its pillars without developing them here, so the list of alternatives is incomplete in this note (my inference).

## Related

- [[dpo-implicit-reward]] — DPO substitutes its implicit reward into this model, so it inherits these assumptions
- [[coverage-separation-offline-online]] — the offline methods fit this model to a fixed dataset of pairs
- [[elicitation-transform-types]] — uses a Bradley-Terry likelihood over pairwise comparisons as one elicitation form
- [[lm-featurized-bayesian-elicitation]] — updates a posterior over personas with a Bradley-Terry choice model, approximated by a particle filter

[^c1]: arxiv-2601-06108 — "The Bradley-Terry model [1] provides the foundational preference model for RLHF."
[^c2]: arxiv-2601-06108 — "Given a reward function r, the probability that"
[^c3]: arxiv-2601-06108 — "Both assumptions are violated"
[^c4]: arxiv-2601-06108 — "binary comparisons cannot identify latent annotator"
[^c5]: arxiv-2601-06108 — "Rankings over three or more"
[^c6]: arxiv-2601-06108 — "Plackett-Luce model generalizes Bradley-Terry:"
[^c7]: arxiv-2601-06108 — "When preferences are nontransitive, the goal shifts from reward maximization"
