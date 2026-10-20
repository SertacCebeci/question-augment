---
description: "Under a fixed evidence budget k, a controller swaps its lowest-utility passage for a gap-closing candidate instead of appending, so distractors do not crowd out the bridge fact."
aliases: ["replace, don't expand", "fixed-budget evidence assembly", "fixed-k gap repair", "fixed-capacity replacement"]
sources: ["arxiv-2512-10787"]
---
# Fixed-capacity evidence replacement

When a generator can read only k passages, a retrieval controller that misses a fact has two responses. It can append new passages, so the set grows with each correction loop. Or it can hold the set at k and exchange one member for a better one. SEAL-RAG takes the second route and names the first one's failure: "simply expanding the context window often leads to context dilution, where distractors crowd out relevant" evidence.[^c1] The paper's framing is that "Unlike prior methods that treat the context window as an append-only log, SEAL treats the top-k slots as" a scarce resource.[^c2]

The mechanism has three parts. First, when the sufficiency check fails, the system works out what is still missing: "The system parses the question" into information needs and subtracts "the facts already present in Ut", the entity ledger built from the current set.[^c3] Each gap is then turned into a targeted query: "The controller translates Gt into atomic micro-queries".[^c4] Second, each candidate that comes back is scored by an entity-first utility with a gap-coverage term, a corroboration term, a novelty term, and a penalty for lexical overlap with what is already held. The form is "inspired by" Maximal Marginal Relevance, and the paper says it "balances relevance against redundancy".[^c5] Third, the controller finds the lowest-scoring member of the set and the highest-scoring candidate, and swaps them only when the candidate wins by a margin. The margin is a "hysteresis threshold to prevent thrashing", so the set is not churned by marginally better items.[^c6] A dwell-time guard protects a newly inserted item from eviction for one iteration, so it reaches the sufficiency check before it can be discarded.[^c7] The set size stays at k on every loop. The paper uses this to argue the generator runs once on a context of fixed size, since "the generator is invoked only once on a fixed context of size k", and only retrieval and extraction repeat per loop.[^c8]

The reported effect is largest where the set is smallest. At k = 1 the authors attribute the gain to the swap itself: "the controller resolves the bridge entity into the ledger", so the one slot can hold the answer-bearing passage.[^c9] At k = 5 on 2WikiMultiHopQA the paper reports that baselines lost precision while "SEAL maintained 96% Precision".[^c10] These numbers come from the authors' own re-implementations of the baselines in one shared environment, scored by an LLM judge.[^c11]

What carries over to asking and answering is a stance rather than the formula. The unmet needs of the question decide which evidence is kept: a passage that closes no gap loses its slot, and the candidates are fetched by the gap. The contrast is with pruning a fixed pool, which "cannot recover" a bridge fact the first retrieval never returned.[^c12]

## Limits

- The gap has to be nameable. "The controller relies on the ability to explicitly name the missing" information, and for an implicit gap the paper expects the extraction to fail and the system to fall back to standard retrieval.[^c13]
- Fixed capacity trades recall for precision. The authors concede that "policy will cycle through evidence rather than accumulating it," so a question that needs more than k documents at once is not served by this design.[^c14]
- The evaluation is two multi-hop QA sets, HotpotQA and 2WikiMultiHopQA, with an LLM judge; the paper itself notes that "LLM-based evaluation remains subject to stochasticity".[^c15] The large gaps are against baselines the authors re-implemented, not against their published systems.
- The slices of the text I read do not report how the utility weights or the swap margin were set, nor a sensitivity check on them. That is a gap in what I could verify, not a finding that they are arbitrary.
- The paper calls the failure "context dilution." The wiki's [[score-dilution]] names a different mechanism, softmax attention spread over near-tie distractors. The shared word does not make the two one concept.

## Related

- [[evidence-gap-state]] — the gap that directs each swap is the same kind of object: an explicit missing-information state, here recomputed from the question minus the ledger each loop.
- [[set-level-selection-over-relevance]] — the same argument that a set carries properties, such as coverage and non-redundancy, that no single item carries.
- [[symmetric-difference-repair]] — a repair that both adds missing facts and deletes wrong ones; the swap here is that move under a size constraint.
- [[sequential-window-reading]] — the same trade between recall and distractor noise, without a swap step.

[^c1]: arxiv-2512-10787 — "simply expanding the context window often leads to context dilution, where distractors crowd out relevant"
[^c2]: arxiv-2512-10787 — "Unlike prior methods that treat the context window as an append-only log, SEAL treats the top-k slots as"
[^c3]: arxiv-2512-10787 — "The system parses the question"
[^c4]: arxiv-2512-10787 — "The controller translates Gt into atomic micro-queries"
[^c5]: arxiv-2512-10787 — "this score balances relevance against redundancy"
[^c6]: arxiv-2512-10787 — "hysteresis threshold to prevent thrashing"
[^c7]: arxiv-2512-10787 — "Additionally, we enforce a Dwell-Time Guard: newly inserted items are protected from eviction"
[^c8]: arxiv-2512-10787 — "Since the generator is invoked only once on a fixed context of size k"
[^c9]: arxiv-2512-10787 — "the controller resolves the bridge entity into the ledger"
[^c10]: arxiv-2512-10787 — "SEAL maintained 96% Precision"
[^c11]: arxiv-2512-10787 — "faithful re-implementations of Basic RAG, CRAG, Self-RAG, and Adaptive-k in a shared environment"
[^c12]: arxiv-2512-10787 — "initial retrieval pool misses a bridge fact entirely, pruning cannot recover it."
[^c13]: arxiv-2512-10787 — "The controller relies on the ability to explicitly name the missing"
[^c14]: arxiv-2512-10787 — "policy will cycle through evidence rather than accumulating it."
[^c15]: arxiv-2512-10787 — "LLM-based evaluation remains subject to stochasticity"
