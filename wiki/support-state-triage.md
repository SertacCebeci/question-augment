---
description: "A four-state ontology — Complete, Clarifiable, Support-Blocked, Unsupported-Now — typing why a task is not yet actionable so an agent picks the matching first action."
aliases: ["SSTA-32", "support-state ontology", "typed deferral", "Preflight Support Check", "PSC"]
sources: ["arxiv-2604-16752"]
---
# Support-state triage

> Before acting, an agent's first question is not "how confident am I?" but "which of four kinds of support am I missing?"

## Definition / Mechanism

Unlu (2026) types every non-solvable task instance by its
*minimal repair distance* from solvability, given a request `u`, in-context
evidence `e`, an available support set `z` (tools, permissions, artifacts) and
an environmental contract `κ` (explicit restrictions like "use only this
excerpt"). A task is **Complete** if already solvable: "Complete if
solvable(u, e, z, κ). Gold action: ANSWER."
[^c1]

It is **Clarifiable** if exactly one semantic clarification repairs it:
"Clarifiable if not complete, but there exists exactly one semantic
clarification c such that solvable(u ⊕ c, e, z, κ). Gold action: CLARIFY."
[^c2]

It is **Support-Blocked** if exactly one support grant repairs it: "there
exists exactly one support grant s (a tool, permission, or artifact access)
such that solvable(u, e, z ⊕ s, κ). Gold action: REQUEST SUPPORT."
[^c3]

Otherwise it is **Unsupported-Now** — "if neither a one-step clarification
nor a one-step support grant makes the request solvable under κ" — gold
action ABSTAIN.
[^c4]

The taxonomy is enforced one-blocker-per-item by construction (SSTA-32's
32-item counterfactual dataset), so the four states are mutually exclusive by
design, not by classifier confidence.

The mechanism that activates the typing is **surfacing the four-label action
vocabulary in the prompt** — either a bare forced choice among the four
labels (Action-Only) or the same choice preceded by a four-boolean Preflight
Support Check (`info_sufficient`, `support_sufficient`, `evidence_sufficient`,
`budget_sufficient`) that maps the first false boolean to its action (PSC).

## Why it matters

A frontier model given no action vocabulary overcommits heavily: "Default
execution overcommits heavily on non-complete tasks (41.7% overcommitment
rate)."
[^c5]

Replacing that default with a *scalar confidence number* instead of typed
labels removes the overcommitment but destroys the typing — a low-confidence
score gets mapped to ABSTAIN regardless of whether the correct action was
CLARIFY or REQUEST SUPPORT: "Scalar confidence mapping avoids overcommitment
but collapses the three-way deferral space (58.3% typed deferral accuracy)."
[^c6]

Simply forcing a choice among the four category labels, with no other
scaffold, recovers both properties at once: "both Action-Only and PSC
achieve 91.7% typed deferral accuracy by surfacing the categorical ontology
in the prompt."
[^c7]

The multi-step Preflight checklist adds nothing over the bare forced choice:
"The Action-Only ceiling effect suggests that simply surfacing the
four-category ontology in the system prompt is sufficient to activate latent
triage capabilities" — implying the bottleneck is the missing decision
vocabulary, not missing reasoning capacity.
[^c8]

Ablating either checklist dimension confirms the ontology's parts are
load-bearing rather than redundant: "Removing either PSC dimension causes
targeted degradation: PSC−Support loses REQUEST SUPPORT accuracy;
PSC−Evidence triggers large-scale overcommitment on unsupported items."
[^c9]

## Limits

The audit is single-session **Dual-Persona Auto-Auditing**: subject and
scorer share one context that also holds the gold-label ontology, so
Action-Only and PSC numbers are *upper-bound* capability estimates under
maximal contextual priming, not unprimed zero-shot behavior — the paper
itself calls for API-isolated multi-model replication. The dataset is small
(N=32, 24 non-complete) and drawn from one frontier model and eight task
families, so effect sizes below the paper's own >30pp threshold are
unverified. Only the first classification action is scored, not downstream
follow-through — a model that types correctly may still fail to execute the
clarification or support request that follows. The taxonomy explicitly
excludes preference-aware repair, multi-step search termination and
progressive blocker discovery, so it does not generalize to agents facing
those failure modes.

## Related

[[abstention]] · [[detection-to-abstention-gap]] ·
[[sigma-triage-regenerate-or-abstain]] · [[i-calm]] ·
[[clarification-request]]

[^c1]: arxiv-2604-16752 — "Complete if solvable(u, e, z, κ). Gold action: ANSWER."
[^c2]: arxiv-2604-16752 — "Clarifiable if not complete, but there exists exactly one semantic clarification c such that solvable(u ⊕ c, e, z, κ). Gold action: CLARIFY."
[^c3]: arxiv-2604-16752 — "Support-Blocked if not complete, but there exists exactly one support grant s (a tool, permission, or artifact access) such that solvable(u, e, z ⊕ s, κ). Gold action: REQUEST SUPPORT."
[^c4]: arxiv-2604-16752 — "Unsupported-Now if neither a one-step clarification nor a one-step support grant makes the request solvable under κ."
[^c5]: arxiv-2604-16752 — "Default execution overcommits heavily on non-complete tasks (41.7% overcommitment rate)."
[^c6]: arxiv-2604-16752 — "Scalar confidence mapping avoids overcommitment but collapses the three-way deferral space (58.3% typed deferral accuracy)."
[^c7]: arxiv-2604-16752 — "both Action-Only and PSC achieve 91.7% typed deferral accuracy by surfacing the categorical ontology in the prompt"
[^c8]: arxiv-2604-16752 — "The Action-Only ceiling effect suggests that simply surfacing the four-category ontology in the system prompt is sufficient to activate latent triage capabilities."
[^c9]: arxiv-2604-16752 — "Removing either PSC dimension causes targeted degradation: PSC−Support loses REQUEST SUPPORT accuracy; PSC−Evidence triggers large-scale overcommitment on unsupported items."
