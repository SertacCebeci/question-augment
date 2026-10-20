---
description: "A cited file:line range is accepted when it overlaps text retrieved into context; this certifies the location was in view, not that the claim it backs is supported."
aliases: ["mechanical citation verification", "citation overlap check", "interval-arithmetic citation check", "citation grounding check", "retrieved-span citation validation"]
sources: ["arxiv-2512-12117"]
---
# Span-overlap citation check

A citation in the form `[file:start-end]` can be checked without reading the claim it supports. Extract the cited range by pattern, then test whether it overlaps a chunk the retriever placed into the model's context. In the code-comprehension system the paper describes, the model is required to end its answer with a "mandatory CITATION: [file:start-end] line", and "citation verification extracts citations via regex", then "validates each cited range overlaps retrieved chunks using interval arithmetic, and flags violations as potential hallucinations."[^c1] The check is mechanical: it needs the retrieved set and the cited numbers, and nothing else.

What it decides is narrow. A passing citation means the cited code was in view when the model answered. The paper states the inference directly: "if citation passes overlap check, cited code demonstrably existed in context."[^c2] The failures it is built to catch are locational: the paper's manual inspection of flagged responses "confirmed genuine hallucination" in the form of "plausible but non-existent file paths", or correct files with wrong line numbers.[^c3] The verifier does not need to understand code. It needs the chunk boundaries and the arithmetic on line intervals.

The reported numbers come from this check combined with a hybrid retriever. Over 30 Python repositories and 180 questions, hybrid retrieval "achieves 92% citation accuracy, significantly outperforming single-mode approaches at 78% (dense-only) and 74%" (sparse-only).[^c4] The metric is defined so that a response counts if it has "at least one valid citation verified through strict overlap checking against retrieved context".[^c5] The paper reports zero false positives for the flags: "if citation passes overlap check, cited code demonstrably existed in context" is the basis for that claim.[^c2]

## Limits

- **Location is not support.** The check never reads the claim. A citation to real, retrieved code that does not bear on the sentence it sits beside passes. My inference, not tested in the text: the check is blind to the case "right place, wrong claim", and the 92% figure cannot tell that case apart from a supported one. A check of this kind is one check of one surface, as the single-check note on fabricated references argues — see [[compound-citation-fabrication-defeats-single-check-verification]].
- **Part of the coverage was supplied by the system.** The paper says that "Auto-cite fallback proved essential: without it, citation coverage would drop to 68% for self-citing models and as low as 22%".[^c6] Among responses with valid citations, "32% required auto-cite fallback appending highestranked" chunk citations, so for those responses the citation is the top-ranked chunk's location, appended by the pipeline.[^c7] A passing check on that citation says the top chunk was in context, which is a fact about retrieval and nothing about the answer.
- **Misses are not counted.** The hallucination rate was "detected through manual inspection of 30% sample".[^c9] The text reports flags and their precision; it does not report how many wrong citations passed the check undetected. "Zero false positives" is a statement about flags, not a recall figure.
- **The residual error is not small.** The paper concedes that "achieving 92% accuracy means 14-15 incorrect citations per 180 questions".[^c8]
- **Untested alternatives.** No support check is compared against this one (for example a second model asked whether the cited span entails the claim). The text covers Python only and six small models; whether the overlap check survives a stronger model that cites more often on its own is not shown.

## Related

- [[compound-citation-fabrication-defeats-single-check-verification]] — a single surface check passes fabricated references; the overlap check is a single check of the same kind, and certifies only locatability.
- [[citation-back-tracking]] — tests whether a cited source supports an uncited claim, the step an overlap check does not take.
- [[structural-neighborhood-expansion]] — decides which chunks enter the context, and so which spans a citation can point to at all.

[^c1]: arxiv-2512-12117 — "range overlaps retrieved chunks using interval arithmetic, and flags"
[^c2]: arxiv-2512-12117 — "if citation passes overlap check, cited code demonstrably existed in"
[^c3]: arxiv-2512-12117 — "models referenced plausible but non-existent file paths"
[^c4]: arxiv-2512-12117 — "achieves 92% citation accuracy, significantly outperforming single-mode approaches at 78% (dense-only) and 74%"
[^c5]: arxiv-2512-12117 — "Citation accuracy computes percentage of responses containing at least one valid citation verified through strict"
[^c6]: arxiv-2512-12117 — "Auto-cite fallback proved essential: without it, citation coverage would drop to 68% for self-citing models and as low as 22%"
[^c7]: arxiv-2512-12117 — "while 32% required auto-cite fallback appending highestranked"
[^c8]: arxiv-2512-12117 — "92% accuracy means 14-15 incorrect citations per 180 questions"
[^c9]: arxiv-2512-12117 — "detected through manual inspection of 30% sample"
