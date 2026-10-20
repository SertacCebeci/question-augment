---
description: "LLM-stated 95% credible intervals cover the truth only 9-44% of the time regardless of reasoning effort; only model size and conformal recalibration close the gap."
aliases: ["Bayesian elicitation with LLMs", "reasoning-effort calibration invariance"]
sources: ["arxiv-2604-01896"]
---
# Credible-interval undercoverage in LLM elicitation

> Ask nine frontier LLMs for a 95% interval and, on average, the truth lands
> inside it less than half the time it should — and turning up the "thinking"
> dial does not fix that.

## Definition / Mechanism

Hobor & al. (2026) query nine LLMs (three OpenAI, three
Anthropic, two Google, one DeepSeek, plus two non-reasoning controls) as
[[bayesian-experimental-design|Bayesian elicitation]] assistants: each is
asked for a point estimate and a 95% credible interval on a derived
population statistic (Big Five traits, NHANES health prevalence, NCD-RisC
country health metrics, Glassdoor salaries), at low, medium and high
vendor-set reasoning effort. Empirical coverage — the fraction of questions
where the stated interval actually contains the ground truth — is the
measure of whether the stated uncertainty is honest, independent of whether
the point estimate is accurate.[^c1]

Across every model-effort combination, coverage of the nominally 95%
intervals ranges from 9% to 44%: models express far more confidence than
their accuracy supports, a systematic overconfidence gap present even in the
non-reasoning control models.[^c2]

Applying split conformal prediction — computing a normalized nonconformity
score on a held-out calibration split per model/effort/dataset group and
widening test-set intervals by the resulting quantile (typically 2-5x) —
recovers near-nominal coverage for most groups, confirming the gap is a
correctable, systematic bias in interval width rather than noise.[^c3]

Reasoning effort does not fix it. Pooled across the nine reasoning-capable
models, neither log-likelihood nor coverage varies significantly with effort
level (coverage: $H=2.8$, $p=0.25$); only interval *width* grows with effort,
so higher effort makes intervals wider without making them better
calibrated. Four of nine models show a per-model effort effect, but the
direction is inconsistent across them. What does move accuracy and
coverage together is model capability: within the Claude family, Opus beats
Haiku on both log-likelihood (134 vs. 498, $p<0.001$) and coverage (42.6% vs.
9.5%, $p<0.001$).[^c5]

## Why it matters

A stated interval is a commitment about how much of the space the answerer
is willing to rule out. This work measures that commitment against ground
truth at scale and finds it is broken by a factor of 2-10x in the direction
of overconfidence, and — contrary to the intuition that more deliberation
means better-calibrated uncertainty — the knob most practitioners reach for
first (reasoning effort) does not move the number that matters. Model choice
and an external, distribution-free recalibration step do.[^c6]

## Limits

- Coverage is measured only against the model's *stated* interval; models
  with higher invalid/refusal rates answer a systematically easier subset of
  questions, which can inflate their apparent accuracy (a selection-bias
  caveat the authors name explicitly).[^c7]
- Conformal recalibration needs a labelled calibration set of at least 15
  points per model-domain-effort group; groups below that are flagged
  statistically insufficient, and the method gives no online, zero-shot fix.[^c8]
- The tool-augmented (web-search) experiment is preliminary — 25 questions
  per dataset, four models — and its finding (search degrades already-strong
  models, helps only the weakest) is not the paper's central result.[^c9]
- "Reasoning effort" is a vendor-controlled token/parameter budget, not a
  controlled manipulation of internal computation; for DeepSeek-Reasoner at
  low effort the budget is exhausted before an answer forms (88.8% invalid),
  confounding effort with response validity for that model.[^c10]

## Related

[[calibration]] · [[conformal-prediction]] · [[confidence-interval-calibration]] · [[bayesian-experimental-design]] · [[layered-reasoning-fallback]] · [[hard-easy-effect]]

[^c1]: arxiv-2604-01896 — "Coverage. We compute empirical coverage as the fraction of questions where the ground truth falls within the predicted interval:"
[^c2]: arxiv-2604-01896 — "Fig. 2 reveals the central finding of this study: all models exhibit severe under-coverage in their raw 95% credible intervals. Across all model–effort combinations, empirical coverage ranges from 9% to 44%, far below the nominal 95% target."
[^c3]: arxiv-2604-01896 — "After applying normalized residual conformal prediction, coverage improves substantially and approaches the 95% target for most model–effort–dataset combinations."
[^c5]: arxiv-2604-01896 — "Within-family comparisons confirm that model capability is the primary driver. For Claude (Opus vs. Haiku), the larger model wins decisively: lower NLL (134 vs. 498, p < 0.001) and higher coverage (42.6% vs. 9.5%,"
[^c6]: arxiv-2604-01896 — "Without recalibration, LLM-generated uncertainty intervals are unreliable for decision-making. Practitioners should prefer larger models and apply conformal calibration (Table II)."
[^c7]: arxiv-2604-01896 — "First, models with higher refusal rates may introduce selection bias; models that respond only to easier questions will appear artificially accurate."
[^c8]: arxiv-2604-01896 — "However, CP requires a calibration set of labeled examples per model–domain group (≥15 points), limiting its applicability in zero-shot scenarios."
[^c9]: arxiv-2604-01896 — "Third, the tool experiment is preliminary (n = 25 per dataset, four models)."
[^c10]: arxiv-2604-01896 — "DeepSeek-Reasoner exhibits a dramatic shift from 88.8% invalid at low effort to 0% at high effort due to thinking budget exhaustion: at 2,000 tokens, the model exhausts its budget on internal reasoning and produces empty outputs."
