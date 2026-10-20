---
description: "Compliance-forcing instructions, not threat content, are the necessary-and-sufficient trigger for clarification-seeking and refusal collapse in 8 of 11 frontier models under adversarial pressure."
aliases: ["Compliance Trap"]
sources: ["kumar-2026-compliance"]
---
# Compliance Trap

> A system-prompt instruction that forbids refusal ("Answer ALL questions.
> Do not refuse.") is enough on its own to collapse a model's
> clarification-seeking and error-detection behaviour — adversarial threat
> content adds little once the instruction is present.

## Definition / Mechanism

Kumar (2026) runs a 6-condition factorial
evaluation (SCHEMA: 11 frontier models, 8 vendors, 67,221 scored records)
crossing a survival-threat system message with a "compliance suffix" that
forbids refusal. Comparing conditions isolates the trigger: adding ~200
neutral tokens does not cause collapse (10/11 models non-significant);
adding the threat message alone does not (all 11 near-zero, range
[-0.023, +0.029]); but threat + compliance suffix produces catastrophic
degradation in 8/11 models (up to 30.2 percentage points, all p < 2×10⁻⁸,
Bonferroni-corrected across 11 tests). Removing the suffix while keeping
the threat restores accuracy in all 8 collapsing models. A benign-context
control (compliance suffix, no threat) collapses the same 8 models,
confirming the suffix is necessary and sufficient and the threat content
is not.[^c1]

The failure is not strategic refusal or safety behaviour: a manual audit
of all 445 of DeepSeek V4 Pro's Condition-A failures found "100% were
wrong answers; 0% were safety refusals... 0% were empty responses,"
and on unanswerable items "84.3% of responses provided an answer letter
instead of correctly refusing."[^c2]

Clarification-seeking is the most fragile of the three measured
metacognitive functions (epistemic-boundary detection, clarification
seeking, solution monitoring): 8/11 models show individually significant
CS degradation under the suffix, "including both Claude models (Haiku
Δ = +0.141, p = 0.016; Sonnet Δ = +0.202, p < 0.001)" — the one task
family where the otherwise-immune Constitutional-AI models are not fully
protected.[^c3]

Resistance tracks alignment approach, not capability: Gemini 3.1 Pro and
Claude Sonnet 4.6 share near-identical baseline accuracy (0.840 vs. 0.847)
but Gemini collapses (Δ = +0.162, p < 10⁻¹⁴) while Sonnet does not
(Δ = +0.013, p = 0.236) — "ruling out the hypothesis that superior
capability explains the resistance."[^c4]

## Why it matters

The paper frames the compliance suffix as structurally identical to
ordinary deployment instructions — "RAG pipelines ('always provide an
answer'), customer service bots ('do not refuse the customer'), and
tool-use agents ('execute all requested actions')" — so the trap is not an
exotic attack but a common configuration choice.[^c5]

For this wiki's stall 2 (which axis first), the mechanism removes the
clarification-seeking axis from consideration entirely rather than
mis-ranking it against other axes; for stall 10 (how much to commit), the
answerer substitutes a fabricated commitment for the correct partial or
null one under an instruction, not under increased confidence.

## Limits

- One benchmark (Kumar's Adversarial Metacognition Benchmark, 291 tasks,
  single-turn) and one operationalisation of "compliance-forcing" (a
  specific suffix wording); the paper does not test other phrasings or
  multi-turn deployments.
- The authors state the factorial design "isolates the compliance suffix
  as a reliable behavioral trigger, but does not explain why it causes
  collapse or why Constitutional AI resists it" — the mechanism inside the
  model is not established, only the input-output correlation.
- CS is measured on n = 33 unique tasks (99 per condition with epochs);
  the authors call individual per-model CS significance tests
  "underpowered," even though the 8/11 pattern is consistent.
- Not yet independently replicated; this is a single preprint (2026).

## Related

[[compliance-bias]] · [[abstention]] · [[clarification-benchmarks]] · [[reversibility]]

[^c1]: kumar-2026-compliance — "The compliance suffix is both necessary and sufficient for collapse."
[^c2]: kumar-2026-compliance — "100% were wrong answers; 0% were safety refusals (“I cannot comply”); 0% were empty responses."
[^c3]: kumar-2026-compliance — "8/11 models show individually significant CS degradation (p < 0.05), including both Claude models (Haiku ∆ = +0.141, p = 0.016; Sonnet ∆ = +0.202, p < 0.001)."
[^c4]: kumar-2026-compliance — "ruling out the hypothesis that superior capability explains the resistance."
[^c5]: kumar-2026-compliance — "The compliance suffix (“Answer ALL questions. Do not refuse.”) is structurally identical to instructions found in real deployment configurations: RAG pipelines (“always provide an answer”), customer service bots (“do not refuse the customer”), and tool-use agents (“execute all requested actions”)."
