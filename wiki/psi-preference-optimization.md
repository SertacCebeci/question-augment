---
description: "One convex function Ψ of the log-ratio margin generates DPO, IPO and hinge-style losses; the choice of Ψ sets how the margin between preferred and dispreferred responses is handled."
aliases: ["ΨPO", "Psi-PO", "general preference optimization objective", "Ψ-objective for preference learning"]
sources: ["arxiv-2601-06108"]
---
# ΨPO: one objective for pairwise preference losses

The work presents "the ΨPO framework of Azar et al. [7]," which puts several pairwise preference losses into one form.[^c1] For a convex function Ψ from the reals to the reals, the objective averages Ψ applied to a β-scaled difference: the log ratio of the policy to the reference for the preferred response, minus the same quantity for the dispreferred one. Its arguments are the margin in log-ratio space between the winning and the losing response, and the loss is a function of that margin alone.[^c2]

The instantiations follow from the choice of Ψ. A log-sigmoid gives DPO, the loss of [[dpo-implicit-reward]]. A squared function of the margin, shifted to a target of one, gives IPO, which differs from DPO in using "Instead of the log-sigmoid, IPO uses a" squared loss.[^c3] A hinge, max(0, 1 − z), gives the SLiC-HF loss. The work's synthesis is that the methods "differ primarily in how they handle the margin between preferred and dispreferred log-ratios."[^c4] In the work's words, the IPO target margin provides regularization that DPO lacks.[^c5]

The same frame is extended to reference-free methods. SimPO, the work says, "eliminates the reference model entirely" by using[^c9] length-normalized log-probabilities as the implicit reward and a target margin γ, "where γ > 0 is a target margin."[^c6] The work's contribution statement lists DPO, IPO, KTO, SimPO, ORPO and GRPO as special cases of a general ΨPO objective, which is the sense in which the framework is called unifying.[^c7]

## Limits

- The Ψ form is the one the work attributes to Azar et al.; the work restates it and does not prove the instantiations here beyond listing them.
- The claim covers pairwise losses in Ψ form. The work's own Table 1 lists ORPO with an odds-ratio term combined with SFT and GRPO with a group-relative policy gradient, which are not Ψ-form losses on the same margin. The table is titled "Unified View of Preference Learning Methods.",[^c8] and it is a classification, not a reduction. Whether the framework reaches those two methods is asserted, not shown, in this work (my reading).
- The work classifies methods qualitatively, with phrases such as "Simple, overfit-prone," and the margin account is its synthesis. No experiment in this note compares the Ψ choices.
- A given Ψ is a claim about the loss shape, not about which method performs best. The work's empirical table is not used for this note.
- The framework is for offline pairwise data; the online and hybrid cases are covered by [[coverage-separation-offline-online]], not by Ψ alone.

## Related

- [[dpo-implicit-reward]] — the Ψ = log-sigmoid instance, and the reparameterization it rests on
- [[bradley-terry-preference-model]] — the preference model under which the margin between the two responses is a difference of rewards
- [[coverage-separation-offline-online]] — the offline-versus-online split that the Ψ family does not itself address
- [[kl-divergence]] — the regularizer that the margin's log-ratios express implicitly

[^c1]: arxiv-2601-06108 — "We present the ΨPO framework of Azar et al. [7],"
[^c2]: arxiv-2601-06108 — "function Ψ : R → R, the ΨPO objective is:"
[^c3]: arxiv-2601-06108 — "Instead of the log-sigmoid, IPO uses a"
[^c4]: arxiv-2601-06108 — "This unification reveals that the methods differ primarily in how they handle the margin between preferred and dispreferred log-ratios."
[^c5]: arxiv-2601-06108 — "The target margin of 1 (in log-odds) provides regularization"
[^c6]: arxiv-2601-06108 — "where γ > 0 is a target margin."
[^c7]: arxiv-2601-06108 — "A unified theoretical framework showing DPO,"
[^c8]: arxiv-2601-06108 — "Unified View of Preference Learning Methods."
[^c9]: arxiv-2601-06108 — "eliminates the reference model entirely"
