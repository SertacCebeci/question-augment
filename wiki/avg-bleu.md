---
description: "A sampling-based calibration score for open-ended VQA that averages likelihood-weighted pairwise BLEU similarity among sampled answers to gate a selective-answering trigger."
aliases: ["AVG BLEU", "Avg BLEU"]
sources: ["eisenschlos-2024"]
---
# AVG BLEU

> A confidence score for a visual question-answering system built from
> nothing but the model's own sampled answers to itself — no ground truth,
> no NLI model, just BLEU.

## Definition / Mechanism

Eisenschlos et al. (2024) frame selective VQA as attaching a scoring
function $s(q,a)$ to every question–answer pair; the system answers when
$s(q,a) > \tau$ and abstains otherwise.[^c1]

Against the existing likelihood
score and two sampling-based scores from text QA (variation-ratio
*Repetition* and *Diversity*, the fraction of unique samples), the authors
propose AVG BLEU: sample $k$ distinct answers, weight each by its own
likelihood $p(a_i\mid q)$, and average the pairwise BLEU similarity between
every pair of sampled answers — an estimate of how tightly the sampled
answer set clusters, without any embedding model or entailment classifier.[^c2]

## Why it matters

Across two VQA answerability benchmarks (VizWiz-VQA, UNK-VQA) and five
in-context-learning models, the authors "find that likelihood based scoring
is better for LMMs than LLMs, without a clear winner" — the ranking of
calibration methods for a visually-grounded model is not the ranking that
holds for a text-only one, so a calibration method validated on text QA does
not transfer to VQA unchanged.[^c3]
AVG BLEU is reported to work "well across the board, matching or improving
the best metric in most cases" across AUC, coverage-at-accuracy and (after
post-hoc rescaling) ECE — the one score that does not need to know in
advance whether the model in front of it is visually grounded.[^c4]

## Transfer

| | |
|---|---|
| **In its home field** | BLEU (Papineni et al., 2002): n-gram precision of a candidate translation against one or more fixed reference translations, in machine-translation evaluation |
| **Here** | no reference exists; BLEU instead scores every sampled answer against every other sampled answer from the same model, as a dispersion estimate for calibration |
| **What survives** | the metric's negligible compute cost and its usable signal: the paper finds trained alternatives (BEM, BLEURT) give only marginal gains over it at higher latency |
| **What does not** | the reference-based comparison BLEU was built for, and its known blindness to legitimate paraphrase — which is why the authors tested embedding-based replacements at all |

[^c5]

## Limits

- The comparison rests on five specific models (LLaVA, Flamingo, BLIP-2,
  PaLM 2, Falcon) over two answerability benchmarks in an in-context-learning
  setting; the paper's own Limitations section notes "no other VQA datasets
  to our knowledge account for unanswerable questions in the same rich
  manner," so the ranking of methods is not shown to generalise beyond this
  setup.[^c6]
- AVG BLEU is the weakest of the four scores on ECE specifically — the
  paper notes this "can be fixed post-hoc by re-scaling," which is a
  correction applied after the fact, not evidence the raw score is
  probabilistically calibrated in the sense of [[calibration]].
- The score needs $k$ sampled answers and their per-answer likelihoods, so
  it is not usable against a black-box answerer that exposes neither.
- "Why are LMMs better calibrated" is explicitly speculation in the source
  ("We leave further experiments in this direction to future work") — not
  a claim this note repeats as established.

## Related

[[calibration]] · [[abstention]] · [[semantic-entropy]] · Commitment

[^c1]: eisenschlos-2024 — "The score can be compared with a threshold τ so that the system answers—aka trig-gers—when s(q, a) > τ or abstains otherwise."
[^c2]: eisenschlos-2024 — "We propose an approach to grad-ing the similarity among model answers that re-lies on averaging a measure of semantic similar-ity."
[^c3]: eisenschlos-2024 — "find that likelihood based scoring is bet-ter for LMMs than LLMs, without a clear winner."
[^c4]: eisenschlos-2024 — "AVG BLEU works well across the board, matching or improving the best metric in most cases."
[^c5]: eisenschlos-2024 — "Both BLEURT and BEM give marginal gains for coverage at the cost of increased latency."
[^c6]: eisenschlos-2024 — "This study was conducted using several models over two datasets, which might limit the generaliza-tion of its conclusions. No other VQA datasets to our knowledge account for unanswerable questions in the same rich manner."
