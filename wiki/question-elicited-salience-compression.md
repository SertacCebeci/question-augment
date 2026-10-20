---
description: "A compressor pretrained on generated questions and paraphrases keeps the facts those questions ask about, instead of reconstructing tokens; the question set decides what survives."
aliases: ["question-driven compression pretraining", "salient information elicitation", "QA-supervised compressor pretraining", "salient compressor pretraining"]
sources: ["arxiv-2511-18659"]
---
# Question-elicited salience compression

Compressing a document into a few continuous vectors needs a training target that says which content to keep. The common target is token reconstruction, and the CLaRa authors argue it is the wrong one: "This risks wasting limited capacity/budget on potentially trivial token-by-token"[^c1] reconstruction. Their replacement is to first make the salient content explicit, and then train the compressor to keep it.

The supervision is generated offline. "Using 2M sampled Wikipedia-2021 documents"[^c2] a locally run LLM writes three kinds of output per document. Simple QA pairs are built so that "each pair targets a single atomic fact."[^c3] Complex QA pairs are built so that "each pair integrates multiple facts to promote relational reasoning."[^c4] Paraphrases restate the whole document. A verification pass checks each output for coverage, and the missing content is regenerated "iteratively up to ten rounds."[^c5] The stated reason for using questions is that "they tell the model which details are essential for answering"[^c6] meaningful questions.

The compressor itself appends learnable memory tokens to the document, and "the final-layer hidden states of the memory tokens" [^c7] form the compressed vector. The generator is trained to produce the QA answers or paraphrases from that vector. The total loss adds a mean-squared term that ties the memory-token states to the averaged document-token states, so that "we encourage their latent representations to remain aligned."[^c8]

What was measured. In an ablation on the data mix, "using either SimpleQA or Paraphrase alone already outperforms the no-pretraining baseline."[^c9] Combining question types and paraphrases gave the best result, "confirming that diverse objectives enhance semantic coverage and generalization."[^c10] The alignment term is described as one that "leads to a modest" gain, though a consistent one.[^c11] The text also ties the size of the pretraining benefit to retrieval: "high-quality retrieval amplifies pretraining benefits."[^c12]

How it fits. The authors position the work against token-level and single-vector compression, arguing that "a more targeted pretraining objective can still yield richer and more informative representations."[^c13] In the mechanism as I read it, the question set is the lever: the compressor is pushed to keep whatever the generated questions can be answered from, so content that no question touches gets less pressure to survive. That is my inference from the design; the text does not measure what was left out.

## Limits

- The supervision is synthetic and produced by one local model family. The verification step uses the same kind of model: outputs are "verified by the locally deployed LLM for factual consistency and information coverage."[^c14] The parts read do not test other corpora, other generators, or a human check of coverage.
- The data-mix ablation does not separate the question signal from the paraphrase signal in a way that makes questions necessary. Either one alone helps, so the question-specific contribution is not isolated as the cause.
- The claim that reconstruction "wastes capacity" is the authors' argument. In the parts read there is no reconstruction-only baseline trained on the same documents, so the comparison is argued rather than measured there.
- The gains are reported on QA with a fixed retrieval setup. The text ties the size of the pretraining benefit to retrieval quality, so with noisy retrieval the benefit may be smaller. The parts read do not show that curve.
- The alignment term is a modest gain by the authors' own description, and it is a term on hidden-state means, not a check that the compressed vector answers the questions it was built from.
- The parts read do not test whether a question-elicited vector keeps facts that a later, unrelated question needs. The training questions are the only ones the compressor was shaped by.

## Related

- [[answer-supervised-retrieval]] — the second stage of the same paper: the compressed vectors built here are the frozen index that a retriever is later trained over.
- [[compress-and-merge-soft-prompt]] — compresses each document into a fixed soft prompt and merges them; its description already marks it lossy for detailed facts, which is the gap question-elicited pretraining targets.
- [[compressed-memory-versus-raw-retrieval]] — whether a compressed store loses what a later query needs; the question-driven compressor here is a trained answer to the same worry.

[^c1]: arxiv-2511-18659 — "This risks wasting limited capacity/budget on potentially trivial token-by-token"
[^c2]: arxiv-2511-18659 — "Using 2M sampled Wikipedia-2021 documents"
[^c3]: arxiv-2511-18659 — "each pair targets a single atomic fact"
[^c4]: arxiv-2511-18659 — "each pair integrates multiple facts to promote relational reasoning"
[^c5]: arxiv-2511-18659 — "iteratively up to ten rounds"
[^c6]: arxiv-2511-18659 — "they tell the model which details are essential for answering"
[^c7]: arxiv-2511-18659 — "The final-layer hidden states of the memory tokens"
[^c8]: arxiv-2511-18659 — "we encourage their latent representations to remain aligned"
[^c9]: arxiv-2511-18659 — "using either SimpleQA or Paraphrase alone already outperforms the no-pretraining baseline"
[^c10]: arxiv-2511-18659 — "confirming that diverse objectives enhance semantic coverage and generalization"
[^c11]: arxiv-2511-18659 — "including this loss leads to a modest"
[^c12]: arxiv-2511-18659 — "high-quality retrieval amplifies pretraining benefits"
[^c13]: arxiv-2511-18659 — "pretraining objective can still yield richer and more informative representations"
[^c14]: arxiv-2511-18659 — "verified by the locally deployed LLM for factual consistency and information coverage"
