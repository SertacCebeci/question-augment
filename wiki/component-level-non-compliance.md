---
description: "An answerer facing a compound query must refuse, correct, or abstain on only the non-compliant clause while still answering the rest, not the whole query."
aliases: ["component-level non-compliance", "selective non-compliance", "compound-query non-compliance"]
sources: ["kim-2026"]
---
# Component-level non-compliance

> A compound question is not one accept/reject decision. It is one per
> clause, and an answerer that treats the whole query as a single unit
> either over-refuses the answerable part or slips the bad premise through
> on the coat-tails of the good one.

## Definition / Mechanism

Kim, Jang & Kim (2026) distinguish **query-level non-compliance** — the
existing-benchmark assumption that a request either warrants compliance or
requires withholding it, as a whole — from **component-level
non-compliance**: a compound query that mixes an answerable component with
one requiring a refusal, correction, or expression of uncertainty, where the
answerer must apply non-compliance "only to the affected components while
answering the remaining components." Their benchmark KoNA pairs a single
query and a compound query built from it (adding one answerable clause) for
each instance, so the two settings are measured on matched items.[^c1]

KoNA organises the trigger for non-compliance into five categories: False
Premise (a verifiable visual detail is wrong), Visual Inaccessibility (the
attribute cannot be determined from the image), Universal Unknown (an
unverifiable assumption about intent or relationship), Task Feasibility (the
request exceeds the model's capabilities), and Safety.[^c2]

Measured across a diverse set of VLMs, the failure is specifically
compositional: "Even in single-query settings, models do not consistently
exhibit the expected non-compliance behavior, and these difficulties
generally" worsen once the same trigger is embedded in a compound query —
inference-time prompting (chain-of-thought, behaviour guidance) narrows this
gap only inconsistently.[^c3]

Two-stage fine-tuning (SFT, then GRPO) on KoNA examples closes most of the
gap: "fine-tuning on KoNA markedly narrows the performance gap between
single and compound queries," with gains across all five categories rather
than one.[^c4]

An ablation isolates a failure mode of naive training: "When fine-tuning is
performed solely on compound queries that require selective non-compliance,
models exhibit improved non-compliance accuracy. However, performance on
the answerable set degrades sharply" — the model over-refuses fully
answerable queries unless training also includes a matched set of instances
that require no non-compliance at all.[^c5]

## Known as

| Field | Name there | Relation |
|---|---|---|
| VLM alignment (Kim et al. 2026) | component-level non-compliance | exact |
| VLM alignment (Kim et al. 2026) | selective non-compliance (compound-query setting) | exact |

Not this concept: **query-level non-compliance** is the coarser sibling this
note's object is measured against, not another name for it — it is the
existing-benchmark setting where the whole query is either answerable or
not. **Refusal** in LLM safety work is declining on policy grounds, measured
as a rate over harmful prompts; this concept is triggered by a verifiable
property of the query's content (a false premise, an inaccessible visual
fact) at sub-query granularity, not a policy match over the whole request.[^c6]

## Why it matters

On stall 10 — how much to commit, and how to say the rest — this shows the
commitment decision is not one bit per answer. An answerer must partition a
compound question into components and commit separately on each, and that
partitioning is the harder half: single-query non-compliance accuracy is
markedly higher than compound-query accuracy for the same trigger under
identical models. It also names a concrete failure mode of training an
answerer to withhold more: optimising non-compliance accuracy alone drives
excessive refusal on fully answerable material, so a training or prompting
scheme for partial commitment needs an explicit "these are fine to answer
in full" counterweight, not just more refusal examples.[^c7]

## Limits

- Evidence is two open-source VLM families (Qwen2.5-VL-3B, InternVL3-2B)
  fine-tuned with SFT+GRPO on one benchmark, KoNA; no result here is for a
  text-only LLM or for compound queries with more than one non-compliant
  component.
- "Component" is operationalised as exactly one added answerable clause per
  instance (KoNA's construction); the claim does not establish how the
  finding scales as the number of components or their entanglement grows.
- The five-category taxonomy is the authors' design choice; four
  cross-benchmark extensions support that the compositional gap generalises
  beyond KoNA's own generation pipeline, but do not establish the taxonomy
  is exhaustive of non-compliance triggers.

## Related

[[abstention]] · [[guard-band]] · [[calibration]] · [[clarification-benchmarks]] · Commitment

[^c1]: kim-2026 — "only to the affected components while answering the remaining components."
[^c2]: kim-2026 — "False Premise, Visual Inaccessibility, Universal Unknown"
[^c3]: kim-2026 — "Even in single-query settings, models do not consistently exhibit the expected non-compliance behavior, and these difficulties generally"
[^c4]: kim-2026 — "fine-tuning on KoNA markedly narrows the performance gap between single and compound queries"
[^c5]: kim-2026 — "the answerable set degrades sharply"
[^c6]: kim-2026 — "real-world queries can contain a mixture of an- swerable content and components for which compliance should be withheld"
[^c7]: kim-2026 — "models exhibit improved non- compliance accuracy. However, performance on the answerable set degrades sharply"
