---
description: "Keeping the top singular directions of a matrix, or of each tensor unfolding, is the best rank-r approximation under Frobenius distortion; the discarded singular energy is the error."
aliases: ["truncated SVD", "spectral hard-thresholding", "Eckart–Young–Mirsky truncation", "truncated HOSVD", "adaptive spectral masking"]
sources: ["arxiv-2601-00938"]
---
# Low-rank spectral truncation

Approximating a matrix by one of lower rank means keeping the largest singular values and their singular vectors and dropping the rest. The paper states the result as "keeping the top singular directions is optimal (matrix case)" under a quadratic distortion, and cites the Eckart–Young–Mirsky theorem for the minimum.[^c1][^c2] The error of that approximation, in Frobenius norm, is the energy in the discarded singular values. That identity is my reading of the paper's per-mode display, which its tensor bound uses.[^c3]

For a tensor the paper works mode by mode. Each unfolding X(n) is projected onto its own top-r_n left singular subspace, and that projector is stated to be optimal for its unfolding.[^c3] The paper's Adaptive Spectral Masking (ASM) sets each mode's rank from a relative threshold: "Given 𝜖 ∈ (0, 1), define" a mask that keeps the singular values at or above ε times the largest.[^c4] The full reconstruction error for a truncated HOSVD is then bounded by the sum over modes of the discarded energies.[^c5] My reading is that this is a bound, not a claim that jointly truncating every mode minimizes the tensor error. The text read does not prove that joint statement.

The rank also sets the query size. The paper takes the budget as a proxy equal to the product of the retained multilinear ranks, on the assumption that the query holds only the masked core and small metadata.[^c6] That counts numbers kept, not bits. The paper says that for r_n much smaller than I_n, "CQD can be orders-of-magnitude smaller than transmitting raw traces."[^c7] That comparison is a rank count against a raw trace, and it is not measured in bits.

## Limits

- The optimality is for a fixed matrix under Frobenius distortion. It says nothing about the task loss the query serves. The paper's learning objective is a loss "reflecting task performance after integrating" the oracle's response, which truncation does not minimize.[^c8] That last step is my reading.
- The tensor case gives mode-wise optimality and an upper bound, as above. No joint optimality is shown in the text read.
- The rank is not fixed across iterations. ASM sets each r_n from ε at each step, yet the update is written on a fixed multilinear-rank manifold: "We perform updates on M𝒓 using a retraction-based step."[^c9] The text read does not say how one rank is kept across iterations. This is a tension in the paper, not a resolved point.
- The benchmark's "query ratio" is not defined in the text read, so the query-size savings are not checked against the budget proxy above.
- The result itself is classical. Theorem 5.2 is Eckart–Young, cited and not proved here. What is the paper's own is the mode-wise restatement and its use as the compressor of a delegated query.

## Related

- [[rate-distortion-theory]] — truncation is the distortion side of a rate constraint; here the rate is a rank count, not the R(D) of a source.
- [[information-bottleneck]] — the same kept-versus-discarded trade, but with no relevance variable: truncation keeps dominant variance whatever the question asks.
- [[query-relative-token-overflow]] — truncation's adequacy is fixed by the spectrum, while the overflow work finds adequacy depends on the question asked.

[^c1]: arxiv-2601-00938 — "keeping the top singular directions is optimal (matrix case)"
[^c2]: arxiv-2601-00938 — "the minimizer is achieved by keeping the top 𝑟 singular values/vectors."
[^c3]: arxiv-2601-00938 — "By Proposition 5.3, 𝑃𝑛 is the optimal rank-𝑟 𝑛 projector, hence"
[^c4]: arxiv-2601-00938 — "Given 𝜖 ∈ (0, 1), define"
[^c5]: arxiv-2601-00938 — "Let X𝒓 be truncated HOSVD reconstruction with ranks"
[^c6]: arxiv-2601-00938 — "a natural budget proxy is"
[^c7]: arxiv-2601-00938 — "CQD can be orders-of-magnitude smaller than transmitting raw traces"
[^c8]: arxiv-2601-00938 — "Let 𝑓 (X; 𝑅) be a differentiable loss reflecting task performance after integrating"
[^c9]: arxiv-2601-00938 — "We perform updates on M𝒓 using a retraction-based step:"
