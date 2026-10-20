---
description: "A robot executes a geometrically valid action on the wrong physical object because referent ambiguity was collapsed before execution instead of triggering a query."
aliases: ["identity switch", "wrong-object execution", "confident wrong-object execution"]
sources: ["wei-2026"]
---
# Identity switch

> A perfectly executed action on the wrong object: the manipulator's motion
> is valid, but the referent it committed to was never actually determined.

## Definition / Mechanism

"In cluttered scenes containing repeated objects, ambiguous anchors, or
frame-dependent spatial terms, a robot can execute a geometrically valid
action on a semantically compatible but unintended instance; we call this
failure an identity switch." Wei et al. (2026)[^c1]

The referent of a manipulation instruction is jointly fixed by three coupled
variables — the target object, the anchor object a spatial relation names,
and the reference frame a directional term is read in. An identity switch
occurs when a system commits early to a single value of one or more of these
(the common pattern in end-to-end vision-language-action policies and
LLM-driven pipelines that ground the scene once and never revisit it) and
the committed value turns out not to be the one the instruction intended,
even though the resulting action is physically well-formed. It is distinct
from a grasp failure or a misdetection: perception and motion planning both
succeed, and the error is invisible to any check that only asks "is this
action feasible."

Measured on a real UF850 arm across [[efe-planning-as-variational-inference|ambiguity]]-stress trials with duplicate
targets, duplicate anchors, and frame-dependent instructions: "RefGuard
records no identity switch on any ambiguity-stress trial and executes
correctly on 90.0% of them, whereas fine-tuned VLA and LLM (Large Language
Model)-based baselines switch identity in 33-46% of the same trials."[^c2]

## Why it matters

Identity switch is the concrete, measured cost of collapsing ambiguity
before acting rather than asking, reobserving, or refusing
([[refguard-decision-policy]]): a system judged only on task-completion or
grasp-success rate can score well while silently acting on the wrong object,
because nothing in the action itself records that its referent was
uncertain.

## Limits

- Defined and measured only for physical manipulation with a discrete,
  enumerable object set; the concept has not been shown to transfer to
  domains without a physical action whose target is checkable after the
  fact (e.g. open-ended text generation).
- The 0% vs. 33–46% contrast is one lab's real-robot trial suite (UF850 arm,
  RGB-D perception, GPT-4o parser) against three specific baselines
  (GR00T, π0.5, an LLM-based pipeline); it is not a general bound on how
  often early commitment fails.
- The rate depends on how "ambiguity-stress" trials are constructed
  (duplicate targets/anchors, frame-dependent phrasing); a scene without
  these properties would show a lower baseline switch rate.

## Related

[[refguard-decision-policy]] · [[clarification-benchmarks]]

[^c1]: wei-2026 — "In cluttered scenes containing repeated objects, ambiguous anchors, or frame-dependent spatial terms, a robot can execute a geometrically valid action on a semantically compatible but unintended instance; we call this failure an identity switch."
[^c2]: wei-2026
