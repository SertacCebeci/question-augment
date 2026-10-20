---
description: "A counterfactual may let upstream causes change when a variable is set; the witness set, not a special mechanism, decides whether a causal definition allows such backtracking."
aliases: ["backtracking", "backtracking counterfactuals", "no-backtracking assumption"]
sources: ["arxiv-2511-21260"]
---
# Backtracking counterfactual

In a causal model, an intervention is forward-looking. Setting X = x changes only the variables that X can affect. The paper states the usual form: "As has often been observed, when considering the effect of an intervention such as X = x in a causal model, no variables upstream of X in the causal network are affected; only descendants of X can be affected."[^c1] The "no backtracking" rule follows, in my reading, from how a structural model is built: the upstream variables are fixed by the context, and an intervention replaces an equation without touching the context.

A backtracking counterfactual drops that rule. Asked what would have been true had X been x, the answer may change the causes of X as well. In the Lewis-style closest-state semantics this is allowed: "in the state(s) closest to (M, s) where X = x is true, it may well be the case that ancestors of X have changed their value."[^c2]

**Why one would want it.** The paper's reason, reporting von Kügelen et al., is that there are cases where we want to ascribe causality "but do not want to consider counterfactuals that result from" an intervention. "Intuitively, these are cases where the causal laws, not the background conditions, are shared between the actual and counterfactual worlds."[^c3] The paper also says that people "certainly consider backtracking counterfactuals when evaluating causality".[^c4] That is a report of the cited literature. This note does not test it.

**How the paper gets it without a new mechanism.** Von Kügelen et al. "introduced a whole mechanism for allowing" backtracking, which changes exogenous variables.[^c5] The paper's move is that the change of context is not an intervention. The agent is uncertain about the exogenous variable, and asks what would happen were it different: "changing the values of an exogenous variable is not viewed as an intervention".[^c6] Within the witness-conditioned definition, that uncertainty is simply part of the closest-state semantics. The paper claims the definition allows backtracking "in a natural way, without having to introduce a special mechanism for it."[^c7]

**What the choice controls.** Backtracking is not all-or-nothing. In the rock-throwing model, with the context fixed, Billy's throw is not a cause of the shattering: "the symmetric argument does not show that BT = 1 is a cause."[^c8] Let the closest state be one where both throws are absent, so the context changes, and Billy's throw becomes a cause: "By allowing the context to change in the closest state to s, we get backtracking."[^c9] The paper's summary is the key line: "we can move smoothly from allowing backtracking to forbidding it, just by fixing an appropriate set of variables."[^c10] Whether a causal claim allows backtracking "depends on the set of formulas CX from which τ is drawn".[^c11] So backtracking is a property of the background chosen for the question, not of the world.

## Limits

- The formal result is a reconstruction. It says what a definition yields under a choice of background. It does not say which choice a reader or a questioner should make, and the text gives no general rule. The choice is left to the set of admissible formulas.
- The support for backtracking as a feature of human causal judgment is cited from the literature (von Kügelen et al. and cognitive psychology). The paper reports it. Nothing here measures it.
- The worked example is one model, the rock-throwing case, with one change of context. The text does not show how much backtracking a realistic model allows, or how often it is the wrong reading.
- The paper says that fixing variables at their actual values "seems at first somewhat ad hoc".[^c12] Its defence is by examples, such as causality along a path, not by a general argument that the fixing rule is correct.

## Related

- [[witness-conditioned-actual-cause]] — the definition whose background set decides whether a causal claim backtracks; this note is the upstream-variable side of that choice.
- [[descriptive-versus-interventional-question]] — a no-backtracking reading is the do-operator reading of a what-if question; a backtracking reading asks a different question, and this is my inference, not the paper's claim.
- [[potential-outcome-counterfactual-semantics]] — another account of what a counterfactual holds fixed when a variable is set; whether the two accounts connect was not checked here.

[^c1]: arxiv-2511-21260 — "As has often been observed, when considering the effect of an intervention such as X = x in a causal model"
[^c2]: arxiv-2511-21260 — "ancestors of X have changed their value"
[^c3]: arxiv-2511-21260 — "we want to ascribe causality but do not want to consider counterfactuals that result from"
[^c4]: arxiv-2511-21260 — "backtracking counterfactuals when evaluating causality"
[^c5]: arxiv-2511-21260 — "backtracking counterfactuals in causal models that involved changing the values of exogenous variables"
[^c6]: arxiv-2511-21260 — "changing the values of an exogenous variable is not viewed as an intervention"
[^c7]: arxiv-2511-21260 — "without having to introduce a special mechanism for it"
[^c8]: arxiv-2511-21260 — "does not show that BT = 1 is a cause"
[^c9]: arxiv-2511-21260 — "By allowing the context to change in the closest state to s, we get backtracking"
[^c10]: arxiv-2511-21260 — "just by fixing an appropriate set of variables"
[^c11]: arxiv-2511-21260 — "whether or not we have backtracking depends on the set of formulas CX from which τ is drawn"
[^c12]: arxiv-2511-21260 — "seems at first somewhat ad hoc"
