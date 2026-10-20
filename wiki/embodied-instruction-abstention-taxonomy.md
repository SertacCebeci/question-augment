---
description: "An eight-category taxonomy of why an embodied VLM planner should abstain from executing an instruction — reference grounding, execution feasibility, or false premise — measured across frontier models."
aliases: ["ROBOABSTENTION", "abstention taxonomy for embodied robotic agents", "eight abstention categories"]
sources: ["yeke-2026"]
---
# Embodied instruction-abstention taxonomy

> Before a robot acts on an instruction, it must decide whether the
> instruction is even actionable as given — and the reasons it might not be
> split into three families, only one of which is [[efe-planning-as-variational-inference|ambiguity]].

## Definition / Mechanism

Yeke, Temirel & Shreekumar (2026) organize the reasons a
vision-language-model [[planner-dynamic-stopping|planner]] should refuse to execute a natural-language
instruction by where in the execution pipeline the defect sits: "First,
Reference Grounding covers instructions that cannot be reliably mapped to a
unique, objective target or goal in the observed scene because the referent
is missing, ambiguous, underspecified, or dependent on subjective user
preferences. Second, Execution Feasibility covers instructions that can be
interpreted but cannot be validly executed because they violate physical
constraints, require capabilities unavailable to the robot, or impose
mutually incompatible requirements. Finally, False Premise covers
instructions that are grounded and otherwise executable but presuppose a
world state contradicted by the scene."[^c1]

The three families expand into eight categories. "Reference Grounding
consists of Missing Referent, Ambiguous Referent, Underspecified Intent,
and Subjective Intent. Execution Feasibility consists of Physical
Infeasibility, Missing Capability, and Contradictory Instructions" — plus
False Premise itself.[^c2]

Each category is instantiated deterministically from a structured scene
representation (VLM visual grounding, then rule-based constraint
derivation, then template instruction generation) over 1,250 images from
five real robotics datasets, producing 6,069 evaluation instructions.

## Why it matters

Frontier models abstain on a minority of instructions that require it.
"Gemini 2.5 Flash has the highest [[abstention]] rate at 39.0%, while Qwen 3.5
27B has the lowest rate at 9.2%. Notably, Gemini Robotics ER 1.6 Preview,
an embodied robotics-specific planner, also has a very low abstention rate
at 16.5%."[^c3]

The categories are not equally hard: "ambiguous referent tasks had the
lowest abstention rate at 2.6% while missing referent had the highest at
41.3%" — models guess at an ambiguous referent but resist a referent that
is simply absent.[^c4]

Extra inference effort does not help: "increasing the reasoning level
hurts abstention performance... additional deliberation may encourage
models to construct plausible action plans or workarounds rather than
recognize when no valid execution is warranted."[^c5]

For a stall-2 selection criterion, the taxonomy names *why* a candidate
axis of $W$ might not be resolvable from the current instruction and scene
at all — before any [[value-of-information]] computation is even applicable,
the planner must first recognize which of three defect classes it is
looking at, since the corrective action differs (ask, refuse, or fail
gracefully).

## Limits

- Instructions are synthetic, template-generated from a rule-based
  constraint layer over VLM-extracted scene structure — not naturally
  occurring robot commands, and errors in the phase-1 visual grounding
  propagate into the labelled category.
- Evaluated as a single forced binary (abstain / act) on isolated images
  with no interaction history or dialogue; the taxonomy motivates a *reason
  not to act*, not a specific asking strategy or question form.
- Category granularity was chosen by the authors to fit robot manipulation
  in one benchmark (two capabilities: vision and a gripper); a robot with
  other sensors or actuators is not covered by "Missing Capability" as
  defined here.

## Related

[[false-premise-question]] · [[embodied-ambiguity-sources]] · [[abstention]] · [[ambiguity-taxonomy]] · [[clarification-benchmarks]]

[^c1]: yeke-2026 — "First, Reference Grounding covers instructions that cannot be reliably mapped to a unique, objective target or goal in the observed scene because the referent is missing, ambiguous, underspecified, or dependent on subjective user preferences. Second, Execution Feasibility covers instructions that can be interpreted but cannot be validly executed because they violate physical constraints, require capabilities unavailable to the robot, or impose mutually incompatible requirements. Finally, False Premise covers instructions that are grounded and otherwise executable but presuppose a world state contradicted by the scene."
[^c2]: yeke-2026 — "Reference Grounding consists of Missing Referent, Ambiguous Referent, Underspecified Intent, and Subjective Intent. Execution Feasibility consists of Physical Infeasibility, Missing Capability, and Contradictory Instructions"
[^c3]: yeke-2026 — "Gemini 2.5 Flash has the highest abstention rate at 39.0%, while Qwen 3.5 27B has the lowest rate at 9.2%. Notably, Gemini Robotics ER 1.6 Preview, an embodied robotics-specific planner, also has a very low abstention rate at 16.5%."
[^c4]: yeke-2026 — "ambiguous referent tasks had the lowest abstention rate at 2.6% while missing referent had the highest at 41.3%"
[^c5]: yeke-2026
