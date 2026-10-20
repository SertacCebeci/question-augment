---
description: "Capping assertion strength by how a claim was obtained (parametric, retrieved, inferred, told) cuts confident falsehoods; on the measured model most of that cut came from confidence gating."
aliases: ["provenance-gated expression", "source-capped assertion", "provenance gating table"]
sources: ["doi-10-48550-arxiv-2609-26035"]
---
# Provenance-gated assertion

A claim is not voiced on its confidence alone. The layer tags each claim with
the resolution path that produced it: model parameters, a retrieval store, a
one-step derivation rule, or a user statement made in the session. A frozen
table then maps the pair (provenance, confidence band) to one of four
expression categories, ordered decline < hedge-low < hedge-high < assert. The
tag is set by pipeline instrumentation, recording which path answered, and is
"never by a classifier".[^c2] The confidence is a conservative combination over
two extractors, so that "no single inflated extractor can unlock a strong
assertion",[^c19] and the bands are split "with band edges at 0.40 and 0.75".[^c17]

The table is where the source caps come in. Its design rules, recorded before
any data, include that "inferred claims never reach bare assert", and
told-this-session claims are hedged rather than presented as the agent's own
knowledge.[^c1] Retrieved content "asserts in the high band"; inferred and
told content is held below assert whatever its confidence.[^c3][^c18] So two
claims with the same confidence can get different voices: one the model
retrieved, one it derived by a rule, one the user supplied. The cap is applied
on top of confidence, not in place of it.

What was measured. On a pinned real model (Qwen2.5-0.5B-Instruct), over a
60-fact geography world, with "120 seeded three-session conversations (24 turns
each)" per arm,[^c20] the rate of confidently asserted falsehoods fell from
0.087 under uniform assertion to 0.018 under the full layer.[^c4] The cost was
coverage: "The price is coverage (0.833 vs. 0.925)".[^c5] Accuracy on the
answered subset rose slightly, "when the full layer answers, it is right 92.4%
of the time versus 90.6% for uniform",[^c16] which the paper reads as the
expression policy filtering the model's least reliable content into declines.
The source cap also has an apparent price in discrimination. The threshold-only
arm, which has no provenance caps, had a higher point estimate of discrimination
(0.715 against 0.653, with overlapping intervals), and the paper describes the
caps as imposing "source-caution at an apparent discrimination cost".[^c7]

## Limits

- **The effect is not shown to come from provenance.** The pre-specified
  provenance margin failed narrowly (a gap of 0.0123 against a 0.02 margin).
  Most of the reduction in confident falsehoods is attributed to confidence
  gating with declines, a mechanism the no-provenance arm shares. The paper's
  reading is that the reduction comes from gating "rather than to provenance
  typing as such".[^c6] Whether typed provenance adds anything beyond confidence
  gating remains unmeasured on this model.
- **The caps create a structural tension with calibration.** The table keeps
  inferred and told content below assert, which "guarantees underconfident bins
  under fixed anchors".[^c9] Anchor-based calibration therefore penalises the
  layer for the very behaviour the cap is for. See [[calibration]].
- **The taxonomy is operational.** "The taxonomy is an operational definition,
  not an epistemological claim", and the boundary between parametric and
  inferred content is ambiguous.[^c10] My own inference: a claim the model
  recalls through a chain of reasoning could be filed under either tag, and the
  cap would then depend on the filing.
- **Scale and realism.** Stage A is synthetic, with injected ground truth.
  Stage B is one 0.5B model on 60 facts. The paper's own sensitivity analysis
  concludes that "Sixty distinct facts are simply too few to resolve the" gates
  at the fact level.[^c8] The result is a single-model, single-world measurement.

## Related

- [[calibration]] — the confidence the cap sits on; the anchor-based check
  reads the cap as miscalibration.
- [[abstention]] — decline is the lowest expression category here; a claim the
  table declines is an abstention in the answer, not a separate mechanism.
- [[semantic-entropy]] — the confidence extractors whose choice changes the
  sign of the layer's discrimination.
- [[gated-correction-acceptance]] — the other half of the same layer: what the
  agent does when a user pushes back on a stored claim.

[^c1]: doi-10-48550-arxiv-2609-26035 — "inferred claims never reach bare assert"
[^c2]: doi-10-48550-arxiv-2609-26035 — "never by a classifier"
[^c3]: doi-10-48550-arxiv-2609-26035 — "The gating table caps inferred and told content below assert whatever its confidence"
[^c4]: doi-10-48550-arxiv-2609-26035 — "Confidently-asserted falsehoods drop from 0.087 (uniform) to 0.018 (full)."
[^c5]: doi-10-48550-arxiv-2609-26035 — "The price is coverage (0.833 vs. 0.925)"
[^c6]: doi-10-48550-arxiv-2609-26035 — "rather than to provenance typing as such"
[^c7]: doi-10-48550-arxiv-2609-26035 — "the provenance caps impose source-caution at an apparent discrimination cost"
[^c8]: doi-10-48550-arxiv-2609-26035 — "Sixty distinct facts are simply too few to resolve the"
[^c9]: doi-10-48550-arxiv-2609-26035 — "guarantees underconfident bins under fixed anchors"
[^c10]: doi-10-48550-arxiv-2609-26035 — "The taxonomy is an operational definition, not an epistemological claim"
[^c16]: doi-10-48550-arxiv-2609-26035 — "when the full layer answers, it is right 92.4% of the time versus 90.6% for uniform"
[^c17]: doi-10-48550-arxiv-2609-26035 — "with band edges at 0.40 and 0.75"
[^c18]: doi-10-48550-arxiv-2609-26035 — "retrieved content asserts in the high band"
[^c19]: doi-10-48550-arxiv-2609-26035 — "no single inflated extractor can unlock a strong assertion"
[^c20]: doi-10-48550-arxiv-2609-26035 — "120 seeded three-session conversations (24 turns each)"
