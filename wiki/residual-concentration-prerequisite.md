---
description: "Content is learnable only once its representational residual concentrates within a bounded focus window; a prerequisite is whatever acquisition achieves that concentration, not a fixed topic order."
aliases: ["residual-concentration prerequisite", "derived developmental prerequisites", "focus-window learnability"]
sources: ["amornbunchornvej-2026"]
---
# Residual-concentration prerequisite

> An order over what to acquire next is derived from geometry — whether the unexplained part of the target content can be pulled into a bounded attention window — rather than stipulated as a fixed curriculum.

## Definition / Mechanism

An agent can only admit a representational edit that reduces the residual within a focus window of size $w$ (the $w$ highest-residual coordinates); if the residual is spread over more coordinates than $w$ can hold, every candidate direction reduces only part of it, no edit is admissible, and learning is stuck. A basis set $B$ is a prerequisite for content $c$, relative to a configuration $\Gamma$ and window $w$, exactly when acquiring $B$ converts $c$ from unlearnable ($\lnot\,\mathrm{Learn}_w(c\mid\Gamma)$) to learnable ($\mathrm{Learn}_w(c\mid\Gamma\oplus B)$), because $B$'s presence concentrates the residual of $c$ into fewer coordinates.[^c1]

The relation this induces is agent-relative — it depends on the agent's current basis $\Gamma$ and its focus capacity $w$, so two agents can face different prerequisite structure over the same target — and need not form a global partial order; widening $w$ can itself remove a prerequisite dependency that a narrower window would have required.[^c2]

## Why it matters

For selecting which axis to ask about first, this gives a criterion distinct from [[expected-information-gain]] or greedy-[[entropy]] orderings: order not by which question drops the most uncertainty next, but by which acquisition would pull an otherwise-unlearnable target's residual into an attendable window — a target can be "worth asking about" and still be premature to ask about directly if its residual cannot yet be concentrated, and the fix is a different, prior question, not more of the same one.

## Limits

This is a derived-not-posited relation, distinct in kind from knowledge-space theory's elicited prerequisite graphs: it depends on treating "learnable" as a residual-concentration test under linear regimes and a fixed focus-window size, both open parameters chosen by the modeller rather than measured. It is demonstrated only on hand-worked examples (algebra before calculus; a framework's API conventions before a code edit) and one small synthetic implementation, with no test against real curriculum or question-sequencing data. It is an unreviewed 2026 preprint. [?]

## Related

[[residual-adequacy-constraint]] · [[expected-information-gain]] · [[optimal-decision-tree]]

[^c1]: amornbunchornvej-2026 — "A basis set B is a prerequisite for content c under configuration Γ when acquiring B converts c from unlearnable to learnable"
[^c2]: amornbunchornvej-2026 — "prerequisite dependence is agent-relative — it depends on Γ and w, so two learners with different held bases or focus capacities can face different prerequisite relations for the same target"
