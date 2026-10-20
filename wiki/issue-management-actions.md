---
description: "Asking, refining and resolving are explicit updates on a second (issue) relation, dual to announcing; they compose as an algebra, but not freely when questions mention knowledge or issues."
aliases: ["dynamic logic of questions", "DEL-Q", "issue management", "question as update on issue relation"]
sources: ["benthem-2012"]
---
# Issue management actions

In a dynamic-epistemic setting a state carries two equivalence relations over the same worlds: what the agent cannot tell apart (information) and what the current issue does not distinguish (the question on the table). The issue is a partition of the options, its cells being the areas where we would like to be.[^c1] Questions had been missing from dynamic-epistemic logic; the usual treatment keeps only the answers, as public announcements.[^c2]

## The actions

Asking a question phi? changes only the issue relation: it is intersected with the equivalence "agree on phi". A soft (link-cutting) announcement phi! does the same to the information relation, so the two are symmetric: "One refines the issue, the other the information partition".[^c3] The model keeps all its worlds; only links or cells change.

Two further actions generalise these. Resolution intersects the information relation with the issue relation (the agent learns whatever would settle the current issue). Refinement intersects the issue relation with the information relation (the issue is adjusted to what the agent already knows). A simultaneous action does both.[^c4] The symmetry also argues for treating asking as always executable, even in worlds where p is false, whereas a truthfulness precondition would break it.[^c5]

Among resolve, refine and the simultaneous action, composition forms a small algebra: resolve then resolve gives resolve, refine then refine gives refine, and any mix of the two gives the simultaneous action.[^c6] (This is read from the composition table in the paper.)

## What fails to commute

For specific questions and announcements the laws are messier. Many prima facie equations are invalid, for example a question followed by an announcement is not the same as the reverse.[^c7] The failures need non-factual content, meaning formulas about knowledge or issues: for purely factual formulas, order does not matter, because the valuation never changes.[^c8] Repetition behaves likewise: asking the same factual question twice equals asking it once, but a question that refers to the issue relation can change the model on each repetition.[^c9] Finally, two questions in sequence cannot be replaced by one question: "There is no question composition principle."[^c10] Starting from the universal issue, a single question yields a two-cell partition, while two independent questions yield four.[^c11]

## Limits

- This is a logic of idealised agents with equivalence relations; the paper notes that lack of introspection into the issue, or belief, need other models. Nothing here measures how people or models actually ask.
- The effect of a question is only to refine the partition. Coarsening (simplifying an issue) is mentioned as a possible action but not built.
- The completeness result, multi-agent product update and temporal protocols are in the paper; I did not read them closely enough to claim them here.
- Which question to ask is not addressed; the logic describes what asking does, not which asking is good. That reading is mine.
- Claim c6 is my reading of a table whose layout is garbled in the text extract; it has no quote.

## Related

- [[question-as-partition]] — the static semantics this note turns into updates
- [[epistemic-actions]] — information-changing acts in the same spirit
- [[question-under-discussion]] — the issue on the table as a conversational object
- [[twenty-questions]] — a sequence of questions as repeated refinement

[^c1]: benthem-2012 — "the current ‘issue’ is a partition of the set of options"
[^c2]: benthem-2012 — "do not give an explicit account of what questions do"
[^c3]: benthem-2012 — "One refines the issue, the other the information partition:"
[^c4]: benthem-2012 — "simultaneously changes both equivalence relations."
[^c5]: benthem-2012 — "every world in a model, even those not satisfying p"
[^c6]: benthem-2012
[^c7]: benthem-2012 — "The following equations are not valid in DEL"
[^c8]: benthem-2012 — "makes no difference with purely factual assertions or questions, it does when"
[^c9]: benthem-2012 — "The equation ϕ?; ϕ? = ϕ? is invalid in DEL"
[^c10]: benthem-2012 — "There is no question composition principle."
[^c11]: benthem-2012 — "such a sequence will always induce a two,"
