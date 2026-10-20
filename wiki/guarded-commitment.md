---
description: "Debate repairs join the shared state only if they keep the question's relation and quote verbatim from context; strict gating beats admit-everything by 6.56 to 7.56 points on gated questions."
aliases: ["guarded resolution", "commit guard", "guarded state extension"]
sources: ["doi-10-48550-arxiv-2608-01463"]
---
# Guarded commitment

In a debate that repairs one disputed step at a time, the repair is not simply appended to the shared state. The protocol first produces the repair. A zero-temperature resolver turns the final positions into a proposed repair, giving one or more replacement nodes together with a supporting quotation for each.[^c1] A commit guard then decides whether the proposal may enter the state. The paper's guard admits it only if the question's subject and relation are preserved and every quotation in the proposal appears verbatim in the provided context.[^c2] The verbatim check needs a supplied context to quote from, which the paper's formulation provides as an optional evidence context x.[^c3]

When the guard admits the repair, the node is appended to the committed state and the agents start the next iteration from that extended state. Nodes already committed are not revisited: the abstract's phrase is that later conflicts are handled "without reopening accepted" steps.[^c4] When a repair fails the guard, the controller does not retry the state; it "falls back to a majority vote, also used when the iteration budget is exhausted."[^c5] So the guard is a gate on writing, and the vote is the exit when writing is refused.

The reason for the guard is that a debate can produce a plausible-looking claim that changes the subject of the question or cites nothing. The paper's ablation tests whether the strict check is needed. It builds a gate-activated subset: questions on which the strict policy rejected at least one candidate repair. On that subset it compares three policies. STRICT, the default, "requires the proposed repair to preserve the relevant relation and be supported by" the evidence.[^c6] CONCRETE "only requires" that "the resolver output to form an explicit claim," with no relation or support check.[^c7] ALWAYS commits every proposal that reaches the gate. STRICT reaches a macro-average of 55.98%,[^c8] against 49.42 for CONCRETE and 48.42 for ALWAYS in the same table, which the paper summarizes as STRICT outperforming them by 6.56 and 7.56 percentage points, respectively.[^c9]

What transfers, in my inference: a shared record that only grows and that a checker can gate is a way to keep agreed-upon steps from being silently rewritten by later rounds. The record's value depends on the checks it can run. A relation check and a verbatim-quotation check are cheap, mechanical tests; a check that needed a judgement would be a different and weaker gate.

## Limits

- The ablation runs only on questions where the strict gate fired. It does not show what the gate does on questions it passed, so it measures the cost of refusing repairs on a hard subset, not the gate's effect across the benchmark (my reading).
- The sections I read do not say how the relation-preservation check itself is carried out (by a model, by rule, or by a judge). Only the verbatim check is described as a string test, so the strength of the relation check is not established there (my reading).
- The guard can refuse a correct repair. A refused repair leaves the state where it was and hands the question to a majority vote, which can keep a wrong majority; the paper's fallback is stated as a vote, and I did not find a measurement of how often the fallback is the wrong answer (my inference).
- Commitment is one-way. A claim that passes the guard but is wrong cannot be retracted by a later round, because accepted nodes are not reopened. The paper does not test this failure in the sections I read (my inference).
- The gate was tested with the open-weight backbones and multi-hop QA benchmarks listed in the paper; its behaviour on tasks whose context is not a quotable passage is not tested here.

## Related

- [[earliest-conflict-localization]] — the step that produces the disputed node this guard decides on
- [[disagreement-retention-in-debate]] — another debate-side filter, which chooses messages rather than gating what enters a shared state
- [[prefix-localized-rubric-credit]] — also writes a credit only up to the sentence that supports it, a restriction of the same kind applied to training signal

[^c1]: doi-10-48550-arxiv-2608-01463 — "A zero-temperature resolver"
[^c2]: doi-10-48550-arxiv-2608-01463 — "appears verbatim in the provided context."
[^c3]: doi-10-48550-arxiv-2608-01463 — "x its optional evidence context"
[^c4]: doi-10-48550-arxiv-2608-01463 — "can be addressed without reopening accepted"
[^c5]: doi-10-48550-arxiv-2608-01463 — "falls back to a majority vote, also used when the iteration budget is exhausted."
[^c6]: doi-10-48550-arxiv-2608-01463 — "preserve the relevant relation and be supported by"
[^c7]: doi-10-48550-arxiv-2608-01463 — "the resolver output to form an explicit claim"
[^c8]: doi-10-48550-arxiv-2608-01463 — "achieves a macro-average accuracy of"
[^c9]: doi-10-48550-arxiv-2608-01463 — "and 7.56 percentage points, respectively"
