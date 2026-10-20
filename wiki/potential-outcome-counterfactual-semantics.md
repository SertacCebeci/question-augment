---
description: "With causally complete realistic variables, potential outcome variables must be mutually independent, which makes counterfactual probabilities unique and point-identified."
aliases: ["PO-SCM", "potential outcome semantics of counterfactuals", "independent potential outcome model"]
sources: ["arxiv-2512-12804"]
---
# Potential outcome counterfactual semantics

Under Pearl's semantics, the counterfactual probabilities of a nondeterministic model depend on which response variables are assumed. Beckers replaces them with the variables of the potential outcomes framework, and the replacement is exact. A single response variable R_X is equivalent to a family of potential outcome variables X_pa, one for each parent configuration pa, each giving the value X would take if the parents were pa.[^c1] Where the actual parents are pa, the actual value is X = X_pa, which is the consistency identity on which both frameworks rest.[^c2]

The model built this way, the PO-SCM, has the same variables as the original model, and its exogenous variables are the potential outcome variables, each with the distribution P(X | pa). The step that fixes everything is independence. The paper's claim is that "if we take seriously the completeness of a causal model, then so-called potential outcome variables have to" be mutually independent.[^c3] The author's reason is that the counterfactual outcome variables are artefacts of the deterministic representation and carry no realistic content, so their joint distribution is set by a formal choice rather than by the world.[^c4] Given that choice, the PO-SCM is unique, which is why "the PO-SCM is unique, and thus probabilities" of counterfactuals are not left open the way they are under Pearl's canonical models.[^c5]

The gain is concrete. In the binary example of [[response-variable]], Pearl's semantics leaves the counterfactual probability unbounded, whereas the PO-SCM gives point values: P(Y1 = 1) = p and P(Y0 = 1) = q, and the counterfactual probability is then fixed. The paper also shows that "there exists a unique canonical SCM" equivalent to the PO-SCM, so the PO semantics is a special case of the Pearlian one in which one canonical model is singled out as the true underlying model.[^c6] The author also states that the semantics is equivalent to two other recent proposals, one of which is the author's earlier actualized refinement, which works by "focussing directly on the relation between the prior and posterior distribution".[^c7]

## Limits

- The independence is the key assumption and it is argued, not tested. The author says the argument "does not by itself prove my semantics to be correct", and that broad agreement with other proposals is only a sign that the principles are "plausible and widely accepted".[^c8]
- The author admits that the PO-SCM "still fall[s] short" of the principle that every element of the model is realistic: the potential outcome variables are not observable, only the actual one is.[^c9]
- Consistency, X = X_pa when pa is actual, is treated as a consequence of the Pearlian setting. The author notes that in the potential outcome framework it must be justified separately, and the paper does not assess that justification.[^c2]
- The scope is causally complete realistic models satisfying the Markov condition. The author is "sympathetic to those who have criticized" the universal applicability of that condition, so the semantics is not claimed for models outside it.[^c10]
- The paper is theoretical and its status is a preprint: "Preprint: currently under review".[^c11]

## Related

- [[response-variable]] — the Pearlian device this semantics refines; the same example gives unbounded versus point-identified counterfactuals.
- [[realistic-scm-extension-failure]] — the nondeterministic models for which Pearl's SCM extension does not exist, and so for which this semantics is needed.
- [[counterfactual-explanation-recourse-gap]] — uses deterministic structural counterfactuals, the special case where no independence choice is needed.

[^c1]: arxiv-2512-12804 — "a single response variable RX can be equivalently represented"
[^c2]: arxiv-2512-12804 — "The assumption that this identity holds is called consistency"
[^c3]: arxiv-2512-12804 — "then so-called potential outcome variables have to"
[^c4]: arxiv-2512-12804 — "nothing but artificial artefacts of our deterministic representation"
[^c5]: arxiv-2512-12804 — "the PO-SCM is unique, and thus probabilities"
[^c6]: arxiv-2512-12804 — "there exists a unique canonical SCM"
[^c7]: arxiv-2512-12804 — "focussing directly on the relation between the prior and posterior distribution"
[^c8]: arxiv-2512-12804 — "does not by itself prove my semantics to be correct"
[^c9]: arxiv-2512-12804 — "still fall short of the principle that all elements of a causal model ought to have a"
[^c10]: arxiv-2512-12804 — "sympathetic to those who have criticized its universal applicability"
[^c11]: arxiv-2512-12804 — "Preprint: currently under review"
