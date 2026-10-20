---
description: "Write-back of a generated answer into the retrieval corpus is gated by grounding, attribution and novelty checks; the gate trades coverage for slower, safer corpus growth."
aliases: ["Bidirectional RAG", "gated write-back", "generated-answer write-back", "safe corpus expansion", "self-improving retrieval-augmented generation"]
sources: ["arxiv-2512-22199"]
---
# Validated answer write-back

A retrieval-augmented system answers a query by retrieving passages from a corpus and generating from them. Write-back adds a backward path: the generated answer is itself stored in the corpus, so later queries can retrieve it. The corpus then grows from use rather than only from ingestion. The paper's point is that the write is conditional. An answer y, produced from retrieved set X for query q, is written only when an acceptance layer returns ACCEPT; otherwise the corpus is left as it was.[^c1]

The gate exists because the unconditioned version is expected to fail. The paper states the central challenge as "storing all outputs would rapidly pollute the corpus with hallucinations, creating a self-reinforcing degradation cycle."[^c2] Gated write-back is therefore a claim about one feedback loop: a system whose answers become its own evidence can amplify its errors unless each answer passes a check before it is stored.

The acceptance layer has three sequential checks, in the paper's order.

- **Grounding.** Each sentence of y is scored by the maximum entailment probability it receives from a cross-encoder NLI model against each retrieved document, averaged over sentences. The paper requires the average to reach 0.65: "require grounding(y, X) ≥ 0.65 for acceptance."[^c3]
- **Attribution.** The fraction of citations in y that name retrieved documents. The paper frames it as checking "that generated citations reference actual retrieved documents."[^c4]
- **Novelty.** One minus the largest similarity between y and the documents already in the corpus, required to be at least 0.10, which keeps near-duplicates out.[^c5]

Rejected answers are not discarded. Their critiques go into an experience store, which is retrieved at query time to steer later generation away from the same failures: "why responses were rejected. These are retrieved at query" time.[^c6]

What was measured. Four datasets (Natural Questions, TriviaQA, HotpotQA, Stack Overflow), 500 queries each split 400 train and 100 test, three seeds, giving 12 experiments per system.[^c7] Coverage is the fraction of queries with a retrieval closer than distance 0.4.[^c8] Standard RAG reached 20.33% coverage with no growth. Naive write-back reached 70.50% coverage by adding 500 documents. The gated system reached 40.58% by adding 140.[^c9] The paper says plainly that the gate costs coverage: the validation "sacrifices some coverage compared to naive write-back" in exchange for safety.[^c10] The gain is therefore relative to standard retrieval, and the cost relative to naive write-back is a deliberate trade the paper argues for, since "false negatives (rejecting good content) preferable to false positives (accepting bad content)."[^c11]

The mechanism, as stated: write-back is a filter on what enters the evidence base, not a way of making answers more correct. The gate decides which answers may become evidence; it does not decide whether an accepted answer is true.

## Limits

- **The coverage metric is partly tautological under write-back.** Coverage counts a query as covered when some document lies within distance 0.4 of it. An accepted answer is a document, and it is generated for the same query, so it will often sit near that query whether or not it is correct. My reading is that Table I therefore cannot separate "more useful evidence" from "more documents near the queries". The paper does not report the correctness of accepted documents in the parts I read.
- **The thresholds are not calibrated.** The paper's grounding threshold "may require per-domain calibration. We report grounding as a binary" signal, and the result is recorded as "feature (present/absent) rather than a continuous score."[^c12]
- **Narrow setup.** One generator: "Generator: Ollama llama3.2:3b (local inference)."[^c13] One retriever and one embedding model, one author, consumer hardware. Nothing here shows the effect for a stronger generator, where the grounding model's errors may differ.
- **No ablation of the three checks** appears in the sections I read, so the separate contribution of grounding, attribution and novelty is not established.
- **Cost.** "Validation adds overhead: 71s vs 32s per query for Standard" RAG,[^c14] which the paper accepts for offline building.
- **Drift.** The paper says "long-term corpus drift effects unexplored."[^c15] Whether the gate keeps the corpus stable over many rounds of its own writes is not tested.

## Related

- [[self-answering-injection-compliance]] — a self-generated answer can carry constraints from its source text; a write-back gate that checks grounding does not address that channel, by my reading.
- [[zoned-experience-evolution]] — also keeps a library of past experiences that guides later generation; it learns the library by evolution, where this paper stores critiques of rejected answers.

[^c1]: arxiv-2512-22199 — "Backward path (novel):"
[^c2]: arxiv-2512-22199 — "storing all outputs would rapidly pollute the corpus with"
[^c3]: arxiv-2512-22199 — "require grounding(y, X) ≥ 0.65 for acceptance."
[^c4]: arxiv-2512-22199 — "reference actual retrieved documents:"
[^c5]: arxiv-2512-22199 — "We require novelty(y, Dt ) ≥ 0.10."
[^c6]: arxiv-2512-22199 — "why responses were rejected. These are retrieved at query"
[^c7]: arxiv-2512-22199 — "Each dataset uses 500 queries (400 train, 100 test) across 3"
[^c8]: arxiv-2512-22199 — "Coverage: Fraction of queries with relevant retrievals"
[^c9]: arxiv-2512-22199 — "while adding 72% fewer documents than naive write-back (140"
[^c10]: arxiv-2512-22199 — "sacrifices some coverage compared to naive write-back"
[^c11]: arxiv-2512-22199 — "false negatives (rejecting good content) preferable to false positives (accepting bad"
[^c12]: arxiv-2512-22199 — "feature (present/absent) rather than a continuous score."
[^c13]: arxiv-2512-22199 — "Generator: Ollama llama3.2:3b (local inference)"
[^c14]: arxiv-2512-22199 — "Validation adds overhead: 71s vs 32s per query for Standard"
[^c15]: arxiv-2512-22199 — "long-term corpus drift effects unexplored."
