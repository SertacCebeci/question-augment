---
description: "A typed slot dictionary that persists elicited constraints across conversation turns and gates deterministic retrieval, measured to be the component that prevents cross-turn constraint drift."
aliases: ["session-persistent preference layer", "session-persistent preference state", "preference pivot detection"]
sources: ["huang-2026-macs"]
---
# Session-persistent preference state

> Constraints elicited across separate turns cohere only if something keeps
> them; the something is tested here by deleting it and watching accumulation
> and reversal fail.

## Definition / Mechanism

Huang et al. (2026) track accepted constraints (budget,
brand exclusions, specification minimums) in a typed session dictionary that
persists across turns and is queried directly by the SQL enforcement layer,
rather than being re-derived from conversation history each turn: "A
session-persistent preference layer tracks constraints across turns,
enabling consistent handling of budget overwrites and exclusion reversals."[^c1]

The state supports three operations on a constraint already in the
dictionary: accumulation (a new constraint is added), update — "a new
budget ceiling replaces the previous value" — and reversal, where a
statement such as "actually HP is fine" reverses an earlier exclusion.[^c2]

## Findings

An ablation clears the slot dictionary after every turn while keeping LLM
conversation history (MACS-NoSession), re-run on all ten multi-turn
scenarios at five runs each: "MACS-Full achieved macro Pass@5 = 72% (mean
score 0.751); MACS-NoSession dropped to 52% / 0.673 (−20 pp, −0.078). The
drop concentrated in two scenarios: S1 (constraint accumulation across four
turns, 100%→0%) and S7 (budget overwrite, 100%→0%) ... Without the slot
dictionary, those predicates reset to unconstrained, and the correct
products were no longer filtered in." Scenarios driven only by within-turn
signals (exclusion reversal, price refinement, long session, dense
first-turn constraint) were unaffected by the ablation.[^c3]

Across all three systems tested (MACS, GPT-4o-mini+catalog, Gemini 2.5
Flash Lite+catalog), measured drift — "fraction of run-scenario pairs with
a constraint violation" — over 50 run-scenario pairs was 0.000 for MACS
and for GPT+Catalog; only Gemini+Catalog recorded a nonzero 0.014 (one
violation).[^c4]

## Why it matters

The ablation isolates what a session state is for on this stall: it is not
what makes constraints coherent in general — GPT+Catalog held zero drift too,
without any persistent structure, on this same benchmark — it is what makes
multi-turn, cross-turn coherence (accumulation, overwrite) survive when the
constraint was set several turns before it is checked. Within-turn coherence
and short-memory coherence did not need it; long-range coherence did.

## Limits

- Ten scripted scenarios, 50 data points at K=5, authored by the research
  team — the paper itself flags this may "introduce unintentional alignment
  between benchmark design and system structure."
- The zero-drift result is not unique to a session-persistent design:
  GPT+Catalog reached the same 0.000 drift on the same benchmark without
  persistent state, so drift alone does not distinguish the two
  architectures — Pass@5 on the accumulation/overwrite scenarios does.
- Single consumer-electronics catalog; no cross-domain test of the same
  slot-dictionary design.
- Response quality is LLM-judged (GPT-4o-mini), not human-rated.

## Related

[[deterministic-constraint-delegation]] · [[multi-agent-clarification]] · [[uncertainty-aware-multi-agent-scaffold]]

[^c1]: huang-2026-macs — "A session-persistent preference layer tracks constraints across turns, enabling consistent handling of budget overwrites and exclusion reversals."
[^c2]: huang-2026-macs — "a new budget ceiling replaces the previous value, and a statement such as “actually HP is fine” reverses an earlier brand exclusion"
[^c3]: huang-2026-macs
[^c4]: huang-2026-macs
