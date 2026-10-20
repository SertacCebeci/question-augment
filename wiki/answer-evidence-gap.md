---
description: "Under KV cache compression, final-answer accuracy can stay high while the visible reasoning stops supporting the answer; accuracy alone cannot detect this."
aliases: ["accuracy-evidence gap", "wrong-chain correct answer", "right answer, unsupported chain"]
sources: ["doi-10-48550-arxiv-2608-01631"]
---
# Answer-evidence gap

A model can keep producing the right final answer while the reasoning it shows no longer supports that answer. The paper names this the answer-evidence gap and treats it as a separate quantity from accuracy: "We call this the" gap.[^c1] Under token-eviction KV compression, methods "can preserve competitive final-answer accuracy while substantially degrading chain support or perturbation faithfulness."[^c2]

The gap is measured on the same outputs by two separate labels. Final correctness is one label. Reasoning status is the other: a chain is "not fully correct" if, for example, "an incorrect setup, applies an invalid formula or" theorem, makes an unsupported transition, or hallucinates the answer without justification.[^c3] A correct answer with a not-fully-correct chain is counted by RWAC, the share of all samples that are correct-looking but unsupported. The paper also reports RWAC over the answer-correct samples alone, since the first figure can be low merely because accuracy is low.[^c4]

The mechanism the paper proposes is that a reasoning trace carries two kinds of content. Some tokens make the answer recoverable, such as answer-like claims and conclusion-adjacent summaries. Others make it auditable, such as "intermediate equations, premise" checks, case splits, and verification steps.[^c5] Compression can keep the first kind and lose the second. Accuracy only tracks the first, so it can stay flat while the second degrades.

The paper is explicit that this distinction is behavioural, not a claim about cache internals: "rather than mechanistic: we do not assume that" the KV states factorize into answer and justification parts.[^c6]

What was measured. On Qwen3-8B the gap appears mostly for token-eviction methods, and accuracy rankings disagree with evidence rankings: on AIME and GPQA-Diamond, "rank highly by final answer tend to rank poorly" on chain validity.[^c7] In a matched-answer subset, where Full-KV and the compressed run both give the same correct answer and the Full-KV chain is correct, eviction methods degrade the chain noticeably, while the quantization control "rarely degrades" it.[^c8] The gap is not uniform across tasks. On GPQA the uncompressed model already "selects the right option without a fully verifiable rationale by guessing", so the gap there partly reflects guessing that compression makes dominant (my reading of the paper's GPQA paragraph).[^c9] On RULER QA the answer depends on exact distant evidence, and accuracy does collapse: "evidence, accuracy itself collapses." In that regime accuracy is an informative diagnostic.[^c10]

## Limits

- The evidence is behavioural. The paper shows that accuracy, chain validity and perturbation faithfulness can separate under compression, but "but we do not provide a causal" account of which cache entries carry answer cues and which carry evidence.[^c11] It states that it does "not claim state-level semantic attribution".[^c12]
- Fixed-trace replay holds the reasoning text constant and changes only the cache. The paper calls itself "diagnostic rather than exhaustive" and notes that in end-to-end generation compression can "change the reasoning trajectory, generation length," as well as capability.[^c13][^c14]
- The chain labels come from an LLM judge. The paper reports agreement with a human auditor on 400 stratified outputs, but says that "exact RWAC values may vary" with judge choice and prompt design.[^c15][^c16]
- The main separation is shown at a tight 256-token budget. The paper says that larger budgets "often made results cluster near Full-KV, making it" harder to see the difference.[^c17]
- The primary model is one 8B reasoning model; other models are validated in an appendix.[^c18] Whether the gap size transfers to other families is not established here.

## Related

- [[accuracy-masks-unstable-reasoning]] — a related finding that a correct answer can come from an unstable route; there the route is measured by internal stability, here by the visible chain under compression.
- [[process-outcome-consistency-verification]] — the same concern, correct answers from wrong derivations, handled as a training reward rather than an evaluation of compression.
- [[hint-adherence-without-acknowledgement]] — another case where the stated reasoning and the actual basis for the answer can diverge.
- [[accuracy-auditability-trade-off]] — the general tension between a final answer that can be checked and a reasoning trace that can be inspected.
- [[cache-coverage-over-precision]] — the mechanism the paper offers for why eviction, but not quantization, opens the gap.

[^c1]: doi-10-48550-arxiv-2608-01631 — "We call this the"
[^c2]: doi-10-48550-arxiv-2608-01631 — "accuracy while substantially degrading"
[^c3]: doi-10-48550-arxiv-2608-01631 — "an incorrect setup, applies an invalid formula or"
[^c4]: doi-10-48550-arxiv-2608-01631 — "We use RWAC as the numerator and report"
[^c5]: doi-10-48550-arxiv-2608-01631 — "Other tokens make the answer auditable, such as intermediate equations, premise"
[^c6]: doi-10-48550-arxiv-2608-01631 — "rather than mechanistic: we do not assume that"
[^c7]: doi-10-48550-arxiv-2608-01631 — "rank highly by final answer tend to rank poorly"
[^c8]: doi-10-48550-arxiv-2608-01631 — "coverage-preserving KIVI rarely degrades"
[^c9]: doi-10-48550-arxiv-2608-01631 — "the uncompressed model often selects the right option without a fully verifiable rationale by guessing"
[^c10]: doi-10-48550-arxiv-2608-01631 — "evidence, accuracy itself collapses."
[^c11]: doi-10-48550-arxiv-2608-01631 — "but we do not provide a causal"
[^c12]: doi-10-48550-arxiv-2608-01631 — "We do not claim state-level semantic attribution or"
[^c13]: doi-10-48550-arxiv-2608-01631 — "Our study is diagnostic rather than exhaustive."
[^c14]: doi-10-48550-arxiv-2608-01631 — "change the reasoning trajectory, generation length,"
[^c15]: doi-10-48550-arxiv-2608-01631 — "exact RWAC values may vary"
[^c16]: doi-10-48550-arxiv-2608-01631 — "On 400 stratified outputs,"
[^c17]: doi-10-48550-arxiv-2608-01631 — "often made results cluster near Full-KV, making it"
[^c18]: doi-10-48550-arxiv-2608-01631 — "Our primary model is Qwen3-8B"
