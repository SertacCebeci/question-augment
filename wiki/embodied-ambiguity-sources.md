---
description: "A robot's ambiguity splits into observation incompleteness (unobserved evidence) and semantic/intent ambiguity (the user's preference); a VLM policy routes among observe, ask and select accordingly."
aliases: ["active-perception-based embodied disambiguation", "two sources of embodied ambiguity"]
sources: ["liu-2026-active"]
---
# Two sources of embodied ambiguity

> Before asking the user, ask whether the missing information is even in the
> user: some [[efe-planning-as-variational-inference|ambiguity]] is a fact about the world the robot has not yet
> looked at.

## Definition / Mechanism

Liu & Yang (2026) formalize an embodied robot's target-disambiguation state
as $u$ (instruction), $o$ (visual observation), and $g^\star$ (the intended
physical target), and distinguish two sources of missing information by
where it resides. Observation incompleteness: "the current observation does
not provide all task-relevant physical evidence required to resolve the
target" — an occluded surface, unreadable text, or a target outside the
current view. Semantic or intent ambiguity: "the environment may be
sufficiently visible, while the instruction still fails to specify the
user's preference."[^c1]

A vision-language model makes a high-level decision $\alpha \in \{O, Q,
S\}$ at each step: "O acquires another physical camera observation, Q
queries the user for clarification, and S commits to the resolved physical
target" — with observation supplying the physical evidence that subsequent
clarification and selection then operate on, so the three are not
independent channels but a single accumulating process.[^c2]

## Why it matters

The routing rule the paper draws from its own results is explicit about
which source to consult first: "When the missing information is in the
world—an occluded surface, unreadable text, or an unobserved region—active
observation supplies it. When the scene is sufficiently visible but the
user preference remains unspecified, clarification supplies the missing
intent. The source of the uncertainty therefore determines the useful next
action."[^c4]

Real-robot experiments (PiPER arm, eye-in-hand RGB-D camera) tested this
against three fixed baselines — passive selection, and two SeeAsk-style
askers (greedy confirmation, static attribute question) that never move
the camera — over nine matched scenarios and four methods per scenario,
36 trials in total, spanning three regimes: recovering evidence for an
already-observed target, improving the semantic grounding of a
clarification that is still needed, and finding a target outside the
initial view.[^c3]

## Limits

- 9 scenarios × 4 methods on one robot platform (PiPER + DABAI DC1) and one
  VLM (Qwen3.7-Plus); no statistical test is reported and the fixed
  baselines are hand-built re-implementations of a prior system (SeeAsk),
  not the field's full range of asking strategies.
- The routing decision inside the VLM carries no explicit scoring rule
  analogous to [[expected-information-gain]] or [[value-of-information]] —
  which action to take is the model's own judgement each step, not an
  optimized or provably convergent criterion.
- The authors scope the claim themselves: it covers cases where the
  decisive information must be acquired in the current interaction, and
  explicitly excludes cases where active observation reveals only an
  intermediate semantic cue that the VLM must then reason over using
  pretrained knowledge before the target is resolved.

## Related

[[epistemic-actions]] · [[value-of-information]] · [[expected-information-gain]] · [[ambiguity-taxonomy]]

[^c1]: liu-2026-active — "The current observation does not provide all task-relevant physical evidence required to resolve the target."
[^c2]: liu-2026-active — "The VLM makes a high-level decision α ∈ {O, Q, S}, where O acquires another physical camera observation, Q queries the user for clarification, and S commits to the resolved physical target."
[^c3]: liu-2026-active — "The main comparison contains nine matched scenarios and four methods per scenario, for 36 real-robot trials."
[^c4]: liu-2026-active — "The source of the uncertainty therefore determines the useful next action."
