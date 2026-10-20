---
description: "Judging whether a passage is relevant to a query needs three or more tokens at once, while attention composes only pairs, so filtering noise may need depth that a small retriever lacks."
aliases: ["triple-wise problem", "triplewise noise filtering", "Match3 relevance", "pairwise attention limit on relevance"]
sources: ["arxiv-2601-01896"]
---
# Triple-wise relevance judgment

Filtering irrelevant text is hard for a structural reason, the paper argues: whether a token or a passage is relevant depends on several tokens together, while self-attention relates tokens two at a time. In its example, the query "Alice and Bob are running, Bob is exhausted. How does Bob feel?" makes "exhausted" useful only if the model links it to the subject "Bob", to the asked-for "feel", and to the copula around them. "Thus, evaluating relevance requires the information from three or even more tokens."[^c1] Each attention layer, by contrast, computes "relationships only between pairs, making it challenging to effectively address this issue."[^c2]

The paper turns this into a claim about capacity. Judging the token "exhausted" means the embedding must already hold the meaning of the whole sentence before the judgment is made. A single layer carries roughly m·p bits, with embedding dimension m and precision p, and that is hard to fit a sentence into when the input is long.[^c3] The paper then reduces noise filtering to a triple-wise matching task, Match3 in the sense of Sanford et al. (2024), and states that the nature of the task "may necessitate numerous transformer layers, which means we can hardly filter out noise documents with small models."[^c4] Its appendix gives a one-layer bound: below a size of order n^H(w)/log log n in the memory product mpH, no one-layer transformer computes the relevance labels.[^c5] For deeper models the paper offers only a conjecture, that any multi-layer transformer computing Match3 needs width, depth, embedding dimension or bit complexity that grows polynomially with the context length.[^c6]

The practical consequence the paper draws is about where the work should sit. Because a small retriever is capacity-limited, it will "always incorporate some noisy information in the retrieval results."[^c7] The burden of noise filtering should then move "from the limited-capacity retriever to the powerful LLM itself," whose embedding dimension (4096 for Llama3-8B) and depth (32 layers) are, on this argument, large enough in principle.[^c8] The move is not free, because the LLM's own attention is pairwise too, and fine-tuning to filter noise runs into the trade-off described in [[linear-update-attention-tradeoff]].

## Limits

- The triple-wise argument is about what one layer or a bounded-capacity model can compute on an abstract matching task. It is not a measurement of any deployed retriever or LLM; the paper does not count how many noisy passages a given retriever returns in its own experiments.
- The multi-layer case is a conjecture in the paper's own appendix, not a theorem. Read it as a hypothesis about depth, not as a bound that holds for the 32-layer models it names.
- The step from one sentence (the "Bob" example) to a whole document judged against a whole query is asserted, not shown. The paper's Match3 reduction is in terms of one bit per match; real relevance is graded, and the mapping is not checked.
- The capacity count mp is a heuristic. Precision and embedding size are not the only way a model can carry information, and the paper does not test whether longer or wider attention escapes the bound in practice.
- The same Match3 problem is bounded in another resource in [[cot-token-complexity-lower-bound]], where the cost is chain-of-thought tokens rather than layers and width. The paper does not connect the two accounts, so a bound on one does not transfer to the other.

## Related

- [[linear-update-attention-tradeoff]] — the paper's next step: given that filtering must happen inside the LLM, why fine-tuning for it is hard.
- [[cot-token-complexity-lower-bound]] — the same Match3 matching task, bounded in reasoning tokens instead of layers.
- [[distractor-similarity-reasoning-inflation]] — the empirical side: distractors that look like the question do the most damage, which is the case a triple-wise judgment has to resolve.

[^c1]: arxiv-2601-01896 — "evaluating relevance requires the information from three or even more tokens"
[^c2]: arxiv-2601-01896 — "self-attention computes relationships only between pairs, making it challenging to effectively address this issue."
[^c3]: arxiv-2601-01896 — "But this can hardly represent the meaning of the whole sentence, especially when the input sequence is long."
[^c4]: arxiv-2601-01896 — "the inherent triple-wise nature of the noise filtering process may necessitate numerous transformer layers"
[^c5]: arxiv-2601-01896
[^c6]: arxiv-2601-01896 — "Every multi-layer transformer that computes Match3 must have width, depth, embedding dimension, or bit complexity at least N"
[^c7]: arxiv-2601-01896 — "would always incorporate some noisy information in the retrieval results"
[^c8]: arxiv-2601-01896 — "This suggests the burden of noise filtering should shift from the limited-capacity retriever to the powerful LLM itself."
