---
description: "A dedicated agent that lists missing diagnostic evidence, ranked by estimated diagnostic utility, for the question generator to prioritize — helpful only inside the full system, harmful alone."
aliases: ["evidence gap agent", "evidence-gap finder"]
sources: ["sanghvi-2026"]
---
# Evidence gap agent

> A separate agent whose only job is to name what is still missing, so the
> question generator prioritizes closing that gap instead of asking whatever
> comes to mind next.

## Definition / Mechanism

"The Evidence Gap agent... identif[ies] information still needed to support
or reject a diagnosis. It identifies: (i) diagnosis-specific gaps that help
differentiate current candidate diagnoses, and (ii) general gaps covering
broadly informative clinical details (such as vitals, lab results)." Before
a fixed turn threshold, when candidate diagnoses are not yet used, it reports
general gaps only; after that threshold it reports both types, and "the
Question agent is prompted to prioritize these gaps when forming the next
query."[^c1]

## Why it matters

Added on its own, the agent does not help: in the paper's four-agent
ablation (Summarizer, Specialist Ensemble, Knowledge Graph, Evidence Gap,
each added individually to the same base system) it is one of "the other
three agents [that] each reduce accuracy by 1-2 points when added in
isolation. Even though the sum of the four individual gains is negative, the
full system outperforms every partial configuration." As the paper notes,
"A standard incremental ablation study would have incorrectly rejected
these components."[^c2]

## Limits

- Measured only as an addition on top of the paper's best flow variant
  ([[differential-questioning|differential questioning]] switched on at turn 10); its isolated effect
  was not tested against the plain baseline, so the reported drop is
  relative to an already-modified system, not a from-scratch comparison.
- Single benchmark and domain (MeDxBench, medical diagnosis); whether
  "gaps ranked by estimated diagnostic utility" are themselves accurate is
  not evaluated against any ground truth — only the resulting diagnostic
  accuracy is.
- The negative solo effect and the positive combined effect come from the
  same GPT-4o run family; cross-model transfer was reported for the full
  combined system only, not for this agent's isolated or paired effects.

## Related

[[differential-questioning]] · [[expected-information-gain]] · [[value-of-information]] · [[adaptive-submodularity]]

[^c1]: sanghvi-2026 — "The Evidence Gap agent follows this principle, identifying information still needed to support or reject a diagnosis. It identifies: (i) diagnosis-specific gaps that help differentiate current candidate diagnoses, and (ii) general gaps covering broadly informative clinical details (such as vitals, lab results)."
[^c2]: sanghvi-2026 — "the other three agents each reduce accuracy by 1-2 points when added in isolation. Even though the sum of the four individual gains is negative, the full system outperforms every partial configuration."
