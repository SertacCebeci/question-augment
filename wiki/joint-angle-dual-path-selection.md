---
description: "Retrieve separately for the query and for an LLM-drafted pseudo-context, then keep documents scoring high on both via cos(θ1+θ2), so a hallucinated draft cannot drag retrieval alone."
aliases: ["DPR-AIS", "dual-path retrieval with adaptive information selection", "query plus pseudo-context retrieval"]
sources: ["arxiv-2601-03908"]
---
# Joint-angle dual-path selection

Sparse queries carry few semantic cues, so retrieval for them is poor. A common fix has the LLM write a pseudo-document or answer and merges it with the query into one retrieval signal. The DTR paper argues that this merge "can amplify noise due to LLM hallucinations", and instead keeps the two signals independent.[^c1]

## Mechanism

Dual-path retrieval (DPR) runs two parallel searches, one on the query embedding and one on the pseudo-context embedding, each returning n documents. The pool is 2n candidates (10 in their setup).[^c2]

Adaptive information selection (AIS) then scores each candidate by how well it matches both. The simple version sums two cosines, s1(d,q)+s2(d,p). The authors say this "may not fully capture the joint relevance, especially if either q or p introduces semantic noise". They instead treat the two similarities as angles and maximise cos(θ1+θ2), which expands to s1·s2 − sqrt(1−s1²)·sqrt(1−s2²).[^c3] My reading: a document close to the query but far from a hallucinated draft, or the reverse, gets a larger combined angle and drops, while one near both rises. The product-like form penalises imbalance more than a sum does. The paper gives geometric intuition for this, not a proof.

The paper's reported evidence is that the combined framework improves EM and F1 over standard RAG and query-augmentation baselines across five QA datasets and several retrievers.[^c4] The pseudo-context is said to compensate for sparse queries.

## Limits

- Evidence for the selection rule is in the full-framework comparisons and ablations I sampled only partly; I did not verify how much of the gain comes from the angle formula versus simply having two paths.
- The angle formula assumes unit-normalised embeddings and similarities in a range where the square roots are defined; behaviour with poorly calibrated retrievers is not discussed.
- Pseudo-context generation adds inference steps, so latency rises over single-pass retrieval, which the authors acknowledge.[^c5]
- When the draft is wrong and the query is sparse, both paths may be uninformative; no case was tested where both fail.
- Only Wikipedia-style open-domain QA and HotpotQA were used.

## Related

- [[query-anchored-expansion-integration]] — also keeps the query as an anchor against expansion drift, by interpolation instead of joint selection
- [[query-expansion-harm-asymmetry]] — when LLM expansions hurt retrieval
- [[uncertainty-guided-retrieval-triggering]] — the gate that decides whether this pipeline runs at all

[^c1]: arxiv-2601-03908 — "an operation that can amplify noise"
[^c2]: arxiv-2601-03908 — "DPR executes two parallel retrieval"
[^c3]: arxiv-2601-03908 — "may not fully capture the joint relevance, especially if either q or p introduces semantic noise"
[^c4]: arxiv-2601-03908 — "consistently improves EM and F1 over"
[^c5]: arxiv-2601-03908 — "generating pseudo-contexts introduces extra inference steps"
