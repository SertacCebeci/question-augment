---
description: "An end-to-end clarification-utility metric that scores a deep-search answer by the judge-weighted fraction of a static, evidence-grounded gold nugget set it restores, with partial credit."
aliases: ["restore_score_100", "weighted nugget recall", "restoration score", "weighted criterion-level rubric score", "weight-recovered rubric score"]
sources: ["huang-2026-clarify", "arxiv-2512-16978", "arxiv-2512-13059"]
---
# Weighted nugget recall

> Score a clarifying question not by how it reads, but by how much of a
> fixed, evidence-grounded answer key the pipeline it kicks off eventually
> recovers.

## Definition / Mechanism

Huang et al. (2026) define `restore_score_100` for
the Clarify-Then-Search benchmark. For each intent query $q^*$, a
deep-search [[backbone-of-a-formula|backbone]] (WebDancer) is run once, and an evidence-grounded
nugget extractor produces a fixed golden set $N=\{(n_j,w_j)\}_{j=1}^m$ of
atomic, weighted, source-traceable statements: "This procedure yields a
single archived nugget set per query, which is reused across all evaluated
systems and all 𝑘 settings."[^c1]

A candidate answer $\hat y$ (produced after $k\in\{1,2,3\}$ clarification
questions, a closed-book rewrite, and a fresh deep-search run on the
rewritten query) is scored against that fixed set by an LLM judge that
labels each nugget's coverage `full` ($s=1$), `partial` ($s=0.5$) or `none`
($s=0$): "We define weighted nugget recall with partial credit as
$\mathrm{Recall}(\hat y)=\sum_j w_j\cdot s(\mathrm{cov}(n_j,\hat
y))/\sum_j w_j$" and `restore_score_100 = 100 × Recall(ŷ)`.[^c2]

## Why it matters

This gives stall 2 a downstream-utility metric for a clarifying question
rather than a proxy for its surface quality: the paper's own framing is
that "many prior benchmarks focus on question-level properties, such as
fluency, plausibility, or topical relevance, which are weak proxies for
whether clarification actually improves downstream search utility." Because
the gold set is archived once from a single oracle run and reused across
every Clarifier and every $k$, differences in `restore_score_100` isolate
the Clarifier's contribution rather than run-to-run variance in the
search backend: "To isolate clarification ability, we vary only the
Clarifier while keeping UA, Rewriter, the deep-search backend, nugget
construction, and nugget judging fixed." Across seven tested Clarifiers at
$k=1$, mean `restore_score_100` rises from 19.434 (no clarification) to
22.527–26.474, with all seven paired-bootstrap 95% confidence intervals on
the improvement strictly above zero.[^c3]

## Transfer

| | Home field | Here |
|---|---|---|
| Formalism | TREC-style nugget-based QA evaluation: score an answer by the weighted, pyramid-graded atomic facts ("nuggets") it covers against a fixed reference set | Applied to the output of a whole clarify→rewrite→deep-search pipeline instead of a single-turn QA answer, so the score attributes to the clarifying question(s) that shaped the rewrite |
| What survives | Weighted, atomic reference units and partial credit for covering a fact incompletely | Both carry over: nuggets keep per-item weights $w_j$ and a three-level (full/partial/none) coverage label |
| What does not | Classic nugget matching judges a static answer against a reference built independently of the system under test | Here the reference is built from a *one-time run of the same class of system being scored* (WebDancer on the oracle query), so the "gold" is only as trustworthy as that single archived run, and coverage is judged by an LLM rather than a human annotator |
[^c4]

The same weighted fraction appears as a rubric score in a long-video benchmark, LongShOTBench, where it is called a weighted criterion-level rubric. Each question carries criteria on a 10-point priority scale, and the score is the "weight recovered by satisfied criteria, scaled to a 0-100 range."[^c5] An LLM verifier decides each criterion as a binary match: it "checks each criterion ci against the gold reference answer and marks it satisfied or not based" on the candidate's match to the gold.[^c6] What carries over is the weighted atomic unit and the weighted sum. What changes is that the three-level full/partial/none label of nugget recall collapses to satisfied or not, and the weights are set per item when the rubric is generated rather than read off an archived oracle run. The reported agreement with four human annotators on 400 criterion decisions is κ=0.75 for the three-verifier ensemble.[^c7] Treating the two as one concept is my reading; the video paper does not test the score against any independent measure of what matters.

A factuality metric of the same family appears in the MMU-RAG deep-research system of arxiv-2512-13059. It is key point recall (KPR), and the authors "refer to" it as factuality.[^c9][^c10] Its reference is not an oracle run: key points are extracted from the web pages that users clicked for each training question.[^c11] The metric is one of the terms summed into that paper's preference score, and it is missing for two of the three sources because the click URLs are not available there.[^c12] Whether KPR weights its key points or gives partial credit is not stated in the text read; any link to this note's weighting is my inference.

## Limits

- The gold nugget set is a single archived WebDancer run per query, not a
  human-curated reference; an error or omission in that one run propagates
  into every system's score for that instance, and no inter-annotator or
  cross-backbone agreement figure is reported for the gold construction
  step itself.
- Nugget coverage is judged by one LLM (ERNIE-4.5-Turbo) at temperature 0;
  the paper reports the improvement trend is stable across ERNIE-, GPT-
  and Claude-based judges but that absolute scores vary across judges, so
  the 0–100 number is judge-relative, not judge-independent.
- Reported only on one benchmark (518 Baidu-search-derived instances, one
  deep-search backbone, $k\le3$): whether the metric behaves the same with
  a different backbone or a larger clarification budget is untested.

- The video rubric's weights come from a generator built on one LLM family, and the paper names this as a limit: "systematic biases in those models can propagate into the benchmark."[^c8] A weighted score is only as fair as its weights, and nothing here checks the weights against an independent measure of importance.

## Related

[[clarification-benchmarks]] · [[turn-discounted-key-question-rate]] · [[optimal-round-adherence]] · [[value-of-information]]

[^c1]: huang-2026-clarify — "This procedure yields a single archived nugget set per query, which is reused across all evaluated systems and all 𝑘 settings."
[^c2]: huang-2026-clarify — "We define weighted nugget recall with partial credit as"
[^c3]: huang-2026-clarify — "many prior benchmarks focus on question-level properties, such as fluency, plausibility, or topical relevance, which are weak proxies for whether clarification actually improves downstream search utility"
[^c4]: huang-2026-clarify — "Nuggetbased protocols score coverage of atomic information units and have been used in QA-style evaluations [14], with pyramid weighting improving robustness [7]."
[^c5]: arxiv-2512-16978 — "weight recovered by satisfied criteria, scaled to a 0-100 range"
[^c6]: arxiv-2512-16978 — "verifier checks each criterion ci against the gold reference answer and marks it satisfied or not based"
[^c7]: arxiv-2512-16978 — "The 3-verifier ensemble reaches κ=0.75"
[^c8]: arxiv-2512-16978 — "systematic biases in those models can propagate into the benchmark"
[^c9]: arxiv-2512-13059 — "we use the KPR metric"
[^c10]: arxiv-2512-13059 — "Evaluating long-context & long-form retrieval-augmented generation with key point recall"
[^c11]: arxiv-2512-13059 — "to extract key points used in the factuality evaluation"
[^c12]: arxiv-2512-13059 — "clarity and insightfulness for Natural Questions and the validation set"
