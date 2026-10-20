---
description: "Coarsening a realistic deterministic model can yield a nondeterministic model with no realistic structural causal model extension, so Pearl's counterfactual semantics does not reach it."
aliases: ["no realistic SCM extension", "nondeterminism from coarse variables", "realistic causal model beyond SCMs"]
sources: ["arxiv-2512-12804"]
---
# Realistic SCM extension failure

Pearl's semantics for counterfactuals assumes that every probabilistic causal model can be extended into a structural causal model over the same signature. The claim is true if the extension may use unrealistic variables, and false if every variable must correspond to a real, observable or known property. The author's counterexample keeps realism throughout.[^c1]

Assume a domain has a fundamental signature, one whose variables are maximally fine-grained, and a fundamental realistic SCM over it, with a single equation Y = f_Y(U) and a distribution on U that puts positive probability on every value. Define a binary variable Z that records whether U equals a given value u'. Z is realistic, since U is, and the pair (Z, Y) forms a realistic signature.[^c2] The correct model over this coarser signature is not an SCM: the child Y has parent configurations whose conditional distributions are not restricted to 0 and 1. The author states that the correct model "is not an SCM, for the probabilities of" the child given its parents are spread out.[^c9]

The reductio shows there is no realistic SCM extension. Suppose one exists, with an equation Y = g_Y(Z, W) and realistic W. Setting Z = 1 forces g_Y(1, w) to equal the single value f_Y(u') for every w, so the one value U = u' would correspond to several distinct realistic properties (1, w_1), ..., (1, w_n). That "contradicts that U is a set of fundamental variables".[^c3] So a realistic deterministic description at the fundamental level does not give a realistic deterministic description at the coarser level. The author concludes that "the existence of a deterministic model at a more abstract level" does not follow from the existence of one at the fundamental level.[^c4]

The same modification gives a realistic and causally complete model that violates the Markov condition: take a fundamental SCM with two effects of one parent, which the author calls Example 2. The author notes that "the above example can easily be modified to show something stronger", namely that Pearl's claim of universal applicability for the Markov condition also fails.[^c5]

The consequence for causal abstraction is that whether a deterministic model exists at a higher level "depends on how one chooses the abstraction" from low-level to high-level values.[^c6] Earlier work on causal abstraction had, in the author's words, left the restriction to realistic models implicit or absent, so "the above negative result had not yet been established".[^c7]

## Limits

- The counterexample assumes a fundamental realistic description exists. The author says one "could resist it by offering an argument that there never exists a fundamental level of description in any domain that" is subject to causal relations, but doubts such an argument can be given.[^c8]
- The example is a single toy case with a binary coarsening. The paper proves the failure by construction and does not measure how common such cases are in practice.
- The Markov-condition counterexample is stated as a "trivial example" and is built the same way; it is not a study of which real systems violate the condition.
- The result is about existence of a realistic extension, not about the counterfactual probabilities themselves. Those are the subject of [[response-variable]] and [[potential-outcome-counterfactual-semantics]].

## Related

- [[response-variable]] — Pearl's device that a realistic extension would have to supply; this note shows where it can fail to be realistic.
- [[potential-outcome-counterfactual-semantics]] — the semantics the author proposes for the nondeterministic models where no SCM extension exists.
- [[counterfactual-explanation-recourse-gap]] — restricts to additive noise models, where counterfactuals are computed deterministically. My reading: that restriction keeps the model inside the class where this failure is not at issue.

[^c1]: arxiv-2512-12804 — "can be extended into an SCM does hold"
[^c2]: arxiv-2512-12804 — "Given that U is realistic, so is Z"
[^c9]: arxiv-2512-12804 — "is not an SCM, for the probabilities of"
[^c3]: arxiv-2512-12804 — "contradicts that U is a set of fundamental variables"
[^c4]: arxiv-2512-12804 — "existence of a deterministic model at a more abstract level"
[^c5]: arxiv-2512-12804 — "The above example can easily be modified to show something stronger"
[^c6]: arxiv-2512-12804 — "depends on how one chooses the abstraction"
[^c7]: arxiv-2512-12804 — "the above negative result had not yet been established"
[^c8]: arxiv-2512-12804 — "in principle one could resist it by offering an argument"
