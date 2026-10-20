---
description: "A small drafter answers each retrieved document separately and a larger verifier picks the draft by a reliability score; the paper reports about 2x lower latency at near-equal accuracy."
aliases: ["speculative RAG", "speculative decoding for retrieval-augmented generation", "draft-and-verify over retrieved documents"]
sources: ["arxiv-2601-01513"]
---
# Per-document speculative drafting

Standard retrieval-augmented generation concatenates the retrieved documents with the question and the input, and one model reads all of it at once. The paper's alternative keeps the documents apart: "we do not concatenate all documents into a single input."[^c1] Each document is paired with the question and the video, and "these inputs are processed in parallel by a lightweight draft VLM," giving one candidate answer per document.[^c2]

The candidates are then judged by a larger verifier. For each candidate, the verifier is asked whether its reasoning supports the answer, and the reliability score is the normalized probability of "Yes" against "No" from a single forward pass.[^c3] Candidates within a tolerance δ of the best reliability score are kept. Among those, the one whose entity best matches the frames is selected.[^c4] The paper sets δ = 0.05 and says it "yields the best empirical performance in our experiments."[^c4]

The method is imported from speculative decoding, which the paper describes as "generating multiple candidate outputs in parallel using a lightweight draft model and then verifying or refining these candidates with a more accurate heavyweight model."[^c5]

What survives the transfer is the split into cheap parallel drafting and more expensive checking, and the latency gain that comes from running the drafts in parallel. What does not survive is the guarantee. In token-level speculative decoding the verifier accepts or rejects tokens, so the output distribution matches the large model's. Here the unit is a whole answer, chosen by a score, and no such equivalence holds: the output can be any draft the score prefers. This is my inference from the algorithm; the paper does not discuss the difference.

## What was measured

On VideoSimpleQA, with Qwen2.5-VL-3B drafting and 32B verifying, accuracy was 91.12%, against 91.30% for standard RAG with the 32B model. On Encyclopedic VQA it was 47.64% against 46.75%.[^c6] Latency on VideoSimpleQA fell from 47.72 s to 25.74 s, and on Encyclopedic VQA from 40.42 s to 16.61 s. The paper gives these as reductions of 46.06% and 58.90%.[^c7] The abstract summarizes the result as "accelerating inference by approximately 2×."[^c8]

The paper attributes the speed gain to two factors: the lightweight drafter processes inputs efficiently, and splitting the documents "mitigates the effect of input context expansion."[^c9] It does not separate the two.

## Limits

- The speedup confounds two changes at once: the drafter is a 3B model, and the documents are no longer concatenated. The comparison does not isolate the effect of speculation itself. My inference: the latency numbers are the most direct evidence, and the accuracy parity is measured on fewer cases.
- Parity is shown on two knowledge-intensive QA sets with Wikipedia-derived questions, and the VideoSimpleQA set is a curated subset.[^c10]
- The tolerance δ and the verifier size (3B+7B or 3B+32B) were chosen on the same experiments, and the paper reports no held-out split.[^c4]
- The reported cost is latency. Total compute, which includes one verifier pass per candidate and a CLIP pass per candidate, is not reported.
- The approach assumes that some retrieved document supports a correct draft. My inference: if every retrieved document is misleading, the scoring can only pick the least misleading draft. The paper does not test that case.

## Related

- [[entity-attribute-transfer-from-retrieved-text]] — the failure the entity check is built to catch: a draft that is fluent and reliable in its reasoning but about the wrong entity.
- [[redundancy-over-diversity-in-evidence-aggregation]] — how grouped evidence sways an answer; per-document drafting removes the grouping by design.
- [[retrieval-order-sensitivity]] — when retrieved content is concatenated, its order changes the answer; separate inputs remove that dependence.
- [[uncertainty-guided-retrieval-triggering]] — also drafts before deciding on retrieval; there the draft gates whether to retrieve, here the drafts are the answer candidates.

[^c1]: arxiv-2601-01513 — "we do not concatenate all documents into a single input"
[^c2]: arxiv-2601-01513 — "these inputs are processed in parallel by"
[^c3]: arxiv-2601-01513 — "A single forward pass computes the"
[^c4]: arxiv-2601-01513 — "yields the best empirical performance in our experiments"
[^c5]: arxiv-2601-01513 — "generating multiple candidate outputs in parallel using a lightweight draft"
[^c6]: arxiv-2601-01513 — "attains 91.12% accuracy on"
[^c7]: arxiv-2601-01513 — "achieving 25.74s and"
[^c8]: arxiv-2601-01513 — "accelerating inference by approximately 2×"
[^c9]: arxiv-2601-01513 — "splitting the retrieved documents mitigates the effect of"
[^c10]: arxiv-2601-01513
