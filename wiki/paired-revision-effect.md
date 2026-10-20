---
description: "A revision's effect on one draft is the paired change in correctness, repair minus harm, visible only when draft and revision are graded together; draft confidence does not reveal it."
aliases: ["conditional recoverability", "repair-minus-harm", "revision effect"]
sources: ["doi-10-48550-arxiv-2609-30087"]
---
# Paired revision effect

A draft answer and its candidate revision can be graded on the same question with the same correctness judge. Each example then falls into one of four cells: the draft and the revision are both correct (preserved), both wrong (unrecovered), the draft is wrong and the revision right (repair), or the draft is right and the revision wrong (harm). Writing z_d and z_I for the two binary labels, the per-example outcome is r = z_I − z_d, which takes the values −1, 0 or +1. Its expectation given the information x available before revision is the conditional effect, and "conditional recoverability is repair probability minus harm probability."[^c1] The paper's figure lays this out as a two-by-two table in which the diagonal cells are ties, so only the off-diagonal cells separate returning from revising.[^c2]

The quantity is defined only for a stated revision setup: a retriever, a retrieval query, an evidence prompt and a refiner. Changing any of these changes the cell counts. Under the paper's three setups, revision repairs between about 9 and 13 percent of drafts and corrupts about 3 percent. "With DPR it repairs 9.32% of drafts and corrupts 3.05%."[^c3] "The other setups repair up to 13.42%"[^c4] and harm a similar share, so the net effect is positive in every setup while harm never falls to zero. Most of the remaining mass is ties, because the refiner often leaves the draft as it is; the paper notes that "the refiner often returns the draft unchanged."[^c5]

## Why the paired form

An aggregate gain cannot tell two revision setups apart. The paper's example: one setup repairs 3% and corrupts none, another repairs 13% and corrupts 10%, and both raise mean accuracy by three points. The aggregate "compares two means and cannot tell the two setups" apart.[^c6] The per-draft transition is the object that matters for a return-or-revise choice, and it is not visible in either accuracy or draft confidence.

Draft confidence is the wrong target for this. "Draft confidence instead estimates Pr(zd = 1 | x). That identifies" the row of the table an example falls in, not the column that says whether revision will repair or harm the draft; the column "requires the paired outcome."[^c7] The paper compares this with cascade deferral, where the same distinction is drawn and "confidence is often close to sufficient" for the deferral decision. My reading, not the paper's claim: the decision logic carries over from cascades, but a cascade's second model answers independently, so it has no harm column in the sense used here. The transfer keeps the logic and drops the paired structure.

The oracle that sees both labels takes the right action whenever either succeeds. When always revising is the better fixed action, which the paper finds in every setup it evaluates, the gap between that fixed action and the oracle is exactly the harm rate: "remaining oracle gap is exactly the harm rate."[^c8] Harm therefore sets the headroom for any policy that chooses between the two answers.

## Limits

- The label depends on the choice of refiner, evidence and judge: "but the label still depends on the chosen refiner,"[^c9] the paper's own wording. Under rescoring with a second judge, "harm is the least stable of the paired outcomes."[^c10]
- The paired label is measured offline, where both answers are generated for every example. A deployed policy never sees the revision; it must predict the effect from pre-revision inputs and "act before revision decoding."[^c11]
- Scope is short-form open-domain QA with one Wikipedia collection; "the models are open and no larger than" GPT-OSS-20B.[^c13] The paper says it does not test "multi-hop, domain-specific, or high-stakes settings."[^c12]
- The word "recoverability" is used in this paper for the paired effect. The wiki's [[recoverability-gated-ask-abstain]] uses the same word for whether missing information could be supplied by a clarifying question. The two share a word, not a definition, and should not be merged.

## Related

- [[return-or-revise-decision]] — the decision this effect is meant to inform; a policy thresholds a predicted paired effect.
- [[counterfactual-search-routing-oracle]] — the same paired-label shape applied to search-or-not: both traces are graded and the label follows which one succeeds. Its oracle is model-specific, and it excludes the both-fail cases, where this paper keeps the both-wrong cell as a tie.
- [[internal-prober]] — predicts whether retrieval will help before an answer is generated. It is a neighbouring predictor of an evidence-conditioned effect, but its target is retrieval, not a revision of a draft.
- [[self-repair-anchoring]] — my inference, not tested here: conditioning a retry on the model's own prior output anchors it on that output, which is one candidate account of why a refiner so often returns the draft unchanged. The paper does not test that mechanism.

[^c1]: doi-10-48550-arxiv-2609-30087 — "Equivalently, conditional recoverability is repair probability minus harm probability."
[^c2]: doi-10-48550-arxiv-2609-30087 — "The diagonal cells are ties."
[^c3]: doi-10-48550-arxiv-2609-30087 — "With DPR it repairs 9.32% of drafts and corrupts 3.05%."
[^c4]: doi-10-48550-arxiv-2609-30087 — "The other setups repair up to 13.42%"
[^c5]: doi-10-48550-arxiv-2609-30087 — "the refiner often returns the draft unchanged."
[^c6]: doi-10-48550-arxiv-2609-30087 — "compares two means and cannot tell the two setups"
[^c7]: doi-10-48550-arxiv-2609-30087 — "Draft confidence instead estimates Pr(zd = 1 | x). That identifies"
[^c8]: doi-10-48550-arxiv-2609-30087 — "remaining oracle gap is exactly the harm rate."
[^c9]: doi-10-48550-arxiv-2609-30087 — "but the label still depends on the chosen refiner,"
[^c10]: doi-10-48550-arxiv-2609-30087 — "harm is the least stable of the paired outcomes."
[^c11]: doi-10-48550-arxiv-2609-30087 — "act before revision decoding."
[^c12]: doi-10-48550-arxiv-2609-30087 — "multi-hop, domain-specific, or high-stakes settings."
[^c13]: doi-10-48550-arxiv-2609-30087 — "the models are open and no larger than"
