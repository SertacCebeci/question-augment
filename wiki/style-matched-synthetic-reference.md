---
description: "Before embedding comparison, a short gold answer is rewritten once into a full-sentence reference in the response style, so a verbose response is no longer compared with a bare token."
aliases: ["synthetic canonicalized reference", "canonicalized reference answer", "distribution-aligned reference", "synthetic answer reference"]
sources: ["arxiv-2511-17432"]
---
# Style-matched synthetic reference

A factoid benchmark stores its gold answer as a bare token: a number, a name, a short phrase. Model responses are written in sentences, and they have been getting longer. The paper calls this a distributional misalignment: "are often lengthier, contrasting with the typical short answers in factoid QA benchmarks."[^s1] An embedding comparison between a long response and a bare token is then dominated by the difference in length and form, not by whether the content agrees.

The remedy is to rewrite the gold answer once, in the style of a response. A language model is given the question and the gold answer and writes a full-sentence reference. The paper uses "a lightweight model (e.g., 3B parameter)" as the generator.[^s2] Its example is a question about a conversion rate with gold answer 8, which yields a sentence ending "an event is 8."[^s3] The reference keeps the gold content and changes only its form. The generator is not the model being evaluated, and the rewrite is not repeated per model: "synthetic answer generation is independent of the model being evaluated and is performed only once, prior to test-time, per evaluation set."[^s4] A stored reference can serve every later evaluation of that set, so the cost is paid once.

The mechanism is the same as the one behind the length problem in grounding scores. A cosine between an answer and its evidence is driven by length and specificity mismatch, not by support, as [[answer-evidence-embedding-similarity]] describes for short answers. A reference in the response's register removes part of that mismatch before the cosine is taken. What the rewrite changes is the embedding comparison. It does not change the gold content, and it does not repair a metric that counts surface overlap.

The paper's comparison of the original and the rewritten references shows this limit. Across datasets and modalities, the traditional metrics "stagnate or degrade under Syn, whereas SMILE remains stable and typically strongest."[^s5] The overlap metrics are hurt for a reason the paper gives: they "over-score verbose or even contradictory responses" because the rewritten reference raises surface overlap, which can hide factual errors.[^s6] So the alignment is useful for a semantic term and harmful for an overlap term. The paper states the general point: "canonicalization alone cannot fix metrics that privilege surface overlap and fluency over semantic correctness."[^s7]

The component ablation of the same paper includes a run without the synthetic answers. The extracted table does not let me read the row values reliably, so I do not report a number for that run (my reading).

## Limits

- The rewrite is produced by a language model, and the paper does not test whether the generated sentence can drift from the gold content. The sections I read check the generator against other generators, not against the gold answer or against human judgment of content (my inference). An error in the rewrite would enter every later score for that item.
- The rewrite targets one register: the typical sentence-length reply to a factoid question. A model that answers tersely or in a list has a different register, and the paper does not test a generator matched to such a model (my inference).
- The benefit is shown for the semantic term. The paper's finding is that the rewrite does not rescue the overlap metrics, so it cannot be used as a general fix for reference-based scoring.
- The study "focuses on factoid QA tasks."[^s8] The claim about the rewrite applies to short gold answers. It is not shown for long gold answers, where the register gap is different.

## Related

- [[composite-lexical-semantic-scoring]] — the metric whose semantic term is computed against this reference; the lexical term is computed against the bare gold answer
- [[exact-match-verbosity-penalty]] — the bare-token exact-match rule penalises the same verbose-response case that the rewrite addresses for embedding scorers
- [[answer-evidence-embedding-similarity]] — the same length-and-specificity mismatch in an answer-to-evidence cosine, where it is a grounding failure rather than a reference mismatch

[^s1]: arxiv-2511-17432 — "are often lengthier, contrasting with the typical short answers in factoid QA benchmarks"
[^s2]: arxiv-2511-17432 — "a lightweight model (e.g., 3B parameter) can be deployed as a synthetic answer generator g"
[^s3]: arxiv-2511-17432 — "an event is 8"
[^s4]: arxiv-2511-17432 — "is performed only once, prior to test-time, per evaluation set"
[^s5]: arxiv-2511-17432 — "or degrade under Syn, whereas SMILE remains stable and typically strongest"
[^s6]: arxiv-2511-17432 — "over-score verbose or even contradictory responses because increased surface overlap with the canonicalized"
[^s7]: arxiv-2511-17432 — "canonicalization alone cannot fix metrics that privilege surface overlap and fluency over semantic correctness"
[^s8]: arxiv-2511-17432 — "our study focuses on factoid QA tasks"
