---
description: "Benchmark scoring whether an asking agent recovers hidden intent from imperfect visualization requests; the full interactive tree-search method beats the best non-interactive baseline 5x."
aliases: ["VisInteract-Bench"]
sources: ["xu-2026"]
---
# VisInteract-Bench

> Visualization requests deliberately made ambiguous, incomplete, or factually wrong, scored on whether an agent that can ask the user recovers the request's hidden true intent — not on whether it merely detects that something is wrong.

## Definition / Mechanism

Xu et al. (2026) build the benchmark from "1,098 samples across 11 databases (75 tables in total) drawn from BIRD Mini-Dev".[^c3]

Each sample pairs an imperfect query with a hidden key-feature set that only a simulated user can see, and a dual LLM judge scores a submission's code and rendered chart against every feature: key features are "only exposed to the User Agent" and provide "the criteria for automated evaluation", and "All methods are assessed by the dual-judge pipeline".[^c4]

The imperfection is injected by template, after a clean reference is already validated. In Xu et al. (2026) "An LLM rewrites the clear query by combining 1–3 of 14 [[efe-planning-as-variational-inference|ambiguity]] templates from three categories (ambiguity for multiple plausible readings, incompleteness for critical details dropped, and factual error for things like a non-existent column)," and "injection occurs after validation, so every imperfect query retains a correct executable reference" — so success is measured against the user's real, never-stated intent, not against the surface query.[^c1]

What the benchmark scores is therefore a whole ask/act sequence, not a single question: a rollout is a trajectory of up to twenty steps ("maximum trajectory depth Lmax = 20") in which several user questions can be asked, and the interactive methods are compared "Under an identical N = 10 rollout budget".[^c5]

## Why it matters

The headline finding of Xu et al. (2026) is that asking is not optional decoration: "even the stronger Self-Correction LLM trails Vis-MCTS by more than 5× on the Merge Task Score (7.38% vs. 51.46% on Qwen; 10.66% vs. 57.19% on Gemini). This large gap quantifies the Interaction Gain from dynamic intent [[recovery-postulate|recovery]], confirming that imperfect queries cannot be reliably resolved by reasoning and self-correction alone." A second, separate finding isolates how the questions are searched for: under an identical ten-rollout budget the tree-structured [[vis-mcts]] "clearly outperforms Best-of-N (ReAct) on Merge Task Score (51.46% / 57.19% vs. 38.06% / 40.92% on Qwen / Gemini, +13.40% / +16.27% improvements)" — the tree structure, not just extra sampling, is what pays off; the size of that margin is [[vis-mcts]]'s finding, not this benchmark's.[^c2]

## Limits

The 5x "Interaction Gain" compares the full method — tree search plus interaction — with the best non-interactive baseline, so it bundles the search method with interaction. The paper's own single-chain ReAct agent, interactive but without a tree, sits at Best-of-N minus the stated +9.01%/+1.30%, i.e. roughly 29%/39.6% Merge Task Score, so the interaction-only contrast against Self-Correction is nearer 4x and the remainder is search.

The benchmark's "user" is a leakage-controlled LLM/VLM simulation, not a person, over one domain (SQL-and-chart generation from the BIRD Mini-Dev corpus). Xu et al. (2026) state that "Our evaluation relies on LLM-based judges, whose [[calibration|reliability]] is bounded by the underlying model capabilities. The User Agent simulates idealized user behavior, whereas real users may provide noisier, less consistent feedback" — so the gap is a ceiling on what interaction can buy against a well-behaved answerer, not a measurement against real ones.[^c6]

Every figure here is from one paper, one benchmark and two backbones (Qwen, Gemini); nothing outside this paper has replicated them (`replicated: null`). Until the verifier confirms it, the Best-of-N half of[^c2] is unverified: its quote spans a line-hyphenated "Vis-MCTS" in the archived extract.

## Related

[[clarification-benchmarks]] · [[vis-mcts]] · [[dimension-aware-reward-decomposition]] · [[leakage-controlled-user-agent]] · [[question-budgets]]

[^c1]: xu-2026 — "An LLM rewrites the clear query by combining 1–3 of 14 ambiguity templates from three categories (ambiguity for multiple plausible readings, incompleteness for critical details dropped, and factual error for things like a non-existent column)"
[^c2]: xu-2026 — "even the stronger Self-Correction LLM trails Vis-MCTS by more than 5× on the Merge Task Score (7.38% vs. 51.46% on Qwen; 10.66% vs. 57.19% on Gemini). This large gap quantifies the Interaction Gain from dynamic intent recovery, confirming that imperfect queries cannot be reliably resolved by reasoning and self-correction alone."
[^c3]: xu-2026 — "VisInteract-Bench fills this gap with 1,098 samples across 11 databases (75 tables in total) drawn from BIRD Mini-Dev [22]."
[^c4]: xu-2026 — "Key features K serve three roles simultaneously, namely 1) defining the user’s true intent and only exposed to the User Agent, 2) specifying the targets for imperfection injection, and 3) providing the criteria for automated evaluation."
[^c5]: xu-2026 — "We use Nrollout = 10 rollouts, maximum trajectory depth Lmax = 20, and progressive-widening child cap Kmax = 3."
[^c6]: xu-2026 — "Our evaluation relies on LLM-based judges, whose reliability is bounded by the underlying model capabilities. The User Agent simulates idealized user behavior, whereas real users may provide noisier, less consistent feedback."
