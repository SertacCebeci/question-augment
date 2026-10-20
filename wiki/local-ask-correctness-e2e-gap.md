---
description: "Per-turn clarification and safe-abstention diagnostics exceed 95% across nine LLM agents while pooled end-to-end task success stays at 82.6%, and the two rankings diverge."
aliases: ["local ask correctness / E2E success gap", "clarification-abstention diagnostic saturation"]
sources: ["qin-2026"]
---
# Local ask-correctness / end-to-end gap

> Getting the "ask or act" decision right at each turn does not mean the
> workflow finishes right: on StructureClaw-Bench, per-turn clarification
> and [[abstention]] accuracy nearly saturate while end-to-end success stays
> well below it.

## Definition / Mechanism

On StructureClaw-Bench's 50 interactive-robustness scenarios (text,
English/Chinese, requiring an agent to clarify, recover, or safely decline
across multi-turn, [[recovery-postulate|recovery]], unsupported and static-analysis conditions),
Qin, Gu, Jiang et al. (2026) report: "Interactive robustness
reaches 82.6% pooled E2E Success, with model rates from 72.0% to 90.0%...
Stable success is 72.4%, and each clarification or safe-abstention
diagnostic exceeds 95%."[^c1]

The ranking by the two metrics diverges: "Claude Opus 4.8 achieves perfect
clarification and abstention diagnostics but not the highest E2E Success,
indicating that interactive [[calibration|reliability]] also requires maintaining artifact
state consistency and completing downstream transitions." GLM-5.2 has the
highest E2E success (90.0%) among the nine tested configurations.[^c2]

## Why it matters

For stall 2, this is a measured limit on what a correct selection decision
buys: an agent can identify, at the point of decision, that it should ask
or should not proceed — the per-turn diagnostic scores this near-perfectly
— and the overall task can still fail because later steps (revalidating an
artifact, completing a downstream transition) break independently. A
selection criterion evaluated only at the moment of the ask/act choice
therefore measures a necessary but not sufficient condition for the
workflow it is embedded in.

## Limits

- Measured on one domain (structural-engineering agent workflows) and nine
  text-agent configurations; the paper does not test whether the same
  decoupling between local diagnostic accuracy and pooled E2E success holds
  outside this artifact-centered setting.
- "Semantic evaluation is the most common first failed stage... these
  labels localize the first inconsistent handoff under the benchmark
  rules; they do not causally explain model reasoning" — the source does
  not attribute *why* correct local clarification/abstention fails to
  propagate to E2E success, only that it does.
- Single-attempt E2E success is a strict, all-assertions-pass measure;
  the 82.6%/95%+ contrast is a property of this scoring choice and would
  narrow under a partial-credit metric.

## Related

[[conjunctive-negative-evidence-gating]] · Selection · [[agentabstain-paired-benchmark]] · [[defect-localization]]

[^c1]: qin-2026
[^c2]: qin-2026 — "Claude Opus 4.8 achieves perfect clarification and abstention diagnostics but not the highest E2E Success, indicating that interactive reliability also requires maintaining artifact state consistency and completing downstream transitions."
