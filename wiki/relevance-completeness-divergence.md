---
description: "Topical relevance scores explain almost none of the variance in human-rated completeness of an answer, so relevance is not a proxy for sufficiency."
aliases: []
sources: ["nakarmi-2026", "doi-10-48550-arxiv-2609-37469", "openalex-org-w7128864259", "arxiv-2511-19481"]
---
# Relevance-completeness divergence

> An answer can score high on context relevance and answer relevance while a
> human still marks it incomplete — relevance and [[sufficient-statistic|sufficiency]] are measuring
> different things.

## Mechanism

Nakarmi et al. (2026) evaluate a water-quality RAG pipeline
with standard relevance metrics (context relevance, answer relevance, both
adopted from prior RAG-evaluation work) alongside a completeness score they
co-designed with community stakeholders — a 1–5 Likert rating of whether a
response covers what a layperson needs to understand the situation,
including transparent disclosure of uncertainty. Across pipeline variants
that differ sharply in context and answer relevance, completeness did not
track them: "relevance-based metrics account for about 1% of the variance in
human-assessed completeness."[^c1]

The correlation figures behind that number: "Analysis showed a weak
association between completeness and answer relevance (ρ = 0.05) and context
relevance (ρ = 0.09). The relevance metrics yield low explanatory power
(R2 = 0.014) in predicting human evaluation of completeness."[^c2]

An LLM judge fine-tuned specifically on the human completeness annotations
did better but still only moderately: "a fine-tuned LLM judge showed improved
alignment with human evaluations (ρ = 0.73)... [but] only showed moderate
agreement (Cohen's κ = 0.54) with human evaluation," up from ρ = 0.41 for the
untuned judge.[^c3]

## Why it matters

Stall 5 asks whether what came back is actually a constraint.
This is a direct negative result for using retrieval-relevance scores as
that check: a response can be judged highly relevant by the standard IR
metrics and still be rated incomplete by the people the answer is for, at an
association (R² = 0.014) close to none. It also bears on [[semantic-entropy]]
and other computable proxies for answer quality — a proxy built on semantic
or topical closeness to the query is not shown here to track whether the
asker's actual information need was met, and even a judge trained
specifically on this task's completeness labels only reaches moderate
agreement with humans.

## Relevance versus sufficiency in retrieval

The same dissociation appears in retrieval evaluation, where the unit is the passage set rather than the answer. A per-passage relevance grade can hold while the set still omits a needed fact: "a relevant passage can omit the fact" the answer needs.[^c4] On constructed sufficient and insufficient evidence sets, the per-passage judges score well below a set-level scorer; the paper's relevance-based UPR reaches "UPR (Sachan et al., 2022) at 0.721" against 0.837 for the set-level scorer RINSE, where the scale is pairwise accuracy and chance is 0.5.[^c5] The domains differ, and the paper does not measure human completeness, so this is a neighbouring result, not a replication of the 1% figure. See [[pre-generation-evidence-sufficiency]].

A design proposal for analytical search states the same break as a requirement rather than a finding. There, relevance is defined by use: "A document may be topically related yet analytically irrelevant if" it does not feed a sub-question, and weakly related evidence can be "crucial for completing a reasoning chain."[^c6][^c7] The proposal asks retrieval to score candidates "by their reasoning value," but it reports no measurement of how far topical and reasoning value diverge.[^c8] The two papers measure different things; the proposal only names the gap (my reading).

A regression study on retrieval-augmented generation reports a link in the opposite direction. Its correlation analysis finds that "analysis reveals a positive relationship (r=0.66) between document relevance and answer quality."[^c9] But the quality variable is not a judgment of completeness alone: "a composite score (0-100) based on expert ratings of answer relevance, accuracy, and completeness."[^c10] A correlation between relevance and a label that already contains relevance is partly a part correlated with its whole (my inference), so it is not a test of the construct the 1% figure measures. What the paper does establish is narrower: in its one dataset, the two variables move together. The claim that relevance is not a proxy for sufficiency is therefore a claim about completeness, not about every answer-quality label.

## Limits

- One domain (water-quality outreach) and one completeness rubric,
  co-designed with a specific community and folding uncertainty-disclosure
  into the same score rather than scoring it separately; the low correlation
  is not shown to hold for other definitions of completeness.
- The completeness ground truth is two annotators' Likert ratings (Cohen's
  κ = 0.65 between them) on 648 answers — substantial but not perfect
  agreement, so part of the "1%" gap could reflect annotator noise as well
  as a real construct difference.
- The paper reports the correlation, not a mechanism for why relevance and
  completeness dissociate; that a checklist-covering answer can still score
  low on topical relevance metrics (and vice versa) is observed, not
  explained.
- The regression paper's correlation is the only measure of its link in the
  text read; the text gives no sample size and no significance test, and its
  quality label is built by expert raters whose number is not stated.
- That paper is not consistent about its own variables. It says "The dataset
  includes 8 key features"[^c13] and elsewhere reports "original 7dimensional
  tabular features into 35-dimensional enhanced"[^c14]. Its diversity
  correlations also change sign between sections: "(-0.89 and 0.88, respectively)"[^c12]
  in one place and "exhibits strong negative correlations with semantic
  similarity (0.89) and redundancy (-0.88)"[^c11] in another. Its figures are
  read with that in mind.

## Related

Answer · [[semantic-entropy]] · [[dual-judge-completeness-recall]] · [[clarification-benchmarks]]

[^c1]: nakarmi-2026 — "relevance-based metrics account for about 1% of the variance in human-assessed completeness"
[^c2]: nakarmi-2026 — "Analysis showed a weak association between completeness and answer relevance (ρ = 0.05) and context relevance (ρ = 0.09). The relevance metrics yield low explanatory power (R2 = 0.014) in predicting human evaluation of completeness."
[^c3]: nakarmi-2026 — "a fine-tuned LLM judge showed improved alignment with human evaluations (ρ = 0.73)"
[^c4]: doi-10-48550-arxiv-2609-37469 — "a relevant passage can omit the fact"
[^c5]: doi-10-48550-arxiv-2609-37469 — "UPR (Sachan et al., 2022) at 0.721"
[^c6]: openalex-org-w7128864259 — "A document may be topically related yet analytically irrelevant if"
[^c7]: openalex-org-w7128864259 — "crucial for completing a reasoning chain"
[^c8]: openalex-org-w7128864259 — "but by their reasoning value"
[^c9]: arxiv-2511-19481 — "analysis reveals a positive relationship (r=0.66) between document relevance and answer quality"
[^c10]: arxiv-2511-19481 — "a composite score (0-100) based on expert ratings of answer"
[^c11]: arxiv-2511-19481 — "exhibits strong negative correlations with semantic similarity (0.89) and redundancy (-0.88)"
[^c12]: arxiv-2511-19481 — "(-0.89 and 0.88, respectively)"
[^c13]: arxiv-2511-19481 — "The dataset includes 8 key features"
[^c14]: arxiv-2511-19481 — "original 7dimensional tabular features into 35-dimensional enhanced"
