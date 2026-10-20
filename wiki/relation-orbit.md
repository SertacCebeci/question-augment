---
description: "A closed-form, parameter-free contrast over eight symmetry-organized VLM likelihoods that decides assert-or-abstain for left-right claims, calibrated by a Clopper-Pearson threshold."
aliases: ["Relation-Orbit", "Relation-Orbit aggregation", "Relation-Orbit contrast"]
sources: ["xiong-2026"]
---
# Relation-Orbit

> An answerer (a frozen vision-language model) that must decide whether to
> assert a left/right spatial claim organizes every likelihood a fixed
> intervention induces by its symmetry role, rather than reading one number
> off the raw prompt, before it commits.

## Definition / Mechanism

For a query claim $c_1=(A,r,B)$, Xiong et al. (2026) form its
equivalent $c_2=(B,\iota(r),A)$ and its counterfactual pair $c_3,c_4$ under
inverse relation and entity exchange, and observe each under the original
image $x$ and a fixed horizontal reflection $T(x)$ — eight length-normalized
log-likelihoods in total. "We introduce Relation-Orbit, a closed-form
contrast with no learned fusion parameters that assigns eight normalized
likelihoods to query-supporting and counterfactual roles determined by
reflection, inverse relation, and entity exchange." The score is the mean of
the four supporting observations minus the mean of the four counterfactual
ones.[^c1]

The answerer commits only past a calibrated line: "A claim is asserted only
when the signed contrast exceeds a threshold selected on held-out data using
pointwise Clopper–Pearson upper confidence bounds." The threshold search
scans the finite set of [[calibration]] scores, keeps those whose upper-confidence
bound on false-assertion rate stays under a declared risk target $\alpha$,
and freezes the one with maximum coverage; if none qualifies the model
abstains on the entire test split.[^c2]

The paper proves the score's symmetry directly: "The Relation-Orbit contrast
is invariant to joint entity exchange and relation inversion, antisymmetric
to relation inversion alone, and invariant under $L_{v,j} \mapsto L_{v,j} +
b_v + a_j$, where $b_v$ and $a_j$ are view- and formulation-specific
offsets." This cancels per-view and per-formulation nuisance shifts in the
raw likelihoods without estimating them.[^c3]

## Why it matters

On four frozen VLMs across VSR and GQA, "Relation-Orbit yields higher mean
test coverage at a 10% selective-risk calibration target than an all-eight
Orbit-Max baseline in all eight dataset–[[backbone-of-a-formula|backbone]] settings" — the same eight
likelihoods and the same supporting/counterfactual split, mean-pooled instead
of max-pooled, already buys more usable coverage at a fixed risk. This is a
case where *how* an answerer aggregates its own evidence before choosing to
answer or withhold changes the commit/withhold boundary at a fixed risk
target, holding the underlying model and its raw evidence fixed.[^c4]

## Transfer

| | |
|---|---|
| Home field | group-symmetry contrast construction + Clopper–Pearson interval calibration, statistics/vision |
| Here | the answerer's commit-or-withhold decision on a single claim (stall 10) |
| What survives | organizing an answerer's redundant self-evidence by a known symmetry before aggregating it, instead of pooling it flat; freezing a threshold under a declared risk target rather than a fixed score cutoff |
| What does not | the specific reflection symmetry — it requires a claim type with a known, semantically valid involution |

The symmetry is not free of the claim type: "an above–below pilot with
vertical reflection produced no stable matched-budget gains," so the
construction does not carry to relations without a checked involution.[^c5]

## Limits

- The result rests on **likelihood access to a frozen VLM and a valid
  transformation**: "Relation-Orbit requires likelihood access and eight
  view–formulation scores, excluding text-only APIs and increasing compute.
  It also relies on a valid transformation: text, handedness, or other
  flip-sensitive cues can invalidate reflection, and domain shift requires
  transformation checks and recalibration." Neither a black-box text API nor
  a claim type without a checked involution is covered.[^c6]
- Calibration needs a labelled held-out split scored under the same
  protocol; the paper reports realized test risk, not a simultaneous
  finite-sample guarantee, and mean risk stays under target while individual
  splits can exceed it.
- A structural diagnostic shows the correct orbit beats most but not all
  relabelled partitions (average rank 1.61/35), so the advantage is
  systematic, not uniquely optimal — reported for spatial left/right claims
  only, not claim verification generally.

## Related

[[abstention]] · [[roc-curve]] · [[calibration]] · [[semantic-entropy]]

[^c1]: xiong-2026 — "We introduce Relation-Orbit, a closed-form contrast with no learned fusion parameters that assigns eight normalized likelihoods to query-supporting and counterfactual roles determined by reflection, inverse relation, and entity exchange."
[^c2]: xiong-2026 — "A claim is asserted only when the signed contrast exceeds a threshold selected on held-out data using pointwise Clopper–Pearson upper confidence bounds."
[^c3]: xiong-2026 — "The Relation-Orbit contrast is invariant to joint entity exchange and relation inversion, antisymmetric to relation inversion alone, and invariant under Lv,j 7→ Lv,j + bv + aj , where bv and aj are view- and formulation-specific offsets."
[^c4]: xiong-2026 — "Relation-Orbit yields higher mean test coverage at a 10% selective-risk calibration target than an all-eight Orbit-Max baseline in all eight dataset–backbone settings"
[^c5]: xiong-2026 — "An above–below pilot with vertical reflection produced no stable matched-budget gains, underscoring that a semantically valid visual involution cannot be assumed across relations; stringent targets may yield abstain-all."
[^c6]: xiong-2026
