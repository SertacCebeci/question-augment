---
description: "A query reformulation method's effectiveness ranking against rival methods is not fixed: it shifts with the generating LLM's backbone and parameter scale, not only with the dataset."
aliases: ["rank instability across LLM backbone", "LLM x method interaction"]
sources: ["arxiv-2604-27421"]
---
# Reformulation method ranking instability

> "Method A outperforms method B" is a claim about a specific generator, not about reformulation in general.

## Definition / Mechanism

Bigdeli et al. (2026) run ten LLM-based query
reformulation methods through two architectural lineages (GPT-4.1,
Qwen2.5) at two parameter scales each (four backbones total) under
identical decoding settings, then ask whether one method's rank
relative to the others is stable across backbones — not whether its
absolute score is. Ranking each method by nDCG@10 within a fixed
backbone and comparing across backbones with Spearman correlation:
"GPT 4.1 and GPT 4.1 nano show low rank correlation (𝜌 = 0.35–0.52,
ns), while Qwen 72B and 7B maintain stable rankings (𝜌 = 0.77–0.86,
𝑝 < 0.01)."[^c1]

Decomposing observed nDCG@10 variance into an LLM main effect, a
method main effect and their interaction shows the interaction is not
noise-sized: "LLM × method interaction explains 16–22% of total
variance, comparable to LLM main effects (8–23%)." Method choice
still explains the most variance (54.5–75.7%), but "the interaction
term remains substantial (16.0–22.2%), indicating that relative
conclusions about methods are not fully portable across LLM
configurations even when overall LLM quality differs only modestly."
[^c2][^c2.2]

The instability is not simply "bigger model, more stable": "scale
effects are method dependent: some strategies become more stable with
larger models while others become less stable, reinforcing our
broader finding that improvements from increasing LLM capacity are
not uniform across reformulation approaches or domains."[^c3]

## Why it matters

Comparative claims in the reformulation literature ("method A beats
method B") are usually reported for one generator. This note
establishes that such a claim is scoped to that generator: the same
comparison run through a smaller or differently-trained model can
reverse. For anyone deriving a general way of reformulating a
question — not just reproducing one paper's leaderboard — the
implication is that a reformulation strategy's *relative* value must
be validated across more than one generator before it is treated as a
property of the strategy rather than of the strategy-generator pair.
Reporting only a mean effectiveness score across datasets also hides
this: "the same average score can arise from a reliable generalist
(moderate ranks everywhere) or an unstable specialist (very high on
some datasets and very low on others)."

## Limits

Only four backbones (two lineages × two scales) are tested; whether
the instability is a property of scale, of training recipe, or of
some other axis the two lineages happen to differ on is not
separated. The correlations are computed within two benchmarks
(DL-HARD, BEIR average), not the full nine-dataset suite, so the
reported 𝜌 ranges may not hold on every dataset individually. `[?]` —
unverified: the paper offers one explanation for GPT-4.1 nano's
weaker correlations ("relatively small and less capable, leading to
noisier reformulations") without a direct measurement of reformulation
noise to support it.

## Related

- [[cross-retriever-reformulation-gain]] — the companion finding from
  the same study: gains are also conditional on the retrieval
  paradigm, a second axis this note holds fixed while varying the
  backbone.
- [[reformulation-pattern-library]] — a reformulation method whose
  claimed gain over baselines is itself reported under one backbone;
  this note names the open question of whether that ranking would
  survive a backbone swap.
- [[compcqr]] — a training-free reformulation method whose head-to-head
  comparisons against LLM4CS, CHIQ-Fusion and AdaRewriter are likewise
  reported for one generator each.

[^c1]: arxiv-2604-27421 — "GPT 4.1 and GPT 4.1 nano show low rank correlation (𝜌 = 0.35–0.52, ns), while Qwen 72B and 7B maintain stable rankings (𝜌 = 0.77–0.86, 𝑝 < 0.01)."
[^c2]: arxiv-2604-27421 — "LLM × method interaction explains 16–22% of total variance, comparable to LLM main effects (8–23%)."
[^c2.2]: arxiv-2604-27421 — "the interaction term remains substantial (16.0–22.2%), indicating that relative conclusions about methods are not fully portable across LLM configurations even when overall LLM quality differs only modestly."
[^c3]: arxiv-2604-27421 — "scale effects are method dependent: some strategies become more stable with larger models while others become less stable, reinforcing our broader finding that improvements from increasing LLM capacity are not uniform across reformulation approaches or domains."
