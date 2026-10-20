---
description: "A policy that predicts the paired revision effect before decoding beats always revising by about a point and, with dense retrieval, a draft-correctness scorer; it still applies many harms."
aliases: ["return-or-revise", "draft-or-revise decision", "revise-or-return policy"]
sources: ["doi-10-48550-arxiv-2609-30087"]
---
# Return-or-revise decision

A system that has produced a draft answer and retrieved evidence, but has not yet decoded a revision, faces a choice: return the draft, or invoke the revision. The paper treats this as a policy. "At decision time, the policy sees only" the pre-revision inputs and then either returns the observed draft or invokes the revision setup.[^d1] A model paired with a threshold "is a policy: it selects an action but does not generate the revision."[^d2] The rule is a threshold on a predicted score: the policy "revises when its predicted recoverability exceeds a threshold chosen on development data."[^d3] Here "recoverability" is the paired effect of [[paired-revision-effect]], so the policy's score is a prediction of repair minus harm, not of whether the draft is right.

## What the policy is trained on

The paper trains two matched LoRA models that read the same complete prompt, with the same backbone, optimizer and seeds. One predicts draft correctness; the other predicts the paired outcome. The paired-outcome model's accuracy-versus-revision-rate curve has the greater area in every fit: "The paired-outcome target has greater area under the" curve at nearly every revision rate.[^d4] At each policy's own development-selected threshold, the paired policy exceeds the draft-correctness policy "by 0.68 points on average" for DPR, and by smaller margins for BM25 and MonoT5 reranking.[^d5] Only the DPR difference is significant across training seeds; the MonoT5 difference is positive at every seed but "narrowly misses the threshold (p=0.058)."[^d6]

Draft confidence already captures most of the gain over always revising. Of the 1.10 to 1.33 points that always revising gains over returning, "draft correctness alone recovers 0.58–1.11 points," and the paired target adds the rest.[^d7] So the paired target refines a decision that confidence can already make in part, rather than replacing it.

The full-prompt policy, the strongest input in the paper's diagnostic, improves on always revising by 1.10 to 1.33 points. It "closes 35.9–41.4% of the oracle gap while" revising 35.5 to 59.5 percent of examples.[^d8] It revises 94 to 96 percent of repairs, but also 38 to 46 percent of harms: "96.0% of the repairs but also 38.0–46.4% of the"[^d20] harms, so "harms, so harmful revision is the main remaining" error.[^d9] The policy is accurate on average while still corrupting correct drafts at a substantial rate.

## The alternatives change the value

The value of revision depends on what else can be returned. The paper adds a draft-free standard-RAG answer as a third option. A policy choosing between the draft and that answer does better than one choosing between the draft and its candidate revision; adding candidate revision as a third option does not significantly raise accuracy.[^d10] The paper states that the value of revision is "tied to the available answers."[^d11] Its general form: "The action set determines the value of revision."[^d12] Adding another answer leaves the paired effect of one revision unchanged; what changes is that effect's value relative to the best alternative.[^d19]

This is the part most easily lost when the decision is framed as "should I revise". My inference, not a result the paper reports: a revision that repairs many drafts can add nothing once a different answer already covers those same repairs.

## Limits

- The paper is an accuracy study on short-form open-domain QA. "This is an accuracy study. The results do not establish deployment readiness."[^d13] It does not test "a refiner that differs from the drafter, larger models,"[^d14] other corpora, or a person revising the draft.
- The three training seeds give thin run-level tests: "and three training runs give the run-level tests little" power.[^d15] The Tian-style regression baseline is "so it is a weak comparison"; the matched draft-correctness model is the real reference.[^d16]
- The paper does not survey calibrated confidence, semantic uncertainty, or other ways of modelling the two outcomes beyond its verbalized baseline.[^d17]
- A non-significant gain from a third action is not evidence of no gain: "a nonsignificant gain is not an equivalence result."[^d18]

## Related

- [[paired-revision-effect]] — the quantity the policy predicts; the decision uses its sign and size against a threshold.
- [[counterfactual-search-routing-oracle]] — a routing policy trained on paired labels for an act-or-not decision (search). It shows the same policy shape, but its oracle is task-success for one model, not a revision of a draft.
- [[internal-prober]] — a probe that predicts, before answering, whether retrieval will help. A neighbouring decision (retrieve or not) with a probe in place of a paired-outcome target.

[^d1]: doi-10-48550-arxiv-2609-30087 — "At decision time, the policy sees only"
[^d2]: doi-10-48550-arxiv-2609-30087 — "is a policy: it selects an action but does not generate the revision"
[^d3]: doi-10-48550-arxiv-2609-30087 — "when its predicted recoverability exceeds a threshold chosen on development data."
[^d4]: doi-10-48550-arxiv-2609-30087 — "The paired-outcome target has greater area under the"
[^d5]: doi-10-48550-arxiv-2609-30087 — "draft-correctness policy by 0.68 points on average"
[^d6]: doi-10-48550-arxiv-2609-30087 — "but narrowly misses the threshold (p=0.058)."
[^d7]: doi-10-48550-arxiv-2609-30087 — "draft correctness alone recovers 0.58–1.11 points"
[^d8]: doi-10-48550-arxiv-2609-30087 — "closes 35.9–41.4% of the oracle gap while"
[^d9]: doi-10-48550-arxiv-2609-30087 — "harms, so harmful revision is the main remaining"
[^d10]: doi-10-48550-arxiv-2609-30087 — "higher mean accuracy than one choosing between"
[^d11]: doi-10-48550-arxiv-2609-30087 — "tied to the available answers. Once standard RAG"
[^d12]: doi-10-48550-arxiv-2609-30087 — "The action set determines the value of revision."
[^d13]: doi-10-48550-arxiv-2609-30087 — "This is an accuracy study. The results do not establish deployment readiness."
[^d14]: doi-10-48550-arxiv-2609-30087 — "refiner that differs from the drafter, larger models,"
[^d15]: doi-10-48550-arxiv-2609-30087 — "and three training runs give the run-level tests little"
[^d16]: doi-10-48550-arxiv-2609-30087 — "so it is a weak comparison"
[^d17]: doi-10-48550-arxiv-2609-30087 — "not survey calibrated confidence, semantic uncertainty, or other ways of modeling the two outcomes"
[^d18]: doi-10-48550-arxiv-2609-30087 — "a nonsignificant gain is not an equivalence result."
[^d19]: doi-10-48550-arxiv-2609-30087 — "Adding another answer leaves that paired difference unchanged"
[^d20]: doi-10-48550-arxiv-2609-30087 — "96.0% of the repairs but also 38.0–46.4% of the"
