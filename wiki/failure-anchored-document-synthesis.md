---
description: "New second-stage questions come from documents retrieved by similarity to the model's failed questions, then kept if answer-consistent: failures pick the neighborhood, not the answer."
aliases: ["knowledge-driven data engine", "failure-conditioned retrieval synthesis", "retrieval-kernel question synthesis", "failure-to-document synthesis"]
sources: ["arxiv-2601-01562"]
---
# Failure-anchored document synthesis

Resampling existing questions cannot add a missing piece of knowledge, so
the failure pass has a second half. The model's failed questions are used as
queries against an external corpus of documents, and new question-answer
pairs are written from the documents that come back. The failure does not
supply the answer; it supplies the neighborhood to look in.

The retrieval is written as a kernel over documents. With an embedding φ and
cosine similarity s(x, d), the authors define a sampling distribution
K_τ(d | x) ∝ exp(s(x, d)/τ) and truncate it to the top-k documents for
sparsity.[^g1] The point of the formalization is stated plainly: a failure
case "activates" related documents, "thereby transferring sampling mass from
failure regions to their neighborhoods in" the knowledge space.[^g2]

Synthesis is a second kernel. A strong LLM (DeepSeek R1 is named) writes a
new question-response pair from each retrieved document, and an acceptance
filter keeps only the pairs that pass a check, given as "answer-consistency
verification."[^g3] The filtered synthetic distribution is then mixed with
the original first-stage data at a fixed proportion λ, and the second stage
trains on the mixture. The stated purpose of the synthetic pairs is to
"compensate for the density ratio in eq. (2)." In my reading, that means
adding samples where the target weights a region more than the original data
does, which is the gap resampling alone cannot close.[^g4]

The corpus is an internal multi-source collection, "encompassing academic
papers, technical monographs, authoritative textbooks, and technical
reports."[^g5] Documents are parsed to structured HTML with "a proprietary, high-precision"
tool and then filtered for text quality, usefulness, and subject.[^g9] The second
stage uses data generated this way with no human annotation.[^g8]

The source of the failures changes what transfers. In the source ablation,
the authors built second-stage data from incorrectly answered questions in
two benchmark groups. Data from GPQA errors "not only significantly improves"
GPQA, and it also generalizes to math benchmarks; data from math benchmarks
alone gave limited gains on STEM overall, with the text stating that
"mathematical benchmarks yields limited improvement in overall STEM
capabilities."[^g6] The authors read this as evidence that scientific QA
carries reasoning patterns that transfer more widely.

Scaling the retrieval hurts. Relaxing the relevance threshold to pull in more
documents per failure case reduced performance.[^g7] The authors' hypothesis is
that the extra documents are less related to the original failures. So the
neighborhood has to stay tight, and more documents are not better documents.

## Limits

- The ablations I read were run on Qwen3-8B; the caption of the data-ablation
  table reads "Ablation performance based on Qwen3-8B across key reasoning
  benchmarks." Whether the source and scaling results hold for the 32B model
  or a different family is not shown here.
- The acceptance filter checks answer consistency. That does not establish
  that a synthesized question is well posed, novel, or harder than the one
  that failed. My inference is that a question can be consistently answered
  and still be trivial; the text does not measure this.
- The corpus is internal and parsed with a proprietary tool. The pipeline
  cannot be rebuilt from the text alone, and the relevance threshold and the
  top-k and temperature values are not stated in the sections I read.
- The scaling result is a single observation with a hypothesis attached
  ("We hypothesize that the additional documents are less strongly related to"),
  not a tested account of why more retrieval fails.
- Synthesis is by a strong teacher model. Whatever that model gets wrong, and
  whatever it leaves out of the documents, enters the second stage without a
  separate check beyond the filter.

## Related

- [[failure-driven-query-resampling]] — the reweighting this step extends with
  new questions; it supplies the failure cases used as retrieval queries.
- [[hierarchical-error-cause-memory]] — also routes a solver's failures back
  into question generation, grouped by failure cause rather than retrieved
  from a document corpus.
- [[learnability-posterior-curriculum]] — another way to aim generated
  questions at the solver's boundary, by topic posteriors, without a document
  source.

[^g1]: arxiv-2601-01562 — "we use a top-𝑘 truncated variant looks like"
[^g2]: arxiv-2601-01562 — "thereby transferring sampling mass from failure regions to their neighborhoods in"
[^g3]: arxiv-2601-01562 — "answer-consistency verification"
[^g4]: arxiv-2601-01562 — "compensate for the density ratio in eq. (2)"
[^g5]: arxiv-2601-01562 — "encompassing academic papers, technical monographs, authoritative textbooks, and technical reports"
[^g6]: arxiv-2601-01562 — "mathematical benchmarks yields limited improvement in overall STEM capabilities"
[^g7]: arxiv-2601-01562 — "associated with each failure case. However, as detailed in section B.3.2, this actually degrades the"
[^g8]: arxiv-2601-01562 — "is generated automatically without any human annotation"
[^g9]: arxiv-2601-01562 — "a proprietary, high-precision"
