---
description: "A per-span ratio of surviving to total tokens under a context-truncation mask, thresholded to label whether the truncated context still determines an answer."
aliases: ["evidence-survival fraction", "tight-span retention"]
sources: ["khodabandehlou-2026"]
---
# Evidence-survival fraction

> Whether a truncated context still supports an answer is not a property of
> how much text survived — it is a property of whether the *few tokens the
> answer depends on* survived, and only measuring at that grain gives a
> usable signal.

## Definition / Mechanism

Khodabandehlou & Krishnamachari (2026) define, for a supporting span
$S_k$ (a contiguous token range jointly required for an answer $a$ to be
derivable from a context $c$) and a per-token survival mask $m \in
\{0,1\}^{n_c}$ produced by a KV-cache compressor, the evidence-survival
fraction $\rho(m, S_k) = \left(\sum_{i \in S_k} m_i\right) / |S_k|$. Given
thresholds $\tau_{low} < \tau_{high}$, an example is labeled CONFIDENT if
$\min_k \rho(m, S_k) \ge \tau_{high}$, ABSTAIN if $\min_k \rho(m, S_k) <
\tau_{low}$, and DROP (excluded from training) otherwise.[^c1]

The granularity of the span is decisive, and the paper reports the
measurement that shows it: with full supporting paragraphs (~100 tokens)
as $S_k$, $\rho$ averages out — at retention ratio 0.50 every paragraph
keeps roughly half its tokens, so every example falls in the dropped zone
and the per-example label [[entropy]] is 0.000. Narrowing $S_k$ to the
verbatim answer-bearing span (median 3 tokens, 99th percentile 11,
located verbatim in 100% of the MuSiQue pool used) raises the label
entropy to 0.95 at the same retention ratio, which the paper states is
the reason the rest of its construction has signal to fit at all.[^c2]

## Why it matters

This is a computable, mask-only test of whether a piece of context still
*determines* an answer, independent of a model's own confidence — a
candidate operationalisation for stall 7 ("is $|W|$ small enough?") when
the threat to [[sufficient-statistic|sufficiency]] is not missing information but evidence that was
present and then silently removed by a lower system layer (a compressor,
a retrieval cutoff, a context window limit). The paper's own finding that
granularity changes the label entropy from 0.000 to 0.95 is itself the
argument against measuring "how much context survived" in aggregate: a
sufficiency measure has to be taken at the grain of the specific fact a
question needs, not at the grain of the passage that contains it.[^c3]

## Limits

- $\rho$ requires the supporting span $S_k$ to already be known and
  localized in the original context; the paper builds this from a QA
  dataset's own decomposition annotations (MuSiQue's
  `question_decomposition` field) and states no method for finding tight
  spans when no such annotation exists.[^c4]
- The thresholds $\tau_{low}=0.3,\ \tau_{high}=0.8$ are set a priori for
  this dataset and compressor family; the paper does not test whether they
  transfer to other evidence-truncation mechanisms.[^c5]
- Multi-hop questions with more than one supporting span use the *minimum*
  of $\rho$ across spans (the weakest-link reading); the paper does not
  test whether a different aggregation (e.g. requiring only a majority of
  spans) changes which examples are CONFIDENT.[^c6]

## Related

[[compression-aware-abstention]] · [[abstention]] · [[sufficient-statistic]]

[^c1]: khodabandehlou-2026 — "ρ(m, Sk ) = . (1) |Sk |"
[^c2]: khodabandehlou-2026 — "at r = 0.50 every paragraph keeps roughly half its tokens, so every example falls in the uncertain zone and is dropped (label entropy 0.000, vs 0.95 for tight spans; Appendix A)."
[^c3]: khodabandehlou-2026 — "The pivot to verbatim answer spans is the reason the rest of the paper has signal to fit."
[^c4]: khodabandehlou-2026 — "the question_decomposition field gives each single-hop sub-answer as a short atomic string"
[^c5]: khodabandehlou-2026 — "assigns y via Eq. 2 with thresholds τlow = 0.3, τhigh = 0.8 (set a priori)"
[^c6]: khodabandehlou-2026 — "mink ρ(m, Sk ) ≥ τhigh"
