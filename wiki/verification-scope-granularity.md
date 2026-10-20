---
description: "Checking a proof in narrow chunks finds errors that one whole-proof read misses, and a coarse-to-fine schedule that drops flawed proofs early buys that detection at a lower token cost."
aliases: ["chunked verification", "segment-wise proof checking", "vertical pessimistic verification", "progressive proof decomposition", "verification span size"]
sources: ["arxiv-2511-21522"]
---
# Verification scope granularity

A verifier that reads a whole proof in one pass spreads its attention over every line at once. The size of the span that one check covers is a separate variable from the verifier's model and its prompt, and the work on pessimistic verification treats it as one. Its vertical variant splits the proof "into chunks with at most k lines," gives each chunk its own review, and keeps the full proof in view: "provided for context."[^v1]

The measured effect runs in one direction. Even with a single read of the proof, finer segmentation improved error detection: the authors "witnessed improved performance in error detection over single-pass whole proof verification."[^v2] They also report "a positive scaling trend of vertical pessimistic verification as its segmentation becomes increasingly refined."[^v3] The stated intuition is that "verification requires a careful examination of details rather than repeated" rough reading.[^v4] A narrow span may force the verifier to attend to the step in front of it, where a whole-proof pass tends to skim; that mechanism is my inference, not something the paper measures.

Fine spans cost tokens. The authors put it directly: "applying it uniformly incurs a high cost for detecting easily discoverable errors."[^v5] Their progressive variant answers this with a schedule. It first checks the whole proof, then halves it: "the proof is subdivided in half and each part is evaluated separately in the" next pass.[^v6] Proofs in which an error has already been found are dropped: "which errors have been detected are filtered out, and verification continues on the remaining proofs."[^v7] The coarse pass "quickly filter[s] out obvious errors," and the fine passes are spent only on proofs that survived.[^v8] The paper attributes the inefficiency of the vertical method to "token wastage."[^v9] Pruning is the progressive variant's answer to it: the method "naturally supports pruning operations, thereby further improving its execution efficiency."[^v14]

So granularity is a dial with two sides (my reading of the trade-off the paper describes). Finer spans find subtler faults and cost more per proof; coarse spans are cheap and miss what is small. A schedule that moves from coarse to fine, and stops early on a flaw, takes the cheap detections first and pays the fine cost only where the proof has not already failed. The paper's summary of its design is "segment-wise partitioning and meticulous proof scrutiny," set against "repeated, superficial reviews."[^v10]

## Limits

- The chunks are cut by line count, not by logical step. A lemma stated in one chunk and used in another cannot be checked inside either chunk alone. The paper supplies the whole proof as context, but does not test whether step-aligned cuts do better than fixed-size ones.
- The granularity parameter is hard to set. The authors write that "hyperparameter selection remains a challenge."[^v11] The progressive variant still needs a stopping depth and a split rule, and their effect is not isolated in the parts I read.
- The effect depends on the dataset. The paper says the vertical method's performance "appears to be more influenced by the specific dataset."[^v12]
- The paper says the progressive decomposition "will also become imperative when dealing with lengthy, intricate proofs."[^v13] That is a forward claim. The experiments use contest and undergraduate-level proofs, and in the parts I read no test is run on long research-level proofs. (my inference)
- Scope and aggregation are both varied in the paper (see [[pessimistic-min-judge-aggregation]]), and the slices I read do not separate their contributions cleanly.

## Related

- [[pessimistic-min-judge-aggregation]] — the rule that rejects on any flag; the progressive variant uses it across its checks, while granularity is a separate axis
- [[coarse-to-fine-evidence-zoom]] — the same coarse-then-fine shape, applied to locating evidence in an image rather than to finding errors in a proof
- [[earliest-error-truncation-correction]] — also localizes the first fault and cuts there, but to regenerate a reasoning tail, not to prune candidate proofs
- [[function-level-step-decomposition]] — chunk or step boundaries induced by the prompt rather than found in the content; the same question of where a unit ends arises here

[^v1]: arxiv-2511-21522 — "Vertical pessimistic verification adopts a hyperparameter k, it first splits the whole proof into chunks with"
[^v2]: arxiv-2511-21522 — "in error detection over single-pass whole proof verification"
[^v3]: arxiv-2511-21522 — "of vertical pessimistic verification as its segmentation becomes increasingly refined."
[^v4]: arxiv-2511-21522 — "requires a careful examination of details rather than repeated"
[^v5]: arxiv-2511-21522 — "it uniformly incurs a high cost for detecting easily discoverable errors."
[^v6]: arxiv-2511-21522 — "the proof is subdivided in half and each part is evaluated separately in the"
[^v7]: arxiv-2511-21522 — "which errors have been detected are filtered out, and verification continues on the remaining proofs."
[^v8]: arxiv-2511-21522 — "This allows it to quickly filter out obvious errors"
[^v9]: arxiv-2511-21522 — "Its inefficiency stems largely from token wastage"
[^v10]: arxiv-2511-21522 — "The second is the strategy of segment-wise partitioning and meticulous proof scrutiny."
[^v11]: arxiv-2511-21522 — "However, hyperparameter selection remains a challenge."
[^v12]: arxiv-2511-21522 — "be more influenced by the specific dataset, but when the"
[^v13]: arxiv-2511-21522 — "when dealing with lengthy, intricate proofs, which is commonly seen in research-level problems."
[^v14]: arxiv-2511-21522 — "naturally supports pruning operations, thereby further improving its execution efficiency."
