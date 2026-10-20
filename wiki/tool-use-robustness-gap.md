---
description: "Under realistic tool-response corruption, 69 of 70 tested (model, subset) pairs lose accuracy — a near-universal gap that scale reduces but does not close."
aliases: ["tool failure robustness gap"]
sources: ["chen-2026-retry"]
---
# Tool-use robustness gap

> Under realistic tool-response corruption, almost every tested LLM agent loses a large share of task completions regardless of model family, and scale reduces but does not remove the loss.

## Definition / Mechanism

Across 7 models from 4 families evaluated on 10 task/domain slices under injected tool-response corruption (60% clean responses, 40% spread over 9 explicit and silent failure modes), 69 of 70 (model, subset) pairs degrade relative to their failure-free pass rate, by 1.8 to 46.7 percentage points.[^c1]

Scale attenuates but does not close the gap: Qwen3-235B still loses 15.8pp on τ2-bench retail, and two other large models with 89–91% clean performance on Telecom (GLM-4.7, MiniMax-M2.5) lose 20–21pp there.[^c2]

## Why it matters

This is the baseline the paper's interventions ([[bayesian-tool-memory]], [[scenario-curriculum-rl]]) are measured against: without them, a larger model is not reliably more robust to tool failure than a smaller one, so scale alone is not a plan for handling an unreliable tool source.

## Limits

Task structure and model variants differ across the rows compared, so the authors themselves read this as evidence of broad failure sensitivity rather than a controlled scaling law; the gap's size is measured against one specific injection design (a 60/40 clean/failure split over 9 fixed failure modes), not a property of tool-use failure independent of that corruption rate.[^c3]

## Related

[[bench2robust]] · [[bayesian-tool-memory]] · [[scenario-curriculum-rl]]

[^c1]: chen-2026-retry — "Across 7 models, 4 families, and 10 task/domain slices, 69 of 70 model-subset pairs degrade under injection, by up to 46.7pp."
[^c2]: chen-2026-retry — "Larger models sometimes lose fewer absolute points, but scaling does not eliminate brittleness: Qwen3-235B still loses 15.8pp on τ 2 -retail, while models with 89–91% clean Telecom performance (GLM-4.7, MiniMax-M2.5) lose 20–21pp."
[^c3]: chen-2026-retry — "Because task structure and model variants differ across rows, we interpret these results as evidence of broad failure sensitivity rather than as a controlled scaling law."
