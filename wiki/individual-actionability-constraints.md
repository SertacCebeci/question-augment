---
description: "A constraint on a recourse recommendation comes from the affected individual, elicited pre-hoc as hard (which features) and soft (how hard) actionability constraints."
aliases: ["individual actionability", "individualized actionability", "personalized causal recourse"]
sources: ["arxiv-2604-08030"]
---
# Individual actionability constraints

> The recourse optimizer is not the source of the constraint on its own
> output — the affected individual is, and only if asked before the
> recommendation is generated.

## Definition / Mechanism

In algorithmic recourse (AR), studied in Budde et al. (2026), a deployed decision system rejects an
individual and a recourse method proposes feature changes that would
overturn the decision. The source formalizes *personalization* in this
setting not as a preference over outcomes but as **individual
actionability**: "we formalize personalization as individual
actionability, characterized along two dimensions: hard constraints that
specify which features are individually actionable, and soft,
individualized constraints that capture preferences over action values and
costs."[^c1]

A **hard constraint** removes a feature from the action space entirely,
independent of whether it is globally actionable: "A user may be unable to
take any action on a given feature, either because the feature is globally
non-actionable or because the user faces circumstances that render a
globally actionable feature effectively non-actionable."
[^c2]

A **soft
constraint** keeps the feature available but reweights its cost —
capturing that, say, a user can change income easily but savings only with
difficulty. Formally the individually feasible action set is a subset of
the globally feasible one (Fu ⊆ F), and the individualized cost function
adds a per-feature actionability weight wu,i to a base cost term.

The source's answer to *who is asked and how* is a **pre-hoc prompting
scheme**, deliberately run before any recommendation is generated rather
than as feedback on a candidate one, and deliberately minimal — no cost
function elicitation, no mathematical input from the user. It offers three
routing granularities, traded off against the effort asked of the
individual: "(i) users group globally actionable features into
individually actionable and non-actionable; (ii) users additionally rank
actionable features by difficulty, providing indirect information about
individualized costs; and (iii) users assign Likert-scale difficulty
scores to each feature while marking features as non-actionable."[^c3]

Truthfulness of the elicited constraint is not enforced but argued from
incentives: "We further assume that users report such preferences
truthfully. This assumption is reasonable because AR is not strategic:
misreporting preferences does not provide systematic advantages to
users."
[^c4]

Because the recommendation must actually be executed by the
same individual, a false report only makes the resulting recourse worse
for them.

## Why it matters

Routing the constraint through the individual rather than assuming it
globally changes what "actionable" means per case: a feature that is
globally actionable (e.g. income) can be individually non-actionable for
one person and merely costly for another. The source also shows the
elicitation channel itself is not neutral: when who reports what
constraint correlates with a demographic axis, group disparities in
recourse cost and plausibility widen or appear where a global-actionability
analysis would miss them — "even randomly assigned individualized
actionability constraints can amplify existing recourse disparities... for
the baseline, female users already face higher recourse costs and less
plausible recommendations... These gaps increase when individual
actionability constraints are considered."
[^c5]

Constraints that correlate
with a protected attribute but not with the model's other features or
label can manufacture a disparity that a global-actionability audit would
not see at all: "Under race-correlated actionability constraints, we
observe cost and plausibility gaps emerging solely from individualized
actionability constraint profiles... if it shapes which features are
actionable, it can lead to higher costs and less plausible recommendations
for certain groups."
[^c6]

The lesson for any system that routes a
constraint through an asked party: the routing rule (who is asked, and
what their answer is allowed to restrict) is itself a place fairness can
fail, separate from the model that consumes the answer.

## Limits

- Truthful reporting is an assumption, not a verified property of the
  elicitation scheme; the source argues it from AR's non-strategic
  payoff structure but does not test it against real users who might
  misreport (e.g. to appear more constrained than they are).
- The prompting scheme is pre-hoc and one-shot in this source's study;
  the source itself notes a post-hoc, iterative refinement is
  complementary but untested here, and that iteration raises cognitive
  load and privacy concerns of its own.
- The fairness findings are a case study on synthetic and semi-synthetic
  preference assignments (uniform random, income-correlated,
  race-correlated), not observed real-world elicited preferences; whether
  real individually-actionable-feature reports correlate with demographics
  this way is unverified.

## Related

- [[patient-context-ambiguity]]
- [[constraint-as-information]]
- [[value-of-information]]
- [[cost-robust-recourse]] — the contrast case: this note's prompting scheme
  deliberately avoids cost-function elicitation, whereas the cost-robust
  method elicits a cost matrix from pairwise comparisons of recourses and
  optimises against every matrix still consistent with the answers

[^c1]: arxiv-2604-08030 — "we formalize personalization as individual actionability, characterized along two dimensions: hard constraints that specify which features are individually actionable, and soft, individualized constraints that capture preferences over action values and costs."
[^c2]: arxiv-2604-08030 — "A user may be unable to take any action on a given feature, either because the feature is globally non-actionable or because the user faces circumstances that render a globally actionable feature effectively non-actionable."
[^c3]: arxiv-2604-08030 — "we explore a flexible scheme allowing for expressing hard constraints, preference ranks, and scoring over actionable features. We consider three prompting schemes of increasing granularity: (i) users group globally actionable features into individually actionable and non-actionable; (ii) users additionally rank actionable features by difficulty, providing indirect information about individualized costs; and (iii) users assign Likert-scale difficulty scores to each feature while marking features as non-actionable."
[^c4]: arxiv-2604-08030 — "We further assume that users report such preferences truthfully. This assumption is reasonable because AR is not strategic: misreporting preferences does not provide systematic advantages to users."
[^c5]: arxiv-2604-08030 — "even randomly assigned individualized actionability constraints can amplify existing recourse disparities. As we see in Figure 4, for the baseline, female users already face higher recourse costs and less plausible recommendations (lower log-densities) compared to male users. These gaps increase when individual actionability constraints are considered."
[^c6]: arxiv-2604-08030 — "Under race-correlated actionability constraints, we observe cost and plausibility gaps emerging solely from individualized actionability constraint profiles. Even though race does not influence other features or the label, if it shapes which features are actionable, it can lead to higher costs and less plausible recommendations for certain groups."
