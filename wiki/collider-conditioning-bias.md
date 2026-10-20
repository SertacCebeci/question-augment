---
description: "Conditioning on a variable that two factors both cause, such as overall satisfaction, can manufacture an association between them that the unconditioned data do not show."
aliases: ["collider bias", "collider stratification", "conditioning on a common effect"]
sources: ["arxiv-2512-02060"]
---
# Collider conditioning bias

A collider is a variable that two other variables both cause. The paper sets it beside the confounder, which is the more familiar case: confounders "causally affect both A and B",[^k7] and colliders are "variables caused by both A and B".[^k1] The collider is the one that misleads when it is conditioned on: colliders "can induce spurious associations when inappropriately conditioned upon."[^k2]

**The mechanism.** Take two causes that are independent of each other, A and B, which both feed a third variable C. Without conditioning on C, A and B carry no information about each other. Once C is fixed, learning A changes what B can be, because only certain combinations of A and B are compatible with the observed C. The association is produced by the act of conditioning, not by any effect of A on B. The paper states the outcome, not this derivation; the derivation is my inference, and it is the standard reason colliders behave this way.

The paper's survey example puts the collider in the workspace setting. Lighting and acoustics both influence overall satisfaction. "Overall satisfaction might act as a collider if both lighting and acoustics independently influence it, and incorrectly conditioning on overall satisfaction could create artificial associations between lighting and acoustics factors."[^k3] An analysis that asks whether acoustic satisfaction tracks lighting satisfaction, and then adjusts for overall satisfaction as a control, can report an association the building does not contain.

**Why the role matters more than the name.** The confounder and the collider call for opposite handling. A confounder must be conditioned on, or the association between its two effects is spurious. A collider must not be. The paper's example of the confounder is office type: without controlling for it, "one might incorrectly infer that lighting satisfaction directly causes thermal comfort satisfaction".[^k4] Both variables are in the survey, and nothing in the column names says which role each one plays. The role is a property of the graph, which is why the question's causal structure has to be fixed before the adjustment set is chosen. The graph itself is what the causal-skeleton-variable-screening note describes.

**Where it comes from in the wiki.** The same mechanism appears in [[predicted-outcome-substitution]], where a predicted value used as a conditioning variable is one of several routes to bias. That note holds the collider as one failure among several in a single setting; this note is the general mechanism, without the substitution.

**What the reader gets from it.** Any question of the form "does X affect Y, holding Z fixed" has a conditioning set, and the set should be chosen from the graph's roles, not from the list of available covariates. Whether a variable is a confounder, a collider or neither is a claim about how the data were generated. The descriptive side of the split in [[descriptive-versus-interventional-question]] cannot read those roles from the data alone.

## Limits

- The paper does not measure collider bias. The survey example is qualitative, and the paper's wording is hedged: "might act as a collider". Its own analysis is not shown to contain a collider-conditioned result, so whether the error appears in its data was not tested.
- The collider label is only as reliable as the graph that gives it. The paper's edge orientations are "testable hypotheses", so the claim that overall satisfaction is a collider is no firmer than its arrows.[^k5]
- Unmeasured causes can make a true collider look like a confounder, or the reverse. The paper names unmeasured variables as its main threat: "The presence of hidden or unmeasured variables is a valid critique."[^k6]
- The note covers conditioning in analysis. Selection of which respondents enter the sample is a related route to a similar distortion, and the paper does not address it; that is not covered here.
- Magnitude is not given. Nothing in the work says how large the spurious association would be for typical survey sizes or effect strengths.

## Related

- [[predicted-outcome-substitution]] — a predicted outcome used as a conditioning variable is one route to this bias, among bias and variance failures.
- [[descriptive-versus-interventional-question]] — the question type that decides whether a variable should be conditioned on at all.
- causal-skeleton-variable-screening — the graph that marks which variables are structurally connected, and so which could be colliders.

[^k1]: arxiv-2512-02060 — "Colliders are variables caused by both A and B"
[^k2]: arxiv-2512-02060 — "when inappropriately conditioned upon"
[^k3]: arxiv-2512-02060 — "incorrectly conditioning on overall satisfaction could create artificial"
[^k4]: arxiv-2512-02060 — "one might incorrectly infer that lighting satisfaction directly causes thermal comfort satisfaction"
[^k5]: arxiv-2512-02060 — "Edge orientations are algorithmically determined and should be interpreted as testable hypotheses"
[^k6]: arxiv-2512-02060 — "The presence of hidden or unmeasured variables is a valid critique"
[^k7]: arxiv-2512-02060 — "causally affect both A and B"
