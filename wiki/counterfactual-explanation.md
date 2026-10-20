---
description: "A counterfactual explanation states which external facts would have to differ to change a decision, so it supports understanding, contesting and acting without exposing the model's internal logic."
aliases: ["unconditional counterfactual explanation", "closest possible world explanation", "explanation without opening the black box"]
sources: ["wachter-2017"]
---
# Counterfactual explanation

A counterfactual explanation has the form: "You were denied a loan because your annual income was £30,000. If your income had been £45,000, you would have been offered a loan."[^c1] It follows the statement of a decision with a statement of how the world would have to differ for another outcome. The work frames explanation by the goal it serves, helping the subject act rather than merely understand, and names three aims: to understand why a decision was reached, to contest it, and to learn what could change to obtain a desired result.[^c2]

## Mechanism

The key move is a change of object. Usual "explanation" conveys the internal state or logic of the algorithm; a counterfactual instead describes a dependency on the external facts that led to the decision.[^c3] It is deliberately small: it gives the minimal information capable of altering a decision and needs no grasp of the model's internals.[^c4] The organising idea is the "closest possible world", the smallest change that yields the desired outcome.

The work qualifies this in three ways:

- Several diverse counterfactuals may serve better than the single closest one, because relevance also depends on how mutable a variable is and how probable a change is.[^c5]
- One counterfactual can be overly restrictive: it may rest on correct data the subject cannot alter, while other alterable data exist. Offering several diverse counterfactuals is the proposed remedy.[^c6]
- Closeness is not enough: it is "at least as important that the solution found comes from a 'possible world' as it is that it is close". Adversarial perturbations are the same computation as the nearest counterfactual, but they land slightly outside the space of real images.[^c7]

Standard adversarial-perturbation methods also lack suitable distance functions and favour small changes to many variables over sparse, interpretable ones, which is the property a human-readable counterfactual needs.[^c8]

## Limits

- The work is a legal and conceptual argument; it reports no user study of whether people understand, contest or act on counterfactuals.
- It treats the counterfactual as a statement about the model's dependence on inputs. It does not address causal links among inputs; the consequence for acting on it is in [[counterfactual-explanation-recourse-gap]].
- Mutability and probability of change are named as relevant but not given a method.
- Reliability in high-dimensional structured spaces such as images is left to further research.
- Applying this to ordinary question answering (an answer that names the smallest change in the asker's situation) is my inference, not a claim of the work.

## Related

- [[counterfactual-explanation-recourse-gap]] — shows that acting on the nearest counterfactual can fail when features are causally linked
- [[individual-actionability-constraints]] — who decides which changes are feasible for the subject
- [[counterfactual-search-routing-oracle]] — counterfactual search used for another purpose

[^c1]: wachter-2017 — "You were denied a loan because your annual income was £30,000. If"
[^c2]: wachter-2017 — "to understand what could be changed to receive a"
[^c3]: wachter-2017 — "counterfactuals describe a dependency on the"
[^c4]: wachter-2017 — "provide a minimal amount"
[^c5]: wachter-2017 — "rather than “the closest possible world” may be more helpful."
[^c6]: wachter-2017 — "individual counterfactuals may"
[^c7]: wachter-2017 — "solution found comes from a “possible world” as it is that it is close to the"
[^c8]: wachter-2017 — "none of the standard works on Adversarial"
