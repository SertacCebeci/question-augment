---
description: "Pearl's response variables make a probabilistic causal model deterministic so its counterfactuals can be read off; the device is realistic only where an extension exists, which can fail."
aliases: ["response variables", "Balke-Pearl response variable", "canonical SCM extension"]
sources: ["arxiv-2512-12804"]
---
# Response variable

A probabilistic causal model gives, for each child, a distribution conditional on its parents, but not a function from parents to child. Pearl's way of giving such a model counterfactuals is to add exogenous variables that absorb the randomness, so that every child becomes a deterministic function of its parents and these extra variables. The device is due to Balke and Pearl (1994), and it works by pulling the probability out of the causal relations and placing it on the added variables.[^c1]

In the simplest case, a binary child Y of a binary parent X receives a four-valued response variable U_Y, each value naming one function from X to Y: the identity, negation, constant 0, or constant 1. Choosing the distribution of U_Y so that it reproduces P(Y=1 given X=1) and P(Y=1 given X=0) makes Y a deterministic function of X and U_Y.[^c2] Probabilities of counterfactuals are then defined over the resulting structural causal model. The Pearlian semantics assumes that one of the possible canonical extensions of the model is the ground truth.[^c3]

Because the true extension is seldom known, counterfactual probabilities are in general not identifiable.[^c4] In the binary example, two canonical extensions that agree on every observational and interventional distribution can give a basic counterfactual probability of 1 or of 0. If one is agnostic about which extension is true, the probabilities of basic counterfactuals for Y are entirely unbounded.[^c5]

The device carries a dilemma. Its values are general enough to encode any relevant omitted cause, which is why it works. Once realism is required of every variable, the same values can encode purely formal properties with no empirical counterpart. The author argues that Pearl "now faces an unappealing dilemma":[^c6] if the response variables are read as real, the negative result that a realistic extension does not always exist applies (see [[realistic-scm-extension-failure]]); if they are read as artificial, Pearl is "attributing properties to the world that are in fact purely formal properties of a conventional mathematical representation".[^c7]

## Limits

- The dilemma is the author's argument about how the device must be read. The author says Pearl's stance is unclear: "this ambiguity is particularly crucial when it comes to the response variables".[^c8] The argument charges a reading, not a doctrine Pearl is shown to hold.
- The reduction is stated for models that satisfy the Markov condition and contain realistic, causally complete variables. The author notes that Zhang et al. studied the method "including causal models that do not satisfy the Markov condition", and that the definitions there are more involved.[^c9] Those cases are not evaluated here.
- The paper shows the non-identifiability with one binary example and does not compute general bounds.
- Dawid's objection is that a realistic response variable amounts to strong determinism, "Such Laplacian determinism is out of favour as a general scientific or" philosophical principle.[^c10] The paper accepts that objection as a reason to drop the deterministic reading, not as a proof that the device is meaningless.

## Related

- [[potential-outcome-counterfactual-semantics]] — replaces the response variables by potential outcome variables, which keep one actual value per world and put the rest on independent exogenous variables.
- [[realistic-scm-extension-failure]] — the case in which the device has no realistic reading at all.
- [[counterfactual-explanation-recourse-gap]] — uses structural counterfactuals only for additive noise models, where they are deterministic. My reading: the response-variable question is what that restriction avoids when the model is not deterministic.

[^c1]: arxiv-2512-12804 — "all the probability from the causal relations"
[^c2]: arxiv-2512-12804 — "response variable UY so that fY is either the identity function"
[^c3]: arxiv-2512-12804 — "one of its canonical SCMs represents the ground-truth"
[^c4]: arxiv-2512-12804 — "such probabilities are in general not identifiable"
[^c5]: arxiv-2512-12804 — "the probabilities of basic counterfactuals for Y are entirely unbounded"
[^c6]: arxiv-2512-12804 — "now faces an unappealing dilemma"
[^c7]: arxiv-2512-12804 — "is attributing properties to the world that are in fact purely formal properties"
[^c8]: arxiv-2512-12804 — "this ambiguity is particularly crucial when it comes to the response variables"
[^c9]: arxiv-2512-12804 — "including causal models that do not satisfy the Markov condition"
[^c10]: arxiv-2512-12804 — "Such Laplacian determinism is out of favour as a general scientific or"
