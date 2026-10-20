---
description: "A controller that carries evidence-so-far and gap-still-missing as a state, updated each step, aims its next query at the gap and stops once none remains; the state, not a ranked list, does the work."
aliases: ["evidence-gap tracker", "evidence–gap state", "global evidence-gap state", "gap-state controller", "explicit gap specification"]
sources: ["arxiv-2512-20237", "arxiv-2512-10787", "arxiv-2511-18303"]
---
# Evidence-gap state

A retrieval controller can carry two named variables across its steps: the evidence E, what has so far been established as relevant to the question, and the gap G, what is still missing between the question and that evidence. MemR3 is built around this pair. Its stated principle is to "maintain and update two state variables: the evidence E and the gap G."[^c1] At each iteration the evidence and gap are rewritten from the previous pair and the newest material: "the evidence Ek and gaps Gk are updated according to the retrieved snippets" from a retrieve step, or the reasoning from a reflect step.[^c2]

The gap does two jobs. While it is non-empty it is the target of the next move: the agent "can proactively issue a refined retrieval query to close the remaining gap."[^c3] When it is empty the controller moves on: the paper says the controller can "stop early once the information gap is resolved."[^c4] A router chooses among retrieve, reflect and answer on each pass, so the gap decides both what to fetch and when to stop.

The paper gives the tracker three properties under an idealized requirement space. It is monotone, in that "evidence never decreases and gaps never increase."[^c5] It is sound, since every supported requirement eventually enters the evidence. It is complete: if every requirement is supported by some memory, "the ideal gap eventually becomes empty."[^c6] The requirement space and the proofs are in the paper's appendix; the properties are stated for that idealized object.

What the state contributes is reported only through ablations on LoCoMo with a RAG retriever. Removing the reflect node takes the overall score from 81.55% to 76.65%.[^c7] Removing the refinement query, which the gap feeds, hurts "multi-hop and single-hop scores decline significantly."[^c8] Removing the masking of already-retrieved snippets costs the most. The paper's reading is that repeated memories "fails to effectively close the remaining gaps."[^c9] So the gap's value shows up as better next queries and fewer wasted fetches, not as a separate score.

The state also has a failure shape. The paper says "some challenging questions are inherently underspecified given the stored memories," so the gap never empties and the loop runs to its budget.[^c10] It reads the extra tokens in that case as "available memory, rather than a failure of the agent."[^c11] In the router the iteration budget overrides the gap: a "maximum iteration budget nmax that forces an answer action once the budget" is spent.[^c12]

A second derivation of the same gap appears in [[fixed-capacity-evidence-replacement]], which builds it without a reflect step. Each loop the gap is computed from the question: "The system parses the question" into information needs, and the facts the entity ledger already supports are removed from them, leaving the gap.[^c17] The paper types what is left: a missing entity that a relation refers to, two known entities whose link is unproven, or a known relation missing a date or place.[^c18] Each gap is then rendered as an atomic micro-query, "The controller translates Gt into atomic micro-queries".[^c20] The authors argue this is more precise than a broad rewrite, which "often retrieves general biography pages rather than the specific missing attribute."[^c19] My reading of the formula is that the gap is recomputed from the ledger each loop rather than kept as a variable of its own. The paper does not compare the two designs in the text I read.

## Limits

- The proofs are about the idealized tracker. The running tracker is a language-model output, and the paper's own wording is that "the practical tracker mirrors this by continuing to search for the missing specificity."[^c13] The text I read does not check the written gap against the memories. My inference: a gap that is wrongly closed, or wrongly kept open, is not caught by anything inside the loop.
- The scope is narrow by the paper's own statement: "we explicitly limit our scope to long-term conversational memory."[^c14] The only benchmark reported is LoCoMo, scored by LLM-as-a-judge: "Empirical results on the LoCoMo benchmark demonstrate that MemR3 surpasses strong baselines on LLM-as-a-Judge score."[^c15] No human check of gap quality is reported in the part I read.
- The ablations in the paragraph I read remove masking, the refinement query and reflect. None removes the tracker as its own condition. My reading is that the state's separate effect is therefore not isolated here; it is bundled with the loop it drives.
- The stop is a state test plus a hard budget, and the reported results do not separate the two. A run that ends on budget and a run that ends on an empty gap are both counted as answers.

## Related

- [[evidence-gap-agent]] — the same name in a diagnostic dialogue, where a separate agent hands a ranked list of missing facts to a question agent each turn. There the gap is a per-turn list, not a cumulative state that gates stopping. Whether the two are one concept is my judgment, not the papers'.
- [[stop-continue-criteria-in-retrieval-loops]] — the gap-empty test is a state-dependent stop, the family that survey finds least common.
- [[retrieval-reasoning-procedure]] — the router's choice among retrieve, reflect and answer is the interleaved plan and the stop, on two of that frame's axes.
- [[chain-of-thought-interleaved-retrieval]] — an interleaved retrieve-reason loop; the paper's added element is the explicit state, which it describes as keeping "verified memories from remaining uncertainties" apart.[^c16]
- [[fixed-capacity-evidence-replacement]] — the same gap drives swaps inside a fixed-size evidence set, not appends to a growing one.
- [[gap-spawned-research-branches]] — the gap as a tree rather than a state: a deep-research controller turns each report's gaps into child research nodes under depth and branch budgets, and stops by prune rule, not by an empty gap.[^c21]

[^c1]: arxiv-2512-20237 — "and update two state variables: the evidence E and the gap G."
[^c2]: arxiv-2512-20237 — "the evidence Ek and gaps Gk are updated according to the retrieved snippets"
[^c3]: arxiv-2512-20237 — "issue a refined retrieval query to close the remaining gap"
[^c4]: arxiv-2512-20237 — "stop early once the information gap is resolved."
[^c5]: arxiv-2512-20237 — "evidence never decreases and gaps never increase"
[^c6]: arxiv-2512-20237 — "the ideal gap eventually becomes empty"
[^c7]: arxiv-2512-20237 — "reduces performance (from 81.55% to 76.65%)"
[^c8]: arxiv-2512-20237 — "multi-hop and single-hop scores decline significantly"
[^c9]: arxiv-2512-20237 — "fails to effectively close the remaining gaps"
[^c10]: arxiv-2512-20237 — "some challenging questions are inherently underspecified given the stored memories"
[^c11]: arxiv-2512-20237 — "available memory, rather than a failure of the agent."
[^c12]: arxiv-2512-20237 — "a maximum iteration budget nmax that forces an answer action once the budget"
[^c13]: arxiv-2512-20237 — "the practical tracker mirrors this by continuing to search for the missing specificity"
[^c14]: arxiv-2512-20237 — "we explicitly limit our scope to long-term conversational memory."
[^c15]: arxiv-2512-20237 — "Empirical results on the LoCoMo benchmark demonstrate that MemR3 surpasses strong baselines on LLM-as-a-Judge score"
[^c16]: arxiv-2512-20237 — "verified memories from remaining uncertainties"
[^c17]: arxiv-2512-10787 — "The system parses the question"
[^c18]: arxiv-2512-10787 — "Missing Entity: A bridge entity referenced by a relation is absent"
[^c19]: arxiv-2512-10787 — "often retrieves general biography pages rather than the specific missing attribute."
[^c20]: arxiv-2512-10787 — "The controller translates Gt into atomic micro-queries"
[^c21]: arxiv-2511-18303 — "explorer to materializes new RNs from this RN targeted to those gaps (depth+1) and updates remaining"
