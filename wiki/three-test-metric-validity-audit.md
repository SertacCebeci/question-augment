---
description: "A metric is audited by style invariance, graded factual-error sensitivity and correlation with experts on metric-disagreement cases; in CT reports, lexical metrics fail and no metric passes all."
aliases: ["CTest-Metric", "metric meta-evaluation by style, error and expert tests"]
sources: ["arxiv-2601-11488", "arxiv-2512-22442"]
---
# Three-test metric validity audit

A metric for generated text can be checked for whether it measures clinical correctness by three separate tests. CTest-Metric, applied to CT radiology report generation, states the criterion: "A clinically grounded metric must be insensitive to report writing styles and sensitive to subtle yet critical factual mismatches."[^c1]

## The three tests

1. **Style invariance (WSG).** An LLM rephrases each prediction while preserving semantics; the metric is run on the original and the rephrasing, and "a lower difference indicates metrics' robustness towards stylistic variations."[^c2]
2. **Graded error sensitivity (SEI).** One, two or multiple factual errors are injected into the ground-truth report, and the score drop from the ideal self-comparison is measured; "a substantial difference in metrics' scores for varying levels of discrepancy shows its strong discriminative ability."[^c3]
3. **Expert correlation on disagreement cases (MvE).** The 25 reports per model on which the metrics' scores vary most (standard deviation across metrics), 175 in all, are rated by clinicians, and each metric is Spearman-correlated with those ratings.[^c4] Choosing the cases where metrics conflict is what makes the expert's time discriminate between metrics.

## What it found (eight metrics, seven CT-CLIP-based generators, CT-RATE)

- Lexical metrics (BLEU, ROUGE, METEOR) changed by -48.82% to -1.16% under rephrasing; F1-RadGraph moved most among clinical metrics; CRG and GREEN were most robust.[^c5]
- BERTScore-F1 was least affected by injected errors (about -2%), whereas GREEN and F1-RadGraph dropped most. All metrics behaved alike with minimal differences and diverged only when multiple errors were injected.[^c6]
- GREEN correlated best with experts (rho = 0.7), then F1-RadGraph (0.53); lexical metrics 0.26 to 0.35; CRG correlated negatively.[^c7]

The tests dissociate: CRG passes style invariance yet fails expert agreement, because it uses label-level presence and so ignores sentence structure.[^c8] So a single test would have ranked metrics differently; passing one is not evidence of the others (my reading of the dissociation).

## A refinement that lowers reference-overlap scores

The same dependence on wording shows up outside clinical reports. HiFi-RAG tried a "Checker" module that critiqued its answers for hallucination. The paper says the checker was "qualitatively better" but that it "degraded automated metrics (ROUGE/DeBERTaScore)", and it gives a guess for the cause: "altering the phrasing too aggressively away from reference text."[^c10][^c11] A reference-overlap score rewards closeness to one phrasing, so an answer revised to be more correct can score lower. The paper gives no count, variance or per-item breakdown for this comparison, so the size of the drop and whether it holds across items are not shown. Its "qualitatively better" judgement is also not described as checked by anyone other than the authors.

## Limits

- Expert validation used two reviewers, with a second opinion on ambiguous cases, and the injected errors were mostly laterality and negation; the fidelity of the LLM edits was not independently validated.[^c9]
- One dataset (CT-RATE); other institutions, contrast phases and body regions untested.[^c9]
- The expert correlation covers only disagreement cases, so it says little about metric ranking on typical reports (my inference).
- Rephrasing is done by an LLM, so the style test inherits that model's own biases.
- No pass thresholds are defined; ranking is comparative.

## Related

- [[validity-screening-protocol]] — another structured check of whether a measure is valid
- [[llm-judge-biases]] — the GREEN-type model-based metrics are LLM judges and share such biases
- [[adversarial-metric-self-review]] — stress-testing a metric before trusting it

[^c1]: arxiv-2601-11488 — "A clinically grounded metric must be insensitive to report writing styles and sensitive to subtle yet critical factual mismatches."
[^c2]: arxiv-2601-11488 — "A lower difference indicates metrics’ robustness"
[^c3]: arxiv-2601-11488 — "A substantial difference in metrics’ scores for"
[^c4]: arxiv-2601-11488 — "The top 25 cases with the highest stan"
[^c5]: arxiv-2601-11488 — "NLG-based metrics were the most"
[^c6]: arxiv-2601-11488 — "all metrics exhibit similar"
[^c7]: arxiv-2601-11488 — "The worst performance was observed using the CRG, which presented a negative correlation"
[^c8]: arxiv-2601-11488 — "CRG remains robust to stylistic changes but correlates"
[^c9]: arxiv-2601-11488 — "Expert validation involved two reviewers, with a second"
[^c10]: arxiv-2512-22442 — "While qualitatively better, it degraded automated metrics (ROUGE/DeBERTaScore)"
[^c11]: arxiv-2512-22442 — "likely by altering the phrasing too aggressively away from reference text"
