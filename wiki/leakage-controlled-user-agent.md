---
description: "A simulated answerer reveals only the intent features a question's topic matches, and for visual critiques says what is wrong but never how to fix it."
aliases: ["leakage-controlled User Agent"]
sources: ["xu-2026"]
---
# Leakage-controlled user agent

> A policy for a simulated answerer that commits partially by design — revealing only the feature type a question addressed, and diagnosing without prescribing — so a benchmark's "user" cannot be interrogated into handing over its hidden ground truth.

## Definition / Mechanism

The User Agent of Xu et al. (2026) ([[visinteract-bench|VisInteract-Bench]]) knows the full hidden intent (a typed set of key features plus the ground-truth code and chart) but exposes it through two gated interfaces rather than directly: "guarding by access gating (which subset of K is visible) and a response policy (what the model may verbalize) to prevent ground-truth leakage." A textual question is first passed through a scanner that labels which feature types it concerns, and only those are ever exposed: "ask_user_text(qtext ) → atext answers a textual question after a pre-filtering step in which a scanner LLM labels which key-feature types the question pertains to, and only the matched features are exposed to the User Agent."[^c1]

The second interface, in the same paper, answers a visual question by rendering the candidate chart and comparing it to the ground truth: "ask_user_vis(c) → (s, m) executes c, shows the rendered chart alongside the ground-truth chart to a VLM, and returns feedback m on the most salient visual discrepancy which describes what is wrong, not how to fix, with a satisfaction score s ∈ [1, 10] ∩ Z, exposing only visual-dimension features." A shared policy additionally refuses to name the target directly: "a shared response policy mandates refusing any direct request for the ground-truth intent."[^c2]

## Why it matters

This gives stall 10 — how much an answerer commits, and how it says the rest — a concrete, implementable partial-disclosure policy instead of an all-or-nothing choice: gate exposure by the question's own topic, and separate diagnosis from prescription in what gets revealed. The two channels play different roles in Xu et al. (2026)'s ablation, and neither is a substitute for the other. The visual channel is what makes the search work at all: "Visual Feedback supplies the terminal reward signal, whose removal collapses UCT to blind exploration, dropping Merge Task Score by 27.22%." The textual channel is the one the paper credits with recovering intent: "Textual Interaction resolves non-visual intent ambiguities (e.g., filters, aggregations) that visual critiques cannot expose, resulting in 7.38% Merge Task Score decrease if remove it." The paper's own conclusion is that "every component plays a distinct, non-redundant role."[^c3]

## Limits

The policy is enforced by an LLM scanner and an LLM/VLM response generator, not by a hard access-control mechanism; the paper does not report how often the scanner mislabels a question's feature type and leaks past the gate, so the "leakage-controlled" guarantee is a design intention checked only by the resulting task-success numbers, not by an audited leak rate. The 27.22-point visual-channel ablation measures the loss of the search's reward signal, not the loss of intent information; whether the visual channel also recovers a part of the hidden intent that the textual channel cannot is not separated out by the paper, and this note does not claim it.

## Related

[[visinteract-bench]] · [[vis-mcts]] · [[question-budgets]] · [[conversational-maxims]]

[^c1]: xu-2026 — "guarding by access gating (which subset of K is visible) and a response policy (what the model may verbalize) to prevent ground-truth leakage."
[^c2]: xu-2026 — "ask_user_vis(c) → (s, m) executes c, shows the rendered chart alongside the ground-truth chart to a VLM, and returns feedback m on the most salient visual discrepancy which describes what is wrong, not how to fix, with a satisfaction score s ∈ [1, 10] ∩ Z, exposing only visual-dimension features."
[^c3]: xu-2026 — "Table 3 confirms every component plays a distinct, non-redundant role."
