---
description: "When a fixed hypothesis space cannot represent a word's meaning, an LLM proposes candidate rules in a restricted language while a deterministic script alone verifies and promotes them."
aliases: ["generate-and-test proposer", "LLM proposer arm"]
sources: ["cordella-2026"]
---
# LLM hypothesis proposer

> A generate-and-test pattern for extending the candidate [[possible-worlds|hypothesis space]]
> itself: an LLM proposes rule candidates outside the scripted space, a
> deterministic script alone decides whether any is promoted.

## Definition / Mechanism

Two words in Cordella & Cappelli (2026)'s constructed
lexicon are "provably outside the base hypothesis space" — one
history-dependent, one an XOR-structured contextual homonym — so no scripted
candidate can ever match them: "the base learner leaves NUR and GUMO
unresolved in 30/30 runs each, with zero kangaroos: a hypothesis space that
cannot represent a referent [is] harmless by construction."[^c1]

When a word's hypothesis set empties, "the observation log is shown to an
LLM that proposes up to five candidate rules in a restricted DSL
(conjunctions, relational comparisons ..., attribute-change predicates,
two-clause disjunctions); the script compiles the candidates, validates
them semantically, filters them against the entire log, and subjects
survivors to $M=4$ fresh pre-registered probes ... before any promotion.
The LLM proposes; the script disposes."[^c2]

Across a capability ladder (no proposer, Claude Haiku 4.5, Claude Sonnet
4.6, a hand-coded oracle space), "coverage scales with proposer capability
(0% → 18% → 72% → 100%) while undetected mistranslations remained at zero
throughout."[^c3]

The judge — semantic validation, retrospective log filtering, fresh
pre-registered probes — never moves to the LLM side; only the space of
candidates does.

## Why it matters

This is a concrete generator for an axis a fixed selection criterion cannot
see: when $\mathcal{H}_0$ has no member that fits the data, no scoring rule
over $\mathcal{H}_0$ ([[mutual-information|mutual information]], GBS's split) can propose the
missing dimension — only something that can generate outside the enumerated
set can. Here that generator is an LLM, kept out of the decision that
promotes or rejects what it proposes.

## Limits

Tested only in one micro-world (32 scenes, two hard words) with a
restricted candidate DSL chosen by the authors; "precision" (log-coherent
candidates over compiled candidates) rose with model capability (~11% to
~67%) but never reached 100%, so the pattern's cost is in discarded
proposals, not in false promotions — the zero-kangaroo guarantee rests
entirely on the script-side verifier, not on proposer [[calibration|reliability]], and this
note makes no claim about domains where a script cannot cheaply verify a
proposed rule against a log.

## Related

[[expected-information-gain]] · [[generalized-binary-search]] · [[version-space]] · [[constraint-seeking]]

[^c1]: cordella-2026
[^c2]: cordella-2026
[^c3]: cordella-2026 — "coverage scales with proposer capability (0% → 18% → 72% → 100%) while undetected mistranslations remained at zero throughout"
