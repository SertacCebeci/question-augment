---
description: "The accuracy cost of asking for a schema is not fixed: models with spare capacity absorb it, models near their limit lose 28–36pp, by truncation and by a non-truncation competition."
aliases: ["capacity competition", "format cost scales with capacity", "structured output as capacity demand"]
sources: ["doi-10-48550-arxiv-2606-09410"]
---
# Capacity-dependent format tax

The [[format-restriction-effect]] is usually reported as a uniform tax on
reasoning. Fan (2026) argues that the tax is an interaction: the same JSON
schema, on the same task, costs nothing for a model with headroom and a great
deal for a model operating near its limit. "The key variable is not the format
but the model’s spare capacity."[^c1] Format compliance and reasoning are
said to compete for one limited generation capacity.

## What was measured

Four closed models (two tiers, two providers) on math, logic and knowledge
benchmarks, with four output conditions including an information-matched prose
control, so that a longer format-requesting prompt is not the explanation.

- **Strong model, no cost.** Sonnet 4.6 scores about 89% on MATH-Hard under
  JSON, prose and chain-of-thought alike.[^c2]
- **Weak model, large cost.** Haiku 4.5 falls from 88.7% to 52.5% (−36.2pp)
  under heavy JSON on MATH-Hard.[^c3] The prose prompt matched to the JSON
  instruction in information gave 80.7% for Haiku against 52.5% with JSON,
  with no parse failures in any condition, which ties the loss to
  doing reasoning and schema-compliant serialization at once rather than to
  prompt length or extraction.[^c4]
- **Frontier model, cost at the boundary.** On AIME, Opus 4.7 drops from
  96.2% to 91.0% under JSON.[^c5] The author reads the apparent immunity of
  frontier models as evaluation inside their comfort zone.
- **Complexity gradient.** Among schemas that elicit reasoning, weaker models
  degrade monotonically as schema complexity rises.[^c6]

## Two mechanisms

Under heavy JSON with a 2048-token cap, Haiku hits the limit on 49% of
responses, Sonnet on 5%, GPT-4o-mini on 0%.[^c7] Raising Haiku's budget to
8192 tokens "recovers 87% of" the gap (52.5% to 84.0%), so truncation is its
dominant proximate mechanism.[^c8] GPT-4o-mini shows no such recovery (34%
to 36% at 8192, zero truncation at both) while still losing 28pp, which the
paper reads as "a distinct non-truncation capacity cost".[^c9] Truncation is
"one mechanism" of capacity competition, not the only one.[^c10]

## Test of the mechanism

A delayed-structure condition (reason freely, then reformat to JSON) recovers
most of the lost accuracy, a 3-run mean of 80–87% for the capacity-limited
models.[^c11] This is the same lever as [[reasoning-formatting-decoupling]],
now with a capacity reading: the loss disappears when reasoning is not
required to share the generation with serialization. Read this as consistent
with, not proof of, the competition account; the paper offers no
internal-representation evidence.

## Limits

- "Capacity" is operationalized as baseline CoT accuracy on MATH-Hard; the
  boundary-zone prediction (largest effects at 50–70% capacity) could not be
  tested on Opus because no public math benchmark places it there.[^c12]
- Schema complexity changes prompt length, field count and nesting together;
  the paper says each factor is not isolated.
- Strongest effects are on math; the paper notes that competition "may manifest
  differently" on generation or open-ended tasks.[^c13]
- Several cells are single-run; Opus cells are exploratory.[^c14] A replication
  audit saw Sonnet's heavy-schema accuracy fall to 60–63% from 93%, attributed
  to backend drift, so absolute numbers on closed APIs are unstable; the
  paper uses within-batch comparisons.[^c15]
- Closed models only, and no grammar-constrained decoding, so the result does
  not speak to [[constrained-decoding]].
- The competition mechanism for GPT-4o-mini is an inference from the absence
  of truncation recovery, not a measured internal quantity.

## Related

- [[format-restriction-effect]] — the uniform-tax framing this note qualifies as a capacity interaction
- [[reasoning-formatting-decoupling]] — the delayed-structure remedy, here tested as a mechanism probe
- [[structured-output]] — the family of ways to obtain a schema-shaped reply
- [[constrained-decoding]] — untested here; token-level enforcement may behave differently

[^c1]: doi-10-48550-arxiv-2606-09410 — "The key variable is not the format but the model’s spare capacity."
[^c2]: doi-10-48550-arxiv-2606-09410 — "prose, and chain-of-thought on MATH-Hard (∼89%). But"
[^c3]: doi-10-48550-arxiv-2606-09410 — "Haiku drops from 88.7% to 52.5% (−36.2pp, p < 0.0001)"
[^c4]: doi-10-48550-arxiv-2606-09410 — "instruction—produced 80.7% accuracy for Haiku vs."
[^c5]: doi-10-48550-arxiv-2606-09410 — "from 96.2% to 91.0% under JSON"
[^c6]: doi-10-48550-arxiv-2606-09410 — "weaker models show monotonic degradation with increasing schema complexity."
[^c7]: doi-10-48550-arxiv-2606-09410 — "Under heavy JSON with max_tokens=2048, Haiku hits the token limit on"
[^c8]: doi-10-48550-arxiv-2606-09410 — "Increasing the budget from 2048 to 8192 recovers 87% of"
[^c9]: doi-10-48550-arxiv-2606-09410 — "consistent with a distinct non-truncation capacity cost."
[^c10]: doi-10-48550-arxiv-2606-09410 — "demonstrating that truncation is one mechanism"
[^c11]: doi-10-48550-arxiv-2606-09410 — "recovers most of the lost accuracy (3-run mean: 80–87%),"
[^c12]: doi-10-48550-arxiv-2606-09410 — "places Opus in the 50–70% capacity boundary zone where"
[^c13]: doi-10-48550-arxiv-2606-09410 — "Capacity competition may manifest differently"
[^c14]: doi-10-48550-arxiv-2606-09410 — "Opus cells are exploratory extensions."
[^c15]: doi-10-48550-arxiv-2606-09410 — "suggesting backend drift rather than a format effect."
