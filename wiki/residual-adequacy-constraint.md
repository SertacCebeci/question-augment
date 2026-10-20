---
description: "One quantity — the residual of content against an agent's active representational scope — is proposed to govern acting, learning, and modelling another agent, evaluated at three different scopes."
aliases: ["residual-adequacy constraint", "residual adequacy"]
sources: ["amornbunchornvej-2026"]
---
# Residual-adequacy constraint

> A claim that three separately-mechanised limits on an agent — when it can act, what it can learn now, and where it will misunderstand another agent — reduce to reading one quantity at three scopes rather than three unrelated mechanisms.

## Definition / Mechanism

The residual $r(c)$ is the part of a content vector $c$ an agent's currently active representational regimes fail to represent (the norm of what an interpretation map leaves unexplained). Amornbunchornvej's central claim is that acting, learning, and modelling another agent are governed by the same residual-against-scope quantity, read at three different scopes: at the scope of one decision, low residual with conflict-free licensed actions permits a clean emission and high residual forces a halt or representational expansion; at the scope of a bounded focus window, whether the residual concentrates within that window (rather than spreading across it) determines what can be learned in the present step; at the scope of another agent modelled through one's own basis, the residual between a simulated and an actual witness is what "empathy error" measures.[^c1]

The engine's mechanics are held fixed across the three scopes; only the open parameters (regime family, thresholds, focus window, attention machine) are bound differently per instantiation.[^c2]

## Why it matters

For an asking/answering agent this reframes three separate design questions — when to stop and answer, what to attempt to learn before answering, and when a model of the other party can be trusted — as reads of one scalar under different scopes rather than three independently-tuned heuristics, giving a single lever (representational scope, i.e. what regimes/axes the agent currently has) instead of three.

## Limits

The unification is argued by showing the same fixed mechanics reproduce three independently-documented phenomena (typed not-knowing, a theory-of-mind error, and prerequisite-structured learning) under different parameter bindings — it is a structural-parsimony argument with worked hand examples and one small synthetic ($\mathbb{R}^4$) implementation, not a proof that no other quantity could explain the same three phenomena, and not tested against real human or LLM-agent data. It is an unreviewed 2026 preprint. [?]

## Related

[[interpretation-decision-unit]] · [[bounded-empathy]] · [[value-of-information]]

[^c1]: amornbunchornvej-2026
[^c2]: amornbunchornvej-2026 — "An instantiation binds them to fit a case, without changing the mechanics."
