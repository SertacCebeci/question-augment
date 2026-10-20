---
description: "When a model must return spans copied from a source, its regenerated text can fall outside the source; this validity failure is separate from span alignment and does not track model size."
aliases: ["verbatim span validity", "span copy fidelity", "non-substring extraction", "extraction validity"]
sources: ["arxiv-2511-21401"]
---
# Extractive copy validity

An evidence span is a contiguous part of a text. When a human highlights one, the selection is a span by construction, because the interface only lets them pick characters that are there. A language model asked for the same thing does not select; it writes out the text it takes to be the span. Nothing in that generation step forces the written text to occur in the source. A reply can therefore be fluent and well placed in meaning and still not be a span of the document at all. The Czech and Slovak fact-checking study (arxiv-2511-21401) states the difference directly: annotators highlight, whereas "LLMs were required to regenerate the selected span, allowing generation of subsequences not appearing in the text."[^c1]

The models were told to output only spans appearing verbatim in the text, but the study notes that "this constraint was not enforced technically", and so some outputs "did not occur in the source text."[^c2][^c3] The measured quantity is the share of samples whose output is unusable. The paper's figure reports "the percentage of incorrectly annotated samples (invalid %) they" generated.[^c4] A reply that is not in the text has no position in it, so it cannot be scored against human spans at all. That the output fails validity is a fact about the text; whether the failure is about the meaning of the answer is a separate question.

The rate is large and varies by model. Over the 186 samples used, "the highest number of incorrect annotations 61.8% was produced by the mixtral:8x7b" model, and "the lowest error rate, which aligns with its considerably larger parameter count" went to qwen2.5:72b.[^c5][^c6] The rate does not follow parameter count cleanly. The paper notes that "llama3.3:72b exhibits a relatively high number of invalid outputs despite its large size", and that "gpt-oss:120b, which would be expected to perform among the best, also shows" unexpectedly poor reliability.[^c7][^c8] In the other direction, "Interestingly, llama3.1:8b, one of the smallest" models produced invalid samples in a number "similar compared with" the 685B deepseek-r1.[^c9] The authors read the inability to produce valid output as "a failure to follow instructions."[^c10] If that reading holds, validity is a property of instruction-following, and size explains only part of it. This is my inference from the three cases, not a result the paper tests.

Validity matters for the score because invalid replies are not dropped at random. The study evaluates some model pairs "using a substantially reduced subset of data."[^c11] The authors warn that excluding these replies "may introduce bias — for instance, by disproportionately removing more challenging samples", "and thereby artificially inflating the performance metrics of certain models."[^c12][^c13] The headline agreement figures are likewise computed "only on samples where LLM annotations were generated correctly."[^c14] The hard cases are the ones most likely to lose their reply, so an alignment score taken over the surviving replies is biased upward. The paper argues this; the size of the bias is not measured.

A validity check on the JSON is not a check on this condition. The schema can be correct while a span is not in the text. [[output-accuracy-format-gap]] separates parseability from task correctness; here a third condition appears, membership in the source, which a parser does not see. The paper's remedy is to restrict generation. It says "future work should explore methods that enforce the generation" of structurally valid evidence, and it proposes "to employ constrained decoding mechanisms in the further work."[^c15][^c16] Restricting decoding to tokens of the source would enforce membership by construction. That is a narrower guarantee than the syntactic one in [[constrained-decoding]], and it is my inference rather than something the study builds.

## Limits

- The sample is 186 claim–text pairs, "comprising 186 samples with two independent sets of fine-grained evidence", in one language pair and with one prompt. The authors do not vary the prompt or the decoding settings, so the rates are for this setup.
- The sections read do not say how far an invalid span departs from the source. A near-copy with changed punctuation and an invented sentence both count as "not occurring in the text." The reported rate therefore mixes failures of very different size.
- The figure's values are partly garbled in the text extraction. This note uses only the values stated in the prose.
- Constrained decoding is proposed, not tested. Nothing read shows whether restricting output to source spans lowers the invalid rate or changes alignment.
- Invalid rates are not broken down by sample difficulty, so the direction of the bias from exclusion is asserted by the authors and not measured.

## Related

- [[output-accuracy-format-gap]] — parseability as a second correctness condition; here the condition is membership in the source, which a schema check cannot see.
- [[constrained-decoding]] — the guarantee-by-construction remedy the study proposes but does not test; a source-restricted decoder would be a narrower case of it.
- [[rationale-level-relevance-judging]] — scores highlighted spans against human spans; a span absent from the document has no position to be scored at.

[^c1]: arxiv-2511-21401 — "allowing generation of subsequences not appearing in the text"
[^c2]: arxiv-2511-21401 — "this constraint was not enforced technically"
[^c3]: arxiv-2511-21401 — "spans that did not occur in the source text"
[^c4]: arxiv-2511-21401 — "the percentage of incorrectly annotated samples (invalid %) they"
[^c5]: arxiv-2511-21401 — "The highest number of incorrect annotations 61.8% was produced by the mixtral:8x7b"
[^c6]: arxiv-2511-21401 — "the lowest error rate, which aligns with its considerably larger parameter count."
[^c7]: arxiv-2511-21401 — "llama3.3:72b exhibits a relatively high number of invalid outputs despite its large size"
[^c8]: arxiv-2511-21401 — "gpt-oss:120b, which would be expected to perform among the best, also shows"
[^c9]: arxiv-2511-21401 — "models, has a number of incorrectly generated samples similar compared with"
[^c10]: arxiv-2511-21401 — "interpreted as a failure to follow instructions."
[^c11]: arxiv-2511-21401 — "certain LLM pairs matches are evaluated using a substantially reduced subset of data."
[^c12]: arxiv-2511-21401 — "by disproportionately removing more challenging samples"
[^c13]: arxiv-2511-21401 — "and thereby artificially inflating the performance metrics of certain models."
[^c14]: arxiv-2511-21401 — "are calculated only on samples where LLM annotations were generated correctly"
[^c15]: arxiv-2511-21401 — "future work should explore methods that enforce the generation"
[^c16]: arxiv-2511-21401 — "to employ constrained decoding mechanisms in the further work."
