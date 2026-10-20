---
description: "A fixed-pool selective-classification method that forces a label only when every Lipschitz-consistent, margin-certified head in a version space agrees, and abstains otherwise."
aliases: ["Lipschitz-consistent version space", "agreement-based selective prediction", "force-or-abstain certificate"]
sources: ["khosravani-2026"]
---
# Lipschitz-consistent version space

> A [[version-space|version space]] computed not from labelled instances but from certified
> geometric envelopes: predict when every consistent head is forced to the
> same class, abstain otherwise — commitment decided by agreement, not by a
> confidence threshold.

## Definition / Mechanism

Fix an embedding $g$ and a labelled subset $S$ with center-margin lower
bounds $m_i$. Khosravani (2026) defines the
**Lipschitz-consistent head class** $F(S)$: every head whose one-vs-rest
margins are $L_{M,c}$-Lipschitz and meet the center constraint at each
labelled point. "Define F (S) as the set of heads f˜ : Rm → RC whose
induced margins M̃c satisfy: 1. (Lipschitz) each M̃c is LM,c -Lipschitz as
in Assumption 1; 2. (Center constraints) for all i ∈ S, M̃yi (zi ) ≥ mi."[^c1]

A label is **forced** at pool point $u$ only when every head in $F(S)$
agrees: "A class c⋆ is forced at pool index u if for every f˜ ∈ F(S) and
every ŷf˜(u) ∈ arg maxc f˜c (zu ) we have ŷf˜(u) = c⋆ . Otherwise we
abstain."[^c2]

The mechanism is computable: two-sided margin envelopes ($LB_c$, $UB_c$)
propagate certified evidence from labelled centers to the whole pool, and
the label is forced exactly when the certified feasible set collapses to
one class — "if Γ (u) = {c⋆ } is a singleton, then every f˜ ∈ F (S)
predicts c⋆ at u" — or when a gap-forcing rule holds instead: "If the
condition in Definition 10 holds, then every f˜ ∈ F (S) predicts c⋆ at
u."[^c3]

A closure property lets this run iteratively: forced pseudo-labels can be
folded back in as new centers without shrinking $F(S)$ further —
"adding forced pseudo-labels as new centers does not strengthen the
consistency constraints: the version space (and hence the semantics of
the certificates) remains unchanged."[^c4]

The author distinguishes this from [[conformal-prediction|conformal prediction]]: "unlike
conformal prediction [13–15], they encode labels consistent with a
constraint-defined hypothesis class on a fixed pool rather than
distribution-free marginal coverage."[^c5]

## Why it matters

On stall 10 the answerer's problem is not just scoring confidence but
deciding *when a claim is forced* by what it already committed to. This
method replaces a tuned confidence threshold with an agreement test over
an explicit, geometrically certified hypothesis class: the answerer
commits only when every model consistent with its prior commitments and
its stated smoothness assumption would say the same thing, and otherwise
declares the gap. The closure property means self-certified answers do
not silently inflate confidence in what follows — each pseudo-label adds
no new constraint beyond what was already entailed.

## Transfer

| | Home field | Here |
|---|---|---|
| Consistency set | classification heads agreeing with labelled examples under a Lipschitz margin bound | claims consistent with everything already committed to, under a declared smoothness/coherence assumption |
| What survives | the force-only-on-agreement rule, and the closure property that certified conclusions do not shrink the space further | |
| What does not | the specific machinery — a fixed embedding $g$, computable Lipschitz constants, a transductive fixed pool known in advance — none of which has an analogue for open-ended, sequentially arriving axes | |

## Limits

- The certificate is only as good as the declared Lipschitz bounds
  $L_{M,c}$; these are *computable upper bounds*, not the true constants,
  and the whole hypothesis class $F(S)$ is defined relative to them. If
  the bounds are wrong, the "sound" guarantee is vacuous, not false —
  but nothing in the method checks the bounds against reality.
- Everything is relative to one fixed representation $g$; the paper notes
  the certificates must be recomputed whenever $g$ changes, so a method
  applied to a changing world model needs re-certification, not amortised
  reuse.
- The guarantees certify **agreement** (identifiability within $F(S)$),
  not correctness; the paper defers the conditions under which agreement
  implies correctness to unread supplementary material — this note claims
  no such conditions.
- The setting is transductive and fixed-pool: the set of candidate points
  is known in advance. An asker facing axes that appear only as the
  conversation unfolds has no fixed pool to certify against.

## Related

[[version-space]] · [[abstention]] · [[conformal-prediction]] · [[calibration]]

[^c1]: khosravani-2026
[^c2]: khosravani-2026 — "A class c⋆ is forced at pool index u if for every f˜ ∈ F(S) and every ŷf˜(u) ∈ arg maxc f˜c (zu ) we have ŷf˜(u) = c⋆ . Otherwise we abstain."
[^c3]: khosravani-2026 — "if Γ (u) = {c⋆ } is a singleton, then every f˜ ∈ F (S) predicts c⋆ at u."
[^c4]: khosravani-2026 — "adding forced pseudo-labels as new centers does not strengthen the consistency constraints: the version space (and hence the semantics of the certificates) remains unchanged."
[^c5]: khosravani-2026 — "unlike conformal prediction [13–15], they encode labels consistent with a constraint-defined hypothesis class on a fixed pool rather than distribution-free marginal coverage."
