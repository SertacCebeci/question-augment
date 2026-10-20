---
description: "A two-stage decide-then-write policy that picks one of six actions, including clarify, for an unresolved memory conflict instead of always committing to one value."
aliases: ["CAAP", "Conflict-Aware Action Policy"]
sources: ["yang-2026-when"]
---
# Conflict-Aware Action Policy

> Given a memory bank and a query, decide *how* to handle the unresolved
> conflict before writing anything — commit, hedge, verify, defer, ask, or
> try reversibly — instead of forcing every case through one fixed
> response template.

## Definition / Mechanism

Yang, Xu & Li (2026) design CAAP as two stages over a
visible memory bank $M$ and query $q$: a decision module produces "a brief
internal decision record $z$ (for example, what is uncertain and what
information is missing) and selects an action $a \in \mathcal{A}$", where
the action space is "$\mathcal{A} = \{$commit, conditionalize, clarify,
verify, defer, reversible\_trial$\}$"; a second, realization module then
turns $(M, q, z, a)$ into the natural-language response. "The decision
stage is instructed to choose the least cautious action that is still
justified by the visible evidence, while becoming more cautious when an
incorrect recommendation would have greater consequences." CAAP is not
given the conflict type or any other definition-level label — only the
memory text and the query.[^c1]

Compared against direct oracle responses on [[tangle-benchmark|TANGLE]] for
three backbones, "Sonnet 5 improves in both action [[calibration]] and
decision-relevant coverage while preserving faithfulness, with the largest
gains on BOC and SCC... GPT-4o improves in action calibration,
clarification, and faithfulness under CAAP, although BOC remains its
weakest conflict type," while Gemini 3.1 Pro's action calibration improves
but its coverage drops, leaving little net change.[^c2]

Without being told the conflict type, CAAP's own action mix tracks it
anyway: "it tends toward reversible trials for BOC, conditionalization or
clarification for CPC, and verification or source-sensitive caution for
SCC."[^c3]

## Known as

| Field | Name there | Relation |
|---|---|---|
| agent-memory (Yang et al. 2026) | CAAP | exact — the acronym |
| agent-memory (Yang et al. 2026) | Conflict-Aware Action Policy | exact — the expansion |

## Why it matters

CAAP is this stall's example of an action *set* that puts asking beside
committing, verifying and deferring as one of several calibrated responses
to unresolved information, rather than treating "ask or answer" as the only
choice: the six-way action space gives a concrete alternative to policies
that either always resolve a conflict to one value or always ask. The
paper is explicit that this is a floor, not a ceiling: "CAAP is therefore a
positive action-policy baseline rather than an upper bound: it moves beyond
a single fixed response template, while temporal-pattern reconstruction and
detailed source reconciliation remain open challenges."[^c4]

## Limits

- Evaluated on three response backbones only (Claude Sonnet 5, Gemini 3.1
  Pro, GPT-4o), against oracle-track TANGLE instances, not the pipeline
  track — so nothing here shows CAAP compensating for the extraction loss
  [[tangle-benchmark]] documents.
- The decision module is prompted, not trained: "choose the least cautious
  action that is still justified" is an instruction to the same LLM being
  evaluated, so CAAP's gains could reflect prompting the model to reason
  about its own uncertainty rather than a separately validated policy.
- Benefit is uneven across backbones (Gemini's net change is small) and the
  paper reports it as a mechanism-level audit, not the primary claimed
  result of the work.
- One paper; the CAAP comparison has no independent replication.

## Related

[[tangle-benchmark]] · [[memory-clarification-boundary]] · [[clarification-request]] · [[value-of-information]]

[^c1]: yang-2026-when
[^c2]: yang-2026-when — "Sonnet 5 improves in both action calibration and decision-relevant coverage while preserving faithfulness, with the largest gains on BOC and SCC."
[^c3]: yang-2026-when — "it tends toward reversible trials for BOC, conditionalization or clarification for CPC, and verification or source-sensitive caution for SCC"
[^c4]: yang-2026-when — "CAAP is therefore a positive action-policy baseline rather than an upper bound: it moves beyond a single fixed response template, while temporal-pattern reconstruction and detailed source reconciliation remain open challenges."
