---
description: "Invariance to equivalent rewrites and sensitivity to answer-changing edits pull against each other: an invariance penalty alone cut sensitivity from 1.0 to 0.47 in one synthetic benchmark."
aliases: ["invariance/sensitivity trade-off", "invariance-sensitivity tension"]
sources: ["arxiv-2512-06393"]
---
# Invariance–sensitivity trade-off

A model can be trained to treat two logically equivalent formulations of a rule set alike. The paper's regulariser (LIRE) does this by penalising "divergence between the next-token distributions" the model assigns to a rule and its rewrite, here De Morgan, double-negation and contrapositive forms, on one shared gold trace.[^i1] The target is that the two inputs yield the same output distribution, so the penalty is applied at the level of the reasoning trace rather than the final label.

The cost shows up on the other side of the ledger. The same penalty improves invariance (the authors report Variant 4 accuracy rising from 0.741 to 0.999),[^i9] but it also "suppresses any distribution shift across rule reformulations, including those that should change the answer."[^i2] In the ablation the authors report, "Empirical sensitivity drops from 1.0 to 0.47, motivating Stage 4."[^i3] The mechanism, in my reading, is that a rewrite which changes the answer is pulled toward the same distribution as the original, because the penalty does not know which rewrites are answer-preserving. The paper does not measure this decomposition directly.

The paper's response is a single reward for both sides. Its oracle returns the same answer for equivalent formulations and a different one for answer-changing edits, so one signal can reward invariance where the answer is preserved and sensitivity where it is not: "A single reward balances both objectives."[^i4] The trade-off is not fully removed by this. At the 1.5B backbone, V4-multi after Stage 4 is still at 0.773, which the authors attribute to capacity, and they describe the residual as "a real residual of the invariance/sensitivity trade-off that LIRE alone cannot resolve."[^i5][^i6]

Read for asking and answering, the point is that a consistency objective has to name which variations must be ignored and which must move the answer. A target that only asks for sameness can make a model deaf to exactly the edits that matter.

## Limits

- The measurement is a propositional, synthetic rule benchmark. The authors say so themselves: "The benchmark is propositional and synthetic."[^i7] The 0.47 sensitivity is one ablation on that benchmark, not a general rate.
- The paper reports the trade-off and a partial fix, not a sweep. The text read here does not vary the weight of the invariance penalty, so whether a lighter penalty keeps most invariance while preserving sensitivity is not tested.
- The oracle that resolves the trade-off is exact only because the rules are propositional and the forward-chaining engine is sound for them. The paper notes its oracle "cannot verify quantified reasoning, induction" in its discussion, so the reward's clean separation of equivalent and non-equivalent edits does not carry over to richer logic without a different verifier.[^i8]
- Whether the same trade-off holds for rewrites of natural-language premises, where equivalence is itself uncertain, is not tested.

## Related

- [[logic-inertia]] — the failure the invariance side is meant to address: a model that keeps its trajectory whatever the premises say. My inference is that a penalty on sameness can make the opposite error when the premises do change.
- [[permutation-consistency-training]] — a neighbouring family of consistency targets; I have not read it for this entry, so the relation is by analogy only.

[^i1]: arxiv-2512-06393 — "penalises divergence between the next-token distributions"
[^i2]: arxiv-2512-06393 — "any distribution shift across rule reformulations, including those that should change the answer"
[^i3]: arxiv-2512-06393 — "Empirical sensitivity drops from 1.0 to 0.47, motivating Stage 4."
[^i4]: arxiv-2512-06393 — "A single reward balances both objectives"
[^i5]: arxiv-2512-06393 — "V4-multi at 1.5B drops to 0.773"
[^i6]: arxiv-2512-06393 — "0.773 (Stage 4)—a real residual of the invariance/sensitivity trade-off that LIRE alone cannot resolve"
[^i7]: arxiv-2512-06393 — "The benchmark is propositional and synthetic; saturation evidences that the structural prior generalises"
[^i8]: arxiv-2512-06393 — "cannot verify quantified reasoning, induction"
[^i9]: arxiv-2512-06393 — "LIRE improves invariance (Variant 4 accuracy 0.741 → 0.999) but suppresses"
