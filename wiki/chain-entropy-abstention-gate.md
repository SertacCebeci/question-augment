---
description: "A two-stage selective-prediction gate for thinking-mode VLMs — refuse unresolved chains, then refuse the longest remaining chains — raised POPE accuracy from 71.0% to 93.8% at 62.7% coverage."
aliases: ["chain gate", "abstention gate", "chain length gate"]
sources: ["singal-2026"]
---
# Chain-entropy abstention gate

> A [[abstention|selective-prediction]] rule for thinking-mode VLMs that first refuses samples whose chain never resolves to a committed answer, then refuses the longest remaining chains — using signals already produced by the forward pass, at no extra inference cost.

## Definition / Mechanism

Built on [[thinking-chain-entropy]], the gate is staged: first refuse
samples the model leaves "unclear" (no committed yes/no answer extracted
from the chain), then progressively refuse the top-quantile of chain
length $L$ among the remaining committed predictions. On POPE adversarial
with Qwen3-VL-8B-Thinking: "None (baseline) 100.0% ... Refuse unclear 77.9% ... +top 20% chain refused 62.7% ... +top 30% chain refused 54.9%" gives accuracy "71.0% ... 91.1% ... 93.8% ... 94.2%" at those coverage levels respectively.[^c1]

## Why it matters

"We demonstrate a practical abstention gate requiring no additional inference: refusing unclear samples and long-chain committed predictions raises accuracy from 71.0% to 93.8% at 62.7% coverage on POPE."[^c2]

This is the deployable form of chain entropy/length as a signal: a
coverage–accuracy trade rather than a raw AUROC, and the paper is explicit
that it only closes, not eliminates, the gap to a non-thinking model's
answer-[[entropy]] gate on the same task: "the instruct model using answer entropy achieves 96.7% at matched coverage. The chain gate thus closes but does not eliminate the practical gap introduced by thinking-mode abstention."[^c3]

The abstentions the gate acts on are not evenly distributed, and the
failure mode differs by benchmark: "Abstention rates are 22.1% on POPE and 12.6% on HallusionBench, with consistent asymmetry toward absent-object queries" — on POPE most abstentions are long chains that never resolve, on HallusionBench most abstentions produce no chain at all.[^c4]

## Limits

The comparison holds only when a thinking-mode VLM is already the
deployment choice: "the instruct model (blue) is not a deployment alternative when a thinking-mode VLM is already in use; its curve is a reference ceiling only."[^c5]

The gate is tuned and reported on one model (Qwen3-VL-8B-Thinking) on one
benchmark's headline number (POPE); the HallusionBench curve uses
different thresholds, and no held-out replication of the 71.0%→93.8%
figure exists outside this paper.

## Related

[[thinking-chain-entropy]] · [[abstention]] · [[entropy-threshold-clarification-trigger]]

[^c1]: singal-2026
[^c2]: singal-2026 — "We demonstrate a practical abstention gate requiring no additional inference: refusing unclear samples and long-chain committed predictions raises accuracy from 71.0% to 93.8% at 62.7% coverage on POPE."
[^c3]: singal-2026 — "the instruct model using answer entropy achieves 96.7% at matched coverage. The chain gate thus closes but does not eliminate the practical gap introduced by thinking-mode abstention."
[^c4]: singal-2026 — "Abstention rates are 22.1% on POPE and 12.6% on HallusionBench, with consistent asymmetry toward absent-object queries"
[^c5]: singal-2026 — "the instruct model (blue) is not a deployment alternative when a thinking-mode VLM is already in use; its curve is a reference ceiling only."
