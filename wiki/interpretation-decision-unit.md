---
description: "A content-interpreting decision unit with finite deterministic regimes is proved total — it always halts in bounded steps, emitting an action or one of three typed, witnessed abstention terminals."
aliases: ["Interpretation-Decision Unit", "IDU", "totality and typed termination theorem", "Theorem 1 (Amornbunchornvej 2026)"]
sources: ["amornbunchornvej-2026"]
---
# Interpretation-Decision Unit

> A formal proof that a bounded, deterministic "should I answer or say what I lack" procedure always terminates, and that its non-answer always carries a structured reason rather than a bare confidence score.

## Definition / Mechanism

The Interpretation-Decision Unit (IDU) interprets a content vector $c$ through a finite family of **regimes** — local representational frames, each with a private basis — and computes a residual: the part of $c$ the active regimes fail to represent. If the residual is low and the actions the active regimes license are conflict-free, the unit emits a clean action. Otherwise it re-interprets a detected conflict, attempts a description-length-gated expansion of its own representation, or halts. Amornbunchornvej proves (Theorem 1) that for any content and any fixed, finite configuration — finite regime family, deterministic activation predicate, a fixed decision priority order, and a bounded re-entry counter $t_{max}$ — the unit halts in finitely many bounded-cost steps with a unique terminal witness.[^c1]

Every non-emitting halt is typed by the unresolved structure that caused it: $\mathrm{freeze}_{halt}$ (a regime licenses HALT outright), $\mathrm{freeze}_{time}$ (an unreconciled conflict or unresolved re-entry exhausts the counter), or $\mathrm{freeze}_{resid}$ (residual coordinates no regime can represent, after expansion fails). All three surface behaviourally as "will not answer," but the witness names which of the three occurred and on what content coordinates.[^c2]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Formal cognitive architecture | Interpretation-Decision Unit (IDU) | exact |
| Formal cognitive architecture | Theorem 1 / totality and typed termination | exact |

## Why it matters

Most machine-[[abstention]] treatments (reject option, selective prediction) gate on one scalar and report only that the system declined. This unit proves, rather than assumes, that a structured, multi-cause halt is achievable with a termination guarantee: the "abstain" branch is not an escape hatch that might loop or silently fail — it is a proven-total output with a labelled cause attached by construction. For an asking/answering agent this is a template for the commitment step: stop and name what is missing, rather than degrade to a confidence number.

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | Finite-state totality proof over a deterministic decision procedure with a bounded re-entry counter | A guarantee that an agent's "answer or say what's missing" step always halts with a labelled cause |
| Survives | The proof pattern: finite regime family + deterministic priority order + bounded counter ⇒ termination with a unique typed witness | |
| Does not survive | The specific linear/orthogonal-projection regime formalism (private bases, MDL-gated basis expansion) — it is a proof vehicle for one instance, not a ready criterion for which question-axis an agent should attend to next | |

## Limits

The guarantee is conditional on the stated finiteness and determinism assumptions (finite regime family, deterministic tie-breaking, a fixed re-entry bound $t_{max}$) holding for a given implementation; it says nothing about whether the three typed causes are the right taxonomy for a given domain, only that whichever causes are configured, the unit halts and reports one. The theorem is proved and demonstrated only for the linear instance (orthogonal-projection regimes) on one small synthetic ($\mathbb{R}^4$) implementation; this is an unreviewed 2026 preprint with no evaluation on real dialogue or agent tasks. [?]

## Related

[[abstention]] · [[sprt]] · [[value-of-information]]

[^c1]: amornbunchornvej-2026
[^c2]: amornbunchornvej-2026
