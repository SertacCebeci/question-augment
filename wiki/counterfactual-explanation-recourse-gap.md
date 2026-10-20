---
description: "A nearest counterfactual explanation is not a safe action recommendation: with causal dependence among features, acting on it can miss the outcome or cost more than a causally planned intervention."
aliases: ["recourse through minimal interventions", "MINT", "CFE-based recourse limitation", "counterfactual explanation vs recourse"]
sources: ["karimi-2020"]
---
# Counterfactual explanation versus recourse gap

A counterfactual explanation (CFE) answers "what is the nearest changed input that flips the decision?". Recourse asks a different question: "what should this person do?". Treating the first answer as the second is the move the work examines. The standard reformulation minimizes a cost over feature shifts, so the shift is read as an action list.[^c1]

## Mechanism

The work models the world as a structural causal model (SCM). Acting on a feature is an intervention that also changes its descendants. A CFE-based action sets the acted-on features to the CFE values and implicitly assumes nothing else moves. Under that reading, the work proves a necessary and sufficient condition: the action reaches the CFE (and so guarantees the flipped outcome) only if the acted-on variables have no descendants.[^c2] The sketch of the argument: "Otherwise, the value of the descendants will depend on the counterfactual value of their parents, leading to a structural counterfactual that does not resemble the nearest counterfactual explanation".[^c3] If all features are independent root nodes, CFE-based actions always work, but that world is unrealistic because it requires all features to be independent of each other.[^c4]

Two repairs fail. Holding descendants fixed means severing their incoming causal edges, which can be infeasible and costly and may still not change the prediction. And the CFE ignores the causal benefit of acting: a change to a parent can move a child toward the target for free.[^c5]

The proposed replacement is recourse through minimal interventions (MINT): search directly over feasible interventions and compute the resulting structural counterfactual for each, minimizing cost subject to the decision flipping. The work proves that if any CFE-based action achieves recourse, the optimal intervention costs no more than it.[^c6] This needs a known causal model, with the work restricting it to additive noise models so counterfactuals can be computed deterministically.[^c7]

## Why it matters for asking and answering

The work is an instance of a general answer failure: a response correct as an explanation ("this change would suffice, holding all else fixed") is read as an instruction ("do this"), and the unstated ceteris paribus clause is exactly what breaks. This reading across fields is my inference, not a claim of the work.

## Limits

- Recourse guarantees depend on knowing the true causal graph and structural equations; the work itself notes that a misspecified model undermines the result, and it offers no way to elicit one from the asker.
- The proofs assume additive noise models and a deterministic counterfactual; hidden confounding and stochastic outcomes are outside the proposition.
- The cost function over interventions is taken as given; where it comes from is not established here (see [[individual-actionability-constraints]]).
- The extension to answering and asking in conversation is my inference; no dialogue or human study is in this work.

## Related

- [[individual-actionability-constraints]] — who supplies the cost and feasibility constraints on the recommended action
- [[counterfactual-search-routing-oracle]] — another use of counterfactual search, as a router rather than a recommendation
- [[causal-control-advantage]] — causal reasoning applied to which intervention to take

[^c1]: karimi-2020 — "Algorithmic Recourse:"
[^c2]: karimi-2020 — "if and only if, the set of descendants of the"
[^c3]: karimi-2020 — "Otherwise, the value of the descendants will depend on the counterfactual value of their parents, leading to a structural counterfactual that does not resemble the nearest counterfactual explanation,"
[^c4]: karimi-2020 — "Unfortunately, the independent world assumption is not realistic,"
[^c5]: karimi-2020 — "as they do not benefit from the causal effect of actions towards"
[^c6]: karimi-2020 — "the optimization problem in (3) yields Recourse through Minimal"
[^c7]: karimi-2020 — "we consider that the SCM M falls in the class"
