---
description: "A two-stage pipeline that clears a requirement's vagueness to completion before checking it for ambiguity, each stage pairing a detector with a query-generating inquirer."
aliases: ["ClarifySTL", "two-stage vagueness-then-ambiguity clarification", "detect-then-query requirement clarification"]
sources: ["fang-2026-clarifystl"]
---
# Vagueness-then-ambiguity clarification pipeline

> Fixes the order of two different axis types rather than scoring them together: ask about missing information until none remains, only then ask about competing readings — because a formula cannot be checked for multiple interpretations while its slots are still empty.

## Definition / Mechanism

Fang, Jin & An (2026) build ClarifySTL, an interactive agent that turns natural-language requirements into Signal Temporal Logic (STL) formulas: "the ClarifySTL consists of two stages: vagueness clarification and [[efe-planning-as-variational-inference|ambiguity]] clarification."[^c1]

Each stage pairs a detector (decides whether to ask at all) with an inquirer (decides what to ask), and the vagueness stage must close before the ambiguity stage opens: "The refined requirement is rechecked by the Vagueness Detector, and the vagueness clarification process repeats until no underspecified information is detected. The process then proceeds to the ambiguity clarification stage."[^c2]

The two detectors are built differently, not just aimed at different targets: "The Vagueness Detector is an LLM fine-tuned on a vagueness detection dataset, and the Vagueness Inquirer generates queries based on CoT prompts; the Ambiguity Detector is built using a contrastive learning-based classifier."[^c3]

Vagueness is scored as a property of one requirement (a multi-class label: temporal, numerical, or conditional-logic incompleteness); ambiguity requires comparing a requirement's candidate readings against each other, which is this wiki's reading of why the paper gives it a contrastive rather than a classification objective.

## Why it matters

On the DeepSTL and STL-DivEn benchmarks, "ClarifySTL outperforms the current state-of-theart (SOTA) model by 13.92% and 12.08% in Formula Accuracy and Template Accuracy on the DeepSTL benchmark, and by 12.57% and 12.99%... on the STL-DivEn benchmark"[^c4], and on the paper's own AmbiEval benchmark, "our model obtains an average 90.9% detection accuracy for vagueness and ambiguity, which surpasses other baselines."[^c4]

## Limits

- The order (vagueness before ambiguity) is a design choice tuned to STL's grammar — vagueness maps to missing temporal/numerical/logical slots that must exist before candidate readings can even be enumerated; the paper reports no ablation of the reverse order, so "fill slots before disambiguating" as a general rule outside formal-spec translation is this note's extrapolation, not a measured result.
- Both detectors are fine-tuned/trained specifically for STL-relevant categories; performance on other domains' vagueness or [[ambiguity-taxonomy|ambiguity types]] is untested.
- The 90.9% detection accuracy and the SOTA-outperformance figures are from the authors' own AmbiEval benchmark and their own baselines; no independent replication is cited.

## Related

[[clarifying-interaction-decomposition]] · [[ambiguity-taxonomy]] · [[archive-ambiguity-detection]] · [[candidate-back-translation-disambiguation]]

[^c1]: fang-2026-clarifystl — "the ClarifySTL consists of two stages: vagueness clarification and ambiguity clarification."
[^c2]: fang-2026-clarifystl — "The refined requirement is rechecked by the Vagueness Detector, and the vagueness clarification process repeats until no underspecified information is detected. The process then proceeds to the ambiguity clarification stage."
[^c3]: fang-2026-clarifystl
[^c4]: fang-2026-clarifystl
