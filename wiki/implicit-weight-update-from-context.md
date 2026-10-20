---
description: "A context-conditioned transformer block predicts as if its first MLP weight were rank-one updated by the context; the result now holds for any token, any block and Pre-LN."
aliases: ["implicit dynamics of in-context learning", "implicit weight update of in-context learning", "context as implicit MLP update"]
sources: ["arxiv-2512-11255"]
---
# Implicit weight update from context

Take a transformer block made of a contextual layer, such as self-attention, followed by an MLP. The contextual layer is any layer that can process a sequence of any length, so the block's output at a position depends on the context and the query together.[^c1] The claim is that the output at a position, computed with the context present, equals the output of the same block fed only the query, with its first MLP weight matrix changed by an update that the context determines.[^c2] An earlier result, reference [4] in the paper, gave this for the last token and the first block only, and its skip connections did not match the standard Pre-LayerNorm block.[^c3] The paper extends the statement to any token position, to any block beyond the first, and to residual blocks with layer normalisation.

The update has a definite form. Written for the query x, it is built from the difference between the contextual layer's output with and without the context, and from the query's own contextual output. The result is the outer product of a column vector and a row vector, so the update is rank one.[^c4] For several positions, each position gets its own update, but each update still has rank one, and all of them share the same row vector, the query's contextual output.[^c5][^c6] Reading the form of the update, it depends on both the context and the query. It is therefore not a fixed edit stored in the weights; it is recomputed for each query (my reading of the equation).

The paper's check is in-context linear regression. A 5-layer transformer is trained to solve linear regression tasks in context.[^c7] The test compares the block run with context against the block run with the updated MLP weights, for the last block and the last token. The paper reports that "Figure 1 shows an excellent match between the theory and experiment," and that the results were consistent across random seeds.[^c8][^c9] The mismatch is also reported for every block at several training steps, not only for one block.

What this changes in the picture of a prompt: the weights are not modified, yet for the query's prediction the context acts like a rank-one change to the first MLP layer, aimed by how the context shifts the attention output. A demonstration or an earlier turn can then be read as a targeted, query-specific change to the feedforward computation. This is a reading of the forward computation, and it does not by itself say which examples help.

## Limits

- The verification is toy. It is a small transformer on linear regression, with the match shown for one block and one token. The paper names the next step itself: "it would be interesting to analyse the implicit weight updates of models trained on language."[^c10] Nothing here is measured on a language model.
- One step only. The paper's own limit: "Our work is still limited by considering one step of token generation." An answer that is itself a sequence of tokens is not covered by the theorem.[^c11]
- The equivalence is of outputs, not of learning. The theorem says one block's prediction equals that of a modified block. It does not say the model learns the context by a gradient-like step, and the word "dynamics" in the literature's title does not name a training process (my inference).
- The theorem is stated for the full context. A more general version, in the paper's footnote, "considers any subset of the context", and the paper leaves that version out for simplicity.[^c12]
- The block-to-block extension is by iterated application with refined inputs, which is a proof device. The empirical check reports per-block agreement; a whole-network claim across many blocks and tasks is not tested.
- The result gives no accuracy numbers and no measure of which context content matters. It establishes that the two computations agree, not that the rank-one update is what makes the answer correct.

## Related

- [[in-context-learning-as-label-propagation]] — another mechanistic reading of the same phenomenon, with demonstrations and query as labelled and unlabelled points; the two readings are not tested against each other here.
- [[personalization-as-model-editing]] — a deliberate rank-one edit to a stored association; the implicit update is also rank one, but it comes from the context and is not written into the weights.

[^c1]: arxiv-2512-11255 — "any layer such as self-attention that can process a d-dimensional input sequence of any length N"
[^c2]: arxiv-2512-11255 — "is equivalent to that of the same block with only the previous query as input and specific MLP parameters updated by the context"
[^c3]: arxiv-2512-11255 — "the analysis of [4] applies only to the last token and the first transformer block"
[^c4]: arxiv-2512-11255 — "is of rank one, as the outer product of a column vector and a row vector"
[^c5]: arxiv-2512-11255 — "each update retains rank 1"
[^c6]: arxiv-2512-11255 — "the same v = A(x)"
[^c7]: arxiv-2512-11255 — "a 5-layer transformer trained to solve linear regression tasks in context"
[^c8]: arxiv-2512-11255 — "Figure 1 shows an excellent match between the theory and experiment"
[^c9]: arxiv-2512-11255 — "Results were consistent across different random seeds"
[^c10]: arxiv-2512-11255 — "it would be interesting to analyse the implicit weight updates of models trained on language"
[^c11]: arxiv-2512-11255 — "Our work is still limited by considering one step of token generation"
[^c12]: arxiv-2512-11255 — "The more general version of the theorem considers any subset of the context"
