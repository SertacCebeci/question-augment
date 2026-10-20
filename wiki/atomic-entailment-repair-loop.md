---
description: "Decompose the source into atomic units, entail each against evidence in the output with a three-way label, accept only at zero-missing/zero-contradiction, else loop targeted repair to a budget."
aliases: ["atom-level entailment validation", "verification-driven self-correction", "conditional revision"]
sources: ["arxiv-2604-05489"]
---
# Atomic entailment repair loop

> Do not score the whole output against the whole source. Decompose the
> source into named atoms, retrieve one evidence chunk per atom, label
> each pair entailed, missing or contradicted, and repair only what the
> labels name — repeating until every atom is entailed or a round budget
> is spent.

## Definition / Mechanism

SCMAPR (2026) verifies a rewritten prompt against
the user's original input for a text-to-video system, but the checking
procedure itself does not depend on prompts or video:

1. **Atomize the source.** An LLM extracts a field-wise dictionary of
   atomic content units from the source ($D_A$: characters, objects,
   actions, locations, scenery for this paper's domain), flattened to a
   list $A = \{a_1, \dots, a_n\}$. These atoms are fixed verification
   targets for the rest of the procedure — the check never re-reads the
   source.
2. **Chunk the candidate.** The output under check is segmented into
   non-overlapping evidence units (sentence-level by default, short ones
   merged to a length threshold).
3. **Match.** Atoms and chunks are embedded into a shared semantic space
   and each atom is paired with its most relevant chunk — one
   evidence unit per atom, not the whole output.
4. **Entail, ternary.** An LLM judges each atom-evidence pair into one of
   three labels rather than a binary pass/fail: "the validator generates
   a ternary decision $v_i = \text{Validator}(a_i, e_i)$, where $v_i \in
   \{ET, MS, CT\}$... ET indicates that the semantics of $a_i$ are well
   supported by $e_i$. MS refers to the case, in which $e_i$ provides
   little support... CT indicates that $e_i$ has opposite semantic
   meanings compared to $a_i$."[^c1]
5. **Gate on a strict criterion, then repair only what failed.** "We
   enforce a strict acceptance criterion that the refinement is accepted
   only if $p_{ET} = 1$ (100%) and $p_{CT} = 0$. Otherwise, Entailment
   Validator returns structured feedback pinpointing missing or
   contradicted atoms, which triggers Content Reviser to revise the
   prompt and produce an updated $P_{rew}$. The procedure repeats until
   the acceptance criterion is met or a maximum number of revision
   rounds is reached." The feedback names *which* atoms failed and
   *how* (missing vs. contradicted), so revision is targeted rather than
   a full re-generation.

The round budget is a chosen constant, not a derived one, set from
observed convergence: "we set the maximum number of revision rounds to
five in our experiments" — chosen after finding that "86.47%
(818/946) of prompts are verified after one rewrite, 12.47% (118/946)
require two rewrites, and 1.06% (10/946) require three rewrites" on
one benchmark, with a similar long tail on a second. An ablation removing
this whole stage — atomization, matching, ternary entailment, gated
repair — "noticeably degrades performance (0.58%), verifying that
atom-level verification and conditional correction contribute to
maintaining semantic fidelity", a smaller effect than removing the
upstream routing stage (1.72%), so the loop is a real but secondary
contributor next to getting the first draft right.

## Why it matters

Two design choices generalize past this paper's prompts. First, the
ternary label separates "the source's atom is absent" from "the output
asserts the opposite" — a missing atom asks for elaboration, a
contradicted one asks for correction, and conflating them (a binary
check) throws away the signal a targeted repair needs. Second,
verification is scoped to one evidence chunk per atom rather than the
whole candidate, which is what lets the feedback name a specific atom
instead of a diffuse "this is inconsistent."

## Limits

- **The loop terminates on a budget, not a proof.** A maximum-round cap
  (five, chosen empirically) is the only guarantee against non-termination;
  a prompt that never reaches $p_{ET}=1, p_{CT}=0$ exits with residual
  missing or contradicted atoms and no repair.
- **Every stage is an LLM call**, named in the paper's own limitations:
  effectiveness "depends on the reasoning capability of the
  instruction-tuned LLM," and the atomization/matching/validation stages
  add inference overhead per round — this is unverified here as a
  general property, only reported for this framework's backbone.
- **The atom schema is fixed and domain-chosen** (five fields for a T2V
  prompt); porting the loop to another domain means re-deriving what
  counts as an atom, which this note does not attempt.
- **Only text was checked here.** The source paper states the framework
  is not extended to multimodal inputs.

## Related

[[conflict-driven-clause-learning]] · [[truth-maintenance-system]] ·
[[residue-of-a-contradiction]] · [[semantic-entropy]] ·
[[constraint-as-information]]

[^c1]: arxiv-2604-05489
