---
description: "A single hard threshold on a multimodal model's own answer confidence gates one crop-and-zoom re-query of the image before it commits to an answer or abstains."
aliases: ["confidence-triggered attention", "visual re-attention"]
sources: ["ding-2026", "arxiv-2512-07564"]
---
# Confidence-triggered visual re-attention

> A scalar confidence the model learned during training decides, at
> inference, whether to look at the image again before answering.

## Definition / Mechanism

Ding et al. (SAVOR) train a multimodal model to emit a scalar answer
confidence $c_{ans}\in[0,1]$ alongside its answer via reinforcement
learning (see [[savor-calibration-abstention-reward]] for the reward that
trains it). At inference, "the same answer confidence triggers a
lightweight visual re-attention step: when confidence is below a
threshold, the model crops the most attended region, queries itself
again, and either returns the revised answer or abstains."[^c1]

The threshold is fixed and reported as "visual re-query when cans < τ ;
we set τ =0.5 by default."[^c2]

The decision is a three-branch rule on two confidence readings: the
initial answer is kept if its confidence already clears $\tau$; otherwise
the model re-queries once, cropping the region its own cross-attention
map weighted most heavily, "where (y1 , c1 ) is the initial output and
(y2 , c2 ) is generated after re-attending to the most relevant visual
region," and keeps the revised answer if its confidence now clears
$\tau$, or abstains ("I am not sure") if it still does not.[^c3]

## Why it matters

The mechanism turns a scalar confidence into a binary control decision —
check once more or commit — without a separate verifier model and without
paying the re-check cost on every prompt, since most rollouts clear
$\tau$ on the first pass. The re-check is targeted: the crop region comes
from the model's own attention map rather than a generic re-decode of the
whole image.

A second paper aims the re-check at claims rather than at the image as a
whole. Sanogo and Ardiccioni score each claim by a weighted sum of four
uncertainty signals and re-examine only the claims above a threshold of 0.3,
with crops of under-attended regions.[^c4] Their ablation replaces that choice
with random refinement, and the text reports a 3.4% drop on POPE-Adversarial;
the authors read it as showing "that blind self-correction is ineffective and
may even introduce noise."[^c5][^c6] So the targeting is a measured part of the
mechanism, not only a saving in compute. See [[multi-signal-uncertainty-gate]].

## Limits

- One re-check at one fixed threshold ($\tau=0.5$); the paper does not
  report how hallucination reduction varies with $\tau$, so the value is
  not shown to be load-bearing rather than incidental.
- The crop is selected from the same model's own cross-attention map: a
  systematically wrong attention pattern could crop the wrong region and
  confirm the original error instead of correcting it; no independent
  check of the crop step's own accuracy is reported.
- Evaluated only on ~8B open multimodal backbones (InternVL3-8B,
  Qwen3-VL-8B) on four hallucination benchmarks; nothing here shows the
  mechanism transfers to text-only agents or to a learned, per-task
  threshold.
- The second paper's claim-level gate is one backbone (Qwen2.5-VL-7B), and
  its weights are unvalidated: "Validating cross-architecture generalization
  remains critical future work."[^c7]

## Related

[[savor-calibration-abstention-reward]] · [[certainty-weighted-grpo-reward]] · [[calibration]] · [[abstention]] · [[multi-signal-uncertainty-gate]]

[^c1]: ding-2026 — "the same answer confidence triggers a lightweight visual re-attention step: when confidence is below a threshold, the model crops the most attended region, queries itself again, and either returns the revised answer or abstains."
[^c2]: ding-2026 — "visual re-query when cans < τ ; we set τ =0.5 by default."
[^c3]: ding-2026 — "where (y1 , c1 ) is the initial output and (y2 , c2 ) is generated after re-attending to the most relevant visual region."
[^c4]: arxiv-2512-07564 — "For claims with high uncertainty (u > τu where τu = 0.3), we perform targeted visual"
[^c5]: arxiv-2512-07564 — "Removing the uncertainty guidance leads to a performance drop of 3.4%, validating"
[^c6]: arxiv-2512-07564 — "that blind self-correction is ineffective and may even introduce noise."
[^c7]: arxiv-2512-07564 — "Validating cross-architecture generalization remains critical future work."
