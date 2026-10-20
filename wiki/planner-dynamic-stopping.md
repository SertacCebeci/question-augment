---
description: "An embodied agent's Planner module decides whether current observations suffice to act, triggers targeted physical exploration when they do not, and halts once enough evidence is gathered."
aliases: ["Planner", "dynamic stopping criterion"]
sources: ["lin-2026"]
---
# Planner dynamic stopping (embodied active perception)

> A stopping rule for a robot deciding whether it has looked long enough:
> not a threshold on accumulated evidence, but a learned judgement of
> [[sufficient-statistic|sufficiency]], re-made after every probe.

## Definition / Mechanism

In Lin et al. (2026)'s PhysCaP agent, "the Planner identifies
missing physical information and initiates targeted exploration when
necessary. It also serves as a dynamic stopping criterion, terminating
exploration once sufficient evidence has been gathered and triggering the
downstream code-generation agent."[^c1]

The Planner outputs a JSON list of exploration candidates (object,
description, expected information) each cycle; after each physical probe
(a `get_mass` or `get_stiffness` call) it re-evaluates whether the task can
now be executed reliably, rather than stopping at a fixed count of probes
or a fixed evidence threshold.[^c2]

The paper frames this against two failure modes it names explicitly:
"under-exploration" (acting on insufficient physical evidence) and
"over-exploration" (continuing to interact once the task is already
decidable); across passive, naive-interactive and full-system conditions,
"existing passive and naive interactive baselines either fail when
physical properties are hidden or over-explore, whereas PhysCaP achieves
comparable performance with fewer interactions and reduced execution
time."[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| Embodied agents (PhysCaP, Lin et al. 2026) | Planner | exact |
| Embodied agents (PhysCaP, Lin et al. 2026) | dynamic stopping criterion | exact |

## Why it matters

This is stall 7 — is $|W|$ small enough? — answered by a VLM's own
judgement of task-sufficiency rather than by a declared error-rate
threshold. It sits next to [[sprt]] as a second instance of the same
question — stop when evidence, not count, says so — but with no accuracy
guarantee attached to the stopping point.

## Limits

- No error rate is declared or bounded. Unlike [[sprt]], which stops on a
  log-[[likelihood-ratio]] crossing $A$ or $B$ fixed from target $(\alpha,\beta)$,
  the Planner's "sufficient evidence" is an unquantified VLM judgement; the
  paper reports task success rate, not a stopping-accuracy guarantee.
- Demonstrated only on partially-observable tabletop manipulation with two
  physical-property probes (mass, stiffness) on one robot arm; whether the
  same stopping judgement generalises to more axes or a larger candidate
  set is untested here.
- Ablating the [[priority-scored-candidate-ranking|Prioritizer]] while keeping the Planner (the `CaP+PhysX+Planner`
  row of Table 1) still over-explores relative to the full system on two of
  three tasks, so the stopping decision alone does not obtain PhysCaP's
  efficiency — it depends on the candidate order the Prioritizer supplies.
- No formalism is imported — the stopping judgement is a learned/prompted
  VLM decision, not a derived rule — so `## Transfer` does not apply; the
  contrast with [[sprt]]'s derived thresholds is the point of the note.

## Related

[[sprt]] · [[value-of-information]] · [[priority-scored-candidate-ranking]]

[^c1]: lin-2026 — "the Planner identifies missing physical information and initiates targeted exploration when necessary. It also serves as a dynamic stopping criterion, terminating exploration once sufficient evidence has been gathered and triggering the downstream code-generation agent."
[^c2]: lin-2026 — "Specifically, the Planner outputs a list of candidates in a JSON file, each with an object name, description, and expected information for exploring the object."
[^c3]: lin-2026 — "existing passive and naive interactive baselines either fail when physical properties are hidden or over-explore, whereas PhysCaP achieves comparable performance with fewer interactions and reduced execution time."
