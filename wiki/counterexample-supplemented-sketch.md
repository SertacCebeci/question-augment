---
description: "A repository-native coding-agent workflow where an ambiguous or conflicting change-authority declaration blocks the edit and forces a clarification question instead of a guess."
aliases: ["Sketch-CE", "counterexample-supplemented sketch"]
sources: ["castle-2026"]
---
# Counterexample-supplemented sketch

> A coding agent that cannot tell, from its own call, whether it has the
> authority to make a change does not guess: it leaves the files alone and
> asks — and the next candidate case is withheld until the current one is
> resolved by two independent checks, not one.

## Definition / Mechanism

Castle & Rubeck (2026) describe a loop with six artifacts —
a partial-program *sketch* $S$, an accepted-counterexample *[[archive-ambiguity-detection|archive]]* $A$, a
curated *regression set* $R \subseteq A$, known-code *anchors*, a
dual-oracle implementation (deterministic code plus prompt-mediated
completion), and a deterministic *gate*. Every call the coding agent
("Developer") makes states its own change authority together with the
rules, holes, anchors and approved behaviour that must survive it: "Every
Developer call names its change authority and the rules, holes, anchors,
and approved behavior that must survive. Conflict or ambiguous permission
leaves the files unchanged and produces a clarification question."[^c1]

Until an operator explicitly approves a candidate failure, it is evidence,
not a rule the archive can cite: "If the case counters the current sketch,
the system raises it to an operator. Only explicit approval gives the case
specification authority."[^c2]

The loop also fixes an order on what gets revealed next, so a candidate is
never exchanged for another while it is still open on either check: "No new
counterexample is revealed until the active case and selected regressions
pass the deterministic gate and a capable model or person reviews their
simulated outputs against the current sketch."[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| software-engineering (Castle & Rubeck 2026) | Sketch-CE | exact |
| software-engineering (Castle & Rubeck 2026) | counterexample-supplemented sketch | exact |
[^c4]

## Why it matters

This is a concrete instance of stall 2 answered by refusal rather than by
ranking: the agent is not choosing among several already-enumerated
candidate edits by a score — it is declining to act at all when its own
stated authority is ambiguous, and only then emitting a question. It also
bears on stall 4 (who may answer): specification authority is reserved to
the human operator, never assumed by the agent from a [[proactive-expertise-clarification|passing]] test or a
plausible repair. On the reported CatSynth captures, the protocol that adds
the second check (sketch review, not just the deterministic gate) passed
more withheld cases than replay alone — 8/8 visible cases each, then
14/21, 17/21 and 16/21 of 21 withheld cases for replay-all, evolved-sketch
rebuild and retained Sketch-CE respectively, with the reviewed evolved
sketch three withheld cases ahead of raw replay.[^c5]

## Transfer

| | |
|---|---|
| In its home field | classical CEGIS (counterexample-guided inductive synthesis): a solver iterates candidate programs against a verifier-supplied counterexample until none remains, under stated formal assumptions |
| Here | a repository where the "specification" is a human-maintained, partial sketch and counterexamples are operator-approved SME corrections rather than solver output |
| What survives | the discipline of turning a rejected candidate into a rule every later candidate must satisfy, plus the refusal to act on an ambiguous authority claim |
| What does not | the solver-backed soundness/completeness guarantee — "Classical CEGIS already has counterexample discipline when its formal assumptions hold. Repository work is smaller and messier... without treating the result as a solver-backed proof." |
[^c6]

## Limits

- The clarification-question trigger itself (^c1) is stated once, in the
  abstract and introduction; the paper reports no rate at which it fires
  and no isolated measurement of its effect — the withheld-case numbers
  (^c5) evaluate the two-check protocol as a whole, not this trigger alone.
- All results are from one synthetic captured application (CatSynth), one
  or two models, and one reveal order; the paper states this directly:
  "One model and one reveal order cannot establish general correctness or
  superiority."
- The earlier open-world capture that produced an alternate set of
  withheld-case numbers "lacked required sketch review and approval," so
  the two tables in the paper are not measuring identical protocols.

## Related

Selection · [[defect-localization]] · [[value-of-information]] · Source

[^c1]: castle-2026 — "Every Developer call names its change authority and the rules, holes, anchors, and approved behavior that must survive. Conflict or ambiguous permission leaves the files unchanged and produces a clarification question."
[^c2]: castle-2026 — "If the case counters the current sketch, the system raises it to an operator. Only explicit approval gives the case specification authority."
[^c3]: castle-2026 — "No new counterexample is revealed until the active case and selected regressions pass the deterministic gate and a capable model or person reviews their simulated outputs against the current sketch."
[^c4]: castle-2026 — "Agentic Synthesis against Counterexample-Supplemented Sketches"
[^c5]: castle-2026 — "Replay-all, evolved-sketch rebuild, and retained Sketch–CE all passed 8/8 visible accepted cases and then passed 14/21, 17/21, and 16/21 withheld cases, respectively."
[^c6]: castle-2026 — "Classical CEGIS already has counterexample discipline when its formal assumptions hold. Repository work is smaller and messier: the human strategy, the accepted counterexample, and the executable check often live in separate artifacts. The repair loop stores the links among them without treating the result as a solver-backed proof."
